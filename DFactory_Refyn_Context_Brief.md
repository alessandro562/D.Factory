# D.Factory / Refyn — Brief di contesto e linee guida operative

> **Scopo di questo file.** È il documento di onboarding per una sessione (Claude Code o
> altra AI) che non conosce nulla del progetto. Contiene lo stato aggiornato di tutte le
> decisioni, il contesto, le convenzioni tecniche e le regole di stile. Leggilo prima di
> toccare qualsiasi deliverable. Ultimo aggiornamento sostanziale: dopo la call cliente del
> **17/07/2026**.
>
> Se qualcosa in un deck o in un file contraddice questo brief, **vince questo brief** (i
> materiali possono essere versioni vecchie precedenti alle decisioni qui sotto).

---

## 1. TL;DR (lo stato in dieci righe)

- **WDA** (società di consulenza) segue **D Factory S.r.l.**, azienda software del gruppo
  Marchiani / Clevertech, su materiali commerciali, di brand e finanziari.
- Prodotto: **middleware industriale per il manifatturiero F&B**, on-premise, che sta tra
  la linea di produzione e gli uffici.
- **Il rebranding completo D Factory → Refyn è stato SCARTATO.** Decisione finale:
  **D.Factory resta l'azienda e il brand madre; Refyn diventa un MODULO di punta** (lo
  strato avanzato di servizi sul dato), "in via di definizione".
- Modello: passaggio a **ricavi ricorrenti solo sui NUOVI clienti**. I 10 clienti esistenti
  restano sul pricing legacy (~€1K/anno): niente migrazione forzata.
- **La parte investimento è messa da parte.** Nessun investor deck da produrre ora.
  Financials (DCF, valutazione, cap table) **fuori dal sales deck** cliente.
- Focus attuale: **sales pitch forte marchiato D.Factory + modulo Refyn**, sito nuovo,
  lead generation ad agosto, test prezzi. Follow-up cliente il **31/08/2026**.

---

## 2. Chi è chi

**Lato consulenza (WDA)**
- **Alessandro Piccinini** — il consulente che guida l'ingaggio. Costruisce i deliverable
  (deck, piano industriale, brand, landing) e conduce le call con il cliente. È l'utente di
  riferimento. (Nota: su alcuni account il nome visualizzato può essere diverso; la persona
  è Alessandro.)
- Altri nominativi che compaiono nei thread lato WDA/progetto: Roberto Macina, Valentina
  Iannucci, Enrico.

**Lato cliente (D Factory / gruppo Marchiani)**
- **Thomas Marchiani** — co-fondatore / Chairman, CEO di Marchiani Automation. Decisore
  finale. Email: tomas.marchiani@marchianisrl.com.
- **Pablo Degl'Innocenti** — proposto CEO, referente commerciale. Email:
  pablo.deglinnocenti@marchianisrl.com.
- **Matteo De Simone** — CTO / R&D Manager, unico dipendente formale di D Factory,
  interlocutore tecnico. Email: matteo.desimone@marchianisrl.com.

**Struttura societaria**
- **D Factory S.r.l.**: azienda software, spin-off di **Marchiani Automation**, parte del
  gruppo **Clevertech**. Sede a Collecchio (PR). Fatturato di gruppo ~€145M.

---

## 3. Il prodotto

- **Cos'è**: middleware industriale per il manifatturiero **Food & Beverage**. "Il sistema
  che sta tra la linea e gli uffici." Prende dati grezzi di produzione ed energia e li
  rende leggibili e azionabili.
- **Vocabolario da usare**: la loro identità è **"Supervisione 4.0"**. NON descriverlo come
  MES/MOM come identità di prodotto (i termini MES/MOM si usano solo per raccontarne
  l'origine, non l'identità).
- **Due anime** (possono interessare la stessa azienda):
  - **Produzione / OEE** — supervisione produzione in tempo reale, base **PackML** (motore:
    MAPST 4.0).
  - **Energia** — monitoraggio energetico/utility (motore: MarEnergy).
- **Deployment**: **on-premise**, PC industriale Linux, **air-gapped**. NON è un SaaS cloud.
- **Trazione**: ~70 macchine, ~30 linee, **10 clienti**, **churn 0%**, 24 mesi di produzione
  continua. (Attenzione: non "70+ clienti"; sono 70 macchine e 10 clienti.)
