---
file: TE-OS_M1.md
title: Terrible Enfant Operating System — Mark II (4C harness)
status: active
owner: Boris
updated: 2026-06-20
---

# TE-OS_M1
**Terrible Enfant Operating System — Mark I**

> El **boot spec**. El primer archivo que Comander lee después del Charter (`CLAUDE.md`).
> Este es el **OS layer** — la harness logic. Léelo completo antes de ejecutar cualquier tarea.

---

## 0 · QUÉ ES ESTE ARCHIVO

`TE-OS_M1.md` es el **spec de OS-layer** del sistema operativo de Terrible Enfant: qué es la
marca, cómo está estructurado el equipo, quién es **Comander**, cómo se rutea el trabajo, y
dónde vive todo bajo el modelo **4C**.

Se alcanza vía el **Charter** (`CLAUDE.md`, auto-cargado por Claude Code), que apunta aquí.
Charter = el runtime sobre el que corrés; este spec = la lógica que corrés. (Ver §4.)

Vivo pero no casual. Versionado por **Mark** (M1 → M2 → …); cualquier cosa más allá de un typo
gana un nuevo Mark + fila de changelog. Mark actual: **M2**.

> El nombre de archivo (`TE-OS_M1.md`) se mantiene estable como puntero de boot auto-cargado; el
> Mark vigente lo registra el changelog (§16), no el filename. Refs históricas a "M1" en
> `context/knowledge/` se preservan intactas (historia cruda).

> **Procedencia.** TE-OS es un sistema de **COMANDO / Terrible Enfant**, independiente de
> "BOTH ventures". Patrones reutilizados de otros repos entran como referencia, no como acople.

Construido sobre el **COMANDO Canon** (`COMANDO-AI/C-OS`). Migrado desde la estructura previa
(CORE / STRATEGY / REFERENCE / OPERATIONS / PROJECTS / AUTOMATION) el 2026-06-14.

---

## 1 · NATURALEZA — qué es este repo

Este es el **sistema operativo** de Terrible Enfant — marca de calzado y accesorios masculinos
de autor con identidad de **"luxury punk"**, base en Buenos Aires (Argentina) y en expansión
hacia São Paulo (Brasil — soft-launch abril 2026, full launch julio 2026 post-Mundial).

No es un proyecto de código. Es un **sistema de documentación viva** sincronizado con GitHub —
en términos de harness theory, una **natural-language, file-backed harness (NLAH)**: una capa
de orquestación, externalizada como artefactos `.md`, que gobierna cómo un agente almacena,
recupera y actúa sobre la información de TE. Funciona como archivo institucional, herramienta
de coordinación operacional y superficie de automatización vía Claude Code.

**Toda decisión operacional que no esté documentada aquí no existe formalmente.**

Fundamento: `canon/spec/harness-theory.md` en el repo del Canon (arXiv:2603.28052 +
2603.25723). Dos principios **vinculan cómo evolucionamos este OS**:
- **Aditivo sobre reescritura** → migrar y evolucionar por relocación (`git mv`), no por
  borrar-y-recrear. Preservar historia.
- **Mantener la historia cruda, cruda** → los logs de Cadence (pulse, decision_log,
  automation-log) son la historia file-backed del harness. Relocar intactos; no resumir ni podar.

---

## 2 · LÉXICO FUSIONADO

| Término | Significa |
|---|---|
| **TE-OS** | el sistema operativo de Terrible Enfant — una NLAH (harness file-backed) |
| **El Canon** (`COMANDO-AI/C-OS`) | el meta-harness que estampó este OS |
| **El Charter** | el runtime: Claude Code + `CLAUDE.md` + `.claude/` — política pinneada |
| **El OS layer** | la harness logic: el contenido 4C + este boot spec — versionado por Mark |
| **4C** | Context / Connections / Capabilities / Cadence — cómo se organiza el estado file-backed |
| **WAT** | Workflows / Agents / Tools — el vocabulario *dentro* de 4C |

---

## 3 · EL MODELO 4C — la columna

Todo el contenido del OS vive en cuatro capas. Definición canónica: `canon/spec/4C.md` (repo del Canon).

| Capa | Pregunta | Eje | Contiene | Carpeta |
|---|---|---|---|---|
| **Context** | quién sos / qué es el negocio | **estático** | identidad, estrategia, conocimiento destilado | `context/` |
| **Connections** | tu data e integraciones en vivo | **vivo** | tiendas, ads, drive, mensajería, feeds | `connections/` |
| **Capabilities** | qué podés hacer | — | agentes, workflows, skills | `capabilities/` |
| **Cadence** | qué corre solo / estado vivo | — | rutinas, pulse, logs, operations, projects, weekly | `cadence/` |

