# D.Factory · Registro placeholder V9.2

221 placeholder · **P0 58** · P1 156 · P2 7

Stessi token della V9.1: il §8.1 vieta di rinominarli, e non sono stati
rinominati. La V9.2 aggiunge una cosa sola, ma cambia come si legge la working
edition — **l'etichetta**. Prima il token era il testo principale, adesso è un
attributo:

```html
<span data-ed="working" class="ph" data-placeholder="PH_CONTACT_NAME">INPUT APERTO</span>
```

Quale delle quattro etichette del §8.3 tocchi a un campo non è una scelta
editoriale: **decide il gate**, e per i campi fuori dai gate decide la colonna
*owner*. La regola vive in `labels92.py`, così registro e documenti non possono
divergere.

| gate | etichetta | perché |
|---|---|---|
| G1 | `INPUT APERTO` | identità, referente e definizione dell'audit sono informazioni da recuperare, non decisioni da prendere |
| G2 | `DECISIONE COMMERCIALE` | prezzi, inclusioni, durata: qualcuno deve decidere |
| G3 · G4 | `VALIDAZIONE TECNICA` | dataset e requisiti si verificano, non si scelgono |
| G5 e `PH_REAL_*` | `ASSET RICHIESTO` | serve un file, con autorizzazione |
| fuori dai gate | dall'owner | Commerciale → decisione · Tecnico → validazione · resto → input aperto |


| etichetta | campi |
|---|--:|
| `VALIDAZIONE TECNICA` | 127 |
| `INPUT APERTO` | 43 |
| `DECISIONE COMMERCIALE` | 43 |
| `ASSET RICHIESTO` | 8 |

---

## 1. I cinque gate

| Gate | Che cosa blocca | Scope | Campi | Stato | Effetto sulla V9.2 |
|---|---|:--:|--:|:--:|---|
| **G1** Identità e CTA | la pubblicazione del Sales Deck | `GLOBAL` | 9 | `OPEN` | La CTA resta nella client edition (§9.13) ma senza referente non è inviabile: il deck si presenta dal vivo, non si manda. |
| **G2** Modello commerciale | la definizione completa dell'offerta | `SECTION` | 10 | `OPEN` | L'appendice pricing non entra nella client edition. Il deck mostra la struttura, non gli importi. |
| **G3** Dataset | la pubblicazione del business case | `SECTION` | 12 | `OPEN` | I valori annualizzati escono dalla client edition. Restano la formula, i dati del turno e della settimana, che sono osservati nello scenario. |
| **G4** Requisiti tecnici minimi | la dichiarazione «pronto per IT» | `SECTION` | 18 | `OPEN` | Il dossier resta «preliminare per assessment e solution design». |
| **G5** Evidenza commerciale | l'invio a freddo e il passaggio in procurement | `NONE` | 8 | `OPEN` | Non blocca l'uso dal vivo. Bastano due elementi approvati fra screenshot, report, schema, foto, fatto aziendale, caso cliente. |
| **CASE** caso cliente | la slide 14 del deck | `PAGE` | 1 | `NO` | La slide 14 non entra nella client edition. |

### Che cosa cambia in ciascun canvas quando il gate si chiude

| gate | canvas che cambiano | oggi il cliente vede |
|---|---|---|
| G1 | `v13_cta` · `p01_cover` | CTA senza referente · warning globale: il deck si presenta, non si invia |
| G2 | `v09_scelta` · `v12_pilot` · `a1_matrice` · `a2_servizi` · **`a3_pricing` esclusa** | struttura economica senza importi |
| G3 | `v11_valore` · `v13_cta` · **`a5_assunzioni` esclusa** | formula e settimana osservata, nessun annualizzato |
| G4 | `p01_cover` · `p08_architettura` · `pa1` · `pa2` · `pa3` · `pa4` | titolo preliminare · metodo invece dei valori |
| G5 | `v03` `v04` `v05` `v10` · `p04` `p05` `p12` | ricostruzioni dichiarate, nessun asset reale |
| CASE | **`v14_caso` esclusa** | nessuna slide di caso cliente |

---

## 2. Il registro

Colonne: `id` · descrizione · owner · fonte · priorità · scope · gate · etichetta nella working edition · canvas in cui compare.

L'asterisco su un canvas significa che lì il token compare nel pannello «INPUT APERTI» in coda alla pagina, che parla al registro e non al lettore.


