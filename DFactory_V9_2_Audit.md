# D.Factory · Audit V9.1 → V9.2

**Fase 1 del §24.** Nessun HTML è stato modificato per produrre questo documento.

Base: `DFactory_SalesDeck_v9_1_working/client.html` (19 / 17 canvas) e
`DFactory_DossierTecnico_v9_1_working/client.html` (18 / 18 canvas).
Specifica: `DFactory_Master_Completion_V9_2_90percent.md`.

---

## 1. Sintesi

| | Sales Deck | Dossier |
|---|---|---|
| canvas V9.1 working / client | 19 / 17 | 18 / 18 |
| canvas V9.2 working / client | 19 / **16** | 18 / 18 |
| canvas riscritti nella sostanza | 4 | 5 |
| canvas con delta di copy | 9 | 6 |
| canvas invariati | 6 | 7 |
| difetti V9.1 trovati in questo audit | 3 | 0 |

Il deck perde una slide nella client edition: **A5 assunzioni**, che il §12 ammette
«soltanto se il business case è pubblicato». Con G3 aperto il business case non è
pubblicato, quindi A5 esce dalla client edition e resta nella working.

Livello raggiungibile alla fine della V9.2, dichiarato in anticipo perché dipende
dai gate e non dal lavoro: **90% ready**. Non *commercial final* (G1 e G2 aperti),
non *IT-ready* (G4 aperto). Il §25 vieta di dichiarare «finale» la client edition
in questa condizione, e non verrà dichiarata.

---

## 2. Elementi preservati

Il §3.1 congela il design. Non viene toccato nulla di quanto segue.

### 2.1 Sistema visuale

| elemento | valore V9.1 | stato V9.2 |
|---|---|---|
| canvas | 1280 × 720 | invariato |
| famiglie | Geist, Geist Mono, incorporate base64 | invariato |
| palette | `--ink #0A0A0A` · `--paper #FFFFFF` · `--acid` giallo funzionale | invariato |
| alternanza | `.dk` / `.lt` come da sequenza V9.1 | invariata |
| uso del giallo | solo su evento, perdita, priorità | invariato |
| scala tipografica deck | h1 52 · h2 52/44 · sup 19 · cp 18 · note 13 · lbl 14 | invariata salvo §4.1 |
| scala tipografica dossier | tt 40/34 · corpo 14 · note 13 · UI 12 | invariata |
| rail di navigazione dossier | quattro sezioni, sempre presente | invariato |
| quattro template dossier | A apertura · B prodotto · C tecnico · D annesso | invariati |
| grammatica delle linee | connettore / confine / separatore | invariata |
| ricostruzioni UI | SVG inline, mai immagini raster | invariata |
| autonomia del file | zero richieste di rete | invariata |

### 2.2 Struttura narrativa

Deck: tensione → categoria → prodotto in azione → produzione ed energia →
priorità → ampiezza → offerta → scelta → perché → valore → pilot → CTA.
La sequenza V9.1 è già quella del §10 e non cambia.

Dossier: quattro sezioni, 14 pagine core, 4 annessi. Il §13 descrive esattamente
la struttura V9.1. Nessuna pagina viene aggiunta, spostata o rimossa.

### 2.3 Meccanica delle edizioni

`data-ed="working"` / `data-ed="client"` / `data-ph-page="<gate>"`, strip fisico
in `edition.py`. Il §8.1 chiede di riusare i token V9.1: **nessun placeholder viene
rinominato**. I 221 record del registro V9.1 sono la base del registro V9.2.

---

## 3. Difetti della V9.1 trovati in questo audit

Tre. Vanno corretti nella V9.2 e sono registrati qui perché sono difetti di una
consegna già fatta, non richieste del master.

### 3.1 Il business case annualizzato compare nella client edition · **grave**

`v11_valore`, elemento `<desc>` della figura, client edition V9.1:

