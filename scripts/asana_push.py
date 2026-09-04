#!/usr/bin/env python3
"""Push mined action items to the live Asana board — deduped by name. Fails loud.

Governance: this is the ONLY automated process authorized to create Asana tasks (TE-OS M2
amendment, approved by Boris + Fanny). Only complete (owner + deliverable + deadline) action items
with confidence >= the config threshold are pushed. Set SKIP_ASANA=1 to no-op.

Usage:
    python scripts/asana_push.py cadence/meetings/<base>.json
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG = json.loads((REPO / "config" / "te-mining.json").read_text(encoding="utf-8"))
API = "https://app.asana.com/api/1.0"
CONF_RANK = {"low": 0, "medium": 1, "high": 2}


def die(msg):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        open(path, "a", encoding="utf-8").write(f"## ❌ Asana push FAILED\n\n{msg}\n")
    print(f"ASANA ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def summary(lines):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    text = "\n".join(lines) + "\n"
    if path:
        open(path, "a", encoding="utf-8").write(text)
    print(text)


def api(method, path, token, payload=None):
    url = f"{API}{path}"
    data = json.dumps({"data": payload}).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json",
        "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        die(f"{method} {path} → HTTP {e.code}: {e.read().decode()[:500]}")
    except urllib.error.URLError as e:
        die(f"{method} {path} → {e}")


def norm(name):
    return re.sub(r"\s+", " ", (name or "").strip().lower())


def is_complete(it):
    return all((it.get(k) or "").strip() for k in ("owner", "deliverable", "deadline"))


def existing_names(token, project_gid):
    seen, offset = set(), None
    while True:
        q = f"/projects/{project_gid}/tasks?opt_fields=name&limit=100"
        if offset:
            q += f"&offset={offset}"
        res = api("GET", q, token)
        for t in res.get("data", []):
            seen.add(norm(t.get("name")))
        offset = (res.get("next_page") or {}).get("offset")
        if not offset:
            return seen


def main():
    if len(sys.argv) < 2:
        die("Falta el path al JSON minado.")
    if os.environ.get("SKIP_ASANA"):
        summary(["## ⏭️ Asana push salteado (SKIP_ASANA)"])
        return
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    token = os.environ.get("TE_ASANA_TOKEN")
    if not token:
        die("TE_ASANA_TOKEN no está seteado (token con scope de escritura).")

    asana = CONFIG["asana"]
    project_gid, section_gid = asana["project_gid"], asana.get("section_gid")
    min_conf = CONF_RANK.get(CONFIG.get("extraction", {}).get("asana_min_confidence", "medium"), 1)
    people = CONFIG.get("people", {})
    recap = data.get("_meta", {}).get("base", "")

    candidates, skipped = [], []
    for it in data.get("action_items", []):
        if CONF_RANK.get(it.get("confidence"), 0) < min_conf:
            skipped.append((it.get("title"), "low confidence")); continue
        if not is_complete(it):
            skipped.append((it.get("title"), "incompleto (falta owner/deliverable/deadline)")); continue
        candidates.append(it)

    existing = existing_names(token, project_gid)
    created, deduped = [], []
    for it in candidates:
        if norm(it["title"]) in existing:
            deduped.append(it["title"]); continue
        notes = (f"{it.get('deliverable','')}\n\n"
                 f"Área: {it.get('area','—')} · Mercado: {it.get('market','—')}\n"
                 f"Confianza: {it.get('confidence','?')}\n"
                 f"Cita: \"{it.get('source_quote','')}\"\n\n"
                 f"— auto-generado por WF_OPS_MINE desde cadence/meetings/{recap}.md")
        payload = {"name": it["title"], "notes": notes, "projects": [project_gid]}
        owner_gid = (people.get(it.get("owner", ""), {}) or {}).get("asana_gid")
        if owner_gid:
            payload["assignee"] = owner_gid
        if re.match(r"^\d{4}-\d{2}-\d{2}$", it.get("deadline", "")):
            payload["due_on"] = it["deadline"]
        task = api("POST", "/tasks", token, payload).get("data", {})
        if section_gid and task.get("gid"):
            api("POST", f"/sections/{section_gid}/addTask", token, {"task": task["gid"]})
        existing.add(norm(it["title"]))
        created.append(it["title"])

    lines = ["## ✅ Asana push OK", "",
             f"- **Creadas:** {len(created)}", f"- **Dedup (ya existían):** {len(deduped)}",
             f"- **Descartadas:** {len(skipped)}"]
    for t in created:
        lines.append(f"  - ✅ {t}")
    for t, why in skipped:
        lines.append(f"  - ⏭️ {t} — {why}")
    summary(lines)


if __name__ == "__main__":
    main()
