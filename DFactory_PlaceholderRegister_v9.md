# D.Factory · Registro placeholder V9

220 placeholder dichiarati · **P0 104** · P1 109 · P2 7 · tutti in stato `OPEN` al 2026-08-03.

Questo file è la fonte unica. Il build lo legge per verificare che ogni
`{{PH_...}}` presente negli HTML sia dichiarato qui, e la client edition lo legge
per sapere che cosa nascondere. Se un placeholder non è in questa tabella, il
build fallisce.

---

## Come si legge

| campo | che cosa dice |
|---|---|
| **ID** | il token da usare negli HTML, sintassi `{{PH_NOME}}` |
| **Owner** | chi può chiudere l'input, non chi lo trascrive |
| **Fonte richiesta** | il documento da cui il valore deve arrivare, non l'opinione |
| **Priorità** | P0 blocca la pubblicazione · P1 riduce credibilità · P2 miglioramento |
| **Working** | che cosa si vede nella working edition |
| **Client** | che cosa succede nella client edition finché lo stato è `OPEN` |

Stati ammessi: `OPEN` · `IN REVIEW` · `APPROVED` · `REJECTED` · `NOT NEEDED`.

**Regola di chiusura.** Uno stato passa ad `APPROVED` solo con la fonte
richiesta allegata. Un valore comunicato a voce resta `IN REVIEW`.

---

## Dove si concentra il lavoro

| owner | P0 | P1 | P2 | totale |
|---|---:|---:|---:|---:|
| Tecnico | 45 | 46 | 0 | 91 |
| Commerciale | 30 | 21 | 1 | 52 |
| Tecnico + IT | 18 | 17 | 3 | 38 |
| Legale | 9 | 11 | 1 | 21 |
| Direzione | 1 | 10 | 2 | 13 |
| Marketing | 1 | 4 | 0 | 5 |

| documento | P0 | P1 | P2 | totale |
|---|---:|---:|---:|---:|
| deck | 58 | 48 | 4 | 110 |
| dossier | 35 | 51 | 3 | 89 |
| entrambi | 11 | 10 | 0 | 21 |

**Il caso cliente da solo vale 53 placeholder, di cui 28 P0.** È il blocco più
grande del registro e il più semplice da valutare: o esiste un caso autorizzato per
iscritto, o la slide 14 non esiste. Non c'è una via di mezzo che non sia inventare.

---


## 5.1 Identità e contatti

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_COMPANY_LEGAL_NAME}}` | Denominazione legale corretta | Direzione | visura o carta intestata | **P0** | entrambi | deck 13 · dossier 01 | visibile | blocco nascosto | `OPEN` |
| `{{PH_COMPANY_BRAND_FORM}}` | Grafia ufficiale del brand | Marketing | manuale di identità | **P0** | entrambi | tutti i canvas | visibile | resta la grafia D.Factory in uso | `OPEN` |
| `{{PH_COMPANY_VAT}}` | Partita IVA | Direzione | visura | **P1** | entrambi | piede legale | visibile | elemento omesso | `OPEN` |
| `{{PH_COMPANY_ADDRESS}}` | Sede legale o operativa | Direzione | visura | **P1** | entrambi | deck 13 · dossier 01 | visibile | elemento omesso | `OPEN` |
| `{{PH_COMPANY_WEBSITE}}` | URL ufficiale | Marketing | conferma marketing | **P1** | entrambi | deck 13 | visibile | elemento omesso | `OPEN` |
| `{{PH_CONTACT_NAME}}` | Referente commerciale | Commerciale | nomina interna | **P0** | deck | deck 13 | visibile | canvas escluso | `OPEN` |
| `{{PH_CONTACT_ROLE}}` | Ruolo del referente | Commerciale | nomina interna | **P0** | deck | deck 13 | visibile | canvas escluso | `OPEN` |
| `{{PH_CONTACT_EMAIL}}` | Email ufficiale | Commerciale | nomina interna | **P0** | entrambi | deck 13 · dossier 01 | visibile | canvas escluso | `OPEN` |
| `{{PH_CONTACT_PHONE}}` | Numero di telefono | Commerciale | nomina interna | **P1** | deck | deck 13 | visibile | elemento omesso | `OPEN` |
| `{{PH_GROUP_RELATIONSHIP}}` | Relazione con Gruppo Clevertech | Direzione | conferma societaria | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_LEGAL_FOOTER}}` | Formula legale del piede | Legale | ufficio legale | **P1** | entrambi | piede di tutti i canvas | visibile | elemento omesso | `OPEN` |
| `{{PH_VERSION_DATE}}` | Data di emissione del documento | Direzione | processo interno | **P1** | dossier | dossier 01 | visibile | elemento omesso | `OPEN` |

