# D.Factory · Registro placeholder V9.1

221 placeholder · **P0 58**, erano 104 nella V9 · P1 156 · P2 7

La differenza con la V9 non è il numero di voci: è che la priorità non è più
un giudizio. **Un campo è P0 se e solo se appartiene a uno dei cinque gate**, o è
il gate del caso cliente. Tutto il resto è utile, e si pubblica con formulazione
prudente.

---

## 1. I cinque gate · §3.1

| Gate | Che cosa blocca | Scope | Campi | Stato | Effetto oggi |
|---|---|:--:|--:|:--:|---|
| **G1** Identità e CTA | la pubblicazione del Sales Deck | `GLOBAL` | 9 | `OPEN` | La CTA resta nella client edition (§9.13) ma senza referente non è inviabile: il deck si presenta dal vivo, non si manda. |
| **G2** Modello commerciale | la definizione completa dell'offerta | `SECTION` | 10 | `OPEN` | L'appendice pricing non entra nella client edition. Il deck mostra la struttura, non gli importi. |
| **G3** Dataset | la pubblicazione del business case | `SECTION` | 12 | `OPEN` | I valori annualizzati escono dalla client edition. Restano la formula, i dati del turno e della settimana, che sono osservati nello scenario. |
| **G4** Requisiti tecnici minimi | la dichiarazione «pronto per IT» | `SECTION` | 18 | `OPEN` | Il dossier resta «preliminare per assessment e solution design». |
| **G5** Evidenza commerciale | l'invio a freddo e il passaggio in procurement | `NONE` | 8 | `OPEN` | Non blocca l'uso dal vivo. Bastano due elementi approvati fra screenshot, report, schema, foto, fatto aziendale, caso cliente. |
| **CASE** caso cliente | la slide 14 | `PAGE` | 1 | `NO` | La slide 14 non entra nella client edition. Gli altri 53 campi del caso scendono a `NONE`: non bloccano nulla, sono il contenuto di una pagina già esclusa. |

**Il caso cliente passa da 28 P0 a uno.** È la riduzione più grande e la più
giusta: non esisteva un modo di chiudere 28 campi separatamente. O il caso è
autorizzato per intero, o la slide non esiste.

### Gli otto elementi che chiudono CASE_STUDY_READY · §3.2

1. autorizzazione
2. cliente o anonimizzazione
3. problema
4. baseline
5. intervento
6. periodo osservato
7. risultato
8. metodologia

Testimonial, logo, fotografia e terzo risultato restano P1: migliorano la slide,
non la abilitano.

---

## 2. BLOCKING_SCOPE

| Scope | Significato | Campi |
|---|---|--:|
| `GLOBAL` | impedisce la client edition del documento | 9 |
| `SECTION` | esclude una sezione o disattiva un contenuto | 40 |
| `PAGE` | esclude un singolo canvas | 5 |
| `NONE` | non blocca: formulazione prudente | 167 |

**Nove campi soltanto sono `GLOBAL`**, e sono tutti di G1: denominazione,
referente, e i cinque campi che definiscono il primo passo commerciale. Sono le
nove risposte che separano un deck presentabile da un deck inviabile.

---

## 3. Il registro


### 5.1 Identità e contatti

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_COMPANY_LEGAL_NAME}}` | Denominazione legale corretta | Direzione | **P0** | `GLOBAL` | G1 | deck 13 · dossier 01 | blocco nascosto | `OPEN` |
| `{{PH_COMPANY_BRAND_FORM}}` | Grafia ufficiale del brand | Marketing | **P1** | `NONE` | — | tutti i canvas | resta la grafia D.Factory in uso | `OPEN` |
| `{{PH_COMPANY_VAT}}` | Partita IVA | Direzione | **P1** | `NONE` | — | piede legale | elemento omesso | `OPEN` |
| `{{PH_COMPANY_ADDRESS}}` | Sede legale o operativa | Direzione | **P1** | `NONE` | — | deck 13 · dossier 01 | elemento omesso | `OPEN` |
| `{{PH_COMPANY_WEBSITE}}` | URL ufficiale | Marketing | **P1** | `NONE` | — | deck 13 | elemento omesso | `OPEN` |
| `{{PH_CONTACT_NAME}}` | Referente commerciale | Commerciale | **P0** | `GLOBAL` | G1 | deck 13 | canvas escluso | `OPEN` |
| `{{PH_CONTACT_ROLE}}` | Ruolo del referente | Commerciale | **P0** | `GLOBAL` | G1 | deck 13 | canvas escluso | `OPEN` |
| `{{PH_CONTACT_EMAIL}}` | Email ufficiale | Commerciale | **P0** | `GLOBAL` | G1 | deck 13 · dossier 01 | canvas escluso | `OPEN` |
| `{{PH_CONTACT_PHONE}}` | Numero di telefono | Commerciale | **P1** | `NONE` | — | deck 13 | elemento omesso | `OPEN` |
| `{{PH_GROUP_RELATIONSHIP}}` | Relazione con Gruppo Clevertech | Direzione | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_LEGAL_FOOTER}}` | Formula legale del piede | Legale | **P1** | `NONE` | — | piede di tutti i canvas | elemento omesso | `OPEN` |
| `{{PH_VERSION_DATE}}` | Data di emissione del documento | Direzione | **P1** | `NONE` | — | dossier 01 | elemento omesso | `OPEN` |

