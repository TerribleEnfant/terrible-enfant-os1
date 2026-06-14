# Terrible Enfant | OS1

Sistema Operativo de Terrible Enfant — documentación viva, coordinación operacional y archivo institucional.

**Versión:** Mark I · 4C · Junio 2026 (migrado al COMANDO Canon)  
**Mercados activos:** Argentina · Brasil (lanzamiento)

---

## Para empezar

Si eres nuevo en este repo, lee en este orden:

1. [CLAUDE.md](CLAUDE.md) — el Charter (puntero de runtime para Claude Code)
2. [TE-OS_M1.md](TE-OS_M1.md) — el boot spec: arquitectura, equipo, cadencia, routing
3. [context/identity/team-structure.md](context/identity/team-structure.md) — quién hace qué
4. [cadence/operations/](cadence/operations/) — encuentra tu área y mercado

---

## Estructura rápida — el modelo 4C

El OS se organiza en cuatro capas (Context · Connections · Capabilities · Cadence):

| Carpeta | Capa | Contenido | Quién escribe |
|---------|------|-----------|---------------|
| [context/](context/) | **Context** (estático) | ADN de marca (`identity/`), estrategia (`strategy/`), conocimiento/legacy (`knowledge/`) | Hache · Comando |
| [connections/](connections/) | **Connections** (vivo) | Integraciones como `TL_*` (GitHub, Asana, Drive, Nuvemshop, Meta Ads…) | Boris |
| [capabilities/](capabilities/) | **Capabilities** | Agentes (`AG_*`), workflows (`WF_*`), skills registry | Boris |
| [cadence/](cadence/) | **Cadence** (vivo) | Pulse, decision_log, logs, runbook + `operations/` (áreas) · `projects/` · `weekly/` | Líderes de área · Boris |

> Tokens funcionales (AREA): **CORE / OPS / PROJ / MKT**. El mercado (ARG/BRA) es una
> sub-dimensión de carpeta dentro de `cadence/operations/`, no un token. Detalle: `TE-OS_M1.md`.

---

## Cómo actualizar tu área (sin saber Git)

Cada área tiene un archivo `STATUS.md`. Para actualizarlo desde el navegador:

1. Navega a tu carpeta: `cadence/operations/ARG/` o `cadence/operations/BRA/` + tu área
2. Abre el archivo `STATUS.md`
3. Haz click en el ícono de lápiz (Edit this file) en GitHub
4. Completa los campos
5. Haz click en **Commit changes** → **Commit changes** (dejá el mensaje por defecto)

Listo. No necesitas saber Git.

**Deadline operacional:** Lunes antes de las 18:00.

Si sos owner de un proyecto en `cadence/projects/active/`, actualizá también tu `STATUS.md` en esa carpeta con el mismo deadline.

---

## Cadencia semanal

```
Lunes   → Líderes actualizan STATUS.md (antes 18:00)
Martes  → Reunión semanal (45 min · solo decisiones)
Martes PM → Fanny publica decisiones en decisions log
Mié–Vie → Ejecución
```

---

## Contacto / Preguntas

- Dudas sobre el sistema → Boris
- Dudas sobre tareas → Fanny
- Dudas sobre marca → Comando
- Decisiones de negocio → Hache
