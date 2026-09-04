#!/usr/bin/env python3
"""
cenarios_catalog.py — funde a planilha de estoque no catálogo embutido de
`docs/cenarios.html`.

O que faz
---------
Lê um CSV (export da planilha de estoque do Google Sheets) e reescreve o bloco
`catalog` do JSON embutido em `docs/cenarios.html`, remapeando por código SKU.
Isto é a via *permanente*: quem abrir a página publicada já vê os dados da
planilha, sem depender do import no navegador de cada pessoa.

O import equivalente pela UI (botão **Importar planilha**) grava só no
localStorage de quem clicou — serve para conferir rápido, não para publicar.

Uso
---
    # 1. Exportar a aba certa do Sheets como CSV (Arquivo → Download → .csv)
    # 2. Conferir o que mudaria (não escreve nada):
    python3 scripts/cenarios_catalog.py estoque.csv --dry-run

    # 3. Aplicar:
    python3 scripts/cenarios_catalog.py estoque.csv

    # Mapeamento manual, quando o cabeçalho não é óbvio:
    python3 scripts/cenarios_catalog.py estoque.csv \
        --col-sku SKU --col-name MODELO --col-cat CATEGORIA \
        --col-srp "MATALAB PRICE" --col-cost COST --col-qty EMBARQUE

Regras
------
* A chave é o **código SKU** (normalizado: maiúsculas, sem espaços).
* Coluna ausente no CSV → o valor atual do catálogo é mantido.
* SKU no CSV e não no catálogo → entra como novo, no fim.
* SKU no catálogo e não no CSV → **é mantido**, nunca apagado. O relatório lista
  esses casos para decisão humana.
* Os três cenários semente (`scenarios`) guardam a lista de SKUs em que foram
  gravados; a página remapeia por SKU ao aplicá-los, então acrescentar ou
  reordenar SKUs não corrompe cenário salvo.
* `meta.catalog_source` e `meta.rev` são atualizados com a origem e a data.

Sem dependências além da stdlib.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "docs" / "cenarios.html"
BLOCK_RX = re.compile(
    r'(<script type="application/json" id="DATA">)(.*?)(</script>)', re.S
)

HINTS = {
    "sku":  ["sku", "codigo", "código", "code", "ref", "referencia", "referência", "id"],
    "name": ["nome", "name", "modelo", "model", "produto", "producto", "descri",
             "articulo", "artículo", "item"],
    "cat":  ["categoria", "category", "cat", "linha", "línea", "linea", "tipo",
             "familia", "família", "grupo"],
    "srp":  ["srp", "pvp", "retail", "preco", "preço", "precio", "price", "venda",
             "matalab", "sugerido", "msrp"],
    "cost": ["cost", "custo", "costo", "fob", "compra", "landed"],
    "qty":  ["qtd", "qty", "quant", "cant", "units", "unidades", "estoque",
             "stock", "embarque", "pcs", "pares"],
}
FIELDS = list(HINTS)


# ----------------------------------------------------------------- leitura
def sniff_rows(text: str) -> list[list[str]]:
    sample = "\n".join(text.splitlines()[:20])
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
    except csv.Error:
        first = next((l for l in text.splitlines() if l.strip()), "")
        delim = max(",;\t|", key=first.count)
        dialect = csv.excel
        dialect.delimiter = delim
    rows = [r for r in csv.reader(io.StringIO(text), dialect) if any(c.strip() for c in r)]
    return rows


def parse_num(v):
    """Aceita 1.234,56 / 1,234.56 / R$ 1.234 / US$ 85 / vazio."""
    s = re.sub(r"[^\d,.\-]", "", str(v or "")).strip()
    if not s:
        return None
    lc, ld = s.rfind(","), s.rfind(".")
    if lc > -1 and ld > -1:
        s = s.replace(".", "").replace(",", ".") if lc > ld else s.replace(",", "")
    elif lc > -1:
        s = s.replace(",", "") if re.fullmatch(r"\d{1,3}(,\d{3})+", s) else s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def guess_map(head: list[str]) -> dict[str, int]:
    out, used = {}, set()
    for f in FIELDS:
        best, score = -1, 0
        for i, h in enumerate(head):
            if i in used:
                continue
            lh = str(h).lower()
            s = max((len(k) for k in HINTS[f] if k in lh), default=0)
            if s > score:
                score, best = s, i
        if best >= 0:
            out[f] = best
            used.add(best)
    return out


norm = lambda s: re.sub(r"\s+", "", str(s or "")).upper()


def match_cat(raw, cats, catl):
    if not raw:
        return None
    n = str(raw).strip().lower()
    for i, c in enumerate(cats):
        alts = [c] + [catl[lg][i] for lg in catl]
        for a in (str(x).lower() for x in alts):
            if a == n or n in a or a in n:
                return c
    return None


def num(x):
    """Números inteiros saem sem `.0` — o catálogo original usa int."""
    return int(x) if float(x).is_integer() else float(x)


# ----------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", help="CSV exportado da planilha de estoque")
    ap.add_argument("--page", default=str(PAGE), help="HTML alvo (default: docs/cenarios.html)")
    ap.add_argument("--dry-run", action="store_true", help="só relata, não escreve")
    ap.add_argument("--source-label", default=None,
                    help="texto para meta.catalog_source (default: nome do CSV)")
    for f in FIELDS:
        ap.add_argument(f"--col-{f}", default=None, help=f"cabeçalho da coluna de {f}")
    args = ap.parse_args()

    page = pathlib.Path(args.page)
    if not page.exists():
        print(f"erro: não achei {page}", file=sys.stderr)
        return 2

    html = page.read_text(encoding="utf-8")
    m = BLOCK_RX.search(html)
    if not m:
        print("erro: bloco <script id=DATA> não encontrado", file=sys.stderr)
        return 2
    data = json.loads(m.group(2))

    raw = pathlib.Path(args.csv).read_text(encoding="utf-8-sig", errors="replace")
    rows = sniff_rows(raw)
    if len(rows) < 2:
        print("erro: CSV com menos de duas linhas", file=sys.stderr)
        return 2
    head, body = rows[0], rows[1:]

    colmap = guess_map(head)
    lower = [str(h).strip().lower() for h in head]
    for f in FIELDS:
        want = getattr(args, f"col_{f}")
        if want:
            try:
                colmap[f] = lower.index(want.strip().lower())
            except ValueError:
                print(f"erro: coluna {want!r} não existe. Cabeçalho: {head}", file=sys.stderr)
                return 2

    print("colunas mapeadas:")
    for f in FIELDS:
        i = colmap.get(f)
        print(f"  {f:5} → {head[i] if i is not None else '—'}")
    if "sku" not in colmap:
        print("erro: sem coluna de SKU não há como casar as linhas.", file=sys.stderr)
        return 2

    cats, catl = data["cats"], data["catl"]
    old = data["catalog"]
    by_sku = {norm(c["sku"]): (i, c) for i, c in enumerate(old)}

    new, changed, added, seen, bad = [], [], [], set(), 0
    provided: dict[str, dict] = {}     # sku normalizado -> valores que a planilha trouxe
    get = lambda r, f: r[colmap[f]] if colmap.get(f) is not None and colmap[f] < len(r) else None

    for r in body:
        sku = str(get(r, "sku") or "").strip()
        if not sku:
            bad += 1
            continue
        key = norm(sku)
        if key in seen:
            bad += 1
            continue
        seen.add(key)

        srp, cost, qty = (parse_num(get(r, f)) for f in ("srp", "cost", "qty"))
        name = (str(get(r, "name") or "").strip() or None)
        cat = match_cat(get(r, "cat"), cats, catl)
        provided[key] = {"srp": srp, "cost": cost, "qty": qty}

        prev = by_sku.get(key)
        base = prev[1] if prev else None
        rec = {
            "sku":  sku,
            "name": name or (base["name"] if base else sku),
            "cat":  cat or (base["cat"] if base else cats[-1]),
            "srp":  num(srp)  if srp  is not None else (base["srp"]  if base else 0),
            "cost": num(cost) if cost is not None else (base["cost"] if base else 0),
            "qty":  num(qty)  if qty  is not None else (base["qty"]  if base else 0),
        }
        if base is None:
            added.append(rec)
        else:
            d = [(k, base[k], rec[k]) for k in ("srp", "cost", "qty", "name", "cat")
                 if base[k] != rec[k]]
            if d:
                changed.append((sku, d))
        new.append(rec)

    missing = [c for c in old if norm(c["sku"]) not in seen]
    new += missing   # nada é apagado

    print(f"\nlinhas lidas      {len(body)}" + (f"  ({bad} ignoradas)" if bad else ""))
    print(f"alterados         {len(changed)}")
    print(f"novos             {len(added)}")
    print(f"não na planilha   {len(missing)}  (mantidos no catálogo)")
    print(f"catálogo          {len(old)} → {len(new)} SKUs")

    if changed:
        print("\nalterações:")
        for sku, d in changed[:80]:
            for k, a, b in d:
                print(f"  {sku:22} {k:5} {a!r} → {b!r}")
        if len(changed) > 80:
            print(f"  … +{len(changed)-80}")
    if added:
        print("\nnovos: " + " · ".join(c["sku"] for c in added[:40])
              + (f" … +{len(added)-40}" if len(added) > 40 else ""))
    if missing:
        print("\nnão na planilha (mantidos): "
              + " · ".join(c["sku"] for c in missing[:40])
              + (f" … +{len(missing)-40}" if len(missing) > 40 else ""))

    if not (changed or added):
        print("\nnada a fazer — catálogo já está igual à planilha.")
        return 0
    if args.dry_run:
        print("\n--dry-run: nenhum arquivo escrito.")
        return 0

    label = args.source_label or pathlib.Path(args.csv).name
    today = dt.date.today().isoformat()

    # --- realinhar os cenários semente ao novo catálogo ------------------
    # As sementes guardam srp_i/cst_i/qty_i por POSIÇÃO. Se o catálogo muda de
    # tamanho ou de ordem, essas posições passam a apontar para outro SKU.
    # Aqui reconstruímos os três campos por SKU: valor da planilha quando
    # existe, senão o que a semente já tinha, senão o do catálogo. Tudo o mais
    # da semente (sell-out, reposição, comunicação, fee, opex) fica intacto.
    seed_order = data["meta"].get("seed_skus") or data["meta"]["legacy_skus"]
    seed_idx = {norm(s): i for i, s in enumerate(seed_order)}
    FMAP = {"srp": "srp", "cost": "cst", "qty": "qty"}
    realigned = 0
    for name_, sc in data.get("scenarios", {}).items():
        # calcula tudo ANTES de escrever: os índices novos e velhos se cruzam,
        # escrever em `sc` durante o laço corromperia as leituras seguintes.
        fresh: dict[str, str] = {}
        for j, rec in enumerate(new):
            k = norm(rec["sku"])
            oi = seed_idx.get(k)
            for field, pre in FMAP.items():
                sheet_v = (provided.get(k) or {}).get(field)
                if sheet_v is not None:
                    val = num(sheet_v)
                elif oi is not None and f"{pre}_{oi}" in sc:
                    val = sc[f"{pre}_{oi}"]
                else:
                    val = rec[field]
                fresh[f"{pre}_{j}"] = str(val)
        # descarta todos os índices antigos, grava os novos
        for key_ in [k for k in sc if re.fullmatch(r"(srp|cst|qty)_\d+", k)]:
            del sc[key_]
        sc.update(fresh)
        realigned += 1
    data["meta"]["seed_skus"] = [c["sku"] for c in new]

    data["catalog"] = new
    data["meta"]["catalog_source"] = f"{label} · {len(new)} SKUs (importado {today})"
    data["meta"]["rev"] = today
    print(f"\ncenários semente realinhados: {realigned}")

    # serialização igual à do arquivo: chaves de máquina em uma linha,
    # catalog/scenarios um item por linha, o resto indentado.
    compact = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    parts = []
    for k, v in data.items():
        if k in ("order", "defaults"):
            parts.append(f" {compact(k)}: {compact(v)}")
        elif k == "scenarios":
            inner = ",\n".join(f"  {compact(n)}: {compact(x)}" for n, x in v.items())
            parts.append(f" {compact(k)}: {{\n{inner}\n }}")
        elif k == "catalog":
            inner = ",\n".join(f"  {compact(x)}" for x in v)
            parts.append(f" {compact(k)}: [\n{inner}\n ]")
        else:
            parts.append(f" {compact(k)}: " + json.dumps(v, ensure_ascii=False, indent=1)
                         .replace("\n", "\n "))
    out = "{\n" + ",\n".join(parts) + "\n}"
    json.loads(out)                       # sanidade
    assert "</script" not in out.lower()  # não pode fechar o bloco

    page.write_text(html[:m.start(2)] + out + html[m.end(2):], encoding="utf-8")
    print(f"\n→ {page} atualizado. Abra no navegador e confira os totais antes de commitar.")
    print("  Lembre: docs/ é público no GitHub Pages. Boris revisa antes do push.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
