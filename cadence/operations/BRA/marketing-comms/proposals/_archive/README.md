# _archive/ — docs en pausa o cerrados

Convención para sacar de circulación documentos sueltos (propuestas, borradores, one-offs) sin
borrarlos. Mantiene limpia la carpeta activa y preserva el registro.

## Cuándo

- **parked** — pausado, **reversible**, puede volver. Tiene un disparador de revival conocido.
- **archived** — cerrado, superado o descartado. Sólo registro histórico.

## Cómo

1. Stampear el frontmatter del doc:
   ```yaml
   estado: parked        # o: archived
   parked:               # bloque sólo si está parked
     fecha: YYYY-MM-DD
     motivo: <una línea>
     revisar_si: <qué lo reactiva>
   ```
2. Mover el archivo a este `_archive/` (`git mv` si ya está trackeado; `mv` si es nuevo/untracked).
3. Si está referenciado desde otro doc, dejar el link `[[...]]` — sigue resolviendo.

## Relación con otros ciclos del OS

- **Proyectos** usan `cadence/projects/{pipeline,active,completed}/` (mueven carpeta).
- **Knowledge/OS-design** usa `status: archived` en frontmatter y queda en `context/knowledge/`.
- Esto cubre el hueco para **propuestas y docs sueltos** de `operations/`.

> Si esta convención se adopta en todo el repo, promoverla al boot spec (`TE-OS_M1.md`) en un
> incremento de Mark con changelog — no acá.
