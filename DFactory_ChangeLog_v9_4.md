# D.Factory · ChangeLog V9.4 — Dossier tecnico in formato A4

**Perimetro della versione.** Solo il dossier tecnico. Il Sales Deck resta alla
V9.3, canvas 1280×720: una slide si proietta e il formato è corretto così.
Il dossier no — e questa versione lo dice cambiandogli formato.

---

## 1 · Che cosa cambia, e perché

### 1.1 Il formato: da slide 1280×720 ad A4 verticale 794×1123

Il dossier V9.3 era un mazzo di ventidue slide chiamato documento. Da lì
venivano quasi tutti i suoi difetti: il testo doveva stare in fasce orizzontali
larghe 1152 px, le tabelle diventavano griglie disegnate a mano perché una
tabella vera non entrava nel canvas, i diagrammi crescevano in larghezza invece
che in profondità.

Un dossier tecnico non si proietta. Si legge da fermi, si stampa, si passa a un
collega che apre solo la sua pagina. A4 verticale è il formato di quel gesto.

| | V9.3 | V9.4 |
|---|---|---|
| canvas | 1280 × 720 | 794 × 1123 (A4 a 96 dpi) |
| pagine | 21 core + chiusura | 18 core + 4 annessi |
| tabelle | griglie CSS disegnate | `<table>` HTML |
| diagrammi SVG | 11 | 2 |
| frecce | 11 | 0 |

### 1.2 Niente etichette in testa alle pagine

Una prima versione di questa release metteva su ogni pagina una riga di
scrematura: un tassello giallo con il ruolo — `PER L'IT`, `PRODUZIONE` — e una
frase che riassumeva la pagina prima del titolo. È uscita.

Diceva al lettore quello che il titolo già gli dice, e lo diceva con la voce di
un sistema che classifica invece che di una persona che scrive. Un documento
tecnico non ha bisogno di annunciarsi: comincia.

Chi legge trova il proprio percorso a pagina 02, una volta sola, e poi legge.

### 1.3 Il wordmark composto in HTML è uscito da tutte le pagine

La V9.3 ricomponeva «D.Factory» in HTML — testo in grassetto e un punto giallo —
e lo ripeteva nel piede di ventidue pagine. Un marchio non si ricompone: si
incorpora. E ripeterlo a ogni piede è un'abitudine da slide, non da documento.

Adesso il piede porta la riga di dichiarazione e il numero di pagina, niente
altro. Il marchio compare due volte in tutto il documento, in copertina e in
chiusura, e lo spazio è **riservato in altezza** in attesa del file originale:
quando arriva entra lì e non sposta niente.

### 1.4 La pagina 02 · «Come si legge»

Nuova. Quattro percorsi di lettura da tre pagine ciascuno — IT di stabilimento,
produzione, energy manager, direzione e acquisti — più l'elenco dei quattro
annessi con l'indicazione di quando si compilano. In fondo, una frase sola:
*«Se leggi una pagina sola, leggi la 03. Se ne leggi due, aggiungi la 08.»*

Nel formato slide questa pagina non poteva esistere: sarebbe stata una slide di
indice, che nessuno guarda.

### 1.5 Le fusioni e i tagli

| V9.3 | V9.4 |
|---|---|
| P03 architettura funzionale + P04 base comune | **P04** · una pagina sola |
| — | **P02** · come si legge (nuova) |
| 11 diagrammi SVG | 2 (vista Connect, scomposizione OEE) |
| wordmark ricomposto in HTML | 22 volte → 0 |

Le due pagine fuse dicevano lo stesso argomento due volte: la catena che porta
il segnale alla decisione, e la base di dati che la rende possibile. Su A4 stanno
insieme senza comprimere niente.

### 1.6 Le frecce sono uscite tutte

La V9.3 conteneva undici frecce SVG, e le frecce sono state il difetto visivo
più segnalato di tutto il progetto. In V9.4 non ce ne sono più: non perché siano
state disegnate meglio, ma perché ogni cosa che facevano la fa qualcos'altro.

| dove c'era una freccia | che cosa c'è adesso |
|---|---|
| catena funzionale a cinque stazioni | `.seq` — cinque stazioni numerate su una linea |
| pila dei quattro livelli logici | `.stack` — quattro rettangoli sovrapposti, numerati dal basso |
| ciclo di Refyn con ritorno | tre colonne e una frase: *«il ciclo si chiude quando l'effetto è stato misurato»* |
| base comune, quattro frecce verso il basso | una tabella e una fascia nera sotto |

Una sequenza numerata si legge da sinistra a destra senza bisogno di dirlo, e non
ha geometria da sbagliare.

### 1.7 I diagrammi che restano, e perché

Due, e sono entrambi grafici veri con solo barre orizzontali:

- **P05 · vista di linea Connect** — è l'unica ricostruzione di prodotto del
  dossier. Il piede la dichiara.
- **P13 · scomposizione di un turno** — 100% → 94,6% → 74,7% → 71,4%, con la
  capacità persa in giallo a ogni gradino.

Il report di periodo di Insight, che in V9.3 era un finto screenshot disegnato in
SVG, è diventato quello che è sempre stato: una tabella. Si legge meglio, si
stampa meglio, e si può copiare.

---

## 2 · Che cosa non cambia