- **Il differenziale (servizi a valore aggiunto)**: "Il software ti dà i dati. Noi ti
  aiutiamo a leggerli." Include: analisi avanzata del dato, report di efficienza, fitting
  della formula OEE del cliente, strategia sensori, affiancamento continuo.
- **Delivery / sensori**: clamp-on (errore 1–5%, nessun fermo linea) vs certificati (MID,
  ISO 50001, fermo pianificato). Messaggio onesto sul trade-off precisione/costo/fermo.

---

## 4. Le decisioni chiave (aggiornate al 17/07/2026)

### 4.1 Brand — D.Factory azienda, Refyn modulo
- **Rebranding aziendale completo SCARTATO.** Troppo pesante per un'entità già strutturata,
  dentro un gruppo, con l'app appena ri-brandizzata.
- **D.Factory = brand azienda e piattaforma**, su tutto il materiale. Resta l'entità legale.
- **Refyn = modulo di punta**, lo strato avanzato di servizi/advisory sul dato (corrisponde
  alla fascia alta "Performance"), presentato come **"in via di definizione"**, di punta ma
  non ancora del tutto spedito. Modello mentale: come i moduli di **Zucchetti**.
- Il concetto di naming **sopravvive**: Refyn = **"raffinare il dato grezzo"**, applicato al
  modulo. Le fasce base (visibilità, energia) restano marchiate D.Factory; la fascia alta
  diventa Refyn.
- Qualsiasi contenuto che parla di "rebranding aziendale a Refyn" va riscritto come
  "D.Factory, con Refyn come modulo di punta".

### 4.2 Modello commerciale — ricorrente sui nuovi
- Passaggio dall'una-tantum (installazione) verso **ricavi ricorrenti**, accettato in
  principio **solo per i NUOVI clienti**.
