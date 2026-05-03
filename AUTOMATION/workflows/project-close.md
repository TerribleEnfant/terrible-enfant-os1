# Workflow: Cerrar un proyecto

**Trigger:** proyecto completado (drop ejecutado, lanzamiento estabilizado, campaña cerrada)
**Dueño del proceso:** Boris
**Tiempo estimado:** 15 minutos

---

## Pasos

### 1. Verificar que el proyecto está realmente terminado

**Quién:** owner del proyecto
- Todos los entregables en `deliverables.md` marcados como completados
- Ningún bloqueador activo en `STATUS.md`
- Fanny confirma que no quedan tareas abiertas en Asana

---

### 2. Actualizar brief.md con retrospectiva

**Quién:** owner del proyecto
**Cómo:** agregar sección al final de `brief.md`:
```
## Retrospectiva
**Fecha de cierre:**
**Qué funcionó:**
**Qué no funcionó:**
**Para la próxima vez:**
```

---

### 3. Actualizar STATUS.md con estado final

**Quién:** Boris
- Estado: ✅ Completado
- Anotar fecha de cierre

---

### 4. Mover carpeta a completed/

**Quién:** Boris
```
git mv PROJECTS/active/[nombre]/ PROJECTS/completed/[nombre]/
```
La carpeta y todo su contenido quedan intactos como registro.

---

### 5. Actualizar project-touchpoints.md

**Quién:** Boris
- Eliminar o marcar como cerradas las dependencias del proyecto

---

### 6. Notificar al equipo

**Quién:** Boris
- Mensaje breve al grupo ejecutivo: "[nombre] cerrado. Retrospectiva en PROJECTS/completed/[nombre]/brief.md"

---

## Criterios de éxito

- Carpeta en `completed/` con retrospectiva en `brief.md`
- `project-touchpoints.md` sin dependencias activas de ese proyecto
- Equipo notificado
