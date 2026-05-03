# Guía — Asana Task Board

Cómo funciona la gestión de tareas en Terrible Enfant. Este documento existe para que todos entiendan el sistema sin necesidad de que se les explique cada vez.

---

## La regla fundamental

**Si no está en Asana con responsable y deadline, no existe como tarea.**  
**Si no está en el decisions log de este repo, no existe como decisión.**

---

## Propiedades de cada tarea en Asana

| Campo | Tipo | Valores posibles |
|-------|------|-----------------|
| Tarea | Título | Descripción accionable ("Enviar brief EDGAR a Freequency") |
| Área | Select | Finance & Admin · Legal · Producto · Operations · Logistics · Marketing |
| Mercado | Select | ARG · BRA · Ambos |
| Responsable | Persona | Un solo responsable (no grupos) |
| Status | Select | Por hacer · En curso · Bloqueada · Completada · Cancelada |
| Prioridad | Select | Alta · Media · Baja |
| Deadline | Fecha | Siempre con fecha específica |
| Origen | Select | Weekly Report · Sync · Decisión directa |

---

## Quién hace qué

| Acción | Quién |
|--------|-------|
| Crear tareas en el Task Board | Solo Fanny |
| Actualizar el status de una tarea | El responsable de esa tarea |
| Marcar una tarea como completada | El responsable + notificación a Fanny |
| Cancelar una tarea | Fanny (previa consulta con el owner del área) |
| Crear subtareas o dependencias | Fanny |

Los líderes de área **reportan** en su STATUS.md semanalmente. Fanny **traduce** esos reportes a tareas en Asana si corresponde.

---

## Flujo semanal

```
Líder de área
  └─ Actualiza STATUS.md (lunes antes 18:00)
       └─ Boris compila STATUS en reporte (lunes PM)
            └─ Reunión martes: se toman decisiones
                 └─ Fanny crea/actualiza tareas en Asana (martes PM)
                      └─ Responsables ejecutan (mié-vie)
```

---

## Prioridades — cómo asignarlas

- **Alta:** Bloquea otra tarea, tiene deadline esta semana, o es un riesgo legal/financiero
- **Media:** Importante pero no urgente, deadline en las próximas 2 semanas
- **Baja:** Nice-to-have, puede moverse sin impacto operacional

---

## Status — cómo usarlos

| Status | Cuándo usarlo |
|--------|--------------|
| Por hacer | La tarea existe pero no se empezó |
| En curso | Se está ejecutando activamente esta semana |
| Bloqueada | No se puede avanzar — especificar el bloqueador en comentarios |
| Completada | Terminada y verificada |
| Cancelada | Se decidió no hacerla — documentar por qué en comentarios |

---

## Lo que este repo y Asana hacen juntos

| Sistema | Para qué |
|---------|---------|
| Asana | Tareas con deadline y responsable · seguimiento de ejecución |
| Este repo | Contexto · narrativa de estado · decisiones · KPIs · archivo institucional |

No duplicar información. Si algo está en Asana, el STATUS.md referencia el estado ("ver Asana"), no lo copia campo por campo.
