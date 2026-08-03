# D.Factory · ContentMap V9.2

**Fase 2 del §24.** Per ogni canvas: obiettivo, visual, copy, fonte, claim, gate,
fallback. È la specifica che la Fase 3 esegue: quello che non è scritto qui non
entra nei documenti.

- Sales Deck · 13 core + 1 caso opzionale + 5 appendici = **19 canvas working**, **16 client**
- Dossier · 14 core + 4 annessi = **18 canvas**, working e client

Convenzioni delle colonne:

- **fonte** — gerarchia del §4: `master` = §10/§15 del V9.2 · `V9.1` = preservato ·
  `dataset` = scenario illustrativo invariante · `claim` = Claim Register
- **claim** — chiave nel `DFactory_ClaimRegister_v9_2.md`
- **gate** — che cosa il gate toglie o aggiunge a *questo* canvas
- **fallback** — che cosa vede il cliente quando il gate è aperto

Lo scenario illustrativo è invariante dalla V8 e non viene ricalcolato:

```
un turno al giorno · 5 giorni · 46 settimane = 230 turni all'anno
500 pz/min · 0,14 €/pz → 70 €/min · fermo 18 min → 1.260 € · turno 26 min → 1.820 €
7 giorni · 58 eventi · 224 min → 15.680 € · prima causa 43%
96 min/sett × 70 €/min × 46 sett → 309.120 € · metà → 154.560 €
454 min × 95 kW + 26 min × 38 kW → 719 + 16 = 735 kWh · × 0,22 → 162 €
454 min × 500 pz/min → 227.000 pz · 735 ÷ 227.000 × 1.000 → 3,2 kWh · 0,71 € · 1,13 kgCO₂e
94,6% × 79% × 95,6% → OEE 71,4% · 16 kWh × 230 × 0,22 → 810 €
```

---

# Parte I · Sales Deck

## S01 · `v01_cover` · Cover

| | |
|---|---|
| **obiettivo** | in cinque secondi: industria, produzione, energia, valore |
| **visual** | vista di turno ricostruita, dark: tre macchine sul turno, curva oraria dell'energia, a destra margine del turno e costo energetico. Invariata dalla V9.1 |
| **copy** | H1 «Dalla linea al margine, / nello stesso dato.» · sottotitolo «D.Factory unisce produzione, energia e costi in una lettura operativa condivisa.» **a 21 px** (unica eccezione tipografica, §10 S01) · didascalia «vista ricostruita · dati illustrativi» |
| **fonte** | master §6.3 e §10 S01 · visual V9.1 · numeri dataset |
| **claim** | — |
| **gate** | G1 · working mostra `PH_COMPANY_BRAND_FORM` come `INPUT APERTO`; G3 · `PH_DATASET_VALIDATOR`, `PH_DATASET_VALIDATION_DATE` |
| **fallback** | nessun badge, nessun logo cliente, nessun numero aziendale |

## S02 · `v02_tensione` · Tensione

| | |
|---|---|
| **obiettivo** | l'unica slide astratta del deck: il problema non è la mancanza di dati |
| **visual** | quattro flussi separati sopra (PLC e stati, produzione e ordini, contatori e utility, costi e gestionale), gli stessi quattro allineati sotto su un asse comune |
| **copy** | H1 «Ogni impianto produce dati. / Pochi diventano decisioni.» · chiusura «Il problema non è l'assenza di dati. È la mancanza di un contesto comune.» |
| **fonte** | master §6.4 e §10 S02 · visual V9.1 |
| **claim** | — |
| **gate** | nessuno |
| **fallback** | — |

## S03 · `v03_categoria` · Categoria di prodotto

| | |
|---|---|
| **obiettivo** | dire che cosa fa il prodotto: da dati grezzi a informazioni operative |
| **visual** | una sola schermata ricostruita con tre annotazioni numerate: 01 che cosa sta succedendo · 02 perché pesa · 03 dove intervenire |
| **copy** | H1 «D.Factory trasforma i dati grezzi di linea / in informazioni operative.» · sottotitolo «Acquisisce i dati, li contestualizza e li rende utilizzabili da Produzione, Energia e Direzione.» · annotazione 03 «Azione proposta» · nota «esempio del flusso Refyn» |
| **fonte** | master §10 S03 · numeri dataset (OEE 71,4%, 26 min, 6.720 €, 4.340 €, 43%) |
| **claim** | `refyn` — l'azione è dichiarata proposta, non eseguita |
| **gate** | G5 · `PH_REAL_SCREENSHOT_NEW_UI` come `ASSET RICHIESTO` in working |
| **fallback** | la nota **non** riporta «modulo in sviluppo»: conflitto risolto nell'audit §7.1, l'unica occorrenza del deck è su S08 |

## S04 · `v04_evento_prodotto` · Prodotto in azione

| | |
|---|---|
| **obiettivo** | causa e costo leggibili nello stesso istante del fermo |
| **visual** | finestra 10:00–12:00 su tre macchine, fermo tappatrice selezionato, curva OEE sotto, un solo indicatore verticale che attraversa timeline e curva |
| **copy** | H1 «**Il fermo si vede. / Causa e costo devono essere leggibili nello stesso momento.**» · «Fermo 18 minuti» · «Causa associata · Mancanza tappi a monte» · «Margine perso stimato · 1.260 €» · formula «18 min · 500 pz/min · 0,14 €/pz» · nessun paragrafo |
| **fonte** | master §10 S04 (headline nuova) · §7.1 causa associata · §7.2 margine perso stimato |
| **claim** | — |
| **gate** | G5 · `PH_REAL_SCREENSHOT_MAPST` |
| **fallback** | «Vista ricostruita · dati illustrativi» a piede pagina |

## S05 · `v05_energia` · Produzione ed energia

| | |
|---|---|
| **obiettivo** | lo stesso minuto letto su capacità e su consumi |
| **visual** | due curve sulla stessa finestra e sullo stesso indicatore: produzione a 0 pz/min, potenza a 38 kW |
| **copy** | H1 «Lo stesso minuto pesa su capacità e consumi.» · sottotitolo «**La linea si ferma. L'energia continua a scorrere.**» · nota «**Il dato energetico completa la lettura e quantifica il consumo improduttivo dello stesso evento.**» in corpo piccolo ma leggibile |
| **fonte** | master §10 S05 · §7.3 consumo improduttivo |
| **claim** | `costo_en` |
| **gate** | G3 · `PH_DATASET_STOPPED_POWER`; G5 · `PH_REAL_SCREENSHOT_MARENERGY` |
| **fallback** | — |

## S06 · `v06_priorita` · Dall'evento alla priorità

| | |
|---|---|
| **obiettivo** | un fermo è un evento, quattordici sono una priorità |
| **visual** | ranking di quattro cause su sette giorni, ordinate per costo, con barra proporzionale |
| **copy** | H1 «Un fermo è un evento. / Quattordici diventano una priorità.» · colonne «Causa · Eventi · Durata · **Costo stimato**» · totale 15.680 € · «Il 43% del costo viene da una causa sola» · chiusura sulle micro-fermate: 38 eventi che valgono meno della metà |
| **fonte** | master §10 S06 · §7.2 (nessun costo presentato come certo) · dataset |
| **claim** | — |
| **gate** | nessuno: sono i dati della settimana osservata, non annualizzati |
| **fallback** | — |

## S07 · `v07_ampiezza` · Ampiezza

| | |
|---|---|
| **obiettivo** | dalla macchina al pezzo senza cambiare contesto |
| **visual** | quattro bande numerate. **01 Macchina** stato, fermi e cause principali · **02 Linea** OEE e i tre fattori, disponibilità performance qualità · **03 Turno** produzione in pezzi, energia, utility e costo · **04 Pezzo** consumo specifico, costo, CO₂ e scarti |
| **copy** | H1 «Dalla macchina al pezzo, / senza cambiare contesto.» · microcopy minimo, nessuna frase di raccordo. Nuovi elementi rispetto alla V9.1: **produzione 227.000 pz**, **utility**, **cause principali**, **scarti 4,4%** (complemento di qualità 95,6%) |
| **fonte** | master §10 S07 «contenuti obbligatori», dieci voci · dataset |
| **claim** | `oee`, `costo_en`, `co2` |
| **gate** | nessuno |
| **fallback** | «Viste ricostruite · dati illustrativi» |

## S08 · `v08_offerta` · Offerta

| | |
|---|---|
| **obiettivo** | tre livelli su una sola base operativa |
| **visual** | la stessa finestra che acquisisce funzioni salendo di livello: Connect, Insight, Refyn |
| **copy** | H1 «Tre livelli, una sola base operativa.» · Connect «vede e misura» · Insight «spiega e quantifica» · Refyn «guida e verifica» · base comune «**Produzione · OEE · energia · utility · storico**» · «Servizi specialistici attivabili su ogni livello» · stato «**Refyn · modulo avanzato in sviluppo**» |
| **fonte** | master §5.2, §5.3, §10 S08 |
| **claim** | `cumulativa`, `refyn` |
| **gate** | G2 · `PH_SERVICES_INCLUDED`, `PH_SERVICES_OPTIONAL` come `DECISIONE COMMERCIALE` |
| **fallback** | **unica occorrenza di «in sviluppo» nel deck**: condizione di build n. 8 |

## S09 · `v09_scelta` · Scelta del livello

| | |
|---|---|
| **obiettivo** | scegliere il livello dalla decisione da prendere, non dal listino |
| **visual** | tre zone verticali con il segmento cumulativo sotto il nome |
| **copy** | H1 «Scegli il livello / dalla decisione che devi prendere.» · tre righe fisse per livello: *quando serve*, *cosa ottieni*, *come si attiva*. Connect: visibilità affidabile e condivisa / baseline, stato linea, OEE, consumi e storico / «Audit, configurazione e canone ricorrente». Insight: capire dove si perde capacità, energia e valore / cause, correlazioni, costo e priorità / «**Sul medesimo impianto, con capacità analitiche aggiuntive**». Refyn: governare le azioni e verificarne i benefici / «**Priorità, responsabili, target e verifica**» / «**Progetto pilota dedicato con perimetro concordato**» |
| **fonte** | master §10 S09, testo integrale |
| **claim** | `cumulativa`, `refyn` |
| **gate** | G2 · `PH_AUDIT_DURATION`, `PH_CONTRACT_TERM`, `PH_REFYN_PRICING_MODEL` |
| **fallback** | client con G2 aperto: «Prezzi, inclusioni e durata contrattuale arrivano con la proposta economica.» Nessun prezzo su questa slide, mai (§10 S09) |