## 5.2 Prova aziendale

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_COMPANY_FOUNDING_YEAR}}` | Anno di avvio | Direzione | visura | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_COMPANY_YEARS_EXPERIENCE}}` | Anni di esperienza | Direzione | conferma direzione | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_CLIENTS}}` | Numero clienti attivi | Direzione | CRM validato | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_SITES}}` | Numero stabilimenti | Tecnico | installato validato | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_LINES}}` | Numero linee collegate | Tecnico | installato validato | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_ACTIVE_MACHINES}}` | Numero macchine collegate | Tecnico | installato validato | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_PROJECTS_COMPLETED}}` | Numero progetti o casi conclusi | Direzione | CRM validato | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_SECTORS_APPROVED}}` | Settori autorizzati alla citazione | Legale | autorizzazione clienti | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_RETENTION_METRIC}}` | Retention o tasso di rinnovo | Direzione | contratti | **P2** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_TEAM_SIZE}}` | Dimensione del team dedicato | Direzione | organigramma | **P2** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_GROUP_PROOF}}` | Evidenza del gruppo industriale | Direzione | conferma societaria | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_PARTNERSHIP_SIEMENS_APPROVAL}}` | Claim di partnership autorizzato | Legale | lettera del partner | **P1** | deck | deck 10 | visibile | elemento omesso | `OPEN` |
| `{{PH_SAP_INTEGRATION_PROOF}}` | Fonte verificabile per il claim ERP | Tecnico | progetto di riferimento | **P1** | entrambi | deck A4 · dossier 12 | visibile | elemento omesso | `OPEN` |
| `{{PH_PATENT_BOX_APPROVAL}}` | Claim Patent Box autorizzato | Legale | parere fiscale | **P2** | deck | deck 10 | visibile | elemento omesso | `OPEN` |

## 5.3 Caso cliente · identificativi

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_CASE_CLIENT_DISPLAY_NAME}}` | Nome cliente o forma anonima | Legale | autorizzazione scritta | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CLIENT_LEGAL_NAME}}` | Nome legale, uso interno | Legale | contratto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CLIENT_SECTOR}}` | Settore | Commerciale | scheda cliente | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CLIENT_SITE}}` | Stabilimento o paese | Commerciale | scheda cliente | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_LINE_TYPE}}` | Tipo di linea | Tecnico | scheda impianto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PROCESS}}` | Processo osservato | Tecnico | scheda impianto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CONFIDENTIALITY}}` | Pubblico, anonimo o confidenziale | Legale | autorizzazione scritta | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_APPROVAL_STATUS}}` | Stato autorizzazione alla pubblicazione | Legale | autorizzazione scritta | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_APPROVAL_OWNER}}` | Chi ha autorizzato | Legale | autorizzazione scritta | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |

## 5.3 Caso cliente · problema e contesto

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_CASE_INITIAL_PROBLEM}}` | Problema iniziale | Commerciale | verbale di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_BUSINESS_IMPACT}}` | Impatto percepito dal cliente | Commerciale | verbale di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_BASELINE_PERIOD}}` | Periodo della baseline | Tecnico | dati di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_BASELINE_DATA}}` | Dati della baseline | Tecnico | dati di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_DATA_SOURCES}}` | PLC, contatori, gestionale, sensori | Tecnico | mappa dati di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_SCOPE}}` | Macchine, linea, sito | Tecnico | perimetro di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PRECONDITIONS}}` | Prerequisiti presenti | Tecnico | audit di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_GAPS}}` | Gap di dati o di misura | Tecnico | audit di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |

## 5.3 Caso cliente · intervento

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_CASE_SOLUTION_MODULE}}` | Connect, Insight o Refyn | Commerciale | contratto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_IMPLEMENTATION_SCOPE}}` | Perimetro implementato | Tecnico | documento di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_INTERVENTION}}` | Attività svolte | Tecnico | documento di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_ADDED_SENSORS}}` | Sensori o contatori aggiunti | Tecnico | documento di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_ERP_INTEGRATION}}` | Integrazione con il gestionale | Tecnico | documento di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_TIME_TO_FIRST_SIGNAL}}` | Tempo al primo segnale | Tecnico | diario di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_TIME_TO_USABLE_DATA}}` | Tempo al dato utilizzabile | Tecnico | diario di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PILOT_DURATION}}` | Durata del pilot | Commerciale | contratto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_USERS}}` | Utenti coinvolti | Commerciale | documento di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |

## 5.3 Caso cliente · risultati

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_CASE_RESULT_1_LABEL}}` | Nome del risultato 1 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_BASELINE}}` | Baseline del risultato 1 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_AFTER}}` | Valore dopo, risultato 1 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_UNIT}}` | Unità di misura, risultato 1 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_1_METHOD}}` | Metodo di misura, risultato 1 | Tecnico | metodo di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_LABEL}}` | Nome del risultato 2 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_BASELINE}}` | Baseline del risultato 2 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_AFTER}}` | Valore dopo, risultato 2 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_UNIT}}` | Unità di misura, risultato 2 | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_2_METHOD}}` | Metodo di misura, risultato 2 | Tecnico | metodo di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_LABEL}}` | Nome del risultato 3 | Tecnico | misura di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_BASELINE}}` | Baseline del risultato 3 | Tecnico | misura di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_AFTER}}` | Valore dopo, risultato 3 | Tecnico | misura di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_UNIT}}` | Unità di misura, risultato 3 | Tecnico | misura di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_3_METHOD}}` | Metodo di misura, risultato 3 | Tecnico | metodo di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_RESULT_PERIOD}}` | Periodo osservato | Tecnico | misura di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_ANNUALIZED_VALUE}}` | Valore annualizzato | Commerciale | calcolo verificato | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PAYBACK}}` | Payback verificato | Commerciale | calcolo verificato | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_CONFIDENCE_NOTE}}` | Limiti e attendibilità della misura | Tecnico | metodo di progetto | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |

## 5.3 Caso cliente · testimonial e asset

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_CASE_QUOTE}}` | Citazione del cliente | Legale | autorizzazione scritta | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_QUOTE_AUTHOR}}` | Autore della citazione | Legale | autorizzazione scritta | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_QUOTE_ROLE}}` | Ruolo dell’autore | Legale | autorizzazione scritta | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_QUOTE_APPROVAL}}` | Autorizzazione alla citazione | Legale | autorizzazione scritta | **P0** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_LOGO_ASSET}}` | Logo cliente autorizzato | Legale | autorizzazione scritta | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_SCREENSHOT_ASSET}}` | Screenshot reale del caso | Tecnico | ambiente di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_PHOTO_ASSET}}` | Foto reale del caso | Marketing | autorizzazione scritta | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |
| `{{PH_CASE_DIAGRAM_ASSET}}` | Schema anonimizzato del caso | Tecnico | documento di progetto | **P1** | deck | deck 14 | visibile nella slide 14 | slide 14 esclusa | `OPEN` |

