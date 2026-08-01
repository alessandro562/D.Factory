# D.Factory · Module Feature Matrix v5

Che cosa contiene ogni modulo, da dove viene la capability, in che stato è.

**Struttura cumulativa.** Insight include Connect. Refyn include Connect e Insight. Il segno
✓ indica che la funzione è compresa in quel livello; non si ripete la logica di inclusione
riga per riga.

**Doppio stato.** *Provenienza* dice se la capability esiste già nel legacy. *Stato* dice a
che punto è nel nuovo packaging. I due non coincidono.

Legenda: `PL` proven legacy · `PR` pilot release · `ID` in development · `PD`
project-dependent · `RM` roadmap · `NO` not offered

---

## 1. Produzione e OEE

| Funzione | Connect | Insight | Refyn | Provenienza | Stato |
|---|:--:|:--:|:--:|---|---|
| Acquisizione da PLC, PC e dispositivi | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR · PD per protocollo |
| Stato macchina e stato linea | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Conteggio pezzi, cicli, avanzamento | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Disponibilità, performance, qualità | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| OEE macchina e OEE di linea di base | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Velocità e tempo ciclo | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Allarmi ed eventi | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Storico per turno, giorno, periodo | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Vista multi-macchina e multi-linea | ✓ | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Scomposizione dell'OEE | — | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Pareto delle cause di fermo | — | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Analisi per durata, frequenza, impatto | — | ✓ | ✓ | MAPST 4.0 + sviluppo | PR |
| Micro-fermi | — | ✓ | ✓ | MAPST 4.0 | PL / PR · PD per granularità |
| Velocità reale contro nominale | — | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Analisi scarti e qualità | — | ✓ | ✓ | MAPST 4.0 | PL / PR |
| Confronti turni, formati, prodotti, linee | — | ✓ | ✓ | MAPST 4.0 + sviluppo | PR |
| Trend, deviazioni, analisi multi-periodo | — | ✓ | ✓ | MAPST 4.0 + sviluppo | PR |
| Ranking delle cause per impatto | — | ✓ | ✓ | Net-new | ID |

## 2. Energia e utility

| Funzione | Connect | Insight | Refyn | Provenienza | Stato |
|---|:--:|:--:|:--:|---|---|
| Consumi in tempo reale e storici | ✓ | ✓ | ✓ | MarEnergy | PL / PR |
| Elettricità, gas, vapore, aria compressa, acqua | ✓ | ✓ | ✓ | MarEnergy | PL / PR · PD per copertura |
| Consumo per macchina, linea, reparto, contatore | ✓ | ✓ | ✓ | MarEnergy | PL / PR · PD |
| Consumo per turno e periodo | ✓ | ✓ | ✓ | MarEnergy | PL / PR |
| Baseline e soglie semplici | ✓ | ✓ | ✓ | MarEnergy | PL / PR |
| Intensità energetica di base | ✓ | ✓ | ✓ | MarEnergy | PD · richiede il dato produttivo |
| Energia per stato macchina | Base / cond. | ✓ | ✓ | Legacy + sviluppo | PD |
| Energia in produzione e fuori produzione | — | ✓ | ✓ | Legacy + sviluppo | PD |
| Energia per prodotto, formato, lotto, turno | — | ✓ | ✓ | Legacy + sviluppo | PD |
| Costo energetico per pezzo | — | ✓ | ✓ | MarEnergy + sviluppo | PR · PD |
| CO₂ calcolata o stimata per pezzo | — | ✓ | ✓ | MarEnergy + sviluppo | PR · PD · richiede fattori documentati |
| Consumo e costo per vettore | — | ✓ | ✓ | MarEnergy | PL / PR |
| Heatmap e diagrammi di flusso energia | — | ✓ | ✓ | MarEnergy | PL / PR |
| Deviazioni e allarmi avanzati | — | ✓ | ✓ | MarEnergy + sviluppo | PR |
| Confronto fra linee e periodi | — | ✓ | ✓ | MarEnergy + sviluppo | PR |

## 3. Analisi congiunta produzione–energia

Componente distintiva dell'offerta. Non è marginale e non va trattata come una funzione fra
le altre.

| Funzione | Connect | Insight | Refyn | Provenienza | Stato |
|---|:--:|:--:|:--:|---|---|
| Energia consumata durante i fermi | — | ✓ | ✓ | Legacy + sviluppo | PD |
| Energia per pezzo buono | — | ✓ | ✓ | Legacy + sviluppo | PD |
| Relazione fra stato macchina e consumo | — | ✓ | ✓ | Legacy + sviluppo | PD |
| Costo della riduzione di velocità | — | ✓ | ✓ | Net-new | ID |
| Costo combinato di capacità persa ed energia non produttiva | — | ✓ | ✓ | Net-new | ID |
| Ranking economico delle inefficienze | — | — | ✓ | Net-new | ID |
| Confronto fra perdita locale e impatto complessivo | — | — | ✓ | Net-new | ID |

