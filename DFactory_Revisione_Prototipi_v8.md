# D.Factory · V8 · revisione dei quattro prototipi

Applica la review del 2026-08-03. Sono stati rigenerati **soltanto** i quattro prototipi
indicati al §8. Gli altri otto non sono stati toccati: le loro micro-correzioni sono in
coda per la Fase C, elencate qui sotto in §3 perché non si perdano.

---

## 1. Che cosa è cambiato nei quattro

### P3 · Categoria — `p3_categoria`

| richiesta | applicato |
|---|---|
| titolo più naturale | «**D.Factory trasforma i dati grezzi di linea in evidenze operative.**» — scelta la prima delle due alternative, non entrambe |
| sottotitolo | «Acquisisce i dati, li contestualizza e li rende utilizzabili da Produzione, Energia e Direzione.» |
| rafforzare i tre passaggi | le tre etichette passano da 13 px grigie a **17 px, peso 600, nero**, con il numero in monospaziato: sono ora la gerarchia più alta della slide, sopra il dato che illustrano |
| non presentare Refyn come disponibile | via «Kit tappi a bordo linea · in corso». Ora: etichetta **Azione proposta**, poi «Kit tappi a bordo linea», poi «Baseline 96 min · verifica **proposta** a 4 settimane» e la nota «esempio del flusso Refyn, in sviluppo» |
| mantenere la composizione | invariata: stessa vista, stessa griglia, stesso taglio a due colonne in basso |

### P5 · Pacchetti — `p5_pacchetti`

Ricostruita da zero. Non è più una matrice.

- **Tre zone verticali senza box chiusi**, separate da due filetti. Per ciascuna soltanto
  i tre campi richiesti: `QUANDO SERVE`, `COSA OTTIENI`, `COME SI ACQUISTA`.
- Sotto il nome di ogni livello, tre segmenti mostrano la **cumulatività**: Connect ne ha
  uno pieno, Insight due, Refyn tre. È l'unico elemento che dice che i livelli si
  contengono, e costa tre righe di grafica invece di un diagramma.
- Titolo: «**Scegli il livello dalla decisione che devi prendere.**»
- **Via `canone base`, `canone premium`, `quotazione dedicata`.** Al loro posto la copy
  della review: «Avvio, poi canone ricorrente», «Canone superiore a Connect, da
  approvare», «Modello economico da approvare».
- Riga di chiusura: «Importi, inclusioni e durata contrattuale: appendice commerciale.»
- Nota di piede cambiata da «Importi in corso di approvazione» a «**Modello economico da
  approvare · C1–C4**», così il rimando alla scheda decisioni è esplicito.
- «in sviluppo» compare **una volta sola**, accanto a Refyn.

### P6 · Perché D.Factory — `p6_perche`

Via i tre mini-schemi equivalenti. Ora un solo visual dominante più tre callout.

- **Il visual**: un unico asse orario del turno con due tracce sovrapposte — cadenza di
  produzione sopra, potenza assorbita sotto. Alle 11:24 la produzione va a zero e il
  consumo scende da 95 a 38 kW: il giallo marca lo stesso istante su **entrambe** le
  misure e un connettore verticale le lega. È la prova numero uno resa visibile invece
  che dichiarata.
- **Tre callout laterali** numerati, separati da filetti: produzione ed energia sullo
  stesso asse; si parte dall'impianto esistente; software e competenze insieme.
- **Claim corretto.** «nessuna sostituzione richiesta per iniziare» → «PLC, sensori e
  contatori già in campo. **Eventuali gap di misura e integrazione vengono definiti in
  audit.**»
- **Rimossa** la nota interna sulle prove aziendali mancanti. Quell'informazione vive
  negli Open Inputs, non nella slide.
- Titolo invariato.

### Q1 · Overview — `q1_overview`

- Titolo: «**Dal segnale all'informazione utilizzabile.**» Sottotitolo: «Che cosa
  acquisisce, come contestualizza il dato e quali output restituisce.»
- **Via la matrice di box.** Un solo pannello diviso in tre passaggi numerati, letti da
  sinistra a destra. Una linea continua attraversa tutti e tre e due triangoli sui
  divisori danno il verso: è un flusso, non tre colonne.
- Contenuto dei tre passaggi come da review: controllori / contatori / ordini →
  i sette attributi → viste, indicatori, report ed export.
- A destra restano «Che cosa richiede» e «Che cosa non richiede».
- **Prudenza sul cloud.** Non ho scritto «cloud obbligatorio» fra le cose non richieste,
  perché il deployment on-premise non è confermato (T1). Al suo posto: «Il modello di
  deployment, le quantità e le taglie si definiscono nel solution design, con IT e OT.»

---

## 2. Due scelte che ho fatto e che vanno sapute

**«da approvare» nel corpo della P5.** La review prescrive questa copy al §5, ma il §6.1
dice che «struttura proposta / modello da confermare / importi in approvazione» vanno usati
«solo negli artefatti interni, non nelle slide client-facing definitive». Ho applicato la
copy prescritta perché questi sono prototipi interni. **Prima del freeze client-facing
quelle tre righe devono sparire**, sostituite dagli importi approvati: se C1–C4 non
arrivano, la slide resta interna e il deck non è finale. È lo stesso vincolo del §12 del
brief V8, e non si risolve con il design.

