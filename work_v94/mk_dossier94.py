#!/usr/bin/env python3
"""Dossier tecnico V9.4 · assembla le 22 pagine A4 del corpo master.

18 pagine core + 4 annessi, un file per pagina in dossier94_parts/.
Il conteggio scende da 22 a 18 nel core perche' la V9.3 aveva due pagine —
catena funzionale e base comune — che dicevano lo stesso argomento due volte,
e perche' entra la pagina 02 «Come si legge», che nel formato slide non
c'era: e' quella che rende leggibile per pezzi un documento di ventidue
pagine.

L'intestazione non si scrive a mano su ventidue pagine: si scrive una volta
qui. Ogni parte porta il token {{HD|<sezione>|<numerazione>}}.
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'work_v93'))
import ph91

SEZIONI = [('0', 'Come si legge'), ('1', 'Prodotto'), ('2', 'Dati'),
           ('3', 'Misure'), ('4', 'Delivery'), ('A', 'Annessi')]

ORDINE = [
    'p01_cover', 'p02_lettura', 'p03_executive', 'p04_catena',
    'p05_connect', 'p06_insight', 'p07_refyn', 'p08_matrice',
    'p09_acquisizione', 'p10_contesto', 'p11_architettura', 'p12_security',
    'p13_oee', 'p14_energia', 'p15_output',
    'p16_delivery', 'p17_servizi', 'p18_chiusura',
    'pa1_compatibilita', 'pa2_sizing', 'pa3_requisiti', 'pa4_kpi',
]
# le pagine senza intestazione: copertina e chiusura non hanno navigazione
SENZA_HD = {'p01_cover', 'p18_chiusura'}
# esenti dal paragrafo esplicativo del §12.2
SENZA_PAR = {'p01_cover', 'p18_chiusura'}


def testata(attiva, numerazione):
    voci = []
    for chiave, nome in SEZIONI:
        cls = ' class="on"' if chiave == attiva else ''
        voci.append(f'<span{cls}><i>{chiave}</i>{nome}</span>')
    return ('<div class="hd"><div class="nav">' + ''.join(voci) +
            f'</div><div class="pg">{numerazione}</div></div>')


def espandi(html, nome):
    def sub(m):
        return testata(m.group(1), m.group(2))
    out, n = re.subn(r'\{\{HD\|([^|]+)\|([^}]+)\}\}', sub, html)
    atteso = 0 if nome in SENZA_HD else 1
    assert n == atteso, f'{nome}: {n} testate, ne servono {atteso}'
    return out


parts = []
for nome in ORDINE:
    p = os.path.join('dossier94_parts', nome + '.html')
    assert os.path.exists(p), 'manca la pagina ' + p
    parts.append(espandi(open(p, encoding='utf-8').read().rstrip(), nome))

body = '<div class="doc">\n\n' + '\n\n\n'.join(parts) + '\n\n</div>\n'
open('dossier94_master.html', 'w', encoding='utf-8').write(body)

used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', body))
undeclared = used - set(ph91.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
residuo = re.findall(r'\{\{(?!PH_)[^}]+\}\}', body)
assert not residuo, f'token non espansi: {set(residuo)}'
n = len(re.findall(r'<section[^>]*class="page', body))
print(f'dossier94_master.html · {n} pagine A4 · {len(used)} placeholder distinti')


def visibile(h):
    """Il documento e' quello che il lettore vede: i commenti del sorgente e
    l'impalcatura della working edition non contano."""
    h = re.sub(r'<!--.*?-->', ' ', h, flags=re.S)
    h = re.sub(r'<div class="phb".*?</div>\s*</div>', ' ', h, flags=re.S)
    return h


def parole(testo):
    testo = re.sub(r'<[^>]+>', ' ', testo)
    testo = re.sub(r'&[a-z]+;|&#\d+;', 'x', testo)
    return len([w for w in testo.split() if any(c.isalnum() for c in w)])


# §12.2 · il paragrafo esplicativo, 45-100 parole su ogni pagina core.
print('  §12.2 · paragrafo esplicativo, 45-100 parole per pagina core')
fuori = []
for nome in ORDINE:
    if nome in SENZA_PAR or nome.startswith('pa'):
        continue
    pg = open(os.path.join('dossier94_parts', nome + '.html'), encoding='utf-8').read()
    pars = re.findall(r'<div class="par[^"]*"[^>]*>(.*?)</div>', pg, re.S)
    k = parole(' '.join(pars))
    ok = 45 <= k <= 100
    if not ok:
        fuori.append((nome, k))
    print(f'    {nome:22s} {k:>3} parole {"ok" if ok else "FUORI INTERVALLO"}')
assert not fuori, f'§12.2 violato: {fuori}'

vis = visibile(body)
core = vis.split('id="pa1_compatibilita"')[0]
annessi = vis[vis.index('id="pa1_compatibilita"'):]
sopra = []
for expr, tetto, dove, ambito in (
        ('solution design', 8, vis, 'nel documento'),
        ('da verificare', 1, core, 'nel core'),
        ('da verificare', 2, annessi, 'negli annessi'),
        ('da approvare', 0, vis, 'nel documento'),
        ('da nominare', 0, vis, 'nel documento'),
        ('chi decide', 0, core, 'nel core'),
        ('owner', 0, core, 'nel core')):
    k = len(re.findall(expr, dove, re.I))
    stato = 'ok' if k <= tetto else 'SOPRA IL TETTO'
    if k > tetto:
        sopra.append((expr, ambito, k, tetto))
    print(f'  §12.5 · «{expr}» {ambito}: {k} (tetto {tetto}) {stato}')
assert not sopra, f'§12.5 violato: {sopra}'
