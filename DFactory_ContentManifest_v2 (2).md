# D.Factory · Content Manifest v2

Fonte di verità per tenere allineati `DFactory_SalesDeck_v2.html` e
`DFactory_DossierTecnico_v2.html`. Se un claim cambia qui, cambia in entrambi.

## Gerarchia delle fonti applicata

| Livello | Fonte | Stato in questo lavoro |
|---|---|---|
| 1 | I due HTML esistenti | Usati come fonte primaria di claim, numeri, nomi e placeholder |
| 2 | `Marchiani_Assessment_12Marzo.docx` | **Non presente nel workspace.** Nessun contenuto ne è stato tratto |
| 3 | Inferenze editoriali | Solo su titoli, ordine, gerarchia, visualizzazione e distribuzione |
| 4 | Ricerca esterna | Non effettuata |

L'assessment interno non è stato trovato: nessun file `.docx` esiste nel repository
né fra i materiali caricati. Di conseguenza **tutti i temi che il brief attribuiva
a quella fonte restano fuori dai documenti** e sono registrati sotto come "fonte non
disponibile". Non sono stati dedotti, riscritti o sostituiti con equivalenti.

---

## 1. Terminologia canonica

| Termine | Forma corretta | Note d'uso |
|---|---|---|
| Prodotto | `D.Factory` | Sempre con il punto. Nome dell'offerta |
| Società | `D Factory S.r.l.` | Solo nella denominazione, nei rail di copertina e chiusura |
| Piattaforma | `MAPST 4.0` | Solo nel dossier. Non compare nel sales deck |
| Livello 1 | `Connect` | Visibilità e supervisione |
| Livello 2 | `Insights` | Analisi, fermi, energia, costo e CO₂ |
| Servizi | `Refyn` | Servizi sul dato, sempre "in definizione". Mai terzo livello di prodotto |
| Efficienza di linea | `OEE di linea` | Sull'intera linea, tiene conto dei polmoni |
| Efficienza di asset | `OEE macchina` | Sul singolo asset |
| Stato | `stato macchina` | 17 stati PackML, modello ridotto a due dove manca lo standard |
| Fermo | `fermo macchina` / `fermo linea` | Distinti sempre: il primo non implica il secondo |
| Polmone | `polmone`, con `buffer` spiegato una volta | Forma primaria italiana |
| Costo unitario | `costo energetico per pezzo` | Mai "costo per unità" |
| Emissioni | `CO₂ per pezzo` | Con il pedice corretto |
| Deployment | `on-premise` | Mai "in locale", mai "cloud privato" |
| Compatibilità | `multi-vendor`, `multi-protocollo` | Mai "qualsiasi marca", mai "compatibile con tutto" |
| Impianti esistenti | `brownfield` | Spiegato alla prima occorrenza |
| Milestone 1 | `first signal` | Primo segnale acquisito |
| Milestone 2 | `first usable data` | Primo dato contestualizzato e verificato |
| Milestone 3 | `pilot live` | Una linea con viste e KPI concordati |
| Milestone 4 | `operational go-live` | Utenti formati, formule validate, supporto attivo |
| Milestone 5 | `scale-up` | Estensione ad altre linee o siti |

Alternanze evitate: sistema/piattaforma/soluzione senza criterio, stabilimento/fabbrica
usati indifferentemente, macchina/asset confusi, canone/fee/subscription mescolati.

---

## 2. Architettura di prodotto

| Nome | Che cosa indica | Stato | Sales deck | Dossier |
|---|---|---|---|---|
| D.Factory | Soluzione, nome contrattuale | Disponibile | Ovunque | Ovunque |
| MAPST 4.0 | Piattaforma tecnologica | Disponibile | Solo `s03` | `d02`, `d03` |
| Connect | Visibilità e supervisione | Disponibile | `s09` | `d02`, `d04` |
| Insights | Analisi, energia, costo e CO₂ | Disponibile | `s09` | `d02`, `d04` |
| Refyn | Servizi sul dato | **In definizione** | `s09`, non altrove | `d02`, `d04` |