## 5.4 Audit e pilot

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_AUDIT_NAME}}` | Nome commerciale del primo passo | Commerciale | decisione commerciale | **P0** | deck | deck 12 · 13 · A3 | visibile | testo prudente | `OPEN` |
| `{{PH_AUDIT_DURATION}}` | Durata dell’audit | Commerciale | decisione commerciale | **P0** | deck | deck 09 · 12 | visibile | elemento omesso | `OPEN` |
| `{{PH_AUDIT_PRICE}}` | Prezzo dell’audit | Commerciale | listino approvato | **P0** | deck | deck 12 · A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_AUDIT_CREDIT_POLICY}}` | Accredito dell’audit sul progetto | Commerciale | decisione commerciale | **P1** | deck | deck A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_AUDIT_PARTICIPANTS}}` | Partecipanti richiesti | Commerciale | metodo di delivery | **P0** | deck | deck 13 | visibile | resta la formulazione V8, già verificata | `OPEN` |
| `{{PH_AUDIT_CLIENT_HOURS}}` | Ore richieste al cliente | Commerciale | metodo di delivery | **P1** | deck | deck 13 | visibile | elemento omesso | `OPEN` |
| `{{PH_AUDIT_INPUTS}}` | Materiali richiesti al cliente | Tecnico | metodo di delivery | **P0** | deck | deck 13 | visibile | resta la formulazione V8, già verificata | `OPEN` |
| `{{PH_AUDIT_DELIVERABLES}}` | Output dell’audit | Tecnico | metodo di delivery | **P0** | deck | deck 13 | visibile | resta la formulazione V8, già verificata | `OPEN` |
| `{{PH_AUDIT_VALIDITY}}` | Validità dell’offerta | Commerciale | decisione commerciale | **P1** | deck | deck A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_PILOT_DURATION}}` | Durata del pilot | Commerciale | decisione commerciale | **P0** | entrambi | deck 12 · dossier 13 | visibile | elemento omesso | `OPEN` |
| `{{PH_PILOT_SCOPE}}` | Perimetro del pilot | Tecnico | metodo di delivery | **P0** | entrambi | deck 12 · dossier 13 | visibile | resta «una linea», già dichiarato | `OPEN` |
| `{{PH_PILOT_SUCCESS_CRITERIA}}` | Criteri di successo | Tecnico | metodo di delivery | **P0** | entrambi | deck 12 · dossier 13 | visibile | restano i criteri di uscita V8 | `OPEN` |
| `{{PH_PILOT_EXIT_CRITERIA}}` | Criteri di uscita | Tecnico | metodo di delivery | **P0** | entrambi | deck 12 · dossier 13 | visibile | restano i criteri di uscita V8 | `OPEN` |
| `{{PH_PILOT_PRICE}}` | Prezzo del pilot | Commerciale | listino approvato | **P0** | deck | deck 12 · A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_PILOT_CONVERSION_POLICY}}` | Conversione del pilot a contratto | Commerciale | decisione commerciale | **P1** | deck | deck 12 | visibile | elemento omesso | `OPEN` |
| `{{PH_PILOT_REVERSIBILITY}}` | Reversibilità del pilot | Commerciale | decisione commerciale | **P1** | deck | deck 12 | visibile | elemento omesso | `OPEN` |

## 5.5 Pricing e contratto

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_SITE_BASE_FEE}}` | Canone base per sito | Commerciale | listino approvato | **P0** | deck | deck 12 · A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_SETUP_FIRST_LINE}}` | Setup della prima linea | Commerciale | listino approvato | **P0** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_CONNECT_ANNUAL_FEE}}` | Canone Connect | Commerciale | listino approvato | **P0** | deck | deck 12 · A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_INSIGHT_ANNUAL_FEE}}` | Canone Insight | Commerciale | listino approvato | **P0** | deck | deck 12 · A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_REFYN_PRICING_MODEL}}` | Modello economico di Refyn | Commerciale | decisione commerciale | **P0** | entrambi | deck 09 · 12 · A1 · A3 · dossier 03 | visibile | canvas escluso | `OPEN` |
| `{{PH_ADDITIONAL_LINE_FEE}}` | Canone per linee successive | Commerciale | listino approvato | **P0** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_SENSOR_PRICING_RULE}}` | Regola di quotazione della sensoristica | Commerciale | decisione commerciale | **P1** | entrambi | deck A3 · dossier 07 | visibile | elemento omesso | `OPEN` |
| `{{PH_SERVICES_INCLUDED}}` | Servizi compresi nell’avvio | Commerciale | decisione commerciale | **P0** | entrambi | deck 08 · A1 · A2 · dossier 03 · 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_SERVICES_OPTIONAL}}` | Servizi opzionali | Commerciale | decisione commerciale | **P0** | entrambi | deck 08 · A2 · dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_PERFORMANCE_REVIEW_FEE}}` | Prezzo della performance review | Commerciale | listino approvato | **P1** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_ENERGY_REVIEW_FEE}}` | Prezzo della energy review | Commerciale | listino approvato | **P1** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_PREMIUM_SUPPORT_FEE}}` | Prezzo del supporto premium | Commerciale | listino approvato | **P1** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_CONTRACT_TERM}}` | Durata contrattuale | Commerciale | contratto tipo | **P0** | deck | deck 09 · A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_RENEWAL_TERMS}}` | Condizioni di rinnovo | Commerciale | contratto tipo | **P0** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_TERMINATION_TERMS}}` | Condizioni di recesso | Legale | contratto tipo | **P1** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_PAYMENT_TERMS}}` | Termini di pagamento | Commerciale | contratto tipo | **P1** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_PRICE_VALIDITY}}` | Validità dei prezzi | Commerciale | listino approvato | **P1** | deck | deck A3 | visibile | canvas escluso | `OPEN` |
| `{{PH_INDEXATION}}` | Indicizzazione | Commerciale | contratto tipo | **P2** | deck | deck A3 | visibile | canvas escluso | `OPEN` |

