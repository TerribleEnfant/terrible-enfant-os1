# Estilo "minimal cards" — sistema visual para documentos

> Sistema visual oficial de TE para **documentos de research y presentación** (informes, análisis,
> 1-pagers, decks-en-web). No reemplaza la voz de marca (`brand-bible.md`) — es la capa **visual** de
> los documentos. La voz sigue siendo la del brand-bible; esto define cómo se ven.
>
> **Procedencia.** Inspirado en sitios tipo *Habillage Graphique* y *Joshua Kaplan* — neo-grotesque
> técnico, suizo, de alto contraste. Estrenado en el informe E-commerce BRA (jun 2026).
>
> **Gobernanza.** Este doc vive en `context/identity/` (dominio de **Comando**). Cambios al sistema
> requieren su visto bueno.

---

## Cuándo usarlo

- Informes de research, análisis de decisión, due diligence.
- 1-pagers y resúmenes ejecutivos.
- Presentaciones entregadas como página web (no PDF/slides).
- Documentos internos o externos que se publican en GitHub Pages.

No usarlo para contenido de campaña/marca (eso lo rige la brand-bible y aprueba Comando aparte).

---

## Principios

1. **Minimal y técnico.** Espacio en blanco, precisión, nada decorativo. La estructura es la información.
2. **Sin serif.** Grotesca neutra (Inter) para todo; mono (IBM Plex Mono) solo para micro-datos.
3. **Blanco y negro + acentos pastel semánticos.** El color significa algo, no decora.
4. **Hairlines.** Líneas finas negras separan filas y secciones — el look "ficha técnica".
5. **Cards redondeadas sobre negro.** Cada sección es una tarjeta blanca (radius 22px) sobre fondo negro.
6. **Numerales grandes** por sección (00, 01, 02…). Pills redondeadas para nav (`→`) y estados.
7. **Toda sigla se explica.** Glosario obligatorio al pie, o inline la primera vez. Sin excepción.

---

## Tokens

| Token | Valor | Uso |
|-------|-------|-----|
| `--page` | `#0a0a0a` | fondo (negro) |
| `--ground` | `#ffffff` | tarjetas |
| `--ink` | `#0d0d0d` | texto, hairlines |
| `--gray` | `#6b6b6b` | texto secundario, labels |
| `--soft` | `#e2e2e2` | hairlines internas suaves |
| `--mint` | `#aeebc4` | **positivo / confirmado / a favor** |
| `--lime` | `#e7ff5a` | **atención / abierto / pendiente** |
| `--coral` | `#ff7a66` | **negativo / refutado / en contra** |
| `--ink` (fill) | `#0d0d0d` | estado duro / "gate" / abierto |
| `--radius` | `22px` | tarjetas (16px componentes internos) |

**Tipografía.** Display + body + labels: **Inter** (400/500/600/700/800). Micro-datos (números,
códigos, siglas, fechas, URLs): **IBM Plex Mono** (400/500). Jerarquía por peso/tamaño/tracking, no
por familia. Tracking de títulos negativo (`-.02` a `-.04em`); labels en mayúscula con `+.07em`.

**Color semántico — regla.** mint = a favor · lime = atención/abierto · coral = en contra/refutado ·
pill negra sólida = estado duro o "gate". Pill con solo borde = neutral/categoría.

---

## Componentes

- **`.card`** — tarjeta blanca redondeada; una por sección.
- **`.bar`** — header de tarjeta: label a la izquierda, meta (fecha/código) a la derecha, hairline abajo. (Motivo "Informations / ✕".)
- **`.code`** — fila de código/etiqueta grande bajo el header.
- **`.statement`** — titular grande y tight (la tesis).
- **`.shead` + `.snum`** — número de sección grande + título.
- **`.pill`** — botón redondeado; nav con `→`. Variantes `.mint/.lime/.coral/.ink`.
- **`.tag`** — pill chica de estado/confianza dentro de tablas (en mono).
- **`.chip`** — etiqueta de tópico (mayúscula) para separar bloques.
- **Tablas** — hairline negra por fila; `th` mayúscula gris; números en mono (`.num`).
- **`.scard`** (scenario cards) — comparación lado a lado; la opción favorable va resaltada (`.hi`, fondo mint).
- **`.path`** — bloques de opción con `+`/`–`; la recomendada con `.hi` (borde grueso) + pill "recomendado".
- **`.note`** / **`.note.verdict`** — callout; el veredicto va en negro sólido con label en lime.
- **`.urlbar`** — barra final con `🔒` + URL, en mono.
- **`.up`** — botón circular flotante "↑ volver arriba".

---

## Reglas de producción

