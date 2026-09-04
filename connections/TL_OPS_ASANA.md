# Herramienta: Asana

**Owner:** Fanny
**Propósito:** tareas operacionales con deadline, responsable y estado de ejecución

---

## Qué vive en Asana

- Toda tarea con nombre + owner + deadline + estado
- Follow-up de decisiones tomadas en reunión del martes
- Tareas derivadas de STATUS.md que requieren ejecución

## Qué NO vive en Asana

- Contexto, narrativa y razonamiento detrás de una decisión → este repo
- KPIs y estado de áreas → `cadence/operations/[mercado]/[área]/STATUS.md` y `kpis.md`
- Briefs de proyectos → `cadence/projects/`
- Archivos binarios → Google Drive

## Quién puede crear tareas en Asana

**Solo Fanny** (humanos). Ningún otro miembro del equipo crea tareas. Claude Code en sesión tampoco.

Flujo estándar: reunión → decisión → Boris hace commit del log → Fanny crea tarea en Asana.

**Excepción automatizada (amendment M2, aprobada por Boris + Fanny):** el **auto-miner de
reuniones** (`WF_OPS_MINE` / `AG_OPS_MINER`, ver `connections/TL_OPS_MINER.md`) crea tareas
directamente en el board live desde action items minados — **solo** los completos
(owner + deliverable + deadline) y con confidence ≥ medium, **dedup por nombre**. Es el único
proceso automatizado autorizado a escribir en Asana. Fanny mantiene la curaduría del board
(triage, reasignación, cierre).

## Quién actualiza el estado de tareas

El responsable de la tarea (owner) actualiza el estado. Fanny hace seguimiento.

## Integración con este repo

| Evento en el repo | Acción en Asana |
|-------------------|----------------|
| Decisión logueada en `weekly-decisions-log.md` | Fanny crea tarea |
| Proyecto pasa a `active/` | Fanny crea project en Asana y vincula |
| STATUS.md reporta bloqueador | Fanny crea tarea de desbloqueo si no existe |

## Task properties estándar

- **Título:** verbo + objeto ("Cerrar contrato showroom BRA")
- **Área:** Finance & Admin / Legal & Contable / Producto / Operations / Logistics / Marketing & Comms
- **Mercado:** ARG / BRA / Ambos
- **Owner:** 1 persona (no grupos)
- **Status:** Por hacer / En curso / Bloqueada / Completada / Cancelada
- **Prioridad:** Alta / Media / Baja
- **Deadline:** obligatorio

---

## Conexión MCP (Claude Code)

**Estado:** activo · configurado en `~/.claude/settings.json` (global)
**Paquete:** `@roychri/mcp-server-asana` (community, PAT-based)
**Modo:** read-only — Claude Code **en sesión** no crea ni modifica tareas (solo consulta). La
escritura automatizada vive aparte, en la Action del miner (`TE_ASANA_TOKEN` con scope de
escritura, no en el MCP) — ver `connections/TL_OPS_MINER.md`.

### IDs del workspace TE

| Recurso | ID |
|---------|----|
| Workspace | `1214079921372448` |
| Proyecto principal | `1214109688126860` |
| Sección activa | `1214103633061371` |

### Cómo usar en una sesión de Claude Code

Dentro de cualquier sesión, Boris puede pedir:
- "Listá las tareas abiertas en el proyecto Asana de TE"
- "¿Qué tareas están bloqueadas esta semana?"
- "Mostrá las tareas de Fanny con deadline esta semana"

Claude Code consulta Asana en vivo via MCP y devuelve los datos en el contexto de la sesión.

### Upgrade pendiente

La configuración actual usa un Personal Access Token (PAT). El upgrade recomendado es migrar al servidor oficial de Asana V2 (`mcp.asana.com`) con OAuth — más seguro, sin token que rotar. Requiere crear una OAuth app en el portal de desarrolladores de Asana.

---

## Auth (1Password)

> Convención del Canon: los secretos nunca van al repo. 1Password es el vault de record;
> se inyectan en runtime vía `op`. Documentar acá solo el **nombre del item**, nunca el valor.

- **Vault item:** `TODO: vault ref` — completar con el nombre del item en el vault de TE.
