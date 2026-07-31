#!/usr/bin/env python3
"""
Render dei documenti Quadro: una PNG per slide, piu' provino a contatto.

Il PDF resta sospeso finche' i documenti non sono approvati: si genera solo con
--pdf, mai per default.

Uso:  python3 quadro/render.py [--contact-sheet] [--pdf] [--only sales|dossier]
Out:  quadro/out/<doc>/slide_NN_<id>.png  (+ provino, + PDF su richiesta)
"""
import argparse
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
W, H, SCALE = 1280, 720, 3
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

DOCS = {
    "sales": {"html": REPO / "DFactory_SalesDeck.html", "pdf": REPO / "DFactory_SalesDeck.pdf"},
    "dossier": {"html": REPO / "DFactory_DossierTecnico.html",
                "pdf": REPO / "DFactory_DossierTecnico.pdf"},
}


def render(html: pathlib.Path, outdir: pathlib.Path) -> list:
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("slide_*.png"):
        old.unlink()
    kw = {"executable_path": CHROME} if pathlib.Path(CHROME).exists() else {}
    shots = []
    with sync_playwright() as p:
        br = p.chromium.launch(**kw)
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=SCALE)
        pg.goto(html.as_uri(), wait_until="networkidle")
        pg.evaluate("() => document.fonts.ready")
        pg.wait_for_timeout(600)
        ids = pg.eval_on_selector_all(".slide", "els => els.map(e => e.id)")
        if not ids:
            sys.exit(f"{html.name}: nessuna slide trovata")
        for i, sid in enumerate(ids, start=1):
            out = outdir / f"slide_{i:02d}_{sid}.png"
            pg.locator(f"#{sid}").screenshot(path=str(out))
            shots.append(out)
        br.close()
    print(f"  {len(shots)} slide a {W * SCALE}×{H * SCALE}")
    return shots


def contact_sheet(shots: list, outdir: pathlib.Path) -> None:
    from PIL import Image
    cols, tw = 4, 460
    th = round(tw * H / W)
    rows = (len(shots) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), "#5A5A58")
    for i, s in enumerate(shots):
        im = Image.open(s).convert("RGB").resize((tw, th), Image.LANCZOS)
        sheet.paste(im, ((i % cols) * tw, (i // cols) * th))
    out = outdir / "contact_sheet.png"
    sheet.save(out)
    print(f"  provino: {out}")


def to_pdf(shots: list, pdf: pathlib.Path) -> None:
    import img2pdf
    layout = img2pdf.get_layout_fun((img2pdf.in_to_pt(13.333), img2pdf.in_to_pt(7.5)))
    with open(pdf, "wb") as fh:
        img2pdf.convert([str(s) for s in shots], outputstream=fh, layout_fun=layout)
    print(f"  {pdf.name}: {pdf.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--contact-sheet", action="store_true")
    ap.add_argument("--pdf", action="store_true",
                    help="genera anche il PDF: solo su documenti approvati")
    ap.add_argument("--only", choices=sorted(DOCS))
    args = ap.parse_args()

    for name, d in DOCS.items():
        if args.only and name != args.only:
            continue
        if not d["html"].exists():
            print(f"--- {name}: {d['html'].name} non esiste ancora, salto")
            continue
        print(f"--- {d['html'].name}")
        shots = render(d["html"], ROOT / "out" / name)
        if args.contact_sheet:
            contact_sheet(shots, ROOT / "out" / name)
        if args.pdf:
            to_pdf(shots, d["pdf"])
    if not args.pdf:
        print("\nPDF non generato: usa --pdf sui documenti approvati.")