### 5.2 Prova aziendale

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_COMPANY_FOUNDING_YEAR}}` | Anno di avvio | Direzione | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_COMPANY_YEARS_EXPERIENCE}}` | Anni di esperienza | Direzione | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_CLIENTS}}` | Numero clienti attivi | Direzione | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_SITES}}` | Numero stabilimenti | Tecnico | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_LINES}}` | Numero linee collegate | Tecnico | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_MACHINES}}` | Numero macchine collegate | Tecnico | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_PROJECTS_COMPLETED}}` | Numero progetti o casi conclusi | Direzione | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_SECTORS_APPROVED}}` | Settori autorizzati alla citazione | Legale | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_RETENTION_METRIC}}` | Retention o tasso di rinnovo | Direzione | **P2** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_TEAM_SIZE}}` | Dimensione del team dedicato | Direzione | **P2** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_GROUP_PROOF}}` | Evidenza del gruppo industriale | Direzione | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_PARTNERSHIP_SIEMENS_APPROVAL}}` | Claim di partnership autorizzato | Legale | **P1** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |
| `{{PH_SAP_INTEGRATION_PROOF}}` | Fonte verificabile per il claim ERP | Tecnico | **P1** | `NONE` | — | deck A4 · dossier 12 | elemento omesso | `OPEN` |
| `{{PH_PATENT_BOX_APPROVAL}}` | Claim Patent Box autorizzato | Legale | **P2** | `NONE` | — | deck 10 | elemento omesso | `OPEN` |

### 5.3 Caso cliente · identificativi

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_CASE_CLIENT_DISPLAY_NAME}}` | Nome cliente o forma anonima | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CLIENT_LEGAL_NAME}}` | Nome legale, uso interno | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CLIENT_SECTOR}}` | Settore | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CLIENT_SITE}}` | Stabilimento o paese | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_LINE_TYPE}}` | Tipo di linea | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PROCESS}}` | Processo osservato | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CONFIDENTIALITY}}` | Pubblico, anonimo o confidenziale | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_APPROVAL_STATUS}}` | Stato autorizzazione alla pubblicazione | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_APPROVAL_OWNER}}` | Chi ha autorizzato | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |

### 5.3 Caso cliente · problema e contesto

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_CASE_INITIAL_PROBLEM}}` | Problema iniziale | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_BUSINESS_IMPACT}}` | Impatto percepito dal cliente | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_BASELINE_PERIOD}}` | Periodo della baseline | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_BASELINE_DATA}}` | Dati della baseline | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_DATA_SOURCES}}` | PLC, contatori, gestionale, sensori | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_SCOPE}}` | Macchine, linea, sito | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PRECONDITIONS}}` | Prerequisiti presenti | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_GAPS}}` | Gap di dati o di misura | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |

### 5.3 Caso cliente · intervento

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_CASE_SOLUTION_MODULE}}` | Connect, Insight o Refyn | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_IMPLEMENTATION_SCOPE}}` | Perimetro implementato | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_INTERVENTION}}` | Attività svolte | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_ADDED_SENSORS}}` | Sensori o contatori aggiunti | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_ERP_INTEGRATION}}` | Integrazione con il gestionale | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_TIME_TO_FIRST_SIGNAL}}` | Tempo al primo segnale | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_TIME_TO_USABLE_DATA}}` | Tempo al dato utilizzabile | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PILOT_DURATION}}` | Durata del pilot | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_USERS}}` | Utenti coinvolti | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |

### 5.3 Caso cliente · risultati

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_CASE_RESULT_1_LABEL}}` | Nome del risultato 1 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_BASELINE}}` | Baseline del risultato 1 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_AFTER}}` | Valore dopo, risultato 1 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_UNIT}}` | Unità di misura, risultato 1 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_METHOD}}` | Metodo di misura, risultato 1 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_LABEL}}` | Nome del risultato 2 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_BASELINE}}` | Baseline del risultato 2 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_AFTER}}` | Valore dopo, risultato 2 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_UNIT}}` | Unità di misura, risultato 2 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_METHOD}}` | Metodo di misura, risultato 2 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_LABEL}}` | Nome del risultato 3 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_BASELINE}}` | Baseline del risultato 3 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_AFTER}}` | Valore dopo, risultato 3 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_UNIT}}` | Unità di misura, risultato 3 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_METHOD}}` | Metodo di misura, risultato 3 | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_PERIOD}}` | Periodo osservato | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_ANNUALIZED_VALUE}}` | Valore annualizzato | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PAYBACK}}` | Payback verificato | Commerciale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CONFIDENCE_NOTE}}` | Limiti e attendibilità della misura | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |

### 5.3 Caso cliente · testimonial e asset

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_CASE_QUOTE}}` | Citazione del cliente | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_QUOTE_AUTHOR}}` | Autore della citazione | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_QUOTE_ROLE}}` | Ruolo dell’autore | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_QUOTE_APPROVAL}}` | Autorizzazione alla citazione | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_LOGO_ASSET}}` | Logo cliente autorizzato | Legale | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_SCREENSHOT_ASSET}}` | Screenshot reale del caso | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PHOTO_ASSET}}` | Foto reale del caso | Marketing | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_DIAGRAM_ASSET}}` | Schema anonimizzato del caso | Tecnico | **P1** | `NONE` | — | deck 14 | slide 14 esclusa | `OPEN` |

### 5.4 Audit e pilot

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_AUDIT_NAME}}` | Nome commerciale del primo passo | Commerciale | **P0** | `GLOBAL` | G1 | deck 12 · 13 · A3 | testo prudente | `OPEN` |
| `{{PH_AUDIT_DURATION}}` | Durata dell’audit | Commerciale | **P0** | `GLOBAL` | G1 | deck 09 · 12 | elemento omesso | `OPEN` |
| `{{PH_AUDIT_PRICE}}` | Prezzo dell’audit | Commerciale | **P0** | `SECTION` | G2 | deck 12 · A3 | canvas escluso | `OPEN` |
| `{{PH_AUDIT_CREDIT_POLICY}}` | Accredito dell’audit sul progetto | Commerciale | **P1** | `NONE` | — | deck A3 | elemento omesso | `OPEN` |
| `{{PH_AUDIT_PARTICIPANTS}}` | Partecipanti richiesti | Commerciale | **P0** | `GLOBAL` | G1 | deck 13 | resta la formulazione V8, già verificata | `OPEN` |
| `{{PH_AUDIT_CLIENT_HOURS}}` | Ore richieste al cliente | Commerciale | **P1** | `NONE` | — | deck 13 | elemento omesso | `OPEN` |
| `{{PH_AUDIT_INPUTS}}` | Materiali richiesti al cliente | Tecnico | **P0** | `GLOBAL` | G1 | deck 13 | resta la formulazione V8, già verificata | `OPEN` |
| `{{PH_AUDIT_DELIVERABLES}}` | Output dell’audit | Tecnico | **P0** | `GLOBAL` | G1 | deck 13 | resta la formulazione V8, già verificata | `OPEN` |
| `{{PH_AUDIT_VALIDITY}}` | Validità dell’offerta | Commerciale | **P1** | `NONE` | — | deck A3 | elemento omesso | `OPEN` |
| `{{PH_PILOT_DURATION}}` | Durata del pilot | Commerciale | **P1** | `NONE` | — | deck 12 · dossier 13 | elemento omesso | `OPEN` |
| `{{PH_PILOT_SCOPE}}` | Perimetro del pilot | Tecnico | **P1** | `NONE` | — | deck 12 · dossier 13 | resta «una linea», già dichiarato | `OPEN` |
| `{{PH_PILOT_SUCCESS_CRITERIA}}` | Criteri di successo | Tecnico | **P1** | `NONE` | — | deck 12 · dossier 13 | restano i criteri di uscita V8 | `OPEN` |
| `{{PH_PILOT_EXIT_CRITERIA}}` | Criteri di uscita | Tecnico | **P1** | `NONE` | — | deck 12 · dossier 13 | restano i criteri di uscita V8 | `OPEN` |
| `{{PH_PILOT_PRICE}}` | Prezzo del pilot | Commerciale | **P1** | `PAGE` | — | deck 12 · A3 | canvas escluso | `OPEN` |
| `{{PH_PILOT_CONVERSION_POLICY}}` | Conversione del pilot a contratto | Commerciale | **P1** | `NONE` | — | deck 12 | elemento omesso | `OPEN` |
| `{{PH_PILOT_REVERSIBILITY}}` | Reversibilità del pilot | Commerciale | **P1** | `NONE` | — | deck 12 | elemento omesso | `OPEN` |

### 5.5 Pricing e contratto

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_SITE_BASE_FEE}}` | Canone base per sito | Commerciale | **P1** | `PAGE` | — | deck 12 · A3 | canvas escluso | `OPEN` |
| `{{PH_SETUP_FIRST_LINE}}` | Setup della prima linea | Commerciale | **P0** | `SECTION` | G2 | deck A3 | canvas escluso | `OPEN` |
| `{{PH_CONNECT_ANNUAL_FEE}}` | Canone Connect | Commerciale | **P0** | `SECTION` | G2 | deck 12 · A3 | canvas escluso | `OPEN` |
| `{{PH_INSIGHT_ANNUAL_FEE}}` | Canone Insight | Commerciale | **P0** | `SECTION` | G2 | deck 12 · A3 | canvas escluso | `OPEN` |
| `{{PH_REFYN_PRICING_MODEL}}` | Modello economico di Refyn | Commerciale | **P0** | `SECTION` | G2 | deck 09 · 12 · A1 · A3 · dossier 03 | canvas escluso | `OPEN` |
| `{{PH_ADDITIONAL_LINE_FEE}}` | Canone per linee successive | Commerciale | **P0** | `SECTION` | G2 | deck A3 | canvas escluso | `OPEN` |
| `{{PH_SENSOR_PRICING_RULE}}` | Regola di quotazione della sensoristica | Commerciale | **P1** | `NONE` | — | deck A3 · dossier 07 | elemento omesso | `OPEN` |
| `{{PH_SERVICES_INCLUDED}}` | Servizi compresi nell’avvio | Commerciale | **P0** | `SECTION` | G2 | deck 08 · A1 · A2 · dossier 03 · 14 | elemento omesso | `OPEN` |
| `{{PH_SERVICES_OPTIONAL}}` | Servizi opzionali | Commerciale | **P0** | `SECTION` | G2 | deck 08 · A2 · dossier 14 | elemento omesso | `OPEN` |
| `{{PH_PERFORMANCE_REVIEW_FEE}}` | Prezzo della performance review | Commerciale | **P1** | `NONE` | — | deck A3 | canvas escluso | `OPEN` |
| `{{PH_ENERGY_REVIEW_FEE}}` | Prezzo della energy review | Commerciale | **P1** | `NONE` | — | deck A3 | canvas escluso | `OPEN` |
| `{{PH_PREMIUM_SUPPORT_FEE}}` | Prezzo del supporto premium | Commerciale | **P1** | `NONE` | — | deck A3 | canvas escluso | `OPEN` |
| `{{PH_CONTRACT_TERM}}` | Durata contrattuale | Commerciale | **P0** | `SECTION` | G2 | deck 09 · A3 | elemento omesso | `OPEN` |
| `{{PH_RENEWAL_TERMS}}` | Condizioni di rinnovo | Commerciale | **P0** | `SECTION` | G2 | deck A3 | canvas escluso | `OPEN` |
| `{{PH_TERMINATION_TERMS}}` | Condizioni di recesso | Legale | **P1** | `NONE` | — | deck A3 | canvas escluso | `OPEN` |
| `{{PH_PAYMENT_TERMS}}` | Termini di pagamento | Commerciale | **P1** | `NONE` | — | deck A3 | canvas escluso | `OPEN` |
| `{{PH_PRICE_VALIDITY}}` | Validità dei prezzi | Commerciale | **P1** | `NONE` | — | deck A3 | canvas escluso | `OPEN` |
| `{{PH_INDEXATION}}` | Indicizzazione | Commerciale | **P2** | `NONE` | — | deck A3 | canvas escluso | `OPEN` |

### 5.6 Supporto e SLA

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_SUPPORT_HOURS}}` | Orari del supporto | Commerciale | **P1** | `NONE` | — | deck A2 · dossier 14 | elemento omesso | `OPEN` |
| `{{PH_SUPPORT_CHANNELS}}` | Canali del supporto | Commerciale | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_SLA_SEVERITY_LEVELS}}` | Livelli di severità | Tecnico | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_SLA_RESPONSE_TIMES}}` | Tempi di risposta | Commerciale | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_SLA_RESOLUTION_TARGETS}}` | Obiettivi di risoluzione | Commerciale | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_ESCALATION_PROCESS}}` | Processo di escalation | Tecnico | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_MAINTENANCE_WINDOWS}}` | Finestre di manutenzione | Tecnico | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_UPDATE_POLICY}}` | Politica di aggiornamento | Tecnico | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_CHANGE_REQUEST_POLICY}}` | Politica delle change request | Commerciale | **P1** | `NONE` | — | dossier 14 | elemento omesso | `OPEN` |
| `{{PH_REMOTE_SUPPORT_POLICY}}` | Politica di supporto remoto | Tecnico + IT | **P0** | `SECTION` | G4 | dossier 14 · A3 | elemento omesso | `OPEN` |

### 5.7 Deployment e infrastruttura

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_DEPLOYMENT_MODEL}}` | On-premise, VM o altro | Tecnico + IT | **P0** | `SECTION` | G4 | dossier 02 · 08 · A2 | testo prudente | `OPEN` |
| `{{PH_SERVER_OWNER}}` | Proprietà dell’ambiente | Tecnico + IT | **P1** | `NONE` | — | dossier 08 · A2 | testo prudente | `OPEN` |
| `{{PH_SUPPORTED_OS}}` | Sistemi operativi supportati | Tecnico + IT | **P0** | `SECTION` | G4 | dossier 08 · A2 | elemento omesso | `OPEN` |
| `{{PH_MIN_CPU}}` | CPU minima | Tecnico + IT | **P0** | `SECTION` | G4 | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_MIN_RAM}}` | RAM minima | Tecnico + IT | **P0** | `SECTION` | G4 | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_MIN_STORAGE}}` | Storage minimo | Tecnico + IT | **P0** | `SECTION` | G4 | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_STORAGE_GROWTH_RULE}}` | Regola di crescita dello storage | Tecnico + IT | **P1** | `NONE` | — | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_RETENTION_DEFAULT}}` | Retention di default | Tecnico + IT | **P0** | `SECTION` | G4 | dossier A2 · A3 | elemento omesso | `OPEN` |
| `{{PH_HIGH_AVAILABILITY}}` | Alta disponibilità | Tecnico + IT | **P1** | `NONE` | — | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_VIRTUALIZATION_SUPPORT}}` | Virtualizzazione supportata | Tecnico + IT | **P1** | `NONE` | — | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_CONTAINER_SUPPORT}}` | Container supportati | Tecnico + IT | **P2** | `NONE` | — | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_TIME_SYNC_REQUIREMENT}}` | Requisito di sincronizzazione oraria | Tecnico + IT | **P1** | `NONE` | — | dossier 09 | elemento omesso | `OPEN` |
| `{{PH_INTERNET_REQUIREMENT}}` | Accesso a internet richiesto | Tecnico + IT | **P1** | `NONE` | — | dossier 08 | elemento omesso | `OPEN` |
| `{{PH_CLOUD_OPTION}}` | Opzione cloud | Tecnico + IT | **P1** | `NONE` | — | dossier 02 · 08 | elemento omesso | `OPEN` |

### 5.8 Rete e protocolli

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_SUPPORTED_PROTOCOLS}}` | Protocolli supportati | Tecnico | **P0** | `SECTION` | G4 | dossier 08 · A1 | elemento omesso | `OPEN` |
| `{{PH_PROTOCOL_VERSIONS}}` | Versioni testate | Tecnico | **P1** | `NONE` | — | dossier A1 | elemento omesso | `OPEN` |
| `{{PH_REQUIRED_PORTS}}` | Porte richieste | Tecnico + IT | **P0** | `SECTION` | G4 | dossier 08 · A1 | elemento omesso | `OPEN` |
| `{{PH_FLOW_DIRECTIONS}}` | Direzioni dei flussi | Tecnico + IT | **P0** | `SECTION` | G4 | dossier 08 | resta lo schema logico V8 | `OPEN` |
| `{{PH_READ_ONLY_POLICY}}` | Regola di sola lettura verso le macchine | Tecnico | **P0** | `SECTION` | G4 | dossier 08 · A1 | testo prudente | `OPEN` |
| `{{PH_NETWORK_SEGMENTATION}}` | Segmentazione di rete richiesta | Tecnico + IT | **P1** | `NONE` | — | dossier 08 | elemento omesso | `OPEN` |
| `{{PH_FIREWALL_RULES}}` | Regole firewall | Tecnico + IT | **P1** | `NONE` | — | dossier 08 · A1 | elemento omesso | `OPEN` |
| `{{PH_GATEWAY_REQUIREMENTS}}` | Requisiti del gateway | Tecnico | **P1** | `NONE` | — | dossier A1 | elemento omesso | `OPEN` |
| `{{PH_BANDWIDTH_REQUIREMENT}}` | Banda richiesta | Tecnico + IT | **P2** | `NONE` | — | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_LATENCY_REQUIREMENT}}` | Latenza richiesta | Tecnico + IT | **P2** | `NONE` | — | dossier A2 | elemento omesso | `OPEN` |
| `{{PH_ERP_INTEGRATION_METHODS}}` | Modalità di integrazione con il gestionale | Tecnico | **P1** | `NONE` | — | dossier 08 · 12 | testo prudente | `OPEN` |
| `{{PH_API_AVAILABILITY}}` | Disponibilità delle API | Tecnico | **P1** | `NONE` | — | dossier 12 | elemento omesso | `OPEN` |
| `{{PH_API_AUTHENTICATION}}` | Autenticazione delle API | Tecnico + IT | **P1** | `NONE` | — | dossier 12 | elemento omesso | `OPEN` |
| `{{PH_EXPORT_FORMATS}}` | Formati di export | Tecnico | **P1** | `NONE` | — | dossier 12 | restano i formati già dichiarati | `OPEN` |

### 5.9 Security, dati e licenza

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_AUTHENTICATION_MODEL}}` | Modello di autenticazione | Tecnico + IT | **P0** | `SECTION` | G4 | dossier 08 · A3 | elemento omesso | `OPEN` |
| `{{PH_ROLE_MODEL}}` | Modello dei ruoli | Tecnico + IT | **P0** | `SECTION` | G4 | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_PASSWORD_POLICY}}` | Politica delle password | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_SSO_SUPPORT}}` | Supporto SSO | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_AUDIT_LOGGING}}` | Registro degli accessi | Tecnico + IT | **P0** | `SECTION` | G4 | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_LOG_RETENTION}}` | Retention dei log | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_PATCHING_POLICY}}` | Politica di patching | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_VULNERABILITY_POLICY}}` | Vulnerability management | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_BACKUP_POLICY}}` | Politica di backup | Tecnico + IT | **P0** | `SECTION` | G4 | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_BACKUP_FREQUENCY}}` | Frequenza di backup | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_RPO}}` | RPO | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_RTO}}` | RTO | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_DISASTER_RECOVERY}}` | Disaster recovery | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_DATA_ENCRYPTION_AT_REST}}` | Cifratura a riposo | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_DATA_ENCRYPTION_IN_TRANSIT}}` | Cifratura in transito | Tecnico + IT | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_DATA_OWNERSHIP}}` | Proprietà dei dati | Legale | **P0** | `SECTION` | G4 | dossier 02 · A3 | testo prudente | `OPEN` |
| `{{PH_LICENSE_RIGHTS}}` | Diritti di licenza | Legale | **P0** | `SECTION` | G4 | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_END_OF_CONTRACT_DATA}}` | Dati a fine contratto | Legale | **P0** | `SECTION` | G4 | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_END_OF_CONTRACT_ACCESS}}` | Accesso a fine contratto | Legale | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_DATA_EXPORT_AT_EXIT}}` | Export a fine rapporto | Legale | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |
| `{{PH_DATA_DELETION_POLICY}}` | Cancellazione dei dati | Legale | **P1** | `NONE` | — | dossier A3 | elemento omesso | `OPEN` |

### 5.10 Dataset illustrativo

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_DATASET_LINE_TYPE}}` | Tipo di linea dello scenario | Tecnico | **P0** | `SECTION` | G3 | deck 01 · 11 · A5 | resta «linea di confezionamento» | `OPEN` |
| `{{PH_DATASET_VALIDATOR}}` | Chi ha validato il dataset | Tecnico | **P0** | `SECTION` | G3 | deck 01 · A5 | elemento omesso | `OPEN` |
| `{{PH_DATASET_VALIDATION_DATE}}` | Data della validazione | Tecnico | **P0** | `SECTION` | G3 | deck 01 · A5 | elemento omesso | `OPEN` |
| `{{PH_DATASET_THROUGHPUT}}` | Pezzi al minuto | Tecnico | **P0** | `SECTION` | G3 | deck 11 · A5 | resta 500 pz/min, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_MARGIN_UNIT}}` | Margine per pezzo | Commerciale | **P0** | `SECTION` | G3 | deck 11 · A5 | resta 0,14 €/pz, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_RUNNING_POWER}}` | Potenza in marcia | Tecnico | **P0** | `SECTION` | G3 | deck 11 · A5 | resta 95 kW, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_STOPPED_POWER}}` | Potenza a impianto fermo | Tecnico | **P0** | `SECTION` | G3 | deck 11 · A5 | resta 38 kW, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_ENERGY_PRICE}}` | Prezzo dell’energia | Commerciale | **P0** | `SECTION` | G3 | deck A5 | resta 0,22 €/kWh, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_EMISSION_FACTOR}}` | Fattore di emissione | Tecnico | **P1** | `NONE` | — | deck A5 | resta 0,35 kgCO₂e/kWh, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_SHIFT_DURATION}}` | Durata del turno | Tecnico | **P0** | `SECTION` | G3 | deck A5 | resta 480 min, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_SHIFTS_PER_YEAR}}` | Turni produttivi in un anno | Tecnico | **P0** | `SECTION` | G3 | deck A5 | resta 230, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_STOP_MIN_WEEK}}` | Minuti di fermo a settimana | Tecnico | **P0** | `SECTION` | G3 | deck 11 · A5 | resta 96 min, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_RECOVERABLE_SHARE}}` | Quota potenzialmente recuperabile | Commerciale | **P0** | `SECTION` | G3 | deck 11 | resta la metà, dichiarata ipotesi | `OPEN` |
| `{{PH_DATASET_ASSUMPTION_OWNER}}` | Owner delle assunzioni | Commerciale | **P1** | `NONE` | — | deck A5 | elemento omesso | `OPEN` |

### 8 Perimetro dei moduli

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_CONNECT_EXACT_SCOPE}}` | Perimetro esatto di Connect | Tecnico | **P1** | `NONE` | — | dossier 04 | resta il perimetro già dichiarato | `OPEN` |
| `{{PH_CONNECT_REPORTS}}` | Report inclusi in Connect | Tecnico | **P1** | `NONE` | — | dossier 04 | elemento omesso | `OPEN` |
| `{{PH_CONNECT_ALERTS}}` | Notifiche e allarmi di Connect | Tecnico | **P1** | `NONE` | — | dossier 04 | elemento omesso | `OPEN` |
| `{{PH_INSIGHT_EXACT_SCOPE}}` | Perimetro esatto di Insight | Tecnico | **P1** | `NONE` | — | dossier 05 | resta il perimetro già dichiarato | `OPEN` |
| `{{PH_COST_CALCULATION_METHOD}}` | Metodo di calcolo del costo | Tecnico | **P1** | `NONE` | — | dossier 05 · 11 | resta il metodo già scritto in A4 | `OPEN` |
| `{{PH_CO2_METHOD}}` | Metodo di calcolo della CO₂ | Tecnico | **P1** | `NONE` | — | dossier 05 · 11 | resta «CO₂ calcolata o stimata» | `OPEN` |
| `{{PH_REFYN_MVP_SCOPE}}` | Perimetro del primo rilascio di Refyn | Tecnico | **P1** | `PAGE` | — | dossier 06 | blocco nascosto | `OPEN` |
| `{{PH_REFYN_PILOT_RULES}}` | Regole di accesso al pilot Refyn | Commerciale | **P1** | `PAGE` | — | dossier 06 | blocco nascosto | `OPEN` |
| `{{PH_REFYN_RELEASE_TARGET}}` | Data obiettivo di rilascio | Direzione | **P1** | `NONE` | — | dossier 06 | blocco nascosto | `OPEN` |
| `{{PH_STANDARD_SIGNAL_LIST}}` | Elenco standard dei segnali | Tecnico | **P1** | `NONE` | — | dossier 07 | elemento omesso | `OPEN` |
| `{{PH_SENSOR_ACCURACY_REQUIREMENTS}}` | Requisiti di precisione della sensoristica | Tecnico | **P1** | `NONE` | — | dossier 07 | elemento omesso | `OPEN` |
| `{{PH_METERING_STANDARDS}}` | Standard di misura adottati | Tecnico | **P1** | `NONE` | — | dossier 07 | elemento omesso | `OPEN` |
| `{{PH_STANDARD_TAG_MODEL}}` | Modello standard dei tag | Tecnico | **P1** | `NONE` | — | dossier 09 | restano i sette attributi | `OPEN` |
| `{{PH_CAUSE_VALIDATION_PROCESS}}` | Processo di validazione della causa | Tecnico | **P1** | `NONE` | — | dossier 09 | resta «validata da chi la conosce» | `OPEN` |
| `{{PH_REPORT_CATALOGUE}}` | Catalogo dei report | Tecnico | **P1** | `NONE` | — | dossier 12 | elemento omesso | `OPEN` |

