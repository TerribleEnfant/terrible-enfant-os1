# Agent: Pulse Strategist

**Trigger:** on-demand (Boris) / mensual (primer lunes de cada mes)
**Responsable actual:** Boris

---

## Qué hace este agente

Lee el estado operacional + las decisiones recientes + los proyectos activos y produce un documento de síntesis estratégica: **dónde está la marca ahora, hacia dónde va, y qué está frenando el movimiento.**

No es un reporte de status. Es una lectura de momentum.

---

## Evolución por versión

| Versión | Método | Estado |
|---------|--------|--------|
| V1 | Boris corre el prompt manualmente desde Claude Code | pendiente |
| V2 | Integración con Asana MCP — el agente puede leer tareas activas además de STATUS.md | pendiente |
| V3 | Scheduled agent mensual — produce `pulse.md` automáticamente el primer lunes de cada mes | pendiente |

---

## Especificación

**Inputs — archivos que lee:**

- `STRATEGY/*.md` — los documentos de dirección vigentes (referentes de norte)
- `PROJECTS/active/*/STATUS.md` — estado de cada proyecto en ejecución
- `OPERATIONS/_GLOBAL/weekly-decisions-log.md` — últimas 4 semanas de decisiones
- `WEEKLY/2026/` — los últimos 2 reportes semanales compilados
- (V2) Asana MCP: tareas abiertas en el proyecto principal

**Output — qué produce y dónde lo guarda:**

- Actualiza `OPERATIONS/_GLOBAL/pulse.md` con la lectura estratégica del momento
- No genera archivos adicionales — pulse.md es acumulativo (secciones con fecha)

**Prompt:** `AUTOMATION/prompts/pulse-strategist.md` ← (a crear)

**Frecuencia:** mensual (o cuando Boris siente que el equipo perdió el norte)

**Tiempo estimado V1:** 15 minutos

---

## Qué produce pulse.md

Secciones que el agente actualiza cada vez que corre:

1. **Norte activo** — los 2-3 objetivos estratégicos que mandan ahora mismo
2. **Momentum** — dónde hay energía real (proyectos ganando velocidad)
3. **Fricción** — qué está frenando el movimiento (bloqueadores estratégicos, no operacionales)
4. **Brecha estrategia ↔ ejecución** — qué está en STRATEGY/ pero sin tracción en PROJECTS/
5. **Señal de la semana** — una observación concisa sobre el estado general del sistema

---

## Señales de que funcionó

- pulse.md tiene una lectura que sorprende: dice algo que no estaba en ningún STATUS.md individual
- Boris o Hache usan el output en una conversación de dirección
- El equipo puede leer pulse.md en 3 minutos y entender dónde está la marca

## Señales de que falló

- Es un resumen del reporte semanal con otras palabras
- No menciona brechas entre estrategia y ejecución
- Tiene más de 600 palabras

## Última ejecución

Nunca · (pendiente primer run)
