# D.Factory · V9.3 · E0 Build Map

**Fase E0 del §5.1.** Mappa di costruzione dei 40 canvas: 19 del Sales Deck e
21 del Dossier. Per ciascuno: ruolo, tipo, archetipo, fonte, azione, claim,
gate, asset, rischio.

Input letti: storyboard Sales e Dossier V9.3 · Claim Register V9.2 ·
Open Inputs V9.2 · `DFactory_V9_3_Prototype_Delta.md` · contact sheet D2.

---

## 1. Regola operativa della Fase E

Il §1.2 è esplicito: approvazione non significa congelamento. Sono approvati
direzione, struttura dei pacchetti, archetipi, progressione bianco → grigio →
nero, architettura a quattro livelli, separazione output/integrazioni,
executive summary scuro e prosa per pagina core.

**Non** sono congelati microgerarchie, densità, spaziatura, contrasto,
trattamento delle fasce, peso dei risultati, precisione delle etichette.

I prototipi D2 sono lo **standard minimo**. Un canvas che resta sotto quello
standard va migliorato, non replicato.

---

## 2. Sales Deck · 15 core + 4 appendici

Fondi: `dk` nero · `lt` bianco · `gr` grigio chiarissimo · `mx` misto.

| # | canvas | ruolo | tipo | fondo | fonte | azione | claim | gate | asset | rischio |
|--:|---|---|---|:--:|---|:--:|---|---|---|---|
| 01 | `s01_promessa` | promessa e posizionamento | narrativa | dk | `v01_cover` V9.2 | **rewrite** · la vista scende a prova di sfondo, la headline domina | — | G1 · G3 | ricostruzione dichiarata | la vista torna a competere con la headline |
| 02 | `s02_problema` | tre fratture, non quattro sorgenti | narrativa | lt | `v02_tensione` V9.2 | **new** | — | — | — | tornare a un elenco tecnico di sorgenti |
| 03 | `s03_visione` | che cos'è il prodotto | narrativa | lt | `v03_categoria` V9.2 | **new** · schema editoriale a quattro stazioni | — | G5 | — | sembrare architettura IT |
| 04 | `s04_trasformazione` | la cerniera | narrativa | mx | prototipo D2 | **keep** | — | — | — | — |
| 05 | `s05_prodotto` | prima prova di prodotto | prodotto | lt | `v04_evento_prodotto` V9.2 | **keep** · visual invariato | — | G5 | `PH_REAL_SCREENSHOT_MAPST` | — |
| 06 | `s06_quattro_letture` | un evento, quattro letture | prodotto | dk | `v05_energia` + `v07_ampiezza` | **merge** | `costo_en` | G3 · G5 | `PH_REAL_SCREENSHOT_MARENERGY` | due dashboard sovrapposte |
| 07 | `s07_priorita` | dall'evento alla priorità | valore | lt | `v06_priorita` V9.2 | **rewrite** · copy narrativo dominante, ranking sotto | — | — | — | restare la terza slide tecnica di fila |
| 08 | `s08_mappa` | mappa delle funzionalità | funzionalità | dk | `v07_ampiezza` V9.2 | **new** · cinque fasce editoriali | — | — | — | mini-dashboard |
| 09 | `s09_connect` | pacchetto 1 | pacchetto | lt | prototipo D2 | **keep** | `cumulativa` | G2 | — | — |
| 10 | `s10_insight` | pacchetto 2 | pacchetto | gr | prototipo D2 | **keep** | `cumulativa` `costo_en` `co2` | G2 | — | numero economico non supportato |
| 11 | `s11_refyn` | pacchetto 3 | pacchetto | dk | prototipo D2 | **keep** | `refyn` `cumulativa` | G2 | — | funzioni future aggiunte |
| 12 | `s12_confronto` | confronto e servizi | pacchetti | lt | `a1_matrice` V9.2 | **rewrite** · sale nel corpo, nove righe, servizi come layer | `cumulativa` | G2 | — | matrice compressa |
| 13 | `s13_perche` | perché D.Factory | azienda | dk | `v10_perche` V9.2 | **rewrite** · tre principi, nessuna timeline | `brownfield` | G5 | prova aziendale assente | inventare numeri |
| 14 | `s14_valore` | valore e modello | valore | lt | `v11_valore` + `v12_pilot` | **merge** | `costo_en` | G2 · G3 | — | pubblicare annualizzati |
| 15 | `s15_pilot_cta` | pilot e CTA | cta | dk | `v12_pilot` + `v13_cta` | **merge** | — | G1 | — | seconda dashboard |
| A1 | `a1_matrice` | matrice completa | appendice | lt | `a1_matrice` V9.2 | **rewrite** · quattordici righe per area | `cumulativa` | G2 | — | microtesto |
| A2 | `a2_servizi` | catalogo servizi | appendice | lt | `a2_servizi` V9.2 | **rewrite** · cinque colonne | — | G2 | — | — |
| A3 | `a3_pricing` | struttura economica | appendice | lt | `a3_pricing` V9.2 | **keep** · condizionale G2 | — | **G2 · PAGE** | — | — |
| A4 | `a4_faq` | FAQ commerciali | appendice | lt | `a4_faq` V9.2 | **rewrite** · solo domande commerciali | `read_only` `compat` | — | — | domande IT nel deck |
| A5 | `a5_assunzioni` | assunzioni | appendice | lt | `a5_assunzioni` V9.2 | **keep** · working only, G3 | — | **G3 · PAGE** | — | — |
| S14b | `s16_caso` | caso cliente | — | lt | `v14_caso` V9.2 | **keep** · working only | — | **CASE · PAGE** | — | — |

