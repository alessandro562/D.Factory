#!/usr/bin/env python3
"""§8.3 · nella working edition il token non è più il testo principale.

Prima:  <span data-ed="working">{{PH_CONTACT_NAME}}</span>
Dopo:   <span data-ed="working"><span class="ph"
              data-placeholder="PH_CONTACT_NAME">INPUT APERTO</span></span>

Le quattro etichette ammesse dal master sono INPUT APERTO, DECISIONE
COMMERCIALE, VALIDAZIONE TECNICA e ASSET RICHIESTO. Quale si applica non è una
scelta editoriale: deriva dal gate a cui il campo appartiene e, per i campi
fuori dai gate, dalla colonna «owner» del registro. Così registro e documenti
non possono divergere.

Un'eccezione dichiarata: la slide del caso cliente. Lì ogni cella è un campo
aperto, e ventotto «INPUT APERTO» identici cancellerebbero l'unica informazione
che quella slide porta oggi, cioè che cosa un caso deve contenere. Per quei
campi si mostra il nome del campo in chiaro. Il token resta comunque
nell'attributo, che è quello che il §8.3 chiede davvero.
"""
import re
import ph91

APERTO = 'INPUT APERTO'
COMMERCIALE = 'DECISIONE COMMERCIALE'
TECNICA = 'VALIDAZIONE TECNICA'
ASSET = 'ASSET RICHIESTO'

OWNER_LABEL = {
    'Commerciale': COMMERCIALE,
    'Tecnico': TECNICA,
    'Tecnico + IT': TECNICA,
    'Legale': APERTO,
    'Direzione': APERTO,
    'Marketing': APERTO,
}

# §19 · un file da procurare non è un'informazione da recuperare
ASSET_PREFIX = ('PH_REAL_',)


# Il gate ha la precedenza sull'owner: G1 raccoglie identità, referente e
# definizione dell'audit, che sono informazioni da recuperare anche quando la
# colonna owner dice «Commerciale». G2 è il modello economico, G3 e G4 sono
# validazioni.
GATE_LABEL = {'G1': APERTO, 'G2': COMMERCIALE, 'G3': TECNICA, 'G4': TECNICA,
              'G5': ASSET, 'CASE': APERTO}


def etichetta(token):
    if token.startswith(ASSET_PREFIX):
        return ASSET
    r = ph91.BY_ID.get(token)
    if not r:
        raise SystemExit(f'token fuori registro: {token}')
    g = r.get('gate')
    if g in GATE_LABEL:
        return GATE_LABEL[g]
    return OWNER_LABEL[r['owner']]


# eccezione dichiarata · slide 14, caso cliente
CAMPI_CASO = {
    'PH_CASE_INITIAL_PROBLEM': 'problema iniziale',
    'PH_CASE_RESULT_1_LABEL': 'risultato 1',
    'PH_CASE_CLIENT_DISPLAY_NAME': 'cliente o dicitura anonima',
    'PH_CASE_CLIENT_SECTOR': 'settore',
    'PH_CASE_LINE_TYPE': 'tipo di linea',
    'PH_CASE_CLIENT_SITE': 'stabilimento',
    'PH_CASE_BASELINE_PERIOD': 'periodo di baseline',
    'PH_CASE_BASELINE_DATA': 'dati di baseline',
    'PH_CASE_SCOPE': 'perimetro',
    'PH_CASE_SOLUTION_MODULE': 'livello attivato',
    'PH_CASE_INTERVENTION': 'intervento',
    'PH_CASE_PILOT_DURATION': 'durata del pilot',
    'PH_CASE_TIME_TO_USABLE_DATA': 'tempo al primo dato utile',
    'PH_CASE_RESULT_1_BASELINE': 'risultato 1 · baseline',
    'PH_CASE_RESULT_1_AFTER': 'risultato 1 · dopo',
    'PH_CASE_RESULT_1_UNIT': 'risultato 1 · unità',
    'PH_CASE_RESULT_2_LABEL': 'risultato 2',
    'PH_CASE_RESULT_2_AFTER': 'risultato 2 · dopo',
    'PH_CASE_RESULT_3_LABEL': 'risultato 3',
    'PH_CASE_RESULT_1_METHOD': 'metodo di misura',
    'PH_CASE_DATA_SOURCES': 'fonti del dato',
    'PH_CASE_ADDED_SENSORS': 'sensori aggiunti',
    'PH_CASE_QUOTE': 'citazione autorizzata',
    'PH_CASE_QUOTE_AUTHOR': 'autore',
    'PH_CASE_QUOTE_ROLE': 'ruolo',
    'PH_CASE_QUOTE_APPROVAL': 'stato dell’autorizzazione',
    'PH_CASE_CONFIDENCE_NOTE': 'limiti dichiarati della misura',
}

TOK = re.compile(r'\{\{(PH_[A-Z0-9_]+)\}\}')


def _intervalli(html, apri, chiudi):
    """Intervalli [start, end) dei blocchi apri…chiudi, per contesto."""
    out, i = [], 0
    while True:
        a = html.find(apri, i)
        if a < 0:
            return out
        b = html.find(chiudi, a)
        if b < 0:
            return out
        out.append((a, b + len(chiudi)))
        i = b + len(chiudi)


def applica(html):
    """Sostituisce i token con l'etichetta, fuori dai pannelli riassuntivi."""
    svg = _intervalli(html, '<svg', '</svg>')
    phb = _intervalli(html, '<div class="phb', '</div>')
    caso = _intervalli(html, 'id="v14_caso"', '\n</div>')

    def dentro(pos, ranges):
        return any(a <= pos < b for a, b in ranges)

    out, i, n = [], 0, 0
    for m in TOK.finditer(html):
        if dentro(m.start(), phb):          # il pannello parla al registro
            continue
        tok = m.group(1)
        if dentro(m.start(), caso) and tok in CAMPI_CASO:
            testo = CAMPI_CASO[tok]
        else:
            testo = etichetta(tok)
        if dentro(m.start(), svg):
            rep = f'<tspan data-placeholder="{tok}">{testo}</tspan>'
        else:
            rep = f'<span class="ph" data-placeholder="{tok}">{testo}</span>'
        out.append(html[i:m.start()])
        out.append(rep)
        i = m.end()
        n += 1
    out.append(html[i:])
    return ''.join(out), n


if __name__ == '__main__':
    import collections
    c = collections.Counter(etichetta(r['id']) for r in ph91.R)
    for k, v in c.most_common():
        print(f'{v:4d}  {k}')
    print(f'{len(CAMPI_CASO)} campi del caso cliente con nome esteso')
