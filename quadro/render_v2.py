#!/usr/bin/env python3
"""
Render di collaudo dei due documenti v2: una PNG per pagina, piu' provino e PDF.

I PDF che escono da qui sono materiale di verifica, non il consegnabile: gli HTML
restano gli artefatti principali.

Uso:  python3 quadro/render_v2.py [--no-pdf]
Out:  qa/sales/, qa/dossier/, qa/DFactory_*_v2.pdf
"""
import argparse
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
QA = REPO / "qa"
W, H, SCALE = 1280, 720, 3
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

DOCS = [
    {"html": REPO / "DFactory_SalesDeck_v2.html", "out": QA / "sales",
     "pdf": QA / "DFactory_SalesDeck_v2.pdf"},
    {"html": REPO / "DFactory_DossierTecnico_v2.html", "out": QA / "dossier",
     "pdf": QA / "DFactory_DossierTecnico_v2.pdf"},
]


def render(html, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("*.png"):
        old.unlink()
    kw = {"executable_path": CHROME} if pathlib.Path(CHROME).exists() else {}
    shots = []
    with sync_playwright() as p:
        br = p.chromium.launch(**kw)
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=SCALE)
        pg.goto(html.as_uri(), wait_until="networkidle")
        pg.evaluate("() => document.fonts.ready")
        pg.wait_for_timeout(700)
        ids = pg.eval_on_selector_all(".slide", "els => els.map(e => e.id)")
        if not ids:
            sys.exit(f"{html.name}: nessuna pagina trovata")
        for i, sid in enumerate(ids, start=1):
            out = outdir / f"{i:02d}_{sid}.png"
            pg.locator(f"#{sid}").screenshot(path=str(out))
            shots.append(out)
        br.close()
    print(f"  {len(shots)} pagine a {W * SCALE}×{H * SCALE} in {outdir.relative_to(REPO)}/")
    return shots


def contact_sheet(shots, outdir):
    from PIL import Image
    cols, tw = 4, 460
    th = round(tw * H / W)
    rows = (len(shots) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), "#5A5A58")
    for i, s in enumerate(shots):
        im = Image.open(s).convert("RGB").resize((tw, th), Image.LANCZOS)
        sheet.paste(im, ((i % cols) * tw, (i // cols) * th))
    out = outdir / "provino.png"
    sheet.save(out)
    print(f"  provino: {out.relative_to(REPO)}")


def to_pdf(shots, pdf):
    import img2pdf
    layout = img2pdf.get_layout_fun((img2pdf.in_to_pt(13.333), img2pdf.in_to_pt(7.5)))
    with open(pdf, "wb") as fh:
        img2pdf.convert([str(s) for s in shots], outputstream=fh, layout_fun=layout)
    print(f"  {pdf.relative_to(REPO)}: {pdf.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()
    QA.mkdir(exist_ok=True)
    for d in DOCS:
        if not d["html"].exists():
            sys.exit(f"manca {d['html'].name}: esegui prima quadro/build.py")
        print(f"--- {d['html'].name}")
        shots = render(d["html"], d["out"])
        contact_sheet(shots, d["out"])
        if not args.no_pdf:
            to_pdf(shots, d["pdf"])
