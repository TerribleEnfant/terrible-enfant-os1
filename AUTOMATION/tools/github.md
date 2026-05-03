# Herramienta: GitHub

**Owner:** Boris
**Propósito:** fuente de verdad del OS. Versionado, sync y acceso del equipo no-técnico.

---

## Para el equipo no-técnico (Fanny, Comando, Hache)

No hace falta saber Git. Para editar un archivo directamente en GitHub web:

1. Ir a [github.com](https://github.com) y abrir el repo
2. Navegar hasta el archivo que querés editar (ej: `OPERATIONS/ARG/marketing-comms/STATUS.md`)
3. Hacer clic en el ícono del lápiz (✏️) arriba a la derecha
4. Editar el contenido
5. Al terminar: bajar a "Commit changes" → escribir una línea descriptiva → "Commit directly to main"

**No rompe nada.** El historial guarda todas las versiones.

## Para Boris (Claude Code en VS Code)

- Trabajo local en el repo clonado
- Push a `main` directamente (no hay branches)
- Claude Code tiene acceso completo al repo para leer y escribir

## Estructura de commits

Convención de mensajes de commit:
```
[área] acción — descripción breve
```
Ejemplos:
- `[OS1] Update STATUS — ARG marketing-comms W18`
- `[PROJECTS] Add collab-edgar — brief inicial`
- `[AUTOMATION] Add agent spec — project-status-roller`

## Quién tiene acceso

- Boris: admin + Claude Code
- Fanny: write (edición web)
- Comando: write (edición web)
- Hache: read (consulta)
- Freequency / Tiago: (a definir en V2 — necesitan write para sus STATUS.md)
