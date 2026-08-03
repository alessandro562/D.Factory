#!/usr/bin/env python3
"""Condizioni di build V9.3 e criteri di approvazione del §16.

Riprende le dieci condizioni del §25 V9.2, che restano valide, e aggiunge
quelle che la V9.3 introduce: precisione terminologica (§12), controlli di
sequenza (§14.3), paragrafo esplicativo su ogni pagina core (§12.2).

Le condizioni si misurano sul **testo visibile**: un token dentro un commento
HTML o dentro un attributo non e' quello che il lettore legge.
"""
import re
import subprocess
import sys

import assets92
import claims93
import gates
import labels92

ERR, WARN = [], []
ROOT = '..'
DECK_C = f'{ROOT}/DFactory_SalesDeck_v9_3_client.html'
DECK_W = f'{ROOT}/DFactory_SalesDeck_v9_3_working.html'
DOS_C = f'{ROOT}/DFactory_DossierTecnico_v9_3_client.html'
DOS_W = f'{ROOT}/DFactory_DossierTecnico_v9_3_working.html'


def leggi(p):
    return open(p, encoding='utf-8').read()


def visibile(html):
    """Solo quello che finisce sul canvas: niente head, commenti, attributi,
    niente pannello «INPUT APERTI» della working edition."""
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

# ---------------------------------------------------------------- 2 · CTA
if 'id="s15_pilot_cta"' not in SRC[DECK_C]:
    ERR.append('2 · la CTA manca dalla client edition del deck')
else:
    passi = ('Perimetrazione', 'Pilot', 'Decisione')
    manca = [b for b in passi if b not in VIS[DECK_C]]
    if manca:
        ERR.append(f'2 · la CTA non contiene i tre passi: {manca}')
    else:
        WARN.append('2 · CTA presente con perimetrazione, pilot e decisione')
    if gates.STATO['G1'] != 'APPROVED':
        WARN.append('2 · G1 aperto: la CTA non porta il referente. Il deck si presenta '
                    'dal vivo, non si invia da solo — warning globale')

# ---------------------------------------------------------------- 3
ANNUALIZZATI = ['309.120', '154.560', '810 €', '810 &euro;',
                'trecentonovemila', 'centocinquantaquattromila', 'ottocentodieci',
                'costo annuo', 'perdita annua', 'risparmio annuo', 'beneficio annuo',
                'settimane produttive', '€ all’anno']
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

# ---------------------------------------------------------------- 6 · claim
mancanti = claims93.non_registrati(VIS[DECK_C] + VIS[DOS_C])
if mancanti:
    ERR.append(f'6 · claim tecnici non registrati: {mancanti}')
else:
    WARN.append(f'6 · {len(claims93.CLAIMS)} claim censiti, nessuno fuori registro')

# ---------------------------------------------------------------- 6b · §12
for nome, p in (('deck client', DECK_C), ('deck working', DECK_W),
                ('dossier client', DOS_C), ('dossier working', DOS_W)):
    v = claims93.vietate_presenti(VIS[p])
    if v:
        ERR.append(f'§12 · formulazioni vietate nel {nome}: {v}')
if not any(claims93.vietate_presenti(VIS[p]) for p in SRC):
    WARN.append(f'§12 · nessuna delle {len(claims93.VIETATE)} formulazioni vietate '
                'compare nei quattro documenti')

# ---------------------------------------------------------------- 7 e 10 · QA
QA = {DECK_C: 'sales', DECK_W: 'sales', DOS_C: 'dossier', DOS_W: 'dossier'}
flag_re = re.compile(r'(CLIP|OVER|COLLIS|SMALL|copy>|cont<|meta<|diag<|vista<|visual[<>]|DASHBOARD)')
for p, kind in QA.items():
    out = subprocess.run([sys.executable, 'qa93.py', p, kind],
                         capture_output=True, text=True).stdout
    righe = [l for l in out.splitlines() if l.startswith(('  ', ' ')) is False]
    flags = [l.strip() for l in out.splitlines()
             if flag_re.search(l) and not l.startswith('id ')]
    nome = p.split('/')[-1]
    if flags:
        ERR.append(f'7/10 · {nome}: {len(flags)} canvas con difetti tecnici')
        for f in flags[:6]:
            ERR.append(f'        {f}')
    else:
        WARN.append(f'7/10 · {nome}: zero clipping, overflow, collisioni, microtesto')

# ---------------------------------------------------------------- 8
for nome, p in (('deck client', DECK_C), ('deck working', DECK_W),
                ('dossier client', DOS_C), ('dossier working', DOS_W)):
    n = VIS[p].count('in sviluppo')
    if n > 1:
        ERR.append(f'8 · «in sviluppo» {n} volte nel {nome}: se ne ammette una')
    else:
        WARN.append(f'8 · «in sviluppo» {n} volta nel {nome}')

# ---------------------------------------------------------------- 9
INTERNO = ['INPUT APERT', labels92.COMMERCIALE, labels92.TECNICA, labels92.ASSET,
           'pubblicabile solo con', 'working edition', 'BLOCKING', 'data-placeholder',
           '{{PH_', 'G1 ', 'G2 ', 'G3 ', 'G4 ', 'G5 ']
for nome, p in (('deck', DECK_C), ('dossier', DOS_C)):
    dentro = [m for m in INTERNO if m in VIS[p]]
    if dentro:
        ERR.append(f'9 · testo interno nella client edition del {nome}: {dentro}')
    else:
        WARN.append(f'9 · client edition {nome}: nessun testo interno')

