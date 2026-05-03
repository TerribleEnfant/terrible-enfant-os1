    # CLAUDE.md — Terrible Enfant OS1

Este archivo es el punto de entrada para cualquier instancia de Claude Code que trabaje en este repositorio. Léelo completo antes de ejecutar cualquier tarea.

---

## Qué es este repositorio

Este es el **sistema operativo (OS)** de Terrible Enfant — una marca de calzado y accesorios de lujo con base en Buenos Aires (Argentina) y en expansión hacia São Paulo (Brasil, abril 2026).

Este repositorio NO es un proyecto de código. Es un **sistema de documentación viva** sincronizado con GitHub. Funciona como archivo institucional, herramienta de coordinación operacional y superficie de trabajo para automatizaciones vía Claude Code.

Toda decisión operacional que no esté documentada aquí no existe formalmente.

---

## Con quién estás hablando

Cuando te abre alguien en este repo, es probable que sea una de estas personas:

| Persona | Rol | Qué te va a pedir |
|---------|-----|-------------------|
| **Boris** | Coordinador de IA / AI Tools Manager | Automatizar, compilar, redactar, analizar el repo completo |
| **Comando** (Mariano López Hermida) | Director Creativo | Campañas, identidad de marca, copy, operaciones |
| **Fanny** | PM Transversal | Estado de áreas, decisiones, prep de reunión |
| **Hache** | CEO | Resúmenes ejecutivos, estado financiero, decisiones |

Si no sabes con quién estás hablando, pregunta antes de asumir el alcance.

---

## Política de idioma

- Documentos operacionales: **español**
- Documentos técnicos / automatizaciones / git: **inglés**
- Conversación con Boris: inglés o español, indistinto
- Borradores para el equipo: español salvo que se indique lo contrario
- Comunicaciones internacionales (Freequency, partners BRA): inglés

---

## La marca: contexto esencial

Terrible Enfant es una marca de calzado y accesorios masculinos de autor con identidad de "luxury punk". No es una marca de moda convencional — es una **posición estética**.

- **Tagline:** *Elegance born from disobedience.*
- **Campaña activa:** Estado de Gracia
- **Referente cultural:** Enfants Riches Déprimés (ERD)
- **Mercados:** Argentina (activo) + Brasil (lanzamiento abril 2026)
- **Canales BRA:** e-commerce · showroom Centro SP · Dover Market / Rosewood

Para contexto completo de marca, leer `CORE/brand-narrative.md` y `CORE/brand-bible.md`.

---

## Estructura del equipo

```
Executive
├── Hache (CEO) — finanzas, admin, producto (ambos mercados)
└── Comando (Dir. Creativo) — identidad, campañas, operaciones (ambos mercados)
    └── Fanny (PM Transversal) — coordina todas las áreas y mercados

Argentina
├── Finance & Admin    → Hache
├── Legal & Contable   → Nacho
├── Producto           → Hache + Comando
├── Operations         → Fanny
├── Logistics          → Jorge
└── Marketing & Comms  → Comando

Brasil
├── Finance & Admin    → Hache + admin local (pendiente)
├── Legal & Contable   → estudio local (SIN ASIGNAR — urgente)
├── Producto           → Tiago (contacto Freequency)
├── Operations         → Fanny + Freequency
├── Logistics          → Jorge + Tiago
└── Marketing & Comms  → Freequency + Comando
```

Para estructura completa, leer `CORE/team-structure.md`.

---

## Las seis áreas operacionales

Cada área existe para ARG y BRA. Los archivos de estado y KPIs viven en `OPERATIONS/`:

| Área | Carpeta | Responsable ARG | Responsable BRA |
|------|---------|----------------|----------------|
| Finance & Admin | `finance-admin/` | Hache | Hache |
| Legal & Contable | `legal-contable/` | Nacho | TBD (urgente) |
| Producto | `producto/` | Comando | Tiago |
| Operations | `operations/` | Fanny | Fanny + Freequency |
| Logistics | `logistics/` | Jorge | Jorge + Tiago |
| Marketing & Comms | `marketing-comms/` | Comando | Freequency |

---

## Cadencia semanal

```
Lunes (antes de 18:00)   → Cada líder de área actualiza su STATUS.md
Lunes PM                 → Boris compila todos los STATUS.md en el reporte semanal
Martes AM                → Boris envía el reporte al equipo antes de la reunión
Martes (reunión, 45 min) → Hache + líderes · solo decisiones, no updates
Martes PM                → Fanny publica decisiones en weekly-decisions-log.md
Miércoles–Viernes        → Ejecución
```

La reunión del martes no es para informar — los updates se leen antes. La reunión es para **decidir**.

---

## Asana y este repositorio

- **Asana** es la fuente de verdad para tareas con deadline y responsable
- **Este repo** provee narrativa, contexto y decisiones que Asana no puede guardar
- Solo Fanny crea y gestiona el Task Board central en Asana
- Este repo NO duplica Asana — lo complementa

