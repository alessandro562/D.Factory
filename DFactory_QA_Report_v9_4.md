# D.Factory · QA Report V9.4 — Dossier tecnico A4

Misurato con Chromium headless sui due HTML consegnati, non sul sorgente.
Motore: `work_v94/qa94.py`.

---

## 1 · Che cosa misura questo QA, e perché è diverso da quello della V9.3

Il QA della V9.3 misurava canvas 1280×720 con il contenuto in posizione
assoluta: lì i difetti erano collisioni, sovrapposizioni e blocchi troppo vicini.
Su A4 il contenuto scorre, e collidere è impossibile. I difetti sono altri:

| controllo | soglia | perché |
|---|---|---|
| formato della pagina | esattamente 794 × 1123 | una pagina che non è A4 non si stampa come A4 |
| niente fuori pagina | tolleranza 0,6 px | `overflow:hidden` nasconde il difetto, non lo risolve |
| stacco dal piede | ≥ 10 px | il contenuto addosso al piede si legge come un errore di impaginazione |
| corpo del testo di contenuto | ≥ 12,0 px | distanza di lettura di un A4 in mano |
| corpo delle etichette | ≥ 10,4 px | mono maiuscolo, ancore e numeri d'ordine |
| corpo dentro i disegni | ≥ 10,9 px | misurato con la scala del `viewBox` |
| elemento visivo | ≥ 1 per pagina | copertina e chiusura esenti: sono la pagina stessa |
| pagine scure | fra 3 e 5 | §9.5 |
| mai 4 pagine di fila senza visivo | — | §9.5 |
| richieste di rete | 0 | il documento deve essere identico offline |

### 1.1 Le soglie tipografiche sono più basse del deck, e la ragione è dichiarata

Il deck ha corpo minimo 18 px perché si guarda proiettato a cinque metri. Il
dossier ha corpo minimo 12 px perché si legge a trenta centimetri, e a quella
distanza 12 px su A4 corrispondono a circa 9 pt su carta: il corpo di una
scheda tecnica, non di un volantino. Le due soglie non sono confrontabili e non
devono esserlo.

### 1.2 Un numero d'ordine non è testo di contenuto

Il primo giro di QA segnalava come «corpo sotto soglia» gli `01`, `02`, `a`,
`b` degli elenchi strutturati. Non è un difetto: quelli sono ancore, e servono
piccoli. Il classificatore adesso li separa dal testo, e la soglia di 12 px
resta piena per il testo vero.

---

## 2 · Esito

| edizione | pagine | difetti |
|---|---|---|
| working | 22 | **0** |
| client | 22 | **0** |

| misura | working | client |
|---|---|---|
| stacco minimo dal piede | 96,2 px (P17) | 103,3 px (A2) |
| corpo minimo del contenuto | 12,0 px | 12,0 px |
| corpo minimo delle etichette | 10,5 px | 10,5 px |
| pagine scure | 5 | 5 |
| placeholder residui | — | **0** |
| richieste di rete | 0 | 0 |
| errori di console | 0 | 0 |

---

## 3 · Pagina per pagina · client edition

`vuoto` è lo spazio fra l'ultimo blocco di contenuto e il piede.
`copy` sono le parole di testo, escluse etichette, ancore e disegni.

