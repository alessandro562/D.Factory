# D.Factory · Decisioni aperte v8

Quello che va deciso prima che la V8 possa essere chiamata definitiva. Copre la Fase 0 del
§11 e le tre tabelle del §10.

Ogni riga ha un owner e una conseguenza. La conseguenza non è generica: è la slide o la
pagina che oggi non si può chiudere.

---

## 1. Commerciale · dieci decisioni

| # | decisione | domanda da chiudere | owner | che cosa sblocca |
|---|---|---|---|---|
| C1 | **Audit** | prezzo, durata, partecipanti, output | Direzione commerciale | deck 14, 15, 16 · dossier 13 |
| C2 | **Pilot** | prezzo, durata, criteri, credito sul contratto | Commerciale + Delivery | deck 15 · dossier 13 |
| C3 | **Setup** | fascia prima linea e linee successive | Delivery + commerciale | deck 14 · A3 |
| C4 | **Connect** | canone annuale e inclusioni | Commerciale | deck 10, 14 · A1, A3 |
| C5 | **Insight** | canone annuale e differenziale su Connect | Commerciale | deck 10, 14 · A1, A3 |
| C6 | **Refyn** | modello economico durante lo sviluppo e dopo il rilascio | Direzione prodotto | deck 10, 14 · A1, A3 |
| C7 | **Servizi** | inclusi, opzionali, frequenze e prezzi | Commerciale | deck 11 · A2, A3 |
| C8 | **Contratto** | durata, rinnovo, recesso, indicizzazione | Legale + commerciale | A3 |
| C9 | **Supporto** | standard e premium, con SLA | Delivery | dossier 14 · annesso A3 |
| C10 | **Contatto** | nome, ruolo, email, telefono, URL | Direzione | deck 16 · cover dossier |

**C4 e C5 sono le due che pesano di più.** Il differenziale fra i due canoni è ciò che
rende leggibile la scala: senza, la slide 10 spiega *per chi* è ogni livello ma non *quanto
costa* passare da uno all'altro, che è la domanda vera.

---

## 2. Tecnico · dieci aree

| # | area | dati necessari | owner | che cosa sblocca |
|---|---|---|---|---|
| T1 | **Deployment** | on-premise, VM, cloud o modelli supportati | Tecnico | dossier 08 · annesso A2 |
| T2 | **Server** | OS, CPU, RAM, storage e sizing per tre taglie | Tecnico | annesso A2 |
| T3 | **Rete** | porte, protocolli, direzioni, segmentazione | Tecnico | dossier 08 · annesso A1 |
| T4 | **Accesso** | autenticazione, ruoli, accesso remoto | Tecnico | annesso A3 |
| T5 | **Sicurezza** | logging, patching, cifratura, vulnerability management | Tecnico | annesso A3 |
| T6 | **Continuità** | backup, retention, restore, disaster recovery | Tecnico | annesso A3 |
| T7 | **Dati** | proprietà, export, conservazione, fine contratto | Legale + tecnico | annesso A3 |
| T8 | **Licenza** | diritti d'uso e condizioni contrattuali | Legale | annesso A3 |
| T9 | **Compatibilità** | PLC, versioni, protocolli e dispositivi testati | Tecnico | annesso A1 |
| T10 | **API** | disponibilità, autenticazione, limiti, formati | Tecnico | dossier 12 · annesso A1 |

**T9 è la più costosa da chiudere e la più preziosa.** Un catalogo di compatibilità
verificata è l'unica cosa che trasforma «approccio multi-vendor» da affermazione a prova.
Finché non esiste, l'annesso A1 non si pubblica.

---

## 3. Aziendale · undici voci

| # | voce | owner | oggi |
|---|---|---|---|
| A1 | denominazione legale | Legale | assente da tutti i documenti |
| A2 | sede | Legale | assente |
| A3 | contatti ufficiali | Direzione | assente |
| A4 | relazione con il gruppo | Direzione | assente |
| A5 | anno di fondazione | Direzione | assente |
| A6 | team e responsabilità | Direzione | assente |
| A7 | base installata validata | Direzione | assente |
| A8 | clienti citabili | Direzione + Legale | assente |
| A9 | settori approvati | Direzione | assente |
| A10 | referenze e testimonial | Direzione + Legale | assente |
| A11 | proprietà intellettuale o certificazioni utilizzabili | Legale | assente |

