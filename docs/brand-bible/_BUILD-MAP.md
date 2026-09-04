# Build map — Brand Bible en Notion (v0.2) — PUBLICADO

> Instrucciones de construcción para el push a Notion. Este archivo NO se importa.
> **Actualizado 2026-09-04** tras leer la Control Tower real vía MCP.

---

## ⚠️ Hallazgo que cambia el encuadre

Este documento **no es nuevo**. Es la pieza faltante de un sistema que ya existe.

**Ya existe** `Brand Bible → Conceptual Identity_0.1` (Notion, últ. edición 2026-04-24, en
**inglés**): 6 secciones — ESSENCE · ORIGIN MYTH · PHILOSOPHICAL FRAMEWORK · TONE OF VOICE ·
CULTURAL POSITION · TAKES. Es el origen de `context/identity/brand-narrative.md` del repo.
**Nuestra v0.2 es su sucesora, no un documento paralelo.**

**Seis fichas del Onboarding Hub ya exigen un "Brand Identity Document" que todavía no
existe** — es exactamente esta pieza:

| Ficha del Onboarding Hub | Qué exige | Cuándo |
|---|---|---|
| NUEVO STAFF | Brand Identity Document, **lectura guiada sección por sección** | 3 días antes |
| COLABORADORES CREATIVOS | Brand Identity Document (versión externa completa) | 48 h antes del 1er encuentro |
| COLABORADORES CREATIVOS | **Guía de Tono y Voz TE** (interna) | En alineación creativa |
| AGENCIAS Y FREELANCERS | Brand Identity Document + Guía de Tono y Voz | Antes del kickoff |
| PARTNERS COMERCIALES / B2B | Brand Identity Document (**versión partner / externa**) | Antes de cerrar acuerdo |
| COORDINADORES DE GESTIÓN | Brand Identity Document listo para entregar | En onboarding |

**Consecuencias de diseño (ya aplicadas a los archivos fuente):**

1. **La sección 07 dejó de ser un onboarding.** El Onboarding Hub (Ops) ya tiene 7 fichas por
   audiencia con fases, criterios, acuerdos y briefs. Duplicarlo era el peor error posible.
   07 pasó a ser **"Cómo leer este documento"**: ruta de lectura por audiencia + puente al Hub.
2. **Las secciones deben ser discretas y discutibles** — NUEVO STAFF prescribe lectura guiada
   sección por sección con el manager. La estructura de 8 subpáginas encaja bien.
3. **Material recuperado de `Conceptual Identity_0.1` que no estaba en el repo** — ya integrado:
   - Origen: las casas venidas a menos de Palermo accesibles para la bohemia (→ `02`)
   - Etapa III: "All of them welcome then." (→ `02`)
   - "Elegance is the ultimate rebellion." — *Manifesto §1* (→ `04`)
   - **Poetics of Encryption** — el artefacto como reliquia cifrada, moda como contra-ritual (→ `04`)
   - Audiencia: "a cosmovision of performative identity" (→ pendiente de integrar en `01`)

---

## Estructura real de la Control Tower (verificada 2026-09-04)

`COMANDO | COMANDO / ⛓️ Terrible Enfant | Control Tower`

```
Marca      → Brand Bible · Colecciones & Producto · Campañas Editoriales Globales · Assets & Archivos
Ops        → Terrible Enfant SO · TERRIBLE | Task Tracker · Decision Log · Meeting Notes
             Weekly Reports · Onboarding Hub
Mercados   → 🇦🇷 Argentina · 🇧🇷 Brasil
Strategy   → General Strategy Workshop · Hiring Plan · Resources allocation
Archived   → Archived TE
```

**`context/knowledge/notion-workspace-architecture.md` del repo está desactualizado:** no
registra la sección *Strategy*, el *Onboarding Hub*, *Terrible Enfant SO*, el *Task Tracker*
ni *Archived*; y llama "Campañas" a lo que en Notion es *Campañas Editoriales Globales*.
Corregirlo es tarea aparte.

**Dentro de `Brand Bible` hoy:** `Conceptual Identity_0.1` · `Protocolo Foto-producto | Social Media`

---

## ✅ PUBLICADO en Notion — 2026-09-04

Creado con las cuatro decisiones de Boris: 0.1 se conserva · una sola versión en español ·
Voz extraída como página hermana · luz verde para crear.

```
Marca → Brand Bible
  ├── Conceptual Identity_0.1        ← intacta, registro histórico
  ├── Protocolo Foto-producto        ← intacto
  ├── 🖤 Brand Bible v0.2            ← página madre
  │   ├── 01 · About                 ├── 05 · Universo en movimiento
  │   ├── 02 · Origen                ├── 06 · Cómo leer este documento
  │   ├── 03 · Alma                  └── 07 · Identidad visual →
  │   └── 04 · Conceptos & Referencias
  └── 🗣️ Guía de Tono y Voz TE       ← página hermana (era 05 · Voz)
```

