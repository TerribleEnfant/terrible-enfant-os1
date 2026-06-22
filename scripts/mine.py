#!/usr/bin/env python3
"""TE meeting auto-miner — quality gate -> one Claude tool-use call -> machine store.

Pure stdlib + `anthropic`. Fails LOUD on any error (non-zero exit + GitHub job summary).
Output is the machine store under cadence/meetings/ — it NEVER touches cadence/decision_log.md.

Usage:
    python scripts/mine.py <path-to-transcript.md> [--force]

Reference pattern (pure-GHA miner) adapted for TE-OS / COMANDO. TE-native; no BOTH coupling.
"""
import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO / "config" / "te-mining.json"
PROMPT_PATH = REPO / "scripts" / "prompts" / "mine-prompt.md"
OUT_DIR = REPO / "cadence" / "meetings"

# --- speaker-attribution heuristics for the quality gate -------------------
NAME = r"[A-Za-zÀ-ÿ0-9'.\- ]{1,40}"
ATTRIBUTION_PATTERNS = [
    re.compile(rf"^\s*{NAME}:\s"),                       # "Fanny: ..."
    re.compile(rf"^\s*\[?\d{{1,2}}:\d{{2}}(:\d{{2}})?\]?\s+{NAME}"),  # "[00:01] Fanny ..."
    re.compile(rf"^\s*{NAME}\s+\d{{1,2}}:\d{{2}}"),      # "Fanny 00:01" (Read AI style)
]


def die(msg: str, summary_lines=None):
    """Fail loud: write a job summary, print to stderr, exit non-zero."""
    write_summary(["## ❌ Mining FAILED", "", msg] + (summary_lines or []))
    print(f"MINE ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def write_summary(lines):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    text = "\n".join(lines) + "\n"
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(text)
    print(text)


def slugify(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[àáâã]", "a", text)
    text = re.sub(r"[éê]", "e", text)
    text = re.sub(r"[íî]", "i", text)
    text = re.sub(r"[óôõ]", "o", text)
    text = re.sub(r"[úû]", "u", text)
    text = re.sub(r"ñ", "n", text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:60] or "reunion"


def content_lines(text: str):
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith("---") or s.startswith(">"):
            continue
        out.append(ln)
    return out


def quality_gate(text: str, max_ratio: float):
    lines = content_lines(text)
    if not lines:
        return 1.0, 0, 0, False
    attributed = sum(1 for ln in lines if any(p.search(ln) for p in ATTRIBUTION_PATTERNS))
    unattributed = len(lines) - attributed
    ratio = unattributed / len(lines)
    return ratio, unattributed, len(lines), ratio <= max_ratio


# --- structured-output schema (forced tool call) ---------------------------
def build_tool():
    item_common = {
        "source_quote": {"type": "string", "description": "Cita textual y literal de una línea del transcript. Obligatoria."},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    }
    return {
        "name": "record_mining",
        "description": "Registra decisiones, riesgos y action items extraídos del transcript.",
        "input_schema": {
            "type": "object",
            "properties": {
                "meeting": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string", "description": "YYYY-MM-DD"},
                        "title": {"type": "string"},
                        "attendees": {
                            "type": "array",
                            "items": {"type": "object", "properties": {
                                "name": {"type": "string"},
                                "email": {"type": "string"},
                            }, "required": ["name"]},
                        },
                    },
                    "required": ["title", "attendees"],
                },
                "decisions": {"type": "array", "items": {"type": "object", "properties": dict(
                    summary={"type": "string"}, area={"type": "string"}, market={"type": "string"},
                    owner={"type": "string"}, **item_common),
                    "required": ["summary", "source_quote", "confidence"]}},
                "risks": {"type": "array", "items": {"type": "object", "properties": dict(
                    summary={"type": "string"}, area={"type": "string"}, market={"type": "string"},
                    venture={"type": "string"}, **item_common),
                    "required": ["summary", "source_quote", "confidence"]}},
                "action_items": {"type": "array", "items": {"type": "object", "properties": dict(
                    title={"type": "string"}, owner={"type": "string"}, deliverable={"type": "string"},
                    deadline={"type": "string"}, area={"type": "string"}, market={"type": "string"},
                    **item_common),
                    "required": ["title", "source_quote", "confidence"]}},
            },
            "required": ["meeting", "decisions", "risks", "action_items"],
        },
    }


