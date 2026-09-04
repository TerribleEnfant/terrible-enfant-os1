# GTM — Go to Market São Paulo

**Tipo:** launch (capa estratégica / umbrella GTM)
**Estado:** active
**Inicio:** junio 2026
**Fecha límite / evento:** launch São Paulo — **julio 2026** (⚠️ conflicto de fecha con `brazil-launch`, ver dashboard)
**Owner:** Boris (arquitectura GTM) + Comando (creativo) + Freequency (ejecución BR)
**Mercado:** BRA (con tronco global compartido ARG+BR)
**Resumen:** Capa estratégica de go-to-market para São Paulo. Define la arquitectura de funnel (Funnel Y), el mapa de canales con owners, el calendario de collabs, los gaps bloqueantes del launch y el stack de IA/automatización que sostiene la operación. No reemplaza a `brazil-launch` — es la capa de dirección que lo orienta.

---

## Por qué este proyecto existe

`cadence/projects/active/brazil-launch/` traquea la **ejecución operacional** del lanzamiento (canales de venta, contratos, product mix). Pero faltaba una **capa de dirección de marketing**: cómo se conectan awareness global y conversión local, quién es dueño de cada canal, dónde están los huecos del embudo, y qué se automatiza con IA.

Este proyecto es esa capa. Es el documento que se abre en una reunión para responder *"¿dónde estamos en el go-to-market de SP y qué nos está frenando?"*.

## Relación con otros proyectos

| Proyecto | Relación |
|----------|----------|
| `brazil-launch` | Ejecución operacional del launch. GTM lo orienta, no lo duplica. |
| `estado-de-gracia` | Campaña de marca activa — provee el concepto narrativo del tronco global. |
| `collab-*` (notthesamo, edgar, selo-risco, normando, barra-crew, dendezeiro) | Activaciones culturales BR = nodos MOFU/TOFU del funnel. |

## Objetivo

Tener una sola superficie viva que responda, en cualquier momento:
1. Cómo se mueve un comprador desde "no conoce la marca" hasta "compró y vuelve", en ARG y en BR.
2. Quién es dueño de cada canal y en qué estado está.
3. Qué gaps bloquean el launch de julio (P1) y qué decisiones están abiertas (P2/P3).
4. Qué parte de esto se automatiza con IA y en qué fase.

## Entregables clave

- [x] `gtm-dashboard.md` — status / dashboard / explainer (v0.1)
- [x] `funnel-architecture.md` — Funnel Y documentado
- [x] `channels.md` — mapa de canales con owner + estado + etapa
- [x] `collabs-calendar.md` — calendario de collabs BR 2026
- [x] `ai-stack.md` — stack de IA + fases de automatización
- [x] `kpis.md` — scaffold de KPIs por etapa de funnel y mercado
- [ ] Resolver conflictos de datos con el repo (fechas, calendario de collabs) — ver dashboard §Conflictos
- [ ] (Fase 2 opcional) Dashboard React interactivo

## Criterios de éxito

- El equipo puede leer el dashboard en 5 min y saber dónde está el GTM.
- Cada canal tiene owner explícito (cero "sin asignar" silenciosos).
- Los 4 gaps P1 tienen dueño y próximo paso antes del launch de julio.

## Dependencias operacionales

- `cadence/operations/BRA/marketing-comms/` — Freequency + Comando ejecutan TOFU/MOFU BR
- `cadence/operations/BRA/operations/` — contratos showroom + MataLab
- `cadence/operations/BRA/legal-contable/` — estudio local (bloqueador heredado de brazil-launch)

## Links externos

- Ejecución operacional: `cadence/projects/active/brazil-launch/`
- Estrategia directional: `context/strategy/market-expansion-roadmap.md` · `context/strategy/brazil-launch-strategy.md`
- Agente de dirección: `capabilities/agents/AG_MKT_CMO.md`
- Drive:
- Asana:
