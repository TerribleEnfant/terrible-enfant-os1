# Cenários · Viabilidade & ROI Brasil — `docs/cenarios.html`

Reescrita local da página
[`freequencyorg.github.io/terrible-enfant-roadmap/cenarios.html`](https://freequencyorg.github.io/terrible-enfant-roadmap/cenarios.html)
(rev 21), agora como **um único arquivo autocontido** — CSS + JS + dados inline, sem build,
sem framework, sem dependências. Mesma convenção de [`status.html`](status.html).

**Paridade numérica verificada.** Os três cenários semente foram medidos campo a campo contra
a página original em Chrome headless: **0 diferenças** em KPIs, DRE trimestral, fluxo acumulado,
OTB, sell-through, carga tributária efetiva e comparação de canais. O modelo é um port fiel,
não uma reinterpretação.

> **Este README é técnico** — arquitetura, verificação, publicação. Para *ler e usar* o modelo,
> o documento é o **guia de leitura**: 13 seções com a cadeia causal do modelo, os sete alertas,
> como ler cada gráfico, receitas de uso, armadilhas e glossário.
>
> - [`cenarios-guia.html`](cenarios-guia.html) — **espanhol**, versão canônica (convenção do
>   CLAUDE.md: docs operacionais em español)
> - [`cenarios-guia-pt.html`](cenarios-guia-pt.html) — **português**, para o lado brasileiro
>
> Os dois se linkam entre si por um seletor ES/PT na barra do topo. O modelo linka para o guia
> no rodapé e no cabeçalho, **seguindo o idioma ativo**: em PT vai para `-pt`, em ES e EN vai
> para o canônico.

---

## ⚠️ Antes de commitar / pushar — duas decisões do Boris

### 1. `docs/` é **público** no GitHub Pages

Ao pushar para `main`, esta página fica acessível na internet (só com `noindex`, que não é
controle de acesso). O conteúdo do catálogo, DRE, fees e margens **já está público** na página
original da Freequency — então esse delta é zero.

**O que é novo e não era público: a seção 11.**

### 2. Seção 11 — "Referência externa · e-commerce" contém dados de fornecedor

A seção 11 traz o DRE mensal de 36 meses do arquivo
`cadence/operations/BRA/ecommerce/JET PROPOSAL/Terrible Enfant DRE_19062026_PROSPECT.xlsx`
— proposta comercial da **JET Tecnologia**, extraída do SharePoint deles. É material de
terceiro, confidencial, e serve aqui só para contrastar a curva de e-commerce do nosso modelo
contra a que o fornecedor projetou.

Está incluída porque é análise útil e porque **nada foi pushado**. A decisão de publicar é sua.

**Para remover a seção inteira**, apague a chave `"reference"` do bloco JSON `id="DATA"`
dentro de `docs/cenarios.html`. A página detecta a ausência e some com a seção 11 — sem
tocar em mais nada, sem erro no console. (Verificado: 11 seções, mesmo EBITDA, zero erros.)

Se quiser manter a análise sem publicar, a alternativa é deixar a seção e **não pushar** —
o arquivo funciona igual aberto por `file://`.

---

## O que mudou em relação à rev 21

### Estrutura

| rev 21 | agora |
|---|---|
| 3 arquivos (`cenarios.html`, `-en`, `-es`) | **1 arquivo**, idioma em runtime (`?lang=pt\|en\|es`) |
| dados espalhados em 606 `<input>` escritos à mão | bloco JSON `id="DATA"` → DOM gerado |
| estado = array posicional de 606 campos, com 19 migrações encadeadas | estado **keyed** `{id: valor}`; o array posicional só sobrevive como formato de import |
| `calc()` de 400 linhas mexendo no DOM | `compute(estado)` **puro** + `paint()` separado |

O `compute()` puro é o que destrava sensibilidade e comparação: dá para rodar o modelo N vezes
sem tocar na tela.

### UX / UI

- **Resumo no topo.** Antes você atravessava 10 seções de input para chegar ao resultado.
  Agora abre com KPIs, fluxo acumulado, receita × EBITDA por trimestre e sell-through.
- **Rail de navegação** com valor ao vivo por seção e badge de alerta na seção problemática.
- **Gráficos** — SVG inline, cientes do tema, zero bibliotecas: fluxo acumulado com marcador
  de payback, barras receita × EBITDA, margem de contribuição por canal, tornado de
  sensibilidade, sparklines mensais da referência.
- **Sensibilidade ±15%** em 9 drivers, ordenada por impacto no EBITDA acumulado. No cenário
  Pessimista a ordem é: SRP do catálogo (±R$ 389 mil) › câmbio = volume (±297) › verba de
  comunicação (±137) › alíquotas (±125) › agency fee (±117) › custo (±92) › margem Matalab
  (±90) › operacional (±41). Isso responde "onde vale negociar" sem tentativa e erro.
- **Comparação de cenários** — tabela de indicadores + curvas sobrepostas.
- **Catálogo navegável** — busca, filtro por categoria, 6 ordenações, barra de margem por linha,
  preenchimento em massa por categoria.
- **Tema claro / escuro / sistema.**
- **Modo Leitura** — os campos editáveis viram texto puro; a página lê como documento.
  Serve para mandar para parceiro sem parecer planilha.
- **Paleta de comandos** (`⌘K` / `Ctrl+K`) — pular para seção, aplicar cenário, disparar ação.
- **Navegação por setas** nas grades de trimestre (162 células de sell-out ficaram usáveis).
- **`/`** foca a busca do catálogo.
- **Painel de alertas** no rail, com link para a seção que causou.
- **Badge de edições** — quantos campos você mexeu em relação ao cenário aplicado.
- **Estilo de impressão** — abre todas as seções, esconde controles, mantém gráficos.
- **Mobile** — sem overflow horizontal em nenhuma largura (verificado a 390/430/560/900 px);
  as preferências que saem da topbar reaparecem no rail-gaveta.

### Compatibilidade preservada

- Links `#v1=` / `#v2=` / `#v3=` da rev 21 ainda abrem — a cadeia inteira de migração posicional
  foi portada, com a referência rev-21 congelada em `meta.legacy_skus` / `meta.legacy_cat`.
- Arquivos `.json` baixados da rev 21 (`{values:[...]}`) carregam.
- Cenários salvos no `localStorage` da rev 21 (`te-viab-sh-scn`) são migrados na primeira abertura.
- O `Baixar` novo grava **os dois formatos** (`vals` keyed + `values` posicional), então o arquivo
  volta a abrir na página antiga se precisar.
- Novo link é `#c1=` (JSON deflate + base64url) — ~3,3 kB, com o nome do cenário base embutido.

---

## A planilha de estoque — acesso bloqueado

O pedido era combinar esta página com
`docs.google.com/spreadsheets/d/1cejjQyOE8G9fS1LOc6fV-c7evAIV4r7a` (gid 749764706).

**Não consegui ler essa planilha.** O que tentei:

| via | resultado |
|---|---|
| conector Google Drive do Claude (`admin@both.ventures`) | `Requested entity was not found` — a conta não tem esse arquivo |
| busca no Drive por `Terrible` / `Enfant` / `DRE` / `Cenario` | zero resultados; a conta não tem nada de TE |
| export público (`/export?format=csv`, `gviz/tq`, `/pub`, `/htmlview`) | **HTTP 401** — a planilha é privada |
| Google Drive montado em `~/Library/CloudStorage` | é a mesma conta `both.ventures`; o arquivo não está lá |
| `op` (1Password) | sem sessão nesta máquina |

O ID tem 33 caracteres, o formato de **arquivo `.xlsx` subido ao Drive** (planilha nativa do
Sheets tem 44). Provavelmente vive numa conta Google da Freequency ou de TE, não em
`both.ventures`.

### O que fiz em vez de adivinhar

Não inventei números. Construí o caminho de integração e deixei o catálogo da rev 21 como
está, explicitamente rotulado `embutido` na própria página.

**Duas vias para plugar a planilha, as duas prontas e testadas:**

#### A. Conferir rápido no navegador — botão **Importar planilha** (seção 2)

Cole o CSV (ou solte o arquivo na textarea). A página:

1. detecta o separador (`,` `;` tab `|`) e o formato decimal (`1.234,56` ou `1,234.56`);
2. adivinha o mapeamento das 6 colunas pelo cabeçalho — testado com cabeçalhos em
   pt/es/en (`SKU`, `MODELO`, `CATEGORIA`, `MATALAB PRICE`, `COST`, `EMBARQUE`);
3. mostra o **diff antes de aplicar**: alterados campo a campo (de → para), novos,
   e os que não estão na planilha;
4. só grava quando você clica em aplicar.

Também aceita URL de CSV publicado (`.../gviz/tq?tqx=out:csv&gid=…`) se a planilha estiver
publicada na web — se der CORS/401, ele avisa e você cola o texto.

⚠️ Isso grava **no `localStorage` de quem clicou**. Serve para conferir, não para publicar.
Um badge na seção 2 mostra a origem do catálogo (`embutido` vs `planilha · data`) e um botão
volta ao catálogo embutido.

#### B. Publicar de verdade — `scripts/cenarios_catalog.py`

```bash
# 1. Sheets → Arquivo → Download → .csv (a aba do gid 749764706)
# 2. conferir o que mudaria, sem escrever nada:
python3 scripts/cenarios_catalog.py estoque.csv --dry-run

# 3. aplicar:
python3 scripts/cenarios_catalog.py estoque.csv --source-label "TE.MATALAB ago/26"

# mapeamento manual, se o cabeçalho não for óbvio:
python3 scripts/cenarios_catalog.py estoque.csv \
    --col-sku SKU --col-srp "MATALAB PRICE" --col-cost COST --col-qty EMBARQUE
```

Reescreve o bloco `catalog` dentro de `docs/cenarios.html`, então quem abrir a página publicada
já vê os dados da planilha. Regras:

- a chave é o **código SKU** (normalizado: maiúsculas, sem espaços);
- coluna ausente no CSV → mantém o valor atual;
- SKU novo → entra no fim;
- **SKU que está no catálogo e não na planilha é mantido, nunca apagado** — o relatório lista
  quais, para decisão humana;
- os três cenários semente são **realinhados por SKU**, então acrescentar ou reordenar SKUs
  não desalinha preço de um produto com quantidade de outro. As curvas de sell-out, reposição,
  comunicação, fee e opex das sementes ficam intactas;
- `meta.legacy_skus` / `meta.legacy_cat` **nunca** são reescritos — é o que mantém os links
  antigos decodificando certo;
- atualiza `meta.catalog_source` e `meta.rev`.

Testado ponta a ponta: CSV com `;`, `R$ 455`, cabeçalho em maiúsculas, 1 SKU alterado +
1 novo + 90 ausentes → catálogo 92→93, quantidade total 1.697→1.757 (aritmética conferida
à mão), preços da planilha sobrevivem ao reaplicar a semente, zero erro no console.

### O que ainda depende de você

1. **Exportar a aba certa em CSV** e rodar o comando B (ou me dar acesso à planilha:
   compartilhar com `admin@both.ventures`, ou publicar a aba em CSV, ou colar o conteúdo).
2. **Dizer o que a planilha significa.** A nota da seção 2 diz *"pré-carregado com a sugestão
   de preço da Matalab quando existe (37 SKUs), senão o preço de catálogo. Custo conforme a
   coluna COST da planilha de estoque"* — isso sugere que a planilha é o catálogo/estoque
   com colunas de SRP, COST e sugestão Matalab. Se for outra coisa (um DRE, um cenário
   alternativo, um plano de compra), o mapeamento de colunas é diferente e eu ajusto.

---

## Anatomia do arquivo

4.450 linhas, ~333 kB (dos quais ~93 kB são o logo TE em base64, herdado da rev 21).
Editável direto, sem build — como `status.html`.

```
linhas   12– 414   <style>   tokens claro/escuro, layout, componentes, print
linhas  416– 493   <body>    casca: topbar, rail, hero, #sections, drawer, paleta
linhas  494–2212   <script type="application/json" id="DATA">
linhas 2213–4447   <script>  app (núcleo → gráficos → render → ações → boot)
```

O bloco `DATA` é serializado para ser diffável no git: chaves de máquina (`order`, `defaults`)
em uma linha; `catalog` e `scenarios` com **um item por linha**; o resto indentado.
Trocar o preço de um SKU é um diff de uma linha.

### Chaves do bloco `DATA`

| chave | o que é |
|---|---|
| `meta` | revisão, origem, URL da planilha, e a referência **congelada** rev-21 |
| `q` | 9 trimestres (`Q3 26`→`Q3 28`), ano de cada um, `phase1: 4` |
| `cats` / `catl` | 6 categorias + tradução pt/en/es |
| `ch` / `chl` | 3 canais (showroom, Matalab atacado, e-commerce) + tradução |
| `comms` / `fees` / `opexl` / `dre` / `prem` / `rz` | linhas de cada tabela + rótulos |
| `regimes` | Simples Nacional vs Lucro Presumido (alíquotas) |
| `order` / `defaults` | os 606 ids na ordem rev-21 — **só** para decodificar formato antigo |
| `catalog` | 92 SKUs: `sku`, `name`, `cat`, `srp` (US$), `cost` (US$), `qty` |
| `scenarios` | 3 cenários semente, em formato keyed |
| `reference` | DRE mensal JET — **apagar para remover a seção 11** |
| `i18n` | todo o texto em pt/en/es |

### Onde mexer no app

| quero | vou em |
|---|---|
| mudar a matemática | `compute(st)` — função pura, sem DOM |
| mudar um número na tela | `paintNow()` |
| mudar a estrutura de uma seção | `secPrem` / `secCatalog` / `secSell` / … |
| mudar um gráfico | `chartCum` / `chartQuarters` / `chartTornado` / `chartChannels` / `chartSpark` |
| mexer em cenário, link, arquivo, import | bloco de ações |
| mudar texto | `DATA.i18n` |

### Chaves de `localStorage`

`te-cen-v1-state` · `-scn` · `-sec` · `-cur` · `-lang` · `-theme` · `-mode` · `-cat` ·
`-bak` · `-base`. Lê as antigas (`te-viab-sh*`) uma vez, para migrar.

---

## Verificação

Rodei tudo em Chrome headless. Para repetir, o padrão é injetar um `<script>` de probe antes de
`</body>` e ler com `--dump-dom`.

| suíte | resultado |
|---|---|
| Paridade vs rev 21 (3 cenários × 40 campos) | **0 diferenças** |
| Funcional (58 asserções) | **58 passam, 0 falham** |
| Erros de console em todos os caminhos | **0** |
| Overflow horizontal a 390 / 430 / 560 / 900 px | **nenhum** |
| Degradação sem `reference.jet` | 11 seções, mesmo EBITDA, 0 erros |
| Import CSV → seed realinhada | aritmética conferida à mão |

A suíte funcional cobre: boot, 3 idiomas, 2 moedas, edição recalculando, máscara de milhar,
salvar/aplicar/excluir cenário, round-trip do link novo e do legado, payload de download,
abrir/fechar seções, busca/filtro/ordem do catálogo, 9 drivers de sensibilidade ordenados,
tabela de comparação, import CSV completo (detecção, mapeamento, diff, aplicação, remapeamento
de cenário, reversão), paleta, modo leitura, tema, troca de regime tributário, replicar linha,
preencher categoria, undo.

---

## Publicar

Pages já está configurado (`main`, pasta `/docs`). O fluxo é o de sempre:

```bash
# 1. abrir docs/cenarios.html no navegador e conferir
# 2. decidir sobre a seção 11 (ver o aviso no topo)
# 3. Boris revisa  ← exigido pelo CLAUDE.md
git add docs/cenarios.html docs/cenarios-guia.html docs/cenarios-guia-pt.html \
        docs/cenarios-README.md scripts/cenarios_catalog.py
git commit -m "[ops] Cenários BR — port da rev 21 + guia de leitura ES/PT + import da planilha"
git push origin main
```

URLs finais:

```
https://terribleenfant.github.io/terrible-enfant-os1/cenarios.html           ← o modelo
https://terribleenfant.github.io/terrible-enfant-os1/cenarios-guia.html      ← guia (ES)
https://terribleenfant.github.io/terrible-enfant-os1/cenarios-guia-pt.html   ← guia (PT)
```

**Não commitei nem pushei nada** — CLAUDE.md pede revisão do Boris antes.

### Ainda em aberto

- Link na home (`docs/index.html`) para estas páginas. Não fiz: é documento de marca publicado,
  e `index.html` só tem âncoras internas hoje. Um `<a>` a mais, se você quiser.
- O guia existe em ES (canônico) e PT. O modelo troca de idioma em runtime; o guia são dois
  arquivos com seletor. Se aparecer necessidade de EN, é o mesmo procedimento.
- Aposentar `cenarios-en.html` / `cenarios-es.html` no repo da Freequency — agora um arquivo
  serve os três idiomas. Fica lá, não é nosso repo.

---
*Terrible Enfant · built on COMANDO Canon*
