# D.Factory · ChangeLog V9.2

Da V9.1 a V9.2. Il design è congelato: nessuna palette, nessun font, nessuna
dimensione di canvas, nessun template, nessuna navigazione è stata toccata.
Sono cambiati copy, un contenuto di visual, tre difetti e due geometrie.

**Nessun file V9 o V9.1 è stato sovrascritto.**

---

## 1. Conteggi

| | V9.1 | V9.2 |
|---|---|---|
| Sales Deck working | 19 canvas | 19 canvas |
| Sales Deck client | 17 canvas | **16 canvas** |
| Dossier working | 18 canvas | 18 canvas |
| Dossier client | 18 canvas | 18 canvas |
| placeholder nel registro | 221 | 221 · *nessuno rinominato* |
| token visibili in client | 0 | 0 |
| canvas con flag di QA | 0/72 | **0/71** |
| condizioni di build | 6 | **10** |

Il deck client perde una slide: **A5 assunzioni**. Il §12 la ammette «soltanto
se il business case è pubblicato», e con G3 aperto non lo è. Resta nella working
edition, dove serve.

Client edition del deck: 13 slide core + A1 matrice + A2 servizi + A4 FAQ,
rinumerata A3. Escluse `v14_caso` (CASE), `a3_pricing` (G2), `a5_assunzioni` (G3).

---

## 2. Tre difetti della V9.1, corretti

Trovati durante l'audit della Fase 1, non richiesti dal master. Vale la pena
distinguerli dalle modifiche: sono errori di una consegna già fatta.

### 2.1 Il business case annualizzato usciva nella client edition · grave

`v11_valore`, elemento `<desc>` della figura. Il testo alternativo raccontava:

> «…quarantasei settimane fanno **trecentonovemilacentoventi** euro. Da lì le due
> leve: **centocinquantaquattromilacinquecentosessanta** euro di capacità…
> **ottocentodieci** euro di energia evitabile.»

Sono 309.120 €, 154.560 € e 810 €, cioè i tre valori che il §21.2 impone di
rimuovere finché il dataset non è validato. Il controllo cercava le stringhe
`309.120`, `154.560`, `810 €` e non le trovava, perché nel testo accessibile i
numeri sono **scritti in lettere**. Ha dato esito positivo su un documento non
conforme.

**Correzione:** la `<desc>` diventa client-safe e racconta la formula, non i
valori; una seconda `<desc id="x3w" data-ed="working">` porta i numeri nella sola
working edition, con `aria-labelledby` che elenca entrambi gli id. La condizione
di build n. 3 cerca adesso anche `trecentonovemila`, `centocinquantaquattromila`
e `ottocentodieci`.

### 2.2 L'appendice A5 dichiarava un calendario incompatibile con i propri numeri

Riga «Durata del turno · 480 min», colonna origine: **«tre turni al giorno»**.
Tutto il resto del deck usa uno scenario a un turno al giorno, 5 giorni,
46 settimane = 230 turni all'anno — ed è da lì che nascono gli 810 € di energia
evitabile (16 kWh × 230 × 0,22 €/kWh). Con tre turni al giorno lo stesso conto
darebbe 2.429 €.

**Correzione:** origine → «un turno al giorno», più una riga nuova
«Turni all'anno · 230 · 46 settimane × 5 giorni». L'appendice passa da nove
parametri a dieci.

### 2.3 La matrice funzionale usava un valore fuori dalla scala ammessa

Il valore **«Base»**, che non è fra i cinque del §12.

**Correzione:** la riga mescolava due capacità diverse — assegnare una causa,
che Connect fa, e analizzare le cause, che è di Insight. Si separano:
riga 1 → «Stato di linea, con causa associata» (incluso in tutti e tre),
riga 4 → «Analisi delle cause, micro-fermate e velocità» (non incluso in
Connect). Solo valori ammessi.

---

## 3. Due geometrie sbagliate, e il controllo che non le vedeva

`v05_energia` aveva `width="1280" height="440" viewBox="0 0 1280 480"`. Con
`preserveAspectRatio` al default la scala è la **minore** dei due rapporti, non
quella orizzontale: 0,917. Effetto reale — testo a 12,5 px renderizzato a
11,5 px, e il grafico rientrato di 53 px per lato rispetto al margine di tutte
le altre slide.

`a1_matrice` aveva `height="440"` su `viewBox` alto 408: contenuto centrato
verticalmente per caso, con 16 px di scarto.

`qa.py` non le vedeva perché calcolava la scala sulle sole larghezze.

**Correzioni:** `v05_energia` → `height="480"`, `top:156px`.
`a1_matrice` → `height="408"`, `top:136px`. E in `qa.py`:

```js
fs = fs * Math.min(r.width / vb.width, r.height / vb.height);
```

---

## 4. Sales Deck · modifiche per canvas

| canvas | modifica |
|---|---|
| `v01_cover` | sottotitolo 19 → **21 px** (§10 S01). Unica eccezione al congelamento tipografico, e vale solo per la cover |
| `v04_evento_prodotto` | headline → «Il fermo si vede. **Causa e costo** devono essere leggibili nello stesso momento.» |
| `v05_energia` | sottotitolo → «La linea si ferma. L'energia continua a scorrere.» · nota → «Il dato energetico completa la lettura e quantifica il consumo improduttivo dello stesso evento.» · geometria corretta |
| `v06_priorita` | colonna «Costo» → **«Costo stimato»** (§7.2: un costo stimato non si presenta come certo) |
| `v07_ampiezza` | **quattro contenuti obbligatori mancanti aggiunti**: produzione (227.000 pz), utility, cause (prima causa della banda macchina), scarti (4,4%). La barra della banda turno lascia il posto a tre cifre con il proprio calcolo |
| `v08_offerta` | base comune → «Produzione · OEE · energia · utility · storico» · stato Refyn → «modulo avanzato in sviluppo», sotto il nome, **unica occorrenza del deck** |
| `v09_scelta` | Insight → «Sul medesimo impianto, con capacità analitiche aggiuntive» · Refyn → «Progetto pilota dedicato con perimetro concordato» · «Priorità, **responsabili**, target e verifica» · «costo e priorità» |
| `v11_valore` | `<desc>` sdoppiata (§2.1) · nota metodologica del §21.3 dentro il canvas · rail → «Scenario illustrativo · non risultato cliente» |
| `v12_pilot` | fallback del §10 S12 in client: «La proposta economica viene costruita sul perimetro validato» · working: «Importi nell'appendice pricing» |
| `v13_cta` | headline → **«Partiamo dalla prima linea da capire.»** · copy → «Condividiamo il perimetro, verifichiamo i dati disponibili e definiamo il passo successivo.» · *cosa preparare* → «…contatori / Dati di produzione · **vincoli IT**» · blocco contatto su una riga con i nomi dei campi |
| `a1_matrice` | «Base» eliminato (§2.3) · geometria corretta (§3) |
| `a2_servizi` | tabella → **Servizio · Output · Quando · Incluso o opzionale**. Cade «Obiettivo»: quattro colonne sono quelle del §12, cinque non stanno |
| `a5_assunzioni` | **condizionata a G3** · origine del turno corretta (§2.2) · riga «Turni all'anno · 230» |

Invariati: `v02_tensione`, `v03_categoria`, `v10_perche`, `v14_caso`,
`a3_pricing`, `a4_faq`.

---

## 5. Dossier · modifiche per canvas

| canvas | modifica |
|---|---|
| `p01_cover` | blocco di emissione: quattro token in fila → nome del campo + etichetta |
| `p02_overview` | «Che cosa non **presuppone**» in tre voci — sostituzione delle macchine, rifacimento completo dei PLC, cloud obbligatorio · nota del §15 · l'elenco del solution design se ne va: è per intero su P08 · **132 → 105 parole** |
| `p08_architettura` | «Definito dal prodotto» → flusso, applicazione, output, logica di calcolo · «Da chiudere nel solution design» → ambiente, rete, autenticazione, **backup**, **supporto remoto** · **132 → 121 parole** |
| `p09_contesto` | riga di decisione del §15: «Il dato diventa leggibile soltanto quando condivide tempo e contesto» |
| `p10_oee` | headline → «L'OEE dice quanto. Le perdite dicono dove.» · nota che dichiara **perimetro, calendario, tempo ciclo ideale e conteggio dei pezzi conformi** |
| `p12_output` | riga **API** aggiunta: cinque righe diventano sei, il tetto del §14.4 · «Disponibilità delle API da confermare» |
| `p14_servizi` | la nota di working che elencava cinque token se ne va: gli stessi cinque sono nel pannello in coda alla pagina, che parla al registro |
| `pa1_compatibilita` | tabella → **Elemento · Cosa si verifica · Esito · Owner** sugli otto campi del §16 · esiti ammessi in legenda · passo di riga più stretto |
| `pa2_sizing` | **tabella delle tre fasce** (Fascia · Tag · Linee · Frequenza · Retention · CPU · RAM · Storage) nella sola working edition, più le cinque grandezze · la client preliminare mantiene il diagramma del metodo |
| `pa3_governo` | colonna 2 → **«Modello»** · **dodici ambiti in otto righe** · stato «per la raccolta dei requisiti» · **134 → 125 parole** |
| `pa4_kpi` | colonne **Versione** e **Approvato** aggiunte: sei colonne diventano otto |