**Context vs Connections = estático vs vivo.** Flujo de datos: `Connections (intake vivo) →
Capability (destilación) → Context (residuo durable)`.

"Construir el segundo cerebro" = Context + Connections. "Hacerlo un OS" = Capabilities + Cadence.

---

## 4 · CHARTER vs OS LAYER

- **El Charter** — pinneado, runtime-level, no es una capa de contenido 4C: el runtime de Claude
  Code, `CLAUDE.md` (puntero auto-cargado), `.claude/` (descubrimiento de skills + settings).
  No mover estos a 4C.
- **El OS layer** — la harness logic: el contenido 4C + este boot spec. Específico de TE, por Mark.

**Skills** son una Capability pero viven físicamente en `.claude/` (el Charter — el runtime las
descubre ahí). Se vinculan a Capabilities **por referencia**: `capabilities/skills/REGISTRY.md`.

---

## 5 · WAT DENTRO DE 4C — vocabulario e IDs

WAT (Workflows / Agents / Tools) no es una estructura top-level; vive dentro de las capas:
**Agents** (`AG_*`) + **Workflows** (`WF_*`) → `capabilities/`; **Tools** (`TL_*`) →
`connections/`; workflows auto-disparados + estado → `cadence/`.

**IDs (stack WAT)**: area-based, auto-descriptivos — `<KIND>_<AREA>_<ROLE>`. `KIND` ∈
{`AG`,`WF`,`TL`}. **AREA tokens de TE** (función, no línea de reporte ni mercado):

- **CORE** — orquestación, gobierno, plataforma/infra (Comander, pulse, GitHub, Drive, WhatsApp, n8n).
- **OPS** — el ritmo operacional semanal permanente (6 áreas × 2 mercados; Asana, Nuvemshop).
- **PROJ** — iniciativas time-bounded (campañas, collabs, lanzamientos).
- **MKT** — marketing, GTM, growth, content (CMO, Meta Ads).

> **Mercado (ARG/BRA) NO es un AREA token** — es una sub-dimensión de contenido (carpetas en
> `cadence/operations/ARG|BRA/` y secciones de estrategia). AREA = qué función cumple un archivo;
> 4C = dónde vive. Dos columnas ortogonales.

**Cada card es un NLAH**: un `AG_*` hace su **Role** explícito; un `WF_*` hace su **Stage
structure** (plan → execute → verify → repair), sus **Contracts** (outputs requeridos, gates de
validación, condiciones de parada) y su **failure taxonomy** explícitos.

**Idioma:** tokens estructurales y nombres de archivo en **inglés** (vocab canónico 4C/WAT);
el contenido de TE queda en su **español** existente.

---

## 6 · LA MARCA — contexto esencial

Identidad de **"luxury punk"**. No es moda convencional — es una **posición estética**.

- **Tagline:** *Elegance born from disobedience.*
- **Campaña activa:** Estado de Gracia
- **Referente cultural:** Enfants Riches Déprimés (ERD)
- **Mercados:** Argentina (activo) + Brasil (soft-launch abril 2026 · full launch julio 2026 post-Mundial)
- **Canales BRA:** e-commerce (Nuvemshop) · showroom Centro SP · Dover Market / Rosewood

Contexto completo: `context/identity/brand-narrative.md` y `context/identity/brand-bible.md`.

---

## 7 · EL EQUIPO Y LAS ÁREAS

**Autoridad humana** — Principal: **Boris** (opera el OS; Partner + Creative Director TE Global +
arquitectura operativa BRA). Escalación dividida por dominio (ver §11): marca → Comando;
finanzas/comercial/producto → Hache.

| Persona | Rol |
|---------|-----|
| **Boris** | Principal del OS · Partner · Creative Director (TE Global) · arquitectura BRA · automatización |
| **Comando** (Mariano López Hermida) | Dirección creativa — brazo externo en retainer (~US$1K/mes) |
| **Fanny** | PM Transversal |
| **Hache** | CEO — finanzas, admin, producto |

```
Executive: Hache (CEO) · Comando (Dir. Creativo) → Fanny (PM Transversal)
Argentina: Finance→Hache · Legal→Nacho · Producto→Hache+Comando · Operations→Fanny · Logistics→Jorge+Guada · Marketing→Comando
Brasil:    Finance→Hache+local(pend.) · Legal→estudio local (SIN ASIGNAR — urgente) · Producto→Tiago · Operations→Fanny+Freequency · e-commerce→Lucas Godoy · Logistics→Jorge+Guada+Tiago · Marketing→Freequency+Comando
```

> Jorge es además **inversor**. Freequency = **Fernanda + Tiago** (São Paulo). Lucas Godoy =
> **contractor** del e-commerce BRA (Nuvemshop). Beco = posible community manager (TikTok, tentativo).

