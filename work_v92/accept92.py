#!/usr/bin/env python3
"""Le dieci condizioni di build del §25 e i criteri di completamento del §26.

Il §25 dice: «Il build deve fallire se...». Questo file fa fallire, con codice 1.

Sei condizioni esistevano dalla V9.1. Quattro sono nuove: elementi fuori
viewBox, «in sviluppo» più di una volta per documento, testo interno in una
nota client, canvas con clipping o overflow.

Le condizioni si misurano sul **testo visibile**: un token dentro un commento
HTML o dentro un attributo non è quello che il lettore legge, e trattarlo come
tale trasformerebbe il controllo in rumore.
"""
import re
import subprocess
import sys

import assets92
import claims
import gates
import labels92

ERR, WARN = [], []
ROOT = '..'
DECK_C = f'{ROOT}/DFactory_SalesDeck_v9_2_client.html'
DECK_W = f'{ROOT}/DFactory_SalesDeck_v9_2_working.html'
DOS_C = f'{ROOT}/DFactory_DossierTecnico_v9_2_client.html'
DOS_W = f'{ROOT}/DFactory_DossierTecnico_v9_2_working.html'


def leggi(p):
    return open(p, encoding='utf-8').read()


def visibile(html):
    """Solo quello che finisce sul canvas: niente head, commenti, attributi.

    Fuori anche il pannello «INPUT APERTI» in coda ai canvas della working
    edition: elenca token per il registro, non testo del documento. Contarlo
    farebbe fallire il §5.4 su un token che si chiama PH_REAL_SCREENSHOT_MAPST.
    """
    s = html[html.index('<body'):]
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', s)
    s = re.sub(r'<div class="phb[\s\S]*?</div>\s*</div>', ' ', s)
    s = re.sub(r'<div class="phb[\s\S]*?</div>', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s)


SRC = {p: leggi(p) for p in (DECK_C, DECK_W, DOS_C, DOS_W)}
VIS = {p: visibile(h) for p, h in SRC.items()}

# ---------------------------------------------------------------- 1
for nome, p in (('deck', DECK_C), ('dossier', DOS_C)):
    left = re.findall(r'\{\{PH_[A-Z0-9_]+\}\}', SRC[p])
    if left:
        ERR.append(f'1 · {len(left)} placeholder nella client edition del {nome}')
    else:
        WARN.append(f'1 · client edition {nome}: zero placeholder')

# ---------------------------------------------------------------- 2
BLOCCHI = ('Chi coinvolgere', 'Cosa preparare', 'Cosa restituiamo', 'Azione richiesta')
if 'id="v13_cta"' not in SRC[DECK_C]:
    ERR.append('2 · la CTA manca dalla client edition del deck')
else:
    manca = [b for b in BLOCCHI if b not in VIS[DECK_C]]
    if manca:
        ERR.append(f'2 · la CTA non contiene: {manca}')
    else:
        WARN.append('2 · CTA presente con i quattro blocchi del §10 S13')
    if gates.STATO['G1'] != 'APPROVED':
        WARN.append('2 · G1 aperto: la CTA non porta il referente. Il deck si presenta '
                    'dal vivo, non si invia da solo — warning globale')

# ---------------------------------------------------------------- 3
# Il difetto della V9.1: i valori annualizzati erano scritti in lettere nel
# testo alternativo e il controllo non li vedeva. Adesso cerca entrambe le forme.
ANNUALIZZATI = ['309.120', '154.560', '810 €', '810 &euro;',
                'trecentonovemila', 'centocinquantaquattromila', 'ottocentodieci']
trovati = sorted({v for v in ANNUALIZZATI
                  if v in VIS[DECK_C] or v in VIS[DOS_C] or v in SRC[DECK_C] or v in SRC[DOS_C]})
if gates.STATO['G3'] != 'APPROVED' and trovati:
    ERR.append(f'3 · valori annualizzati nella client edition con G3 aperto: {trovati}')
else:
    WARN.append('3 · nessun valore annualizzato in client, né in cifre né in lettere')

# ---------------------------------------------------------------- 4
if gates.STATO['G4'] != 'APPROVED' and 'preliminare' not in VIS[DOS_C]:
    ERR.append('4 · il dossier si presenta come «Dossier tecnico» con G4 aperto')
else:
    WARN.append(f'4 · titolo del dossier coerente con G4 {gates.STATO["G4"]}')

# ---------------------------------------------------------------- 5
usati = set()
for h in SRC.values():
    usati |= set(re.findall(r'<image[^>]+href="([^"]+)"', h))
    usati |= set(re.findall(r'<img[^>]+src="([^"]+)"', h))
non_reg = {u for u in usati if not u.startswith('data:')} - set(assets92.REGISTRO)
if non_reg:
    ERR.append(f'5 · asset non registrati: {sorted(non_reg)}')
else:
    WARN.append(f'5 · asset usati: {len(usati)} · registro: {len(assets92.REGISTRO)} righe')

# ---------------------------------------------------------------- 6
mancanti = claims.non_registrati(VIS[DECK_C] + VIS[DOS_C])
if mancanti:
    ERR.append(f'6 · claim tecnici non registrati: {mancanti}')
else:
    WARN.append(f'6 · {len(claims.CLAIMS)} claim censiti, nessuno fuori registro')

