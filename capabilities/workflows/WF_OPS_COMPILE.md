# Prompt: Compilar Reporte Semanal

**Uso:** Pegar esto en Claude Code (VS Code) cada lunes PM, después de que los STATUS.md estén actualizados.  
**Completar los campos entre corchetes antes de enviar.**

---

```
Lee todos los archivos STATUS.md en las siguientes rutas:

OPERATIONS/ARG/finance-admin/STATUS.md
OPERATIONS/ARG/legal-contable/STATUS.md
OPERATIONS/ARG/producto/STATUS.md
OPERATIONS/ARG/operations/STATUS.md
OPERATIONS/ARG/logistics/STATUS.md
OPERATIONS/ARG/marketing-comms/STATUS.md

OPERATIONS/BRA/finance-admin/STATUS.md
OPERATIONS/BRA/legal-contable/STATUS.md
OPERATIONS/BRA/producto/STATUS.md
OPERATIONS/BRA/operations/STATUS.md
OPERATIONS/BRA/logistics/STATUS.md
OPERATIONS/BRA/marketing-comms/STATUS.md

Para cada área y mercado, extrae:
1. Estado general (🟢/🟡/🔴) con una línea de contexto
2. Avances principales de la semana
3. Bloqueadores activos
4. Próximos pasos
5. Notas para el martes (si las hay)

Luego produce un reporte consolidado usando el formato exacto de la plantilla en:
WEEKLY/_template-weekly-report.md

Variables a completar en el reporte:
- Semana: W[NUMERO] · [FECHA LUNES]
- Fecha de reunión martes: [FECHA MARTES]

Si algún STATUS.md tiene el campo "Semana" sin completar (dice "W__"), indicarlo explícitamente en el reporte — ese líder no actualizó a tiempo.

Guardar el reporte final con el nombre: W[NUMERO]-[FECHA-LUNES].md
(ejemplo: W16-2026-04-20.md)

Idioma del reporte: español.
```

---

**Después de ejecutar el prompt:**
1. Revisar el output — verificar que no haya información faltante o incorrecta
2. Guardar en `WEEKLY/2026/`
3. Commit: `[W__] Compile weekly report`
4. Enviar por WhatsApp/email al equipo antes del martes AM