## 4. Refyn · oggetti e workflow

Nessuna riga di questa sezione è disponibile oggi.

| Funzione | Connect | Insight | Refyn | Provenienza | Stato |
|---|:--:|:--:|:--:|---|---|
| Opportunity Prioritization | — | — | ✓ | Net-new | **ID** |
| Action Management | — | — | ✓ | Net-new | **ID** |
| Benefit Tracking | — | — | ✓ | Net-new | **ID** |
| Guided Improvement Workspace | — | — | ✓ | Net-new | **ID** |
| Distinzione fermo macchina / fermo linea | — | — | ✓ | Net-new | **ID** |
| Modellazione dei polmoni · logica buffer-aware | — | — | ✓ | Net-new | **ID** |
| Propagazione degli eventi e collo di bottiglia | — | — | ✓ | Net-new | **ID** |
| Line balancing | — | — | ✓ | Net-new | **RM** |
| Operational Performance Index | — | — | ✓ | Net-new | **RM** |
| Benchmarking interno: linee, turni, formati, siti | — | — | ✓ | Net-new | **RM** |
| Best operating window e baseline dinamiche | — | — | ✓ | Net-new | **RM** |
| Diagnostica per regole, statistica, deviazioni, pattern | — | — | ✓ | Net-new | **ID** |

## 5. Output e integrazioni

| Funzione | Connect | Insight | Refyn | Provenienza | Stato |
|---|:--:|:--:|:--:|---|---|
| Viste e dashboard standard | ✓ | ✓ | ✓ | Legacy | PL / PR |
| Report standard | ✓ | ✓ | ✓ | Legacy | PL / PR |
| Export standard | ✓ | ✓ | ✓ | Legacy | PL / PR |
| Notifiche di base | ✓ | ✓ | ✓ | Legacy | PL / PR |
| Storico configurato | ✓ | ✓ | ✓ | Legacy | PL / PR · PD per retention |
| Ruoli utente essenziali | ✓ | ✓ | ✓ | Legacy | PD · da verificare |
| KPI configurabili | — | ✓ | ✓ | Legacy + sviluppo | PR |
| Editor di formule | — | ✓ | ✓ | Legacy + sviluppo | PR |
| Report programmati e direzionali | — | ✓ | ✓ | Legacy + sviluppo | PR |
| Export avanzato | — | ✓ | ✓ | Sviluppo | PR |
| Notifiche su condizioni e scostamenti | — | ✓ | ✓ | Sviluppo | PR |
| Scambio dati con ERP | — | ✓ | ✓ | Da verificare | **PD** · previa verifica tecnica |

## 6. Funzioni non offerte

Nessuna di queste è disponibile, in sviluppo o promessa. Non compare nei materiali
client-facing se non come esplicita esclusione.

| Funzione | Stato |
|---|---|
| Raccomandazioni automatiche | NO |
| Simulazioni e forecast | NO |
| Manutenzione predittiva | NO |
| Qualità predittiva | NO |
| Prescrizione parametri | NO |
| Benchmark cross-client | NO · richiede modello legale, privacy e anonimizzazione |
| Modelli proprietari | NO |
| Assistente in linguaggio naturale · AI generativa | NO |
| Digital twin completo | NO |
| Ottimizzazione autonoma | NO |
| Video e streaming da telecamere IP | NO |

---

## 7. Come si legge una riga

> **Energia per stato macchina** · Connect: base o condizionata · Insight: ✓ · Refyn: ✓ ·
> Provenienza: legacy + sviluppo · Stato: project-dependent

Significa: la capability nasce nel legacy ma è stata estesa; è compresa da Insight in su; su
Connect esiste in forma ridotta o solo a certe condizioni; e comunque **dipende dal progetto**,
perché serve che la misura di energia sia associabile allo stato macchina su quell'impianto.

## 8. Righe che richiedono una decisione prima della pubblicazione

| Riga | Cosa manca |
|---|---|
| Perimetro esatto di Connect | Quali funzioni sono incluse davvero nel primo livello |
| Perimetro esatto di Insight | Dove finisce Connect e dove comincia Insight |
| Refyn MVP | Quali degli otto oggetti entrano nella prima release |
| Ruoli utente essenziali | Se esistono già nel legacy e in che forma |
| Scambio dati con ERP | Se è mai stato fatto e con quale sistema |
| Intensità energetica di base su Connect | Se è sensato averla senza il livello Insight |
| Micro-fermi su Insight | Soglia minima rilevabile e granularità garantita |
