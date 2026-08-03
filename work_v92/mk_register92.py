#!/usr/bin/env python3
"""Genera DFactory_PlaceholderRegister_v9_2.md e DFactory_ClaimRegister_v9_2.md.

Il registro placeholder è lo stesso della V9.1 — il §8.1 vieta di rinominare i
token — con due colonne in più che la V9.2 introduce: l'etichetta mostrata nella
working edition e il canvas in cui quell'etichetta compare davvero.
"""
import collections
import re

import assets92
import claims
import gates
import labels92
import ph91

ROOT = '..'
FILES = {
    'deck working': f'{ROOT}/DFactory_SalesDeck_v9_2_working.html',
    'dossier working': f'{ROOT}/DFactory_DossierTecnico_v9_2_working.html',
}

# dove ogni token compare davvero, letto dagli HTML consegnati
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


P = ph91.R
c_prio = collections.Counter(r['prio'] for r in P)
c_scope = collections.Counter(r['scope'] for r in P)
c_lab = collections.Counter(labels92.etichetta(r['id']) for r in P)

out = []
w = out.append

w('# D.Factory · Registro placeholder V9.2\n')
w(f"{len(P)} placeholder · **P0 {c_prio['P0']}** · P1 {c_prio['P1']} · P2 {c_prio['P2']}\n")
w("""Stessi token della V9.1: il §8.1 vieta di rinominarli, e non sono stati
rinominati. La V9.2 aggiunge una cosa sola, ma cambia come si legge la working
edition — **l'etichetta**. Prima il token era il testo principale, adesso è un
attributo:

```html
<span data-ed="working" class="ph" data-placeholder="PH_CONTACT_NAME">INPUT APERTO</span>
```

Quale delle quattro etichette del §8.3 tocchi a un campo non è una scelta
editoriale: **decide il gate**, e per i campi fuori dai gate decide la colonna
*owner*. La regola vive in `labels92.py`, così registro e documenti non possono
divergere.

| gate | etichetta | perché |
|---|---|---|
| G1 | `INPUT APERTO` | identità, referente e definizione dell'audit sono informazioni da recuperare, non decisioni da prendere |
| G2 | `DECISIONE COMMERCIALE` | prezzi, inclusioni, durata: qualcuno deve decidere |
| G3 · G4 | `VALIDAZIONE TECNICA` | dataset e requisiti si verificano, non si scelgono |
| G5 e `PH_REAL_*` | `ASSET RICHIESTO` | serve un file, con autorizzazione |
| fuori dai gate | dall'owner | Commerciale → decisione · Tecnico → validazione · resto → input aperto |
""")
w('\n| etichetta | campi |\n|---|--:|')
for k, v in c_lab.most_common():
    w(f'| `{k}` | {v} |')

w('\n---\n\n## 1. I cinque gate\n')
w('| Gate | Che cosa blocca | Scope | Campi | Stato | Effetto sulla V9.2 |')
w('|---|---|:--:|--:|:--:|---|')
for g, d in gates.GATES.items():
    w(f'| **{g}** {d["nome"]} | {d["blocca"]} | `{d["scope"]}` | {len(d["campi"])} | '
      f'`{gates.STATO[g]}` | {d["effetto"]} |')
w(f'| **CASE** caso cliente | la slide 14 del deck | `PAGE` | 1 | '
  f'`{gates.CASE_STUDY_READY}` | La slide 14 non entra nella client edition. |')

w('\n### Che cosa cambia in ciascun canvas quando il gate si chiude\n')
w('| gate | canvas che cambiano | oggi il cliente vede |')
w('|---|---|---|')
w('| G1 | `v13_cta` · `p01_cover` | CTA senza referente · warning globale: il deck si presenta, non si invia |')
w('| G2 | `v09_scelta` · `v12_pilot` · `a1_matrice` · `a2_servizi` · **`a3_pricing` esclusa** | struttura economica senza importi |')
w('| G3 | `v11_valore` · `v13_cta` · **`a5_assunzioni` esclusa** | formula e settimana osservata, nessun annualizzato |')
w('| G4 | `p01_cover` · `p08_architettura` · `pa1` · `pa2` · `pa3` · `pa4` | titolo preliminare · metodo invece dei valori |')
w('| G5 | `v03` `v04` `v05` `v10` · `p04` `p05` `p12` | ricostruzioni dichiarate, nessun asset reale |')
w('| CASE | **`v14_caso` esclusa** | nessuna slide di caso cliente |')

w('\n---\n\n## 2. Il registro\n')
w('Colonne: `id` · descrizione · owner · fonte · priorità · scope · gate · '
  'etichetta nella working edition · canvas in cui compare.\n')
w("L'asterisco su un canvas significa che lì il token compare nel pannello "
  "«INPUT APERTI» in coda alla pagina, che parla al registro e non al lettore.\n")

gruppi = collections.OrderedDict()
for r in P:
    gruppi.setdefault(r['gruppo'], []).append(r)

for gr, righe in gruppi.items():
    w(f'\n### {gr}\n')
    w('| id | descrizione | owner | prio | scope | gate | etichetta | canvas |')
    w('|---|---|---|:--:|:--:|:--:|---|---|')
    for r in righe:
        lab = labels92.CAMPI_CASO.get(r['id']) or labels92.etichetta(r['id'])
        w(f'| `{r["id"]}` | {r["desc"]} | {r["owner"]} | {r["prio"]} | '
          f'`{r["scope"]}` | {r["gate"]} | {lab} | {canvas(r["id"])} |')

w('\n---\n\n## 3. Distribuzione\n')
w('| scope | campi | che cosa significa |')
w('|---|--:|---|')
SIG = {'GLOBAL': 'impedisce la client edition del documento',
       'SECTION': 'esclude una sezione o disattiva un contenuto',
       'PAGE': 'esclude un singolo canvas',
       'NONE': 'non blocca: si pubblica con formulazione prudente'}