## 5.6 Supporto e SLA

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_SUPPORT_HOURS}}` | Orari del supporto | Commerciale | contratto tipo | **P0** | entrambi | deck A2 · dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_SUPPORT_CHANNELS}}` | Canali del supporto | Commerciale | contratto tipo | **P1** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_SLA_SEVERITY_LEVELS}}` | Livelli di severità | Tecnico | contratto tipo | **P0** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_SLA_RESPONSE_TIMES}}` | Tempi di risposta | Commerciale | contratto tipo | **P0** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_SLA_RESOLUTION_TARGETS}}` | Obiettivi di risoluzione | Commerciale | contratto tipo | **P1** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_ESCALATION_PROCESS}}` | Processo di escalation | Tecnico | contratto tipo | **P1** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_MAINTENANCE_WINDOWS}}` | Finestre di manutenzione | Tecnico | contratto tipo | **P1** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_UPDATE_POLICY}}` | Politica di aggiornamento | Tecnico | contratto tipo | **P0** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_CHANGE_REQUEST_POLICY}}` | Politica delle change request | Commerciale | contratto tipo | **P1** | dossier | dossier 14 | visibile | elemento omesso | `OPEN` |
| `{{PH_REMOTE_SUPPORT_POLICY}}` | Politica di supporto remoto | Tecnico + IT | contratto tipo | **P0** | dossier | dossier 14 · A3 | visibile | elemento omesso | `OPEN` |

## 5.7 Deployment e infrastruttura

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_DEPLOYMENT_MODEL}}` | On-premise, VM o altro | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 02 · 08 · A2 | visibile | testo prudente | `OPEN` |
| `{{PH_SERVER_OWNER}}` | Proprietà dell’ambiente | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 08 · A2 | visibile | testo prudente | `OPEN` |
| `{{PH_SUPPORTED_OS}}` | Sistemi operativi supportati | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 08 · A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_MIN_CPU}}` | CPU minima | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_MIN_RAM}}` | RAM minima | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_MIN_STORAGE}}` | Storage minimo | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_STORAGE_GROWTH_RULE}}` | Regola di crescita dello storage | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_RETENTION_DEFAULT}}` | Retention di default | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A2 · A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_HIGH_AVAILABILITY}}` | Alta disponibilità | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_VIRTUALIZATION_SUPPORT}}` | Virtualizzazione supportata | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_CONTAINER_SUPPORT}}` | Container supportati | Tecnico + IT | scheda tecnica di prodotto | **P2** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_TIME_SYNC_REQUIREMENT}}` | Requisito di sincronizzazione oraria | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier 09 | visibile | elemento omesso | `OPEN` |
| `{{PH_INTERNET_REQUIREMENT}}` | Accesso a internet richiesto | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 08 | visibile | elemento omesso | `OPEN` |
| `{{PH_CLOUD_OPTION}}` | Opzione cloud | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier 02 · 08 | visibile | elemento omesso | `OPEN` |

## 5.8 Rete e protocolli

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_SUPPORTED_PROTOCOLS}}` | Protocolli supportati | Tecnico | catalogo verificato in campo | **P0** | dossier | dossier 08 · A1 | visibile | elemento omesso | `OPEN` |
| `{{PH_PROTOCOL_VERSIONS}}` | Versioni testate | Tecnico | catalogo verificato in campo | **P1** | dossier | dossier A1 | visibile | elemento omesso | `OPEN` |
| `{{PH_REQUIRED_PORTS}}` | Porte richieste | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 08 · A1 | visibile | elemento omesso | `OPEN` |
| `{{PH_FLOW_DIRECTIONS}}` | Direzioni dei flussi | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 08 | visibile | resta lo schema logico V8 | `OPEN` |
| `{{PH_READ_ONLY_POLICY}}` | Regola di sola lettura verso le macchine | Tecnico | scheda tecnica di prodotto | **P0** | dossier | dossier 08 · A1 | visibile | testo prudente | `OPEN` |
| `{{PH_NETWORK_SEGMENTATION}}` | Segmentazione di rete richiesta | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier 08 | visibile | elemento omesso | `OPEN` |
| `{{PH_FIREWALL_RULES}}` | Regole firewall | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 08 · A1 | visibile | elemento omesso | `OPEN` |
| `{{PH_GATEWAY_REQUIREMENTS}}` | Requisiti del gateway | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier A1 | visibile | elemento omesso | `OPEN` |
| `{{PH_BANDWIDTH_REQUIREMENT}}` | Banda richiesta | Tecnico + IT | scheda tecnica di prodotto | **P2** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_LATENCY_REQUIREMENT}}` | Latenza richiesta | Tecnico + IT | scheda tecnica di prodotto | **P2** | dossier | dossier A2 | visibile | elemento omesso | `OPEN` |
| `{{PH_ERP_INTEGRATION_METHODS}}` | Modalità di integrazione con il gestionale | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier 08 · 12 | visibile | testo prudente | `OPEN` |
| `{{PH_API_AVAILABILITY}}` | Disponibilità delle API | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier 12 | visibile | elemento omesso | `OPEN` |
| `{{PH_API_AUTHENTICATION}}` | Autenticazione delle API | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier 12 | visibile | elemento omesso | `OPEN` |
| `{{PH_EXPORT_FORMATS}}` | Formati di export | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier 12 | visibile | restano i formati già dichiarati | `OPEN` |

## 5.9 Security, dati e licenza

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_AUTHENTICATION_MODEL}}` | Modello di autenticazione | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier 08 · A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_ROLE_MODEL}}` | Modello dei ruoli | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_PASSWORD_POLICY}}` | Politica delle password | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_SSO_SUPPORT}}` | Supporto SSO | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_AUDIT_LOGGING}}` | Registro degli accessi | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_LOG_RETENTION}}` | Retention dei log | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_PATCHING_POLICY}}` | Politica di patching | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_VULNERABILITY_POLICY}}` | Vulnerability management | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_BACKUP_POLICY}}` | Politica di backup | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_BACKUP_FREQUENCY}}` | Frequenza di backup | Tecnico + IT | scheda tecnica di prodotto | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_RPO}}` | RPO | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_RTO}}` | RTO | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_DISASTER_RECOVERY}}` | Disaster recovery | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_DATA_ENCRYPTION_AT_REST}}` | Cifratura a riposo | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_DATA_ENCRYPTION_IN_TRANSIT}}` | Cifratura in transito | Tecnico + IT | scheda tecnica di prodotto | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_DATA_OWNERSHIP}}` | Proprietà dei dati | Legale | contratto tipo | **P0** | dossier | dossier 02 · A3 | visibile | testo prudente | `OPEN` |
| `{{PH_LICENSE_RIGHTS}}` | Diritti di licenza | Legale | contratto tipo | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_END_OF_CONTRACT_DATA}}` | Dati a fine contratto | Legale | contratto tipo | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_END_OF_CONTRACT_ACCESS}}` | Accesso a fine contratto | Legale | contratto tipo | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_DATA_EXPORT_AT_EXIT}}` | Export a fine rapporto | Legale | contratto tipo | **P0** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |
| `{{PH_DATA_DELETION_POLICY}}` | Cancellazione dei dati | Legale | contratto tipo | **P1** | dossier | dossier A3 | visibile | elemento omesso | `OPEN` |

