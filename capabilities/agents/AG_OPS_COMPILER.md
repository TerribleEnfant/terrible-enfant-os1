# Agent: weekly-compiler

**Trigger:** manual — Boris lo ejecuta cada lunes PM
**Responsable actual:** Boris

---

## Evolución por versión

| Versión | Método | Estado |
|---------|--------|--------|
| V1 | Boris corre `compile-weekly-status.md` desde Claude Code en VS Code | activo |
| V2 | Boris corre el prompt + Freequency puede llenar STATUS de proyectos vía GitHub web | pendiente (Q3 2026) |
| V3 | GitHub Action ejecuta automáticamente cada lunes a las 20:00 y hace commit del reporte | pendiente (Q4 2026) |

---

## Especificación

**Inputs — archivos que lee:**

- `OPERATIONS/ARG/*/STATUS.md` (6 archivos)
- `OPERATIONS/BRA/*/STATUS.md` (6 archivos)
- `PROJECTS/active/*/STATUS.md` (variable)
- `WEEKLY/_template-weekly-report.md`

**Output — qué produce y dónde lo guarda:**

- `WEEKLY/2026/W##-YYYY-MM-DD.md` — reporte semanal consolidado

**Prompt:** [`AUTOMATION/prompts/compile-weekly-status.md`](../prompts/compile-weekly-status.md)

**Frecuencia:** semanal, lunes PM (antes de las 22:00)

**Tiempo estimado V1:** 20 minutos

---

## Señales de que funcionó

- Todos los STATUS tienen estado (🟢/🟡/🔴), no placeholder
- El archivo W##-YYYY-MM-DD.md existe en WEEKLY/2026/
- La sección "Estado de Proyectos Activos" está incluida

## Señales de que falló

- STATUS.md con campos vacíos o con texto "completar"
- Archivo de reporte no generado
- Inconsistencia entre mercados (ej: BRA reporta problema que ARG no menciona)

## Última ejecución

W15 · 2026-04-10 (setup) — primera compilación real: W16 · 2026-04-20