### 5.1 Identità e contatti

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_COMPANY_LEGAL_NAME` | Denominazione legale corretta | Direzione | P0 | `GLOBAL` | G1 | INPUT APERTO | p01_cover · p01_cover* |
| `PH_COMPANY_BRAND_FORM` | Grafia ufficiale del brand | Marketing | P1 | `NONE` | — | INPUT APERTO | v01_cover* |
| `PH_COMPANY_VAT` | Partita IVA | Direzione | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_COMPANY_ADDRESS` | Sede legale o operativa | Direzione | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_COMPANY_WEBSITE` | URL ufficiale | Marketing | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_CONTACT_NAME` | Referente commerciale | Commerciale | P0 | `GLOBAL` | G1 | INPUT APERTO | p01_cover · p01_cover* · v13_cta · v13_cta* |
| `PH_CONTACT_ROLE` | Ruolo del referente | Commerciale | P0 | `GLOBAL` | G1 | INPUT APERTO | v13_cta* |
| `PH_CONTACT_EMAIL` | Email ufficiale | Commerciale | P0 | `GLOBAL` | G1 | INPUT APERTO | p01_cover · p01_cover* · v13_cta* |
| `PH_CONTACT_PHONE` | Numero di telefono | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_GROUP_RELATIONSHIP` | Relazione con Gruppo Clevertech | Direzione | P1 | `NONE` | — | INPUT APERTO | v10_perche* |
| `PH_LEGAL_FOOTER` | Formula legale del piede | Legale | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_VERSION_DATE` | Data di emissione del documento | Direzione | P1 | `NONE` | — | INPUT APERTO | p01_cover · p01_cover* |

### 5.2 Prova aziendale

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_COMPANY_FOUNDING_YEAR` | Anno di avvio | Direzione | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_COMPANY_YEARS_EXPERIENCE` | Anni di esperienza | Direzione | P1 | `NONE` | — | INPUT APERTO | v10_perche* |
| `PH_ACTIVE_CLIENTS` | Numero clienti attivi | Direzione | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_ACTIVE_SITES` | Numero stabilimenti | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_ACTIVE_LINES` | Numero linee collegate | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_ACTIVE_MACHINES` | Numero macchine collegate | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_PROJECTS_COMPLETED` | Numero progetti o casi conclusi | Direzione | P1 | `NONE` | — | INPUT APERTO | v10_perche* |
| `PH_SECTORS_APPROVED` | Settori autorizzati alla citazione | Legale | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_RETENTION_METRIC` | Retention o tasso di rinnovo | Direzione | P2 | `NONE` | — | INPUT APERTO | — |
| `PH_TEAM_SIZE` | Dimensione del team dedicato | Direzione | P2 | `NONE` | — | INPUT APERTO | — |
| `PH_GROUP_PROOF` | Evidenza del gruppo industriale | Direzione | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_PARTNERSHIP_SIEMENS_APPROVAL` | Claim di partnership autorizzato | Legale | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_SAP_INTEGRATION_PROOF` | Fonte verificabile per il claim ERP | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_PATENT_BOX_APPROVAL` | Claim Patent Box autorizzato | Legale | P2 | `NONE` | — | INPUT APERTO | — |

### 5.3 Caso cliente · identificativi

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_CASE_CLIENT_DISPLAY_NAME` | Nome cliente o forma anonima | Legale | P1 | `NONE` | — | cliente o dicitura anonima | v14_caso |
| `PH_CASE_CLIENT_LEGAL_NAME` | Nome legale, uso interno | Legale | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_CASE_CLIENT_SECTOR` | Settore | Commerciale | P1 | `NONE` | — | settore | v14_caso |
| `PH_CASE_CLIENT_SITE` | Stabilimento o paese | Commerciale | P1 | `NONE` | — | stabilimento | v14_caso |
| `PH_CASE_LINE_TYPE` | Tipo di linea | Tecnico | P1 | `NONE` | — | tipo di linea | v14_caso |
| `PH_CASE_PROCESS` | Processo osservato | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_CONFIDENTIALITY` | Pubblico, anonimo o confidenziale | Legale | P1 | `NONE` | — | INPUT APERTO | v14_caso* |
| `PH_CASE_APPROVAL_STATUS` | Stato autorizzazione alla pubblicazione | Legale | P1 | `NONE` | — | INPUT APERTO | v14_caso* |
| `PH_CASE_APPROVAL_OWNER` | Chi ha autorizzato | Legale | P1 | `NONE` | — | INPUT APERTO | v14_caso* |

### 5.3 Caso cliente · problema e contesto

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_CASE_INITIAL_PROBLEM` | Problema iniziale | Commerciale | P1 | `NONE` | — | problema iniziale | v14_caso |
| `PH_CASE_BUSINESS_IMPACT` | Impatto percepito dal cliente | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_CASE_BASELINE_PERIOD` | Periodo della baseline | Tecnico | P1 | `NONE` | — | periodo di baseline | v14_caso |
| `PH_CASE_BASELINE_DATA` | Dati della baseline | Tecnico | P1 | `NONE` | — | dati di baseline | v14_caso |
| `PH_CASE_DATA_SOURCES` | PLC, contatori, gestionale, sensori | Tecnico | P1 | `NONE` | — | fonti del dato | v14_caso |
| `PH_CASE_SCOPE` | Macchine, linea, sito | Tecnico | P1 | `NONE` | — | perimetro | v14_caso |
| `PH_CASE_PRECONDITIONS` | Prerequisiti presenti | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_GAPS` | Gap di dati o di misura | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |

