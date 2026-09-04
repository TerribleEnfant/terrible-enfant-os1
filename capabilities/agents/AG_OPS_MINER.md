# Agent: AG_OPS_MINER — minero de reuniones

**Trigger:** event (commit de `transcripts/**.md`) + manual (`workflow_dispatch` / force-mine)
**Responsable actual:** sistema (GitHub Actions) · operador: Boris

---

## Evolución por versión

| Versión | Método | Estado |
|---------|--------|--------|
| V1 | Commit de transcript (o `workflow_dispatch`) dispara la Action; mina, escribe store, Asana, email | activo |
| V2 | Webhook de Read AI → relay mínimo → `repository_dispatch` (sin intervención humana) | pendiente |
| V2 | Force-mine de **audio**: paso de transcripción (Whisper/Deepgram) antes de minar | pendiente |
| V3 | Curación asistida: proponer promoción de decisiones minadas al `decision_log.md` para revisión humana | idea |

---

## Especificación

**Inputs — archivos que lee:**

- `transcripts/<YYYY-MM-DD>-<slug>.md` — transcript crudo (trigger + archivo)
- `config/te-mining.json` — markets, áreas, proyectos, people→Asana GID, allowlist de email, gids de Asana
- `scripts/prompts/mine-prompt.md` — reglas de extracción

**Output — qué produce y dónde lo guarda:**

- `cadence/meetings/<base>.md` (recap) + `.json` (estructurado)
- `cadence/meetings/decisions/<base>-<n>.md` · `cadence/meetings/risks/<base>-<n>.md`
- Tareas en Asana (board live, dedup por nombre) — solo high/med-confidence y completas
- Email recap a participantes internos (∩ allowlist)
- **Nunca** escribe en `cadence/decision_log.md`

**Prompt:** `scripts/prompts/mine-prompt.md` · workflow humano: `capabilities/workflows/WF_OPS_MINE.md`

**Frecuencia:** on-demand / event (por reunión)

**Tiempo estimado V1:** ~1–2 min de Action

---

## Señales de que funcionó

- Job verde; job summary con counts de decisiones/riesgos/action items
- Recap committeado en `cadence/meetings/`, cada ítem con `source_quote`
- Tareas creadas en Asana sin duplicar; recap solo a internos

## Señales de que falló

- Job rojo en el quality gate (transcript corrupto) — correcto: no minó basura
- Ítems sin `source_quote` en el output (no debería pasar — se descartan en validación)
- Tareas duplicadas en Asana (revisar dedup por nombre) o recap a un externo (revisar allowlist)

## Última ejecución

W__ · [fecha] — (sin corridas aún)
