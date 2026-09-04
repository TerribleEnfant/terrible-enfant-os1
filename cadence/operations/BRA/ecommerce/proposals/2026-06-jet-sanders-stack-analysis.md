# Análisis — Stack JET + Sanders + DRE (E-commerce BRA)

> Digest consolidado del paquete recibido el **19/06/2026**, archivado en [`../JET PROPOSAL/`](../JET%20PROPOSAL/).
> Tres archivos, un mismo caso de negocio: una plataforma (JET), una agencia de performance (Sanders) y un modelo financiero a 3 años (DRE) que ya trae los costos de ambos embebidos.
> Fecha: 2026-06-22 · Owner: Boris · Estado: **digest para decisión — nada aprobado, nada firmado, nada comprometido.**
>
> **Contexto que manda sobre todo el análisis: el canal D2C de BRA es _greenfield_.** TE no tiene tienda en vivo en Brasil. La "plataforma Nuvemshop" que figura en los docs era la *propuesta* de Lucas Godoy — **nunca se empezó a implementar**. Por lo tanto, esto **NO es un replatform**: no hay tienda que migrar, ni inversión hundida que abandonar. La decisión es limpia: **sobre qué plataforma y con qué proveedor(es) construir el canal desde cero.**

---

## Lectura ejecutiva

El paquete propone **construir el canal D2C de Brasil** sobre la plataforma de JET, con Sanders cubriendo medios, respaldado por un modelo financiero que dice que el canal llega a breakeven al ~mes 10 y deja 7% de margen del año 2 en adelante.

Como nada está construido todavía, esto es una **selección de plataforma + proveedor**, comparable contra la propuesta —también nunca arrancada— de Lucas Godoy sobre Nuvemshop. En plata, el stack JET+Sanders es **dramáticamente más barato**: del orden de 3× menos cash en año 1, sin diluir equity. Las condiciones que mandan sobre ese número:

1. **Es una decisión greenfield, no un replatform.** No hay nada construido en BRA, así que elegir JET no abandona ninguna inversión ni dispara costo de migración — solo elige sobre qué construir. Lo que **sí** queda en pie es la **portabilidad futura**: JET es plataforma **propietaria y cerrada**, de modo que salir más adelante sí sería una migración. Eso es pérdida de opcionalidad a futuro, no costo hundido hoy — un peso real, pero más liviano que un replatform. (Es la misma categoría —plataforma propia— por la que el research de junio desclasificó a WX3; JET tampoco estaba en ese shortlist.)
2. **El caso financiero vive o muere por un solo número: el margen bruto (CMV).** El propio DRE trae dos escenarios; a 50% de CMV el canal es marginalmente rentable, a 70% **pierde los tres años**. Antes de cualquier otra cosa hay que clavar el margen bruto real de TE en Brasil (impuestos, importación, ICMS). Es agnóstico a la plataforma.
3. **La diligencia ya corrió — y debilita a ambos proveedores.** Un deep research (22 jun, abajo § Diligencia) confirma que JET tiene mal fit (enterprise/rígido, vitrine sin lujo, defectos documentados, antigüedad "1999" no comprobada) y que Sanders es en realidad un shop de **CRO, no de paid media**, sin portfolio de moda ni credenciales verificables. Sumado a un **DRE sell-side** (escenario base "Terrible", optimista), el research **inclina el fork hacia Nuvemshop + una agencia vetada (Wave Commerce)**.

**Recomendación de proceso (no de decisión):** no firmar nada. Antes — (a) Hache valida el margen bruto real y corre el DRE con números propios; (b) Boris elige **sobre qué plataforma construir** — y la diligencia inclina la balanza hacia **Nuvemshop + Wave Commerce** (verificada fuerte) por encima de JET+Sanders; (c) Nacho revisa lock-in, rescisión y propiedad de datos si JET sigue en carrera; (d) confirmar referencias directas de cualquier proveedor antes de contratar (la diligencia es de fuentes públicas, no de clientes hablados).

---