### 5.3 Caso cliente · intervento

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_CASE_SOLUTION_MODULE` | Connect, Insight o Refyn | Commerciale | P1 | `NONE` | — | livello attivato | v14_caso |
| `PH_CASE_IMPLEMENTATION_SCOPE` | Perimetro implementato | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_INTERVENTION` | Attività svolte | Tecnico | P1 | `NONE` | — | intervento | v14_caso |
| `PH_CASE_ADDED_SENSORS` | Sensori o contatori aggiunti | Tecnico | P1 | `NONE` | — | sensori aggiunti | v14_caso |
| `PH_CASE_ERP_INTEGRATION` | Integrazione con il gestionale | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_TIME_TO_FIRST_SIGNAL` | Tempo al primo segnale | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_TIME_TO_USABLE_DATA` | Tempo al dato utilizzabile | Tecnico | P1 | `NONE` | — | tempo al primo dato utile | v14_caso |
| `PH_CASE_PILOT_DURATION` | Durata del pilot | Commerciale | P1 | `NONE` | — | durata del pilot | v14_caso |
| `PH_CASE_USERS` | Utenti coinvolti | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |

### 5.3 Caso cliente · risultati

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_CASE_RESULT_1_LABEL` | Nome del risultato 1 | Tecnico | P1 | `NONE` | — | risultato 1 | v14_caso |
| `PH_CASE_RESULT_1_BASELINE` | Baseline del risultato 1 | Tecnico | P1 | `NONE` | — | risultato 1 · baseline | v14_caso |
| `PH_CASE_RESULT_1_AFTER` | Valore dopo, risultato 1 | Tecnico | P1 | `NONE` | — | risultato 1 · dopo | v14_caso |
| `PH_CASE_RESULT_1_UNIT` | Unità di misura, risultato 1 | Tecnico | P1 | `NONE` | — | risultato 1 · unità | v14_caso |
| `PH_CASE_RESULT_1_METHOD` | Metodo di misura, risultato 1 | Tecnico | P1 | `NONE` | — | metodo di misura | v14_caso |
| `PH_CASE_RESULT_2_LABEL` | Nome del risultato 2 | Tecnico | P1 | `NONE` | — | risultato 2 | v14_caso |
| `PH_CASE_RESULT_2_BASELINE` | Baseline del risultato 2 | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_RESULT_2_AFTER` | Valore dopo, risultato 2 | Tecnico | P1 | `NONE` | — | risultato 2 · dopo | v14_caso |
| `PH_CASE_RESULT_2_UNIT` | Unità di misura, risultato 2 | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_RESULT_2_METHOD` | Metodo di misura, risultato 2 | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_RESULT_3_LABEL` | Nome del risultato 3 | Tecnico | P1 | `NONE` | — | risultato 3 | v14_caso |
| `PH_CASE_RESULT_3_BASELINE` | Baseline del risultato 3 | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_RESULT_3_AFTER` | Valore dopo, risultato 3 | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_RESULT_3_UNIT` | Unità di misura, risultato 3 | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_RESULT_3_METHOD` | Metodo di misura, risultato 3 | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_RESULT_PERIOD` | Periodo osservato | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | v14_caso* |
| `PH_CASE_ANNUALIZED_VALUE` | Valore annualizzato | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_CASE_PAYBACK` | Payback verificato | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_CASE_CONFIDENCE_NOTE` | Limiti e attendibilità della misura | Tecnico | P1 | `NONE` | — | limiti dichiarati della misura | v14_caso |

### 5.3 Caso cliente · testimonial e asset

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_CASE_QUOTE` | Citazione del cliente | Legale | P1 | `NONE` | — | citazione autorizzata | v14_caso |
| `PH_CASE_QUOTE_AUTHOR` | Autore della citazione | Legale | P1 | `NONE` | — | autore | v14_caso |
| `PH_CASE_QUOTE_ROLE` | Ruolo dell’autore | Legale | P1 | `NONE` | — | ruolo | v14_caso |
| `PH_CASE_QUOTE_APPROVAL` | Autorizzazione alla citazione | Legale | P1 | `NONE` | — | stato dell’autorizzazione | v14_caso |
| `PH_CASE_LOGO_ASSET` | Logo cliente autorizzato | Legale | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_CASE_SCREENSHOT_ASSET` | Screenshot reale del caso | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CASE_PHOTO_ASSET` | Foto reale del caso | Marketing | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_CASE_DIAGRAM_ASSET` | Schema anonimizzato del caso | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |

### 5.4 Audit e pilot

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_AUDIT_NAME` | Nome commerciale del primo passo | Commerciale | P0 | `GLOBAL` | G1 | INPUT APERTO | — |
| `PH_AUDIT_DURATION` | Durata dell’audit | Commerciale | P0 | `GLOBAL` | G1 | INPUT APERTO | v09_scelta* |
| `PH_AUDIT_PRICE` | Prezzo dell’audit | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a3_pricing · v12_pilot* |
| `PH_AUDIT_CREDIT_POLICY` | Accredito dell’audit sul progetto | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | a3_pricing* |
| `PH_AUDIT_PARTICIPANTS` | Partecipanti richiesti | Commerciale | P0 | `GLOBAL` | G1 | INPUT APERTO | v13_cta* |
| `PH_AUDIT_CLIENT_HOURS` | Ore richieste al cliente | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_AUDIT_INPUTS` | Materiali richiesti al cliente | Tecnico | P0 | `GLOBAL` | G1 | INPUT APERTO | v13_cta* |
| `PH_AUDIT_DELIVERABLES` | Output dell’audit | Tecnico | P0 | `GLOBAL` | G1 | INPUT APERTO | v13_cta* |
| `PH_AUDIT_VALIDITY` | Validità dell’offerta | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_PILOT_DURATION` | Durata del pilot | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | p13_pilot* |
| `PH_PILOT_SCOPE` | Perimetro del pilot | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p13_pilot* |
| `PH_PILOT_SUCCESS_CRITERIA` | Criteri di successo | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p13_pilot* |
| `PH_PILOT_EXIT_CRITERIA` | Criteri di uscita | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_PILOT_PRICE` | Prezzo del pilot | Commerciale | P1 | `PAGE` | — | DECISIONE COMMERCIALE | p13_pilot* · v12_pilot* |
| `PH_PILOT_CONVERSION_POLICY` | Conversione del pilot a contratto | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_PILOT_REVERSIBILITY` | Reversibilità del pilot | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |

### 5.5 Pricing e contratto

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_SITE_BASE_FEE` | Canone base per sito | Commerciale | P1 | `PAGE` | — | DECISIONE COMMERCIALE | a3_pricing |
| `PH_SETUP_FIRST_LINE` | Setup della prima linea | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a3_pricing |
| `PH_CONNECT_ANNUAL_FEE` | Canone Connect | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a3_pricing · v12_pilot* |
| `PH_INSIGHT_ANNUAL_FEE` | Canone Insight | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a3_pricing · v12_pilot* |
| `PH_REFYN_PRICING_MODEL` | Modello economico di Refyn | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a1_matrice* · a3_pricing · p03_livelli* · v09_scelta* · v12_pilot* |
| `PH_ADDITIONAL_LINE_FEE` | Canone per linee successive | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a3_pricing |
| `PH_SENSOR_PRICING_RULE` | Regola di quotazione della sensoristica | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | p07_sorgenti* |
| `PH_SERVICES_INCLUDED` | Servizi compresi nell’avvio | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a1_matrice* · a2_servizi · a2_servizi* · p03_livelli* · v08_offerta* |
| `PH_SERVICES_OPTIONAL` | Servizi opzionali | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a2_servizi* · v08_offerta* |
| `PH_PERFORMANCE_REVIEW_FEE` | Prezzo della performance review | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_ENERGY_REVIEW_FEE` | Prezzo della energy review | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_PREMIUM_SUPPORT_FEE` | Prezzo del supporto premium | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | a3_pricing |
| `PH_CONTRACT_TERM` | Durata contrattuale | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a3_pricing · v09_scelta* |
| `PH_RENEWAL_TERMS` | Condizioni di rinnovo | Commerciale | P0 | `SECTION` | G2 | DECISIONE COMMERCIALE | a3_pricing |
| `PH_TERMINATION_TERMS` | Condizioni di recesso | Legale | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_PAYMENT_TERMS` | Termini di pagamento | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | a3_pricing* |
| `PH_PRICE_VALIDITY` | Validità dei prezzi | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | a3_pricing* |
| `PH_INDEXATION` | Indicizzazione | Commerciale | P2 | `NONE` | — | DECISIONE COMMERCIALE | — |

### 5.6 Supporto e SLA

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_SUPPORT_HOURS` | Orari del supporto | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | a2_servizi* · p14_servizi* |
| `PH_SUPPORT_CHANNELS` | Canali del supporto | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | p14_servizi* |
| `PH_SLA_SEVERITY_LEVELS` | Livelli di severità | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_SLA_RESPONSE_TIMES` | Tempi di risposta | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | p14_servizi* |
| `PH_SLA_RESOLUTION_TARGETS` | Obiettivi di risoluzione | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_ESCALATION_PROCESS` | Processo di escalation | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_MAINTENANCE_WINDOWS` | Finestre di manutenzione | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_UPDATE_POLICY` | Politica di aggiornamento | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p14_servizi* |
| `PH_CHANGE_REQUEST_POLICY` | Politica delle change request | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | — |
| `PH_REMOTE_SUPPORT_POLICY` | Politica di supporto remoto | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | p14_servizi* |