La relazione formale fra marchio, piattaforma e società non è documentata:
`[[PH_T01_ARCHITETTURA_PRODOTTO]]` in `d02`. La pagina descrive la nomenclatura d'uso
e non afferma una gerarchia societaria.

---

## 3. Matrice dei claim

Stati ammessi: `presente negli HTML` · `presente solo nell'assessment` ·
`da validare` · `placeholder` · `non pubblicare` · `roadmap`.

| ID | Claim o termine | Valore canonico | Fonte | Stato | Owner | Sales | Dossier | Note |
|---|---|---|---|---|---|---|---|---|
| C01 | Base installata · clienti | 10 clienti in produzione | HTML v1 | da validare | Commerciale | `s06` | — | Conferma formale prima dell'uso esterno |
| C02 | Base installata · macchine | circa 70 macchine | HTML v1 | da validare | Commerciale | `s06` | — | Non confondere con clienti o casi |
| C03 | Base installata · linee | circa 30 linee | HTML v1 | da validare | Commerciale | `s06` | — | |
| C04 | Mesi di esercizio | 24 mesi | HTML v1 | da validare | Commerciale | `s06` | — | |
| C05 | Installazioni dismesse | 0 | HTML v1 | da validare | Commerciale | `s06` | — | Claim forte: va confermato |
| C06 | Referenza Acmi | citabile o no | HTML v1 | placeholder | Commerciale | `[[PH_15_ACMI_OK]]` | — | Testo, mai logo |
| C07 | Referenza Toyota | citabile o no | HTML v1 | placeholder | Commerciale | `[[PH_13_TOYOTA]]` | — | Testo, mai logo |
| C08 | Caso cliente | struttura pronta, dati assenti | — | placeholder | Commerciale | `[[PH_01_CASO_CLIENTE]]` | `[[PH_T14_CASO_TECNICO]]` | Stesso impianto nelle due letture |
| C09 | Citazione cliente | assente | — | placeholder | Commerciale | `[[PH_02_CITAZIONE_CLIENTE]]` | — | Nessuna frase attribuita senza autorizzazione |
| C10 | Partnership Siemens | — | assessment | **non pubblicare** | Direzione | — | — | Fonte non disponibile. Nessun riferimento nei documenti |
| C11 | Seconda generazione di sviluppo | — | assessment | **non pubblicare** | Direzione | — | — | Fonte non disponibile |
| C12 | Settori oltre F&B | — | assessment | **non pubblicare** | Direzione | — | — | Posizionamento resta su linee F&B multi-linea |
| C13 | Consegna in circa 60 giorni | — | assessment | **non pubblicare** | Delivery | — | — | Fonte non disponibile. I tempi sono dichiarati indicativi |
| C14 | Pricing facility management | — | assessment | **non pubblicare** | Commerciale | — | — | Non trasferibile a linee F&B |
| C15 | Integrazione SAP | — | assessment | **non pubblicare** | Tecnico | — | `d15` come "da verificare" | Nessun nome di prodotto ERP nei documenti |
| C16 | Patent Box | — | assessment | **non pubblicare** | Direzione | — | — | Non è una prova commerciale |
| C17 | Intelligenza artificiale | assente dal prodotto | HTML v1 | presente negli HTML | Tecnico | — | `d04` | Dichiarata come assente, non come roadmap datata |
| C18 | Manutenzione e qualità predittive | non disponibili | HTML v1 | roadmap | Tecnico | — | `d04` | Nessuna data associata |
| C19 | PackML · 17 stati nativi | 17 stati | HTML v1 | presente negli HTML | Tecnico | `s07` | `d04`, `d05`, `d12` | |
| C20 | Modello ridotto | 2 stati | HTML v1 | presente negli HTML | Tecnico | `s07` | `d12` | Per macchine senza standard |
| C21 | Protocolli supportati | elenco assente | — | placeholder | Tecnico | — | `[[PH_T02_PROTOCOLLI_SUPPORTATI]]` | Sostituisce "qualsiasi protocollo" |
| C22 | Porte e flussi di rete | assenti | — | placeholder | Tecnico | — | `[[PH_T03_PORTE_FLUSSI_RETE]]` | |
| C23 | Deployment | on-premise, server del cliente | HTML v1 | presente negli HTML | Tecnico | `s03`, `s11` | `d13` | |
| C24 | Server e sistema operativo | PC industriale Linux del cliente | HTML v1 | presente negli HTML | Tecnico | — | `d13` | |
| C25 | Sizing del server | assente | — | placeholder | Tecnico | — | `[[PH_T04_SIZING_SERVER]]` | |
| C26 | Autenticazione e ruoli | assenti | — | placeholder | Tecnico | — | `[[PH_T05_AUTENTICAZIONE_RUOLI]]` | |
| C27 | Backup e retention | assenti | — | placeholder | Tecnico | — | `[[PH_T06_BACKUP_RETENTION]]` | |
| C28 | Aggiornamenti e patching | assenti | — | placeholder | Tecnico | — | `[[PH_T07_UPDATE_PATCHING]]` | |
| C29 | Logging e audit trail | assenti | — | placeholder | Tecnico | — | `[[PH_T08_LOGGING_AUDIT_TRAIL]]` | |
| C30 | Supporto remoto | assente | — | placeholder | Tecnico | — | `[[PH_T09_SUPPORTO_REMOTO]]` | |
| C31 | Proprietà del dato | dati sul server del cliente, con export | HTML v1 | presente negli HTML | Legale | `s11` | `d13` | Distinto dai diritti di licenza |
| C32 | Licenza a fine contratto | non specificata | — | placeholder | Legale | — | `[[PH_T13_LICENZA_FINE_CONTRATTO]]` | Il dato tuo non implica software per sempre |
| C33 | Zero hardware proprietario | nessun hardware D.Factory a bordo linea | HTML v1 | presente negli HTML | Tecnico | `s03` | `d12` | Qualificato: servono server e, dove manca, sensori |
| C34 | Sensoristica | a carico del cliente, installata dal suo tecnico | HTML v1 | presente negli HTML | Delivery | `s09` | `d14` | |
| C35 | Costo sensoristica | assente | — | placeholder | Commerciale | `[[PH_12_COSTO_SENSORI]]` | — | |
| C36 | Strumentazione MID | dove la norma o il contratto la richiedono | HTML v1 | presente negli HTML | Tecnico | — | `d14` | Separata da ISO 50001 |
| C37 | ISO 50001 | supporta processi coerenti con la norma | HTML v1 | presente negli HTML | Tecnico | — | `d11`, `d14` | Il software non è certificato: la norma riguarda l'organizzazione |
| C38 | Scope 1 e 2 | dati associabili ai fattori emissivi documentati | HTML v1 | presente negli HTML | Tecnico | — | `d11` | |
| C39 | Fattori emissivi e versione | assenti | — | placeholder | Tecnico | — | `[[PH_T11_METODO_FATTORI_GHG]]` | |
| C40 | Campionamento e dati mancanti | assenti | — | placeholder | Tecnico | — | `[[PH_T12_CAMPIONAMENTO_DATI_MANCANTI]]` | |
| C41 | API e formati di export | non definiti | — | placeholder | Tecnico | — | `[[PH_T10_API_FORMATI_EXPORT]]` | |
| C42 | Report ITA ed ENG, PDF, Gantt, vista 3D | disponibili | HTML v1 | presente negli HTML | Tecnico | — | `d15` | |
| C43 | SLA | assenti | — | placeholder | Commerciale | — | `[[PH_08_SLA]]` | |
| C44 | Orari e severità del supporto | assenti | — | placeholder | Commerciale | — | `[[PH_T15_ORARI_SEVERITA_SUPPORTO]]` | |
| C45 | Ore a carico cliente | assenti | — | placeholder | Delivery | `[[PH_07_ORE_CLIENTE]]` | `[[PH_07_ORE_CLIENTE]]` | Stesso token nei due documenti |
| C46 | Durata dell'audit | assente | — | placeholder | Commerciale | `[[PH_04_AUDIT_DURATA]]` | — | Blocca la call to action |
| C47 | Costo dell'audit | assente | — | placeholder | Commerciale | `[[PH_05_AUDIT_COSTO]]` | — | Blocca la call to action |
| C48 | Partecipanti all'audit | assenti | — | placeholder | Commerciale | `[[PH_06_AUDIT_PARTECIPANTI]]` | — | Blocca la call to action |
| C49 | Forbice di prezzo | assente | — | placeholder | Commerciale | `[[PH_03_FORBICE_PREZZO]]` | — | Il titolo di `s09` non promette un numero |
| C50 | Agevolazione | assente | — | placeholder | Commerciale | `[[PH_11_AGEVOLAZIONE]]` | — | |
| C51 | Durata e rinnovo del contratto | assenti | — | placeholder | Legale | `[[PH_09_CONTRATTO]]` | — | |
| C52 | Reversibilità del pilota | assente | — | placeholder | Commerciale | `[[PH_10_REVERSIBILITA]]` | — | Criterio di uscita della fase 03 |
| C53 | Margine per ora di linea | assente | — | placeholder | Cliente | `[[PH_16_MARGINE_ORA]]` | — | Senza questo non si scrive un ritorno |
| C54 | Dominio | assente | — | placeholder | Marketing | `[[PH_17_DOMINIO]]` | `[[PH_17_DOMINIO]]` | Mai usato come `href` |
| C55 | Prenotazione audit | assente | — | placeholder | Commerciale | `[[PH_18_BOOKING]]` | `[[PH_18_BOOKING]]` | Mai usato come `href` |
| C56 | Referente | Pablo Degl'Innocenti · pablo.deglinnocenti@marchianisrl.com | HTML v1 | presente negli HTML | Commerciale | `s12` | `d18` | Identico nei due documenti |
| C57 | Certificazione TÜV SÜD | norma non specificata | HTML v1 | **non pubblicare** | Direzione | — | — | Rimossa nella revisione precedente, non reintrodotta |
| C58 | Vettori energetici | elettricità, gas, vapore, aria compressa, acqua | HTML v1 | presente negli HTML | Tecnico | `s05` | `d09`, `d10`, `d11` | Cinque, sempre gli stessi |