Estructura completa: `context/identity/team-structure.md` y `context/identity/org-structure.md`.

**Las seis áreas operacionales** (cada una ARG y BRA, estado vivo en `cadence/operations/`):
Finance & Admin · Legal & Contable · Producto · Operations · Logistics · Marketing & Comms.

---

## 8 · COMANDER — el agente de orquestación

**Comander** es el agente maestro de orquestación — un **rol** que asume cualquier modelo
suficientemente capaz en este workspace. Claude Code aquí **es** Comander salvo que se indique lo
contrario. Card: `capabilities/agents/AG_CORE_COMANDER.md`.

Comander lee el Charter → este spec primero; rutea el trabajo a la capa 4C correcta;
selecciona/compone Workflows, despacha Agents, llama Connections; mantiene el pulse; escala
cuando se requiere autoridad (§11). Si no sabe con quién está hablando, pregunta antes de asumir
el alcance.

---

## 9 · CADENCIA SEMANAL

```
Lunes (antes 18:00)   → cada líder de área actualiza su STATUS.md en cadence/operations/[mercado]/[área]/
Lunes PM              → Boris corre WF_OPS_COMPILE (+ WF_PROJ_COMPILE) → cadence/weekly/2026/W##-YYYY-MM-DD.md
Martes AM             → Boris corre WF_OPS_AGENDA → agenda al equipo
Martes (reunión 45')  → Hache + líderes · solo decisiones, no updates
Martes PM             → WF_OPS_DECISIONS → entradas en cadence/decision_log.md
Mié–Vie               → ejecución
```

La reunión del martes no es para informar — los updates se leen antes. Es para **decidir**.
Proceso humano completo: `capabilities/workflows/WF_OPS_WEEKLY.md`. Rutinas: `cadence/routines.md`.

---

## 10 · ROUTING DE AUTOMATIZACIÓN

Antes de improvisar un proceso, verificar si ya existe un WAT card.

| Trigger / tarea | Recurso | Output |
|-----------------|---------|--------|
| "compilá el semanal" | `capabilities/workflows/WF_OPS_COMPILE.md` (agente `AG_OPS_COMPILER`) | `cadence/weekly/2026/W##-YYYY-MM-DD.md` |
| "estado de proyectos" | `capabilities/workflows/WF_PROJ_COMPILE.md` (agente `AG_PROJ_STATUS`) | resumen de `cadence/projects/active/` |
| "generá la agenda" | `capabilities/workflows/WF_OPS_AGENDA.md` (agente `AG_OPS_AGENDA`) | agenda del martes |
| "loggueá las decisiones" | `capabilities/workflows/WF_OPS_DECISIONS.md` (agente `AG_OPS_DECISIONS`) | entradas en `cadence/decision_log.md` |
| "pulse" / "¿dónde estamos?" | `capabilities/agents/AG_CORE_PULSE.md` | `cadence/pulse.md` |
| "brief de marketing" / "modo CMO" | `capabilities/workflows/WF_MKT_CMO.md` (agente `AG_MKT_CMO`) | `cadence/projects/active/gtm-sao-paulo/cmo-brief-Q#-YYYY.md` |
| "nuevo proyecto" | `capabilities/workflows/WF_PROJ_SETUP.md` | carpeta en `cadence/projects/active/` |
| "cerrá el proyecto" | `capabilities/workflows/WF_PROJ_CLOSE.md` | carpeta movida a `cadence/projects/completed/` |
| "nueva collab" | `capabilities/workflows/WF_PROJ_COLLAB.md` | brief + estructura de collab |
| "miná esta reunión" / transcript nuevo | `capabilities/workflows/WF_OPS_MINE.md` (agente `AG_OPS_MINER`) | recap + items en `cadence/meetings/` · tareas en Asana · email a participantes |

Runbook del operador (Boris): `cadence/runbook.md`.

---

## 11 · ESCALACIÓN & AUTORIDAD

Comander escala cuando: (1) hay dinero involucrado; (2) sale una comunicación externa del estudio;
(3) cambiaría un archivo de `context/identity/`; (4) se redacta copy de campaña sin brief que lo
autorice; (5) se haría commit/push sin revisión de Boris; (6) una herramienta tocaría un sistema
no inventariado. Default: **ante la duda, preguntar.**

**Mapa de autoridad (dividido):**
- **Boris** — principal del OS; commit/push, arquitectura, automatización, dirección creativa.
- **Comando** — aprueba todo contenido de marca (copy, briefs, comunicaciones externas) y
  cambios a `context/identity/`.
- **Hache** — aprueba compromisos financieros/comerciales, producto y decisiones de CEO.

