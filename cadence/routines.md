---
file: routines.md
title: Terrible Enfant — Routines
status: active
owner: Boris
updated: 2026-06-14
---

# Routines

> El loop auto-disparado de Cadence: qué corre, cuándo, qué lee y qué escribe. El proceso humano
> completo de la cadencia semanal vive en `capabilities/workflows/WF_OPS_WEEKLY.md`.

| Routine | Cadencia | Trigger | Lee → Escribe | WAT |
|---|---|---|---|---|
| RT-001 · Status update | Lunes < 18:00 | manual (líderes de área) | — → `cadence/operations/[mercado]/[área]/STATUS.md` | — |
| RT-002 · Compilar semanal | Lunes PM | manual (Boris) | `cadence/operations/**` + `cadence/projects/active/**` → `cadence/weekly/2026/W##-YYYY-MM-DD.md` | `WF_OPS_COMPILE`, `WF_PROJ_COMPILE` |
| RT-003 · Agenda del martes | Martes AM | manual (Boris) | reporte semanal → agenda al equipo | `WF_OPS_AGENDA` |
| RT-004 · Log de decisiones | Martes PM | manual (Boris/Fanny) | notas de reunión → `cadence/decision_log.md` (append-only) | `WF_OPS_DECISIONS` |
| RT-005 · Pulse | inicio/cierre de sesión + mensual | manual (Boris) | estado del OS → `cadence/pulse.md` | `AG_CORE_PULSE` |
| RT-006 · CMO quarterly brief | 1ª semana de trimestre | on-demand (Boris) | GTM + funnel → `cadence/projects/active/gtm-sao-paulo/cmo-brief-Q#-YYYY.md` | `WF_MKT_CMO` |
| RT-007 · Minado de reuniones | por reunión / on-demand | **event** (commit en `transcripts/**.md`) + manual (`workflow_dispatch`) | `transcripts/**.md` + `config/te-mining.json` → `cadence/meetings/` + Asana + email recap | `WF_OPS_MINE`, `AG_OPS_MINER` |

> **Estado de automatización:** RT-001…RT-006 son **V1 — manuales** (Boris las dispara vía Claude
> Code). **RT-007 es la primera rutina automatizada del OS** — corre en **GitHub Actions** (pure-GHA,
> sin n8n; ver `connections/TL_OPS_MINER.md`), disparada por el commit del transcript. Fase n8n
> (V2/V3) sigue sin activar. Principio: automatizar **después** de validar el flujo manual — RT-007
> arranca en V1 con trigger manual (`workflow_dispatch`) para validar la calidad del minado antes de
> sumar el webhook de Read AI.
