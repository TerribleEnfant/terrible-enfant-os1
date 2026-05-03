# Prompt: Compilar Estado de Proyectos Activos

**Uso:** Pegar esto en Claude Code (VS Code) junto con la compilación semanal (lunes PM).
**Completar los campos entre corchetes antes de enviar.**

---

```
Lee todos los archivos STATUS.md en PROJECTS/active/ — uno por proyecto activo.
Lee también los brief.md de todos los proyectos en PROJECTS/pipeline/ para extraer las fechas de activación próximas.

Para cada proyecto activo, extrae:
1. Nombre del proyecto
2. Estado general (🟢/🟡/🔴) con una línea de contexto
3. Avances de la semana
4. Bloqueadores activos
5. Próximos pasos clave
6. Notas para el martes (si las hay)

Para cada proyecto en pipeline, extrae:
1. Nombre
2. Fecha de drop / evento
3. Si la fecha está dentro de los próximos 30 días: marcarlo como "⚠️ activar pronto"

Produce una sección con este formato para incluir en el reporte semanal:

---
## Estado de Proyectos Activos — W[NUMERO]

### Proyectos en ejecución

| Proyecto | Estado | Bloqueador principal | Próximo hito |
|---------|--------|---------------------|-------------|
[tabla generada]

### Detalle por proyecto

[Para cada proyecto activo: nombre, estado, avances, bloqueadores, próximos pasos, notas para martes]

### Pipeline — próximas activaciones

[Lista de proyectos en pipeline con fecha, destacando los que activar en los próximos 30 días]
---

Si algún proyecto activo no tiene STATUS.md actualizado esta semana, indicarlo explícitamente.

Idioma: español.
```

---

**Después de ejecutar el prompt:**
1. Revisar que todos los proyectos activos están incluidos
2. Copiar la sección generada al reporte semanal (después del semáforo BRA y antes de la agenda propuesta)
3. Si hay proyectos de pipeline con activación próxima, asegurarse de que estén en la agenda del martes