> «Novantasei minuti a settimana per settanta euro al minuto per quarantasei
> settimane fanno **trecentonovemilacentoventi** euro. Da lì le due leve:
> **centocinquantaquattromilacinquecentosessanta** euro di capacità se la causa si
> dimezza, **ottocentodieci** euro di energia evitabile.»

Sono 309.120 €, 154.560 € e 810 €: i tre valori che il §21.2 impone di rimuovere
finché il dataset non è validato, e che la condizione di build n. 3 dichiara
bloccanti. Il controllo `accept.py` cercava le stringhe `309.120`, `154.560`,
`810 €` e non le trovava perché nel testo alternativo i numeri sono **scritti in
lettere**. Il controllo ha dato esito positivo su un documento non conforme.

Effetto V9.2: il controllo cerca anche le forme testuali, e la `<desc>` della slide
11 viene sdoppiata come il resto della slide — versione working con i numeri,
versione client con la sola formula.

### 3.2 A5 dichiara un calendario incompatibile con i propri numeri

Appendice A5, riga «Durata del turno · 480 min», colonna origine: **«tre turni al
giorno»**. Il resto del deck usa uno scenario a **un turno al giorno, 5 giorni,
46 settimane = 230 turni**: è da lì che nasce l'energia evitabile di 810 €
(16 kWh × 230 × 0,22 €/kWh). Con tre turni al giorno lo stesso conto darebbe
2.429 €. L'origine dichiarata contraddice la cifra.

Effetto V9.2: origine corretta in «un turno al giorno · 230 turni all'anno», e
riga esplicita per i turni all'anno.

### 3.3 A1 usa un valore fuori dalla scala ammessa

La matrice funzionale contiene il valore **«Base»**, che non è fra i cinque valori
ammessi dal §12 (incluso, configurabile, avanzato, previsto, non incluso).
Effetto V9.2: sostituito.

---

## 4. Modifiche · Sales Deck

Legenda del tipo di intervento: **C** copy · **S** struttura del canvas ·
**V** contenuto del visual · **G** comportamento di gate · **—** invariato.

| # | canvas | tipo | che cosa cambia |
|--:|---|:--:|---|
| S01 | `v01_cover` | C | sottotitolo da 19 px a 21 px (§10 S01 «aumentare leggermente il sottotitolo»); nessun'altra modifica |
| S02 | `v02_tensione` | — | headline, visual e copy inferiore già conformi |
| S03 | `v03_categoria` | — | headline, sottotitolo, tre passaggi e «Azione proposta» già conformi. Nota Refyn: vedi conflitto §7.1 |
| S04 | `v04_evento_prodotto` | C | headline → «Il fermo si vede. / Causa e costo devono essere leggibili nello stesso momento.» (caduta degli articoli) |
| S05 | `v05_energia` | C | sottotitolo → «La linea si ferma. L'energia continua a scorrere.»; nota → «Il dato energetico completa la lettura e quantifica il consumo improduttivo dello stesso evento.», in corpo piccolo ma leggibile |
| S06 | `v06_priorita` | C | intestazione di colonna «Costo» → «Costo stimato» (§7.2: mai un costo presentato come certo) |
| S07 | `v07_ampiezza` | V | i contenuti obbligatori del §10 S07 sono dieci; ne mancano quattro. Aggiungere **produzione**, **utility**, **cause** e **scarti** alle quattro bande, restando a microcopy minimo |
| S08 | `v08_offerta` | C | base comune → «Produzione · OEE · energia · utility · storico»; stato Refyn → «Refyn · modulo avanzato in sviluppo», unica occorrenza del deck |
| S09 | `v09_scelta` | C | Insight *come si attiva* → «Sul medesimo impianto, con capacità analitiche aggiuntive»; Refyn → «Progetto pilota dedicato con perimetro concordato»; Refyn *cosa ottieni* → «Priorità, responsabili, target e verifica» |
| S10 | `v10_perche` | G | tre callout invariati. Prova aziendale: con G5 aperto non entra alcun numero; il fallback MAPST/MarEnergy **non** viene usato (conflitto §7.2). Working edition: tre etichette leggibili al posto dei token |
| S11 | `v11_valore` | S | `<desc>` sdoppiata working/client (difetto §3.1); nota metodologica del §21.3 al posto della riga di piede attuale |
| S12 | `v12_pilot` | C | aggiunta del fallback §10 S12: «La proposta economica viene costruita sul perimetro validato», visibile in client con G2 aperto |
| S13 | `v13_cta` | C | headline → **«Partiamo dalla prima linea da capire.»**; copy → «Condividiamo il perimetro, verifichiamo i dati disponibili e definiamo il passo successivo.»; blocco *Cosa preparare* → «Schema linea · elenco PLC · contatori · dati di produzione · vincoli IT» |
| S14 | `v14_caso` | — | invariata, resta governata da `CASE_STUDY_READY` |
| A1 | `a1_matrice` | C | «Base» → valore ammesso (§3.3) |
| A2 | `a2_servizi` | S | colonne → **Servizio · Output · Quando · Incluso/opzionale**. Cade la colonna «Obiettivo», entra la colonna del §12. Compilata al 10% finale: working etichetta leggibile, client «in proposta» |
| A3 | `a3_pricing` | — | invariata, resta condizionata a G2 |
| A4 | `a4_faq` | — | le sei domande sono già quelle del §12 |
| A5 | `a5_assunzioni` | G + C | **diventa condizionale a G3**: fuori dalla client edition finché il business case non è pubblicato. Origine del turno corretta (§3.2) |

