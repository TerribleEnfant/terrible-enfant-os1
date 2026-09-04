# WF_OPS_DECISIONS · Generar Log de Decisiones

**Uso:** Pegar esto en Claude Code (VS Code) el martes PM, después de la reunión.  
**Completar los campos entre corchetes antes de enviar.**

---

```
Se acaba de realizar la reunión semanal de Terrible Enfant.

Fecha de la reunión: [FECHA MARTES]

A continuación van las notas crudas de la reunión (pueden ser texto libre, 
WhatsApp, fragmentos de conversación — no importa el formato):

---
[PEGAR NOTAS AQUÍ]
---

Con esas notas, extrae todas las decisiones tomadas y formatea cada una así:

## Decisión · [fecha]

**Área:** [área operacional]  
**Mercado:** ARG / BRA / Ambos  
**Decisión:** [descripción clara y accionable — qué se decidió hacer]  
**Responsable de ejecución:** [nombre]  
**Fecha límite:** [si se mencionó en la reunión, si no: "no especificada"]  
**Próximo checkpoint:** [siguiente martes — fecha]  
**Contexto:** [una línea — por qué se tomó esta decisión]

---

Reglas:
- Cada decisión en un bloque separado
- Si algo fue "para evaluar" o "pensarlo" — NO es una decisión, no lo incluyas
- Si una decisión no tiene responsable claro, marcarlo como "pendiente de asignar"
- Máximo de precisión en los responsables — nombres propios, no roles genéricos
- Idioma: español

Al final, también genera una versión condensada para el índice:
Formato de cada fila: | [fecha] | [área] | [mercado] | [decisión en 10 palabras max] | [responsable] | ⏳ |
```

---

**Después de ejecutar el prompt:**
1. Revisar cada decisión — verificar que son precisas y completas
2. Appendear al final de `cadence/decision_log.md`
3. Agregar las filas del índice al final de `cadence/weekly/decisions-index.md`
4. Commit: `[DECISION] Log decisions [fecha]`
5. Notificar a Fanny por WhatsApp que el log está actualizado