## Las tres piezas

### 1. JET — plataforma + implementación

**Qué es:** JET Tecnologia em Comércio Eletrônico LTDA (São Paulo, Av. Paulista). Plataforma de e-commerce **propietaria** (SaaS), con marketplaces vía Anymarket, módulo omnichannel propio (JET Omni) y hub de APIs (JET Hub).

**Setup (one-shot):**

| Ítem | Valor |
|------|-------|
| Onboarding | R$ 8.000 |
| Layout Personalizado | R$ 8.000 |
| Treinamento Exclusivo | R$ 4.000 |
| Implementação JET Omni | R$ 5.000 |
| Implementação JET Hub | R$ 3.000 |
| **Total** | **R$ 28.000** |
| **Total con descuento** | **R$ 22.400** |

Parcelable en 6× sin interés. Prazo de implantación: **90 días post-aprobación del layout** (no desde la firma).

> Nota greenfield: el "Pacote migração" de JET (importación de productos, imágenes, redirects 301, base de clientes) presupone migrar desde una tienda existente. TE BRA no tiene una. Confirmar qué compra realmente ese alcance para una tienda nueva (¿carga de catálogo desde planilla / desde ARG?) y si parte del setup es prescindible.

**Mensualidad — dos niveles:**

| Nivel | Fijo | Variable | Incluye |
|-------|------|----------|---------|
| Tecnología | **R$ 2.000** | **1,5% s/ ventas concluidas + 1,0% JET Hub** (≈ 2,5% s/ GMV) | Hosting SLA 99,9%, soporte 24/7 (ticket/teléfono/WhatsApp horario comercial), APIs, MultiCDN, 3 meses gratis de servicios profesionales (10 h/mes post-Go-Live) |
| Estratégico | **R$ 6.000** | (mismo esquema) | Lo anterior + reuniones semanales + acompañamiento estratégico (metas trimestrales/anuales, conversión, ticket medio, carrito abandonado, cohortes de clientes) |

**No incluye** (costo extra / responsabilidad del cliente): cadastro de productos, producción de fotos/textos/videos, integraciones con sistemas de terceros (ej. ERP). Vencimiento mensual día 15 del mes siguiente.

### 2. Sanders — performance / paid media

**Qué es:** agencia de marketing de performance (Google Ads, Meta/Instagram Ads, SEO, e-mail/CRM, B.I & Google Analytics), 80+ clientes. Complementa a JET — cubre la capa de medios que JET explícitamente no toca. Su documento se dirige a "Terrible Ele**f**ant" (señal menor de prolijidad).

| Verba (inversión en medios) | Fee de gestión |
|-----------------------------|----------------|
| Hasta R$ 50.000 | **R$ 4.500/mes** |
| Hasta R$ 100.000 | R$ 8.000/mes |
| Más de R$ 100.000 | R$ 12.000 fijo |

Total propuesto: **R$ 4.500/mes** (tier de entrada). Contrato **12 meses, sin multa rescisória.** Validez de la propuesta: 30 días.

### 3. DRE — modelo financiero a 3 años

Proyección mensual (régimen LUCRO REAL), inicio sep-2026, dos escenarios. La única diferencia estructural relevante entre ellos es el **CMV (costo de mercadería vendida)**.

| | Escenario "Terrible" (CMV 50%) | Cenário 1 (CMV 70%) |
|--|-------------------------------|---------------------|
| Faturamento Año 1 | R$ 1,32 M | R$ 1,09 M |
| Resultado líquido Año 1 | **−R$ 28,9 k** (−2,2%) | **−R$ 202,3 k** (−18,6%) |
| Resultado líquido Año 2 | +R$ 262,9 k (7,2%) | −R$ 375,1 k |
| Resultado líquido Año 3 | +R$ 273,5 k (7,2%) | −R$ 406,5 k |
| Breakeven | ~mes 10 (jun-2027) | nunca |