## S10 · `v10_perche` · Perché D.Factory

| | |
|---|---|
| **obiettivo** | tecnologia industriale, non reporting |
| **visual** | un solo asse orario: cadenza di produzione sopra, potenza assorbita sotto, il salto 95 → 38 kW alle 11:24 |
| **copy** | H1 «Tecnologia industriale, / non solo reporting.» · tre callout: 01 produzione ed energia sullo stesso asse · 02 si parte dall'impianto esistente · 03 software e competenze insieme |
| **fonte** | master §6.5, §6.6, §6.7, §10 S10 |
| **claim** | `brownfield` |
| **gate** | **G5 · determinante.** Working: `PH_GROUP_RELATIONSHIP`, `PH_COMPANY_FOUNDING_YEAR`/`PH_COMPANY_YEARS_EXPERIENCE`, `PH_PROJECTS_COMPLETED` come `INPUT APERTO`. Il §10 ne ammette al massimo due, **se approvati** |
| **fallback** | nessuna prova aziendale in client. Il fallback «esperienza maturata attraverso MAPST 4.0 e MarEnergy» **non viene usato**: audit §7.2, perché il §5.4 lo vieta nel corpo del deck e perché non è approvato come claim |

## S11 · `v11_valore` · Valore

| | |
|---|---|
| **obiettivo** | il valore nasce da due leve, senza pareggiarle |
| **visual** | canvas SVG: la formula in grande, sotto le due leve numerate |
| **copy · client (G3 aperto)** | H1 «Il valore nasce da due leve: / capacità e consumi.» · «minuti di fermo × margine al minuto × settimane produttive» · «Il risultato si calcola sul dato della vostra linea, durante l'audit.» · «Nella settimana osservata la prima causa vale 96 minuti e 6.720 €.» · leve: **Capacità recuperabile** «la leva principale», **Energia evitabile** «la lettura che la completa» · nota §21.3 |
| **copy · working (G3 approvato)** | in più: «96 min × 70 €/min × 46 settimane», **309.120 €**, **154.560 €** se la causa si dimezza, **810 €** dai 16 kWh per turno a linea ferma |
| **fonte** | master §10 S11, §21.2, §21.3 · dataset |
| **claim** | `costo_en` |
| **gate** | **G3 · sostanziale.** Anche la `<desc>` della figura è sdoppiata: la versione client racconta la formula, non i valori annualizzati (correzione del difetto V9.1, audit §3.1) |
| **fallback** | nota metodologica del §21.3: «In questo scenario la leva principale è la capacità recuperabile. Il dato energetico completa la lettura e misura il consumo improduttivo dello stesso evento.» |

## S12 · `v12_pilot` · Pilot

| | |
|---|---|
| **obiettivo** | una linea, una baseline, una decisione di scala |
| **visual** | tre momenti in sequenza (Verifica → Pilot → Decisione di scala) con quello che ciascuno produce; sotto, le tre voci della struttura economica |
| **copy** | H1 «Una linea. Una baseline. / Una decisione di scala.» · deliverable: mappa dati, baseline, cause, consumi, prime priorità, gap, proposta di estensione · criteri di uscita: dati completi, formule approvate, cause validate, report condiviso · struttura economica: **Avvio** (audit, setup e configurazione) · **Canone** (per sito, per linea, per livello) · **Servizi** (review, formazione, supporto) |
| **fonte** | master §10 S12 · §17.1 |
| **claim** | — |
| **gate** | G2 · `PH_AUDIT_PRICE`, `PH_PILOT_PRICE`, `PH_CONNECT_ANNUAL_FEE`, `PH_INSIGHT_ANNUAL_FEE`, `PH_REFYN_PRICING_MODEL` |
| **fallback** | client con G2 aperto: «**La proposta economica viene costruita sul perimetro validato.**» La struttura resta visibile, gli importi no |

## S13 · `v13_cta` · CTA

| | |
|---|---|
| **obiettivo** | rendere azionabile il passo successivo |
| **visual** | a sinistra i quattro blocchi, a destra la vista di turno con il costo di fermo del periodo osservato |
| **copy** | H1 «**Partiamo dalla prima linea da capire.**» · «**Condividiamo il perimetro, verifichiamo i dati disponibili e definiamo il passo successivo.**» · **Chi coinvolgere** «Produzione · manutenzione · energia · IT/OT» · **Cosa preparare** «Schema linea · elenco PLC · contatori · **dati di produzione · vincoli IT**» · **Cosa restituiamo** «Perimetro · gap · ipotesi pilot · proposta economica» · **Azione richiesta** «Una sessione di perimetrazione sulla prima linea.» · **Contatto** |
| **fonte** | master §6.8 (formula unica in tutto il deck), §10 S13, §17.1 |
| **claim** | — |
| **gate** | **G1 · GLOBAL.** `PH_CONTACT_NAME`, `PH_CONTACT_ROLE`, `PH_CONTACT_EMAIL`; G3 sul costo annuo a destra |
| **fallback** | la CTA **resta sempre**, condizione di build n. 2. Senza contatto approvato: working mostra `INPUT APERTO`, client mostra il blocco contatto con `PH_COMPANY_WEBSITE` se approvato — non lo è, quindi **warning globale di build**: la client edition si presenta dal vivo, non si invia |