---

## 4. Contenuti del Sales Deck

| # | ID | Tesi | Prova o strumento | Placeholder |
|---|---|---|---|---|
| 01 | `s01_cover` | Dalla linea al margine, nello stesso dato | Vista hero con stati, OEE e costo per pezzo | — |
| 02 | `s02_perche_adesso` | Capacità, energia e margine si perdono nello stesso punto | Tre punti ciechi e tre trigger | — |
| 03 | `s03_come_funziona` | Quattro sorgenti, un solo modello | Flusso a tre nodi, quattro rassicurazioni | — |
| 04 | `s04_tre_decisioni` | Lo stesso dato serve a tre ruoli | Domanda, dato, decisione per ruolo | — |
| 05 | `s05_prodotto_in_azione` | Quello che succede in linea diventa una decisione | Quattro letture di prodotto | — |
| 06 | `s06_prova` | Base installata in esercizio da anni | Metriche e caso da validare | 01, 02, 13, 15 |
| 07 | `s07_perche_dfactory` | Quattro differenze verificabili | Quattro micro-diagrammi | — |
| 08 | `s08_business_case` | Il ritorno si misura su due leve | Formula per leva, input dichiarati | 03, 16 |
| 09 | `s09_offerta` | Come si compone l'offerta | Tre livelli con stato, struttura economica | 03, 09, 11, 12 |
| 10 | `s10_audit_scala` | Dall'audit alla scala, con criteri di uscita | Quattro passi, condizioni dell'audit | 04, 05, 06, 07, 10 |
| 11 | `s11_faq` | Le obiezioni si risolvono prima del contratto | Quattro risposte con rimando tecnico | — |
| 12 | `s12_cta` | Fissiamo l'audit della prima linea | Cosa guardiamo, cosa ricevi, contatto | 04, 05, 17, 18 |