Costos operativos embebidos (mensual, base): Plataforma JET ~R$ 2.500 · Estrategia Ecommerce R$ 8.000 · Marketing ~R$ 7.000 (Infra/SEO R$ 4.500 + compra de medios R$ 2.000 + fotos R$ 500). Más variables % sobre ventas: pagos 3%, atendimiento 3%, reversa 2%, marketplace 15-20%.

---

## Condiciones comerciales — JET+Sanders vs. Lucas Godoy

Ambas son propuestas para construir **desde cero**: ninguna se implementó. Cifras de Lucas Godoy tomadas del [cronograma](2026-03-lucas-godoy-cronograma.md) (Service Agreement v17), no del resumen del README.

| Dimensión | Stack JET + Sanders | Lucas Godoy |
|-----------|---------------------|-------------|
| **Plataforma de construcción** | JET propia (SaaS cerrada) | Nuvemshop (la prevista originalmente) |
| **Setup (one-shot)** | R$ 22.400 (JET, c/desc.) | R$ 61.200 |
| **Fijo mensual** | R$ 6.000 (JET estratégico) + R$ 4.500 (Sanders) = **R$ 10.500** | **R$ 36.390** (Módulos III-VIII) |
| **Variable s/ ventas** | ≈ 2,5% s/ GMV (JET) | **Take Rate 15% / 14% / 12%** s/ GMV por tramos |
| **Equity** | — (ninguno) | **3%** en 4 tramos + Quotaholders' Agreement (D+60) |
| **Medios/performance** | Cubierto por Sanders (+ presupuesto de verba aparte) | Incluido (Módulo VI, piso R$ 5.600 + USD 2.000 de verba) |
| **SLA** | 24/7 vía ticket; teléfono/WhatsApp horario comercial | 8 h hábiles standard / 4 h urgente |
| **Proveedores** | Dos (coordinación a cargo de TE) | Uno (orchestration incluida) |
| **Portabilidad futura** | Baja — plataforma propietaria; salir después = migración | Mayor — Nuvemshop es estándar |
| **Vetado vs. brief research** | No | Es el contractor que el research buscaba reemplazar |

**Costo indicativo Año 1** (aproximado, fijo + setup + variable estimado sobre ~R$ 1,3 M de GMV; **no es apples-to-apples** — alcances difieren): stack JET+Sanders ≈ **R$ 180 k** · Lucas Godoy ≈ **R$ 558 k** (excl. valor del 3% de equity).

El factor que domina la diferencia es el **variable**: 2,5% vs. 12-15% sobre GMV es, en sí mismo, una brecha de seis cifras anuales. Visto al revés: dado lo ajustado que el propio DRE muestra el año 1, la estructura de costos barata del stack JET+Sanders es probablemente **condición necesaria** para que el canal cierre — con la estructura de Lucas Godoy encima, el DRE empeora materialmente.

---

## El DRE bajo la lupa

El modelo es el argumento de venta del paquete, y hay que leerlo como tal.

- **El CMV es el pivote único.** 50% → marginalmente rentable; 70% → pérdida los tres años. No es un detalle de sensibilidad: es la decisión. **Validar el margen bruto real de TE en Brasil es el paso #1**, antes que cualquier comparación de proveedores.
- **ROAS ramp 5 → 7,39.** El modelo asume que cada real de medios devuelve de 5× a 7,4× en ventas, creciendo. Para una marca de lujo en lanzamiento, es una hipótesis optimista; si el ROAS real arranca más abajo, el año 1 se hunde más.
- **Ticket medio R$ 1.500 (Terrible) / R$ 1.200 (Cenário 1)** y **conversión 1%** sobre visitas institucionales — coherentes con lujo, pero son supuestos, no datos.
- **El arranque en sep-2026 es revelador.** El DRE no modela un launch en julio: arranca en septiembre. Eso es consistente con construir desde cero ahora con un build de ~90 días (la ventana de JET), que cae a fin de septiembre. Conclusión: **el full launch de julio 2026 (brand-bible) no es alcanzable arrancando un build hoy con ninguna de las dos vías** — la fecha de launch hay que reconciliarla con el build elegido.
- **Reconciliación con las propuestas:** el DRE pone "Plataforma JET" en ~R$ 2.500/mes (entre el tier tech de R$ 2.000 y la comisión) y "Estrategia Ecommerce" en R$ 8.000/mes (≠ los R$ 6.000 del tier estratégico de JET). Los números del modelo **no calzan exactamente** con los line items de las propuestas — reconciliarlos antes de tomarlos como verdad.
- **Sesgo sell-side:** correr el modelo con supuestos propios de Hache, no con los del vendedor.

