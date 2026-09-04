# transcripts/

Transcripts crudos de reuniones. **Cada archivo es a la vez el trigger y el archivo permanente.**

Commitear un `.md` acá dispara `WF_OPS_MINE` (GitHub Action `mine-meeting`): quality gate → un
call a Claude (structured output) → escribe el recap + ítems en `cadence/meetings/` → crea tareas
en Asana → emailea el recap a los participantes internos.

## Convención de nombre

```
transcripts/<YYYY-MM-DD>-<slug>.md
ej: transcripts/2026-06-20-comando-semanal.md
```

El prefijo de fecha se usa como fallback si el transcript no trae fecha en su contenido.

## Force-mine (on-demand)

Para minar a mano un texto/transcript: commitealo acá y corré la Action vía **workflow_dispatch**
con el `path`. Inputs disponibles: `force` (saltea quality gate), `skip_asana`, `skip_email`.

Audio: **fase 2** (se agrega un paso de transcripción Whisper/Deepgram). Por ahora, pasá texto.

## Qué NO va acá

- El output minado → `cadence/meetings/` (lo genera la Action).
- Decisiones curadas por humanos → `cadence/decision_log.md` (el miner nunca lo toca).
