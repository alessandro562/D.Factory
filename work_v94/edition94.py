#!/usr/bin/env python3
"""Deriva working edition e client edition dallo stesso corpo A4.

  [data-ed="working"]  impalcatura editoriale e placeholder
  [data-ed="client"]   la formulazione prudente che li sostituisce

  edition94.py <in> <out> working|client

Per la client edition verifica la §11.4: zero occorrenze di {{PH_...}}.
Se ne trova una il build fallisce, non avvisa.
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


def build(src, dst, mode):
    html = open(src, encoding='utf-8').read()
    if mode == 'working':
        html = strip_attr(html, 'data-ed', 'client')
    else:
        html = strip_attr(html, 'data-ed', 'working')
        left = re.findall(r'\{\{PH_[A-Z0-9_]+\}\}', html)
        if left:
            raise SystemExit(f'§11.4 violata: {len(left)} placeholder nella client edition '
                             f'— {sorted(set(left))[:5]}')
    open(dst, 'w', encoding='utf-8').write(html)
    n = len(re.findall(r'<section[^>]*class="page', html))
    print(f'{dst} · {mode} · {n} pagine')


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], sys.argv[3])