- **La palette.** Nero, bianco, un giallo acido. Nessun altro colore.
- **I contenuti tecnici.** Nessuna affermazione nuova sul prodotto. Le tre
  correzioni obbligatorie della review D2 restano tutte: «output e sistemi
  esterni» con perimetro da definire, «accodamento e persistenza temporanea» al
  posto di *buffer*, «elaborazione KPI» al posto di *motore KPI*.
- **Le reticenze volute.** La formulazione contrattuale sulla titolarità del dato
  non è pubblicata. Le interfacce applicative non sono dichiarate disponibili.
  CPU, RAM e storage non sono dichiarati.
- **I 221 placeholder** e le due edizioni, working e client.
- **Il livello dichiarato:** narrativa ✓ · assessment ✓ · commerciale ✗ (G1, G2)
  · IT-ready ✗ (G4).

---

## 3 · Le correzioni fatte durante il build, e la loro ragione

| # | difetto | correzione |
|---|---|---|
| 1 | A3 sforava la pagina di 36 px nella working edition | i valori di segnaposto sono passati a `.phv`, corpo mono 11,5 px: sono impalcatura, non testo del documento |
| 2 | P17 finiva a 0,8 px dal piede | la nota su supporto e SLA è salita nel piede, dov'è comunque una dichiarazione |
| 3 | ventidue pagine finivano fra 100 e 315 px sopra il piede | scala tipografica alzata del 4% e quattro pagine allungate con contenuto vero, non con aria |
| 4 | il QA leggeva i numeri d'ordine degli elenchi come corpo del testo | classificati come ancore: la soglia di 12 px vale per il testo, non per un «01» |
| 5 | la cella marcata di P10 era oliva | il giallo al 16% su nero non è giallo. Filetto giallo e fondo più chiaro, niente velatura |
| 6 | «solution design» compariva dodici volte | sette. Sopra le otto la formula diventa un tic e smette di significare qualcosa |
| 7 | la riga di scrematura classificava le pagine invece di lasciarle parlare | tolta da tutte e venti le pagine |
| 8 | il marchio era testo ricomposto, ripetuto ventidue volte | uscito dai piedi; in copertina e in chiusura lo spazio aspetta il file originale |

### 3.1 Le quattro pagine allungate con contenuto

Non con interlinea:

- **P05** · da dove arriva quello che si vede — stato, causa, consumo
- **P07** · che cosa porta con sé un'azione — cinque campi, compresa la baseline
- **P16** · che cosa serve dal cliente, fase per fase
- **A1** · i quattro esiti ammessi del censimento, in tabella

---

## 4 · Verifica

| controllo | esito |
|---|---|
| difetti QA, working edition | **0** su 22 pagine |
| difetti QA, client edition | **0** su 22 pagine |
| formato di ogni pagina | 794 × 1123 |
| stacco minimo dal piede | 96,2 px (working) · 103,3 px (client) |
| corpo minimo del testo di contenuto | 12,0 px |
| corpo minimo delle etichette | 10,5 px |
| paragrafo esplicativo §12.2 | 16 pagine core su 16, fra 45 e 100 parole |
| pagine scure | 5 (§9.5 chiede da 3 a 5) |
| placeholder nella client edition | 0 |
| richieste di rete | 0 |
| errori di console | 0 |

---

## 5 · Che cosa resta aperto

Invariato rispetto alla V9.3, e non è il formato a chiuderlo:

1. **Il marchio originale non c'è.** Il file non è mai stato consegnato e non è
   nel repository: cercato anche dentro i due PDF Refyn, che contengono solo
   pagine rasterizzate. Copertina e chiusura tengono lo spazio pronto; la
   working edition lo dichiara con una casella tratteggiata.
2. **Nessuno screenshot reale di prodotto.** La vista di P05 è una ricostruzione
   e lo dichiara. Finché non arriva una schermata vera, resta tale.
3. **G1 · referente e denominazione** — il documento non si invia senza.
4. **G2 · struttura di prezzo senza importi.**
5. **G4 · dimensionamento e requisiti IT da chiudere in audit.**
6. **Il dataset illustrativo non è validato.** I numeri di P06, P13 e P14 sono
   coerenti fra loro e dichiarati illustrativi, ma non vengono da un impianto.

---

## 6 · Consegna

| file | contenuto |
|---|---|
| `DFactory_DossierTecnico_A4_v9_4_client.html` | 22 pagine A4, zero placeholder |
| `DFactory_DossierTecnico_A4_v9_4_working.html` | 22 pagine A4 con impalcatura editoriale |
| `DFactory_DossierTecnico_A4_v9_4_client.pdf` | stampabile |
| `DFactory_DossierTecnico_A4_v9_4_working.pdf` | stampabile |
| `render/v94/dossier_client/` | 22 PNG più provino a contatto |
| `render/v94/dossier_working/` | 22 PNG più provino a contatto |
| `DFactory_QA_Report_v9_4.md` | misure pagina per pagina |
| `DFactory_ContentMap_Dossier_A4_v9_4.md` | che cosa dice ogni pagina e a chi |

Il sorgente sta in `work_v94/`: `dossier94.css`, `dossier94_parts/` (una pagina
per file), `mk_dossier94.py`, `edition94.py`, `build94.py`, `qa94.py`,
`render94.py`, `build_all94.sh`.
