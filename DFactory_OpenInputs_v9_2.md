# D.Factory · Open Inputs V9.2

Tutto quello che manca, e che cosa costa ciascuna mancanza.

**221 campi aperti**, dei quali **58 bloccanti** perché appartengono a uno dei
cinque gate. Gli altri 163 migliorano i documenti; nessuno di loro tiene ferma
una consegna.

Il registro completo campo per campo è in
`DFactory_PlaceholderRegister_v9_2.md`. Questo documento dice invece **chi deve
fare che cosa, in che ordine, e che cosa si sblocca**.

---

## 1. In una riga

| | stato |
|---|---|
| Sales Deck | **presentabile dal vivo**, non inviabile: manca il referente |
| Dossier tecnico | **preliminare per assessment e solution design**, non specifica per approvazione IT |
| Business case | **formula sì, risultato no**: il dataset non è validato |
| Prezzi | **struttura sì, importi no** |
| Asset reali | **zero su due**: tutte le viste sono ricostruzioni dichiarate |
| Caso cliente | **assente**, e non inventato |

---

## 2. I cinque gate, in ordine di ritorno

L'ordine non è l'ordine dei nomi: è quanto ciascuno sblocca rispetto a quanto
costa chiuderlo.

### 1° · G1 · Identità e CTA — 9 campi · `GLOBAL`

**Costa una riunione da trenta minuti. Sblocca l'invio del deck.**

| campo | che cosa serve | owner |
|---|---|---|
| `PH_COMPANY_LEGAL_NAME` | denominazione sociale esatta, come in visura | Direzione |
| `PH_CONTACT_NAME` · `PH_CONTACT_ROLE` · `PH_CONTACT_EMAIL` | il referente che riceve le risposte | Commerciale |
| `PH_AUDIT_NAME` | come si chiama l'audit nella proposta | Commerciale |
| `PH_AUDIT_DURATION` | quanto dura la sessione iniziale | Commerciale |
| `PH_AUDIT_PARTICIPANTS` · `PH_AUDIT_INPUTS` · `PH_AUDIT_DELIVERABLES` | chi partecipa, che cosa portare, che cosa si restituisce | Commerciale + Tecnico |

Finché resta aperto: la CTA c'è, i quattro blocchi ci sono, il referente no.
Il deck si presenta dal vivo e non si manda da solo. **`accept92.py` emette il
warning globale a ogni build.**

### 2° · G3 · Dataset — 12 campi · `SECTION`

**Costa una settimana di dati di una linea vera. Sblocca il business case.**

I dodici parametri sono in appendice A5 della working edition, con origine e
stato. Oggi sono tutti `OPEN` e tutti dichiarati illustrativi.

Finché resta aperto, dalla client edition escono:

- 309.120 € — costo annuo della prima causa
- 154.560 € — capacità recuperabile se la causa si dimezza
- 810 € — energia evitabile
- l'intera appendice A5

Restano la formula, la settimana osservata e i numeri del turno, che nello
scenario sono coerenti fra loro e verificabili a mano.

> La V9.1 aveva un difetto qui: i tre valori erano **scritti in lettere** nel
> testo alternativo della slide 11 e uscivano nella client edition senza che il
> controllo se ne accorgesse. Corretto, e il controllo adesso cerca entrambe le
> forme.

### 3° · G2 · Modello commerciale — 10 campi · `SECTION`

**Costa una decisione, non un'informazione. Sblocca l'appendice pricing.**

| campo | che cosa si decide |
|---|---|
| `PH_AUDIT_PRICE` · `PH_SETUP_FIRST_LINE` | le due voci una tantum |
| `PH_SITE_BASE_FEE` · `PH_CONNECT_ANNUAL_FEE` · `PH_INSIGHT_ANNUAL_FEE` · `PH_ADDITIONAL_LINE_FEE` | il canone, per sito, per livello, per linea successiva |
| `PH_REFYN_PRICING_MODEL` | Refyn: pilot dedicato con quotazione sul perimetro, o listino |
| `PH_SERVICES_INCLUDED` · `PH_SERVICES_OPTIONAL` | la colonna incluso/opzionale dell'appendice A2 |
| `PH_CONTRACT_TERM` · `PH_RENEWAL_TERMS` | durata e rinnovo |