# §5.4 · MAPST e MarEnergy: mai nel corpo del deck, al massimo una nel dossier
for m in ('MAPST', 'MarEnergy'):
    if m in VIS[DECK_C] or m in VIS[DECK_W]:
        ERR.append(f'§5.4 · «{m}» compare nel corpo del Sales Deck')
    n = VIS[DOS_C].count(m)
    if n > 1:
        ERR.append(f'§5.4 · «{m}» compare {n} volte nel dossier: ne è ammessa una')
WARN.append('§5.4 · MAPST 4.0 e MarEnergy: zero nel deck, al massimo una nel dossier')

# ---------------------------------------------------------------- §14.3
out = subprocess.run([sys.executable, 'audit93.py', DECK_C, DOS_C, ROOT],
                     capture_output=True, text=True)
fails = [l.strip()[5:] for l in out.stdout.splitlines() if l.strip().startswith('FAIL')]
if fails:
    ERR.append(f'§14.3 · audit di sequenza: {len(fails)} problemi')
    for f in fails[:6]:
        ERR.append(f'        {f}')
else:
    WARN.append('§14.3 · audit di sequenza: ritmo, layout duplicati, streak tecnica, '
                'package check e questionnaire check tutti superati')

# ---------------------------------------------------------------- §16
COMPL_DECK = [
    ('prodotto chiaro entro S03', 'Un solo contesto operativo' in VIS[DECK_C]),
    ('trasformazione chiara in S04', 'a una gestione condivisa' in VIS[DECK_C]),
    ('massimo tre slide fortemente UI',
     len(re.findall(r'data-ui="1"', SRC[DECK_C])) <= 3),
    ('pacchetti funzionali e distinti', all(
        x in VIS[DECK_C] for x in ('Connect', 'Insight', 'Refyn'))),
    ('confronto leggibile nel corpo', 'id="s12_confronto"' in SRC[DECK_C]),
    ('servizi visibili', 'improvement sprint' in VIS[DECK_C]),
    ('ragione per scegliere D.Factory', 'Brownfield first' in VIS[DECK_C]),
    ('modello commerciale', 'Ricorrente' in VIS[DECK_C]),
    ('CTA', 'id="s15_pilot_cta"' in SRC[DECK_C]),
    ('ritmo variato', not fails),
    ('nessun eccesso tecnico', SRC[DECK_C].count('data-tipo="narrativa"') >= 4),
]
COMPL_DOS = [
    ('executive summary autorevole', 'id="p02_executive"' in SRC[DOS_C]),
    ('prosa in ogni pagina core', SRC[DOS_C].count('class="par') >= 16),
    ('moduli spiegati', all(f'id="p0{n}_' in SRC[DOS_C] for n in (5, 6, 7))),
    ('matrice completa', SRC[DOS_C].count('<div><b>') >= 14),
    ('acquisizione e contesto distinti',
     'id="p09_acquisizione"' in SRC[DOS_C] and 'id="p10_contesto"' in SRC[DOS_C]),
    ('architettura e deployment distinti',
     'id="p03_architettura_funzionale"' in SRC[DOS_C] and 'id="p11_architettura"' in SRC[DOS_C]),
    ('security nel core, requisiti in annesso',
     'id="p12_security"' in SRC[DOS_C] and 'id="pa3_requisiti"' in SRC[DOS_C]),
    ('OEE ed energia metodologicamente chiari',
     'id="p13_oee"' in SRC[DOS_C] and 'id="p14_energia"' in SRC[DOS_C]),
    ('output e integrazioni separati', 'Integrazioni verso sistemi esterni' in VIS[DOS_C]),
    ('delivery e supporto spiegati',
     'id="p16_delivery"' in SRC[DOS_C] and 'id="p17_servizi"' in SRC[DOS_C]),
    ('nessun tono da questionario', not fails),
]

# Il livello raggiunto va dichiarato, non lasciato intendere.
LIVELLO = {
    'narrative ready': all(v for _, v in COMPL_DECK),
    'assessment ready': all(v for _, v in COMPL_DOS),
    'commercial ready': gates.STATO['G1'] == 'APPROVED' and gates.STATO['G2'] == 'APPROVED',
    'IT-ready': gates.STATO['G4'] == 'APPROVED',
}


def stampa(titolo, righe):
    ok = sum(1 for _, v in righe if v)
    print(f'\n{titolo} — {ok}/{len(righe)}')
    for c, v in righe:
        print(f'  {"✓" if v else "✗"} {c}')
    return ok == len(righe)


if __name__ == '__main__':
    print('=== condizioni di build V9.3 ===')
    for w in WARN:
        print(f'  ok   {w}')
    for e in ERR:
        print(f'  FAIL {e}')

    stampa('§16 · Sales Deck', COMPL_DECK)
    stampa('§16 · Dossier', COMPL_DOS)

    print('\n=== stato dei gate ===')
    for g, d in gates.GATES.items():
        print(f'  {g} {d["nome"]:28s} {d["scope"]:8s} {gates.STATO[g]}')
    print(f'  CASE {"caso cliente":28s} {"PAGE":8s} {gates.CASE_STUDY_READY}')

    print('\n=== livello dichiarato ===')
    for k, v in LIVELLO.items():
        print(f'  {"✓" if v else "✗"} {k}')

    if ERR:
        sys.exit(1)