### 4.1 Unica eccezione al congelamento tipografico

Il §3.1 vieta di cambiare il sistema, il §10 S01 chiede esplicitamente di
aumentare il sottotitolo di cover. Si applica solo lì: `.sup` resta a 19 px per
tutto il deck, la cover usa 21 px inline. Nessun'altra dimensione cambia.

---

## 5. Modifiche · Dossier

| # | canvas | tipo | che cosa cambia |
|--:|---|:--:|---|
| P01 | `p01_cover` | — | titolo «preliminare» corretto con G4 aperto; destinatari, indice, annessi già conformi |
| P02 | `p02_overview` | S + C | «Cosa non presuppone» passa da una frase a **tre voci**: sostituzione delle macchine, rifacimento completo dei PLC, cloud obbligatorio. Nota → «Perimetro e requisiti vengono definiti nel solution design». **132 parole → sotto 130** |
| P03 | `p03_livelli` | — | conforme; lo stato Refyn resta senza «in sviluppo» perché l'unica occorrenza del dossier è a P06 |
| P04 | `p04_connect` | — | tre insight, uso e decisione già conformi |
| P05 | `p05_insight` | — | conforme |
| P06 | `p06_refyn` | — | ciclo, contenuti e unica occorrenza di «modulo avanzato in sviluppo» |
| P07 | `p07_sorgenti` | — | tabella, classificazione e nota già conformi |
| P08 | `p08_architettura` | S + C | blocco «Definito dal prodotto» riallineato al §15 (flusso, applicazione, output, logica); blocco solution design → ambiente, rete, autenticazione, **backup**, **supporto remoto**. **132 parole → sotto 130** |
| P09 | `p09_contesto` | C | riga di decisione → «Il dato diventa leggibile soltanto quando condivide tempo e contesto», con la validazione della causa mantenuta accanto |
| P10 | `p10_oee` | C | headline → «L'OEE dice quanto. Le perdite dicono dove.»; nota che dichiara **perimetro, calendario, ideal cycle e good count** (§15 P10) |
| P11 | `p11_energia` | — | conforme; 130 parole, al limite ma dentro |
| P12 | `p12_output` | S | riga **API** aggiunta alla tabella: 5 → 6 righe, tetto del §14.4 |
| P13 | `p13_pilot` | — | conforme e allineato al deck |
| P14 | `p14_servizi` | — | conforme; unica citazione consentita di MAPST 4.0 e MarEnergy nel dossier |
| A1 | `pa1_compatibilita` | S | tabella riformulata su **Elemento · Cosa si verifica · Esito · Owner**, con esiti *supportato / condizionato / da verificare / da aggiungere*, sugli otto campi del §16 |
| A2 | `pa2_sizing` | S + G | si aggiunge la **tabella delle tre fasce** (piccola, media, grande) con le sette colonne del §16, visibile **solo in working**. La client preliminare continua a mostrare il metodo, non i valori |
| A3 | `pa3_governo` | S | colonna 2 → «Modello»; i **dodici ambiti** del §16 condensati in **otto righe**; stato «Annesso per la raccolta dei requisiti» con G4 aperto. **134 parole → sotto 130** |
| A4 | `pa4_kpi` | S | colonne **versione** e **data approvazione** aggiunte alle sei attuali; sei righe, tetto del §16 a otto |

