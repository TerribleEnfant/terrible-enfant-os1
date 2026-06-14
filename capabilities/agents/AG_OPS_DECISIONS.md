# AG_OPS_DECISIONS · decision-logger

**Trigger:** manual — Boris o Fanny lo ejecuta cada martes PM (post-reunión)
**Responsable actual:** Boris / Fanny

---

## Evolución por versión

| Versión | Método | Estado |
|---------|--------|--------|
| V1 | Fanny pega notas de reunión; Boris corre el prompt desde Claude Code | activo |
| V2 | Fanny corre el prompt directamente desde Claude Code o interfaz web | pendiente (Q3 2026) |
| V3 | Fanny hace commit de las notas de reunión; GitHub Action extrae y appendea decisiones automáticamente | pendiente (2027) |

---

## Especificación

**Inputs — archivos que lee:**

- Notas crudas de la reunión (pegadas en el prompt como contexto)
- `cadence/decision_log.md` (para append)
- `cadence/weekly/decisions-index.md` (para actualizar el índice)

**Output — qué produce y dónde lo guarda:**

- Nuevas decisiones formateadas → appendeadas a `cadence/decision_log.md`
- Líneas de índice → appendeadas a `cadence/weekly/decisions-index.md`

**Prompt:** [`capabilities/workflows/WF_OPS_DECISIONS.md`](../prompts/generate-decision-log.md)

**Frecuencia:** semanal, martes PM (después de la reunión)

**Tiempo estimado V1:** 15 minutos

---

## Reglas críticas

- El log es **append-only** — nunca editar decisiones previas
- Solo extraer decisiones claras con owner y deadline, no "hay que pensar en X"
- Owner ambiguo → marcar como "pendiente de asignar"

## Señales de que funcionó

- Nuevas decisiones en `weekly-decisions-log.md` con todos los campos
- `decisions-index.md` actualizado con las nuevas entradas

## Señales de que falló

- Notas de reunión no disponibles o incompletas
- Decisiones sin owner o sin deadline claros

## Última ejecución

W__ · [fecha]
