#!/usr/bin/env python3
"""Genera DFactory_PlaceholderRegister_v9.md dal registro in ph.py."""
import collections
import ph

R = ph.R
out = []
w = out.append

w('# D.Factory · Registro placeholder V9\n')
w(f'{len(R)} placeholder dichiarati · '
  f'**P0 {len(ph.P0)}** · P1 {len(ph.P1)} · P2 {len(ph.P2)} · '
  f'tutti in stato `OPEN` al {ph.VERIFICA}.\n')
w('''Questo file è la fonte unica. Il build lo legge per verificare che ogni
`{{PH_...}}` presente negli HTML sia dichiarato qui, e la client edition lo legge
per sapere che cosa nascondere. Se un placeholder non è in questa tabella, il
build fallisce.\n''')

w('''---

## Come si legge

| campo | che cosa dice |
|---|---|
| **ID** | il token da usare negli HTML, sintassi `{{PH_NOME}}` |
| **Owner** | chi può chiudere l\'input, non chi lo trascrive |
| **Fonte richiesta** | il documento da cui il valore deve arrivare, non l\'opinione |
| **Priorità** | P0 blocca la pubblicazione · P1 riduce credibilità · P2 miglioramento |
| **Working** | che cosa si vede nella working edition |
| **Client** | che cosa succede nella client edition finché lo stato è `OPEN` |

Stati ammessi: `OPEN` · `IN REVIEW` · `APPROVED` · `REJECTED` · `NOT NEEDED`.

**Regola di chiusura.** Uno stato passa ad `APPROVED` solo con la fonte
richiesta allegata. Un valore comunicato a voce resta `IN REVIEW`.

---
''')

# ---- riepilogo per priorita' e owner ----
w('## Dove si concentra il lavoro\n')
w('| owner | P0 | P1 | P2 | totale |')
w('|---|---:|---:|---:|---:|')
byo = collections.defaultdict(lambda: collections.Counter())
for r in R:
    byo[r['owner']][r['prio']] += 1
for o in sorted(byo, key=lambda k: -sum(byo[k].values())):
    c = byo[o]
    w(f'| {o} | {c["P0"]} | {c["P1"]} | {c["P2"]} | {sum(c.values())} |')
w('')

w('| documento | P0 | P1 | P2 | totale |')
w('|---|---:|---:|---:|---:|')
byd = collections.defaultdict(lambda: collections.Counter())
for r in R:
    byd[r['doc']][r['prio']] += 1
for d in ('deck', 'dossier', 'entrambi'):
    c = byd[d]
    w(f'| {d} | {c["P0"]} | {c["P1"]} | {c["P2"]} | {sum(c.values())} |')
w('')

_case = [r for r in R if r['gruppo'].startswith('5.3')]
_c0 = sum(1 for r in _case if r['prio'] == 'P0')
w(f'''**Il caso cliente da solo vale {len(_case)} placeholder, di cui {_c0} P0.** È il blocco più
grande del registro e il più semplice da valutare: o esiste un caso autorizzato per
iscritto, o la slide 14 non esiste. Non c'è una via di mezzo che non sia inventare.

---
''')

# ---- tabelle per gruppo ----
cur = None
for r in R:
    if r['gruppo'] != cur:
        cur = r['gruppo']
        w(f'\n## {cur}\n')
        w('| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |')
        w('|---|---|---|---|:--:|---|---|---|---|:--:|')
    w(f'| `{{{{{r["id"]}}}}}` | {r["desc"]} | {r["owner"]} | {r["fonte"]} | '
      f'**{r["prio"]}** | {r["doc"]} | {r["canvas"]} | {r["working"]} | {r["client"]} | `{r["stato"]}` |')

w('''

---

## Effetto complessivo sulla client edition di oggi

Con tutti i placeholder `OPEN`, la client edition esclude:

| canvas | perché |
|---|---|
| deck 13 · CTA | `PH_CONTACT_NAME`, `PH_CONTACT_ROLE`, `PH_CONTACT_EMAIL` sono P0 e la §5.1 vieta di pubblicare la CTA senza contatto |
| deck 14 · caso cliente | `PH_CASE_APPROVAL_STATUS` non è `APPROVED` |
| deck A3 · pricing | nessun importo approvato: la §5.5 impone di rimuovere la pagina di pricing dettagliato |
| dossier 06 · riquadro Refyn | `PH_REFYN_RELEASE_TARGET` non approvata: nessuna data di rilascio |

Tutto il resto passa nella client edition con i blocchi di placeholder rimossi e,
dove previsto, con la formulazione prudente già in uso nella V8 — che era stata
scritta proprio per reggere senza quei valori.

**Il deck client-facing di oggi ha quindi 12 slide e 4 appendici.** Non è una
riduzione di qualità: è la conseguenza aritmetica di quattro input mancanti.
''')

open('../DFactory_PlaceholderRegister_v9.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'DFactory_PlaceholderRegister_v9.md · {len(R)} righe')
