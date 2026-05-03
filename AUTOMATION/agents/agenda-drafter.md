# Agent: agenda-drafter

**Trigger:** manual — Boris lo ejecuta cada martes AM (antes de la reunión)
**Responsable actual:** Boris

---

## Evolución por versión

| Versión | Método | Estado |
|---------|--------|--------|
| V1 | Boris corre `draft-meeting-agenda.md` desde Claude Code después de compilar el reporte | activo |
| V2 | Boris o Fanny corren el prompt; la agenda se envía al grupo de WhatsApp antes de las 10:00 | pendiente (Q3 2026) |
| V3 | GitHub Action genera la agenda automáticamente al detectar el nuevo archivo en WEEKLY/2026/ | pendiente (Q4 2026) |

---

## Especificación

**Inputs — archivos que lee:**

- `WEEKLY/2026/W##-YYYY-MM-DD.md` — reporte de la semana actual
- `OPERATIONS/_GLOBAL/meeting-agenda-template.md`

**Output — qué produce y dónde lo guarda:**

- Agenda del martes (texto) enviada al grupo ejecutivo de WhatsApp
- (opcional) guardada como `OPERATIONS/_GLOBAL/agenda-W##.md` para referencia

**Prompt:** [`AUTOMATION/prompts/draft-meeting-agenda.md`](../prompts/draft-meeting-agenda.md)

**Frecuencia:** semanal, martes AM (antes de las 10:00)

**Tiempo estimado V1:** 10 minutos

---

## Priorización de puntos en agenda

1. Bloqueadores BRA (críticos para el lanzamiento)
2. Bloqueadores que afectan más de un área
3. Temas de finance / legal con deadline
4. Resto (por impacto descendente)

## Señales de que funcionó

- Agenda enviada a WhatsApp antes de las 10:00 del martes
- Todos los "Decisión requerida" del reporte están incluidos
- Agenda respeta el límite de 45 minutos con estimaciones de tiempo

## Señales de que falló

- Reporte semanal no disponible (dependencia)
- Agenda con más de 5 puntos sin priorización clara

## Última ejecución

W__ · [fecha]
