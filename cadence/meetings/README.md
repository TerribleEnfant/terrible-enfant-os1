# cadence/meetings/ — machine store del auto-miner

Salida **generada por máquina** de `WF_OPS_MINE`. No editar a mano: se sobrescribe en cada corrida
(idempotente por nombre de archivo).

```
cadence/meetings/
├── <YYYY-MM-DD>-<slug>.md      ← recap legible (decisiones / riesgos / action items)
├── <YYYY-MM-DD>-<slug>.json    ← salida estructurada (alimenta Asana + email)
├── decisions/<base>-<n>.md     ← una decisión por archivo
└── risks/<base>-<n>.md         ← un riesgo por archivo
```

Cada ítem lleva **cita textual** (`source_quote`) + **confianza** (high/medium/low).

## Relación con el decision_log

Este store es **separado** de `cadence/decision_log.md`. El log es humano, append-only y curado
por Fanny. El miner **nunca** escribe ahí. Si una decisión minada amerita entrar al log oficial,
una persona la promueve (curación manual). Así un mal minado no contamina la fuente de verdad.