- **Clienti esistenti (10) restano sul legacy** (~€1K/anno): niente migrazione forzata a
  prezzi più alti (Thomas l'ha esclusa esplicitamente). Qualsiasi ipotesi di modello o di
  piano che facesse migrare gli esistenti a prezzi superiori **va rimossa/ricalcolata**.
- **Prezzi da validare** sul mercato reale (test con prospect ad agosto). I numeri attuali
  sono ipotesi, non validati.

### 4.3 Investimento — deferito
- Ingaggio originario: spin-off + **pre-seed SAFE €500K a cap €2.5M**.
- **Ora la raccolta è messa da parte.** "D Factory non è più una startup round zero"
  (Pablo). Il near-term è modernizzazione commerciale e di prodotto, non fundraising.
- Conseguenze operative: **nessun investor deck da produrre ora**; **togliere DCF,
  valutazione, cap table, proiezioni finanziarie dal sales deck cliente**; tenere
  un'eventuale versione investor **separata** per dopo.

---

## 5. Stato dei deliverable

| Deliverable | Stato | Azione richiesta |
|---|---|---|
| Sales deck | Esiste, marchiato Refyn | Ri-brandizzare D.Factory + Refyn modulo; togliere financials; rafforzare la narrativa |
| Company deck / profile | Esiste | Aggiornare a brand D.Factory |
| Piano industriale 3Y + DCF (Excel) | Esiste | Rivedere: esistenti su legacy, ricorrenza dai nuovi; ricalcolare ARR e valutazione |
| Brand identity Refyn | Esiste come rebrand aziendale | Ri-scopare come brand di modulo dentro D.Factory |
| Landing page | Prima bozza | Riadattare a D.Factory |
| Sito D.Factory + dashboard | Da fare | Sito nuovo (look non-template); dashboard aggiornate (bassa priorità) |

---

## 6. Brand & identità visiva

### 6.1 Palette (unica, definita dal cliente)
- **Primario / accento: `#e6e011`** (giallo acido).
- **Ink / testo: `#000000`** (nero).
- **Base / sfondo: `#ffffff`** o near-white pulito e freddo (NON il "bone" caldo delle
  versioni precedenti).
- Nessun altro colore in palette.

### 6.2 Regole colore (vincolanti)
- Il giallo `#e6e011` è **ACCENTO**, non sfondo diffuso: riempimenti, barre, highlight di
  parole chiave, forme d'accento. Non "giallo-washare" le slide.
- Contrasto: **nero su giallo OK · bianco su nero OK · MAI testo giallo su bianco/chiaro**
  (sparisce).
- Nel recolor: sostituire ovunque il vecchio accento "cadmio" con `#e6e011` e il neutro
  "bone" caldo con near-white freddo.
- Momenti bold concentrati: 2–3 slide full-bleed (nere, oppure gialle con testo nero) su
  apertura "5.0" e su CTA/chiusura. Il resto tiene la sobrietà del dossier.

### 6.3 Logo
- Marchio **"d.factory"**: D nera con dot bianco + wordmark.
- L'asset fornito (`Logo-D-Factory-*.webp`) ha il **fondo giallo incorporato**: non si posa
  bene su chiaro né su scuro. Servono varianti **pulite nero-su-trasparente** e
  **bianco-su-trasparente** (idealmente dal vettore del rebrand app; in alternativa estratte
  dal webp).

### 6.4 Formato deck (invariato, è ciò che al cliente è piaciuto)
- Deck **HTML standalone**, stile **dossier editoriale** (cartiglio, frame border, slide
  numerate). Viewport **1280×720**.
- Font **Geist / Geist Mono** per il corpo. Il display del logo resta solo nel logo, non va
  esteso alle slide. La struttura sofisticata NON va stravolta in un deck giallo-nero da
  agenzia: si innesta il brand sulla struttura esistente.

---

## 7. Il modello commerciale in dettaglio (in revisione — trattare come ipotesi)

**Tre tier, "dalla visibilità alla performance"** (i prezzi in euro NON sono nel sales deck,
si definiscono in fase di offerta; vivono nel piano industriale):

- **01 · Connect** (base, D.Factory) — visibilità: supervisione linea live, OEE in tempo
  reale, vista multi-macchina.
- **02 · Insights** (★ raccomandato, D.Factory) — efficienza + energia: analisi fermi e
  cause, energia per stato / costo·CO₂ per pezzo, report multilingua.
- **03 · Performance / Operator Performance = modulo REFYN** ("in via di definizione") —
  Operator Performance Index + **servizi di advisory sul dato**.

**Pricing journey nel piano (da rivedere, esistenti esclusi dalla migrazione):**
land-low → expand. Prezzi €/anno indicativi per fase: Connect 2.500→5.000, Insights
6.000→15.000, Performance 0→30.000; setup fee nuovo cliente ~22.000→30.000. **Nota: la
componente ricorrente cresce nel tempo, ma nei primi anni il grosso dei ricavi è il setup
una-tantum. Non è un SaaS puro.**

**ROI (resta nel sales deck, è vendita non investor)**: payback su **due leve misurabili →
OEE recuperato + energia ottimizzata**. Esempio ≈ €69.000/anno, payback < 6 mesi su linea
pilota, **sempre flaggato "ESEMPIO ILLUSTRATIVO, calibrato in audit"**.

**Motion commerciale**: audit di linea → pilota → kickoff → estensione ad altre linee +
attivazione servizi a valore aggiunto. CTA unica: "fissiamo l'audit di linea", primo passo
a basso impegno.

---

## 8. Contesto regolatorio e competitivo (per la narrativa "Perché ora")

- **EU Omnibus I (marzo 2026)** ha ridotto sensibilmente lo scope della **CSRD**.
- **Transizione 5.0**: i crediti d'imposta sono **scaduti**, sostituiti
  dall'**iperammortamento (L.199/2025)**. La narrativa "Perché ora / Industry 5.0" deve
  riflettere questo, non citare Transizione 5.0 come attiva.
- **Competitor**: **Zerynth, Miraitek, 40Factory** offrono **moduli di monitoraggio
  energetico/ESG**. Nella matrice competitiva NON marcarli "assente" su quelle voci: è
  falso.

---

## 9. Convenzioni tecniche & pipeline (per Claude Code)

**Deck**
- HTML standalone. Le slide si targettano **per id DOM**, NON per numero visualizzato
  (offset che parte da `s07_super`).
- Editing: script **Python `str_replace`** con guardia di unicità `assert s.count(old)==1`.
- Render: **Playwright/Chromium** → PNG per slide a **1280×720**, `device_scale_factor=3`,
  attesa `networkidle` + `document.fonts.ready` + **600ms** → assemblaggio **PDF via
  img2pdf** a **13.333"×7.5" (960×540pt)**.
- Font **Geist** embeddati **base64** dal pacchetto npm `geist`
  (`node_modules/geist/dist/fonts/`), **nessuna dipendenza CDN**.

**File "deck" esportati**
- I file con estensione `.pdf` esportati dal pipeline sono in realtà **archivi ZIP** che
  contengono le slide come **immagini JPEG** (+ manifest). `pdftotext` NON funziona:
  estrarre con `unzip` e leggere le immagini (view / OCR).

**Piano industriale (Excel)**
- Fogli chiave: **"Pricing Journey", "Assumptions", "InputBase", "Riepilogo"** (più
  Valuation, Simulation Con/Senza Parent, DCF 5Y, Cassa & Round, Cap Table, Capex). Dati
  concentrati nelle prime ~50–80 righe.

**Transcript DOCX**: leggibili unzippando e parsando `word/document.xml` con ElementTree.

**Deploy landing**: **Vercel**, sito statico, entry `index.html`, `vercel.json` con
`cleanUrls: true`.

**Path**: input in `/mnt/project/` e `/mnt/user-data/uploads/`; output in
`/mnt/user-data/outputs/`.

---

## 10. Regole di stile e guardrail (non negoziabili)

**Verità e rigore**
- **Nessun dato inventato o non verificabile.** Ogni claim numerico deve avere una fonte
  primaria tracciabile. I numeri illustrativi vanno flaggati come tali.
- **Refyn "in via di definizione"**: non spacciarlo come già completo. Non presentare
  **AI / modulo predittivo / benchmark di settore** come esistenti (sono roadmap).
- **Moat**: raccontarlo come **radicamento operativo** (churn zero, sistema che è la fonte
  di verità quotidiana negli impianti), NON come risorse del gruppo madre né come asset di
  dati non provato.

**Stile di scrittura (copy cliente, italiano)**
- Professionale ma caldo, senza filler, senza costruzioni "da AI".
- **Niente trattini lunghi (em-dash) nella prosa.**
- Al massimo **una** costruzione "Non X. Y." in tutto il deck, allocata di proposito.
- Firma con il nome proprio (Alessandro); elenchi puntati per le liste di deliverable.

**Termini banditi**
- world-class, seamless, game-changer, disruptive, "engine" come anglicismo, packaging-native,
  cross-vertical, "go-to-market" (salvo contesto tecnico preciso).
- **Niente MES/MOM come identità di prodotto**: usa "Supervisione 4.0" e "il sistema tra la
  linea e gli uffici".

**Disciplina finanziaria**
- I financials nel deck vanno sempre cross-checkati contro il piano industriale in Excel:
  figure stagnanti hanno già causato incoerenze tra versioni.

---

## 11. Prossimi step & timeline

1. Ri-brandizzare sales deck e company profile su **D.Factory + modulo Refyn** (recolor
   giallo/nero/bianco, wordmark, riscrittura del posizionamento del brand).
2. **Togliere DCF/financials** dal sales deck; tenerne una versione investor separata.
3. **Rivedere il piano industriale**: esistenti su legacy, ricorrenza dai nuovi; ricalcolare
   ARR, mix e valutazione. (È il pezzo più urgente: Thomas ha già acceso un faro sui numeri.)
4. **Sito nuovo D.Factory** (look non-template, no "cloud design"); dashboard aggiornate
   (bassa priorità). Accessi forniti da Pablo.
5. **Lead generation ad agosto**: questionari, campagne, contatti; test prezzi sui prospect
   reali; metodologia di gestione lead condivisa col cliente.
6. **Follow-up cliente: 31/08/2026.**

---

## 12. Lezioni & principi da tenere presenti

- **Calibrare l'ambizione di rebrand sulla maturità dell'entità.** Il rebrand aziendale
  completo era troppo per D.Factory; la soluzione "modulo" è emersa dal cliente stesso ed è
  quella giusta. Il concetto forte ("perché ora / 5.0", il naming "raffinare il dato") va
  preservato.
- **Consegnare versioni concrete come base di confronto, mai come decisioni prese.** La
  cornice "prima versione, decidiamo insieme" ha reso digeribile anche il rifiuto del
  rebrand. Mantenerla.
- **Distinguere sempre sales da investor.** Il ROI/payback è vendita e resta; DCF,
  valutazione e proiezioni sono investor e ora restano fuori dai materiali cliente.
- **I prezzi sono ipotesi finché non testati.** Nessuna sicurezza numerica sul pricing
  prima della validazione di mercato.