Finché resta aperto: `a3_pricing` non entra nella client edition, la slide 12
chiude con «la proposta economica viene costruita sul perimetro validato», e la
quarta colonna dell'appendice A2 dice «in proposta» su tutte e nove le righe.

### 4° · G4 · Requisiti tecnici — 18 campi · `SECTION`

**Costa una sessione con l'IT. Sblocca il titolo «Dossier tecnico».**

Deployment, sistema operativo, CPU, RAM, storage, protocolli, porte, direzione
dei flussi, policy di sola lettura, autenticazione, ruoli, backup, retention,
audit log, supporto remoto, proprietà dei dati, licenza, dati a fine contratto.

Finché resta aperto:

- il dossier si chiama **«Dossier tecnico preliminare per assessment e solution
  design»**, e la condizione di build n. 4 impedisce di chiamarlo diversamente;
- l'annesso A2 mostra il metodo di dimensionamento, non i valori;
- l'annesso A3 è «per la raccolta dei requisiti»;
- l'annesso A1 ha tutti gli esiti a «da verificare».

Il materiale per prepararla è in `DFactory_ITOT_Baseline_v9_1.md`.

### 5° · G5 · Evidenza — 8 campi · `NONE`

**Costa un'autorizzazione e un'anonimizzazione. Sblocca l'invio a freddo.**

Servono **due** elementi fra screenshot reale, report reale, schema di linea,
foto di installazione, fatto aziendale verificato, caso cliente. Siamo a zero.

Non blocca l'uso dal vivo, dove chi presenta è l'evidenza. Blocca il passaggio
in procurement.

### Gate del caso cliente · `CASE_STUDY_READY` · `PAGE`

Otto elementi, tutti insieme: autorizzazione, cliente o anonimizzazione,
problema, baseline, intervento, periodo osservato, risultato, metodologia.

Finché non è `APPROVED`, `v14_caso` non entra nella client edition. Lo scenario
illustrativo **non** viene trasformato in caso cliente: il §20.4 lo vieta, e
sarebbe comunque la cosa più facile da smontare in una riunione.

---

## 3. Che cosa non è un input aperto

Perché il 10% finale resti un 10% e non diventi un secondo progetto, vale la
pena scrivere che cosa è **chiuso**.

- La struttura: 13 slide core + 4 appendici, 14 pagine + 4 annessi.
- Il sistema visuale: palette, font, canvas, template, navigazione, uso del giallo.
- La narrativa: la sequenza del deck e le quattro sezioni del dossier.
- L'architettura commerciale: Connect, Insight, Refyn, cumulativi, con i servizi
  attivabili su tutti e tre.
- Il copy master: definizione, promessa, problema, differenziatore, brownfield,
  software e servizi, CTA.
- Le formulazioni prudenti: sola lettura, residenza dei dati, ERP, ISO 50001,
  compatibilità, OEE di linea.
- Il metodo di calcolo dello scenario: le formule sono scritte, i parametri no.

---

## 4. Ordine di lavoro consigliato

| # | azione | chi | sblocca |
|--:|---|---|---|
| 1 | riunione di trenta minuti su G1 | Direzione + Commerciale | il deck diventa inviabile |
| 2 | scelta di due asset reali e loro anonimizzazione | Marketing + Legale | G5, l'invio a freddo |
| 3 | una settimana di dati da una linea reale | Tecnico | G3, il business case |
| 4 | decisione sul modello economico | Direzione | G2, l'appendice pricing |
| 5 | sessione con l'IT del primo cliente | Tecnico + IT | G4, il dossier tecnico |
| 6 | revisione legale su proprietà dei dati e licenza | Legale | la pubblicazione del claim `proprieta` |

I passi 1 e 2 sono i soli che dipendono solo da noi. Il 3 e il 5 richiedono un
cliente disponibile, e sono la ragione per cui il dossier è preliminare.

---

## 5. Che cosa manca ai documenti, e che cosa manca al prodotto

Vale la pena tenerli separati.

**Manca ai documenti** — prezzi, contatto, dataset validato, specifiche IT/OT,
asset reali, caso cliente. Sono i sei del §0 del master, e sono la ragione del
10% residuo.

**Manca al prodotto** — Refyn è un modulo avanzato in sviluppo, e i documenti lo
dicono una volta per ciascuno, senza inventare funzioni e senza roadmap. Non è
un input aperto: è uno stato dichiarato.
