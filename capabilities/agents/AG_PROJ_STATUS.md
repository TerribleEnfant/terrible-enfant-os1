# AG_PROJ_STATUS · project-status-roller

**Trigger:** manual — Boris lo corre como parte de la compilación semanal
**Responsable actual:** Boris

---

## Evolución por versión

| Versión | Método | Estado |
|---------|--------|--------|
| V1 | Boris corre `compile-project-status.md` antes o después del weekly-compiler | activo (nuevo) |
| V2 | Owners de proyectos (Comando, Freequency) actualizan sus STATUS.md vía GitHub web; Boris compila | pendiente (Q3 2026) |
| V3 | Integrado en GitHub Action del weekly-compiler | pendiente (Q4 2026) |

---

## Especificación

**Inputs — archivos que lee:**

- `cadence/projects/active/*/STATUS.md` (todos los STATUS de proyectos activos)
- `cadence/projects/pipeline/*/brief.md` (para visibilidad de próximas fechas)

**Output — qué produce y dónde lo guarda:**

- Sección "Estado de Proyectos Activos" para incluir en el reporte semanal
- (eventualmente integrado directamente en el weekly-compiler)

**Prompt:** [`capabilities/workflows/WF_PROJ_COMPILE.md`](../prompts/compile-project-status.md)

**Frecuencia:** semanal, lunes PM (junto con weekly-compiler)

**Tiempo estimado V1:** 10 minutos

---

## Señales de que funcionó

- Todos los proyectos en `active/` tienen estado (🟢/🟡/🔴)
- Proyectos en pipeline con fechas próximas (<30 días) están marcados como "activar pronto"

## Señales de que falló

- STATUS.md de proyectos no actualizado esta semana
- Proyecto activo sin STATUS.md (falta el archivo)

## Última ejecución

— (agente nuevo)