def call_claude(transcript: str, config: dict, model: str) -> dict:
    try:
        import anthropic
    except ImportError:
        die("Falta el paquete `anthropic`. `pip install anthropic`.")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        die("ANTHROPIC_API_KEY no está seteado.")

    prompt = PROMPT_PATH.read_text(encoding="utf-8")
    cfg_block = json.dumps({k: config[k] for k in ("markets", "areas", "projects", "people")
                            if k in config}, ensure_ascii=False, indent=2)
    tool = build_tool()
    client = anthropic.Anthropic()
    try:
        resp = client.messages.create(
            model=model,
            max_tokens=4096,
            system=prompt,
            tools=[tool],
            tool_choice={"type": "tool", "name": "record_mining"},
            messages=[{"role": "user", "content":
                       f"CONFIG:\n{cfg_block}\n\n=== TRANSCRIPT ===\n{transcript}"}],
        )
    except Exception as e:  # noqa: BLE001 — fail loud, no swallow
        die(f"La llamada a Claude falló: {e}")

    for block in resp.content:
        if getattr(block, "type", None) == "tool_use" and block.name == "record_mining":
            return block.input
    die("Claude no devolvió la tool call `record_mining`.")


# --- validation: enforce the extraction rules in code ----------------------
def validate(data: dict, config: dict):
    ex = config.get("extraction", {})
    cap = ex.get("max_items_per_meeting", 7)
    require_quote = ex.get("require_source_quote", True)

    def clean(items):
        if require_quote:
            items = [it for it in items if (it.get("source_quote") or "").strip()]
        return items[:cap]

    data["decisions"] = clean(data.get("decisions", []))
    data["risks"] = clean(data.get("risks", []))
    data["action_items"] = clean(data.get("action_items", []))
    return data


# --- output -----------------------------------------------------------------
def confidence_badge(c):
    return {"high": "🟢 high", "medium": "🟡 medium", "low": "🔴 low"}.get(c, c or "?")


def render_recap(data, base):
    m = data.get("meeting", {})
    out = [f"# Recap · {m.get('title', base)}", "",
           f"**Fecha:** {m.get('date', '—')}  ",
           f"**Archivo:** `{base}`  ",
           f"**Participantes:** " + ", ".join(a.get("name", "?") for a in m.get("attendees", [])) or "—",
           "",
           "> Generado por el auto-miner (`WF_OPS_MINE`). Machine store — **no es** el "
           "`decision_log.md` (ese es humano, append-only). Cada ítem lleva cita textual + confianza.",
           ""]

    def section(title, items, fmt):
        out.append(f"## {title} ({len(items)})")
        if not items:
            out.append("\n_(ninguno)_\n")
            return
        for i, it in enumerate(items, 1):
            out.append(fmt(i, it))
        out.append("")

    section("Decisiones", data["decisions"], lambda i, it:
            f"\n### D{i}. {it.get('summary','')}\n"
            f"- Área: {it.get('area','—')} · Mercado: {it.get('market','—')} · "
            f"Owner: {it.get('owner','—')} · {confidence_badge(it.get('confidence'))}\n"
            f"> {it.get('source_quote','')}")
    section("Riesgos", data["risks"], lambda i, it:
            f"\n### R{i}. {it.get('summary','')}\n"
            f"- Área: {it.get('area','—')} · Mercado: {it.get('market','—')} · "
            f"Venture: {it.get('venture','—')} · {confidence_badge(it.get('confidence'))}\n"
            f"> {it.get('source_quote','')}")
    section("Action items", data["action_items"], lambda i, it:
            f"\n### A{i}. {it.get('title','')}\n"
            f"- Owner: {it.get('owner','—')} · Deliverable: {it.get('deliverable','—')} · "
            f"Deadline: {it.get('deadline','—')}\n"
            f"- Área: {it.get('area','—')} · Mercado: {it.get('market','—')} · "
            f"{confidence_badge(it.get('confidence'))}\n"
            f"> {it.get('source_quote','')}")
    return "\n".join(out) + "\n"


