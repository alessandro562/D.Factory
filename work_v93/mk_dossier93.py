#!/usr/bin/env python3
"""Dossier tecnico V9.3 · assembla i 21 canvas del corpo master.

17 pagine core + 4 annessi, un file per canvas in dossier93_parts/, nell'ordine
del §6 del Fase E Build Master. Il conteggio e' 17 e non 16 perche' il metodo di
misura sta su due pagine: OEE ed energia hanno quattro grandezze ciascuna e una
catena di calcolo, e non entrano su una pagina sola (§5.2 dell'audit).
"""
import os
import re

import ph91

ORDINE = [
    'p01_cover', 'p02_executive', 'p03_architettura_funzionale', 'p04_base_comune',
    'p05_connect', 'p06_insight', 'p07_refyn', 'p08_matrice',
    'p09_acquisizione', 'p10_contesto', 'p11_architettura', 'p12_security',
    'p13_oee', 'p14_energia', 'p15_output',
    'p16_delivery', 'p17_servizi',
    'pa1_compatibilita', 'pa2_sizing', 'pa3_requisiti', 'pa4_kpi',
    'p18_chiusura',
]

parts = []
for nome in ORDINE:
    p = os.path.join('dossier93_parts', nome + '.html')
    assert os.path.exists(p), 'manca il canvas ' + p
    parts.append(open(p, encoding='utf-8').read().rstrip())

body = '<div class="doc">\n\n' + '\n\n\n'.join(parts) + '\n\n</div>\n'
open('dossier93_master.html', 'w', encoding='utf-8').write(body)

used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', body))
undeclared = used - set(ph91.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
n = len(re.findall(r'<div[^>]*class="slide', body))
print(f'dossier93_master.html · {n} canvas · {len(used)} placeholder distinti')

# §12.5 · conteggio delle formule di stato aperto, obiettivo misurabile.
# Si conta il testo che il lettore vede: i commenti del sorgente e
# l'impalcatura della working edition non sono il documento.
def visibile(h):
    h = re.sub(r'<!--.*?-->', ' ', h, flags=re.S)
    h = re.sub(r'<div class="phb".*?</div>\s*</div>', ' ', h, flags=re.S)
    return h

vis = visibile(body)
core = vis.split('id="pa1_compatibilita"')[0]
# §12.2 · il paragrafo esplicativo: 45-100 parole su ogni pagina core.
# La copertina e' esente: non e' una pagina di contenuto.
print('  §12.2 · paragrafo esplicativo, 45-100 parole per pagina core')
fuori = []
for nome in ORDINE:
    if nome in ('p01_cover', 'p18_chiusura') or nome.startswith('pa'):
        continue
    pg = open(os.path.join('dossier93_parts', nome + '.html'), encoding='utf-8').read()
    pars = re.findall(r'<div class="par[^"]*"[^>]*>(.*?)</div>', pg, re.S)
    testo = ' '.join(re.sub(r'<[^>]+>', ' ', x) for x in pars)
    testo = re.sub(r'&[a-z]+;|&#\d+;', 'x', testo)
    k = len([w for w in testo.split() if any(c.isalnum() for c in w)])
    ok = 45 <= k <= 100
    if not ok:
        fuori.append((nome, k))
    print(f'    {nome:30s} {k:>3} parole {"ok" if ok else "FUORI INTERVALLO"}')
assert not fuori, f'§12.2 violato: {fuori}'

annessi = vis[vis.index('id="pa1_compatibilita"'):]
for expr, tetto, dove, ambito in (
        ('solution design', 8, vis, 'nel documento'),
        # §12.5: «da verificare» vive negli annessi. L'unica occorrenza
        # ammessa nel core e' la formulazione che il §2.4 della review D2
        # prescrive per P15: «da verificare sul perimetro».
        ('da verificare', 1, core, 'nel core'),
        ('da verificare', 2, annessi, 'negli annessi'),
        ('da approvare', 0, vis, 'nel documento'),
        ('da nominare', 0, vis, 'nel documento'),
        ('chi decide', 0, core, 'nel core'),
        ('owner', 0, core, 'nel core')):
    k = len(re.findall(expr, dove, re.I))
    stato = 'ok' if k <= tetto else 'SOPRA IL TETTO'
    print(f'  «{expr}» {ambito}: {k} · tetto {tetto} · {stato}')
