#!/usr/bin/env python3
"""Email the mined recap to INTERNAL call participants only. Fails loud on send error.

Recipients = (Read AI attendee emails) ∩ (config internal allowlist: domain OR explicit email).
External guests are dropped. If no internal recipient remains, it skips (not an error).
Set SKIP_EMAIL=1 to no-op. Sends via Resend (TE_RESEND_API_KEY).

Usage:
    python scripts/send_recap.py cadence/meetings/<base>.json
"""
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG = json.loads((REPO / "config" / "te-mining.json").read_text(encoding="utf-8"))


def die(msg):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        open(path, "a", encoding="utf-8").write(f"## ❌ Recap email FAILED\n\n{msg}\n")
    print(f"EMAIL ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def summary(lines):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    text = "\n".join(lines) + "\n"
    if path:
        open(path, "a", encoding="utf-8").write(text)
    print(text)


def is_internal(email, email_cfg):
    email = (email or "").strip().lower()
    if not email or "@" not in email:
        return False
    if email in {e.lower() for e in email_cfg.get("internal_allowlist_emails", [])}:
        return True
    domain = email.split("@", 1)[1]
    domains = [d.lower() for d in email_cfg.get("internal_allowlist_domains", []) if "TODO" not in d]
    return domain in domains


def main():
    if len(sys.argv) < 2:
        die("Falta el path al JSON minado.")
    if os.environ.get("SKIP_EMAIL"):
        summary(["## ⏭️ Recap email salteado (SKIP_EMAIL)"])
        return

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    base = data.get("_meta", {}).get("base", "")
    md_path = REPO / "cadence" / "meetings" / f"{base}.md"
    body = md_path.read_text(encoding="utf-8") if md_path.is_file() else "(recap no encontrado)"
    m = data.get("meeting", {})

    email_cfg = CONFIG.get("email", {})
    recipients = sorted({a["email"].strip().lower() for a in m.get("attendees", [])
                         if a.get("email") and is_internal(a["email"], email_cfg)})

    if not recipients:
        summary(["## ⏭️ Recap email omitido", "",
                 "No quedó ningún participante interno (allowlist) en la lista de asistentes."])
        return

    token = os.environ.get("TE_RESEND_API_KEY")
    if not token:
        die("TE_RESEND_API_KEY no está seteado.")
    sender = email_cfg.get("from", "")
    if "TODO" in sender:
        die("config email.from todavía es TODO — configurá el dominio sender (DKIM) en Resend.")

    payload = {
        "from": sender,
        "to": recipients,
        "subject": f"Recap · {m.get('title', base)} ({m.get('date', '')})",
        "text": body,
    }
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=json.dumps(payload).encode(), method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        die(f"Resend → HTTP {e.code}: {e.read().decode()[:500]}")
    except urllib.error.URLError as e:
        die(f"Resend → {e}")

    summary(["## ✅ Recap email enviado", "",
             f"- **Para ({len(recipients)}):** " + ", ".join(recipients)])


if __name__ == "__main__":
    main()