**Client edition:** 15 core + A1 + A2 + A4 = **18 canvas**. Escluse `a3_pricing`
(G2), `a5_assunzioni` (G3), `s16_caso` (CASE).

### 2.1 Ritmo dichiarato · §7.1

| # | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| fondo | dk | lt | lt | mx | lt | dk | lt | dk | lt | gr | dk | lt | dk | lt | dk |
| tipo | nar | nar | nar | nar | pro | pro | val | fun | pac | pac | pac | pac | azi | val | cta |

- Nessun fondo ripetuto tre volte di fila ✔
- Slide fortemente UI: **03 — S05, S06, S07** ✔ (tetto del §16)
- Slide tecniche consecutive: **due** (S05, S06) ✔
- Matrici nel corpo: **una** (S12) ✔
- Dashboard consecutive dopo S06: **zero** ✔
- Slide pacchetto visivamente identiche: **zero** — tre fondi, tre trattamenti del risultato ✔

---

## 3. Dossier · 17 core + 4 annessi

| # | canvas | ruolo | archetipo | fondo | fonte | azione | claim | gate | rischio |
|--:|---|---|---|:--:|---|:--:|---|---|---|
| 01 | `p01_cover` | copertina | editoriale scuro | dk | `p01_cover` V9.2 | **rewrite** · destinatari su una riga | — | G1 · **G4** | — |
| 02 | `p02_executive` | sintesi | editoriale scuro | dk | prototipo D2 | **keep + refine** · contrasto e corpo (§2.1) | `cumulativa` `brownfield` | — | concetti laterali in eccesso |
| 03 | `p03_architettura_funzionale` | dal segnale alla decisione | architecture | lt | — | **new** | — | — | duplicare P11 |
| 04 | `p04_base_comune` | base funzionale comune | product page | lt | `p03_livelli` V9.2 | **rewrite** | `cumulativa` | G2 | ripetere le pagine pacchetto |
| 05 | `p05_connect` | modulo 1 | product page | lt | prototipo D2 | **keep + refine** · tre capability, configurazione in fascia (§2.2) | — | G5 | — |
| 06 | `p06_insight` | modulo 2 | product page | lt | `p05_insight` V9.2 | **rewrite** · visuale diverso da P05 | `costo_en` `co2` | G5 | stesso layout di P05 |
| 07 | `p07_refyn` | modulo 3 | product page | lt | `p06_refyn` V9.2 | **rewrite** · ciclo, visuale diverso | `refyn` | — | stesso layout di P05/P06 |
| 08 | `p08_matrice` | perimetro dei tre livelli | reference | lt | — | **new** · quattordici righe | `cumulativa` | G2 | microtesto |
| 09 | `p09_acquisizione` | sorgenti e punti di misura | architecture | lt | `p07_sorgenti` V9.2 | **rewrite** · esempio dichiarato | `compat` | G4 | sembrare la configurazione standard |
| 10 | `p10_contesto` | modello di contesto | modello | **dk** | `p09_contesto` V9.2 | **rewrite** · evento e attributi, non timeline | — | G4 | ridimostrare il fermo |
| 11 | `p11_architettura` | architettura e deployment | architecture | lt | prototipo D2 | **keep + refine** · livello 4, buffer, motore KPI (§2.3) | `read_only` `residenza` | **G4** | — |
| 12 | `p12_security` | sicurezza e governo | reference | lt | — | **new** · principi e aree, valori in A3 | — | G4 | tono da questionario |
| 13 | `p13_oee` | metodo · produzione | method | lt | `p10_oee` V9.2 | **rewrite** | `oee` | G4 | ripetere il ranking di P06 |
| 14 | `p14_energia` | metodo · energia | method | lt | `p11_energia` V9.2 | **rewrite** · stessa grammatica, layout diverso da P13 | `costo_en` `co2` | G3 | stesso layout di P13 |
| 15 | `p15_output` | output e integrazioni | reference | lt | prototipo D2 | **keep + refine** · API non dichiarata disponibile (§2.4) | `erp` | G4 | claim API |
| 16 | `p16_delivery` | dall'assessment alla scala | delivery | **dk** | `p13_pilot` V9.2 | **rewrite** · sei fasi | — | G2 | — |
| 17 | `p17_servizi` | servizi e supporto | delivery | lt | `p14_servizi` V9.2 | **rewrite** · narrativa più tabella | — | G2 · G4 | solo tabella |
| A1 | `pa1_compatibilita` | compatibilità | annesso | lt | `pa1` V9.2 | **rewrite** · senza owner in client | `compat` | G4 | — |
| A2 | `pa2_sizing` | dimensionamento | annesso | lt | `pa2` V9.2 | **rewrite** · tre fasce anche in client | — | G4 | — |
| A3 | `pa3_requisiti` | requisiti IT e security | annesso | lt | `pa3` V9.2 | **rewrite** · rinominato, è la sede di owner e valori | — | G4 | — |
| A4 | `pa4_kpi` | dizionario KPI | annesso | lt | `pa4` V9.2 | **rewrite** · nota unica al posto delle ripetizioni | `oee` `costo_en` | G4 | — |

