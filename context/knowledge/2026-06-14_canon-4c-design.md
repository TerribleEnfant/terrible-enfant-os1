---
file: 2026-06-14_canon-4c-design.md
title: Canon 4C Migration · Stage 2 Design — move-map + WAT
status: archived
owner: Boris
updated: 2026-06-14
---

# Design · Terrible Enfant OS

> Stage 2 del `WF_CANON_DEPLOY`. Mapa current → 4C, AREA tokens, WAT renaming. Firmado por Boris
> el 2026-06-14 (decisiones gating: OPERATIONS+PROJECTS → cadence/; principal = Boris con
> escalación dividida).

## AREA tokens (decididos)
**CORE / OPS / PROJ / MKT** — cuatro tokens funcionales, espejando la altitud de COMANDO.
- **CORE** — orquestación, gobierno, plataforma/infra.
- **OPS** — ritmo operacional semanal permanente (6 áreas × 2 mercados).
- **PROJ** — iniciativas time-bounded (campañas, collabs, lanzamientos).
- **MKT** — marketing / GTM / growth / content.

**Rechazados:** geográfico `ARG`/`BRA` (mercado = sub-dimensión de contenido, no función);
`BRAND` (DNA de marca = prosa de Context, sin WAT que necesite el token); `AUTO` (infra de
automatización pliega en CORE).

## Move-map (resumen — todo vía `git mv`, historia preservada)
- **Context:** `CORE/*`→`context/identity/`; `STRATEGY/*`→`context/strategy/`; `REFERENCE/*`→`context/knowledge/`.
- **Connections (TL_*):** github→`TL_CORE_GITHUB`, google-drive→`TL_CORE_GDRIVE`,
  whatsapp→`TL_CORE_WHATSAPP`, n8n→`TL_CORE_N8N`, asana→`TL_OPS_ASANA`, nuvemshop→`TL_OPS_NUVEMSHOP`,
  meta-ads→`TL_MKT_METAADS`; `_tools-index.md`→`connections/README.md`; asana-board-guidelines→companion.
- **Capabilities (AG_*/WF_*):** weekly-compiler→`AG_OPS_COMPILER`, agenda-drafter→`AG_OPS_AGENDA`,
  decision-logger→`AG_OPS_DECISIONS`, project-status-roller→`AG_PROJ_STATUS`,
  pulse-strategist→`AG_CORE_PULSE`, cmo-strategist→`AG_MKT_CMO`; weekly-rhythm→`WF_OPS_WEEKLY`,
  new-project-setup→`WF_PROJ_SETUP`, project-close→`WF_PROJ_CLOSE`, collab-launch→`WF_PROJ_COLLAB`,
  compile-weekly→`WF_OPS_COMPILE`, compile-project→`WF_PROJ_COMPILE`, draft-agenda→`WF_OPS_AGENDA`,
  generate-decision-log→`WF_OPS_DECISIONS`, cmo-quarterly-brief→`WF_MKT_CMO`.
- **Cadence:** pulse→`cadence/pulse.md`; weekly-decisions-log→`cadence/decision_log.md`;
  automation-log→`cadence/automation-log.md`; boris-playbook→`cadence/runbook.md`;
  project-touchpoints→`cadence/project-touchpoints.md`; `OPERATIONS/{ARG,BRA}`→`cadence/operations/`;
  `PROJECTS/*`→`cadence/projects/`; `WEEKLY/*`→`cadence/weekly/`.

## Nuevos artefactos (autorados, no movidos)
`TE-OS_M1.md` (boot spec) · `CLAUDE.md` adelgazado · `AG_CORE_COMANDER.md` ·
`capabilities/skills/REGISTRY.md` · `cadence/routines.md` · `context/knowledge/INDEX.md` +
estos dos docs de migración.

## Decisiones de sign-off (Boris, 2026-06-14)
1. **OPERATIONS + PROJECTS → `cadence/`** (estado vivo que el loop semanal lee/escribe). ✔
2. **Principal = Boris**; escalación dividida preservada (marca→Comando, finanzas/producto→Hache). ✔
3. Placements menores aceptados (asana-guidelines→connections; meeting-template→workflows; product-catalog→identity).

## Pendientes post-migración (no bloqueantes)
- Wirear referencias 1Password/`op` en los `TL_*` (hoy stubs `TODO: vault ref`).
- Escribir el prompt/WF de `AG_CORE_PULSE` (gap pre-existente).
- Cards de Connections para Instagram/TikTok (listados, sin card).
- Revisar cross-refs de prosa internos que aún apunten a rutas viejas (boot path ya corregido).