## 5.10 Dataset illustrativo

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_DATASET_LINE_TYPE}}` | Tipo di linea dello scenario | Tecnico | validazione interna | **P0** | deck | deck 01 · 11 · A5 | visibile | resta «linea di confezionamento» | `OPEN` |
| `{{PH_DATASET_VALIDATOR}}` | Chi ha validato il dataset | Tecnico | validazione interna | **P0** | deck | deck 01 · A5 | visibile | elemento omesso | `OPEN` |
| `{{PH_DATASET_VALIDATION_DATE}}` | Data della validazione | Tecnico | validazione interna | **P0** | deck | deck 01 · A5 | visibile | elemento omesso | `OPEN` |
| `{{PH_DATASET_THROUGHPUT}}` | Pezzi al minuto | Tecnico | validazione interna | **P0** | deck | deck 11 · A5 | visibile | resta 500 pz/min, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_MARGIN_UNIT}}` | Margine per pezzo | Commerciale | validazione interna | **P0** | deck | deck 11 · A5 | visibile | resta 0,14 €/pz, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_RUNNING_POWER}}` | Potenza in marcia | Tecnico | validazione interna | **P0** | deck | deck 11 · A5 | visibile | resta 95 kW, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_STOPPED_POWER}}` | Potenza a impianto fermo | Tecnico | validazione interna | **P0** | deck | deck 11 · A5 | visibile | resta 38 kW, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_ENERGY_PRICE}}` | Prezzo dell’energia | Commerciale | contratto di fornitura | **P0** | deck | deck A5 | visibile | resta 0,22 €/kWh, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_EMISSION_FACTOR}}` | Fattore di emissione | Tecnico | mix dichiarato dal fornitore | **P0** | deck | deck A5 | visibile | resta 0,35 kgCO₂e/kWh, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_SHIFT_DURATION}}` | Durata del turno | Tecnico | validazione interna | **P0** | deck | deck A5 | visibile | resta 480 min, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_SHIFTS_PER_YEAR}}` | Turni produttivi in un anno | Tecnico | validazione interna | **P0** | deck | deck A5 | visibile | resta 230, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_STOP_MIN_WEEK}}` | Minuti di fermo a settimana | Tecnico | validazione interna | **P0** | deck | deck 11 · A5 | visibile | resta 96 min, dichiarato illustrativo | `OPEN` |
| `{{PH_DATASET_RECOVERABLE_SHARE}}` | Quota potenzialmente recuperabile | Commerciale | validazione interna | **P0** | deck | deck 11 | visibile | resta la metà, dichiarata ipotesi | `OPEN` |
| `{{PH_DATASET_ASSUMPTION_OWNER}}` | Owner delle assunzioni | Commerciale | nomina interna | **P0** | deck | deck A5 | visibile | elemento omesso | `OPEN` |

## 8 Perimetro dei moduli

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_CONNECT_EXACT_SCOPE}}` | Perimetro esatto di Connect | Tecnico | scheda funzionale | **P0** | dossier | dossier 04 | visibile | resta il perimetro già dichiarato | `OPEN` |
| `{{PH_CONNECT_REPORTS}}` | Report inclusi in Connect | Tecnico | scheda funzionale | **P1** | dossier | dossier 04 | visibile | elemento omesso | `OPEN` |
| `{{PH_CONNECT_ALERTS}}` | Notifiche e allarmi di Connect | Tecnico | scheda funzionale | **P1** | dossier | dossier 04 | visibile | elemento omesso | `OPEN` |
| `{{PH_INSIGHT_EXACT_SCOPE}}` | Perimetro esatto di Insight | Tecnico | scheda funzionale | **P0** | dossier | dossier 05 | visibile | resta il perimetro già dichiarato | `OPEN` |
| `{{PH_COST_CALCULATION_METHOD}}` | Metodo di calcolo del costo | Tecnico | scheda funzionale | **P1** | dossier | dossier 05 · 11 | visibile | resta il metodo già scritto in A4 | `OPEN` |
| `{{PH_CO2_METHOD}}` | Metodo di calcolo della CO₂ | Tecnico | scheda funzionale | **P1** | dossier | dossier 05 · 11 | visibile | resta «CO₂ calcolata o stimata» | `OPEN` |
| `{{PH_REFYN_MVP_SCOPE}}` | Perimetro del primo rilascio di Refyn | Tecnico | piano di prodotto | **P0** | dossier | dossier 06 | visibile | blocco nascosto | `OPEN` |
| `{{PH_REFYN_PILOT_RULES}}` | Regole di accesso al pilot Refyn | Commerciale | decisione commerciale | **P0** | dossier | dossier 06 | visibile | blocco nascosto | `OPEN` |
| `{{PH_REFYN_RELEASE_TARGET}}` | Data obiettivo di rilascio | Direzione | piano di prodotto | **P1** | dossier | dossier 06 | visibile | blocco nascosto | `OPEN` |
| `{{PH_STANDARD_SIGNAL_LIST}}` | Elenco standard dei segnali | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier 07 | visibile | elemento omesso | `OPEN` |
| `{{PH_SENSOR_ACCURACY_REQUIREMENTS}}` | Requisiti di precisione della sensoristica | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier 07 | visibile | elemento omesso | `OPEN` |
| `{{PH_METERING_STANDARDS}}` | Standard di misura adottati | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier 07 | visibile | elemento omesso | `OPEN` |
| `{{PH_STANDARD_TAG_MODEL}}` | Modello standard dei tag | Tecnico | scheda tecnica di prodotto | **P1** | dossier | dossier 09 | visibile | restano i sette attributi | `OPEN` |
| `{{PH_CAUSE_VALIDATION_PROCESS}}` | Processo di validazione della causa | Tecnico | metodo di delivery | **P1** | dossier | dossier 09 | visibile | resta «validata da chi la conosce» | `OPEN` |
| `{{PH_REPORT_CATALOGUE}}` | Catalogo dei report | Tecnico | scheda funzionale | **P1** | dossier | dossier 12 | visibile | elemento omesso | `OPEN` |

