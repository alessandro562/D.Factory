#!/usr/bin/env python3
"""Sales Deck V9.3 · assembla i 19 canvas del corpo master.

Il corpo e' scritto in deck93_parts/*.html, un file per canvas, nell'ordine
del §6 del Fase E Build Master. Due visuali arrivano verbatim dalla V9.2
perche' il §6 dello storyboard dice «keep»: la vista del fermo e il ranking
delle cause. Tutto il resto e' nuovo o riscritto.
"""
import glob
import os
import re

import ph91

ORDINE = [
    's01_promessa', 's02_problema', 's03_visione', 's04_trasformazione',
    's05_prodotto', 's06_quattro_letture', 's07_priorita', 's08_mappa',
    's09_connect', 's10_insight', 's11_refyn', 's12_confronto',
    's13_perche', 's14_valore', 's15_pilot_cta',
    's16_caso', 'a1_matrice', 'a2_servizi', 'a3_pricing', 'a4_faq', 'a5_assunzioni',
]

parts = []
for nome in ORDINE:
    p = os.path.join('deck93_parts', nome + '.html')
    assert os.path.exists(p), 'manca il canvas ' + p
    parts.append(open(p, encoding='utf-8').read().rstrip())

body = '<div class="doc">\n\n' + '\n\n\n'.join(parts) + '\n\n</div>\n'
open('deck93_master.html', 'w', encoding='utf-8').write(body)

used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', body))
undeclared = used - set(ph91.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
n = len(re.findall(r'<div[^>]*class="slide', body))
cond = re.findall(r'data-ph-page="([^"]+)"[^>]*id="([^"]+)"', body)
print(f'deck93_master.html · {n} canvas · {len(used)} placeholder distinti')
print('  condizionali: ' + ' · '.join(f'{i} ⟵ {g}' for g, i in cond))