---

## Lo que puedes hacer en este repo

- Leer cualquier archivo para obtener contexto
- Redactar o actualizar archivos STATUS.md de OPERATIONS/ y PROJECTS/ cuando se te pida
- Compilar el reporte semanal leyendo STATUS.md de OPERATIONS/ y PROJECTS/active/ (ver prompts en `AUTOMATION/prompts/`)
- Redactar agendas de reunión a partir del reporte compilado
- Actualizar el decisions log después de una reunión cuando te den notas
- Redactar briefs de campaña, textos de marca, documentos operacionales
- Generar narrativas de KPIs cuando se te provean datos
- Señalar inconsistencias entre estados de ambos mercados o entre proyectos y operaciones
- Archivar reportes semanales completados en `WEEKLY/2026/`
- Crear la carpeta de un proyecto nuevo desde los templates en `PROJECTS/_templates/` (siguiendo el workflow en `AUTOMATION/workflows/new-project-setup.md`)

---

## Lo que NO debes hacer

- No modificar archivos en `CORE/` sin instrucción explícita de Hache o Comando
- No hacer proyecciones financieras sin datos provistos en el contexto de la conversación
- No asumir que una tarea está completada a menos que un STATUS.md lo diga explícitamente
- No crear archivos fuera de la estructura de carpetas establecida sin consultar a Boris
- No crear tareas en Asana — eso es dominio exclusivo de Fanny
- No modificar el decisions log de manera retroactiva — es append-only
- No publicar ni enviar contenido de marca (copy, briefs, comunicaciones externas) sin aprobación de Comando
- No redactar copy de campaña sin el brief correspondiente como contexto — el brief es la autorización
- No hacer commit ni push al repo sin que Boris haya revisado los cambios

---

## Protocolo de automatización (Boris)

Boris opera Claude Code en VS Code. Antes de improvisar cualquier proceso, verificar si ya existe un prompt o workflow en `AUTOMATION/`.

**Routing de automatización — cuándo usar qué:**

| Trigger / tarea | Recurso | Output |
|-----------------|---------|--------|
| "compilá el semanal" | `AUTOMATION/prompts/compile-weekly-status.md` | `WEEKLY/2026/W##-YYYY-MM-DD.md` |
| "generá la agenda del martes" | `AUTOMATION/prompts/draft-meeting-agenda.md` | Agenda para enviar al equipo |
| "loggueá las decisiones" | `AUTOMATION/prompts/generate-decision-log.md` | Entradas en `weekly-decisions-log.md` |
| "estado de proyectos" | `AUTOMATION/prompts/compile-project-status.md` | Resumen de `PROJECTS/active/` |
| "nuevo proyecto" | `AUTOMATION/workflows/new-project-setup.md` | Carpeta en `PROJECTS/active/` |
| "cerrá el proyecto" | `AUTOMATION/workflows/project-close.md` | Carpeta movida a `PROJECTS/completed/` |
| "nueva collab" | `AUTOMATION/workflows/collab-launch.md` | Brief + estructura de collab |

Playbook completo con pasos detallados: `AUTOMATION/boris-playbook.md`.

---

## Estructura de carpetas del repo

```
TERRIBLE ENFANT | OS1/
├── CLAUDE.md                    ← este archivo
├── README.md                    ← orientación para humanos
│
├── CORE/                        ← ADN de marca (no duplicar por mercado)
├── STRATEGY/                    ← documentos de dirección estratégica (roadmaps, no briefs)
│
├── OPERATIONS/                  ← corazón operacional — ritmo semanal
│   ├── _GLOBAL/                 ← coordinación transversal (Fanny)
│   │   └── project-touchpoints.md  ← puente entre PROJECTS/ y OPERATIONS/
│   ├── ARG/                     ← 6 áreas con STATUS.md + kpis.md
│   └── BRA/                     ← espejo de las 6 áreas ARG
│
├── PROJECTS/                    ← iniciativas time-bounded — con ciclo de vida
│   ├── _templates/              ← kits de inicio por tipo de proyecto
│   ├── active/                  ← proyectos en ejecución (con STATUS.md actualizable)
│   ├── pipeline/                ← planificados, aún no iniciados (brief stub only)
│   └── completed/               ← proyectos cerrados (carpeta intacta como registro)
│
├── WEEKLY/                      ← reportes semanales compilados
│   └── 2026/                    ← archivo por semana
│
├── AUTOMATION/                  ← dominio de Boris — 4 capas
│   ├── agents/                  ← definición de tareas automatizables (specs V1→V3)
│   ├── workflows/               ← procesos paso a paso para humanos y Claude
│   ├── tools/                   ← catálogo de integraciones externas
│   ├── prompts/                 ← prompts reutilizables para Claude
│   └── logs/                    ← registro de ejecuciones
│
├── ARCHIVE/                     ← ciclos cerrados, reportes de años anteriores
│
└── REFERENCE/                   ← documentos originales, Notion, legacy
```