## 5. Contenuti del Dossier Tecnico

| # | ID | Domanda tecnica | Sezione | Placeholder |
|---|---|---|---|---|
| 01 | `d01_cover` | A chi serve e cosa copre | — | — |
| 02 | `d02_architettura_prodotto` | Come si chiamano le cose e cosa è disponibile | 1 | T01 |
| 03 | `d03_architettura_tecnica` | Da dove arrivano i dati e dove risiedono | 1 | T02, T03 |
| 04 | `d04_capability` | Cosa è disponibile, opzionale, roadmap | 1 | — |
| 05 | `d05_supervisione` | Cosa vedo in tempo reale e da dove viene | 2 | — |
| 06 | `d06_oee_fermi` | Perché macchina ferma non è linea ferma | 2 | — |
| 07 | `d07_velocita_qualita` | Come si vedono i micro-fermi | 2 | — |
| 08 | `d08_multi_impianto` | Come si legge tutto l'impianto | 2 | — |
| 09 | `d09_distribuzione_energia` | Dove finisce l'energia che entra | 2 | — |
| 10 | `d10_costo_co2_stato` | Quanto costa un pezzo e quanto si spende da fermo | 2 | — |
| 11 | `d11_metodo_misura` | Come si arriva a quei numeri | 3 | T11, T12 |
| 12 | `d12_brownfield` | Funziona sul mio parco macchine | 3 | T02, T03 |
| 13 | `d13_deployment_security` | Cosa chiede al mio IT | 3 | T03…T09, T13 |
| 14 | `d14_sensori` | Dove serve misurare bene | 3 | — |
| 15 | `d15_output_integrazioni` | In che forma esce il dato | 3 | T10 |
| 16 | `d16_delivery_raci` | Chi fa cosa e in quanto tempo | 4 | 07 |
| 17 | `d17_caso_tecnico` | Com'è andata davvero su un impianto | 4 | T14 |
| 18 | `d18_supporto_audit` | Cosa serve per partire e per restare in esercizio | 4 | 08, 17, 18, T07, T09, T15 |

