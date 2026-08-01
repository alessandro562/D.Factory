# D.Factory · QA Report v5

`DFactory_SalesDeck_v5.html` · 11 slide + 4 appendici
`DFactory_DossierTecnico_v5.html` · 31 pagine, cinque sezioni

Strumenti: `work_v5/render.py` (Playwright/Chromium, 1280 × 720, `device_scale_factor=2`),
`work_v5/qa.py` (misure nel DOM, con scalatura del `viewBox` per il testo SVG).

---

## 1. QA tecnico

| Controllo | Sales deck | Dossier |
|---|---|---|
| Canvas renderizzati | 15 | 31 |
| Elementi fuori canvas | **0** | **0** |
| Collisioni non intenzionali | **0** | **0** |
| Errori console | **0** | **0** |
| Richieste di rete | **0** | **0** |
| Font incorporati | Geist, Geist Mono, Instrument Serif · base64 | idem |
| Link interni rotti | **0** | **0** · 5 àncore di sezione risolte |
| ID duplicati | **0** | **0** |
| CSS di stampa | `@media print` + `@page 1280×720` | idem |
| PDF generabile | sì | sì |

## 2. Densità

Conteggio di tutto il testo visibile, incluso quello dentro gli SVG con il corpo effettivo
dopo la scalatura del `viewBox`.

### Sales deck · corpo · target 40–60, limite 70

| # | Slide | Parole | Frammenti | Corpo min | Area visual |
|---|---|---|---|---|---|
| 01 | `s01_promessa` | 53 | 28 | 12,5 px | 79 % |
| 02 | `s02_punto_cieco` | 53 | 18 | 12,5 px | 54 % |
| 03 | `s03_come_funziona` | 68 | 21 | 12,5 px | 61 % |
| 04 | `s04_prodotto` | 56 | 22 | 12,0 px | 98 % |
| 05 | `s05_decisioni` | 64 | 18 | 12,5 px | 59 % |
| 06 | `s06_differenziatore` | 70 | 20 | 12,5 px | 53 % |
| 07 | `s07_ipotesi_misure` | 70 | 19 | 12,5 px | 55 % |
| 08 | `s08_architettura` | 57 | 20 | 12,5 px | 61 % |
| 09 | `s09_valore` | 65 | 23 | 12,5 px | 61 % |
| 10 | `s10_percorso` | 68 | 23 | 12,5 px | 55 % |
| 11 | `s11_cta` | 68 | 16 | 12,0 px | — |
| | **Corpo** | **media 63 · max 70** | max 28 | **12,0 px** | **10 su 11 oltre il 50 %** |
| A1 | `a01_offerta` | 139 | 33 | 12,0 px | 50 % |
| A2 | `a02_faq` | 165 | 31 | 12,5 px | 73 % |
| A3 | `a03_ipotesi` | 131 | 23 | 12,5 px | — |
| A4 | `a04_legacy` | 101 | 28 | 12,0 px | 50 % |

### Dossier · target 95–135, limite 165

Media **131**, massimo **165** (`d13`, `d25`), minimo 63. Nessuna pagina oltre il limite.
Corpo minimo effettivo **11,5 px**. Ventinove pagine su 31 sopra il 38 % di area visual; le
due eccezioni sono la copertina (23 %) e nessun'altra — `d19` sta al 41 %, `d30` al 40 %.

| Sezione | Pagine | Media parole |
|---|---|---|
| A · prodotto e maturità | 01–06 | 137 |
| B · funzioni proven e pilot | 07–14 | 115 |
| C · Refyn in sviluppo | 15–18 | 144 |
| D · integrazione e IT | 19–24 | 135 |
| E · servizi, delivery e migrazione | 25–31 | 131 |

### Confronto con il v4

| | v4 | v5 |
|---|---|---|
| Slide sales, corpo | 10 | **11** |
| Appendici sales | 3 | **4** |
| Parole/slide, corpo | 62 | **63** |
| Pagine dossier | 23 | **31** |
| Parole/pagina dossier | 125 | **131** |
| Corpo minimo | 11,5 px | **11,5 px** |
| Funzioni con stato dichiarato | 0 | **oltre 60** |

## 3. QA semantico

Controllo lessicale automatico su entrambi gli HTML, incluso il testo accessibile degli SVG
(`<title>` e `<desc>`).

### Termini vietati · attesi 0

| Termine | Deck | Dossier | Esito |
|---|---|---|---|
| `Insights` (plurale) | 0 | 0 | OK |
| `Refyn by`, `D.Factory Refyn` | 0 | 0 | OK |
| `un solo modello dati` | 0 | 0 | OK |
| `modello dati` in qualsiasi forma | 0 | 0 | OK |
| `Operator Performance Index` | 0 | 0 | OK |
| `consulenza inclusa` | 0 | 0 | OK |
| `tempo reale` non qualificato | 0 | 0 | OK |
| `Siemens` · `SAP` · `Patent Box` | 0 | 0 | OK |
| `70 casi` · `60 giorni` | 0 | 0 | OK |
| Numeri di trazione | 0 | 0 | OK |
| `digital twin` | 0 | 0 | OK |
| Token `[[PH_…]]` | 0 | 0 | OK |

