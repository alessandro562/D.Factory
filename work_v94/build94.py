#!/usr/bin/env python3
"""Assembla un HTML A4 autonomo: fonts.css + dossier94.css + corpo.
Uso: build94.py <css> <body> <out> "<title>"

I font viaggiano incorporati in base64: il documento aperto senza rete deve
essere identico a quello aperto con la rete. La verifica finale controlla che
non resti nessun riferimento esterno.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(HERE, '..', 'work_v93', 'assets', 'fonts.css'),
             encoding='utf-8').read()

TPL = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=794">
<title>{title}</title>
<style>
{fonts}
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def build(css_path, body_path, out_path, title):
    css = open(css_path, encoding='utf-8').read()
    body = open(body_path, encoding='utf-8').read()
    html = TPL.format(title=title, fonts=FONTS, css=css, body=body)
    open(out_path, 'w', encoding='utf-8').write(html)
    stripped = re.sub(r'base64,[A-Za-z0-9+/=]+', '', html)
    bad = re.findall(r'(?:src|href)\s*=\s*["\'](https?:|//)', stripped)
    ids = re.findall(r'id="([^"]+)"', stripped)
    dup = {i for i in ids if ids.count(i) > 1}
    pages = len(re.findall(r'<section[^>]*class="page', stripped))
    print(f'{out_path}  {os.path.getsize(out_path)/1024:.0f} KB  ·  {pages} pagine  ·  '
          f'riferimenti esterni: {bad or "nessuno"}  ·  id duplicati: {dup or "nessuno"}')


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
