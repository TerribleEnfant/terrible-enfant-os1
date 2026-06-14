# Workflow: Cadencia Semanal

**Trigger:** inicio de semana (lunes)
**Dueño del proceso:** Boris (coordinación) + Fanny (decisiones post-reunión)
**Participantes:** todos los líderes de área, Boris, Fanny, Hache, Comando
**Frecuencia:** semanal
**Tiempo estimado:** ~2 horas distribuidas en lunes y martes

---

## Pasos

### 1. Actualización de STATUS — líderes de área

**Quién:** cada líder de área (Hache, Nacho, Comando, Fanny, Jorge, Tiago/Freequency)
**Cuándo:** lunes antes de las 18:00
**Cómo:** editar directamente en GitHub web o desde el repo local
**Archivos a actualizar:**
- `OPERATIONS/ARG/[área]/STATUS.md` → responsable ARG
- `OPERATIONS/BRA/[área]/STATUS.md` → responsable BRA
- `PROJECTS/active/[proyecto]/STATUS.md` → owner del proyecto

**Output:** 12 STATUS.md operacionales + N STATUS.md de proyectos activos actualizados

---

### 2. Compilación del reporte semanal — Boris

**Quién:** Boris
**Cuándo:** lunes PM (después de las 18:00)
**Cómo:**
1. Abrir Claude Code en VS Code
2. Ejecutar agent `weekly-compiler` con prompt en `AUTOMATION/prompts/compile-weekly-status.md`
3. Ejecutar agent `project-status-roller` con prompt en `AUTOMATION/prompts/compile-project-status.md`
4. Revisar el borrador generado: verificar que no haya campos vacíos
5. Guardar como `WEEKLY/2026/W##-YYYY-MM-DD.md`

**Output:** reporte semanal compilado en WEEKLY/2026/

---

### 3. Generación de agenda — Boris

**Quién:** Boris
**Cuándo:** martes AM antes de las 10:00
**Cómo:**
1. Ejecutar agent `agenda-drafter` con prompt en `AUTOMATION/prompts/draft-meeting-agenda.md`
2. Revisar que la agenda respete el límite de 45 minutos
3. Enviar al grupo ejecutivo de WhatsApp

**Output:** agenda del martes enviada al equipo

---

### 4. Reunión ejecutiva

**Quién:** Hache + Comando + Fanny (+ líderes de área según agenda)
**Cuándo:** martes (horario fijo)
**Duración:** 45 minutos
**Formato:** solo decisiones — los updates ya están en el reporte
- Apertura (2 min)
- Semáforo rápido (5 min)
- Decisiones (20 min)
- Update BRA (10 min)
- Cierre (5 min)

**Output:** decisiones tomadas (documentadas por Fanny en notas)

---

### 5. Registro de decisiones — Fanny (+ Boris)

**Quién:** Fanny con asistencia de Boris
**Cuándo:** martes PM (dentro de las 2 horas post-reunión)
**Cómo:**
1. Fanny pasa las notas de reunión a Boris
2. Boris ejecuta agent `decision-logger` con prompt en `AUTOMATION/prompts/generate-decision-log.md`
3. Las decisiones se appendean a `OPERATIONS/_GLOBAL/weekly-decisions-log.md`
4. El índice en `WEEKLY/decisions-index.md` se actualiza
5. Fanny crea las tareas correspondientes en Asana

**Output:** decisiones documentadas + tareas en Asana creadas

---

### 6. Ejecución — miércoles a viernes

**Quién:** cada área / owner de tarea
**Cómo:** seguir tareas en Asana
**Bloqueos urgentes:** WhatsApp grupo ejecutivo

---

## Criterios de éxito

- Reporte compilado antes del martes AM
- Agenda enviada antes de las 10:00 del martes
- Decisiones logueadas antes del miércoles AM
- Todos los STATUS.md actualizados sin campos vacíos

## Errores comunes y cómo resolverlos

| Problema | Causa probable | Solución |
|---------|---------------|---------|
| STATUS.md no actualizado el lunes | Líder de área no lo hizo | Boris pide por WhatsApp; si no llega, reportar como "sin update" |
| Reporte con campos vacíos | Claude genera placeholder | Boris completa manualmente o consulta al responsable |
| Reunión se extiende más de 45 min | Demasiados updates, no decisiones | Recordar que el reporte se lee antes; cortarla en 45 min sin excepción |
