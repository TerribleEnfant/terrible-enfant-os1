# Herramienta: Auto-Miner de reuniones (Read AI → GitHub Actions)

**Owner:** Boris
**Propósito:** convertir llamadas online en conocimiento durable — archivar transcript, minar
decisiones/riesgos/tareas, crear tareas en Asana y emailear el recap a participantes internos.
**Status:** activo (V1 — trigger manual) · webhook + audio en fase 2

---

## Arquitectura — pure GitHub Actions

Sin servidor, sin Cloudflare Worker, sin n8n (V1). El transcript en git es el trigger y el archivo.

```
commit transcripts/**.md  (git push → on:push)   ← o workflow_dispatch (force-mine / backfill)
        ▼  GitHub Action `mine-meeting` (.github/workflows/mine.yml)
  1. quality gate   — si >50% de líneas sin atribuir → falla fuerte, no mina
  2. un call a Claude (structured output / tool-use `record_mining`) — no regex
  3. escribe machine store en cadence/meetings/  (recap + .json + decisiones/risks por ítem)
  4. commitea el resultado de vuelta al repo
  5. crea tareas en Asana (board live, dedup por nombre)        → scripts/asana_push.py
  6. emailea el recap a participantes internos (∩ allowlist)    → scripts/send_recap.py
        ▼  rojo + logs + job summary ante cualquier fallo (outcome binario)
```

## Reglas de seguridad (cada una pagada en un incidente real)

- **Structured output** vía tool-use validado, nunca regex sobre markdown.
- **Quality gate** antes de minar (un transcript corrupto hace fabricar contenido).
- Cada ítem lleva **`source_quote`** (cita textual) + **`confidence`**. Sin cita → se descarta.
- Action item = **owner + deliverable + deadline/trigger** (los 3 o no es action item); fusión por
  owner+resultado; cap ~7/meeting; riesgo solo para entidad que ya existe en config.
- **Fail loud / binario:** cualquier error → exit ≠ 0 + job summary. Nada de try/catch que traga.
- **Idempotente:** nombres `<YYYY-MM-DD>-<slug>`; re-correr sobrescribe, no duplica (Asana dedup por nombre).
- **Modelo fuerte** (Opus 4.8 default). Nada de Haiku.

## Archivos

| Pieza | Path |
|---|---|
| Workflow | `.github/workflows/mine.yml` |
| Minado (gate + Claude + store) | `scripts/mine.py` |
| Push a Asana | `scripts/asana_push.py` |
| Email recap | `scripts/send_recap.py` |
| Prompt de extracción | `scripts/prompts/mine-prompt.md` |
| Config TE-nativo | `config/te-mining.json` |
| Trigger / archivo | `transcripts/**.md` |
| Output (machine store) | `cadence/meetings/` |
| Cards WAT | `capabilities/agents/AG_OPS_MINER.md` · `capabilities/workflows/WF_OPS_MINE.md` |

## Gobierno

El miner es el **único proceso automatizado autorizado a crear tareas en Asana** (amendment M2,
aprobada por Boris + Fanny — ver `TE-OS_M1.md §11/§13`) y a enviar recaps por email a
participantes **internos**. **Nunca** escribe en `cadence/decision_log.md`.

## Procedencia

Patrón adaptado de un miner pure-GHA de otro repo. **TE es COMANDO / Terrible Enfant — no "BOTH
ventures".** Naming, secrets y config son TE-nativos; cero acople.

## Fases

- **V1 (activo):** trigger manual — commit de transcript + `workflow_dispatch`. Validar calidad en reuniones reales.
- **V2:** relay de webhook de Read AI (Worker mínimo ~30 líneas: HMAC + `repository_dispatch`; el Action hace todo lo pesado) + force-mine de audio (transcripción Whisper/Deepgram).

## Prerequisitos pendientes

- Confirmar que Read AI expone webhook/API y en qué plan (gate de V2). Si no, usar export por email de Read AI.
- Asana: token con scope de escritura; mapa people→assignee GID; confirmar `section_gid` destino.
- Email: dominio sender + DKIM en Resend.

---

## Auth (1Password)

> Convención del Canon: los secretos nunca van al repo. 1Password es el vault de record;
> se inyectan en runtime vía `op`. Documentar acá solo el **nombre del item**, nunca el valor.

Los scripts corren en GitHub Actions; los secretos van como **GitHub Actions secrets** (espejo del
item de 1Password). Documentar acá solo el nombre del item:

- **`ANTHROPIC_API_KEY`** — vault item: `TODO: vault ref`
- **`TE_ASANA_TOKEN`** (scope escritura) — vault item: `TODO: vault ref`
- **`TE_RESEND_API_KEY`** — vault item: `TODO: vault ref`