### 3.1 Ritmo dichiarato · §9.2

| # | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | A1 | A2 | A3 | A4 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| fondo | dk | dk | lt | lt | lt | lt | lt | lt | lt | dk | lt | lt | lt | lt | lt | dk | lt | lt | lt | lt | lt |
| archetipo | ed | ed | ar | pr | pr | pr | pr | rf | ar | mo | ar | rf | me | me | rf | de | de | an | an | an | an |

- Pagine scure: **4** — cover, executive summary, modello di contesto, delivery ✔ (§9.5: 3–4)
- Reference consecutive: massimo **una** nel core ✔
- Diagrammi architetturali consecutivi: 09 e 11 separati da 10 ✔
- Annessi consecutivi: A2 porta un diagramma e rompe la sequenza ✔
- Quattro pagine senza elemento visivo forte: **nessuna sequenza** ✔

---

## 4. I quattro miglioramenti D2 obbligatori · §17

| pagina | correzione | come viene applicata |
|---|---|---|
| **P02** | aumentare contrasto e leggibilità | prosa da `--d2` a `--d1` con opacità 0,86 · corpo da 17 a 17,5 px · i tre principi guadagnano peso rispetto alla descrizione · la sezione attiva della navigazione passa da 600 a 700 e riceve un marcatore |
| **P05** | tre capability, configurazione in fascia separata | «Configurazione» esce dalle quattro colonne e diventa una fascia tecnica finale: «Configurabile per: anagrafiche, calendari, soglie, stati, utenti e viste» · visuale +8% · più spazio fra i gruppi · causa associata evidenziata · dicitura di ricostruzione più contrastata |
| **P11** | livello 4, buffer, motore KPI | livello 4 → **«Output e sistemi esterni»** con divisione visiva fra output ed ERP/API · «Buffer» → **«Accodamento e persistenza temporanea»** (non confermato come componente) · «Motore KPI» → **«Elaborazione KPI»** (concetto funzionale, non componente) · frecce più spesse · contrasto dei livelli 1, 2 e 4 · la nota sola lettura diventa nota tecnica, non callout |
| **P15** | non dichiarare API disponibile | «API» → **«Interfacce applicative»**, modalità **«da verificare sul perimetro»** · «ERP e gestionale» → **«ERP / gestionale»** con lo scopo e la modalità prescritti dal §2.4 · fascia più chiara per gli output · colonna contenuto più stretta · corpo del paragrafo e della nota aumentati |