Solo **Fanny** crea y gestiona tareas en Asana — no crear tareas en Asana. **Excepción acotada
(M2, aprobada por Boris + Fanny):** el auto-miner de reuniones (`WF_OPS_MINE` / `AG_OPS_MINER`)
crea tareas directamente en el board live desde action items minados — solo high/med-confidence
y completos (owner + entregable + deadline/trigger), dedup por nombre. Es el **único** proceso
automatizado autorizado a escribir en Asana; Fanny mantiene la curaduría del board.

El mismo miner puede **enviar el recap por email a los participantes internos** de la llamada
(intersección con allowlist) sin gate adicional. Recaps a externos siguen requiriendo **Comando**.

---

## 12 · REPO LAYOUT (4C)

```
TERRIBLE ENFANT | OS1/
├── TE-OS_M1.md          ← este boot spec (OS layer)
├── CLAUDE.md            ← Charter pointer (auto-cargado)
├── README.md            ← entrada humana
├── context/             ← C1 · estático: identity/ · strategy/ · knowledge/
├── connections/         ← C2 · live data / integraciones (TL_*) + README.md (índice)
├── capabilities/        ← C3 · agents/ (AG_*) · workflows/ (WF_*) · skills/REGISTRY.md
├── cadence/             ← C4 · pulse · decision_log · automation-log · runbook · routines
│   ├── operations/ARG|BRA/   ← 6 áreas × STATUS+kpis (estado vivo)
│   ├── projects/{active,pipeline,completed,_templates}/
│   └── weekly/2026/          ← reportes semanales compilados
├── docs/                ← outputs web + briefs (Charter-adjacent)
└── .claude/             ← Charter · runtime + skills/comandos (pinneado)
```

---

## 13 · ASANA Y ESTE REPO

- **Asana** (`connections/TL_OPS_ASANA.md`) es la fuente de verdad para tareas con deadline y
  responsable. Solo Fanny gestiona el Task Board.
- **Este repo** provee narrativa, contexto y decisiones que Asana no puede guardar. No duplica
  Asana — lo complementa.
- **Auto-miner de reuniones.** `WF_OPS_MINE` mina transcripts (`transcripts/**.md`) → escribe el
  machine store en `cadence/meetings/` (recap + decisiones/risks por ítem, cada uno con
  `source_quote` + `confidence`) → crea tareas en Asana (ver excepción §11) → emailea el recap a
  participantes internos. **Nunca toca `cadence/decision_log.md`** (humano, append-only): la
  curación de decisiones minadas al log la hace una persona. Detalle: `connections/TL_OPS_MINER.md`.

---

## 14 · POLÍTICA DE IDIOMA

- Documentos operacionales y boot spec: **español**.
- Tokens estructurales, nombres de archivo, git, automatizaciones técnicas: **inglés**.
- Conversación con Boris: indistinto. Borradores para el equipo: español. Comunicaciones
  internacionales (Freequency, partners BRA): inglés.

---

## 15 · PROTOCOLO DE AUTO-AUDITORÍA

Después de cualquier tarea sustancial: ¿cambió algo en el equipo, herramientas, campañas activas
o estructura del repo? Si sí, proponer una actualización concreta de este boot spec (con
incremento de Mark si es estructural). Una fuente de verdad. Sin bloat.

---

## 16 · CHANGELOG

| Mark | Fecha | Nota |
|---|---|---|
| M1 | 2026-06-14 | Boot spec creado en la **migración al COMANDO Canon (4C)**. TE-OS reestructurado de CORE/STRATEGY/REFERENCE/OPERATIONS/PROJECTS/AUTOMATION a las cuatro capas Context/Connections/Capabilities/Cadence. WAT renombrado area-based (AG_/WF_/TL_ · CORE/OPS/PROJ/MKT). Charter/OS-layer split: `CLAUDE.md` adelgazado a puntero, este spec absorbe la arquitectura. Historia preservada vía `git mv`; logs crudos intactos. Gap map + design archivados en `context/knowledge/`. |
| M2 | 2026-06-20 | **Auto-miner de reuniones** (pure GitHub Actions). Nuevo WAT: `AG_OPS_MINER` + `WF_OPS_MINE` + `TL_OPS_MINER` + `TL_CORE_EMAIL`; rutina `RT-007`; machine store `cadence/meetings/`; trigger `transcripts/**.md`. **Amendment de gobierno (aprobada por Boris + Fanny):** el miner es el único proceso automatizado autorizado a crear tareas en Asana (live board, solo items high/med-confidence + completos, dedup por nombre) y a enviar recaps por email a participantes **internos**. Nunca escribe en `decision_log.md`. Nota de procedencia (COMANDO/TE, no "BOTH ventures") agregada al Charter y a §0. Fases: V1 manual (commit/`workflow_dispatch`); V2 webhook Read AI + audio. |

---

*end of TE-OS_M1 · built on COMANDO Canon*
