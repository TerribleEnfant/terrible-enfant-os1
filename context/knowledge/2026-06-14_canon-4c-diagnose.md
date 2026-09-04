---
file: 2026-06-14_canon-4c-diagnose.md
title: Canon 4C Migration · Stage 1 Diagnose — gap map
status: archived
owner: Boris
updated: 2026-06-14
---

# Diagnose · Terrible Enfant OS

> Stage 1 del `WF_CANON_DEPLOY` adaptado a refactor in-place. Auditoría de TE-OS contra 4C.
> TE-OS ya era una NLAH madura — el contenido estaba casi todo presente; los gaps eran
> estructurales (sin spine 4C) + algunos artefactos faltantes.

## Context (estático — quién es TE)
- **Identidad:** presente — `CORE/` (brand-bible, brand-narrative, org/team-structure, product-catalog).
- **Estrategia:** presente — `STRATEGY/` (brazil-launch, estado-de-gracia, market-expansion).
- **Conocimiento:** presente — `REFERENCE/` (legacy, notion, diagramas).
- **Gap:** disperso en 3 carpetas top-level; sin `context/` spine; sin INDEX de knowledge.

## Connections (vivo — data real)
- 7 tools documentados como prosa: github, asana, google-drive, whatsapp, meta-ads, nuvemshop, n8n.
- **Gap:** sin nombres `TL_*`; sin referencias de auth 1Password/`op`; IG/TikTok listados pero sin card.

## Capabilities (qué puede hacer hoy)
- 6 agents, 4 workflows (+template), 5 prompts, comando `.claude/commands/upc.md`.
- **Gap:** sin nombres `AG_*`/`WF_*`; sin framing NLAH (Role/Stage/Contract); **sin AG_CORE_COMANDER**
  (rol implícito solo en CLAUDE.md); sin `skills/REGISTRY.md`; `pulse-strategist` sin prompt/WF.

## Cadence (qué corre solo / estado vivo)
- `OPERATIONS/_GLOBAL/pulse.md`, `weekly-decisions-log.md`, `AUTOMATION/logs/automation-log.md`,
  `boris-playbook.md`, `OPERATIONS/ARG|BRA/` (6 áreas × STATUS+kpis), `PROJECTS/`, `WEEKLY/`.
- **Gap:** sin `cadence/` spine; pulse/decision-log/logs no co-locados; sin `routines.md`; sin boot spec.

## Charter / OS-layer split
- `CLAUDE.md` cargaba a la vez política de runtime + arquitectura completa.
- **Gap:** sin boot spec (`TE-OS_M1.md`); Charter no adelgazado a puntero.

## Summary gap map (ranked)
1. Sin spine 4C — contenido en CORE/STRATEGY/REFERENCE/OPERATIONS/PROJECTS/AUTOMATION.
2. Sin boot spec; `CLAUDE.md` mezcla Charter + OS layer.
3. WAT sin nombrar (`AG_/WF_/TL_`), sin framing NLAH.
4. Falta `AG_CORE_COMANDER` y `skills/REGISTRY.md`.
5. Connections sin auth-of-record (1Password).