**Il titolo della Q5.** La review chiede «costo energetico del pezzo» e non «costo del
pezzo»; il titolo attuale della Q5 dice «Dal consumo del turno al costo del pezzo». È un
errore di merito, non di forma: il costo del pezzo non è solo energia. Non l'ho corretto
adesso perché il §8 vieta di rigenerare gli altri otto, ma **è la prima micro-correzione
della lista qui sotto**, non una nota a margine.

---

## 3. Le micro-correzioni in coda per la Fase C

Ordinate per gravità, non per numero di pagina. Le prime tre cambiano il significato di
un'affermazione; le altre sono leggibilità e ritmo.

| # | dove | correzione | tipo |
|---|---|---|---|
| 1 | Q5 | titolo «costo **energetico** del pezzo»; mantenere «CO₂ calcolata o stimata» | merito |
| 2 | Q3 | se la sola lettura non è regola tecnica assoluta → «configurazione standard prevista in sola lettura» (**T11**) | merito |
| 3 | Q5 | dichiarare il perimetro dei 38 kW: linea, macchine, ausiliari o stabilimento (**T12**) | merito |
| 4 | Q2 | verificare che «aggiornato 11:33» corrisponda a una frequenza reale (**T13**); usare sempre «causa associata» | merito |
| 5 | Q3 | titolo «**Dove risiede e come comunica con la rete di stabilimento.**» | editoriale |
| 6 | P1 | leggibilità del sottotitolo; la cifra 1.820 € non deve leggersi come risultato cliente | editoriale |
| 7 | P2 | contrasto delle quattro etichette di sorgente e della riga «tempi diversi, perimetri diversi…» | leggibilità |
| 8 | P4 | più peso visivo a Insight e Refyn — oggi Refyn sembra marginale; leggibilità delle due righe di base | leggibilità |
| 9 | Q3 | rendere più visibile il confine dell'ambiente applicativo | leggibilità |
| 10 | Q4 | fascia scura solo sulla prima pagina di sezione; dichiarare il perimetro macchina / linea / turno / calendario | regola |
| 11 | Q6 | massimo 6–8 righe per pagina, continuare su una seconda se serve; colonna «versione / owner» solo se il documento diventa riferimento contrattuale | regola |
| 12 | P1 | decidere se il riferimento food & beverage resta posizionamento o diventa «linee industriali» (**P1 della scheda decisioni**) | posizionamento |

---

## 4. QA dopo la revisione

```
DECK · soglie sales                    DOSSIER · soglie dossier
id            copy vista  vis%         id                copy vista  vis%
p1_cover        18    50  58.3         q1_overview        106     0    34
p2_tensione     21    40  58.9         q2_connect          76    49  37.4
p3_categoria    24    64  59.4  ←rev   q3_architettura    120     0  35.1
p4_offerta      15    79  62.8         q4_oee              95     0  26.6
p5_pacchetti     8    85  63.9  ←rev   q5_energia         127     0  35.6
p6_perche        5   100  61.1  ←rev   q6_annesso          78     0     0
canvas con flag 0/6                    canvas con flag 0/6   ←rev q1_overview
```

Zero elementi fuori canvas, zero collisioni, zero richieste di rete, zero errori di
console, zero id duplicati, zero apostrofi diritti anche nei testi accessibili, nessuno
dei 23 termini della lista semantica.

**Una nota onesta sulla colonna `vista`.** Su P5 e P6 quel numero è alto (85 e 100) perché
la copy è composta dentro l'SVG per avere controllo tipografico: non è cromatura di
interfaccia, è testo che il lettore legge. Il carico reale di lettura della P5 è circa 93
parole, sopra il budget narrativo di 45. È una scelta deliberata — una slide di scelta
commerciale porta più parole di una slide di racconto — e la dichiaro qui invece di
nasconderla dentro una soglia.

Un errore trovato leggendo i render e corretto: sulla P6 l'etichetta «11:24 · lo stesso
minuto, due misure» sconfinava oltre il filetto verticale e finiva sopra il callout 02.
Accorciata e spostata a sinistra del connettore; la colonna dei callout è stata risalita
di 24 px perché l'ultima riga arrivava a filo del bordo inferiore.

---

## 5. Criterio di approvazione del §9

| # | criterio | stato |
|---|---|---|
| 1 | P3 definisce chiaramente la categoria di prodotto | fatto |
| 2 | P5 sembra una scelta commerciale, non una matrice | fatto |
| 3 | P6 costruisce fiducia senza claim assoluti | fatto |
| 4 | Q1 spiega il funzionamento senza sembrare un framework | fatto |
| 5 | il modello commerciale non è presentato come approvato | fatto nel corpo; resta la riserva del §2 |
| 6 | nessun prototipo compensa con il design un input mancante | fatto — P6 non ha più la nota interna, Q1 non nega il cloud, P5 non ha importi |

Mi fermo qui. La Fase C parte su tua conferma.
