# Workflow: WF_OPS_MINE — minado de reuniones

**Trigger:** commit de un transcript en `transcripts/**.md` (o `workflow_dispatch` para force-mine/backfill)
**Dueño del proceso:** Boris
**Participantes:** sistema (GitHub Actions) · Fanny (curaduría del board Asana) · participantes de la llamada (recap)
**Frecuencia:** por reunión / on-demand
**Tiempo estimado:** ~1–2 min

> Agente: `capabilities/agents/AG_OPS_MINER.md`. Conexión: `connections/TL_OPS_MINER.md`.
> Estado/contrato del NLAH: plan → execute → verify → repair, outcome **binario** (ok | failed).

---

## Pasos

### 1. Capture

**Quién:** participante de la llamada (Read AI graba) / cualquiera del equipo
**Cuándo:** al terminar la reunión
**Cómo:** obtener el transcript (de Read AI) y commitearlo como `transcripts/<YYYY-MM-DD>-<slug>.md`.
En fase 2 esto lo dispara el webhook de Read AI automáticamente.
**Output:** transcript crudo versionado (trigger + archivo permanente)

### 2. Quality gate

**Quién:** Action
**Cómo:** si >50% de las líneas con contenido no tienen speaker atribuido → **falla fuerte** y no
mina (un transcript corrupto fabrica contenido). `workflow_dispatch force=true` puede saltearlo (logueado).
**Output:** pasa, o job rojo sin tocar nada

### 3. Mine

**Quién:** Action → un call a Claude (structured output / tool-use)
**Cómo:** extrae decisiones / riesgos / action items con `source_quote` + `confidence` cada uno,
según las reglas de `scripts/prompts/mine-prompt.md`. Validación en código (cita obligatoria, cap, completitud).
**Output:** objeto estructurado validado

### 4. Store

**Quién:** Action
**Cómo:** escribe `cadence/meetings/<base>.{md,json}` + ítems por archivo, y **commitea de vuelta**.
**Output:** machine store versionado (idempotente; nunca toca `decision_log.md`)

### 5. Asana

**Quién:** Action (`scripts/asana_push.py`)
**Cómo:** crea en el board live solo action items completos (owner+deliverable+deadline) y
confidence ≥ medium, dedup por nombre. Fanny cura desde ahí.
**Output:** tareas creadas (o dedup/descartadas, con detalle en el job summary)

### 6. Recap

**Quién:** Action (`scripts/send_recap.py`)
**Cómo:** emailea el recap (Resend) a participantes ∩ allowlist interna; externos descartados;
sin internos → no manda.
**Output:** email enviado a internos, o skip logueado

---

## Criterios de éxito

- Job verde con counts en el job summary; recap committeado; cada ítem con `source_quote`.
- Tareas en Asana sin duplicar; recap solo a participantes internos.
- Re-correr el mismo transcript sobrescribe, no duplica.

## Errores comunes y cómo resolverlos

| Problema | Causa probable | Solución |
|---------|---------------|---------|
| Job rojo en quality gate | transcript con pocas líneas atribuidas | corregir el transcript; o `force=true` si es legítimo |
| Falta `ANTHROPIC_API_KEY` | secret no configurado | cargar el GitHub Actions secret (espejo de 1Password) |
| Tarea duplicada en Asana | nombre cambió entre corridas | el dedup es por nombre normalizado; mantener títulos estables |
| Recap no llega | nadie interno en la llamada, o `email.from`/dominio en TODO | revisar allowlist y config de Resend |
| Falla el commit de vuelta | permisos del token | `permissions: contents: write` en el workflow |
