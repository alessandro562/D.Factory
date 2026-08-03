#!/usr/bin/env python3
"""Genera i registri della Fase E: placeholder, claim, asset, open inputs.

Gli altri deliverable del §15 — Content Map, Change Log, QA Report, Final
Review Checklist, Rhythm Map e Duplicate Layout Map — sono scritti a mano o
da audit93.py, perche' contengono giudizio e non solo dati.
"""
import collections
import re

import assets92
import claims93
import gates
import labels92
import ph91

ROOT = '..'
FILES = {
    'deck working': f'{ROOT}/DFactory_SalesDeck_v9_3_working.html',
    'dossier working': f'{ROOT}/DFactory_DossierTecnico_v9_3_working.html',
}
CLIENT = {
    'deck client': f'{ROOT}/DFactory_SalesDeck_v9_3_client.html',
    'dossier client': f'{ROOT}/DFactory_DossierTecnico_v9_3_client.html',
}

DOVE = collections.defaultdict(set)
for nome, path in FILES.items():
    html = open(path, encoding='utf-8').read()
    for m in re.finditer(r'<div[^>]*class="slide[^"]*"[^>]*id="([^"]+)"|'
                         r'<div[^>]*id="([^"]+)"[^>]*class="slide[^"]*"', html):
        cid = m.group(1) or m.group(2)
        end = html.find('\n</div>', m.start())
        seg = html[m.start():end]
        for t in set(re.findall(r'data-placeholder="(PH_[A-Z0-9_]+)"', seg)):
            DOVE[t].add(cid)
        for t in set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', seg)):
            DOVE[t].add(cid + '*')


def canvas(tok):
    v = sorted(DOVE.get(tok, []))
    return ' · '.join(v) if v else '—'


# ======================================================= placeholder register
P = ph91.R
c_prio = collections.Counter(r['prio'] for r in P)
c_scope = collections.Counter(r['scope'] for r in P)
usati = {t for t in DOVE}

out = []
w = out.append
w('# D.Factory · Registro placeholder V9.3\n')
w(f"{len(P)} placeholder censiti · **P0 {c_prio['P0']}** · P1 {c_prio['P1']} · "
  f"P2 {c_prio['P2']} · {len(usati)} presenti nei documenti consegnati\n")
w("""Gli stessi token della V9.1 e della V9.2: il §8.1 vieta di rinominarli, e la
riscrittura narrativa della V9.3 non ne ha rinominato nessuno. Quello che cambia
è **dove** compaiono, perché il corpo dei due documenti è stato riscritto: la
colonna «canvas» è ricalcolata sugli HTML consegnati, non ereditata.

Nella working edition il token è un attributo e il lettore vede un'etichetta:

```html
<span data-ed="working" class="ph" data-placeholder="PH_CONTACT_NAME">INPUT APERTO</span>
```

L'asterisco accanto a un canvas segnala che lì il token è ancora scritto per
esteso — succede nei pannelli «INPUT APERTI» a piè di canvas, che sono
impalcatura e non testo del documento.
""")
w('| token | prio | gate | scope | etichetta | canvas |')
w('|---|:--:|:--:|:--:|---|---|')
for r in sorted(P, key=lambda x: (x['prio'], x['id'])):
    w(f"| `{r['id']}` | {r['prio']} | {r.get('gate') or '—'} | {r['scope']} | "
      f"{labels92.etichetta(r['id'])} | {canvas(r['id'])} |")
w('\n## Come si chiudono\n')
w('| gate | placeholder | che cosa serve |')
w('|---|--:|---|')
for g, d in gates.GATES.items():
    n = sum(1 for r in P if r.get('gate') == g)
    w(f"| **{g}** {d['nome']} | {n} | {d['blocca']} |")
open(f'{ROOT}/DFactory_PlaceholderRegister_v9_3.md', 'w', encoding='utf-8').write(
    '\n'.join(out) + '\n')

