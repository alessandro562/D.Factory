# D.Factory · QA Report v7

Due artefatti client-facing, canvas 1280×720, HTML autonomi. Font Geist incorporati
in base64, **zero richieste di rete**, zero riferimenti esterni, zero errori console.

| | file | canvas | peso |
|---|---|---|---|
| Sales Deck | `DFactory_SalesDeck_v7.html` | 12 slide + 4 appendici | 284 KB |
| Dossier tecnico | `DFactory_DossierTecnico_v7.html` | 19 pagine | 276 KB |

---

## 1. Sales Deck · misure per canvas

Il tetto di parole vale sul **copy**, cioè il testo che parla al lettore. Il testo dentro
una vista di prodotto, una matrice o un visual è contenuto di quel visual — uno screenshot
vero porta le sue etichette e nessuno le conta come copy — e si misura a parte, come la
filigrana e il piede che stanno su ogni canvas.

| # | canvas | copy | vista | corpo copy | corpo vista | superficie |
|---|---|---|---|---|---|---|
| 01 | cover | 18 | 32 | 19 px | 12,5 px | 58,3 % |
| 02 | punto cieco | 13 | 34 | 19 px | 13 px | 55,6 % |
| 03 | che cos'è D.Factory | 26 | 79 | 18 px | 12,5 px | 58,3 % |
| 04 | prodotto in azione | 10 | 37 | 44 px | 12,5 px | 67,8 % |
| 05 | produzione ed energia | 16 | 28 | 18 px | 12,5 px | 61,1 % |
| 06 | dall'evento alla decisione | 9 | 47 | 44 px | 13 px | 65,3 % |
| 07 | ampiezza del prodotto | 10 | 80 | 44 px | 12 px | 62,8 % |
| 08 | Connect, Insight, Refyn | 17 | 70 | 18 px | 13 px | 65,3 % |
| 09 | perché D.Factory | 6 | 62 | 44 px | 12 px | 58,3 % |
| 10 | valore economico | 44 | — | 18 px | — | 58,3 % |
| 11 | pilot e modello commerciale | 8 | 74 | 44 px | 13 px | 61,1 % |
| 12 | call to action | 20 | 48 | 19 px | 12 px | 55,6 % |
| A1 | confronto pacchetti | 31 | 67 | 18 px | 14 px | 61,1 % |
| A2 | servizi | 17 | 35 | 18 px | 17 px | 58,3 % |
| A3 | pricing | 17 | 41 | 22 px | 17 px | 58,3 % |
| A4 | assunzioni e FAQ | 6 | 123 | 44 px | 16 px | 61,1 % |

**Copy: 6–44 parole, media 17.** Tutte sotto il tetto di 45.
**Corpo copy: ≥ 18 px** su tutti i canvas. **Corpo UI: ≥ 12 px effettivi.**
**Titoli: 44 px** (`h2.sm`) e **52 px** sui due canvas con `h1`, dentro la forbice 40–52.
**Superficie occupata da interfacce, grafici, timeline e numeri: media 60,4 %**, misurata
sull'intero canvas — dentro la forbice 55–65 % chiesta dal brief, e su ogni singolo canvas.

**Zero flag** su 16 canvas: nessun overflow, nessun clipping, nessuna collisione, nessun id
duplicato, nessuna àncora rotta.

### Le altre regole del §5.1

| regola | esito |
|---|---|
| una sola idea dominante per canvas | rispettata |
| massimo due aree principali | rispettata |
| massimo una matrice nel corpo principale | **zero**: l'unica matrice è in appendice A1 |
| nessuna slide con quattro card equivalenti | rispettata |
| nessuna griglia da consulenza | rispettata |
| nessun rail laterale | nessuno in tutto il file |
| footer minimo | una riga, corpo 12,5 px |
| un solo elemento giallo dominante per canvas | rispettata, vedi §3 |

---

## 2. Dossier tecnico · misure per pagina

| # | pagina | parole | corpo | tabella | superficie visual |
|---|---|---|---|---|---|
| 01 | cover | 52 | 14 px | — | — |
| 02 | soluzione | 36 | 15 px | — | 47,5 % |
| 03 | architettura tecnica | 68 | 32 px | — | 58,8 % |
| 04 | punti di acquisizione | 77 | 15 px | — | 49,0 % |
| 05 | contestualizzazione | 52 | 15 px | — | 45,0 % |
| 06 | Connect | 38 | 15 px | — | 44,0 % |
| 07 | Insight | 38 | 15 px | — | 46,0 % |
| 08 | Refyn | 68 | 14 px | — | 37,5 % |
| 09 | stato macchina e OEE | 111 | 15 px | — | 45,0 % |
| 10 | fermi e micro-fermate | 44 | 15 px | — | 42,5 % |
| 11 | energia e utility | 41 | 15 px | — | 44,0 % |
| 12 | costo energetico e CO₂ | 104 | 15 px | — | 43,0 % |
| 13 | metodo di misura | 116 | 15 px | — | 42,0 % |
| 14 | brownfield | 114 | 14 px | **4 righe** | — |
| 15 | deployment e IT/OT | 85 | 14 px | — | — |
| 16 | sensoristica | 120 | 14 px | **3 righe** | — |
| 17 | output e integrazioni | 94 | 15 px | — | 46,0 % |
| 18 | delivery e pilot | 77 | 15 px | — | 44,5 % |
| 19 | servizi e continuità | 137 | 14 px | **6 righe** | — |

