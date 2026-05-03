# Workflow: Iniciar un nuevo proyecto

**Trigger:** se aprueba una nueva iniciativa (campaña, collab, lanzamiento)
**Dueño del proceso:** Boris (setup técnico) + owner del proyecto (contenido)
**Tiempo estimado:** 30 minutos

---

## Pasos

### 1. Determinar tipo y estado inicial

**Quién:** Boris + owner del proyecto
**Cómo:** responder estas preguntas:
- ¿Qué tipo es? → `campaign` / `collab` / `launch`
- ¿Ya empezó el trabajo? → `active` / sigue en planificación → `pipeline`
- ¿Tiene fecha de drop / evento / cierre?

---

### 2. Crear carpeta con template

**Quién:** Boris
**Cómo:**

Si es `pipeline`:
```
PROJECTS/pipeline/[tipo]-[nombre]/
└── brief.md    ← llenar datos básicos: tipo, estado, fecha, owner, resumen
```

Si es `active`:
```
PROJECTS/active/[tipo]-[nombre]/
├── brief.md      ← copiar de PROJECTS/_templates/[tipo]-template/
├── STATUS.md     ← copiar de PROJECTS/_templates/[tipo]-template/
└── [archivos adicionales según tipo]
```

Nomenclatura de carpetas: `collab-[nombre-en-minúsculas-con-guiones]`

---

### 3. Completar el brief

**Quién:** owner del proyecto (Comando para campañas/collabs, Hache para lanzamientos)
**Qué completar en `brief.md`:**
- Resumen (2-3 líneas)
- Objetivo
- Entregables clave
- Criterios de éxito
- Dependencias operacionales (qué áreas de OPERATIONS/ necesita)

---

### 4. Registrar dependencias operacionales

**Quién:** Boris + Fanny
**Cómo:** agregar una línea en `OPERATIONS/_GLOBAL/project-touchpoints.md` con el proyecto y qué área operacional necesita y para cuándo.

---

### 5. Notificar a Fanny

**Quién:** Boris
**Cómo:** WhatsApp al grupo ejecutivo o DM a Fanny
**Mensaje tipo:** "Creé la carpeta para [nombre del proyecto] en PROJECTS/active/. Owner: [nombre]. Fecha: [fecha]. ¿Creás las tareas en Asana?"

**Output:** Fanny crea las tareas correspondientes en Asana.

---

### 6. (Si el proyecto pasó de pipeline a active)

Mover la carpeta de `PROJECTS/pipeline/` a `PROJECTS/active/`, agregar los archivos faltantes (STATUS.md, deliverables.md, etc.) desde los templates.

---

## Criterios de éxito

- Carpeta creada con los archivos correctos
- brief.md con resumen + objetivo + entregables completos
- Dependencias registradas en project-touchpoints.md
- Fanny notificada → tareas en Asana creadas
