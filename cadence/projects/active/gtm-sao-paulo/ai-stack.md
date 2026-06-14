# AI Stack & Automatización — GTM

**Última actualización:** 2026-06-01

**Principio rector:** automatizar solo después de validar el hábito manual.

---

## Stack operacional actual

| Herramienta | Propósito | Estado |
|-------------|-----------|--------|
| Claude Code (VS Code) | Automatizaciones, redacción, compilaciones, este OS | 🟢 Activo |
| Claude Projects | Thinking estratégico, briefs, documentos | 🟢 Activo |
| Notion | Tres capas: Global / OPS / Mercados | 🟢 Activo |
| Asana | Task tracking (reemplazó Linear) | 🟢 Activo |
| GitHub | Source of truth del OS — interfaz pasiva de Hache | 🟢 Activo |
| WooCommerce | Ecomm ARG | 🟢 Activo |
| Nuvemshop | Ecomm BR (Lucas) | 🟡 En construcción |
| Meta Ads | Paid ARG activo; paid BR en diseño | 🟡 |
| n8n | Automatización Fase 3 (post-launch) | ⚪ Planeado |

---

## Fases del AI stack

### Fase 1 — Manual validado 🟢 Activo
Claude Projects, Notion, Asana, gestión manual de procesos. El OS1 vive acá.

### Fase 2 — En curso 🟡 (diseñar ahora)
- Claude API para **copy BR en PT** (traducción + transcreación con voz de marca)
- **Video AI** (Kling / Eversince) para contenido de campaña
- **Scheduling IG** automatizado
- Ecomm BR (Nuvemshop) operativo
- Meta Ads BR estructurado

### Fase 3 — Post-launch Q4 2026 ⚪ Planificado
Pipeline de reporting semanal:
```
n8n agrega → Meta Ads + Nuvemshop + IG
          → digest semanal vía Claude API
          → tasks automáticas en Asana
          → alertas por anomalías de ROAS o stock
```

---

## Cómo la IA sostiene el GTM (agentes + skills)

| Capa | Recurso | Qué automatiza |
|------|---------|----------------|
| Dirección | `AUTOMATION/agents/cmo-strategist.md` | Lectura estratégica de marketing + apuestas por trimestre |
| Momentum | `AUTOMATION/agents/pulse-strategist.md` | Síntesis de momentum del sistema completo |
| Reporting | `AUTOMATION/agents/weekly-compiler.md` | Compila STATUS.md → reporte semanal |
| Copy / contenido | Claude API (Fase 2) | Copy BR en PT, transcreación con voz de marca |
| Producción visual | Kling / Runway / FLUX (Fase 2) | Video y editorial para campañas |
| Datos (Fase 3) | n8n + Claude API | Digest de métricas → tasks → alertas |

El **cmo-strategist** es el cerebro de marketing: lee este dashboard + KPIs + decisiones y propone dónde invertir esfuerzo cada trimestre, con conciencia explícita de qué se puede automatizar.