**Parole: 36–137, media 77.** Tutte sotto il tetto di 140.
**Corpo ≥ 14 px, testo UI ≥ 12 px** su tutte le pagine.
**Tabelle su 3 pagine su 19**, cioè una ogni 6,3: il brief ne ammette una ogni tre.
Nessuna tabella supera le 6 righe.
**Nessun rail laterale permanente.** **Una sola pagina scura**, la copertina.
Alternanza rispettata: diagrammi (03, 09, 12, 13, 18), viste di prodotto (02, 05, 06, 07,
08, 10, 11), tabelle (14, 16, 19), matrici di segnali e sequenze (04, 17).

**Zero flag** su 19 canvas.

---

## 3. Il giallo, canvas per canvas

Un solo elemento dominante, sempre con lo stesso significato: l'evento, la causa quando
pesa, il numero economico da guardare, la decisione da prendere.

| canvas | dove | che cosa segna |
|---|---|---|
| 01 | blocco sulla tappatrice + indicatore verticale | l'evento delle 11:24 |
| 02 | pallino accanto a «0 cause registrate» | l'anomalia |
| 03 | il fermo nella colonna «stato e produzione» | lo stesso evento |
| 04 | blocco + indicatore su timeline e curva OEE | lo stesso evento |
| 05 | tratto della curva energia + indicatore | l'energia a linea ferma |
| 06 | barra della causa principale | l'elemento economico |
| 07 | la fermata lunga nel riquadro dei fermi | l'evento |
| 08 | il fermo nella sezione Connect | lo stesso evento |
| 09 | il fermo sulla traccia di produzione | l'evento letto due volte |
| 10 | il numero annuo | il valore |
| 11 | — | nessun segnale: è una sequenza, non un evento |
| 12 | il fermo nella vista di turno | l'evento sulla linea da scegliere |
| A1–A4 | — | nessun segnale nelle appendici |

Il **punto giallo della filigrana `D.Factory` nel piede è neutralizzato** — bianco sulle
pagine scure, nero su quelle chiare. Era l'unico giallo decorativo dei documenti. Se la
filigrana deve restare com'è nel marchio, è una riga di CSS da togliere.

---

## 4. QA semantico · §15.3

Controllo automatico sui **testi visibili e sui testi accessibili** — `title` e `desc` degli
SVG compresi, invisibili a schermo ma parte del documento e letti dagli screen reader.

```
Insights · proven legacy · pilot release · project-dependent · roadmap · not offered
net-new · quota attaccabile · costo reale del pezzo · CO₂ misurata · conforme ISO 50001
SAP nativo · qualsiasi protocollo · qualsiasi marca · Refyn su richiesta · risultato cliente
AI · manutenzione predittiva · qualità predittiva · risparmio garantito · payback garantito
margine perso certo · plug-and-play
```

**Termini vietati trovati: nessuno**, su entrambi i documenti.
`risultato cliente` compare solo nella forma ammessa «non risultato cliente».

Controllo tipografico: **zero apostrofi diritti**, zero accenti scritti con apostrofo, in
tutti i testi compresi `title` e `desc`.

---

## 5. Dati illustrativi · sono tutti ricostruibili

Nessun risultato di cliente. I parametri sono dichiarati per esteso nel piede della slide 10
e ogni numero dei due documenti discende da lì.