# ============================================================ claim register
def visibile(path):
    h = open(path, encoding='utf-8').read()
    s = h[h.index('<body'):]
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'<(script|style)[\s\S]*?</\1>', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s)


VIS = {n: visibile(p) for n, p in list(FILES.items()) + list(CLIENT.items())}

out = []
w = out.append
w('# D.Factory · Claim Register V9.3\n')
w(f'{len(claims93.CLAIMS)} claim tecnici. Nessuno nuovo rispetto alla V9.2: la '
  'revisione narrativa non ha aggiunto affermazioni tecniche, le ha tolte.\n')
w("""Due claim cambiano **formulazione**, e il cambio è di sostanza:

| claim | prima | dopo | perché |
|---|---|---|---|
| — | «Motore KPI» come componente dell'architettura | «Elaborazione KPI» come funzione | il §2.3 della review D2: non si dichiara un componente architetturale che non è confermato |
| `erp` | «API · dati selezionati · da definire» | «Interfacce applicative · da verificare sul perimetro» | il §2.4: la presenza di un'interfaccia applicativa è un claim di prodotto, e non è confermata |

Il build fallisce se un marcatore tecnico compare nei documenti senza un claim
che lo copra: `accept93.py` condizione 6.
""")
w('| claim | stato | frase | marcatore | fonte |')
w('|---|:--:|---|---|---|')
for k, frase, marc, stato, fonte in claims93.CLAIMS:
    w(f"| `{k}` | {stato} | {frase} | `{marc}` | {fonte} |")
w('\n## Dove compaiono\n')
w('| marcatore | deck client | dossier client |')
w('|---|--:|--:|')
for k, frase, marc, stato, fonte in claims93.CLAIMS:
    for m in marc.split('|'):
        w(f"| `{m}` | {VIS['deck client'].count(m)} | {VIS['dossier client'].count(m)} |")
w(f'\n## Formulazioni vietate dal §12\n')
w(f'{len(claims93.VIETATE)} espressioni. Nessuna compare nei quattro documenti; '
  'il controllo è una condizione di build, non una raccomandazione.\n')
for v in claims93.VIETATE:
    w(f'- ~~{v}~~')
open(f'{ROOT}/DFactory_ClaimRegister_v9_3.md', 'w', encoding='utf-8').write(
    '\n'.join(out) + '\n')

# ============================================================ asset register
out = []
w = out.append
w('# D.Factory · Asset Register V9.3\n')
w(f'**{len(assets92.REGISTRO)} asset registrati.** Il registro è vuoto perché '
  'nessun asset reale è stato consegnato.\n')
w("""Non è una dimenticanza ed è la ragione per cui ogni vista di prodotto dei due
documenti porta la dicitura «vista ricostruita · dati illustrativi». Il build
fallisce se un file compare in un canvas senza essere in questa tabella
(`accept93.py`, condizione 5): oggi la condizione passa perché di file non ce
n'è nessuno.

Colonne richieste per ogni asset, quando arriverà:
""")
w('| ' + ' | '.join(assets92.COLONNE) + ' |')
w('|' + '---|' * len(assets92.COLONNE))
w('| ' + ' | '.join('—' for _ in assets92.COLONNE) + ' |')
w('\n## Che cosa serve, in ordine di priorità\n')
w('| # | asset | token | dove andrebbe | stato |')
w('|--:|---|---|---|:--:|')
for o in assets92.OBIETTIVO:
    w(f"| {o['n']} | {o['asset']} | `{o['token']}` | {o['dove']} | {o['stato']} |")
w(f"\n**Soglia dichiarata:** deck {assets92.SOGLIA['deck']} asset reale, "
  f"dossier {assets92.SOGLIA['dossier']}. Raggiunti: 0 e 0.\n")
open(f'{ROOT}/assets_v9_3_AssetRegister.md', 'w', encoding='utf-8').write(
    '\n'.join(out) + '\n')

print('registri scritti: placeholder, claim, asset')
