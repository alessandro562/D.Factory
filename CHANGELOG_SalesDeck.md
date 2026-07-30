# Sales deck: da Refyn a D.Factory (Refyn come modulo di punta)

Da `Refyn_SalesDeck.pdf` (28 slide, brand Refyn) a `DFactory_SalesDeck.pdf` (30 slide,
brand D.Factory). Sorgente HTML standalone in `DFactory_SalesDeck.html`.

**Nota sul punto di partenza.** Nel repo non c'era l'HTML del deck, solo i PDF renderizzati
(che sono PDF veri, con le slide come immagini). L'HTML è stato quindi riscritto da zero
seguendo le convenzioni esistenti: dossier editoriale con cartiglio e frame, viewport
1280x720, Geist/Geist Mono embeddati in base64, slide targettate per id DOM. Da qui in
avanti l'editing per `str_replace` sui file in `deck/src/` funziona come da convenzione.

---

## 1. Brand swap: Refyn -> D.Factory

- **Palette.** Accento unico `#e6e011`, ink `#000000`, base near-white freddo `#fafafb`.
  Rimossi il "bone" caldo e il cadmio delle versioni precedenti, e le sei tinte
  categoriali (verde, blu, rosso, viola, arancio) che marcavano colonne e righe: ora la
  gerarchia è per peso e posizione, non per tinta. QA automatico: zero colori fuori palette.
- **Regole colore rispettate.** Il giallo è accento (barre, top-rule, riempimenti,
  highlight di parole chiave con testo nero sopra), mai fondo diffuso. Nessun testo giallo
  su fondo chiaro in tutto il deck: sul chiaro l'evidenza è un blocco giallo con testo nero,
  sullo scuro il giallo può fare da testo. Verificato a runtime, non a occhio.
- **Momenti bold concentrati:** cover nera, slide 02 "Perché ora" nera, slide 06 Refyn
  giallo pieno con testo nero, slide 30 CTA nera. Le altre 26 tengono la sobrietà del dossier.
- **Logo.** L'asset fornito ha il fondo giallo incorporato e il wordmark spezzato su tre
  righe (artefatto della gabbia quadrata). Da quel file sono state estratte le lettere reali
  e ricomposto un **lockup orizzontale** `D + d.factory`, in due varianti pulite
  nero-su-trasparente e bianco-su-trasparente (`deck/assets/`). Il punto del marchio è
  gestito come controforma, quindi legge correttamente sia su chiaro sia su scuro.
  Nessun wordmark ridisegnato con un font sostitutivo.
- **Cartiglio e masthead.** Codice documento `REF-SLS` -> `DF-SLS`, badge di piede col
  marchio D, masthead col lockup. Tagline di cover ora "Il sistema tra la tua linea e i tuoi
  uffici"; "dato grezzo, decisione raffinata" resta, assegnata al modulo Refyn.
