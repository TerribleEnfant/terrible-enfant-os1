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
- KPIs y estado de áreas → `OPERATIONS/[mercado]/[área]/STATUS.md` y `kpis.md`
- Briefs de proyectos → `PROJECTS/`
- Archivos binarios → Google Drive

## Quién puede crear tareas en Asana

**Solo Fanny.** Ningún otro miembro del equipo crea tareas. Claude Code tampoco.

Flujo estándar: reunión → decisión → Boris hace commit del log → Fanny crea tarea en Asana.

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
**Modo:** read-only — Claude Code no crea ni modifica tareas

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
