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

> **Estado de automatización:** todas las rutinas son **V1 — manuales** (Boris las dispara vía
> Claude Code). La fase n8n (V2/V3) no está activa — ver `connections/TL_CORE_N8N.md`. Principio:
> automatizar **después** de validar el flujo manual.