## S14 · `v14_caso` · Caso cliente *(condizionale)*

| | |
|---|---|
| **obiettivo** | un caso reale, autorizzato, con metodo e limiti |
| **visual** | quattro blocchi numerati — contesto, problema, intervento, risultati — più metodo, citazione e limiti |
| **copy** | interamente segnaposto. Nessun valore inventato, nessun cliente anonimo costruito |
| **fonte** | master §11 e §20 |
| **claim** | — |
| **gate** | **`CASE_STUDY_READY = NO`** → canvas escluso dalla client edition |
| **fallback** | §20.4: nessuna slide. Lo scenario illustrativo **non** viene trasformato in caso cliente |

## A1 · `a1_matrice` · Matrice funzionale

| | |
|---|---|
| **obiettivo** | perimetro dei tre livelli, senza checkmark ambigui |
| **visual** | tabella 8 righe × 4 colonne (capacità, Connect, Insight, Refyn) + riga di profilo «cliente ideale» |
| **copy** | valori ammessi e usati: **incluso · configurabile · avanzato · previsto · non incluso**. Il valore «Base» della V9.1 esce (audit §3.3): la riga «Cause, micro-fermate e velocità» diventa *non incluso / incluso / incluso*, coerente con il §5.2 che assegna le cause a Insight |
| **fonte** | master §12 A1 · §5.2 · §5.3 |
| **claim** | `cumulativa` |
| **gate** | G2 · `PH_SERVICES_INCLUDED`, `PH_REFYN_PRICING_MODEL` |
| **fallback** | nota: «Il perimetro effettivo dipende dai dati disponibili e dalla configurazione dell'impianto.» |

## A2 · `a2_servizi` · Servizi

| | |
|---|---|
| **obiettivo** | il software rende visibile, le competenze accelerano il risultato |
| **visual** | tabella **Servizio · Output · Quando · Incluso/opzionale**, nove righe |
| **copy** | i nove servizi del §12: assessment e perimetrazione, setup e integrazione, KPI e formule, data quality review, performance ed energy review, improvement sprint, formazione, supporto, scale-up. Cade la colonna «Obiettivo» della V9.1 per fare posto alla quarta colonna del master |
| **fonte** | master §6.7, §12 A2 |
| **claim** | — |
| **gate** | **G2 · la quarta colonna.** Working: `DECISIONE COMMERCIALE` con `data-placeholder="PH_SERVICES_INCLUDED"` |
| **fallback** | client: «in proposta» su tutte le righe, più la nota già presente «Che cosa è compreso nell'avvio e che cosa resta opzionale è indicato nella proposta economica» |

## A3 · `a3_pricing` · Pricing *(condizionale)*

| | |
|---|---|
| **obiettivo** | avvio, canone, servizi |
| **visual** | tre fasce — una tantum, ricorrente, opzionale e contratto |
| **copy** | audit, setup della prima linea, canone base per sito, Connect, Insight, linee successive, Refyn, supporto premium, durata, rinnovo. Ogni importo è segnaposto |
| **fonte** | master §12 A3 · §17.1 modello di prezzo |
| **claim** | — |
| **gate** | **G2 · PAGE.** `data-ph-page="G2"` |
| **fallback** | §12: appendice **esclusa dalla client edition**, presente in working |

## A4 · `a4_faq` · FAQ

| | |
|---|---|
| **obiettivo** | le sei domande che arrivano sempre, con risposte prudenti |
| **visual** | sei coppie domanda/risposta, ciascuna con rimando alla pagina di dossier |
| **copy** | fermare la linea / sensori nuovi / marche diverse / residenza dei dati / gestionale / dal pilot alla scala. Risposte nelle formulazioni approvate del §7.6, §7.7, §7.8, §7.9 |
| **fonte** | master §12 A4 · §7 |
| **claim** | `read_only`, `residenza`, `erp`, `compat` |
| **gate** | G4 sul merito delle risposte tecniche, ma nessuna esclusione: le risposte sono già condizionali |
| **fallback** | — |

## A5 · `a5_assunzioni` · Assunzioni *(condizionale, nuovo in V9.2)*

| | |
|---|---|
| **obiettivo** | i parametri e le formule dietro i numeri del deck |
| **visual** | tabella parametro · valore · origine · stato, più le due formule |
| **copy** | nove parametri. **Correzione**: «Durata del turno · 480 min» aveva come origine «tre turni al giorno», incompatibile con i 230 turni all'anno da cui nascono gli 810 € (audit §3.2). Diventa «**un turno al giorno**», e si aggiunge la riga «Turni all'anno · 230 · 46 settimane × 5 giorni» |
| **fonte** | master §12 A5 · §7.2 · dataset |
| **claim** | — |
| **gate** | **G3 · PAGE, nuovo.** Il §12 la ammette «soltanto se il business case è pubblicato»: con G3 aperto non lo è |
| **fallback** | appendice esclusa dalla client edition. Le assunzioni restano nel `DFactory_OpenInputs_v9_2.md` e nella working edition |

---

# Parte II · Dossier tecnico