def per_item_file(kind, idx, it):
    head = it.get("summary") or it.get("title") or kind
    lines = [f"# {kind.capitalize()}: {head}", ""]
    for k, v in it.items():
        if k == "source_quote":
            continue
        lines.append(f"- **{k}:** {v}")
    lines += ["", f"> {it.get('source_quote','')}", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--force", action="store_true", help="saltea el quality gate (queda logueado)")
    args = ap.parse_args()

    tpath = Path(args.transcript)
    if not tpath.is_file():
        die(f"Transcript no encontrado: {tpath}")
    transcript = tpath.read_text(encoding="utf-8")

    if not CONFIG_PATH.is_file():
        die(f"Config no encontrado: {CONFIG_PATH}")
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    model = os.environ.get("MINER_MODEL", config.get("model", "claude-opus-4-8"))
    max_ratio = config.get("quality_gate", {}).get("max_unattributed_ratio", 0.5)

    ratio, unattr, total, ok = quality_gate(transcript, max_ratio)
    gate_msg = f"Quality gate: {unattr}/{total} líneas sin atribuir ({ratio:.0%}); límite {max_ratio:.0%}."
    if not ok and not args.force:
        die("Transcript de baja calidad — minar fabricaría contenido. " + gate_msg +
            " Corregí el transcript o re-corré con --force si estás seguro.")
    if not ok and args.force:
        write_summary([f"⚠️ Quality gate SALTEADO con --force. {gate_msg}"])

    data = validate(call_claude(transcript, config, model), config)

    m = data.setdefault("meeting", {})
    mdate = m.get("date") or _date_from_name(tpath) or date.today().isoformat()
    m["date"] = mdate
    base = f"{mdate}-{slugify(m.get('title') or tpath.stem)}"

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "decisions").mkdir(exist_ok=True)
    (OUT_DIR / "risks").mkdir(exist_ok=True)

    data["_meta"] = {"source_transcript": str(tpath.relative_to(REPO)), "model": model,
                     "mined_at": datetime.utcnow().isoformat() + "Z", "base": base}
    (OUT_DIR / f"{base}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / f"{base}.md").write_text(render_recap(data, base), encoding="utf-8")
    for i, it in enumerate(data["decisions"], 1):
        (OUT_DIR / "decisions" / f"{base}-{i}.md").write_text(per_item_file("decision", i, it), encoding="utf-8")
    for i, it in enumerate(data["risks"], 1):
        (OUT_DIR / "risks" / f"{base}-{i}.md").write_text(per_item_file("risk", i, it), encoding="utf-8")

    write_summary([
        "## ✅ Mining OK", "",
        f"- **Reunión:** {m.get('title','?')} ({mdate})",
        f"- **Base:** `{base}`",
        f"- **Decisiones:** {len(data['decisions'])} · **Riesgos:** {len(data['risks'])} · "
        f"**Action items:** {len(data['action_items'])}",
        f"- {gate_msg}",
    ])
    # hand the base off to later workflow steps
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as fh:
            fh.write(f"base={base}\n")
    print(base)


def _date_from_name(p: Path):
    mtch = re.match(r"(\d{4}-\d{2}-\d{2})", p.stem)
    return mtch.group(1) if mtch else None


if __name__ == "__main__":
    main()
