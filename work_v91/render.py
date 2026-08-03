#!/usr/bin/env python3
"""Render ogni .slide di un HTML a PNG 1280x720, provino a contatto, provino
piccolo (640x360), variante gerarchia (grayscale + blur) e PDF di verifica."""
import sys, os, math, argparse
from playwright.sync_api import sync_playwright
from PIL import Image, ImageFilter, ImageDraw

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
W, H = 1280, 720


def render(html_path, outdir, scale=2):
    os.makedirs(outdir, exist_ok=True)
    url = 'file://' + os.path.abspath(html_path)
    shots, console, requests = [], [], []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox', '--force-color-profile=srgb'])
        pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=scale)
        pg.on('console', lambda m: console.append(f'{m.type}: {m.text}') if m.type in ('error', 'warning') else None)
        pg.on('request', lambda r: requests.append(r.url) if not r.url.startswith(('file://', 'data:')) else None)
        pg.goto(url, wait_until='networkidle')
        pg.wait_for_timeout(400)
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(400)
        ids = pg.eval_on_selector_all('.slide', 'els => els.map(e => e.id)')
        for i, sid in enumerate(ids, 1):
            el = pg.query_selector(f'#{sid}')
            path = os.path.join(outdir, f'{i:02d}_{sid}.png')
            el.screenshot(path=path)
            shots.append(path)
        b.close()
    return shots, console, requests


def contact(shots, out, cols=4, thumb_w=420, bg=(22, 22, 22), label=True):
    tw, th = thumb_w, int(thumb_w * H / W)
    pad, gap = 26, 16
    rows = math.ceil(len(shots) / cols)
    cw = pad * 2 + cols * tw + (cols - 1) * gap
    ch = pad * 2 + rows * (th + (22 if label else 0)) + (rows - 1) * gap
    sheet = Image.new('RGB', (cw, ch), bg)
    d = ImageDraw.Draw(sheet)
    for i, s in enumerate(shots):
        im = Image.open(s).convert('RGB').resize((tw, th), Image.LANCZOS)
        x = pad + (i % cols) * (tw + gap)
        y = pad + (i // cols) * (th + gap + (22 if label else 0))
        sheet.paste(im, (x, y))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(90, 90, 90))
        if label:
            d.text((x + 2, y + th + 5), os.path.basename(s).replace('.png', ''), fill=(190, 190, 190))
    sheet.save(out)
    return out


def hierarchy(shots, out, cols=4, thumb_w=420):
    tw, th = thumb_w, int(thumb_w * H / W)
    pad, gap = 26, 16
    rows = math.ceil(len(shots) / cols)
    sheet = Image.new('RGB', (pad * 2 + cols * tw + (cols - 1) * gap,
                              pad * 2 + rows * th + (rows - 1) * gap), (22, 22, 22))
    for i, s in enumerate(shots):
        im = Image.open(s).convert('L').convert('RGB').resize((tw, th), Image.LANCZOS)
        im = im.filter(ImageFilter.GaussianBlur(2.4))
        sheet.paste(im, (pad + (i % cols) * (tw + gap), pad + (i // cols) * (th + gap)))
    sheet.save(out)
    return out


def to_pdf(shots, out):
    ims = [Image.open(s).convert('RGB') for s in shots]
    ims[0].save(out, save_all=True, append_images=ims[1:], resolution=150.0)
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('html'); ap.add_argument('outdir'); ap.add_argument('prefix')
    ap.add_argument('--cols', type=int, default=4)
    a = ap.parse_args()
    shots, console, reqs = render(a.html, a.outdir)
    print(f'{len(shots)} render')
    print('console errors/warnings:', console or 'none')
    print('network requests:', reqs or 'none')
    contact(shots, f'{a.prefix}_contact.png', cols=a.cols)
    contact(shots, f'{a.prefix}_small_contact.png', cols=a.cols, thumb_w=213, label=False)
    hierarchy(shots, f'{a.prefix}_hierarchy.png', cols=a.cols)
    to_pdf(shots, f'{a.prefix}.pdf')
    print('done ->', a.prefix)
