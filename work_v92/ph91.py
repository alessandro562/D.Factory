#!/usr/bin/env python3
"""Registro placeholder V9.1 · aggiunge BLOCKING_SCOPE e riduce i P0.

Il registro V9 aveva 104 P0 indistinti: ogni cosa mancante bloccava tutto.
Il §3 del piano chiede di separare che cosa blocca davvero. Qui la priorità
non è più un giudizio: è una conseguenza del gate a cui il campo appartiene.

  P0  il campo è dentro uno dei cinque gate, oppure è il gate del caso cliente
  P1  utile, non blocca: si pubblica con formulazione prudente
  P2  miglioramento successivo
"""
import ph as v9
import gates

CASE_DETAIL_SCOPE = 'NONE'   # il dettaglio del caso non blocca: blocca il gate

R = []
for r in v9.R:
    e = dict(r)
    gid = gates.CAMPI_GATE.get(e['id'])
    if gid:
        e['prio'] = 'P0'
        e['scope'] = gates.GATES[gid]['scope']
        e['gate'] = gid
    else:
        e['gate'] = '—'
        if e['gruppo'].startswith('5.3'):
            # §3.2 · il dettaglio del caso cliente non genera P0 globali
            e['prio'] = 'P1' if e['prio'] == 'P0' else e['prio']
            e['scope'] = CASE_DETAIL_SCOPE
        elif e['prio'] == 'P0':
            # ex P0 fuori dai gate: resta importante, non blocca la pubblicazione
            e['prio'] = 'P1'
            e['scope'] = 'PAGE' if e['client'] in ('canvas escluso', 'blocco nascosto') else 'NONE'
        else:
            e['scope'] = 'NONE'
    R.append(e)

# §3.2 · il gate unico del caso cliente
R.append({
    'gruppo': '5.3 Caso cliente · gate', 'id': gates.CASE_GATE,
    'desc': 'Caso cliente pronto: servono tutti e otto gli elementi del §3.2',
    'owner': 'Legale', 'fonte': 'autorizzazione scritta + dati di progetto',
    'prio': 'P0', 'doc': 'deck', 'canvas': 'deck 14',
    'working': 'visibile', 'client': 'slide 14 esclusa finché non è APPROVED',
    'stato': gates.CASE_STUDY_READY, 'verifica': v9.VERIFICA,
    'gate': 'CASE', 'scope': 'PAGE'})

BY_ID = {r['id']: r for r in R}
P0 = [r['id'] for r in R if r['prio'] == 'P0']
P1 = [r['id'] for r in R if r['prio'] == 'P1']
P2 = [r['id'] for r in R if r['prio'] == 'P2']
GLOBAL = [r['id'] for r in R if r['scope'] == 'GLOBAL']

if __name__ == '__main__':
    import collections
    print(f'{len(R)} placeholder · P0 {len(P0)} (erano {len(v9.P0)}) · '
          f'P1 {len(P1)} · P2 {len(P2)}')
    c = collections.Counter(r['scope'] for r in R)
    print('scope:', dict(c))
    print('GLOBAL:', len(GLOBAL), 'campi — tutti di G1')