### 9 Dizionario KPI e definizioni OEE

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_OEE_DEFINITION_OWNER}}` | Owner della definizione di OEE | Tecnico | **P1** | `NONE` | — | dossier 10 · A4 | elemento omesso | `OPEN` |
| `{{PH_OEE_CALENDAR_RULES}}` | Regole di calendario e tempo pianificato | Tecnico | **P1** | `NONE` | — | dossier 10 · A4 | resta «si concordano prima del go-live» | `OPEN` |
| `{{PH_IDEAL_CYCLE_TIME_RULE}}` | Regola del tempo ciclo ideale | Tecnico | **P1** | `NONE` | — | dossier 10 · A4 | resta la formula di A4 | `OPEN` |
| `{{PH_GOOD_COUNT_RULE}}` | Regola del conteggio dei pezzi conformi | Tecnico | **P1** | `NONE` | — | dossier 10 · A4 | resta la formula di A4 | `OPEN` |
| `{{PH_LINE_OEE_AGGREGATION}}` | Regola di aggregazione dell’OEE di linea | Tecnico | **P1** | `NONE` | — | dossier 10 | resta «collo di bottiglia» | `OPEN` |
| `{{PH_ENERGY_PRICE_SOURCE}}` | Fonte del prezzo dell’energia | Commerciale | **P1** | `NONE` | — | dossier 11 | resta «contratto di fornitura» | `OPEN` |
| `{{PH_EMISSION_FACTOR_SOURCE}}` | Fonte del fattore di emissione | Tecnico | **P1** | `NONE` | — | dossier 11 | resta «mix dichiarato» | `OPEN` |
| `{{PH_COST_ALLOCATION_RULE}}` | Regola di allocazione del costo | Tecnico | **P1** | `NONE` | — | dossier 11 | elemento omesso | `OPEN` |
| `{{PH_KPI_OWNER}}` | Owner del dizionario KPI | Tecnico | **P1** | `NONE` | — | dossier A4 | elemento omesso | `OPEN` |
| `{{PH_KPI_VERSION}}` | Versione del dizionario KPI | Tecnico | **P1** | `NONE` | — | dossier A4 | elemento omesso | `OPEN` |
| `{{PH_KPI_APPROVAL_DATE}}` | Data di approvazione del dizionario | Tecnico | **P1** | `NONE` | — | dossier A4 | elemento omesso | `OPEN` |

### 10 Asset reali

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_REAL_SCREENSHOT_MAPST}}` | Screenshot reale MAPST 4.0 | Tecnico | **P0** | `NONE` | G5 | deck 04 · dossier 04 | resta la vista ricostruita dichiarata | `OPEN` |
| `{{PH_REAL_SCREENSHOT_MARENERGY}}` | Screenshot reale MarEnergy | Tecnico | **P0** | `NONE` | G5 | deck 05 · dossier 11 | resta la vista ricostruita dichiarata | `OPEN` |
| `{{PH_REAL_SCREENSHOT_NEW_UI}}` | Screenshot della nuova interfaccia | Tecnico | **P0** | `NONE` | G5 | deck 03 · dossier 04 | resta la vista ricostruita dichiarata | `OPEN` |
| `{{PH_REAL_REPORT_EXPORT}}` | Report reale esportato | Tecnico | **P0** | `NONE` | G5 | dossier 12 | elemento omesso | `OPEN` |
| `{{PH_REAL_INSTALLATION_PHOTO}}` | Foto di un’installazione | Marketing | **P0** | `NONE` | G5 | deck 10 · dossier 01 | elemento omesso | `OPEN` |
| `{{PH_REAL_LINE_DIAGRAM}}` | Schema di linea reale anonimizzato | Tecnico | **P0** | `NONE` | G5 | dossier 07 | resta lo schema tipo dichiarato | `OPEN` |
| `{{PH_REAL_SENSOR_PHOTO}}` | Foto di sensore o contatore | Marketing | **P0** | `NONE` | G5 | dossier 07 | elemento omesso | `OPEN` |
| `{{PH_REAL_SERVER_DIAGRAM}}` | Schema di deployment reale | Tecnico + IT | **P0** | `NONE` | G5 | dossier 08 | resta lo schema logico dichiarato | `OPEN` |

### 5.3 Caso cliente · gate

| ID | Descrizione | Owner | Pri | Scope | Gate | Canvas | Client edition | Stato |
|---|---|---|:--:|:--:|:--:|---|---|:--:|
| `{{PH_CASE_STUDY_READY}}` | Caso cliente pronto: servono tutti e otto gli elementi del §3.2 | Legale | **P0** | `PAGE` | CASE | deck 14 | slide 14 esclusa finché non è APPROVED | `NO` |


---

## 4. Che cosa contiene la client edition di oggi

| documento | canvas | esclusi | gate responsabile |
|---|--:|---|---|
| Sales Deck | **17** | slide 14 caso cliente · appendice A3 pricing | `CASE` · `G2` |
| Dossier | **18** | nessuno | — |

**La CTA è tornata.** Nella V9 era esclusa perché il contatto manca; il §9.13
dice di tenerla e ha ragione: una CTA senza referente resta una CTA, un deck
senza CTA non è un deck. Il deck client-facing ha di nuovo **13 slide di corpo**
e 4 appendici.

Quello che G1 aperto comporta è scritto in `DFactory_QA_Report_v9_1.md`: il deck
si presenta dal vivo, non si invia.

