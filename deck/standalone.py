#!/usr/bin/env python3
"""
Impacchetta i frammenti HTML in documenti autonomi, da scaricare e aprire in locale.

I frammenti in deck/web/ e deck/review/ sono senza doctype/head/body perche' nati per
essere pubblicati come pagina ospitata. Questo script li chiude in un documento completo:
font e immagini sono gia' in base64, quindi il file resta a dipendenza zero e funziona
offline, anche inoltrato per email.

Uso: python3 deck/standalone.py
Out: DFactory_SalesDeck_Viewer.html, DFactory_SalesDeck_Review.html
"""
import pathlib
import sys
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent

DOCS = [
    {
        "src": ROOT / "web" / "DFactory_SalesDeck_web.html",
        "out": REPO / "DFactory_SalesDeck_Viewer.html",
        "title": "D.Factory · Sales Deck",
        "desc": "Sales deck D.Factory, 14 slide.",
        "emoji": "🏭",
    },
    {
        "src": ROOT / "web" / "DFactory_DossierTecnico_web.html",
        "out": REPO / "DFactory_DossierTecnico_Viewer.html",
        "title": "D.Factory · Dossier tecnico",
        "desc": "Dettaglio di prodotto, integrazione e delivery, 16 slide.",
        "emoji": "🔧",
    },
    {
        "src": ROOT / "review" / "sales_review.html",
        "out": REPO / "DFactory_SalesDeck_Review.html",
        "title": "D.Factory · Review commerciale del sales deck",
        "desc": "23 rilievi su conversione, struttura, design e wording, ordinati per impatto.",
        "emoji": "🔍",
    },
]

SHELL = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="data:image/svg+xml,{favicon}">
<style>*{{margin:0;padding:0;box-sizing:border-box}}</style>
</head>
<body>
{fragment}
</body>
</html>
"""


def favicon(emoji: str) -> str:
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
           f"<text y='.9em' font-size='88'>{emoji}</text></svg>")
    return quote(svg, safe="")


def main() -> None:
    for d in DOCS:
        if not d["src"].exists():
            sys.exit(f"manca {d['src']}: esegui prima build_web.py")
        frag = d["src"].read_text(encoding="utf-8")
        low = frag.lower()
        if "<!doctype" in low or "<body" in low:
            sys.exit(f"{d['src'].name} sembra gia' un documento completo")
        html = SHELL.format(desc=d["desc"], title=d["title"],
                            favicon=favicon(d["emoji"]), fragment=frag)
        d["out"].write_text(html, encoding="utf-8")
        print(f"{d['out'].name}: {len(html) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
