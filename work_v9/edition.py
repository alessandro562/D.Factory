#!/usr/bin/env python3
"""Deriva working edition e client edition dallo stesso corpo.

Il corpo master contiene entrambe le varianti:
  [data-ed="working"]  impalcatura editoriale e placeholder
  [data-ed="client"]   la formulazione prudente che li sostituisce
  [data-ph-page]       canvas che nella client edition non esiste

  edition.py <in> <out> working|client

Alla fine, per la client edition, verifica la §11.4: zero occorrenze di
{{PH_...}}. Se ne trova una il build fallisce, non avvisa.
"""
import re
import sys


def strip_attr(html, attr, value=None):
    """Rimuove ogni elemento che porta l'attributo, con il suo contenuto."""
    out = []
    i = 0
    pat = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?\b%s\s*=\s*"([^"]*)"[^>]*?(/?)>' % attr)
    while True:
        m = pat.search(html, i)
        if not m:
            out.append(html[i:])
            break
        if value is not None and m.group(2) != value:
            out.append(html[i:m.end()])
            i = m.end()
            continue
        out.append(html[i:m.start()])
        if m.group(3) == '/':                       # elemento vuoto
            i = m.end()
            continue
        tag = m.group(1)
        depth, j = 1, m.end()
        open_re = re.compile(r'<%s\b' % tag, re.I)
        close_re = re.compile(r'</%s\s*>' % tag, re.I)
        while depth:
            no = open_re.search(html, j)
            nc = close_re.search(html, j)
            if not nc:
                raise SystemExit(f'tag {tag} non chiuso a offset {j}')
            if no and no.start() < nc.start():
                depth += 1
                j = no.end()
            else:
                depth -= 1
                j = nc.end()
        i = j
    return ''.join(out)


# Rinumerazione della client edition: escludere un canvas lascerebbe un buco
# nella numerazione, e un buco si legge come un errore. La mappa e' esplicita
# perche' sia verificabile, e finisce nel changelog.
RENUM = {
    'deck9_c_body.html': [
        ('>13 / 13<', None),                       # CTA: canvas gia' escluso
        ('>02 / 13<', '>02 / 12<'), ('>03 / 13<', '>03 / 12<'),
        ('>04 / 13<', '>04 / 12<'), ('>05 / 13<', '>05 / 12<'),
        ('>06 / 13<', '>06 / 12<'), ('>07 / 13<', '>07 / 12<'),
        ('>08 / 13<', '>08 / 12<'), ('>09 / 13<', '>09 / 12<'),
        ('>10 / 13<', '>10 / 12<'), ('>11 / 13<', '>11 / 12<'),
        ('>12 / 13<', '>12 / 12<'),
        ('>A4<', '>A3<'), ('>A5<', '>A4<'),        # A3 pricing e' escluso
        ('assunzioni in appendice A5', 'assunzioni in appendice A4'),
    ],
}


def build(src, dst, mode):
    html = open(src, encoding='utf-8').read()
    if mode == 'working':
        html = strip_attr(html, 'data-ed', 'client')
        removed = []
    else:
        html = strip_attr(html, 'data-ed', 'working')
        removed = re.findall(r'<div data-ph-page="[^"]*" class="slide[^>]*id="([^"]+)"', html)
        html = strip_attr(html, 'data-ph-page')
        left = re.findall(r'\{\{PH_[A-Z0-9_]+\}\}', html)
        if left:
            raise SystemExit(f'§11.4 violata: {len(left)} placeholder nella client edition '
                             f'— {sorted(set(left))[:5]}')
        for a, b in RENUM.get(dst, []):
            if b is not None:
                html = html.replace(a, b)
    open(dst, 'w', encoding='utf-8').write(html)
    n = len(re.findall(r'<div[^>]*class="slide', html))
    extra = f' · canvas esclusi: {", ".join(removed)}' if removed else ''
    print(f'{dst} · {mode} · {n} canvas{extra}')
    return removed


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], sys.argv[3])