---

## 6. Matrice di coerenza incrociata

Verificata automaticamente da `quadro/qa_v2.py`, sezione "coerenza incrociata".

| Elemento | Sales Deck | Dossier | Verifica |
|---|---|---|---|
| Nomi dei livelli | `s09` | `d02`, `d04` | Connect, Insights, Refyn in entrambi |
| Stato di Refyn | in definizione | in definizione | Stessa formula |
| PackML | 17 stati | 17 stati | Stesso numero |
| Modello ridotto | 2 stati | due stati | Stesso concetto |
| On-premise | rassicurazione | specifica completa | Presente in entrambi |
| Proprietà del dato | server del cliente | server del cliente + licenza distinta | Il deck non promette la licenza |
| Sensoristica | a carico tuo | a carico tuo | Stessa attribuzione |
| Caso cliente | risultato commerciale | implementazione tecnica | Stesso impianto, due letture |
| Timeline | audit → pilota → validazione → scala | 8 passi + 5 milestone | Il deck non parla di go-live come primo dato |
| Contatto | Pablo Degl'Innocenti | Pablo Degl'Innocenti | Una sola occorrenza per documento |
| Dominio e booking | token | stesso token | Identici |
| Vettori energetici | cinque | cinque | Stesso elenco |
| Link reciproci | 3 verso il dossier | 4 verso il deck | Tutti risolti su ancore esistenti |

---

## 7. Dati mancanti, in ordine di urgenza

1. `PH_04_AUDIT_DURATA`, `PH_05_AUDIT_COSTO`, `PH_06_AUDIT_PARTECIPANTI` · senza
   questi la chiamata all'azione chiede un impegno senza dirne il prezzo.
2. `PH_16_MARGINE_ORA` e `PH_03_FORBICE_PREZZO` · senza, il business case resta una
   formula senza risultato.
3. `PH_01_CASO_CLIENTE`, `PH_02_CITAZIONE_CLIENTE`, `PH_T14_CASO_TECNICO` · la prova
   è oggi una struttura vuota in entrambi i documenti.
4. `PH_T02`…`PH_T13` · il dossier non può essere consegnato a un IT senza almeno
   protocolli, porte, sizing, autenticazione, backup e licenza.
5. `PH_08_SLA`, `PH_T15_ORARI_SEVERITA_SUPPORTO` · il supporto resta indefinito.
6. `PH_17_DOMINIO`, `PH_18_BOOKING` · nessun URL è stato inventato: i token restano
   chip, mai `href`.
