# Herramienta: WhatsApp

**Owner:** todos
**Propósito:** comunicación interna en tiempo real

---

## Grupos activos

| Grupo | Participantes | Para qué |
|-------|--------------|---------|
| Ejecutivo TE | Hache, Comando, Fanny, Boris | Agenda del martes, alertas críticas, decisiones urgentes |
| (otros grupos a documentar) | | |

## Qué va por WhatsApp

- Alertas urgentes que no pueden esperar al martes
- Envío de la agenda del martes (Boris → grupo ejecutivo)
- Notificaciones de cambios importantes en el repo
- Coordinación operacional día a día

## Qué NO va por WhatsApp

- Decisiones formales → deben quedar en `cadence/decision_log.md`
- Contexto de proyectos → `cadence/projects/`
- Estado de áreas → `cadence/operations/`

**Regla:** si algo se decide por WhatsApp, Fanny o Boris lo documentan en el decisions log para que quede en el OS.

---

## Auth (1Password)

> Convención del Canon: los secretos nunca van al repo. 1Password es el vault de record;
> se inyectan en runtime vía `op`. Documentar acá solo el **nombre del item**, nunca el valor.

- **Vault item:** `TODO: vault ref` — completar con el nombre del item en el vault de TE.