for k in ('GLOBAL', 'SECTION', 'PAGE', 'NONE'):
    w(f'| `{k}` | {c_scope[k]} | {SIG[k]} |')

w('\n---\n\n## 4. I campi che bloccano davvero\n')
w('I 58 P0, per gate. Sono gli unici che tengono ferma una consegna.\n')
for g in ('G1', 'G2', 'G3', 'G4', 'G5'):
    campi = [r for r in P if r.get('gate') == g]
    w(f'\n**{g} · {gates.GATES[g]["nome"]}** — {len(campi)} campi\n')
    for r in campi:
        w(f'- `{r["id"]}` — {r["desc"]} · owner {r["owner"]}')
w(f'\n**CASE · caso cliente** — 1 campo\n')
w(f'- `{gates.CASE_GATE}` — servono tutti e otto gli elementi del §20.3')

open(f'{ROOT}/DFactory_PlaceholderRegister_v9_2.md', 'w', encoding='utf-8').write('\n'.join(out))
print(f'DFactory_PlaceholderRegister_v9_2.md · {len(P)} voci · '
      f'{len(DOVE)} token localizzati nei canvas')

# =====================================================================
# Claim Register
# =====================================================================
VIS = {}
for nome, path in (('deck', f'{ROOT}/DFactory_SalesDeck_v9_2_client.html'),
                   ('dossier', f'{ROOT}/DFactory_DossierTecnico_v9_2_client.html')):
    h = open(path, encoding='utf-8').read()
    h = h[h.index('<body'):]
    h = re.sub(r'<!--.*?-->', ' ', h, flags=re.S)
    h = re.sub(r'<[^>]+>', ' ', h)
    VIS[nome] = re.sub(r'\s+', ' ', h)

out = []
w = out.append
w('# D.Factory · Claim Register V9.2\n')
w("""Dieci claim tecnici. La regola è quella del §25: **se una frase tecnica
compare nei documenti e non è qui, il build fallisce.** Il controllo è in
`accept92.py`, condizione 6, e passa.

Gli stati:

- **DIMOSTRATO** — la frase è verificabile dal documento stesso, perché la
  formula o la catena aritmetica sono scritte per esteso.
- **DIMOSTRATO CON RISERVA** — il metodo è scritto, un parametro è dichiarato
  illustrativo.
- **PRUDENTE** — la formulazione è stata approvata come prudente, la verifica
  tecnica è aperta.
- **AFFERMATO** — è un'affermazione sul prodotto o sul metodo, non una misura.
- **AFFERMATO CON RISERVA** — affermazione condizionale, con la condizione scritta.
""")
w('\n| # | claim | stato | marcatore | deck | dossier | fonte |')
w('|--:|---|---|---|:--:|:--:|---|')
for i, (k, frase, marc, stato, fonte) in enumerate(claims.CLAIMS, 1):
    nd = VIS['deck'].count(marc)
    nq = VIS['dossier'].count(marc)
    w(f'| {i} | {frase} | **{stato}** | `{marc}` | {nd or "—"} | {nq or "—"} | {fonte} |')

w('\n---\n\n## Le formulazioni approvate\n')
for k, d in gates.CLAIM_APPROVATI.items():
    w(f'\n### `{k}`\n')
    w(f'> {d["testo"]}\n')
    w(f'*Fonte:* {d["fonte"]} · *in breve:* {d["breve"]}\n')

w("""
---

## Il claim che non viene pubblicato

`proprieta` — proprietà dei dati e diritti di licenza. Il §25 è esplicito:
«proprietà dati: non pubblicare senza approvazione legale». La formulazione
esiste, è scritta qui sopra, e **non compare in nessuno dei quattro HTML**.
L'annesso A3 del dossier continua a dichiarare che cosa si decide e chi decide,
che è vero oggi e non richiede il legale.

`accept92.py` verifica che la frase non sia finita nel dossier: criterio
«proprietà dei dati non pubblicata», §26.

---

## Espressioni sorvegliate

Ogni marcatore di questa lista, se compare nei documenti, deve avere un claim.

""")
for m in claims.SORVEGLIATI:
    w(f'- `{m}` — deck {VIS["deck"].count(m)} · dossier {VIS["dossier"].count(m)}')

w("""
---

## Formulazioni vietate, e che cosa si usa al loro posto · §7

| non si usa | si usa | dove vale |
|---|---|---|
| causa rilevata automaticamente | **causa associata** | deck 03, 04, 06 · dossier 04, 05, 09 |
| costo reale del pezzo | **margine perso stimato**, **costo della perdita** | deck 04, 06 |
| risparmio garantito · valore certo | **capacità potenzialmente recuperabile**, **energia potenzialmente evitabile** | deck 11 |
| costo del pezzo (per il solo perimetro energia) | **costo energetico del pezzo** | deck 07 · dossier 11 |
| la differenza fra OEE macchina e linea è il polmone | **il calcolo di linea considera confini, blocking, starvation, buffer e regole di aggregazione** | dossier 10 |
| software certificato ISO 50001 | **supporta dati e processi coerenti con ISO 50001** | non pubblicato in V9.2 |
| qualsiasi marca e protocollo | **multi-vendor, con compatibilità verificata in audit** | dossier annesso A1 |
| integrazione con ERP | **integrazione con ERP o gestionale, previa verifica tecnica** | dossier 12 · deck A4 |
""")

open(f'{ROOT}/DFactory_ClaimRegister_v9_2.md', 'w', encoding='utf-8').write('\n'.join(out))
print(f'DFactory_ClaimRegister_v9_2.md · {len(claims.CLAIMS)} claim')
