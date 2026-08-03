#!/usr/bin/env python3
"""Misura, per ogni canvas, il riquadro dei blocchi di primo livello.

Serve a posizionare tabelle e note senza indovinare: l'altezza di una griglia
dipende dal numero di righe che vanno a capo, e a occhio si sbaglia.
  probe93.py <html> [id1 id2 ...]
"""
import os
import sys

from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

JS = r"""
() => {
  const out = [];
  for (const s of document.querySelectorAll('.slide')) {
    const sb = s.getBoundingClientRect();
    const rows = [];
    for (const e of s.children) {
      const r = e.getBoundingClientRect();
      if (r.width < 2 && r.height < 2) continue;
      rows.push({ cls: (e.className.baseVal || e.className || e.tagName).toString().slice(0, 26),
                  top: Math.round(r.top - sb.top), bottom: Math.round(r.bottom - sb.top),
                  h: Math.round(r.height),
                  txt: (e.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 26) });
    }
    out.push({ id: s.id, rows });
  }
  return out;
}
"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1280, 'height': 720})
    pg.goto('file://' + os.path.abspath(sys.argv[1]), wait_until='networkidle')
    pg.evaluate('document.fonts.ready')
    pg.wait_for_timeout(400)
    data = pg.evaluate(JS)
    b.close()

want = set(sys.argv[2:])
for rec in data:
    if want and rec['id'] not in want:
        continue
    print(f'\n── {rec["id"]}')
    for r in rec['rows']:
        print(f'   {r["top"]:>4} → {r["bottom"]:>4}  h={r["h"]:>3}  {r["cls"]:<26} {r["txt"]}')