Navigazione a quattro sezioni su ogni pagina: **1 Prodotto** (02–06) ·
**2 Dati e architettura** (07–09) · **3 Misure e analisi** (10–12) ·
**4 Delivery e supporto** (13–14). Template A/B/C/D, mai tre pagine consecutive
con lo stesso template (§14.3).

## P01 · `p01_cover` · Cover · template A

| | |
|---|---|
| **obiettivo** | dichiarare che cosa è il documento e a chi parla |
| **visual** | fascia scura, indice delle quattro sezioni, elenco degli annessi |
| **copy** | «**Dossier tecnico preliminare** / per assessment e solution design» · sottotitolo «Acquisizione, supervisione e analisi integrata di produzione ed energia.» · destinatari Operations, Engineering, IT/OT, manutenzione, energia, procurement tecnico |
| **fonte** | master §15 P01 |
| **claim** | — |
| **gate** | **G4 · il titolo.** Con G4 approvato diventa «Dossier tecnico». G1 · `PH_COMPANY_LEGAL_NAME`, `PH_CONTACT_NAME`, `PH_CONTACT_EMAIL`, `PH_VERSION_DATE` |
| **fallback** | «Denominazione, referente e data di emissione si compilano prima dell'invio» · «Le viste di prodotto sono ricostruzioni con dati illustrativi, dichiarate pagina per pagina» |

## P02 · `p02_overview` · Overview · template C

| | |
|---|---|
| **obiettivo** | dal segnale all'informazione utilizzabile, in tre passaggi |
| **visual** | flusso 01 Acquisisce → 02 Contestualizza → 03 Restituisce, con i sette attributi al centro |
| **copy** | **Che cosa richiede**: accesso ai dati, punti di misura, anagrafiche, ambiente di deployment concordato con IT. **Che cosa non presuppone**, in tre voci: *sostituzione delle macchine · rifacimento completo dei PLC · cloud obbligatorio*. Nota «**Perimetro e requisiti vengono definiti nel solution design.**» Sotto le 130 parole (V9.1: 132) |
| **fonte** | master §15 P02 · §6.6 brownfield |
| **claim** | `brownfield`, `residenza` |
| **gate** | G4 · `PH_DEPLOYMENT_MODEL`; legale · `PH_DATA_OWNERSHIP` |
| **fallback** | «Eventuali adeguamenti ai segnali vengono verificati in audit» |

## P03 · `p03_livelli` · Livelli · template C

| | |
|---|---|
| **obiettivo** | tre gradi di valore da una sola acquisizione |
| **visual** | base dati comune, tre livelli sovrapposti |
| **copy** | H «Connect, Insight e Refyn sulla stessa base dati.» · che cosa aggiunge ogni livello · servizi specialistici attivabili su tutti e tre · stato Refyn «modulo avanzato» |
| **fonte** | master §15 P03 · §5.2 · §5.3 |
| **claim** | `cumulativa` |
| **gate** | G2 · `PH_SERVICES_INCLUDED`, `PH_REFYN_PRICING_MODEL` |
| **fallback** | «in sviluppo» **non** compare qui: l'unica occorrenza del dossier è a P06 |

## P04 · `p04_connect` · Connect · template B

| | |
|---|---|
| **obiettivo** | Connect rende visibile ciò che sta succedendo |
| **visual** | UI grande ricostruita: stato di linea, timeline del turno, elenco eventi con causale |
| **copy** | tre insight numerati (stato di linea · timeline · causa associata) · chi la usa · «Intervenire sul fermo in corso e assegnare la causa mentre è ancora nota» |
| **fonte** | master §15 P04 · §7.1 |
| **claim** | — |
| **gate** | G5 · asset reale se disponibile; `PH_CONNECT_EXACT_SCOPE`, `PH_CONNECT_REPORTS`, `PH_CONNECT_ALERTS` |
| **fallback** | «vista ricostruita · dati illustrativi» |

## P05 · `p05_insight` · Insight · template B

