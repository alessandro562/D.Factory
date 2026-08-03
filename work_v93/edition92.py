#!/usr/bin/env python3
"""Deriva working edition e client edition dal corpo master V9.2.

Rispetto alla V9.1 cambiano due cose.

1. Un canvas condizionale esce dalla client edition soltanto se il suo gate
   non è approvato. Prima usciva sempre: funzionava perché tutti i gate erano
   aperti, ma era un caso, non una regola.

2. La working edition passa dal token all'etichetta leggibile (§8.3). Il token
   resta, in data-placeholder, dove lo cerca il registro.

  edition92.py <in> <out> working|client
"""
import re
import sys

import gates
import labels92
from edition import strip_attr

RENUM = {
    # Con G2 e G3 aperti escono A3 pricing e A5 assunzioni: restano A1, A2 e
    # la FAQ, che deve chiamarsi A3. Un buco nella numerazione si legge come
    # un errore, e questa mappa finisce nel changelog.
    'deck92_c_body.html': [('>A4<', '>A3<')],
}


def gate_aperto(nome):
    if nome == 'CASE_STUDY_READY':
        return gates.CASE_STUDY_READY != 'APPROVED'
    return gates.STATO.get(nome, 'OPEN') != 'APPROVED'


def build(src, dst, mode):
    html = open(src, encoding='utf-8').read()
    removed = []
    if mode == 'working':
        html = strip_attr(html, 'data-ed', 'client')
        html, n = labels92.applica(html)
        print(f'  §8.3 · {n} token sostituiti da etichette leggibili')
    else:
        html = strip_attr(html, 'data-ed', 'working')
        for g, i in re.findall(r'data-ph-page="([^"]+)"[^>]*id="([^"]+)"', html):
            if gate_aperto(g):
                removed.append(f'{i} ({g})')
                html = strip_attr(html, 'data-ph-page', g)
        html = re.sub(r'\s+data-ph-page="[^"]*"', '', html)
        left = re.findall(r'\{\{PH_[A-Z0-9_]+\}\}', html)
        if left:
            raise SystemExit(f'§8.4 violata: {len(left)} placeholder nella client edition '
                             f'— {sorted(set(left))[:5]}')
        for a, b in RENUM.get(dst, []):
            html = html.replace(a, b)
    open(dst, 'w', encoding='utf-8').write(html)
    n = len(re.findall(r'<div[^>]*class="slide', html))
    extra = f' · esclusi: {", ".join(removed)}' if removed else ''
    print(f'{dst} · {mode} · {n} canvas{extra}')
    return removed


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], sys.argv[3])