---

## Diligencia de proveedores — deep research (22 jun 2026)

> **Veredicto del research: construir en Nuvemshop con agencia vetada; evitar JET y Sanders.**
> Método: 6 ángulos · 22 fuentes (sitios oficiales, LinkedIn, Reclame Aqui, registros CNPJ) · 61 claims extraídos · 25 verificados con votación adversarial (3 votos c/u) → 14 confirmados / 11 descartados. Fuentes primarias en portugués.

### JET — confirmado

| Hallazgo | Confianza |
|----------|-----------|
| Vitrine de casos: ~18-22 tiendas, 3-4 de moda, **cero calzado masculino de lujo** → fit vertical débil | Alta · 3-0 |
| Plataforma **enterprise, rígida, vendida vía agencias** → mal fit para un greenfield boutique | Media · 2-1 |
| **Defectos documentados** (Reclame Aqui): pagos, búsqueda, frete; un cliente **4 meses sin poder aceptar tarjetas** | Alta · 3-0 |
| Antigüedad **"desde 1999" NO se sostiene** (claim refutado). Empresa mediana (51-200 empl.), CNPJ 04.029.884/0001-68 | Alta · refutado 0-3 |
| Aclaración justa: la acusación de "cobra por cada update" es **falsa** | Alta · refutado 0-3 |

**Sigue abierto:** el **lock-in real / portabilidad de datos no se pudo verificar** → el riesgo del análisis sigue en pie, no resuelto.

### Sanders — confirmado

| Hallazgo | Confianza |
|----------|-----------|
| Su especialidad real es **CRO, no paid media** — pero la propuesta es de paid media (mismatch de capacidad) | Alta · 2-1 |
| Portfolio **skew beauty/enterprise, sin calzado ni fashion DTC** | Alta · 3-0 |
| Sitio **sin badges (Google/Meta), sin premios, sin casos, sin nº de clientes, sin CNPJ** → "80+ clientes / profesores en FIAP" no verificable | Alta · 3-0 |
| Precio **dentro de la banda de mercado** — el problema no es el precio, es el fit y la credibilidad | Media · 3-0 |

**Sigue abierto:** **identidad / registro / credenciales no verificables** (varias versiones de identidad refutadas; CNPJ desconocido).

### El otro lado del fork — verificado

- **Wave Commerce: confirmada fuerte** — partner Nuvemshop certificado, fundada 2017, **ganadora ABComm 2025**. Es el path creíble. (Alta · 3-0)
- **Ideia Vertical: credenciales NO verificadas** (1-2) — la otra del shortlist queda más débil de lo que pensábamos.
- **Nuvemshop:** tier gratis + **sin fee de setup** — pero **no es comisión cero**: tiene fees de transacción (el claim de "0%" fue refutado).

### Cómo cambia la decisión

La economía barata de JET+Sanders queda **contrapesada por fit, credibilidad y riesgo operativo**. JET: mal fit + defectos documentados + lock-in sin verificar. Sanders: especialidad equivocada + sin fit fashion + identidad no verificable. El research **inclina el fork hacia Nuvemshop + Wave Commerce** — pero la decisión final sigue siendo de Boris, con la validación de margen de Hache.

> Caveats: Reclame Aqui es one-sided (una de las quejas se resolvió); los benchmarks de precio salen de blogs de agencias; no se encontró el CNPJ de Sanders. Lo no verificable se reporta como abierto, no como negativo probado.