| Página | URL |
|---|---|
| 🖤 Brand Bible v0.2 | https://app.notion.com/p/3d1a957986e781299d44cd6059ca69e2 |
| 🗣️ Guía de Tono y Voz TE | https://app.notion.com/p/3d1a957986e78119b975d873262aa2c7 |
| 01 · About | https://app.notion.com/p/3d1a957986e781828571fe05659685c2 |
| 02 · Origen | https://app.notion.com/p/3d1a957986e781499d0ff8ff0827d44e |
| 03 · Alma | https://app.notion.com/p/3d1a957986e78172b265c9c7778e744d |
| 04 · Conceptos & Referencias | https://app.notion.com/p/3d1a957986e781ee9f36cef0eb498162 |
| 05 · Universo en movimiento | https://app.notion.com/p/3d1a957986e78127a9cdfc93985b8eb3 |
| 06 · Cómo leer este documento | https://app.notion.com/p/3d1a957986e78137a07efc28f1a9a3c1 |
| 07 · Identidad visual → | https://app.notion.com/p/3d1a957986e7812f9702ea84db21bc5b |

**Verificado en vivo:** toggles, callouts de color, tablas, links a las fichas del Onboarding
Hub y el **synced block** de la esencia (hub ↔ 06). Los archivos locales fueron renumerados
para espejar esta estructura (`05-voz.md` → `guia-tono-voz.md`, y 06/07/08 → 05/06/07).

**Nota de construcción:** envolver los `<page>` en un `<details>` hace que Notion cree una
página intermedia real y anide las subpáginas un nivel de más. No hacerlo — los bloques de
subpágina van sueltos en el cuerpo, con la descripción en un párrafo gris debajo.

## Convenciones de los archivos fuente

- `<!-- TOGGLE: Título -->` … `<!-- /TOGGLE -->` → bloque **toggle** (heading-toggle si es sección).
- `<!-- CALLOUT (emoji[, estilo]) -->` … `<!-- /CALLOUT -->` → **callout** con ese emoji.
  Los "Nunca hacer" en rojo; la regla de oro destacada.
- `<!-- SYNCED BLOCK -->` → **synced block** (la esencia de 1 frase: hub + 07).
- Links relativos `[x](0N-*.md)` → links internos entre subpáginas.
- Tablas markdown → simple tables. Blockquotes de manifiesto → quote block.

## Decisiones de arquitectura (respaldadas por research)

- **Manifiesto primero, esencia después** — why-before-what; lo emocional nunca en toggles.
  Voz y léxico al final: son las secciones más *consultadas*, no las más leídas de corrido.
- **Hub + 8 subpáginas de 1 nivel** — máx. recomendado 2 niveles. El hub resuelve el 80%.
- **Cada regla con ejemplo** — pares on-brand/off-brand en columnas (sección Voz).
- **Caveat:** si se comparte como link público de Notion, los toggles rinden peor —
  considerar headings planos + TOC para esa vista.

## Presupuesto de extensión

≈ 5–7 páginas A4 de corrido (rango acordado 5–10). Si una sección crece, crece dentro de sus
toggles, no en el cuerpo.

---

## Decisiones tomadas (Boris, 2026-09-04)

1. **`Conceptual Identity_0.1` se conserva** al lado, como registro histórico. La nueva entra
   como `Brand Bible v0.2`. ✅ aplicado
2. **Una sola versión, en español.** La "versión externa/partner" que exige el Hub será un
   recorte de esta misma, no una traducción paralela. ✅ aplicado
3. **`Guía de Tono y Voz TE` extraída** como página hermana dentro de Brand Bible, tal como la
   nombra el Onboarding Hub. ✅ aplicado
4. **Luz verde para crear en Notion.** ✅ aplicado

## Abierto — próximos pasos

- **Revisión de Comando y Hache** sobre el documento ya publicado (esto reemplaza la aprobación
  previa; ahora revisan sobre algo concreto).
- **Versión externa / partner:** definir el recorte. Propuesta: excluir `05 · Universo`
  (campañas en desarrollo, información reservada hasta el drop) y dejar `01 · About`,
  `02 · Origen`, `03 · Alma`, `04 · Conceptos`. Requiere visto bueno antes de generarla.
- **Actualizar las fichas del Onboarding Hub** para que el "Brand Identity Document" y la
  "Guía de Tono y Voz TE" apunten a las páginas nuevas — hoy las nombran sin link.
- **Covers de página:** esperar dirección del Brand Deck de Figma.
- **`Los Siete`:** decisión de Comando (sub-serie de Estado de Gracia o campaña autónoma)
  — afecta `05 · Universo`.
- **Corregir `context/knowledge/notion-workspace-architecture.md`**, desactualizado (ver arriba).

## Otras discrepancias detectadas (no bloquean, pero conviene resolver)

- El Onboarding Hub nombra un rol **"Manager Operacional"** que no figura en
  `context/identity/team-structure.md` (que registra a Fanny como PM transversal). ¿Es el mismo rol?
- El Hub asigna a **Boris** la decisión final de collabs y a **COMANDO** la aprobación de
  comunicación. El repo dice "aprueba Comando" para todo lo de identidad. Vale precisar la frontera
  (ya está marcada como pendiente de reconciliación en `team-structure.md`).
- El Hub menciona a **Horacio** donde el repo usa **Hache**. Confirmar que es la misma persona
  y unificar el nombre en el documento externo.