### 5.1 Le tre pagine sopra le 130 parole

Misurate sulla client edition V9.1 con il conteggio per popolazione (esclusi UI,
metadati e scaffolding):

| pagina | parole V9.1 | tetto | intervento |
|---|--:|--:|---|
| `p02_overview` | 132 | 130 | la tripartizione di «cosa non presuppone» sostituisce la frase lunga: si guadagna spazio, non se ne consuma |
| `p08_architettura` | 132 | 130 | i due blocchi passano da frasi a voci brevi |
| `pa3_governo` | 134 | 130 | la condensazione da 12 ambiti a 8 righe accorpa anche il testo |
| `p11_energia` | 130 | 130 | nessun intervento: è al limite, non oltre |

### 5.2 Mappa dei dodici ambiti dell'annesso A3 sulle otto righe

| # | riga A3 V9.2 | ambiti §16 coperti |
|--:|---|---|
| 1 | Autenticazione e identità | autenticazione · password/SSO |
| 2 | Ruoli e permessi | ruoli |
| 3 | Registro degli accessi | audit log |
| 4 | Cifratura | cifratura |
| 5 | Backup, ripristino e conservazione | backup · retention |
| 6 | Aggiornamenti e supporto remoto | patching · remoto |
| 7 | Proprietà del dato e licenza | proprietà dati · licenza |
| 8 | Fine contratto | fine contratto |

Dodici ambiti, otto righe, nessun ambito perso.

---

## 6. Gate

Stato invariato rispetto alla V9.1. Nessun gate è stato approvato fra le due
versioni, e questo determina metà delle scelte della V9.2.

| gate | nome | scope | stato | effetto sulla V9.2 |
|---|---|---|---|---|
| G1 | identità e contatto | GLOBAL | **OPEN** | la CTA resta senza referente; la client edition si presenta dal vivo ma non si invia da sola. Vietato dichiararla «finale» |
| G2 | modello commerciale | SECTION | **OPEN** | A3 pricing fuori dalla client edition; S12 usa il fallback «la proposta economica viene costruita sul perimetro validato»; colonna incluso/opzionale di A2 non compilata |
| G3 | dataset | SECTION | **OPEN** | nessun valore annualizzato in client, **nemmeno scritto in lettere** (§3.1); A5 fuori dalla client edition |
| G4 | IT/OT | SECTION | **OPEN** | il dossier resta «Dossier tecnico preliminare per assessment e solution design»; A2 mostra il metodo, non i valori; A3 è «annesso per la raccolta dei requisiti» |
| G5 | evidenze | NONE | **OPEN** | nessuna prova aziendale numerica in S10; nessun asset reale in nessun canvas |
| CASE | caso cliente | PAGE | **NO** | `v14_caso` fuori dalla client edition |

### 6.1 Che cosa cambierebbe l'approvazione di ciascun gate

| se si approva | il documento guadagna | senza toccare il design |
|---|---|---|
| G1 | referente, ruolo, email in S13 e in P01; la client edition diventa inviabile | sì |
| G2 | A3 pricing rientra in client; A2 si compila; S12 mostra le voci con importo | sì |
| G3 | S11 mostra 309.120 / 154.560 / 810 €; A5 rientra in client; S13 mostra il costo annuo | sì |
| G4 | il dossier perde «preliminare»; A2 mostra i valori; A3 diventa specifica concordata | sì |
| G5 | S10 ospita fino a due elementi di prova; gli asset reali sostituiscono le ricostruzioni | sì |