| | |
|---|---|
| **obiettivo** | Insight spiega dove si perde capacità e valore |
| **visual** | ranking delle cause per costo, sette giorni |
| **copy** | che cosa aggiunge (cause validate, correlazione con l'energia, costo energetico per pezzo e CO₂, confronti fra turni e formati) · come ordina (per impatto economico) · «La causa è associata all'evento e validata da chi la conosce» |
| **fonte** | master §15 P05 · §7.1 · dataset |
| **claim** | `costo_en`, `co2` |
| **gate** | G5 · report reale se disponibile; `PH_INSIGHT_EXACT_SCOPE`, `PH_COST_CALCULATION_METHOD`, `PH_CO2_METHOD` |
| **fallback** | — |

## P06 · `p06_refyn` · Refyn · template C

| | |
|---|---|
| **obiettivo** | un ciclo che si chiude: priorità, azioni, verifica |
| **visual** | ciclo a tre nodi con ritorno alle priorità |
| **copy** | che cosa porta con sé un'azione: responsabile e ambito, baseline e target, scadenza e stato, beneficio verificato o no · «**Modulo avanzato in sviluppo**» |
| **fonte** | master §5.2 · §15 P06 |
| **claim** | `refyn` |
| **gate** | `PH_REFYN_MVP_SCOPE`, `PH_REFYN_PILOT_RULES`, `PH_REFYN_RELEASE_TARGET` |
| **fallback** | **unica occorrenza di «in sviluppo» nel dossier**: condizione di build n. 8. Nessuna funzione futura aggiunta (§15 P06) |

## P07 · `p07_sorgenti` · Punti di misura · template A + D

| | |
|---|---|
| **obiettivo** | da dove leggiamo e dove il dato va aggiunto |
| **visual** | apertura di sezione 2, poi tabella macchina × (PLC e stati · conta pezzi · contatore energia · che cosa manca), quattro righe |
| **copy** | classificazione **già presente / da verificare / da aggiungere** · quando serve nuova sensoristica: precisione, installazione, proprietà dello strumento e calibrazione si decidono in audit; la sensoristica è voce separata dal software |
| **fonte** | master §15 P07 |
| **claim** | `compat` |
| **gate** | G4 · `PH_STANDARD_SIGNAL_LIST`, `PH_SENSOR_ACCURACY_REQUIREMENTS`, `PH_METERING_STANDARDS`; G2 · `PH_SENSOR_PRICING_RULE` |
| **fallback** | «la classificazione riguarda l'impianto, non il prodotto» — il §15 P07 vieta di leggerla come maturità di prodotto |

## P08 · `p08_architettura` · Architettura · template C

| | |
|---|---|
| **obiettivo** | dove risiede e come comunica con la rete di stabilimento |
| **visual** | quattro livelli — impianto, acquisizione, applicazione e dati, utenti — con il confine di rete e il collegamento tratteggiato verso il gestionale |
| **copy** | **Definito dal prodotto**: flusso di acquisizione, applicazione e regole, output, logica di calcolo. **Da chiudere nel solution design**: ambiente, segmentazione di rete, autenticazione e ruoli, **backup e ripristino**, **supporto remoto**. Sotto le 130 parole (V9.1: 132) |
| **fonte** | master §15 P08 · §7.8 · §7.9 |
| **claim** | `read_only` (formulazione approvata integrale), `residenza` |
| **gate** | **G4.** `PH_DEPLOYMENT_MODEL`, `PH_SERVER_OWNER`, `PH_SUPPORTED_OS`, `PH_REQUIRED_PORTS`, `PH_ERP_INTEGRATION_METHODS`, `PH_READ_ONLY_POLICY` |
| **fallback** | «La configurazione standard privilegia l'acquisizione in sola lettura. Eventuali scambi ulteriori vengono definiti nel solution design.» · «schema logico · non è un disegno di rete» |

## P09 · `p09_contesto` · Contestualizzazione · template B

| | |
|---|---|
| **obiettivo** | lo stesso evento, lo stesso tempo, lo stesso prodotto |
| **visual** | cinque tracce (produzione, stato, energia, ordine e formato, causa) sullo stesso asse, un solo indicatore alle 11:24 |
| **copy** | i sette attributi · tre controlli di qualità: completezza, coerenza fra sorgenti, validazione della causa · decisione «**Il dato diventa leggibile soltanto quando condivide tempo e contesto.**» · «La causa è proposta sulla base dello stato e validata da chi la conosce.» |
| **fonte** | master §15 P09 · §7.1 |
| **claim** | — |
| **gate** | G4 · `PH_TIME_SYNC_REQUIREMENT`, `PH_STANDARD_TAG_MODEL`, `PH_CAUSE_VALIDATION_PROCESS` |
| **fallback** | — |

## P10 · `p10_oee` · OEE e perdite · template A + C

| | |
|---|---|
| **obiettivo** | l'OEE dice quanto, le perdite dicono dove |
| **visual** | apertura di sezione 3, poi scomposizione a gradini 100 → 94,6 → 74,7 → 71,4 con la capacità persa in giallo, e ranking delle quattro cause |
| **copy** | H «**L'OEE dice quanto. Le perdite dicono dove.**» · «OEE del turno: 94,6% × 79% × 95,6% = 71,4%» · nota che dichiara **perimetro, calendario, ideal cycle e good count** (§15 P10) · «La prima causa vale il 43% del costo» |
| **fonte** | master §15 P10 · §7.4 (mai «il polmone») · dataset |
| **claim** | `oee` |
| **gate** | G4 · `PH_OEE_CALENDAR_RULES`, `PH_IDEAL_CYCLE_TIME_RULE`, `PH_GOOD_COUNT_RULE`, `PH_LINE_OEE_AGGREGATION` |
| **fallback** | «dataset illustrativo · turno e settimana tipo» |

## P11 · `p11_energia` · Energia e costo energetico · template C

| | |
|---|---|
| **obiettivo** | dal consumo al costo energetico del pezzo |
| **visual** | potenza per stato sopra; sotto, i tre numeri del turno ciascuno col proprio calcolo, e i tre indicatori per 1.000 pezzi |
| **copy** | 735 kWh · 162 € · 227.000 pz · 3,2 kWh / 0,71 € / 1,13 kgCO₂e per 1.000 pezzi · parametri del calcolo · «CO₂ calcolata o stimata» |
| **fonte** | master §15 P11 · §7.3 (mai «costo del pezzo» per il solo perimetro energia) · dataset |
| **claim** | `costo_en`, `co2` |
| **gate** | G3 sui parametri · `PH_ENERGY_PRICE_SOURCE`, `PH_EMISSION_FACTOR_SOURCE`, `PH_CO2_METHOD`, `PH_COST_ALLOCATION_RULE` |
| **fallback** | «Prezzo e fattore di emissione arrivano dal contratto di fornitura. Il perimetro della potenza a impianto fermo — linea, macchine o ausiliari — si dichiara nel solution design.» |

## P12 · `p12_output` · Output · template D

| | |
|---|---|
| **obiettivo** | il dato esce nella forma in cui viene usato |
| **visual** | tabella output × chi lo usa × che decisione abilita, **sei righe** |
| **copy** | dashboard a bordo linea · report programmati · export CSV ed Excel · PDF di periodo · **API** *(riga nuova, §15 P12)* · integrazioni. Utenti: operatori, produzione, manutenzione, energia, direzione, IT |
| **fonte** | master §15 P12 · §7.7 |
| **claim** | `erp` |
| **gate** | G4 · `PH_EXPORT_FORMATS`, `PH_API_AVAILABILITY`, `PH_REPORT_CATALOGUE`, `PH_ERP_INTEGRATION_METHODS` |
| **fallback** | «Le integrazioni con il gestionale sono possibili previa verifica del punto di innesto — perimetro, formato e frequenza si chiudono nel solution design.» L'API è dichiarata come **disponibilità da confermare**, non come funzione certa |

## P13 · `p13_pilot` · Pilot · template A + C

| | |
|---|---|
| **obiettivo** | il pilot non si chiude con una demo ma con una decisione |
| **visual** | apertura di sezione 4, poi i quattro deliverable in sequenza |
| **copy** | mappa dati e segnali · baseline produzione ed energia · prime cause e priorità · decisione di scala · criteri di uscita: dati completi, formule approvate, cause validate, report condiviso |
| **fonte** | master §15 P13 · allineato a S12 del deck |
| **claim** | — |
| **gate** | G2 · `PH_PILOT_DURATION`, `PH_PILOT_SCOPE`, `PH_PILOT_SUCCESS_CRITERIA`, `PH_PILOT_PRICE` |
| **fallback** | «Durata, partecipanti e condizioni economiche si fissano nella proposta di pilot» |

## P14 · `p14_servizi` · Servizi e supporto · template D

| | |
|---|---|
| **obiettivo** | il progetto continua dopo il go-live |
| **visual** | tabella servizio × che cosa produce × modello, sei righe |
| **copy** | assessment, setup, KPI e formule, performance ed energy review, formazione e adozione, supporto e scale-up · **unica citazione consentita**: «Le soluzioni Connect, Insight e Refyn evolvono le competenze e le funzionalità sviluppate con MAPST 4.0 e MarEnergy, che continuano a essere supportati per l'installato esistente» |
| **fonte** | master §15 P14 · §5.4 (una volta nel dossier, mai nel deck) |
| **claim** | — |
| **gate** | G2 · `PH_SERVICES_INCLUDED`, `PH_SERVICES_OPTIONAL`; G4 · `PH_SUPPORT_HOURS`, `PH_SLA_RESPONSE_TIMES`, `PH_UPDATE_POLICY`, `PH_REMOTE_SUPPORT_POLICY` |
| **fallback** | «**Condizioni da formalizzare nella proposta e nel contratto.**» (§15 P14, SLA aperto) |

## A1 · `pa1_compatibilita` · Compatibilità · template D

| | |
|---|---|
| **obiettivo** | preparare il confronto con OT |
| **visual** | tabella **Elemento · Cosa si verifica · Esito · Owner**, otto righe |
| **copy** | gli otto campi del §16: PLC · protocollo · versione · accesso · gateway · contatore · ERP · lettura/scrittura. Esiti ammessi: **supportato · condizionato · da verificare · da aggiungere**. Owner: audit tecnico, solution design, IT del cliente, manutenzione. Nota: «Un elenco generico di protocolli non dice se un impianto è leggibile: conta la versione installata su quella macchina e i tag che espone» |
| **fonte** | master §16 A1 · §7.6 |
| **claim** | `compat` |
| **gate** | **G4.** `PH_SUPPORTED_PROTOCOLS`, `PH_PROTOCOL_VERSIONS`, `PH_REQUIRED_PORTS`, `PH_READ_ONLY_POLICY`, `PH_GATEWAY_REQUIREMENTS`, `PH_FIREWALL_RULES` |
| **fallback** | con G4 aperto tutti gli esiti sono «da verificare»: la colonna si compila durante l'audit tecnico, e il piede pagina lo dichiara |

## A2 · `pa2_sizing` · Sizing · template D

| | |
|---|---|
| **obiettivo** | fornire una stima preliminare, e dire come si calcola |
| **visual** | le cinque grandezze → la taglia dell'ambiente. **In working**, in più: tabella **Fascia · Tag · Linee · Frequenza · Retention · CPU · RAM · Storage** su tre righe (piccola, media, grande) |
| **copy** | che cosa serve per calcolarlo: tag, frequenza, conservazione, linee, utenti concorrenti · «Le tre taglie sono la conseguenza delle cinque grandezze, non un catalogo da cui scegliere» |
| **fonte** | master §16 A2 |
| **claim** | — |
| **gate** | **G4 · la tabella delle fasce.** `PH_MIN_CPU`, `PH_MIN_RAM`, `PH_MIN_STORAGE`, `PH_RETENTION_DEFAULT`, `PH_STORAGE_GROWTH_RULE`, `PH_HIGH_AVAILABILITY` |
| **fallback** | §16: *client preliminare* mostra il **metodo**, non i valori. La tabella delle tre fasce resta nella working edition finché G4 è aperto |

## A3 · `pa3_governo` · Security e governo · template D

| | |
|---|---|
| **obiettivo** | che cosa si decide e chi lo decide |
| **visual** | tabella **Ambito · Modello · Valore · Chi decide**, otto righe che coprono i dodici ambiti del §16 |
| **copy** | 1 autenticazione e identità · 2 ruoli e permessi · 3 registro degli accessi · 4 cifratura · 5 backup, ripristino e conservazione · 6 aggiornamenti e supporto remoto · 7 proprietà del dato e licenza · 8 fine contratto. Stato con G4 aperto: «**Annesso per la raccolta dei requisiti.**» Sotto le 130 parole (V9.1: 134) |
| **fonte** | master §16 A3 |
| **claim** | — |
| **gate** | **G4.** `PH_AUTHENTICATION_MODEL`, `PH_ROLE_MODEL`, `PH_AUDIT_LOGGING`, `PH_DATA_ENCRYPTION_AT_REST`, `PH_BACKUP_POLICY`, `PH_RETENTION_DEFAULT`, `PH_PATCHING_POLICY`, `PH_REMOTE_SUPPORT_POLICY`, `PH_DATA_OWNERSHIP`, `PH_LICENSE_RIGHTS`, `PH_END_OF_CONTRACT_DATA` |
| **fallback** | la formulazione approvata sulla **proprietà dei dati non viene pubblicata**: il §25 la vieta senza approvazione legale. La riga dichiara che cosa si decide e chi decide, e rimanda al legale |

## A4 · `pa4_kpi` · Dizionario KPI · template D

| | |
|---|---|
| **obiettivo** | ogni indicatore ha una formula scritta |
| **visual** | tabella a otto colonne — **indicatore · formula · unità · sorgente · frequenza · owner · versione · data approvazione** — su sei righe |
| **copy** | disponibilità · performance · qualità · OEE · consumo specifico · perdita del fermo. Nota: «Il tempo pianificato, le fermate programmate e la cadenza di riferimento di ogni formato si concordano prima del go-live» |
| **fonte** | master §16 A4 |
| **claim** | `oee`, `costo_en` |
| **gate** | G4 · `PH_KPI_OWNER`, `PH_KPI_VERSION`, `PH_KPI_APPROVAL_DATE`, `PH_OEE_DEFINITION_OWNER` |
| **fallback** | client: owner «da nominare», versione «—», data «da approvare». Il dizionario è la struttura, i valori arrivano col go-live |

---

# Parte III · Riepiloghi

## Alternanza dei template nel dossier

| pagina | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | A1 | A2 | A3 | A4 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| template | A | C | C | B | B | C | A+D | C | B | A+C | C | D | A+C | D | D | D | D | D |

Nessuna sequenza di tre pagine core con lo stesso template: 02–03 sono C ma la 04
è B; 10–11 sono C ma la 12 è D. Gli annessi sono tutti D per definizione (§14.2
template D = annesso) e non sono pagine core: il §14.3 riguarda la lettura
continua del corpo.

## Occorrenze sorvegliate

| espressione | deck | dossier | limite |
|---|--:|--:|---|
| «in sviluppo» | 1 · S08 | 1 · P06 | max 1 per documento (§5.2, build n. 8) |
| «MAPST 4.0» / «MarEnergy» | **0** | 1 · P14 | vietato nel corpo del deck (§5.4) |
| «Insight» al singolare | sempre | sempre | §22.2 |
| «causa associata» | S03, S04, S06 | P04, P05, P09 | mai «rilevata automaticamente» (§7.1) |
| «costo energetico» | S07 | P05, P11 | mai «costo del pezzo» sul solo perimetro energia (§7.3) |
| «calcolata o stimata» | S07 | P05, P11 | sempre accanto alla CO₂ (§7.3) |
| valori annualizzati | working | — | mai in client con G3 aperto, **cifre e lettere** (§21.2) |

## Fallback client attivi oggi

| gate | canvas toccati | che cosa vede il cliente |
|---|---|---|
| G1 aperto | S13, P01 | CTA senza referente · warning globale di build: il deck si presenta, non si invia |
| G2 aperto | S09, S12, A1, A2, **A3 esclusa** | struttura economica senza importi · «la proposta economica viene costruita sul perimetro validato» |
| G3 aperto | S11, S13, **A5 esclusa** | formula e settimana osservata, nessun risultato annualizzato |
| G4 aperto | P01, P08, A1, A2, A3, A4 | titolo «preliminare» · metodo invece dei valori · «da definire nel solution design» sulle sole pagine tecniche |
| G5 aperto | S03, S04, S05, S10, P04, P05, P12 | ricostruzioni dichiarate, nessuna prova aziendale numerica |
| CASE = NO | **S14 esclusa** | nessuna slide di caso cliente |
