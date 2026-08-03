#!/usr/bin/env python3
"""Assembla un HTML autonomo: fonts.css + <css> + <body fragment>.
Uso: build.py <css> <body> <out> "<title>"
"""
import sys, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(HERE, 'assets', 'fonts.css'), encoding='utf-8').read()

TPL = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1280">
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
    # sanity: no network refs
    stripped = re.sub(r'base64,[A-Za-z0-9+/=]+', '', html)
    bad = re.findall(r'(?:src|href)\s*=\s*["\'](https?:|//)', stripped)
    ids = re.findall(r'id="([^"]+)"', stripped)
    dup = {i for i in ids if ids.count(i) > 1}
    print(f'{out_path}  {os.path.getsize(out_path)/1024:.0f} KB  ·  '
          f'{len(re.findall(chr(60)+chr(34)*0+"section", stripped))} sec  ·  '
          f'external refs: {bad or "none"}  ·  duplicate ids: {dup or "none"}')


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