| # | pagina | sez. | vuoto | visivi | copy | fondo |
|---|---|---|---|---|---|---|
| 01 | copertina | — | 192 px | — | 22 | scuro |
| 02 | come si legge | 0 | 231 px | 2 | 243 | chiaro |
| 03 | executive summary | 1 | 237 px | 1 | 187 | scuro |
| 04 | dal segnale alla decisione | 1 | 230 px | 2 | 131 | chiaro |
| 05 | Connect | 1 | 156 px | 1 | 170 | chiaro |
| 06 | Insight | 1 | 137 px | 2 | 178 | chiaro |
| 07 | Refyn | 1 | 125 px | 4 | 188 | chiaro |
| 08 | perimetro dei tre livelli | 1 | 226 px | 1 | 164 | chiaro |
| 09 | sorgenti e punti di misura | 2 | 119 px | 1 | 189 | chiaro |
| 10 | modello di contesto | 2 | 212 px | 2 | 146 | scuro |
| 11 | architettura e integrazione | 2 | 107 px | 1 | 149 | chiaro |
| 12 | sicurezza e ciclo di vita | 2 | 233 px | 1 | 192 | chiaro |
| 13 | OEE di linea | 3 | 145 px | 2 | 200 | chiaro |
| 14 | energia, costo e CO₂ | 3 | 189 px | 3 | 143 | chiaro |
| 15 | output e integrazioni | 3 | 144 px | 2 | 194 | chiaro |
| 16 | delivery e pilot | 4 | 131 px | 1 | 210 | scuro |
| 17 | servizi e continuità | 4 | 112 px | 1 | 204 | chiaro |
| 18 | chiusura | — | 203 px | — | 60 | scuro |
| A1 | compatibilità tecnica | A | 232 px | 2 | 205 | chiaro |
| A2 | dimensionamento | A | 103 px | 2 | 195 | chiaro |
| A3 | requisiti IT e security | A | 276 px | 1 | 198 | chiaro |
| A4 | dizionario KPI | A | 133 px | 1 | 161 | chiaro |

### 3.1 Sulla colonna «vuoto»

Nessuna pagina è piena fino al piede, ed è voluto: un documento in cui tutte le
pagine finiscono alla stessa riga si legge come un modulo. Le pagine che
respirano di più sono le due di apertura e chiusura, l'indice e A3 — dove la
colonna del valore di progetto è vuota per costruzione, perché si compila con
l'IT del cliente.

La working edition e la client edition differiscono su tre pagine (P17, A1, A3):
i valori di segnaposto occupano più spazio delle formulazioni prudenti che li
sostituiscono. È la ragione per cui la working edition è la
versione stretta, e il QA gira su entrambe.

---

## 4 · Contenuti verificati dal build, non dall'occhio

`work_v94/mk_dossier94.py` blocca il build se una di queste condizioni cade.

| controllo | soglia | esito |
|---|---|---|
| paragrafo esplicativo §12.2 | 45–100 parole su ogni pagina core | 16 su 16 ✓ |
| «solution design» | ≤ 8 nel documento | 7 ✓ |
| «da verificare» nel core | ≤ 1 | 1 ✓ |
| «da verificare» negli annessi | ≤ 2 | 0 ✓ |
| «da approvare» | 0 | 0 ✓ |
| «da nominare» | 0 | 0 ✓ |
| «chi decide» nel core | 0 | 0 ✓ |
| «owner» nel core | 0 | 0 ✓ |
| placeholder non dichiarati | 0 | 0 ✓ |
| token di testata non espansi | 0 | 0 ✓ |

---

## 5 · Che cosa questo QA non dice

1. **Che i numeri siano veri.** P06, P13 e P14 portano un dataset illustrativo,
   coerente al suo interno e dichiarato tale nel piede di ogni pagina che lo usa.
   Nessuno di quei numeri viene da un impianto reale.
2. **Che il documento sia inviabile.** G1 è aperto: denominazione, referente e
   data si compilano prima dell'invio, e la pagina di chiusura lo dice.
3. **Che la vista di P05 sia il prodotto.** È una ricostruzione grafica.
   L'asset register non contiene nessuno screenshot reale.
4. **Che il marchio sia quello giusto.** Il file originale non è mai stato
   consegnato: copertina e chiusura tengono lo spazio riservato e vuoto.
5. **Che il dimensionamento sia dichiarato.** G4 è aperto: CPU, RAM e storage si
   chiudono con l'audit tecnico, e A2 lo dichiara riga per riga.

---

## 6 · Livello dichiarato

**narrativa ready ✓ · assessment ready ✓ · commerciale ready ✗ (G1, G2) ·
IT-ready ✗ (G4)**

Il documento è pronto per essere usato in un assessment e in un solution design.
Non è pronto per essere inviato senza referente, né per rispondere a un
questionario IT con i valori compilati.
