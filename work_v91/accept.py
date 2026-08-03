#!/usr/bin/env python3
"""I sei controlli di build della §14 e i criteri di accettazione della §13.

Il piano dice: «Il build deve fallire se...». Questo file fa fallire.
Esce con codice 1 se una delle sei condizioni non è rispettata.
"""
import re
import sys
import gates
import ph91
import claims

ERR, WARN = [], []


def leggi(p):
    return open(p, encoding='utf-8').read()


DECK_C, DOS_C = leggi('deck91_c_body.html'), leggi('dossier91_c_body.html')
DECK_W, DOS_W = leggi('deck91_w_body.html'), leggi('dossier91_w_body.html')

# 1 · nessun placeholder nella client edition
for nome, h in (('deck', DECK_C), ('dossier', DOS_C)):
    left = re.findall(r'\{\{PH_[A-Z0-9_]+\}\}', h)
    (ERR if left else WARN).append(
        f'1 · placeholder nella client edition del {nome}: {len(left)}'
        if left else f'1 · client edition {nome}: zero placeholder')

# 2 · la CTA deve esserci
if 'id="v13_cta"' not in DECK_C:
    ERR.append('2 · la CTA manca dalla client edition del deck')
else:
    for campo, etichetta in (('Azione richiesta', 'azione richiesta'),
                             ('Chi coinvolgere', 'partecipanti'),
                             ('Cosa restituiamo', 'output')):
        if campo not in DECK_C:
            ERR.append(f'2 · la CTA non contiene {etichetta}')
    WARN.append('2 · CTA presente con partecipanti, output e azione richiesta')
    if gates.STATO['G1'] != 'APPROVED':
        WARN.append('2 · G1 aperto: la CTA non porta il referente, il deck si presenta '
                    'dal vivo ma non si invia')

# 3 · business case pubblicato solo con G3 approvato
annualizzati = ['309.120', '154.560', '810 &euro;', '810 €']
trovati = [v for v in annualizzati if v in DECK_C]
if gates.STATO['G3'] != 'APPROVED' and trovati:
    ERR.append(f'3 · valori annualizzati nella client edition con G3 aperto: {trovati}')
else:
    WARN.append('3 · nessun valore annualizzato con G3 aperto')

# 4 · «Dossier tecnico» senza «preliminare» solo con G4 approvato
prelim = 'preliminare' in DOS_C
if gates.STATO['G4'] != 'APPROVED' and not prelim:
    ERR.append('4 · il dossier si chiama «Dossier tecnico» con G4 aperto')
else:
    WARN.append(f'4 · titolo del dossier coerente con G4 {gates.STATO["G4"]}')

# 5 · ogni asset usato deve essere nel registro
import assets91
usati = set(re.findall(r'<image[^>]+href="([^"]+)"', DECK_C + DOS_C + DECK_W + DOS_W))
non_reg = usati - set(assets91.REGISTRO)
if non_reg:
    ERR.append(f'5 · asset non registrati: {sorted(non_reg)}')
else:
    WARN.append(f'5 · asset usati: {len(usati)} · tutti registrati')

# 6 · ogni claim tecnico deve essere nel Claim Register
mancanti = claims.non_registrati(DECK_C + DOS_C)
if mancanti:
    ERR.append(f'6 · claim tecnici non registrati: {mancanti}')
else:
    WARN.append(f'6 · {len(claims.CLAIMS)} claim censiti, nessuno fuori registro')

# ---- criteri di accettazione §13 ----
ACC_DECK = [
    ('CTA presente', 'id="v13_cta"' in DECK_C),
    ('contatto presente', gates.STATO['G1'] == 'APPROVED'),
    ('audit definito', gates.STATO['G1'] == 'APPROVED'),
    ('struttura economica coerente', 'Struttura economica' in DECK_C),
    ('prezzi o formula approvata', gates.STATO['G2'] == 'APPROVED'),
    ('servizi inclusi', gates.STATO['G2'] == 'APPROVED'),
    ('dataset validato o numeri rimossi', gates.STATO['G3'] == 'APPROVED' or not trovati),
    ('almeno un asset reale', len(assets91.REGISTRO) >= 1),
    ('nessun placeholder', '{{PH_' not in DECK_C),
    ('nessuna nota interna', 'INPUT APERTI' not in DECK_C),
]
ACC_DOS_PREL = [
    ('claim tecnici prudenti', claims.tutti_prudenti()),
    ('deployment dichiarato da chiudere', 'solution design' in DOS_C),
    ('annessi strutturati', DOS_C.count('ANNESSO') >= 4),
    ('proprietà dati prudente', 'Titolarit' in DOS_C),
    ('nessun placeholder', '{{PH_' not in DOS_C),
]
ACC_DOS_IT = [(c, gates.STATO['G4'] == 'APPROVED') for c in
              ('protocolli', 'porte', 'sizing', 'autenticazione', 'backup',
               'retention', 'logging', 'supporto remoto', 'licenza', 'dati a fine contratto')]


def stampa(titolo, righe):
    ok = sum(1 for _, v in righe if v)
    print(f'\n{titolo} — {ok}/{len(righe)}')
    for c, v in righe:
        print(f'  {"✓" if v else "✗"} {c}')
    return ok == len(righe)


if __name__ == '__main__':
    print('=== §14 · controlli di build ===')
    for w in WARN:
        print(f'  ok   {w}')
    for e in ERR:
        print(f'  FAIL {e}')

    d1 = stampa('§13 · Sales Deck', ACC_DECK)
    d2 = stampa('§13 · Dossier, come preliminare', ACC_DOS_PREL)
    d3 = stampa('§13 · Dossier, pronto per IT', ACC_DOS_IT)

    print('\n=== stato dei gate ===')
    for g, d in gates.GATES.items():
        print(f'  {g} {d["nome"]:28s} {d["scope"]:8s} {gates.STATO[g]}')
    print(f'  CASE {"caso cliente":28s} {"PAGE":8s} {gates.CASE_STUDY_READY}')

    print(f'\nSales Deck approvato: {"sì" if d1 else "NO"}')
    print(f'Dossier approvato come preliminare: {"sì" if d2 else "NO"}')
    print(f'Dossier pronto per IT: {"sì" if d3 else "NO"}')

    if ERR:
        sys.exit(1)