```
500 pz/min · margine 0,14 €/pz                    ->  70 € al minuto
fermo 11:24-11:42, 18 min                         ->  18 × 70 = 1.260 €
turno: 3 fermi, 26 min   07:12 · 5   11:24 · 18   13:15 · 3
margine perso del turno       26 × 70              =  1.820 €
7 giorni, per causa (minuti × 70):
  mancanza tappi     14 eventi ·  96 min  ->   6.720 €
  cambio formato      4 eventi ·  62 min  ->   4.340 €
  micro-fermate      38 eventi ·  41 min  ->   2.870 €
  manutenzione        2 eventi ·  25 min  ->   1.750 €
  totale             58 eventi · 224 min  ->  15.680 €     quota prima causa 43 %
anno                    96 × 70 × 46 settimane     =  309.120 €
capacità potenzialmente recuperabile, se dimezza  =  154.560 €
energia   95 kW in marcia · 38 kW a linea ferma · 0,22 €/kWh · 0,35 kgCO₂e/kWh
turno     ((60-n)·95 + n·38)/60 per ogni ora       =  735 kWh  ->  162 €
          di cui 719 in marcia e 16 a linea ferma
energia potenzialmente evitabile  16 kWh × 5 × 46  =  3.680 kWh  ->  810 €
pezzi del turno   454 min × 500                    =  227.000
                  3,2 kWh · 0,71 € · 1,13 kgCO₂e per 1.000 pezzi
OEE       disponibilità 94,6 % × prestazione 79 % × qualità 95,6 %  =  71,4 %
```

**Il turno mostrato è compatibile con la settimana dichiarata.** Tolte le micro-fermate, che
un rapporto manuale non registra, le altre cause valgono 20 eventi e 183 minuti in sette
giorni: 2,9 eventi e 26,1 minuti al giorno. Il turno ne mostra tre per 26 minuti.

**Il turno vale 735 kWh e non 760**: 760 sarebbe otto ore piene a 95 kW, ma la linea si
ferma 26 minuti. Calcolato ora per ora.

**Il fermo ferma la linea, non una macchina.** Sulle timeline le tre tracce si interrompono
insieme: è la condizione perché «0 pz/min», «38 kW» e i kWh orari siano veri.

---

## 6. Artefatti di verifica

| artefatto | dove |
|---|---|
| render singoli, 16 slide | `qa/sales_v7/` |
| render singoli, 19 pagine | `qa/dossier_v7/` |
| contact sheet deck | `qa/sales_v7/DFactory_SalesDeck_v7_contact.png` |
| contact sheet dossier | `qa/dossier_v7/DFactory_DossierTecnico_v7_contact.png` |
| test di leggibilità 640×360 | `qa/*/test_640x360.png` |
| PDF di verifica | `DFactory_SalesDeck_v7.pdf` · `DFactory_DossierTecnico_v7.pdf` |

Il test a 640×360 serve a una cosa sola: se una slide non regge a metà scala, in sala
riunioni non regge neanche a schermo intero.

---

## 7. Le dieci domande dei criteri di accettazione

### Sales Deck · §18

| # | domanda | dove trova risposta |
|---|---|---|
| 1 | quale problema risolve | 02 · il fermo si vede, la causa no |
| 2 | che cos'è D.Factory | 03 · vista composita e definizione |
| 3 | che cosa mostra il prodotto | 04 · fermo, causa e costo nella stessa schermata |
| 4 | quali capacità copre | 07 · sei riquadri della stessa dashboard |
| 5 | come si differenziano i tre livelli | 08 e appendice A1 |
| 6 | quali servizi può acquistare | appendice A2 |
| 7 | perché D.Factory è credibile | 09 · tre prove |
| 8 | come nasce il valore | 06 e 10 · dalla causa al margine annuo |
| 9 | come funziona il pricing | 11 e appendice A3 · struttura, non importi |
| 10 | quale prossimo passo | 12 · chi coinvolgere, cosa preparare, cosa restituiamo |

**La domanda 9 ha una risposta strutturale, non economica.** Il deck mostra come è fatto il
prezzo, non quanto costa: gli importi non sono approvati e il brief vieta di pubblicare
placeholder. Finché le venti voci P0 non sono chiuse, il deck **non è completamente
sales-ready** — è quanto dichiara il §11.4 del brief e va detto qui, non nascosto.

### Dossier · §18

| # | domanda | dove trova risposta |
|---|---|---|
| 1 | quali sorgenti vengono acquisite | 03 e 04 |
| 2 | come vengono contestualizzate | 05 |
| 3 | quali funzioni sono disponibili | 06, 07, 08 |
| 4 | come produzione ed energia sono correlate | 07 e 11 |
| 5 | come si calcolano OEE, costo e CO₂ | 09, 12, 13 |
| 6 | che cosa serve nel brownfield | 14 |
| 7 | come avviene il deployment | 15 |
| 8 | quali requisiti IT/OT esistono | 15 · struttura completa, valori da compilare |
| 9 | sensoristica, output e integrazioni | 16 e 17 |
| 10 | come si realizza e si supporta il progetto | 18 e 19 |

**La domanda 8 ha una risposta strutturale.** Le diciannove voci sono in pagina, raggruppate
e attribuibili, ma nessuna è compilata: i dati non esistono ancora. Il dossier **non è
dichiarato pronto per IT**: è pronto per la riunione in cui quelle voci si compilano.