---

## Stack operacional

Ver catálogo completo en `AUTOMATION/tools/_tools-index.md`.

| Herramienta | Propósito | Owner |
|-------------|-----------|-------|
| GitHub | Fuente de verdad del OS | Boris |
| Asana | Tareas con deadline y responsable | Fanny |
| Claude Code (VS Code) | Automatizaciones, redacción, compilaciones | Boris |
| Google Drive | Assets, contratos, planillas | Hache / Fanny |
| WhatsApp | Comunicación interna | Todos |
| Instagram / TikTok | Canales de marca | Comando |

---

## Voz para redacción

Cuando Claude redacta contenido de marca — copy, briefs, comunicaciones — debe seguir estas reglas:

- **Registro:** preciso, cargado, nunca aspiracional-genérico
- **Evitar:** "innovador", "tendencia", "exclusivo", "lujo" (sin elaboración) — palabras vacías para esta marca
- **Preferir:** contradicción productiva ("elegancia que incomoda"), brevedad cargada, frases que dejan silencio
- Frases cortas. Fragmentos aceptables. Sin exclamaciones.
- **Referentes:** ERD, Helmut Lang tardío, Nick Cave, cine de Haneke
- **Idioma:** seguir la política de idioma del repo según destino de la pieza

**Audiencia — segmentos y registro para cada uno:**

| Segmento | Quiénes son | Qué buscan | Ángulo de entrada |
|----------|-------------|------------|-------------------|
| Románticos decadentes | Creativos urbanos, intelectuales, artistas | Identidad no negociable, estética como posición | "Uniformes para los que se niegan a ser nadie." |
| Luxury explorers | Compradores HNWI ARG/BRA/EU, 28–45 | Objeto con narrativa, no moda de temporada | "Hecho para destruirse bellamente." |
| Luxury punk circle | Referentes de gusto, insiders de moda | Credibilidad cultural, no masividad | "Lujo para los que vieron demasiado." |
| Compradores Brasil (BRA launch) | Mercado SP, consumidor de marca autor | Marca con origen y posición, no genérico | "Elegancia nacida de la desobediencia." |

---

## Sistema de automatización (capas)

`AUTOMATION/` tiene cuatro capas. Antes de improvisar un proceso, revisar si ya existe algo en alguna de estas carpetas.

| Capa | Carpeta | Qué contiene |
|------|---------|--------------|
| Agentes | `AUTOMATION/agents/` | Definición de tareas automatizables: trigger, inputs, output, evolución V1→V3 |
| Workflows | `AUTOMATION/workflows/` | Procesos paso a paso para humanos y Claude (cadencia semanal, setup de proyectos, etc.) |
| Tools | `AUTOMATION/tools/` | Catálogo de integraciones externas y cómo se usan |
| Prompts | `AUTOMATION/prompts/` | Fragmentos de texto listos para usar con Claude Code |

Prompts disponibles:

| Prompt | Propósito |
|--------|-----------|
| `compile-weekly-status.md` | Compila los STATUS.md de OPERATIONS/ en reporte semanal |
| `compile-project-status.md` | Compila los STATUS.md de PROJECTS/active/ |
| `draft-meeting-agenda.md` | Genera agenda del martes desde el reporte compilado |
| `generate-decision-log.md` | Extrae decisiones de notas de reunión |

Playbook completo: `AUTOMATION/boris-playbook.md`.

---

## Sistema de proyectos

Los proyectos time-bounded (campañas, collabs, lanzamientos) viven en `PROJECTS/`. No mantener tabla de iniciativas en este archivo — se desactualiza. Leer directamente las carpetas.

- `PROJECTS/active/` → proyectos en ejecución. Cada carpeta tiene `STATUS.md` actualizable semanalmente (mismo formato que OPERATIONS/).
- `PROJECTS/pipeline/` → proyectos planificados, aún no iniciados. Solo tienen `brief.md` con fecha y owner.
- `PROJECTS/completed/` → proyectos cerrados. Carpeta intacta como registro histórico.

Para leer el estado de todos los proyectos activos: leer todos los `PROJECTS/active/*/STATUS.md`.

Para iniciar un nuevo proyecto: seguir el workflow en `AUTOMATION/workflows/new-project-setup.md`.

Para cerrar un proyecto: seguir el workflow en `AUTOMATION/workflows/project-close.md`.

Dependencias entre proyectos y áreas operacionales: `OPERATIONS/_GLOBAL/project-touchpoints.md`.

---

## Protocolo de auto-auditoría

Después de cualquier tarea sustancial: ¿cambió algo en el equipo, herramientas, campañas activas o estructura del repo? Si sí, proponer una actualización concreta de este archivo. Una fuente de verdad. Sin bloat.
