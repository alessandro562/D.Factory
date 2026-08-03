# D.Factory · Content Map v9

Ogni canvas delle quattro edizioni con la domanda a cui risponde, il dato che
porta, i placeholder che aspetta e che cosa succede nella client edition.

---

## 1. Sales Deck · 13 slide + 5 appendici + caso cliente

Sequenza: `tensione → categoria → prodotto → prova → ampiezza → offerta → valore → acquisto`

| # | id | domanda del lettore | dato | placeholder | client edition |
|---|---|---|---|--:|---|
| 01 | `v01_cover` | di che cosa mi parli? | 1.820 € · 162 € · 735 kWh | 3 | presente, banda rimossa |
| 02 | `v02_tensione` | perché adesso? | — | 0 | presente |
| 03 | `v03_categoria` | che categoria di prodotto è? | OEE 71,4% · 26 min · 6.720 € | 1 | presente |
| 04 | `v04_evento_prodotto` | mi fai vedere? | 11:24–11:42 · 18 min · 1.260 € | 1 | presente |
| 05 | `v05_energia` | e l’energia? | 0 pz/min · 38 kW a linea ferma | 2 | presente |
| 06 | `v06_priorita` | e poi? | 14 eventi · 96 min · 6.720 € · 43% | 0 | presente |
| 07 | `v07_ampiezza` | copre solo i fermi? | 71,4% · 735 kWh · 3,2 kWh/1.000 pz | 0 | presente |
| 08 | `v08_offerta` | com’è organizzata l’offerta? | 6.720 € · 4.340 € · 162 € | 2 | presente |
| 09 | `v09_scelta` | quale livello è per me? | — | 3 | presente, riga finale riformulata |
| 10 | `v10_perche` | perché fidarmi? | 500→0 pz/min · 95→38 kW | 3 | presente |
| 11 | `v11_valore` | quanto vale? | 309.120 € · 154.560 € · 810 € | 4 | presente |
| 12 | `v12_pilot` | come si comincia e quanto costa? | — | 5 | presente |
| 13 | `v13_cta` | qual è il prossimo passo? | 15.680 € · 309.120 € | 9 | **esclusa** · manca il contatto |
| 14 | `v14_caso` | avete un caso reale? | — | **33** | **esclusa** · caso non autorizzato |
| A1 | `a1_matrice` | che cosa comprende ogni livello? | 7 capacità + cliente ideale | 2 | presente |
| A2 | `a2_servizi` | quali servizi e che cosa producono? | 9 servizi | 3 | presente |
| A3 | `a3_pricing` | quanto costa, voce per voce? | — | **13** | **esclusa** · nessun importo approvato |
| A4 | `a4_faq` | le domande che arrivano sempre | — | 0 | presente |
| A5 | `a5_assunzioni` | da dove vengono i numeri? | 9 parametri + 3 formule | 3 | presente |

### Le tre fusioni

- **04** era due slide: la V8·04 anticipava il fermo, la V8·05 lo mostrava con
  causa, OEE e costo. Dicevano la stessa cosa a due livelli di dettaglio.
- **12** riprende dalla V8·14 le tre voci del modello economico e le mette sotto
  i tre momenti del pilot: chi legge «come si comincia» vuole sapere subito anche
  «con che struttura di costo».
- **A2** assorbe la V8·11 «servizi a valore aggiunto» e guadagna la colonna
  **obiettivo**: il nome di un servizio non dice niente, il suo obiettivo e il suo
  deliverable sì.

### La catena dei numeri

Tutto il deck si ricostruisce da nove parametri, tutti in A5 con origine e stato:

```
scenario: un turno al giorno, 5 giorni, 46 settimane = 230 turni

500 pz/min · 0,14 €/pz            → 70 €/min
fermo 18 min                      → 1.260 €
turno 26 min                      → 1.820 €
7 giorni · 58 eventi · 224 min    → 15.680 €  ·  prima causa 43%
96 × 70 × 46                      → 309.120 €  ·  metà 154.560 €
95 kW marcia · 38 kW fermo        → 719 + 16 = 735 kWh
735 kWh × 0,22 €/kWh              → 162 €
454 min × 500 pz/min              → 227.000 pezzi
735 ÷ 227.000 × 1.000             → 3,2 kWh · 0,71 € · 1,13 kgCO₂e / 1.000 pz
94,6% × 79% × 95,6%               → OEE 71,4%
16 kWh × 230 turni × 0,22         → 810 €
```

---

## 2. Dossier tecnico preliminare · 14 pagine + 4 annessi

