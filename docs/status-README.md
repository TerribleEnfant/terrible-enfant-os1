# Tablero de Estado — `docs/status.html`

Dashboard de una sola página que comunica el estado de Terrible Enfant en seis dominios:
**Estrategia · Concepto · Producto · Comunicación · Señal social · Máquina**.

Tema visual: **"Ficha Técnica Editorial"** — merge de los dos sistemas visuales de TE:
[`context/identity/minimal-cards.md`](../context/identity/minimal-cards.md) (grilla negra + cards
blancas + acentos semánticos mint/lime/coral) y el registro editorial de las páginas de campaña
(hero chiaroscuro con Fraunces). Autocontenido: un solo archivo, CSS + JS inline, fuentes vía
Google Fonts. Sin build, sin framework, sin dependencias.

---

## Publicar en GitHub Pages

Pages **ya está configurado** en este repo (rama `main`, carpeta `/docs`). No hay que tocar nada de
config. El flujo es:

```bash
# 1. Revisar el render localmente (ver abajo)
# 2. Boris revisa los cambios  ← requerido por CLAUDE.md antes de cualquier commit
git add docs/status.html docs/status-README.md
git commit -m "[ops] Add status dashboard (docs/status.html)"
git push origin main
```

Al pushear a `main`, Pages republica solo. La URL queda:

```
https://terribleenfant.github.io/terrible-enfant-os1/status.html
```

`index.html` (el GTM São Paulo) queda intacto — este es un archivo aparte, no lo reemplaza.

## Ver en local

Es autocontenido y **funciona con `file://`** (los datos van embebidos, no hay `fetch`):

```bash
open "docs/status.html"          # macOS
```

Para verificar el render como en producción (headless, igual que la regla de `minimal-cards.md`):

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --virtual-time-budget=6000 --window-size=1440,2400 \
  --screenshot=/tmp/status.png "file://$PWD/docs/status.html"
```

---

## Modelo de datos (swappable)

Todo el contenido vive en un objeto `const DATA = {…}` al inicio del `<script>`. Para repuntar el
tablero a datos nuevos, **editás ese objeto** — no hace falta tocar el layout ni el CSS.

Cada dominio tiene esta forma (campos opcionales según lo que aplique):

```js
strategy: {
  num:"00", title:"Estrategia", code:"STR", updated:"2026-07-01",
  span:"span7",                                  // span4 | span5 | span6 | span7 | span8 (grilla 12-col)
  status:{ kind:"lime", label:"…" },             // kind ∈ mint | lime | coral | ink  (color semántico)

  // — métrica primaria (número grande): ring O num —
  metric:{ kind:"ring", pct:45, tone:"lime", cap:["título","subtítulo"] },
  // metric:{ kind:"num", num:"45", unit:"/3", tone:"ink", cap:["…","…"] },

  stats:[ {v:"1", unit:"/3", k:"etiqueta"},       // v numérico entero → cuenta con count-up
          {v:"585", k:"…", spark:[3,4,3,5,8,7,9]} ], // spark: sparkline opcional bajo el número
  ring:{ kind:"ring", pct:30, tone:"coral", cap:[…] },   // ring secundario opcional
  mlegend:[ {color:"var(--mint)", label:"…"} ],  // mini-leyenda de descomposición
  stepper:{ steps:[ {label:"armado", state:"done"}, {label:"live", state:"pend"} ] },
  timeline:{ points:[ {when:"Mar", tone:"lime"}, {when:"May", tone:"coral"} ] },
  chips:[ "…","…" ],                             // pills de tópico
  img:{ idx:"S/01–07", label:"…", dim:"4:5" },   // placeholder IMAGEN (ver abajo)
  empty:true,                                     // sparkline vacío honesto (sin datos)
  table:{ head:["…"], rows:[ ["a","b","estado","coral"] ] },
  stack:[ {t:"GitHub", lead:"source of truth"}, {t:"n8n", off:true} ],

  summary:"HTML corto — se muestra chico y gris al pie de la card",
  note:{ label:"…", text:"…", soft:true },        // callout; soft=borde / sin soft=negro sólido
  raw:{ … }                                        // objeto que muestra el botón { } (JSON crudo)
}
```

Orden de dominios y claves de `localStorage` en `const ORDER` y `const LS`.

### Colores semánticos (regla de marca — no decorar)
- `mint` = a favor / confirmado / ok
- `lime` = atención / abierto / pendiente
- `coral` = problema / crítico
- `ink` (pill negra sólida) = estado duro / gate / neutral

---

## Placeholders de imagen / GIF

Donde va una imagen o loop todavía no provisto, hay un marco con **crop-marks** (estilo contact
sheet) etiquetado `Imagen / GIF`. Para reemplazarlo por media real:

1. **Hero** (`.hero-visual .imgslot`): dropear un `<video autoplay muted loop playsinline>` o
   `<img>` self-hosted en `docs/`. Recomendado 4:3, loop editorial de *Estado de Gracia*.
2. **Concepto** (`img:{…}` en DATA): los 7 stills de arquetipo (Serie I–VII), vertical 4:5.

Mantener el archivo autocontenido: hospedar la media dentro de `docs/` (no CDN externo). Si se
agrega una carpeta de assets cuyo nombre arranca con `_`, sumar un `docs/.nojekyll` vacío.

---

## Interacciones

- **Toggles por dominio** — mostrar/ocultar cada card (persiste en `localStorage`).
- **Focus** — atenúa las cards no fijadas; fijás con el botón `◆` de cada card.
- **Colapsar todo** / colapso por card (`–`) — deja solo título + pill de estado.
- **`{ }`** — abre el JSON crudo del dominio en un diálogo.
- Entrada animada escalonada, count-up de números, relleno de rings y barras — todo respeta
  `prefers-reduced-motion`.

## Accesibilidad

HTML semántico; toggles con `aria-pressed` y operables por teclado; `:focus-visible` visible;
estados nunca solo por color (siempre con label de texto); contraste alto; `@media print`
(fondo blanco, sin controles). Glosario de siglas obligatorio al pie (regla `minimal-cards.md`).

## Gobernanza

- Superficie **interna** (`noindex, nofollow`). Renderiza datos de estrategia/marca pero es un
  artefacto de ops, no publicación de marca. Si se hace público o se comparte a externos, eso entra
  en dominio de **Comando** (aprobar aparte).
- **No commitear sin revisión de Boris** (CLAUDE.md). Sin secretos en disco.
- Datos: solo hechos verificados de los `STATUS.md`. `pulse.md`/`decision_log.md` están vacíos
  (scaffolds) — no representarlos como poblados. La fecha de full launch se muestra en su tensión
  real (abril soft / julio plan / DRE septiembre), no hardcodeada.

---
*Terrible Enfant · built on COMANDO Canon*