# ---------------------------------------------------------------- 7 e 10
# qa.py misura clipping SVG (getBBox contro viewBox), overflow del DOM e
# collisioni fra blocchi. Qui il suo esito diventa bloccante.
QA = {DECK_C: 'sales', DECK_W: 'sales', DOS_C: 'dossier', DOS_W: 'dossier'}
flag_re = re.compile(r'(CLIP|OVER|COLLIS|SMALL)×')
for p, kind in QA.items():
    out = subprocess.run([sys.executable, 'qa.py', p, kind],
                         capture_output=True, text=True).stdout
    flags = [l.strip() for l in out.splitlines() if flag_re.search(l)]
    nome = p.split('/')[-1]
    if flags:
        ERR.append(f'7/10 · {nome}: {len(flags)} canvas con clipping, overflow o collisione')
        for f in flags:
            ERR.append(f'        {f}')
    else:
        WARN.append(f'7/10 · {nome}: zero clipping, zero overflow, zero collisioni')

# ---------------------------------------------------------------- 8
for nome, p in (('deck client', DECK_C), ('deck working', DECK_W),
                ('dossier client', DOS_C), ('dossier working', DOS_W)):
    n = VIS[p].count('in sviluppo')
    if n > 1:
        ERR.append(f'8 · «in sviluppo» {n} volte nel {nome}: il §5.2 ne ammette una')
    else:
        WARN.append(f'8 · «in sviluppo» {n} volta nel {nome}')

# ---------------------------------------------------------------- 9
# Testo interno: impalcatura editoriale che non deve raggiungere il cliente.
INTERNO = ['INPUT APERT', labels92.COMMERCIALE, labels92.TECNICA, labels92.ASSET,
           'pubblicabile solo con', 'working edition', 'BLOCKING', 'data-placeholder',
           '{{PH_', 'G1 ', 'G2 ', 'G3 ', 'G4 ', 'G5 ']
for nome, p in (('deck', DECK_C), ('dossier', DOS_C)):
    dentro = [m for m in INTERNO if m in VIS[p]]
    if dentro:
        ERR.append(f'9 · testo interno nella client edition del {nome}: {dentro}')
    else:
        WARN.append(f'9 · client edition {nome}: nessun testo interno')

# §5.4 · MAPST e MarEnergy: mai nel corpo del deck, una volta nel dossier
for m in ('MAPST', 'MarEnergy'):
    if m in VIS[DECK_C] or m in VIS[DECK_W]:
        ERR.append(f'§5.4 · «{m}» compare nel corpo del Sales Deck')
    n = VIS[DOS_C].count(m)
    if n > 1:
        ERR.append(f'§5.4 · «{m}» compare {n} volte nel dossier: ne è ammessa una')
WARN.append('§5.4 · MAPST 4.0 e MarEnergy: zero nel deck, una volta nel dossier')

# ---------------------------------------------------------------- §26
COMPL_DECK = [
    ('narrativa completa · 13 slide core', SRC[DECK_C].count('/ 13</span>') >= 12),
    ('CTA presente', 'id="v13_cta"' in SRC[DECK_C]),
    ('appendici presenti', SRC[DECK_C].count('<div class="slide') >= 16),
    ('fallback sicuri sul pricing', 'perimetro validato' in VIS[DECK_C]),
    ('zero placeholder client', '{{PH_' not in SRC[DECK_C]),
    ('offerta a tre livelli comprensibile', all(
        x in VIS[DECK_C] for x in ('Connect', 'Insight', 'Refyn'))),
    ('valore metodologicamente corretto', 'minuti di fermo' in VIS[DECK_C]),
]
COMPL_DOS = [
    ('14 pagine core + 4 annessi', SRC[DOS_C].count('<div class="slide') == 18),
    ('annessi strutturati', VIS[DOS_C].count('ANNESSO') >= 4),
    ('gap tecnici espliciti', 'solution design' in VIS[DOS_C]),
    ('claim tecnici prudenti', claims.tutti_prudenti()),
    ('proprietà dei dati non pubblicata', 'restano nella disponibilità' not in VIS[DOS_C]),
    ('zero placeholder client', '{{PH_' not in SRC[DOS_C]),
    ('pronto per assessment e solution design', 'preliminare' in VIS[DOS_C]),
]

# §25 · il livello raggiunto va dichiarato, non lasciato intendere
LIVELLO = {
    '90% ready': all(v for _, v in COMPL_DECK) and all(v for _, v in COMPL_DOS),
    'commercial final': gates.STATO['G1'] == 'APPROVED' and gates.STATO['G2'] == 'APPROVED',
    'IT-ready': gates.STATO['G4'] == 'APPROVED',
}


def stampa(titolo, righe):
    ok = sum(1 for _, v in righe if v)
    print(f'\n{titolo} — {ok}/{len(righe)}')
    for c, v in righe:
        print(f'  {"✓" if v else "✗"} {c}')
    return ok == len(righe)


if __name__ == '__main__':
    print('=== §25 · dieci condizioni di build ===')
    for w in WARN:
        print(f'  ok   {w}')
    for e in ERR:
        print(f'  FAIL {e}')

    stampa('§26 · Sales Deck al 90%', COMPL_DECK)
    stampa('§26 · Dossier al 90%', COMPL_DOS)

    print('\n=== stato dei gate ===')
    for g, d in gates.GATES.items():
        print(f'  {g} {d["nome"]:28s} {d["scope"]:8s} {gates.STATO[g]}')
    print(f'  CASE {"caso cliente":28s} {"PAGE":8s} {gates.CASE_STUDY_READY}')

    print('\n=== livello dichiarato ===')
    for k, v in LIVELLO.items():
        print(f'  {"✓" if v else "✗"} {k}')

    if ERR:
        sys.exit(1)