Nessuna approvazione richiede una nuova pagina o un nuovo template. È la
condizione che il §26 chiede: al 10% finale non deve restare né redesign né
riscrittura.

---

## 7. Conflitti registrati

Il §4 impone di registrare i conflitti fra fonti e di non sceglierli in silenzio.
Ce ne sono due, entrambi interni al master.

### 7.1 La nota Refyn di S03 contro il conteggio delle occorrenze

- Il **§10 S03** chiede, sotto l'azione proposta, la nota: «Esempio del flusso
  Refyn · modulo in sviluppo».
- Il **§5.2** e il **§22.2** impongono che «modulo avanzato in sviluppo» compaia
  **una sola volta** nel Sales Deck, e il **§10 S08** assegna quella occorrenza
  alla slide 08.
- La condizione di build n. 8 del §25 fa fallire il build se «in sviluppo»
  compare più di una volta per documento.

**Risoluzione adottata:** vince il §25, che è una condizione di build esplicita.
La nota di S03 resta **«esempio del flusso Refyn»**, senza «in sviluppo».
La dichiarazione di stato vive solo in S08. Il lettore di S03 sa comunque di
guardare un esempio, e a due slide di distanza legge lo stato del modulo.

### 7.2 Il fallback di prova aziendale contro il divieto su MAPST e MarEnergy

- Il **§10 S10** e il **§18.2** propongono, in assenza di numeri approvati, il
  fallback: «Esperienza maturata attraverso MAPST 4.0 e MarEnergy».
- Il **§5.4** vieta MAPST 4.0 e MarEnergy **nel corpo principale del Sales Deck**.
- Entrambi i paragrafi che propongono il fallback lo condizionano a
  «solo se approvato come claim». G5 è aperto: non è approvato.

**Risoluzione adottata:** il fallback **non viene usato**. Le due condizioni non
si contraddicono nemmeno davvero — la seconda non si verifica mai finché G5 è
aperto. S10 chiude con i tre callout, che sono affermazioni sul prodotto e non
sull'azienda, e la working edition tiene visibili i tre input aperti. Se G5 venisse
approvato con quel claim, resterebbe comunque da sciogliere il §5.4: la sede
naturale della frase è il **dossier P14**, dove la citazione è già ammessa e già
presente.

---

## 8. Asset

Registro V9.1: **zero righe**. Nessun file reale è mai stato consegnato.

| obiettivo §19.2 | richiesto | disponibile | esito |
|---|--:|--:|---|
| asset reali nel Sales Deck | ≥ 1 | 0 | **non raggiunto** |
| asset reali nel Dossier | ≥ 2 | 0 | **non raggiunto** |

I quattro candidati del §19.1 restano tutti scoperti:

| # | asset | token | etichetta obbligatoria | stato |
|--:|---|---|---|---|
| 1 | screenshot MAPST 4.0 | `PH_REAL_SCREENSHOT_MAPST` | *Interfaccia MAPST 4.0 · prodotto legacy* | mancante |
| 2 | screenshot MarEnergy | `PH_REAL_SCREENSHOT_MARENERGY` | *Interfaccia MarEnergy · prodotto legacy* | mancante |
| 3 | report reale | `PH_REAL_REPORT_EXPORT` | *Report reale anonimizzato* | mancante |
| 4 | schema o foto di linea | `PH_REAL_LINE_DIAGRAM` | *Schema di linea anonimizzato* | mancante |

Conseguenza sulla V9.2: **tutte** le viste di prodotto restano ricostruzioni
inline dichiarate pagina per pagina. Il §8.4 lo ammette esplicitamente
(«Asset reali mancanti → mantenere ricostruzioni dichiarate») e il §19.2 resta
un obiettivo non raggiunto, dichiarato come tale, non aggirato.

