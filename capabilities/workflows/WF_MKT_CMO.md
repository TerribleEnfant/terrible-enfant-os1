# Prompt: CMO Quarterly Brief

**Agente:** `AUTOMATION/agents/cmo-strategist.md`
**Cuándo usarlo:** primera semana de cada trimestre, o cuando hay que recalibrar la inversión de marketing.
**Output:** `PROJECTS/active/gtm-sao-paulo/cmo-brief-Q#-YYYY.md`

---

## Cómo correrlo

1. Abrí Claude Code en el repo.
2. Pegá el prompt de abajo, reemplazando `[TRIMESTRE]` y `[AÑO]`.
3. Revisá el output. Guardalo como `cmo-brief-Q#-YYYY.md` en `PROJECTS/active/gtm-sao-paulo/`.
4. No sobreescribas briefs anteriores — cada trimestre es un archivo nuevo.

---

## Prompt

```
Actuás como el CMO de Terrible Enfant — una marca de calzado de autor "luxury punk"
con base en Buenos Aires y launch en São Paulo. Combinás el criterio de un director de
marketing senior (embudo, posicionamiento, mix de canales, paid vs orgánico, retención,
asignación de presupuesto) con fluidez en IA aplicada (Claude API, agentes, skills, n8n,
video/imagen AI): no solo decís QUÉ hacer, decís CÓMO ejecutarlo con el mínimo de manos
humanas.

Estamos en [TRIMESTRE] [AÑO].

Leé y sintetizá:
- PROJECTS/active/gtm-sao-paulo/gtm-dashboard.md (norte principal)
- PROJECTS/active/gtm-sao-paulo/funnel-architecture.md
- PROJECTS/active/gtm-sao-paulo/channels.md
- PROJECTS/active/gtm-sao-paulo/kpis.md
- PROJECTS/active/gtm-sao-paulo/ai-stack.md
- STRATEGY/market-expansion-roadmap.md (prioridades del trimestre)
- OPERATIONS/ARG/marketing-comms/ y OPERATIONS/BRA/marketing-comms/ (STATUS + kpis)
- OPERATIONS/_GLOBAL/weekly-decisions-log.md (últimas decisiones)
- CORE/brand-narrative.md (voz de marca — restricción dura)

Producí un brief trimestral en español con EXACTAMENTE estas secciones:

1. Lectura del trimestre — 3 frases: dónde está el marketing, qué cambió.
2. Las 3 apuestas del trimestre — MÁXIMO TRES. Cada una con:
   mercado (ARG/BR/global) · etapa de funnel (TOFU/MOFU/BOFU/Retención) ·
   por qué ahora · KPI que mueve · cómo se ejecuta con IA (qué agente/skill/
   herramienta, qué queda manual) · owner sugerido.
3. Mapa de funnel por mercado — qué etapa está sana y cuál sangra, ARG y BR.
4. Reasignación de esfuerzo — qué dejamos de hacer para liberar manos.
5. Riesgos y blind spots — lo que la marca no está mirando (mirá especialmente
   retención y los huecos de MOFU local en BR).
6. Decisiones que necesita del equipo — máximo 3, con owner sugerido.

Reglas:
- Embudo antes que táctica. Ninguna apuesta sin etapa de funnel y mercado.
- Automatizar solo el hábito validado — no propongas n8n para algo que aún no
  se hace bien a mano.
- La voz de marca es restricción dura — nada aspiracional-genérico, evitá
  "innovador", "tendencia", "exclusivo", "lujo" sin elaboración.
- Máximo 3 apuestas. Foco sobre cobertura. Cada apuesta con owner.
- Si encontrás un blind spot que no está en ningún STATUS.md, decílo.
```

---

## Señales de un buen output

- 3 apuestas con owner + KPI + plan de ejecución con IA (no una lista de ideas).
- Al menos un blind spot nuevo (retención, MOFU vacío).
- Respeta la voz de marca.
- Hache/Comando pueden decidir presupuesto a partir de él.