---

## La decisión de plataforma (greenfield)

No hay tienda en vivo, así que no es "quedarse vs. irse": es elegir limpio sobre qué construir, sin costo de cambio presente. Dos caminos:

**Construir en Nuvemshop**
- Plataforma originalmente prevista; alinea con la brand-bible. Del shortlist del [research de junio](2026-06-research-ecommerce-agency-alternatives.md), **Wave Commerce quedó confirmada fuerte** (partner certificado, ganadora ABComm 2025); **Ideia Vertical no pasó la verificación** de credenciales.
- Más portable a futuro (plataforma estándar).
- El proveedor original (Lucas Godoy) es caro, pide equity y —según el research— es lento/hands-off; el research existe justamente para reemplazarlo sin cambiar de plataforma.

**Construir en JET**
- Mucho más barato en fijo, setup y variable; sin equity.
- Plataforma cerrada → **lock-in / baja portabilidad futura** (sin verificar); si más adelante se quiere mover, eso sí sería una migración.
- Diligencia hecha (§ arriba): **mal fit (enterprise/rígido), vitrine sin lujo, defectos documentados**; y Sanders es un shop de CRO sin portfolio de moda. Dos proveedores que TE debe coordinar, vs. un solo orchestrator.
- Build de 90 días desde la aprobación del layout.

> En ambos casos el build arranca de cero. La única ventaja de timing es que ninguna vía "pierde" trabajo ya hecho — pero ninguna llega a un launch de julio si arranca ahora.

---

## Banderas rojas

1. **Elección de plataforma de largo plazo, no un replatform.** No hay costo de migración hoy (greenfield), pero JET cerrada compromete la **portabilidad futura**. No elegir por precio solo: pesar el ahorro contra quedar atado a un proveedor propietario.
2. **Margen bruto como único pivote** — el caso entero depende de un número que todavía no validamos internamente.
3. **Diligencia hecha — debilita a ambos** (§ Diligencia). JET: fit enterprise/rígido, vitrine sin lujo, defectos documentados, "1999" no comprobado. Sanders: shop de CRO (no paid media), sin portfolio de moda, sin credenciales verificables. El research inclina el fork hacia Nuvemshop + Wave Commerce.
4. **DRE sell-side** — modelo armado por/para la venta; correr con supuestos propios.
5. **Timing de launch** — el full launch de julio 2026 no es realista con un build desde cero arrancando ahora; el propio DRE asume septiembre. Reconciliar la fecha.
6. **Prolijidad** — "Terrible Elefant" en el documento de Sanders. Menor, pero es señal.

---

## Diligencia y próximos pasos (ruteo por dueño)

Nada de esto compromete a TE; son pasos de evaluación. Reusa las *diligence questions* del [research de junio](2026-06-research-ecommerce-agency-alternatives.md).

| Dueño | Acción |
|-------|--------|
| **Hache** (comercial/financiero) | Validar el **margen bruto real BRA** (¿CMV ~50% o ~70%?). Correr el DRE con supuestos propios. Decidir si la economía cierra. |
| **Boris** (plataforma/dirección) | Elegir **sobre qué plataforma construir** (Nuvemshop con agencia vetada vs. JET), pesando ahorro vs. portabilidad futura. Reconciliar la fecha de launch con el build. |
| **Nacho** (legal) | Revisar contratos JET y Sanders: **lock-in**, rescisión, **propiedad y portabilidad de datos** en plataforma cerrada, CNPJ de ambas entidades. (Sin equity acá — diferencia clave vs. Lucas Godoy.) |
| **Fanny** (Asana) | Crear tareas de seguimiento **solo si se avanza** — su dominio. No antes. |
| **Comando** | Sin acción: no hay comunicación externa involucrada en esta etapa. |

> Recordatorio de gobernanza: este documento es análisis interno. No se firmó nada, no se tocó `decision_log.md`, no se crearon tareas en Asana, no se contactó a ningún proveedor.