`assets_v9_2/` viene creata con il registro a dieci colonne e zero righe, e la
condizione di build n. 5 continua a far fallire il build se un file compare in un
canvas senza essere registrato. Il file `Logo-D-Factory-cce0b268-1.webp` presente
nel repository **non** entra nei documenti: non ha riga di registro, non ha
autorizzazione documentata, e il wordmark è già composto tipograficamente.

---

## 9. Pagine condizionali

| canvas | documento | condizione | working | client oggi |
|---|---|---|---|---|
| `v14_caso` | deck | `CASE_STUDY_READY = APPROVED` | visibile, tutta segnaposto | **esclusa** |
| `a3_pricing` | deck | `G2 = APPROVED` | visibile, importi segnaposto | **esclusa** |
| `a5_assunzioni` | deck | `G3 = APPROVED` *(nuovo in V9.2)* | visibile | **esclusa** |
| blocco «due leve» di `v11_valore` | deck | `G3 = APPROVED` | numeri visibili | formula senza risultato |
| `<desc>` di `v11_valore` | deck | `G3 = APPROVED` *(nuovo in V9.2)* | narrazione con i valori | narrazione con la sola formula |
| costo annuo in `v13_cta` | deck | `G3 = APPROVED` | visibile | nascosto |
| tabella tre fasce di `pa2_sizing` | dossier | `G4 = APPROVED` *(nuovo in V9.2)* | visibile con segnaposto | metodo, non valori |
| «preliminare» nel titolo di `p01_cover` | dossier | `G4 = APPROVED` | — | presente finché G4 è aperto |

Risultato sui conteggi:

- **deck working 19** → 13 core + `v14_caso` + A1 A2 A3 A4 A5
- **deck client 16** → 13 core + A1 A2 A4
- **dossier working 18** e **dossier client 18** → 14 core + 4 annessi, invariati

Il §9 fissa il massimo a 13 + 4, o 14 + 4 col caso cliente. La client edition ne
consegna 16: sotto il massimo, perché due appendici sono chiuse dai gate.

---

## 10. Working edition · l'etichetta al posto del token

Il §8.3 è il cambiamento più esteso della V9.2, e non è visibile nella client
edition. Oggi ogni campo aperto si presenta così:

```html
<span data-ed="working" class="ph">{{PH_CONTACT_NAME}}</span>
```

Il token è il testo principale. La V9.2 chiede il contrario: etichetta leggibile
in chiaro, token nell'attributo.

```html
<span data-ed="working" class="ph" data-placeholder="PH_CONTACT_NAME">INPUT APERTO</span>
```

Le quattro etichette ammesse e il criterio di assegnazione:

| etichetta | quando | esempi di token |
|---|---|---|
| `INPUT APERTO` | manca un'informazione che qualcuno in azienda già possiede | `PH_CONTACT_NAME`, `PH_COMPANY_LEGAL_NAME`, `PH_VERSION_DATE` |
| `DECISIONE COMMERCIALE` | serve una decisione, non un'informazione | `PH_AUDIT_PRICE`, `PH_CONNECT_ANNUAL_FEE`, `PH_CONTRACT_TERM`, `PH_SERVICES_INCLUDED` |
| `VALIDAZIONE TECNICA` | serve una verifica su un impianto o un ambiente | `PH_SUPPORTED_PROTOCOLS`, `PH_MIN_CPU`, `PH_READ_ONLY_POLICY`, `PH_DEPLOYMENT_MODEL` |
| `ASSET RICHIESTO` | serve un file, con autorizzazione | `PH_REAL_SCREENSHOT_MAPST`, `PH_REAL_REPORT_EXPORT` |