### 5.7 Deployment e infrastruttura

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_DEPLOYMENT_MODEL` | On-premise, VM o altro | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | p02_overview* · p08_architettura* |
| `PH_SERVER_OWNER` | Proprietà dell’ambiente | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | p08_architettura* |
| `PH_SUPPORTED_OS` | Sistemi operativi supportati | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | p08_architettura* |
| `PH_MIN_CPU` | CPU minima | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa2_sizing · pa2_sizing* |
| `PH_MIN_RAM` | RAM minima | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa2_sizing · pa2_sizing* |
| `PH_MIN_STORAGE` | Storage minimo | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa2_sizing · pa2_sizing* |
| `PH_STORAGE_GROWTH_RULE` | Regola di crescita dello storage | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa2_sizing* |
| `PH_RETENTION_DEFAULT` | Retention di default | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa2_sizing · pa3_governo* |
| `PH_HIGH_AVAILABILITY` | Alta disponibilità | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa2_sizing* |
| `PH_VIRTUALIZATION_SUPPORT` | Virtualizzazione supportata | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CONTAINER_SUPPORT` | Container supportati | Tecnico + IT | P2 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_TIME_SYNC_REQUIREMENT` | Requisito di sincronizzazione oraria | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | p09_contesto* |
| `PH_INTERNET_REQUIREMENT` | Accesso a internet richiesto | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_CLOUD_OPTION` | Opzione cloud | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |

### 5.8 Rete e protocolli

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_SUPPORTED_PROTOCOLS` | Protocolli supportati | Tecnico | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa1_compatibilita · pa1_compatibilita* |
| `PH_PROTOCOL_VERSIONS` | Versioni testate | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa1_compatibilita · pa1_compatibilita* |
| `PH_REQUIRED_PORTS` | Porte richieste | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | p08_architettura* · pa1_compatibilita · pa1_compatibilita* |
| `PH_FLOW_DIRECTIONS` | Direzioni dei flussi | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | — |
| `PH_READ_ONLY_POLICY` | Regola di sola lettura verso le macchine | Tecnico | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | p08_architettura · pa1_compatibilita · pa1_compatibilita* |
| `PH_NETWORK_SEGMENTATION` | Segmentazione di rete richiesta | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_FIREWALL_RULES` | Regole firewall | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_GATEWAY_REQUIREMENTS` | Requisiti del gateway | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa1_compatibilita · pa1_compatibilita* |
| `PH_BANDWIDTH_REQUIREMENT` | Banda richiesta | Tecnico + IT | P2 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_LATENCY_REQUIREMENT` | Latenza richiesta | Tecnico + IT | P2 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_ERP_INTEGRATION_METHODS` | Modalità di integrazione con il gestionale | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p08_architettura* · p12_output* · pa1_compatibilita |
| `PH_API_AVAILABILITY` | Disponibilità delle API | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p12_output* |
| `PH_API_AUTHENTICATION` | Autenticazione delle API | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_EXPORT_FORMATS` | Formati di export | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p12_output* |

### 5.9 Security, dati e licenza

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_AUTHENTICATION_MODEL` | Modello di autenticazione | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa3_governo |
| `PH_ROLE_MODEL` | Modello dei ruoli | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa3_governo |
| `PH_PASSWORD_POLICY` | Politica delle password | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_SSO_SUPPORT` | Supporto SSO | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_AUDIT_LOGGING` | Registro degli accessi | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa3_governo |
| `PH_LOG_RETENTION` | Retention dei log | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_PATCHING_POLICY` | Politica di patching | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa3_governo |
| `PH_VULNERABILITY_POLICY` | Vulnerability management | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_BACKUP_POLICY` | Politica di backup | Tecnico + IT | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa3_governo |
| `PH_BACKUP_FREQUENCY` | Frequenza di backup | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_RPO` | RPO | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa3_governo* |
| `PH_RTO` | RTO | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa3_governo* |
| `PH_DISASTER_RECOVERY` | Disaster recovery | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_DATA_ENCRYPTION_AT_REST` | Cifratura a riposo | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa3_governo |
| `PH_DATA_ENCRYPTION_IN_TRANSIT` | Cifratura in transito | Tecnico + IT | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_DATA_OWNERSHIP` | Proprietà dei dati | Legale | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | p02_overview* · pa3_governo |
| `PH_LICENSE_RIGHTS` | Diritti di licenza | Legale | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa3_governo* |
| `PH_END_OF_CONTRACT_DATA` | Dati a fine contratto | Legale | P0 | `SECTION` | G4 | VALIDAZIONE TECNICA | pa3_governo |
| `PH_END_OF_CONTRACT_ACCESS` | Accesso a fine contratto | Legale | P1 | `NONE` | — | INPUT APERTO | — |
| `PH_DATA_EXPORT_AT_EXIT` | Export a fine rapporto | Legale | P1 | `NONE` | — | INPUT APERTO | pa3_governo* |
| `PH_DATA_DELETION_POLICY` | Cancellazione dei dati | Legale | P1 | `NONE` | — | INPUT APERTO | — |