Invariati: `p03_livelli`, `p04_connect`, `p05_insight`, `p06_refyn`,
`p07_sorgenti`, `p11_energia`, `p13_pilot`.

### I dodici ambiti dell'annesso A3 in otto righe

| riga | ambiti del §16 coperti |
|---|---|
| Autenticazione e identità | autenticazione · password/SSO |
| Ruoli e permessi | ruoli |
| Registro degli accessi | audit log |
| Cifratura | cifratura |
| Backup e conservazione | backup · retention |
| Aggiornamenti e accesso remoto | patching · remoto |
| Proprietà e licenza | proprietà dati · licenza |
| Fine contratto | fine contratto |

---

## 6. §8.3 · dall'etichetta al posto del token

Il cambiamento più esteso, e invisibile nella client edition.

Prima il token era il testo principale:

```html
<span data-ed="working" class="ph">{{PH_CONTACT_NAME}}</span>
```

Adesso l'etichetta è il testo, il token è un attributo:

```html
<span data-ed="working" class="ph" data-placeholder="PH_CONTACT_NAME">INPUT APERTO</span>
```

**78 sostituzioni** — 49 nel deck, 29 nel dossier. Quale delle quattro etichette
tocchi a un campo non è una scelta editoriale: **decide il gate**, e per i campi
fuori dai gate decide la colonna *owner* del registro. La regola vive in
`labels92.py`.

| gate | etichetta | campi |
|---|---|--:|
| G1 | `INPUT APERTO` | 9 |
| G2 | `DECISIONE COMMERCIALE` | 10 |
| G3 · G4 | `VALIDAZIONE TECNICA` | 30 |
| G5 e `PH_REAL_*` | `ASSET RICHIESTO` | 8 |
| CASE | `INPUT APERTO` | 1 |
| fuori dai gate | dall'owner | 163 |

### Due letture dichiarate

**La slide del caso cliente.** Ventotto celle, tutte segnaposto, tutte con owner
Legale o Direzione: ventotto «INPUT APERTO» identici avrebbero cancellato
l'unica informazione che quella slide porta oggi, cioè **che cosa un caso deve
contenere**. Per quei campi si mostra il nome del campo in chiaro — «periodo di
baseline», «metodo di misura», «limiti dichiarati della misura» — e il token
resta nell'attributo, che è quello che il §8.3 chiede.

**Le celle strette.** Nell'annesso A4 le colonne Versione e Approvato sono larghe
100 e 114 px: «VALIDAZIONE TECNICA» non ci sta, e rimpicciolire il corpo
violerebbe il §22.1. Quelle due celle mostrano «in bozza» e «da approvare», con
`data-placeholder` su `PH_KPI_VERSION` e `PH_KPI_APPROVAL_DATE`.

Il pannello «INPUT APERTI» in coda a ogni canvas della working edition continua
a elencare i **token**: lì servono per parlare col registro, non col lettore.

---

## 7. §25 · quattro condizioni di build nuove

Da sei a dieci.

| # | condizione | stato |
|--:|---|---|
| 7 | elementi SVG fuori dal viewBox | il controllo `getBBox()` esisteva in `qa.py` dalla V9.1 — **adesso è bloccante** |
| 8 | «in sviluppo» più di una volta per documento | nuovo |
| 9 | testo interno in una nota client | nuovo |
| 10 | canvas con clipping o overflow | rilevato da `qa.py` — **adesso è bloccante** |

Le condizioni si misurano sul **testo visibile**: un token dentro un commento
HTML o dentro l'attributo `data-placeholder` non è quello che il lettore legge,
e trattarlo come tale avrebbe reso i controlli 8 e 9 rumore puro.

La 9 ha trovato un caso reale in corso d'opera: il piede dell'annesso A3 diceva
«per la raccolta dei requisiti, **finché G4 è aperto**». Il nome di un gate
interno in un documento destinato al cliente. Rimosso.

---

## 8. Conflitti registrati · §4

Il §4 impone di registrare i conflitti e di non scegliere in silenzio. Tre.

### 8.1 La nota Refyn della slide 03 contro il conteggio delle occorrenze

Il §10 S03 chiede la nota «Esempio del flusso Refyn · **modulo in sviluppo**».
Il §5.2, il §22.2 e la condizione di build n. 8 impongono che «in sviluppo»
compaia una sola volta per documento, e il §10 S08 assegna quella occorrenza
alla slide 08.

