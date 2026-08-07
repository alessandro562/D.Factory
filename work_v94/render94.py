#!/usr/bin/env python3
"""Render di ogni pagina A4 a PNG, provino a contatto e PDF di verifica.
  render94.py <file.html> <outdir> [<pdf>]
"""
import math
import os
import sys

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
W, H = 794, 1123


def render(html_path, outdir, pdf_path=None, scale=2):
    os.makedirs(outdir, exist_ok=True)
    url = 'file://' + os.path.abspath(html_path)
    shots = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME,
                              args=['--no-sandbox', '--force-color-profile=srgb'])
        pg = b.new_page(viewport={'width': W + 60, 'height': 1000},
                        device_scale_factor=scale)
        pg.goto(url, wait_until='networkidle')
        pg.wait_for_timeout(400)
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(400)
        ids = pg.eval_on_selector_all('.page', 'els => els.map(e => e.id)')
        for i, sid in enumerate(ids, 1):
            path = os.path.join(outdir, f'{i:02d}_{sid}.png')
            pg.query_selector(f'#{sid}').screenshot(path=path)
            shots.append(path)
        if pdf_path:
            pg.emulate_media(media='print')
            pg.pdf(path=pdf_path, width=f'{W}px', height=f'{H}px',
                   print_background=True, margin={'top': '0', 'bottom': '0',
                                                  'left': '0', 'right': '0'})
        b.close()
    return shots


def contatto(shots, out, cols=6, thumb_w=250, bg=(22, 22, 22)):
    tw, th = thumb_w, int(thumb_w * H / W)
    pad, gap, lab = 20, 12, 20
    rows = math.ceil(len(shots) / cols)
    sheet = Image.new('RGB', (pad * 2 + cols * tw + (cols - 1) * gap,
                              pad * 2 + rows * (th + lab) + (rows - 1) * gap), bg)
    d = ImageDraw.Draw(sheet)
    for i, s in enumerate(shots):
        im = Image.open(s).convert('RGB').resize((tw, th), Image.LANCZOS)
        x = pad + (i % cols) * (tw + gap)
        y = pad + (i // cols) * (th + gap + lab)
        sheet.paste(im, (x, y))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(90, 90, 90))
        d.text((x + 2, y + th + 4), os.path.basename(s).replace('.png', ''),
               fill=(190, 190, 190))
    sheet.save(out)
    return out


if __name__ == '__main__':
    html, outdir = sys.argv[1], sys.argv[2]
    pdf = sys.argv[3] if len(sys.argv) > 3 else None
    shots = render(html, outdir, pdf)
    foglio = os.path.join(outdir, '_contatto.png')
    contatto(shots, foglio)
    print(f'{len(shots)} pagine · {outdir} · provino {foglio}' + (f' · pdf {pdf}' if pdf else ''))