---

## 5. Claim e gate

### 5.1 Claim in gioco

Dieci, invariati dal Claim Register V9.2. Nessun claim nuovo viene introdotto
dalla V9.3: la revisione narrativa non ha aggiunto affermazioni tecniche.

Due claim cambiano **formulazione** per effetto del §2.3 e del §2.4:

| claim | prima | dopo | perché |
|---|---|---|---|
| — | «Motore KPI» come componente | «Elaborazione KPI» come funzione | il §2.3 chiede di non dichiarare un componente architetturale che non è confermato |
| `erp` | «API · dati selezionati · da definire» | «Interfacce applicative · da verificare sul perimetro» | il §2.4: la presenza di API è un claim di prodotto e non è confermata |

### 5.2 Gate, invariati

| gate | stato | effetto sulla V9.3 |
|---|:--:|---|
| G1 identità e CTA | `OPEN` | S15 senza referente · warning globale · P01 senza denominazione |
| G2 modello commerciale | `OPEN` | A3 fuori dalla client edition · S14 mostra il modello, non gli importi |
| G3 dataset | `OPEN` | nessun annualizzato · A5 fuori dalla client edition |
| G4 IT/OT | `OPEN` | dossier «preliminare» · A2 metodo e fasce, non valori · A3 raccolta requisiti |
| G5 evidenze | `OPEN` | zero asset reali · S13 senza numeri aziendali |
| CASE | `NO` | `s16_caso` fuori dalla client edition |

---

## 6. Rischi di sequenza, sorvegliati dal build

| rischio | dove | controllo automatico |
|---|---|---|
| tre slide tecniche di fila | S05–S07 | `technical streak` |
| tre fondi uguali di fila | tutto il deck | `rhythm map` |
| due strutture identiche di fila | S09–S11, P05–P07 | `duplicate layout map` |
| pacchetto con dashboard | S09, S10, S11 | `package check` — condizione di build |
| tono da questionario nel core | P03–P17 | `dossier questionnaire check` — condizione di build |
| microtesto | tutti | `text-size audit` per popolazione |
| claim fuori registro | tutti | `accept93.py` |

---

## 7. Che cosa questa mappa non risolve

Restano fuori, come da §13 e §15 del master precedente: prezzi, contatti, asset
reali, validazione del dataset, specifiche IT/OT definitive e caso cliente.

La Fase E crea lo spazio per ciascuno — S14 e A3 per gli importi, S13 per la
prova aziendale, S15 e P01 per il contatto, A1/A2/A3 del dossier per i valori
tecnici — e non ne inventa nessuno.
