# Sales deck D.Factory — changelog revisione v2

Da un documento unico di 35 slide costruito per essere presentato, a **due documenti
costruiti per essere inviati**: un sales deck di 14 slide che si manda a freddo, e un
dossier tecnico di 16 che si manda dopo l'audit o all'IT su richiesta.

| File | Contenuto | Uso |
|---|---|---|
| `DFactory_SalesDeck.html` + `.pdf` | 14 slide | Si manda al prospect, a freddo |
| `DFactory_DossierTecnico.html` + `.pdf` | 16 slide | Si manda dopo l'audit, o all'IT |

Mappatura completa id DOM → destinazione in `deck/MAPPATURA.md`, prodotta prima delle
modifiche. Contact sheet di QA in `deck/out/sales/` e `deck/out/dossier/`.

---

## 1. Slide rimosse

| Slide | Motivo |
|---|---|
| **Quattro forze convergono** (`s02_perche_ora`) | Tre argomenti su quattro erano di compliance, mentre la slide stessa dichiarava che non è la compliance a far comprare. Scope 3 e Omnibus/CSRD erano la stessa forza detta due volte. E "senza quei dati resti fuori" è falsificabile da un lettore che quella richiesta non l'ha mai ricevuta: un'apertura smentibile svaluta tutto il resto. |
| **Quanto ti costa non saperlo** (`s04_gap`) | Il benchmark "82-85% classe alta" viene dalla tradizione TPM ed è contestato nel packaging multi-formato, dove i cambi formato lo rendono irrealistico. Un capo stabilimento esperto lo legge come vendita. Recuperata una sola riga in slide 04, riformulata come gap rispetto al target dichiarato dal cliente. |
| **Matrice competitiva** (`s24_posizionamento`) | Sei pallini pieni su sette, criteri scelti dal venditore, e un criterio che coincide con la propria definizione di sé. **Fuori da entrambi i file.** Conservata in `deck/src/_interno_matrice.html` come materiale interno per le situazioni competitive dichiarate. |

## 2. Slide fuse

| Nuova slide | Origine | Nota |
|---|---|---|
| **05 · Cos'è** | `s05_soluzione` + `s08_platform` | La prima screenshot passa da pagina 9/18 a pagina 5/14. In un invio a freddo era l'asset più persuasivo del documento, e una quota di lettori non ci arrivava. |
| **08 · Perché noi** | `s06_refyn` + `s25_differenziatori` + due righe da `s27_gruppo` | Solo capacità esistenti oggi. Il €145M di gruppo esce dall'evidenza gialla e diventa una riga di continuità del fornitore. |
| **11 · Come si paga e quanto** | `s10b_modello` + `s22_pacchetti` | I tre livelli non avevano bisogno di una slide propria: stanno in una riga dentro la struttura di prezzo. |

## 3. Slide nuove

| Slide | Cosa risolve |
|---|---|
| **03 · È per te se + cinque trigger** (`s03_trigger`) | Sostituisce l'apertura macro. Qualificazione esplicita del destinatario, che nel deck non c'era, e i cinque modi reali in cui un'azienda F&B arriva a comprare. Nessuna statistica in apertura. |
| **09 · Come entra in casa tua** (`s09c_integrazione`) | Le sei domande che fermano davvero una trattativa industriale vivevano tutte in appendice: IT e rete, sovranità del dato, macchine miste, tempi, impegno richiesto al cliente, assistenza. |

## 4. Slide spostate

- **Il quadro in una pagina** passa dalla posizione 17 alla **02**. Chi scorre un PDF vuole
  la mappa subito e legge tutto il resto con quella in mano; in fondo non serviva a nessuno.
  Rimosso l'occhiello "da girare a chi non era in sala": il deck ora si manda, non si presenta.

## 5. Claim corretti

| Correzione | Prima | Adesso |
|---|---|---|
| **Il differenziale** | La slide-eroe a fondo pieno era dedicata a Refyn, marcato "in via di definizione" | Le quattro capacità che funzionano già: energia misurata per stato macchina, OEE buffer-aware, PackML nativo, un solo modello dati. Refyn resta nominato come strato di servizi del tier alto, una riga in coda |
| **Il churn zero** | "0 clienti che hanno abbandonato": su una base di 10 non è una statistica, e si legge come lock-in | "0 installazioni dismesse dopo l'avvio", letto come profondità d'uso: il sistema è la fonte su cui le squadre decidono ogni giorno |
| **Benchmark OEE** | Confronto con un world class astratto | Gap rispetto al target dichiarato dal cliente. Il confronto resta interno, non normativo |
| **Il dato +55%** | Compariva due volte, senza quantificare una perdita evitabile | Rimosso con le slide che lo ospitavano. Zero occorrenze |
| **La sensoristica** | "€0 di hardware proprietario nostro", presentato come vantaggio | Riformulata come costo del cliente: spesso i contatori ci sono già, l'audit lo dice prima di qualsiasi impegno, e l'ordine di grandezza è un placeholder aperto |
| **Certificazione TÜV SÜD** | Riga senza norma specifica | **Rimossa.** Senza la norma era troppo vaga; il §6.8 del brief prevede la rimozione come esito, quindi non è stata flaggata ma tolta |
| **Toyota** | "Toyota / automotive" secco in un deck posizionato su F&B | Placeholder per la ragione sociale esatta |
| **Acmi** | Casellina grigia come le altre | Riquadro dedicato: un costruttore di linee che usa il sistema è la referenza più forte del set |