## 9 Dizionario KPI e definizioni OEE

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_OEE_DEFINITION_OWNER}}` | Owner della definizione di OEE | Tecnico | nomina interna | **P1** | dossier | dossier 10 · A4 | visibile | elemento omesso | `OPEN` |
| `{{PH_OEE_CALENDAR_RULES}}` | Regole di calendario e tempo pianificato | Tecnico | metodo concordato | **P0** | dossier | dossier 10 · A4 | visibile | resta «si concordano prima del go-live» | `OPEN` |
| `{{PH_IDEAL_CYCLE_TIME_RULE}}` | Regola del tempo ciclo ideale | Tecnico | metodo concordato | **P0** | dossier | dossier 10 · A4 | visibile | resta la formula di A4 | `OPEN` |
| `{{PH_GOOD_COUNT_RULE}}` | Regola del conteggio dei pezzi conformi | Tecnico | metodo concordato | **P0** | dossier | dossier 10 · A4 | visibile | resta la formula di A4 | `OPEN` |
| `{{PH_LINE_OEE_AGGREGATION}}` | Regola di aggregazione dell’OEE di linea | Tecnico | metodo concordato | **P0** | dossier | dossier 10 | visibile | resta «collo di bottiglia» | `OPEN` |
| `{{PH_ENERGY_PRICE_SOURCE}}` | Fonte del prezzo dell’energia | Commerciale | contratto di fornitura | **P1** | dossier | dossier 11 | visibile | resta «contratto di fornitura» | `OPEN` |
| `{{PH_EMISSION_FACTOR_SOURCE}}` | Fonte del fattore di emissione | Tecnico | mix dichiarato dal fornitore | **P1** | dossier | dossier 11 | visibile | resta «mix dichiarato» | `OPEN` |
| `{{PH_COST_ALLOCATION_RULE}}` | Regola di allocazione del costo | Tecnico | metodo concordato | **P1** | dossier | dossier 11 | visibile | elemento omesso | `OPEN` |
| `{{PH_KPI_OWNER}}` | Owner del dizionario KPI | Tecnico | nomina interna | **P1** | dossier | dossier A4 | visibile | elemento omesso | `OPEN` |
| `{{PH_KPI_VERSION}}` | Versione del dizionario KPI | Tecnico | processo interno | **P1** | dossier | dossier A4 | visibile | elemento omesso | `OPEN` |
| `{{PH_KPI_APPROVAL_DATE}}` | Data di approvazione del dizionario | Tecnico | processo interno | **P1** | dossier | dossier A4 | visibile | elemento omesso | `OPEN` |

## 10 Asset reali

| ID | Descrizione | Owner | Fonte richiesta | Pri | Doc | Canvas | Working | Client | Stato |
|---|---|---|---|:--:|---|---|---|---|:--:|
| `{{PH_REAL_SCREENSHOT_MAPST}}` | Screenshot reale MAPST 4.0 | Tecnico | ambiente reale | **P1** | entrambi | deck 04 · dossier 04 | visibile | resta la vista ricostruita dichiarata | `OPEN` |
| `{{PH_REAL_SCREENSHOT_MARENERGY}}` | Screenshot reale MarEnergy | Tecnico | ambiente reale | **P1** | entrambi | deck 05 · dossier 11 | visibile | resta la vista ricostruita dichiarata | `OPEN` |
| `{{PH_REAL_SCREENSHOT_NEW_UI}}` | Screenshot della nuova interfaccia | Tecnico | ambiente reale | **P1** | entrambi | deck 03 · dossier 04 | visibile | resta la vista ricostruita dichiarata | `OPEN` |
| `{{PH_REAL_REPORT_EXPORT}}` | Report reale esportato | Tecnico | ambiente reale | **P1** | dossier | dossier 12 | visibile | elemento omesso | `OPEN` |
| `{{PH_REAL_INSTALLATION_PHOTO}}` | Foto di un’installazione | Marketing | autorizzazione scritta | **P1** | entrambi | deck 10 · dossier 01 | visibile | elemento omesso | `OPEN` |
| `{{PH_REAL_LINE_DIAGRAM}}` | Schema di linea reale anonimizzato | Tecnico | documento di progetto | **P1** | dossier | dossier 07 | visibile | resta lo schema tipo dichiarato | `OPEN` |
| `{{PH_REAL_SENSOR_PHOTO}}` | Foto di sensore o contatore | Marketing | autorizzazione scritta | **P1** | dossier | dossier 07 | visibile | elemento omesso | `OPEN` |
| `{{PH_REAL_SERVER_DIAGRAM}}` | Schema di deployment reale | Tecnico + IT | documento di progetto | **P1** | dossier | dossier 08 | visibile | resta lo schema logico dichiarato | `OPEN` |


---

## Effetto complessivo sulla client edition di oggi

Con tutti i placeholder `OPEN`, la client edition esclude:

| canvas | perché |
|---|---|
| deck 13 · CTA | `PH_CONTACT_NAME`, `PH_CONTACT_ROLE`, `PH_CONTACT_EMAIL` sono P0 e la §5.1 vieta di pubblicare la CTA senza contatto |
| deck 14 · caso cliente | `PH_CASE_APPROVAL_STATUS` non è `APPROVED` |
| deck A3 · pricing | nessun importo approvato: la §5.5 impone di rimuovere la pagina di pricing dettagliato |
| dossier 06 · riquadro Refyn | `PH_REFYN_RELEASE_TARGET` non approvata: nessuna data di rilascio |

Tutto il resto passa nella client edition con i blocchi di placeholder rimossi e,
dove previsto, con la formulazione prudente già in uso nella V8 — che era stata
scritta proprio per reggere senza quei valori.

**Il deck client-facing di oggi ha quindi 12 slide e 4 appendici.** Non è una
riduzione di qualità: è la conseguenza aritmetica di quattro input mancanti.

