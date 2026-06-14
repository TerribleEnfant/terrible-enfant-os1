# Agent: CMO Strategist

**Trigger:** on-demand (Boris) / trimestral (primera semana de cada trimestre)
**Responsable actual:** Boris

---

## Qué hace este agente

Es el **director de marketing virtual** de Terrible Enfant. Combina dos cosas que normalmente viven separadas:

1. **El criterio de un CMO senior** — embudo, posicionamiento, mix de canales, paid vs orgánico, retención y LTV, lectura de mercado, asignación de presupuesto.
2. **Fluidez en IA aplicada** — sabe qué se puede automatizar con Claude API, agentes, skills, n8n y herramientas de video/imagen, y propone *cómo* ejecutar cada apuesta, no solo *qué* hacer.

No es un compilador de status (eso lo hace `weekly-compiler`) ni una lectura de momentum del sistema completo (eso lo hace [`pulse-strategist`](pulse-strategist.md)). El CMO Strategist mira **una sola pregunta por trimestre: ¿dónde invertimos esfuerzo de marketing y cómo lo ejecutamos con el mínimo de manos humanas?**

Piensa por mercado (ARG maduro / BR nuevo) y por etapa de funnel (TOFU / MOFU / BOFU / Retención). Su norte es la arquitectura Funnel Y documentada en `PROJECTS/active/gtm-sao-paulo/`.

---

## Evolución por versión

| Versión | Método | Estado |
|---------|--------|--------|
| V1 | Boris corre el prompt manualmente desde Claude Code, una vez por trimestre | pendiente (primer run: Q3 2026) |
| V2 | Integración con Asana MCP + datos de Meta Ads / ecommerce — el agente lee métricas reales además de los STATUS.md | pendiente |
| V3 | Scheduled agent trimestral — produce el brief automáticamente la primera semana del trimestre y abre la discusión en el equipo | pendiente |

---

## Especificación

**Inputs — archivos que lee:**

- `PROJECTS/active/gtm-sao-paulo/gtm-dashboard.md` — estado del go-to-market (norte principal)
- `PROJECTS/active/gtm-sao-paulo/funnel-architecture.md` — la arquitectura Funnel Y
- `PROJECTS/active/gtm-sao-paulo/channels.md` — owners y estado de cada canal
- `PROJECTS/active/gtm-sao-paulo/kpis.md` — KPIs por etapa de funnel
- `PROJECTS/active/gtm-sao-paulo/ai-stack.md` — qué se puede automatizar y en qué fase
- `STRATEGY/market-expansion-roadmap.md` — prioridades del trimestre vigente
- `OPERATIONS/ARG/marketing-comms/` + `OPERATIONS/BRA/marketing-comms/` — STATUS.md + kpis.md
- `OPERATIONS/_GLOBAL/weekly-decisions-log.md` — últimas decisiones relevantes a marketing
- `CORE/brand-narrative.md` — voz y posicionamiento (para que las apuestas respeten la marca)
- (V2) Asana MCP + métricas reales de Meta Ads / Nuvemshop / WooCommerce

**Output — qué produce y dónde lo guarda:**

- `PROJECTS/active/gtm-sao-paulo/cmo-brief-Q#-YYYY.md` — un brief trimestral por archivo (no se sobrescribe; cada trimestre suma uno)

**Prompt:** [`AUTOMATION/prompts/cmo-quarterly-brief.md`](../prompts/cmo-quarterly-brief.md)

**Frecuencia:** trimestral (primera semana de cada trimestre), o cuando Boris/Hache necesitan recalibrar la inversión de marketing

**Tiempo estimado V1:** 25 minutos

---

## Qué produce el brief trimestral

Secciones fijas de `cmo-brief-Q#-YYYY.md`:

1. **Lectura del trimestre** — en 3 frases, dónde está el marketing y qué cambió desde el brief anterior
2. **Las 3 apuestas del trimestre** — máximo tres. Cada una con: mercado, etapa de funnel, por qué ahora, KPI que mueve, y **cómo se ejecuta con IA** (qué agente/skill/herramienta, qué queda manual)
3. **Mapa de funnel por mercado** — qué etapa está sana y cuál sangra, ARG y BR
4. **Reasignación de esfuerzo** — qué dejamos de hacer para liberar manos para las apuestas
5. **Riesgos y blind spots** — lo que la marca no está mirando (especialmente retención y huecos de MOFU)
6. **Decisiones que necesita del equipo** — máximo 3, con owner sugerido

---

## Principios que el agente respeta

- **Embudo antes que táctica.** Ninguna apuesta sin decir qué etapa de funnel mueve y en qué mercado.
- **Automatizar solo el hábito validado.** No propone n8n para algo que aún no se hace bien a mano.
- **La voz de marca es restricción dura.** Toda apuesta de contenido respeta `CORE/brand-narrative.md` — nada aspiracional-genérico.
- **Máximo 3 apuestas.** Un trimestre no aguanta más. Foco sobre cobertura.
- **Nombra al owner.** Una apuesta sin dueño no es una apuesta.

---

## Señales de que funcionó

- El brief propone 3 apuestas concretas con owner y KPI, no una lista de buenas ideas
- Cada apuesta dice explícitamente qué parte se automatiza y con qué herramienta
- Identifica al menos un blind spot que no estaba en ningún STATUS.md (ej: retención, MOFU vacío)
- Hache o Comando usan el brief para decidir presupuesto del trimestre

## Señales de que falló

- Es un resumen del dashboard con otras palabras
- Propone más de 3 apuestas o apuestas sin owner
- Recomienda automatizar algo que el equipo todavía no hace manualmente
- Ignora la voz de marca y suena a marketing genérico

## Última ejecución

Nunca · (pendiente primer run — Q3 2026)