**Nessuna di queste undici voci compare oggi nei documenti**, ed è una scelta, non una
dimenticanza: il brief vieta di inventarle e la V7 costruisce la credibilità su tre prove
strutturali. Ma undici voci assenti su undici significa che la slide «perché D.Factory»
regge su argomenti e non su fatti verificabili — e in una gara con un concorrente che ha
referenze, questo si paga.

Se anche solo **A4, A5 e A7** fossero disponibili e autorizzate, la slide 12 cambierebbe
natura.

---

## 4. Asset · sette elementi

| # | asset | owner | dove entrerebbe |
|---|---|---|---|
| S1 | screenshot reali del prodotto | Tecnico + Marketing | deck 05, 08, 09 · dossier 04, 05, 12 |
| S2 | foto di un impianto o di un quadro | Marketing | deck 01, 12 · dossier 01, 07 |
| S3 | un report reale esportato | Tecnico | dossier 12 |
| S4 | schema di rete reale anonimizzato | Tecnico | dossier 08 |
| S5 | un caso tecnico autorizzato | Direzione + Legale | deck 12 |
| S6 | logo ufficiale nella versione corretta | Marketing | tutti i canvas |
| S7 | eventuali loghi cliente autorizzati | Legale | deck 12 |

**S1 è la più importante.** Oggi il 100 % delle evidenze dei due documenti è ricostruito e
dichiarato tale. Il §9.6 del brief dice che le ricostruzioni possono restare ma non devono
occupare tutte le evidenze: con anche due o tre schermate vere, l'impianto grafico non
cambia — cambia che cosa il lettore crede.

---

## 5. La validazione che non costa niente e vale molto

| # | decisione | owner |
|---|---|---|
| V1 | **plausibilità del dataset illustrativo** | Commerciale + Tecnico |

Tutti i numeri dei due documenti discendono da nove parametri:

```
500 pz/min · margine 0,14 €/pz · 95 kW in marcia · 38 kW a linea ferma
0,22 €/kWh · 0,35 kgCO₂e/kWh · 46 settimane
disponibilità 94,6 % · prestazione 79 % · qualità 95,6 %
```

Sono stati scelti per rendere l'aritmetica verificabile, non presi da un impianto reale.
Serve **una persona che conosca una linea F&B** e dica se sono plausibili. È mezz'ora di
lavoro e protegge la slide del valore, che è quella su cui il controllo di gestione del
cliente si ferma per primo.

Se i parametri non reggono, cambia un file di nove numeri e tutti gli importi dei due
documenti si ricalcolano: l'aritmetica è già scritta per essere rifatta.

---

## 6. Due decisioni di posizionamento

| # | decisione | owner |
|---|---|---|
| P1 | **«food & beverage» oppure «linee industriali»** | Direzione commerciale |
| P2 | **nome del dossier: «Dossier tecnico» oppure «Dossier di soluzione»** | Direzione |

Su **P2** il brief è netto: finché le domande 2–9 dei criteri di accettazione tecnica
restano vuote, il documento va chiamato *Dossier di soluzione / pre-design*. Nei prototipi
V8 la copertina porta **«Dossier di soluzione»**, e tornerà a «Dossier tecnico» il giorno
in cui gli annessi A1, A2 e A3 sono compilati. È una parola sola, ma dice al lettore
tecnico che cosa aspettarsi — e non promette una specifica che il documento non contiene.

---

## 7. Che cosa succede se nulla di tutto questo arriva

I due documenti restano quello che sono oggi: **un pitch visivamente forte e un dossier di
pre-design onesto**. Utilizzabili per aprire una conversazione, non per chiuderla.

Il salto da lì a «coppia commerciale definitiva» non è un lavoro di grafica. È
l'inserimento di **dieci decisioni commerciali, dieci aree tecniche e undici voci
aziendali** in una struttura che li aspetta già.