Quattro sezioni: `1 Prodotto` · `2 Dati e architettura` · `3 Misure e analisi` ·
`4 Delivery e supporto`. Le aperture di sezione sono fasce scure in testa alle
pagine 07, 10 e 13.

| # | id | sez. | template | domanda del lettore | placeholder | client edition |
|---|---|:--:|:--:|---|--:|---|
| 01 | `p01_cover` | — | A | che documento ho in mano? | 8 | blocco «emesso da» riformulato |
| 02 | `p02_overview` | 1 | B | che cosa fa, richiede, restituisce? | 2 | presente |
| 03 | `p03_livelli` | 1 | C | com’è fatto il prodotto? | 2 | presente |
| 04 | `p04_connect` | 1 | B | che cosa vedo? | 3 | presente |
| 05 | `p05_insight` | 1 | B | che cosa capisco? | 3 | presente |
| 06 | `p06_refyn` | 1 | C | che cosa governo? | 6 | **riquadro rilascio rimosso** |
| 07 | `p07_sorgenti` | 2 | D | da dove leggete? | 4 | presente |
| 08 | `p08_architettura` | 2 | C | dove gira, come parla con la mia rete? | 6 | riga sola lettura riformulata |
| 09 | `p09_contesto` | 2 | B | perché il dato grezzo non basta? | 3 | presente |
| 10 | `p10_oee` | 3 | C | come calcolate l’OEE? | 4 | presente |
| 11 | `p11_energia` | 3 | C | come arrivate al costo energetico del pezzo? | 4 | presente |
| 12 | `p12_output` | 3 | D | come esce il dato? | 4 | presente |
| 13 | `p13_pilot` | 4 | C | come si svolge il pilot? | 4 | presente |
| 14 | `p14_servizi` | 4 | D | e dopo il go-live? | 10 | riga SLA riformulata · citazione legacy |
| A1 | `pa1_compatibilita` | 2 | D | funziona sui miei PLC? | 9 | 2 celle riformulate |
| A2 | `pa2_sizing` | 2 | C | che ambiente devo prevedere? | 9 | valori sostituiti dal metodo |
| A3 | `pa3_governo` | 2 | D | come governate sicurezza e dati? | **13** | colonna valore → «solution design» |
| A4 | `pa4_kpi` | 3 | D | come sono definiti gli indicatori? | 10 | colonna owner → «da nominare» |

**Nessuna pagina del dossier viene esclusa dalla client edition.** Ogni blocco con
placeholder ha una formulazione prudente che lo sostituisce: sono le frasi che la
V8 aveva già scritto proprio per reggere senza quei valori.

---

## 3. Dove i due documenti si toccano

Otto punti in cui dicono la stessa cosa e devono restare allineati.

| argomento | deck | dossier |
|---|---|---|
| i tre livelli e la loro cumulatività | 08 · 09 · A1 | 03 |
| la vista Connect e la causa associata | 03 · 04 | 04 |
| il ranking delle cause per costo | 06 | 05 |
| Refyn, modulo avanzato in sviluppo | 08 | 06 |
| OEE, tre fattori, quattro perdite | 07 | 10 |
| consumo, costo energetico, CO₂ per 1.000 pezzi | 07 | 11 |
| il pilot e i suoi criteri di uscita | 12 | 13 |
| servizi e deliverable | A2 | 14 |
| il modello economico | 12 · A3 | — |
| le assunzioni dei numeri | A5 | — |

Il dossier **non contiene prezzi** e il deck **non contiene specifiche IT**: è una
scelta. Chi decide il budget e chi valuta l’architettura non sono la stessa
persona, e costringerli a leggere le pagine dell’altro allunga entrambi i
documenti senza aiutare nessuno dei due.

---

## 4. Densità dei placeholder

| canvas | placeholder | perché tanti |
|---|--:|---|
| deck 14 · caso cliente | 33 | tutta la slide è da compilare: non esiste un caso autorizzato |
| deck A3 · pricing | 13 | ogni voce del modello ha il suo importo, nessuno approvato |
| dossier A3 · governo | 13 | otto ambiti, ciascuno con valore e responsabile |
| dossier 14 · servizi | 10 | orari, canali, tempi di risposta, aggiornamenti, supporto remoto |
| dossier A4 · KPI | 10 | owner, versione e data di approvazione del dizionario |

Le prime due righe sono anche i due canvas esclusi dalla client edition. Non è un
caso: **la densità di placeholder è un buon indicatore di pubblicabilità**.