**Risoluzione:** vince il §25, che è una condizione di build esplicita. La nota
di S03 resta «esempio del flusso Refyn». Lo stato del modulo vive su S08, due
slide dopo.

### 8.2 Il fallback di prova aziendale contro il divieto su MAPST e MarEnergy

Il §10 S10 e il §18.2 propongono, in assenza di numeri approvati, «Esperienza
maturata attraverso MAPST 4.0 e MarEnergy». Il §5.4 vieta MAPST 4.0 e MarEnergy
nel **corpo principale del Sales Deck**. Entrambi i paragrafi che propongono il
fallback lo condizionano a «solo se approvato come claim»; G5 è aperto.

**Risoluzione:** il fallback non viene usato. La slide 10 chiude con i tre
callout, che sono affermazioni sul prodotto e non sull'azienda. La citazione dei
due prodotti legacy resta dove il §5.4 la ammette: **una volta, nella pagina 14
del dossier.**

### 8.3 Sei righe di tabella contro otto campi negli annessi

Il §14.4 fissa «max 6 righe tabella principale», il §16 chiede otto campi in A1,
otto ambiti in A3 e ammette otto righe in A4.

**Risoluzione:** il tetto di sei vale per le pagine core, che lo rispettano
tutte. Gli annessi seguono il §16, con il passo di riga più stretto per starci.
Un annesso è una tabella per definizione — il §14.2 lo chiama template D — e
comprimerlo a sei righe avrebbe significato perdere ambiti.

---

## 9. Livello raggiunto · dichiarazione richiesta dal §25

| livello | esito |
|---|---|
| **90% ready** | **✔ raggiunto** |
| commercial final | ✗ G1 e G2 aperti |
| IT-ready | ✗ G4 aperto |

**La client edition non è dichiarata «finale».** Il §25 lo vieta con G1 o G2
aperti, e sono aperti entrambi.

Il 10% residuo è nella `DFactory_FinalReviewChecklist_v9_2.md`: quarantadue
caselle, nessuna delle quali è un lavoro di design.

---

## 10. File consegnati

### HTML e PDF

- `DFactory_SalesDeck_v9_2_working.html` · 19 canvas
- `DFactory_SalesDeck_v9_2_client.html` · 16 canvas
- `DFactory_DossierTecnico_v9_2_working.html` · 18 canvas
- `DFactory_DossierTecnico_v9_2_client.html` · 18 canvas
- `DFactory_SalesDeck_v9_2_client.pdf`
- `DFactory_DossierTecnico_v9_2_client.pdf`
- `DFactory_SalesDeck_v9_2_working.pdf` · `DFactory_DossierTecnico_v9_2_working.pdf`

### Documenti

- `DFactory_V9_2_Audit.md` — Fase 1, prodotto senza toccare gli HTML
- `DFactory_ContentMap_v9_2.md` — 37 canvas, sette campi ciascuno
- `DFactory_ClaimRegister_v9_2.md` — dieci claim con stato e fonte
- `DFactory_PlaceholderRegister_v9_2.md` — 221 campi, con etichetta e canvas
- `DFactory_FinalReviewChecklist_v9_2.md` — le quarantadue caselle del 10%
- `DFactory_OpenInputs_v9_2.md` — i cinque gate in ordine di ritorno
- `DFactory_QA_Report_v9_2.md`
- `DFactory_ChangeLog_v9_2.md`
- `assets_v9_2/AssetRegister.md` — dieci colonne, zero righe

### Provini e render

- `DFactory_SalesDeck_v9_2_client_contact.png` + `_small_contact` + `_hierarchy`
- `DFactory_SalesDeck_v9_2_working_contact.png` + varianti
- `DFactory_DossierTecnico_v9_2_client_contact.png` + varianti
- `DFactory_DossierTecnico_v9_2_working_contact.png` + varianti
- `render/v92/deck_client/` · `deck_working/` · `dossier_client/` · `dossier_working/`
  — 71 PNG a 2560×1440

### Catena di build · `work_v92/`

`mk_deck92.py` · `mk_dossier92.py` · `labels92.py` · `edition92.py` ·
`accept92.py` · `assets92.py` · `mk_register92.py` · `qa.py` (corretto) ·
`build.py` · `render.py` · `gates.py` · `ph91.py` · `claims.py` · `semantic9.py`

Per rigenerare tutto dopo l'approvazione di un gate basta cambiare `gates.STATO`
e rilanciare la catena: i documenti si aggiornano da soli, e `accept92.py`
verifica che il risultato sia coerente con il nuovo stato.