**Due occorrenze intenzionali**, verificate a mano e conformi al backlog:

- `intelligenza artificiale` compare **una volta nel dossier**, a pagina 18, nella colonna
  delle funzioni `not offered`. È un'esclusione esplicita, non un claim.
- `benchmark cross-client` compare **una volta nel dossier**, sempre a pagina 18, con la
  condizione che ne bloccherebbe la valutazione (modello legale, privacy, anonimizzazione).

### Termini obbligatori nel dossier · attesi > 0

| Termine | Occorrenze |
|---|---|
| `proven legacy` | 7 |
| `pilot release` | 7 |
| `in development` | 15 |
| `project-dependent` | 8 |
| `roadmap` | 7 |
| `MAPST 4.0` | 8 |
| `MarEnergy` | 7 |
| `migrazione volontaria` | 2 |
| `servizi a valore aggiunto` | 1 |

### Presenza dell'architettura nel deck

`Connect` 7 · `Insight` 6 · `Refyn` 7 · `servizi a valore aggiunto` 3 · `pilot release` 4 ·
`in sviluppo` 4 · `MAPST 4.0` 4 · `MarEnergy` 3 · `migrazione volontaria` 2 · `D.Factory` 2.

**`MAPST 4.0` e `MarEnergy` compaiono solo nelle appendici A2 e A4**, mai nel corpo
principale e mai nel visual di slide 3, come richiesto.

**`D.Factory` compare due volte**: rail di copertina e rail di chiusura. Mai come prefisso
di modulo.

## 4. Criterio di accettazione finale del backlog

Il lavoro è accettabile quando un lettore capisce senza spiegazioni aggiuntive:

| # | Condizione | Dove si legge | Esito |
|---|---|---|---|
| 1 | D.Factory è il brand | Copertina deck, dossier 02 | ✓ |
| 2 | Connect, Insight, Refyn sono i nuovi livelli | Deck 08, dossier 02 e 06 | ✓ |
| 3 | Produzione ed energia sono in tutti i livelli | Deck 08 riga "in ogni livello", dossier 06 | ✓ |
| 4 | La profondità cresce da visibilità a diagnosi a miglioramento | Deck 08, scala a tre gradini | ✓ |
| 5 | Refyn è in sviluppo | Deck 06 e 08, dossier 02 e sezione C | ✓ |
| 6 | I servizi sono attivabili su tutti i moduli | Deck 08 e A1, dossier 25 | ✓ |
| 7 | MAPST 4.0 e MarEnergy restano legacy per l'installato | Deck A4, dossier 03 e 30 | ✓ |
| 8 | Nessuna capability futura è presentata come disponibile | Dossier 18, stati su ogni riga | ✓ |
| 9 | Il pilot è il prossimo passo | Deck 10 e 11 | ✓ |
| 10 | Il dossier distingue capability, packaging e roadmap | Dossier 03 e 06, doppio stato | ✓ |

## 5. Cosa questo QA non può dichiarare

**Nessun asset reale è entrato nei documenti.** Tutte le viste di prodotto restano
ricostruzioni etichettate: `s04` porta "vista illustrativa del nuovo packaging", le pagine
funzionali del dossier portano "dati illustrativi". Il backlog chiede otto asset reali in
priorità alta — screenshot MAPST 4.0 e MarEnergy, foto di linea, report esportato,
dashboard anonimizzata. Nessuno era disponibile. Finché mancano, i due documenti mostrano
*che cosa il sistema calcola*, non *com'è fatto il sistema*.

**Il dossier non è "pronto per IT".** Pagina 22 elenca le voci decisive con stato, owner e
momento di chiusura, ma il backlog §9.9 chiede diciotto voci compilate con dati reali:
protocolli, porte, direzione dei flussi, sizing, autenticazione, backup, retention,
patching, logging, remote support, API, licenza, disaster recovery, SLA. Oggi la maggior
parte è "da concordare". La formulazione corretta resta: **pronto per la riunione tecnica in
cui quelle voci si compilano, non per l'approvazione che viene dopo.**

**Il perimetro dei moduli non è deciso.** Le righe della capability matrix riflettono la
proposta del backlog §3, non una decisione di prodotto. Finché Connect e Insight non hanno
un perimetro approvato, l'appendice A1 del deck descrive un'ipotesi ragionata, non un
listino. È il primo dei quattordici bloccanti P0.
