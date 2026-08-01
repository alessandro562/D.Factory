# D.Factory · Open Inputs v5

Cosa manca per rendere i due documenti utilizzabili in una trattativa reale. Ordinato per
impatto, non per facilità.

---

## P0 · bloccanti

Senza questi, i documenti restano una proposta di architettura, non un'offerta.

| # | Input | Owner | Blocca | Cosa cambia |
|---|---|---|---|---|
| 1 | **Perimetro esatto di Connect** | Prodotto + Commerciale | Deck A1, dossier 06 | Oggi la matrice è una proposta ragionata. Con il perimetro approvato diventa un listino di funzioni |
| 2 | **Perimetro esatto di Insight** | Prodotto + Commerciale | Deck A1, dossier 06 | Dove finisce Connect e dove comincia Insight decide il salto di prezzo |
| 3 | **Refyn MVP approvato** | Prodotto | Dossier 15, 16, 17 | Le tre pagine mostrano quattro oggetti. Se il primo rilascio ne contiene due, quelle pagine promettono troppo |
| 4 | **Stato pilot reale dei nuovi moduli** | Prodotto | Ovunque compare "pilot release" | Se non esiste un cliente pilota attivo, il termine va cambiato |
| 5 | **Durata dell'audit** | Commerciale | Deck 11 | Con questa la CTA torna contrattuale |
| 6 | **Costo dell'audit** | Commerciale | Deck 11 | Idem. E va deciso se è accreditato sul progetto |
| 7 | **Partecipanti dell'audit** | Commerciale | Deck 11 | Chi serve in sala determina la fattibilità della data |
| 8 | **Fascia di investimento** | Commerciale | Deck 09, A3 | L'esempio economico resta illustrativo finché non c'è un investimento con cui confrontarlo |
| 9 | **Pricing recurring per modulo** | Commerciale | Deck A1 | Nessun importo compare oggi |
| 10 | **Entitlement dei servizi** | Commerciale | Deck A1, dossier 25 | Cosa è compreso nel canone e cosa si acquista a parte. Oggi tutto è "attivabile" |
| 11 | **SLA** | Commerciale + Delivery | Dossier 29 | Cinque righe su sei sono "da concordare" |
| 12 | **Requisiti IT fondamentali** | Tecnico | Dossier 21, 22 | Vedi §2 |
| 13 | **Relazione tecnica fra nuovo packaging e legacy** | Tecnico | Dossier 03, 30 | Se esiste una migrazione uno-a-uno o va costruita caso per caso |
| 14 | **Conferma su "un contesto operativo unico"** | Tecnico | Deck 03, dossier 04 | Il claim originale è stato riformulato in via prudenziale. Se il modello dati unico esiste davvero, si può tornare alla formulazione forte |

## P1 · alta priorità

| # | Input | Owner |
|---|---|---|
| 15 | Modalità e condizioni della migrazione legacy | Commerciale + Tecnico |
| 16 | Nome legale della società da usare nei rail | Legale |
| 17 | Policy di proprietà dei dati | Legale |
| 18 | Licenza a fine contratto, distinta dalla proprietà del dato | Legale |
| 19 | **Screenshot reali** · vedi §3 | Tecnico + Marketing |
| 20 | Fonte e autorizzazione del claim Siemens | Direzione + Legale |
| 21 | Chiarimento su "70 casi": casi, macchine o clienti | Commerciale |
| 22 | A quale milestone si riferiscono i "60 giorni" | Delivery |
| 23 | Sensoristica: costi indicativi e responsabilità | Delivery |
| 24 | Verifica dell'integrazione ERP su un progetto reale | Tecnico |
| 25 | Fattori emissivi documentati per Scope 1 e 2 | Tecnico |

## P2 · successivi

Benchmarking · Operational Performance Index · funzioni di AI e modelli proprietari ·
simulazioni · cross-client insights · manutenzione e qualità predittive · nuova UI completa ·
landing page · versioni in inglese.

---

## 2. Le diciotto voci IT/OT

Il backlog §9.9 chiede che la pagina 22 sia compilata con dati reali. Oggi nove voci hanno
uno stato e un owner, ma la maggior parte dice "da concordare". Le voci mancanti o incomplete:

| Voce | Stato oggi |
|---|---|
| Protocolli supportati, per modello e versione | Da compilare |
| Porte | Da compilare |
| Direzione dei flussi | Dichiarata: OT → IT, sola lettura |
| Lettura e scrittura | Dichiarata: nessuna scrittura verso le macchine |
| Requisiti del server, sizing per fascia | Da compilare |
| Sistema operativo | Da confermare |
| Autenticazione | Da compilare |
| Ruoli e permessi | Da compilare |
| Backup | Da compilare |
| Retention | Da compilare |
| Patching | Da compilare |
| Logging e audit trail | Da compilare |
| Remote support | Da concordare, disattivabile |
| API | Da definire |
| Licenza | Da definire in contratto |
| Fine contratto | Da definire in contratto |
| Disaster recovery | **Non ancora nel documento** |
| Disponibilità e SLA | **Non ancora nel documento** |

Le ultime due vanno aggiunte alla pagina 22 appena esiste una posizione da dichiarare.

**Finché questa tabella non è compilata, non si dichiara il dossier "pronto per IT".** È
pronto per la riunione in cui queste voci si compilano.

## 3. Gli otto asset reali

Il backlog §11 li mette in priorità alta. Nessuno è entrato nei v5: tutte le viste restano
ricostruzioni etichettate.

| # | Asset | Dove entrerebbe |
|---|---|---|
| 1 | Screenshot reale MAPST 4.0 | Dossier 03, come prova della capability legacy |
| 2 | Screenshot reale MarEnergy | Dossier 03 e 11 |
| 3 | Foto di una linea installata | Deck 01 o 02, dossier 05 |
| 4 | Schema reale anonimizzato di un impianto | Dossier 05, al posto dello schema tipo |
| 5 | Report reale esportato | Dossier 24 |
| 6 | Dashboard cliente anonimizzata | Deck 04, dossier 07 |
| 7 | Screenshot di allarmi e stati | Dossier 07 |
| 8 | Screenshot di energia, costo e CO₂ | Dossier 12 |

**Regole di etichettatura**, da rispettare quando arriveranno: ogni asset porta fonte,
prodotto, versione, stato, autorizzazione e se i dati sono reali o demo. Uno screenshot
legacy si etichetta "Interfaccia MAPST 4.0 — prodotto legacy", mai come nuova UI di Connect
o Insight.

---

## 4. Decisioni di posizionamento, non dati mancanti

### 4.1 Se le tre domande diventano pubbliche

Il backlog §2 dice che "che cosa sta succedendo / perché e quanto pesa / che cosa conviene
fare" è una struttura interna e non è obbligatorio usarla come slogan. Nei v5 **è stata usata
pubblicamente**, su slide 08 e nel dossier 02: è la cosa che rende comprensibile la scala
cumulativa in tre secondi. Se si preferisce tenerla interna, slide 08 va ridisegnata.

### 4.2 Data Readiness Assessment e audit commerciale

Il deck chiude con "condividiamo il perimetro della prima linea". Il catalogo servizi apre
con un Data Readiness Assessment. **Se sono la stessa cosa va detto**; se non lo sono va
spiegata la differenza, perché un cliente che legge entrambi i documenti se lo chiede.

### 4.3 Il claim riformulato di slide 03

"Un solo modello dati" è stato sostituito da "un contesto operativo unico" perché il primo è
nell'elenco dei claim da validare. La formulazione nuova è più debole e lo si nota. Se il
modello dati unico esiste tecnicamente ed è documentabile, **conviene tornare alla
formulazione forte**: è uno dei pochi punti in cui il prodotto ha un vantaggio strutturale
raccontabile in tre parole.

### 4.4 L'esempio economico

I valori di slide 09 e appendice A3 (4.000 h/anno · 3 punti di OEE · 250 €/h · 180.000 €/anno
· 22 % · 25 %) sono stati scelti per rendere l'aritmetica verificabile, non presi da un
impianto reale. **Vanno validati come plausibili** per una linea F&B tipo: un esempio non
plausibile è peggio di nessun esempio, perché il primo a notarlo è il controllo di gestione
del cliente.