### 5.10 Dataset illustrativo

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_DATASET_LINE_TYPE` | Tipo di linea dello scenario | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | — |
| `PH_DATASET_VALIDATOR` | Chi ha validato il dataset | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | a5_assunzioni* · v01_cover* |
| `PH_DATASET_VALIDATION_DATE` | Data della validazione | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | a5_assunzioni* · v01_cover* |
| `PH_DATASET_THROUGHPUT` | Pezzi al minuto | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | v11_valore* |
| `PH_DATASET_MARGIN_UNIT` | Margine per pezzo | Commerciale | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | v11_valore* |
| `PH_DATASET_RUNNING_POWER` | Potenza in marcia | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | — |
| `PH_DATASET_STOPPED_POWER` | Potenza a impianto fermo | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | v05_energia* |
| `PH_DATASET_ENERGY_PRICE` | Prezzo dell’energia | Commerciale | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | — |
| `PH_DATASET_EMISSION_FACTOR` | Fattore di emissione | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | — |
| `PH_DATASET_SHIFT_DURATION` | Durata del turno | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | — |
| `PH_DATASET_SHIFTS_PER_YEAR` | Turni produttivi in un anno | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | — |
| `PH_DATASET_STOP_MIN_WEEK` | Minuti di fermo a settimana | Tecnico | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | v11_valore* |
| `PH_DATASET_RECOVERABLE_SHARE` | Quota potenzialmente recuperabile | Commerciale | P0 | `SECTION` | G3 | VALIDAZIONE TECNICA | v11_valore* |
| `PH_DATASET_ASSUMPTION_OWNER` | Owner delle assunzioni | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | a5_assunzioni* |

### 8 Perimetro dei moduli

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_CONNECT_EXACT_SCOPE` | Perimetro esatto di Connect | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p04_connect* |
| `PH_CONNECT_REPORTS` | Report inclusi in Connect | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p04_connect* |
| `PH_CONNECT_ALERTS` | Notifiche e allarmi di Connect | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p04_connect* |
| `PH_INSIGHT_EXACT_SCOPE` | Perimetro esatto di Insight | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p05_insight* |
| `PH_COST_CALCULATION_METHOD` | Metodo di calcolo del costo | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p05_insight* |
| `PH_CO2_METHOD` | Metodo di calcolo della CO₂ | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p05_insight* · p11_energia* |
| `PH_REFYN_MVP_SCOPE` | Perimetro del primo rilascio di Refyn | Tecnico | P1 | `PAGE` | — | VALIDAZIONE TECNICA | p06_refyn · p06_refyn* |
| `PH_REFYN_PILOT_RULES` | Regole di accesso al pilot Refyn | Commerciale | P1 | `PAGE` | — | DECISIONE COMMERCIALE | p06_refyn · p06_refyn* |
| `PH_REFYN_RELEASE_TARGET` | Data obiettivo di rilascio | Direzione | P1 | `NONE` | — | INPUT APERTO | p06_refyn · p06_refyn* |
| `PH_STANDARD_SIGNAL_LIST` | Elenco standard dei segnali | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p07_sorgenti* |
| `PH_SENSOR_ACCURACY_REQUIREMENTS` | Requisiti di precisione della sensoristica | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p07_sorgenti* |
| `PH_METERING_STANDARDS` | Standard di misura adottati | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p07_sorgenti* · pa1_compatibilita |
| `PH_STANDARD_TAG_MODEL` | Modello standard dei tag | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p09_contesto* |
| `PH_CAUSE_VALIDATION_PROCESS` | Processo di validazione della causa | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p09_contesto* |
| `PH_REPORT_CATALOGUE` | Catalogo dei report | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p12_output* |