## 6. Aggiunte di sostanza

- **Anti-lock-in dichiarato**: il sistema è on-premise, quindi lo storico resta sul server
  del cliente anche se smette di pagare. Non era scritto da nessuna parte ed è vero.
- **La quinta obiezione**: "ce lo facciamo in casa con Excel e Power BI", che nel
  mid-market italiano è il concorrente numero uno. Power BI legge quello che qualcuno ha
  già raccolto e strutturato; il lavoro vero è il tag mapping e il modello dati.
- **L'energia come porta d'ingresso autonoma**: era in appendice, ora è dichiarata in
  slide 05. È l'ingresso a più basso attrito, con un budget suo.
- **Ponte lessicale**, una riga sola: chi ha il problema cerca "monitoraggio produzione",
  "OEE", "monitoraggio energetico". "Supervisione 4.0" resta l'identità, ma ora il lettore
  sa dove collocarla a budget.
- **Due scenari di margine orario** sul ROI invece di uno: 400 €/h è plausibile su una
  linea veloce e fuori scala su molte altre, e un esempio fuori scala sembra costruito.
- **Reversibilità del pilota**: cosa succede se i numeri non arrivano.

## 7. Placeholder ancora aperti

**Diciassette token visibili nel deck, nessuno riempito con dati dedotti.** Sono resi con
lo stile placeholder (riquadro tratteggiato, tratteggio giallo) e restano leggibili nel PDF.

| Token | Slide | Cosa serve |
|---|---|---|
| `PH_01_CASO_CLIENTE` | 07 | Caso con numeri prima/dopo: settore, n. linee, metrica di partenza, metrica dopo, orizzonte. Anche anonimizzato |
| `PH_02_CITAZIONE_CLIENTE` | 07 | Una frase di un cliente reale, con ruolo e azienda o ruolo e settore |
| `PH_03_FORBICE_PREZZO` | 11 | Range primo anno su linea pilota + canone annuo per linea attivata |
| `PH_04_AUDIT_DURATA` | 13 | Durata dell'audit di linea |
| `PH_05_AUDIT_COSTO` | 13 | Costo dell'audit. **Se è gratuito è la leva di conversione più forte del documento** |
| `PH_06_AUDIT_PARTECIPANTI` | 13 | Chi serve in sala lato cliente, e per quanto |
| `PH_07_ORE_CLIENTE` | 09 | Ore di impegno richieste al cliente in attivazione |
| `PH_08_SLA` | 09 | Assistenza: copertura, tempo di risposta, canale |
| `PH_09_CONTRATTO` | 11 | Durata dell'impegno ricorrente, rinnovo, disdetta |
| `PH_10_REVERSIBILITA` | 13 | Cosa succede se il pilota non dà i numeri attesi |
| `PH_11_AGEVOLAZIONE` | 11 | Se e a quali condizioni rientra nelle misure 4.0. **Da verificare con un fiscalista** |
| `PH_12_COSTO_SENSORI` | 11 | Ordine di grandezza della sensoristica a carico del cliente |
| `PH_13_TOYOTA` | 07 | Ragione sociale esatta dell'entità Toyota cliente |
| `PH_15_ACMI_OK` | 07 | Conferma che si può raccontare Acmi come costruttore che usa il sistema |
| `PH_16_MARGINE_ORA` | 12 | Secondo scenario di margine orario, per una linea più lenta |
| `PH_17_DOMINIO` | 14 | Dominio del sito nuovo |
| `PH_18_BOOKING` | 14 | Link di prenotazione diretta dell'audit |

`PH_14_TUV` non compare: la riga sulla certificazione è stata rimossa invece che flaggata,
come previsto dal brief in assenza della norma specifica.

**Le più urgenti sono `PH_04`, `PH_05` e `PH_06`:** finché mancano, la slide 13 è la call to
action del documento e non è completa.

## 8. QA

`deck/qa.py` esegue la checklist del brief e va tenuto a zero fallimenti. Stato attuale:
**tutti i controlli superati**, inclusi struttura (14 slide, sintesi in posizione 02, prima
screenshot entro la 05, chiusura unica), contenuto (nessuna capacità di roadmap presentata
come esistente, Refyn sempre flaggato, quinta obiezione presente, ponte lessicale una volta
sola), placeholder (nessun token grezzo, nessun `[confermare]` residuo), stile (zero
trattini lunghi, una sola costruzione "Non X. Y.", nessun termine vietato, nessun MES/MOM) e
tecnica (zero chiamate a CDN, font embeddati, PDF a 960×540 pt).

La costruzione "Non X. Y." è assegnata deliberatamente a un solo punto, in slide 09:
*"Non è un abbonamento che tiene i dati in ostaggio. È software che gira su un server tuo."*