L'assegnazione è meccanica, non discrezionale, e ha la precedenza sul gate:
**G1** → input aperto (identità, referente e definizione dell'audit sono
informazioni da recuperare, anche quando l'owner è Commerciale) · **G2** →
decisione commerciale · **G3** e **G4** → validazione tecnica · **G5** e ogni
token `PH_REAL_*` → asset richiesto. Per i campi fuori dai gate decide la colonna
**owner**: Commerciale → decisione commerciale, Tecnico o Tecnico + IT →
validazione tecnica, tutto il resto → input aperto. La regola vive in
`labels92.py`, così registro e documenti non possono divergere.

Il pannello riassuntivo in coda a ogni canvas working («INPUT APERTI …») continua a
elencare i **token**: lì servono per parlare col registro, non col lettore.

---

## 11. Che cosa la V9.2 non farà

Elencato perché il §26 chiede che al 10% finale non resti nulla di strutturale, e
perché ognuno di questi è stato considerato e scartato.

- **Nessun nuovo template**, nessuna nuova pagina, nessuna nuova sezione.
- **Nessuna roadmap, maturity matrix, griglia consulenziale** (§3.2).
- **Nessun nuovo servizio e nessuna nuova funzione Refyn** oltre ai nove servizi
  del §12 e ai contenuti del §15 P06.
- **Nessun caso cliente costruito** dallo scenario illustrativo (§20.4).
- **Nessun numero aziendale** finché G5 è aperto (§18.3).
- **Nessuna pubblicazione della formulazione sulla proprietà dei dati**: il §25
  la vieta senza approvazione legale. Resta in
  `DFactory_Decisioni_Tecniche_v9_1.md`; l'annesso A3 continua a dichiarare che
  cosa si decide e chi decide, che è vero oggi.
- **Nessun asset non registrato**, incluso il logo presente nel repository.
- **Nessuna dichiarazione di «finale»** sulla client edition finché G1 e G2 sono
  aperti (§25).

---

## 12. Condizioni di build della V9.2

Il §25 ne elenca dieci. Sei esistono dalla V9.1, quattro sono nuove.

| # | condizione | stato del controllo |
|--:|---|---|
| 1 | placeholder residuo nella client edition | esiste dalla V9 |
| 2 | CTA mancante | esiste dalla V9.1 |
| 3 | business case annualizzato con G3 aperto | esiste, **da estendere alle forme scritte in lettere** (§3.1) |
| 4 | «Dossier tecnico» senza «preliminare» con G4 aperto | esiste dalla V9.1 |
| 5 | asset non registrato | esiste dalla V9.1 |
| 6 | claim fuori dal Claim Register | esiste dalla V9.1 |
| 7 | **elementi SVG fuori dal viewBox** | il controllo `getBBox()` esiste in `qa.py` dalla V9.1; **da promuovere a condizione di build** |
| 8 | **«in sviluppo» più di una volta per documento** | **nuovo** |
| 9 | **nota client che contiene testo interno** | **nuovo** |
| 10 | **canvas con clipping o overflow** | rilevato da `qa.py`; **da promuovere a condizione di build** |

Le condizioni 7 e 10 nascono da un difetto reale della V9: il blocco contatto
della CTA era tagliato dal viewBox del proprio SVG e nessun controllo se n'era
accorto, perché il clipping interno a un SVG non è un overflow del DOM. Il
controllo è stato scritto allora; adesso diventa bloccante.

---

## 13. Ordine di lavoro

| fase | §24 | oggetto | esito atteso |
|--:|---|---|---|
| 1 | Audit | questo documento | ✔ prodotto, nessun HTML toccato |
| 2 | ContentMap | `DFactory_ContentMap_v9_2.md` | obiettivo, visual, copy, fonte, claim, gate e fallback per 37 canvas |
| 3 | Working | delta §4 e §5 sul master, etichette §8.3 | 19 + 18 canvas |
| 4 | Client | fallback §8.4, strip dei token e delle pagine condizionali | 16 + 18 canvas, zero token |
| 5 | QA | i quattro blocchi del §22 e le dieci condizioni del §25 | build che fallisce se una condizione cade |
| 6 | Consegna | i 18 output del §1 | senza sovrascrivere V9 o V9.1 |

---

*Fase 1 chiusa. Nessun file HTML è stato modificato.*