### 9 Dizionario KPI e definizioni OEE

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_OEE_DEFINITION_OWNER` | Owner della definizione di OEE | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa4_kpi* |
| `PH_OEE_CALENDAR_RULES` | Regole di calendario e tempo pianificato | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p10_oee* |
| `PH_IDEAL_CYCLE_TIME_RULE` | Regola del tempo ciclo ideale | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p10_oee* |
| `PH_GOOD_COUNT_RULE` | Regola del conteggio dei pezzi conformi | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p10_oee* |
| `PH_LINE_OEE_AGGREGATION` | Regola di aggregazione dell’OEE di linea | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p10_oee* |
| `PH_ENERGY_PRICE_SOURCE` | Fonte del prezzo dell’energia | Commerciale | P1 | `NONE` | — | DECISIONE COMMERCIALE | p11_energia* |
| `PH_EMISSION_FACTOR_SOURCE` | Fonte del fattore di emissione | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p11_energia* |
| `PH_COST_ALLOCATION_RULE` | Regola di allocazione del costo | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | p11_energia* |
| `PH_KPI_OWNER` | Owner del dizionario KPI | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa4_kpi · pa4_kpi* |
| `PH_KPI_VERSION` | Versione del dizionario KPI | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa4_kpi · pa4_kpi* |
| `PH_KPI_APPROVAL_DATE` | Data di approvazione del dizionario | Tecnico | P1 | `NONE` | — | VALIDAZIONE TECNICA | pa4_kpi · pa4_kpi* |

### 10 Asset reali

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_REAL_SCREENSHOT_MAPST` | Screenshot reale MAPST 4.0 | Tecnico | P0 | `NONE` | G5 | ASSET RICHIESTO | v04_evento_prodotto* |
| `PH_REAL_SCREENSHOT_MARENERGY` | Screenshot reale MarEnergy | Tecnico | P0 | `NONE` | G5 | ASSET RICHIESTO | v05_energia* |
| `PH_REAL_SCREENSHOT_NEW_UI` | Screenshot della nuova interfaccia | Tecnico | P0 | `NONE` | G5 | ASSET RICHIESTO | v03_categoria* |
| `PH_REAL_REPORT_EXPORT` | Report reale esportato | Tecnico | P0 | `NONE` | G5 | ASSET RICHIESTO | — |
| `PH_REAL_INSTALLATION_PHOTO` | Foto di un’installazione | Marketing | P0 | `NONE` | G5 | ASSET RICHIESTO | — |
| `PH_REAL_LINE_DIAGRAM` | Schema di linea reale anonimizzato | Tecnico | P0 | `NONE` | G5 | ASSET RICHIESTO | — |
| `PH_REAL_SENSOR_PHOTO` | Foto di sensore o contatore | Marketing | P0 | `NONE` | G5 | ASSET RICHIESTO | — |
| `PH_REAL_SERVER_DIAGRAM` | Schema di deployment reale | Tecnico + IT | P0 | `NONE` | G5 | ASSET RICHIESTO | — |

### 5.3 Caso cliente · gate

| id | descrizione | owner | prio | scope | gate | etichetta | canvas |
|---|---|---|:--:|:--:|:--:|---|---|
| `PH_CASE_STUDY_READY` | Caso cliente pronto: servono tutti e otto gli elementi del §3.2 | Legale | P0 | `PAGE` | CASE | INPUT APERTO | v14_caso* |

---

## 3. Distribuzione

| scope | campi | che cosa significa |
|---|--:|---|
| `GLOBAL` | 9 | impedisce la client edition del documento |
| `SECTION` | 40 | esclude una sezione o disattiva un contenuto |
| `PAGE` | 5 | esclude un singolo canvas |
| `NONE` | 167 | non blocca: si pubblica con formulazione prudente |

---

## 4. I campi che bloccano davvero

I 58 P0, per gate. Sono gli unici che tengono ferma una consegna.


**G1 · Identità e CTA** — 9 campi

- `PH_COMPANY_LEGAL_NAME` — Denominazione legale corretta · owner Direzione
- `PH_CONTACT_NAME` — Referente commerciale · owner Commerciale
- `PH_CONTACT_ROLE` — Ruolo del referente · owner Commerciale
- `PH_CONTACT_EMAIL` — Email ufficiale · owner Commerciale
- `PH_AUDIT_NAME` — Nome commerciale del primo passo · owner Commerciale
- `PH_AUDIT_DURATION` — Durata dell’audit · owner Commerciale
- `PH_AUDIT_PARTICIPANTS` — Partecipanti richiesti · owner Commerciale
- `PH_AUDIT_INPUTS` — Materiali richiesti al cliente · owner Tecnico
- `PH_AUDIT_DELIVERABLES` — Output dell’audit · owner Tecnico

**G2 · Modello commerciale** — 10 campi