- **Glosario de siglas** obligatorio (ver principio 7).
- **`<meta name="robots" content="noindex, nofollow">`** en toda página publicada.
- **Self-contained:** fuentes vía Google Fonts; sin otras dependencias externas salvo que se justifique.
- **Verificar el render** (headless Chrome / screenshot) antes de publicar — no publicar a ciegas.
- **Accesibilidad:** `:focus-visible` visible, `prefers-reduced-motion` respetado, contraste alto.
- **Responsive + print:** columnas colapsan en móvil; `@media print` para 1-pagers (fondo blanco, sin botón flotante, `break-inside: avoid`).
- **Idioma:** español; tokens estructurales y siglas técnicas en su forma original (con glosario).

---

## CSS base reutilizable

Copiar este bloque en `<style>` y construir con los componentes de arriba.

```css
:root{
  --ink:#0d0d0d;--ground:#ffffff;--page:#0a0a0a;--soft:#e2e2e2;--gray:#6b6b6b;
  --mint:#aeebc4;--lime:#e7ff5a;--coral:#ff7a66;--radius:22px;
  --sans:"Inter",system-ui,"Helvetica Neue",Arial,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font-family:var(--sans);font-weight:400;
  line-height:1.5;font-feature-settings:"tnum" 1;letter-spacing:-.011em;
  -webkit-font-smoothing:antialiased;padding:18px 14px 90px}
.shell{max-width:840px;margin:0 auto}
.card{background:var(--ground);border-radius:var(--radius);padding:32px 36px;margin:0 0 14px}
.rule{height:1.5px;background:var(--ink);margin:18px 0}
.bar{display:flex;justify-content:space-between;align-items:center;gap:14px}
.bar b{font-size:19px;font-weight:600;letter-spacing:-.02em}
.bar .x{font-family:var(--mono);font-size:13px;color:var(--gray)}
.code{font-size:21px;font-weight:600;letter-spacing:-.01em}
.statement{font-size:clamp(29px,6.2vw,52px);font-weight:700;line-height:1.0;letter-spacing:-.03em;margin:0}
.statement em{font-style:normal;color:var(--gray)}
.shead{display:flex;align-items:baseline;gap:18px;margin:0 0 6px}
.snum{font-size:clamp(30px,6vw,44px);font-weight:700;letter-spacing:-.04em;line-height:.85}
.shead h2{font-size:clamp(20px,3.2vw,29px);font-weight:700;letter-spacing:-.025em;margin:0}
.pill{display:inline-flex;align-items:center;gap:7px;border:1.5px solid var(--ink);border-radius:999px;
  padding:8px 16px;font-size:14px;font-weight:500;line-height:1;white-space:nowrap;color:var(--ink);text-decoration:none}
.pill.mint{background:var(--mint);border-color:transparent}
.pill.lime{background:var(--lime);border-color:transparent}
.pill.coral{background:var(--coral);border-color:transparent}
.pill.ink{background:var(--ink);color:#fff}
.tag{display:inline-flex;align-items:center;border:1.4px solid var(--ink);border-radius:999px;
  padding:3px 11px;font-size:12px;font-weight:500;font-family:var(--mono);letter-spacing:-.02em;white-space:nowrap}
.tag.mint{background:var(--mint);border-color:transparent}
.tag.lime{background:var(--lime);border-color:transparent}
.tag.coral{background:var(--coral);border-color:transparent}
.tag.ink{background:var(--ink);color:#fff}
table{width:100%;border-collapse:collapse;font-size:14.5px}
th{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.07em;color:var(--gray);
  text-align:left;padding:0 14px 11px 0;border-bottom:1.5px solid var(--ink)}
td{padding:13px 14px 13px 0;border-bottom:1px solid var(--ink);vertical-align:top;line-height:1.38}
.num{font-family:var(--mono);font-size:13.5px;letter-spacing:-.02em;white-space:nowrap}
.note{border:1.5px solid var(--ink);border-radius:14px;padding:16px 20px;margin:18px 0;font-size:14.5px;line-height:1.45}
.note.verdict{background:var(--ink);color:#fff;font-size:16px}
.note .lbl{font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--gray);display:block;margin-bottom:6px}
.note.verdict .lbl{color:var(--lime)}
.urlbar{display:flex;align-items:center;justify-content:center;gap:8px;margin-top:18px;padding-top:16px;
  border-top:1.5px solid var(--ink);font-family:var(--mono);font-size:13px}
@media print{body{background:#fff;padding:0}.card{margin:0 0 8px;break-inside:avoid;border:1px solid var(--soft)}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
```

Fuentes: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap`

---

## Ejemplos en vivo

- Informe completo — E-commerce BRA: `cadence/operations/BRA/ecommerce/` → GitHub Pages `ecommerce-jet-sanders.html`
- 1-pager — Caso JET: GitHub Pages `ecommerce-jet-1pager.html`

*Glosario: TE = Terrible Enfant · OS1 = sistema operativo de archivos (este repo).*
