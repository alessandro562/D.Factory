#!/usr/bin/env python3
"""
Render del sales deck D.Factory: HTML -> PNG per slide -> PDF.

Playwright/Chromium, viewport 1280x720, device_scale_factor=3.
Attesa: networkidle + document.fonts.ready + 600 ms.
Assemblaggio PDF con img2pdf a 13.333" x 7.5" (960 x 540 pt).

Uso:  python3 deck/render.py [--contact-sheet]
Out:  DFactory_SalesDeck.pdf  +  deck/out/slide_NN_<id>.png
"""
import argparse
import pathlib
import sys

import img2pdf
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
DOCS = [
    {"html": REPO / "DFactory_SalesDeck.html", "pdf": REPO / "DFactory_SalesDeck.pdf",
     "out": ROOT / "out" / "sales"},
    {"html": REPO / "DFactory_DossierTecnico.html", "pdf": REPO / "DFactory_DossierTecnico.pdf",
     "out": ROOT / "out" / "dossier"},
]

W, H, SCALE = 1280, 720, 3
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def chromium_kwargs() -> dict:
    return {"executable_path": CHROME} if pathlib.Path(CHROME).exists() else {}


def render(HTML, OUTDIR) -> list:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    for old in OUTDIR.glob("slide_*.png"):
        old.unlink()
    shots = []
    with sync_playwright() as p:
        browser = p.chromium.launch(**chromium_kwargs())
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=SCALE)
        page.goto(HTML.as_uri(), wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")
        page.wait_for_timeout(600)
        ids = page.eval_on_selector_all("section.slide", "els => els.map(e => e.id)")
        if not ids:
            sys.exit("nessuna slide trovata")
        for i, sid in enumerate(ids, start=1):
            out = OUTDIR / f"slide_{i:02d}_{sid}.png"
            page.locator(f"#{sid}").screenshot(path=str(out))
            shots.append(out)
        browser.close()
    print(f"render: {len(shots)} slide a {W * SCALE}x{H * SCALE}")
    return shots


def to_pdf(shots: list, PDF) -> None:
    layout = img2pdf.get_layout_fun((img2pdf.in_to_pt(13.333), img2pdf.in_to_pt(7.5)))
    with open(PDF, "wb") as fh:
        img2pdf.convert([str(s) for s in shots], outputstream=fh, layout_fun=layout)
    print(f"{PDF.name}: {PDF.stat().st_size / 1024 / 1024:.1f} MB")


def contact_sheet(shots: list, OUTDIR) -> None:
    from PIL import Image
    cols, tw = 5, 384
    th = round(tw * H / W)
    rows = (len(shots) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), "#54565b")
    for i, s in enumerate(shots):
        im = Image.open(s).convert("RGB").resize((tw, th), Image.LANCZOS)
        sheet.paste(im, ((i % cols) * tw, (i // cols) * th))
    out = OUTDIR / "contact_sheet.png"
    sheet.save(out)
    print(f"contact sheet: {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--contact-sheet", action="store_true")
    args = ap.parse_args()
    for d in DOCS:
        print(f"--- {d['html'].name}")
        s = render(d["html"], d["out"])
        to_pdf(s, d["pdf"])
        if args.contact_sheet:
            contact_sheet(s, d["out"])