- **Font.** Geist/Geist Mono confermati, variable woff2 embeddati base64. Zero dipendenze
  esterne (verificato: nessuna URL http/https nell'HTML).
- **Struttura invariata:** nessun layout ridisegnato, cambiano colori, logo e copy.

## 2. Refyn riposizionato come modulo

- D.Factory è l'azienda e la piattaforma su tutto il deck. Refyn compare 7 volte, sempre
  come modulo: "il modulo Refyn", "modulo di punta", "in via di definizione". Zero residui
  di "Refyn azienda".
- **Slide 06 (nuova collocazione, giallo pieno)** è il baricentro del deck: "Il software ti
  dà i dati. Noi ti aiutiamo a leggerli." Era la slide 21 dell'originale, spostata in
  apertura di racconto e riscritta come presentazione del modulo, con i cinque servizi e la
  nota esplicita che il perimetro si chiude in fase di offerta.
- **Slide 23 (pacchetti):** Connect e Insights restano marchiati D.Factory, la fascia alta
  Performance diventa **Refyn**, con tag "in via di definizione". Nessun prezzo in euro:
  restano nel piano industriale, in slide si rimanda alla fase di offerta.
- La logica di naming "raffinare il dato grezzo" è conservata e applicata al modulo.
- Cosa non viene spacciato per esistente: sulla slide 08 la manutenzione predittiva, la
  qualità predittiva, il video streaming e gli indicatori operatore sono raccolti in una
  quarta colonna **ROADMAP / NON DISPONIBILE OGGI**. Nell'originale predittiva e qualità
  predittiva stavano in una colonna di capability come se fossero disponibili.

## 3. Contenuti investor e finanziari

- Il sales deck di partenza **non conteneva slide investor**: DCF, valutazione, cap table,
  ARR, break-even e il €500K stavano nel *company deck* (`Refyn_CompanyDeck.pdf`, slide
  27-31). Da lì non è stato importato nulla di finanziario.
- Verifica sul testo del deck costruito: 0 occorrenze di DCF, cap table, valutazione,
  ARR/MRR, churn, expansion, EBITDA, pre-seed/SAFE, round, proiezioni, CAC/LTV, investitore.
- Gergo investor ripulito anche dove era innocuo: "churn 0%" è diventato **"0 clienti che
  hanno abbandonato"**, linguaggio da cliente e non da metrica di cohort.
- Dal company deck sono stati importati **solo due contenuti di vendita**, quelli che
  reggono la narrativa: il "Perché ora" (slide 02) e la matrice competitiva (slide 25).
  Non è stata importata la market sizing (€10 mld parco macchine, quote di mercato): è
  materiale da investitore, non serve a un capo stabilimento.
- La slide **ROI/payback resta** (slide 24): è vendita. Doppio flag "ESEMPIO" sulle due leve
  e riquadro "ESEMPIO ILLUSTRATIVO" con la precisazione che i numeri si calibrano in audit e
  che il payback non è una promessa contrattuale.
- La slide gruppo (28) è stata riscritta come **continuità del fornitore** e spostata da
  fondo nero a carta: il €145M di Clevertech serve a de-riskare la scelta del fornitore, non
  a raccontare un moat. Il moat è raccontato altrove come radicamento operativo.

## 4. Rafforzamento narrativo

- **Apertura sul "perché ora" (slide 02, la seconda del deck).** Quattro forze convergenti
  con fonti in piedi di slide: divario energia PMI (CGIA 2024), Scope 3 di filiera (CDP),
  iperammortamento 4.0-5.0 della L. 199/2025 fino a settembre 2028, Omnibus I sulla CSRD.
  Transizione 5.0 è citata come chiusa, non come attiva. La chiusa non promette obblighi
  che non esistono: "da opzionale a requisito di fornitura", che è quello che accade
  davvero, via contratti e non via legge.
- **Dolore del buyer affilato (slide 03).** Dai tre box generici dell'originale
  (produzione / energia / macchine miste) a quattro dolori operativi e riconoscibili:
  la causa del fermo ricostruita a memoria il giorno dopo, il costo reale per pezzo che
  non si sa, la bolletta che arriva a mese chiuso e aggregata, due linee gemelle con resa
  diversa e nessuno che sappia dire perché.
- **Il differenziale è ora il centro del deck** e non una slide in coda: "il software ti dà
  i dati, noi ti aiutiamo a leggerli" è la slide 06, a fondo giallo pieno, ed è
  esplicitamente Refyn.
- **Prova e fossato (slide 27).** 10 clienti, ~70 macchine su ~30 linee, 24 mesi, zero
  abbandoni, raccontati come radicamento operativo: "il sistema è la fonte operativa su cui
  le squadre decidono ogni giorno, e per questo nessuno lo ha spento". Nessun accenno a
  risorse del gruppo madre o ad asset di dati non provati.
- **Posizionamento onesto (slide 25).** Matrice competitiva con Miraitek, Zerynth,
  40Factory e Guidewheel. I tre italiani sono segnati **parziali** su energia per stato,
  MID, Scope 1-2 ed ESG, non assenti, e la nota lo dice a parole: "tutti e tre hanno moduli
  di monitoraggio energetico ed ESG, la differenza è l'integrazione con lo stato macchina,
  non la presenza della funzione". Conservato il riquadro "dove il mercato è avanti oggi",
  che ammette copilot generativi, predittiva e plug-and-play in mano ai competitor.
- **CTA unica** su tutto il deck: l'audit di linea. Slide 29 lo scompone in audit, pilota,
  kickoff, con l'esito di ciascun passo, e aggiunge l'argomento a basso impegno: a valle
  dell'audit il documento resta al cliente anche se non compra. Slide 30 chiude col
  contatto completo.
- **Contatto compilato:** Pablo Degl'Innocenti, referente commerciale,
  pablo.deglinnocenti@marchianisrl.com, D Factory S.r.l., Collecchio (PR).
- **Stile.** Zero trattini lunghi in prosa. Una sola costruzione "Non X. Y." in tutto il
  deck, spesa dove pesa più: "Non è la compliance a far comprare. È la filiera." Rimossa
  quella dell'originale ("Non l'ennesima dashboard"). Zero termini banditi; "time-to-value"
  è diventato "tempo al primo dato".
- **Claim non verificabili rimossi:** il "fino a ~34% di recupero" sull'energia da fermo,
  che non aveva fonte, è sostituito dalla quota non produttiva resa visibile e dalla
  precisazione che quanto si recuperi si stabilisce in audit, asset per asset.

---

## Da confermare col cliente

1. **Wordmark vettoriale ufficiale.** Il lockup è stato ricomposto dalle lettere del webp
   fornito. Se esiste il vettore del rebrand app, va sostituito in `deck/assets/`.
2. **Dominio del sito nuovo:** segnaposto in slide 30, in attesa del sito D.Factory.
3. **Referenze:** i quattro loghi in slide 27 restano testuali, "previa autorizzazione".
4. **Perimetro Refyn:** la slide 23 dichiara "in via di definizione". Quando il perimetro si
   chiude, va sostituito il tag e completato l'elenco.
