# D.Factory · Content Map v8

Ogni canvas con la domanda a cui risponde, il dato che porta e la fonte di quel
dato. Serve a due cose: sapere dove toccare quando un input arriva, e verificare
che nessun numero sia scollegato dagli altri.

---

## 1. Sales Deck · 16 slide + 5 appendici

`tensione → categoria → prodotto → prova → ampiezza → offerta → valore → acquisto`

| # | id | domanda del lettore | dato | fonte del dato |
|---|---|---|---|---|
| 01 | `s01_cover` | di che cosa mi stai parlando? | 1.820 € · 162 € · 735 kWh | dataset illustrativo · A5 |
| 02 | `s02_tensione` | perché ne ho bisogno adesso? | — | — |
| 03 | `s03_categoria` | che categoria di prodotto è? | OEE 71,4% · 26 min · 6.720 € | dataset illustrativo · A5 |
| 04 | `s04_evento` | mi fai un esempio? | fermo 11:24 · 18 min · 78 kWh | dataset illustrativo · A5 |
| 05 | `s05_prodotto` | come lo vedo? | 1.260 € = 18 min × 500 pz/min × 0,14 €/pz | A5 |
| 06 | `s06_energia` | e l’energia? | 0 pz/min · 38 kW a linea ferma | A5 · **perimetro dei 38 kW da chiudere · T12** |
| 07 | `s07_priorita` | e poi? | 14 eventi · 96 min · 6.720 € · 43% · totale 15.680 € | dataset 7 giorni · A5 |
| 08 | `s08_ampiezza` | copre solo i fermi? | 71,4% · 735 kWh · 3,2 kWh/1.000 pz · 162 € | A5 |
| 09 | `s09_offerta` | come è organizzata l’offerta? | 6.720 € · 4.340 € · 162 € · baseline 96 min | A5 |
| 10 | `s10_livelli` | quale livello è per me? | — | struttura · **prezzi in A3 quando approvati** |
| 11 | `s11_servizi` | che cosa compro oltre al software? | — | brief §11 |
| 12 | `s12_perche` | perché dovrei fidarmi? | 500 pz/min → 0 · 95 kW → 38 kW | A5 |
| 13 | `s13_valore` | quanto vale? | 96 × 70 × 46 = 309.120 € · 154.560 € · 810 € | A5 |
| 14 | `s14_struttura` | quanto costa iniziare? | — | struttura · **importi mancanti · C1–C5** |
| 15 | `s15_pilot` | che cosa ricevo dal pilot? | — | **durata e prezzo mancanti · C8** |
| 16 | `s16_cta` | qual è il prossimo passo? | 15.680 € · 309.120 € | A5 · **contatto mancante · A2** |
| A1 | `a1_matrice` | che cosa comprende ogni livello? | 8 capacità + cliente ideale | perimetro dichiarato |
| A2 | `a2_servizi` | quali servizi esistono e che cosa producono? | 9 servizi | brief §11 · **inclusioni in C6** |
| A3 | `a3_pricing` | com’è fatto il modello economico? | — | struttura · **importi in C1–C5** |
| A4 | `a4_faq` | le domande che arrivano sempre | — | rimandi al dossier |
| A5 | `a5_assunzioni` | da dove vengono i numeri? | i parametri + 3 formule | **da validare · V1** |

### La catena dei numeri, in un punto solo

Tutto il deck si ricostruisce da questi parametri. Se uno cambia, si tocca A5 e si
propaga:

```
scenario: un turno al giorno, 5 giorni, 46 settimane = 230 turni

500 pz/min · 0,14 €/pz            → 70 €/min
fermo 18 min                      → 1.260 €
turno: 3 fermi, 26 min            → 1.820 €
7 giorni: 58 eventi, 224 min      → 15.680 €  ·  prima causa 43%
anno: 96 × 70 × 46                → 309.120 €  ·  metà = 154.560 €
95 kW marcia · 38 kW fermo        → turno 719 + 16 = 735 kWh
735 kWh × 0,22 €/kWh              → 162 €
454 min × 500 pz/min              → 227.000 pezzi
735 ÷ 227.000 × 1.000             → 3,2 kWh · 0,71 € · 1,13 kgCO₂e per 1.000 pz
94,6% × 79% × 95,6%               → OEE 71,4%
16 kWh/turno × 230 turni × 0,22   → 810 € di energia evitabile
```

