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

Para contexto completo de marca, leer `00_CORE/brand-narrative.md` y `00_CORE/brand-bible.md`.

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

Para estructura completa, leer `00_CORE/team-structure.md`.

---

## Las seis áreas operacionales

Cada área existe para ARG y BRA. Los archivos de estado y KPIs viven en `02_OPERATIONS/`:

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
- Redactar o actualizar archivos STATUS.md cuando se te pida
- Compilar el reporte semanal leyendo todos los STATUS.md (ver prompt en `04_AUTOMATION/prompts/`)
- Redactar agendas de reunión a partir del reporte compilado
- Actualizar el decisions log después de una reunión cuando te den notas
- Redactar briefs de campaña, textos de marca, documentos operacionales
- Generar narrativas de KPIs cuando se te provean datos
- Señalar inconsistencias entre estados de ambos mercados
- Archivar reportes semanales completados en `03_WEEKLY/2026/`

---

## Lo que NO debes hacer

- No modificar archivos en `00_CORE/` sin instrucción explícita de Hache o Comando
- No hacer proyecciones financieras sin datos provistos en el contexto de la conversación
- No asumir que una tarea está completada a menos que un STATUS.md lo diga explícitamente
- No crear archivos fuera de la estructura de carpetas establecida sin consultar a Boris
- No crear tareas en Asana — eso es dominio exclusivo de Fanny
- No modificar el decisions log de manera retroactiva — es append-only

---

## Protocolo de automatización (Boris)

Boris opera Claude Code en VS Code. Cuando Boris dice "compilá el semanal" o similar:

1. Leer todos los archivos `STATUS.md` en `02_OPERATIONS/ARG/` y `02_OPERATIONS/BRA/`
2. Extraer por área y mercado: estado general (🟢🟡🔴), avances, bloqueadores, notas para el martes
3. Producir un reporte consolidado usando la plantilla en `03_WEEKLY/_template-weekly-report.md`
4. Guardar el resultado como `03_WEEKLY/2026/W[XX]-[fecha-lunes].md`

Prompts reutilizables completos en `04_AUTOMATION/prompts/`.
Instrucciones del playbook completo en `04_AUTOMATION/boris-playbook.md`.

---

## Estructura de carpetas del repo

```
TERRIBLE ENFANT | OS1/
├── CLAUDE.md                    ← este archivo
├── README.md                    ← orientación para humanos
│
├── 00_CORE/                     ← ADN de marca (no duplicar por mercado)
├── 01_STRATEGY/                 ← documentos estratégicos globales
│
├── 02_OPERATIONS/               ← corazón operacional
│   ├── _GLOBAL/                 ← coordinación transversal (Fanny)
│   ├── ARG/                     ← 6 áreas con STATUS.md + kpis.md
│   └── BRA/                     ← espejo de las 6 áreas ARG
│
├── 03_WEEKLY/                   ← reportes semanales compilados
│   └── 2026/                    ← archivo por semana
│
├── 04_AUTOMATION/               ← dominio de Boris
│   ├── prompts/                 ← prompts reutilizables para Claude
│   └── logs/                    ← registro de automatizaciones
│
├── 05_ARCHIVE/                  ← campañas cerradas, ciclos completados
│
└── 06_REFERENCE/                ← documentos originales, Notion, legacy
```