- `PH_AUDIT_PRICE` — Prezzo dell’audit · owner Commerciale
- `PH_SETUP_FIRST_LINE` — Setup della prima linea · owner Commerciale
- `PH_CONNECT_ANNUAL_FEE` — Canone Connect · owner Commerciale
- `PH_INSIGHT_ANNUAL_FEE` — Canone Insight · owner Commerciale
- `PH_REFYN_PRICING_MODEL` — Modello economico di Refyn · owner Commerciale
- `PH_ADDITIONAL_LINE_FEE` — Canone per linee successive · owner Commerciale
- `PH_SERVICES_INCLUDED` — Servizi compresi nell’avvio · owner Commerciale
- `PH_SERVICES_OPTIONAL` — Servizi opzionali · owner Commerciale
- `PH_CONTRACT_TERM` — Durata contrattuale · owner Commerciale
- `PH_RENEWAL_TERMS` — Condizioni di rinnovo · owner Commerciale

**G3 · Dataset** — 12 campi

- `PH_DATASET_LINE_TYPE` — Tipo di linea dello scenario · owner Tecnico
- `PH_DATASET_VALIDATOR` — Chi ha validato il dataset · owner Tecnico
- `PH_DATASET_VALIDATION_DATE` — Data della validazione · owner Tecnico
- `PH_DATASET_THROUGHPUT` — Pezzi al minuto · owner Tecnico
- `PH_DATASET_MARGIN_UNIT` — Margine per pezzo · owner Commerciale
- `PH_DATASET_RUNNING_POWER` — Potenza in marcia · owner Tecnico
- `PH_DATASET_STOPPED_POWER` — Potenza a impianto fermo · owner Tecnico
- `PH_DATASET_ENERGY_PRICE` — Prezzo dell’energia · owner Commerciale
- `PH_DATASET_SHIFT_DURATION` — Durata del turno · owner Tecnico
- `PH_DATASET_SHIFTS_PER_YEAR` — Turni produttivi in un anno · owner Tecnico
- `PH_DATASET_STOP_MIN_WEEK` — Minuti di fermo a settimana · owner Tecnico
- `PH_DATASET_RECOVERABLE_SHARE` — Quota potenzialmente recuperabile · owner Commerciale

**G4 · Requisiti tecnici minimi** — 18 campi

- `PH_REMOTE_SUPPORT_POLICY` — Politica di supporto remoto · owner Tecnico + IT
- `PH_DEPLOYMENT_MODEL` — On-premise, VM o altro · owner Tecnico + IT
- `PH_SUPPORTED_OS` — Sistemi operativi supportati · owner Tecnico + IT
- `PH_MIN_CPU` — CPU minima · owner Tecnico + IT
- `PH_MIN_RAM` — RAM minima · owner Tecnico + IT
- `PH_MIN_STORAGE` — Storage minimo · owner Tecnico + IT
- `PH_RETENTION_DEFAULT` — Retention di default · owner Tecnico + IT
- `PH_SUPPORTED_PROTOCOLS` — Protocolli supportati · owner Tecnico
- `PH_REQUIRED_PORTS` — Porte richieste · owner Tecnico + IT
- `PH_FLOW_DIRECTIONS` — Direzioni dei flussi · owner Tecnico + IT
- `PH_READ_ONLY_POLICY` — Regola di sola lettura verso le macchine · owner Tecnico
- `PH_AUTHENTICATION_MODEL` — Modello di autenticazione · owner Tecnico + IT
- `PH_ROLE_MODEL` — Modello dei ruoli · owner Tecnico + IT
- `PH_AUDIT_LOGGING` — Registro degli accessi · owner Tecnico + IT
- `PH_BACKUP_POLICY` — Politica di backup · owner Tecnico + IT
- `PH_DATA_OWNERSHIP` — Proprietà dei dati · owner Legale
- `PH_LICENSE_RIGHTS` — Diritti di licenza · owner Legale
- `PH_END_OF_CONTRACT_DATA` — Dati a fine contratto · owner Legale

**G5 · Evidenza commerciale** — 8 campi

- `PH_REAL_SCREENSHOT_MAPST` — Screenshot reale MAPST 4.0 · owner Tecnico
- `PH_REAL_SCREENSHOT_MARENERGY` — Screenshot reale MarEnergy · owner Tecnico
- `PH_REAL_SCREENSHOT_NEW_UI` — Screenshot della nuova interfaccia · owner Tecnico
- `PH_REAL_REPORT_EXPORT` — Report reale esportato · owner Tecnico
- `PH_REAL_INSTALLATION_PHOTO` — Foto di un’installazione · owner Marketing
- `PH_REAL_LINE_DIAGRAM` — Schema di linea reale anonimizzato · owner Tecnico
- `PH_REAL_SENSOR_PHOTO` — Foto di sensore o contatore · owner Marketing
- `PH_REAL_SERVER_DIAGRAM` — Schema di deployment reale · owner Tecnico + IT

**CASE · caso cliente** — 1 campo

- `PH_CASE_STUDY_READY` — servono tutti e otto gli elementi del §20.3