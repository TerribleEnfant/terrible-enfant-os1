# WF_OPS_COMPILE · Compilar Reporte Semanal

**Uso:** Pegar esto en Claude Code (VS Code) cada lunes PM, después de que los STATUS.md estén actualizados.  
**Completar los campos entre corchetes antes de enviar.**

---

```
Lee todos los archivos STATUS.md en las siguientes rutas:

cadence/operations/ARG/finance-admin/STATUS.md
cadence/operations/ARG/legal-contable/STATUS.md
cadence/operations/ARG/producto/STATUS.md
cadence/operations/ARG/operations/STATUS.md
cadence/operations/ARG/logistics/STATUS.md
cadence/operations/ARG/marketing-comms/STATUS.md

cadence/operations/BRA/finance-admin/STATUS.md
cadence/operations/BRA/legal-contable/STATUS.md
cadence/operations/BRA/producto/STATUS.md
cadence/operations/BRA/operations/STATUS.md
cadence/operations/BRA/logistics/STATUS.md
cadence/operations/BRA/marketing-comms/STATUS.md

Para cada área y mercado, extrae:
1. Estado general (🟢/🟡/🔴) con una línea de contexto
2. Avances principales de la semana
3. Bloqueadores activos
4. Próximos pasos
5. Notas para el martes (si las hay)

Luego produce un reporte consolidado usando el formato exacto de la plantilla en:
cadence/weekly/_template-weekly-report.md

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
2. Guardar en `cadence/weekly/2026/`
3. Commit: `[W__] Compile weekly report`
4. Enviar por WhatsApp/email al equipo antes del martes AM