---

## 2. Dossier tecnico · 14 pagine core + 4 annessi

Quattro sezioni: `1 Prodotto` · `2 Dati e architettura` · `3 Misure e analisi` ·
`4 Delivery e supporto`. Le aperture di sezione sono fasce scure in testa alla
prima pagina della sezione: 07, 10 e 13.

| # | id | sez. | template | domanda del lettore | stato del contenuto |
|---|---|---|---|---|---|
| 01 | `p01_cover` | — | A | che documento ho in mano? | completo |
| 02 | `p02_overview` | 1 | B | che cosa fa, richiede e restituisce? | completo |
| 03 | `p03_livelli` | 1 | C | come è fatto il prodotto? | completo |
| 04 | `p04_connect` | 1 | B | che cosa vedo? | vista ricostruita · **S1** |
| 05 | `p05_insight` | 1 | B | che cosa capisco? | vista ricostruita · **S1** |
| 06 | `p06_refyn` | 1 | C | che cosa governo? | funzionamento previsto · modulo in sviluppo |
| 07 | `p07_sorgenti` | 2 | D | da dove leggete? | completo |
| 08 | `p08_architettura` | 2 | C | dove gira e come parla con la mia rete? | **T1–T7 aperte** |
| 09 | `p09_contesto` | 2 | B | perché il dato grezzo non basta? | completo |
| 10 | `p10_oee` | 3 | C | come calcolate l’OEE e che perdite vedete? | dataset illustrativo · **V1** |
| 11 | `p11_energia` | 3 | C | come arrivate al costo energetico del pezzo? | dataset illustrativo · **V1, T12** |
| 12 | `p12_output` | 3 | D | come esce il dato? | **T10 aperta** |
| 13 | `p13_pilot` | 4 | C | come si svolge? | criteri completi · **durata e costo in C8** |
| 14 | `p14_servizi` | 4 | D | e dopo il go-live? | **livelli di supporto in C10** |
| A1 | `pa1_compatibilita` | 2 | D | funziona sui miei PLC? | metodo di verifica · **esito in T9** |
| A2 | `pa2_sizing` | 2 | C | che ambiente devo prevedere? | metodo di calcolo · **taglie in T2** |
| A3 | `pa3_governo` | 2 | D | come governate sicurezza e dati? | ambiti e responsabilità · **valori in T4–T8** |
| A4 | `pa4_kpi` | 3 | D | come sono definiti gli indicatori? | **completo** |

**A4 è l’unico annesso completo**, perché le formule dipendono dal metodo e non da
dati che non abbiamo. A1, A2 e A3 dicono che cosa si verifica, come e chi decide:
è contenuto vero e utile a chi legge, ma non sostituisce le risposte.

---

## 3. Dove il deck e il dossier si toccano

Cinque punti in cui i due documenti dicono la stessa cosa e devono restare
allineati se uno dei due cambia.

| argomento | deck | dossier |
|---|---|---|
| i tre livelli e la loro cumulatività | 09 · 10 · A1 | 03 |
| la vista Connect e le sue tre aree | 03 · 05 | 04 |
| il ranking delle cause per costo | 07 | 05 |
| OEE, i suoi tre fattori e le quattro perdite | 08 | 10 |
| consumo, costo energetico e CO₂ per 1.000 pezzi | 08 · 12 | 11 |
| il pilot e i suoi criteri | 15 | 13 |
| i servizi e i loro deliverable | 11 · A2 | 14 |
| il modello economico | 10 · 14 · A3 | — *(il dossier non parla di prezzi)* |
| le assunzioni dei numeri | A5 | — *(il dossier rimanda al deck)* |

Il dossier **non contiene prezzi**: è una scelta, non una dimenticanza. Il lettore
tecnico non è quello che decide il budget, e mescolare le due cose costringe
entrambi a leggere pagine che non li riguardano.
