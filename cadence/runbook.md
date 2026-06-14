# Playbook de Automatización — Boris

Este documento describe qué automatiza Boris, cómo lo hace, y cómo replicarlo si fuera necesario.  
Audiencia: Boris, y cualquier Claude Code instance que trabaje con Boris en este repo.

---

## Stack técnico

- **Claude Code:** VS Code extension · modelo claude-sonnet-4-6
- **Repositorio:** Este repo local, sincronizado con GitHub private
- **Método:** Boris abre el repo en VS Code, da instrucciones a Claude Code en lenguaje natural, Claude Code lee los archivos relevantes y produce el output
- **No hay scripts automáticos en V1** — todo es disparado manualmente por Boris

---

## Automatizaciones activas (V1)

### 1. Compilación del reporte semanal

**Cuándo:** Cada lunes después de las 18:00 (cuando ya están todos los STATUS.md actualizados)  
**Duración:** ~20 minutos de trabajo de Boris + Claude  
**Output:** Archivo `WEEKLY/2026/W[XX]-[fecha-lunes].md`

**Pasos:**
1. Abrir VS Code en este repo
2. Abrir una nueva conversación con Claude Code
3. Pegar el contenido del prompt `AUTOMATION/prompts/compile-weekly-status.md`
4. Completar los campos variables (número de semana, fecha del martes)
5. Revisar el output de Claude, ajustar si hay errores factuales
6. Guardar el reporte en `WEEKLY/2026/`
7. Commit: `[W15] Compile weekly report`

**Señales de que algo está mal:**
- Un STATUS.md dice "W__" en vez de la semana actual → ese líder no actualizó
- El reporte tiene áreas con estado vacío → falta input de ese líder
- Acción: contactar al líder por WhatsApp y pedir el update

---

### 2. Agenda de la reunión semanal

**Cuándo:** Martes AM, antes de las 10:00  
**Duración:** ~10 minutos  
**Output:** Agenda enviada al grupo de WhatsApp ejecutivo

**Pasos:**
1. Abrir VS Code, nueva conversación con Claude Code
2. Pegar el prompt `AUTOMATION/prompts/draft-meeting-agenda.md`
3. Reemplazar `[archivo]` con el nombre del reporte de esta semana
4. Copiar el output
5. Enviarlo por WhatsApp o email al grupo ejecutivo

---

### 3. Log de decisiones post-reunión

**Cuándo:** Martes entre las 15:00 y 18:00 (después de la reunión)  
**Duración:** ~15 minutos  
**Output:** Entradas nuevas en `OPERATIONS/_GLOBAL/weekly-decisions-log.md`

**Pasos:**
1. Durante o inmediatamente después de la reunión, Boris o Fanny anotan las decisiones en crudo (texto libre, WhatsApp, notas de voz — cualquier formato)
2. Abrir VS Code, nueva conversación con Claude Code
3. Pegar el prompt `AUTOMATION/prompts/generate-decision-log.md`
4. Pegar las notas crudas donde indica el prompt
5. Revisar el output formateado
6. Appendear al decisions log
7. Actualizar el índice en `WEEKLY/decisions-index.md`
8. Commit: `[DECISION] Log decisions [fecha]`

---

### 4. Tracker de lanzamiento BRA

**Cuándo:** Semanal, como parte de la compilación del reporte  
**Duración:** ~5 minutos adicionales  
**Output:** Tabla de estado de los 3 canales BRA + próxima collab

Este output ya está integrado en el reporte semanal (sección Operations BRA). No requiere un paso separado — Claude lo extrae del STATUS.md de `OPERATIONS/BRA/operations/`.

---

### 5. Narrativa de KPIs mensual

**Cuándo:** Primer lunes de cada mes  
**Duración:** ~20 minutos  
**Output:** Párrafo narrativo de estado por mercado, para el investor update a Jorge

**Pasos:**
1. Asegurarse de que los kpis.md de todas las áreas están actualizados con datos del mes
2. Abrir VS Code, nueva conversación con Claude Code
3. Instrucción: "Lee todos los archivos kpis.md en OPERATIONS/ARG/ y OPERATIONS/BRA/. Para cada mercado, genera un párrafo de 5-7 líneas que describa el estado operacional del mes, destacando los KPIs más relevantes y señalando los que están fuera de meta. Tono: directo, ejecutivo, en español."
4. Revisar y ajustar el output
5. Usar como base para el update mensual a Jorge (investor)

---

## Señales de que el sistema funciona

- El reporte del martes AM tiene estado verde/amarillo/rojo en todas las áreas
- El decisions log tiene entradas de la semana anterior
- Los STATUS.md de las áreas de Fanny están actualizados al lunes
- Boris puede producir el reporte semanal completo en menos de 20 minutos

---

## Señales de que algo se rompió

| Síntoma | Causa probable | Acción |
|---------|---------------|--------|
| STATUS.md sin actualizar el lunes | El líder olvidó o no adoptó el sistema | WhatsApp directo, recordatorio |
| Reporte semanal inconsistente | Campos vacíos o contradictorios | Boris revisa y llena con lo que sabe |
| Claude no encuentra los archivos | El repo tiene conflictos o archivos movidos | Verificar estructura de carpetas |
| Decisions log sin entradas | Fanny no pudo documentar post-reunión | Boris lo hace con sus notas |

---

## Roadmap de automatización

### V1 — Ahora (manual, Boris ejecuta)
- Compilación del reporte semanal
- Agenda de reunión
- Log de decisiones
- Tracker BRA

### V2 — Q3 2026 (más equipo adoptó el sistema)
- Freequency completa STATUS.md via GitHub web editor
- KPI narrativa mensual automatizada
- Brief templates para collabs BRA

### V3 — Q4 2026 / 2027 (agentic)
- GitHub Actions + Claude API → compilación automática lunes 20:00
- Integración Asana ↔ repo (tareas cerradas → STATUS actualizado)
- Cada líder de área tiene VS Code + Claude Code setup propio
- Boris pasa de ejecutor a arquitecto de automatizaciones
