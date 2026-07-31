#!/usr/bin/env python3
"""
Assembla i due documenti D.Factory sul sistema di design "Quadro".

Il foglio di sistema e' la fonte di verita' e viene inlinato in un unico <style>
in testa a ogni documento. I font (Geist, Geist Mono, Instrument Serif) sono gia'
incorporati in base64 nel foglio: nessuna chiamata a CDN, i documenti funzionano
anche senza rete.

Uso:  python3 quadro/build.py [filtro]
Out:  i quattro documenti; con un filtro solo quelli il cui nome lo contiene
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
SYSTEM = ROOT / "dfactory-system.css"

DOCS = [
    # v1: resta compilabile, non si sovrascrive.
    {"src": ROOT / "src" / "sales.html", "out": REPO / "DFactory_SalesDeck.html",
     "title": "D.Factory · Sales Deck", "atteso": 14},
    {"src": ROOT / "src" / "dossier.html", "out": REPO / "DFactory_DossierTecnico.html",
     "title": "D.Factory · Dossier tecnico", "atteso": 16},
    # v2: revisione congiunta, 12 slide e 18 pagine.
    {"src": ROOT / "src" / "sales_v2.html", "out": REPO / "DFactory_SalesDeck_v2.html",
     "title": "D.Factory · Sales Deck", "atteso": 12},
    {"src": ROOT / "src" / "dossier_v2.html", "out": REPO / "DFactory_DossierTecnico_v2.html",
     "title": "D.Factory · Dossier tecnico", "atteso": 18},
]

SHELL = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
{css}
/* --- impaginazione del documento: fuori dal sistema, non tocca le slide --- */
html,body{{margin:0;padding:0;background:#5A5A58;}}
.doc{{display:flex;flex-direction:column;align-items:center;gap:28px;padding:28px 0;}}
@media print{{
  html,body{{background:#fff;}}
  .doc{{gap:0;padding:0;}}
  .slide{{break-after:page;page-break-after:always;}}
  @page{{size:1280px 720px;margin:0;}}
}}
</style>
</head>
<body>
<div class="doc">
{body}
</div>
</body>
</html>
"""


def numera(html: str, tot: int) -> str:
    """Riempie @@DOC@@ con la posizione della slide nel documento.

    I numeri non si scrivono a mano: si ricavano dall'ordine, cosi' riordinare o
    inserire una slide non obbliga a rincorrere i cartigli.
    """
    out, pos, seq = [], 0, 0
    for m in re.finditer(r'<div class="slide[^"]*"', html):
        seq += 1
        end = html.find("</div><!--/slide-->", m.end())
        if end == -1:
            sys.exit(f"slide {seq}: manca il marcatore <!--/slide-->")
        chunk = html[m.start():end].replace("@@DOC@@", f"{seq:02d} / {tot:02d}")
        out.append(html[pos:m.start()])
        out.append(chunk)
        pos = end
    out.append(html[pos:])
    return "".join(out)


def main() -> None:
    only = sys.argv[1] if len(sys.argv) > 1 else ""
    css = SYSTEM.read_text(encoding="utf-8")
    for d in DOCS:
        if not d["src"].exists():
            if only and only not in d["out"].name:
                continue
            sys.exit(f"{d['out'].name}: manca il sorgente {d['src'].name}")
        if only and only not in d["out"].name:
            continue
        body = d["src"].read_text(encoding="utf-8")
        n = body.count('<div class="slide')
        if n != d["atteso"]:
            sys.exit(f"{d['out'].name}: attese {d['atteso']} slide, trovate {n}")
        body = numera(body, n)

        html = SHELL.format(title=d["title"], css=css, body=body)
        leftover = sorted(set(re.findall(r"@@[A-Z_0-9]+@@", html)))
        if leftover:
            sys.exit(f"{d['out'].name}: token non risolti: {leftover}")

        d["out"].write_text(html, encoding="utf-8")
        ph = sorted(set(re.findall(r"\[\[(PH_\d+_[A-Z_]+)\]\]", html)))
        scure = len(re.findall(r'class="slide slide--dark"', html))
        print(f"{d['out'].name}: {n} slide ({scure} scure + {n - scure} chiare), "
              f"{len(html) / 1024:.0f} KB, {len(ph)} placeholder")
        for t in ph:
            print(f"    {t}")


if __name__ == "__main__":
    main()
