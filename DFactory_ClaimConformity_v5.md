# D.Factory · Claim Conformity v5

Ogni claim che compare, o che compariva, nei due documenti. Tre colonne che contano: che cosa
si dice oggi, con quale autorizzazione, e chi la rilascia.

Stati: `ammesso` · `ammesso con qualifica` · `da validare` · `non pubblicare`

---

## 1. Claim ammessi con prudenza

Presenti nei v5, con la formulazione indicata.

| Claim | Formulazione nei v5 | Dove |
|---|---|---|
| Acquisizione e storicizzazione dati | "acquisizione da PLC, PC e dispositivi, con storico configurato" | Deck 03, dossier 04, 05, 06 |
| Stati macchina e linea | "stato macchina e stato linea" | Dossier 06, 07 |
| Allarmi ed eventi | "allarmi ed eventi" | Dossier 06 |
| Performance di produzione | "disponibilità, performance, qualità, OEE macchina e di linea di base" | Dossier 06, 08 |
| Consumi e utility | "elettricità, gas, vapore, aria compressa, acqua, dove esiste la strumentazione" | Dossier 06, 11 |
| Costo energetico | "costo energetico per pezzo, sui vettori strumentati" | Deck 09, dossier 12 |
| CO₂ | "CO₂ **calcolata o stimata** per pezzo, con fattori documentati" | Dossier 12, 13 |
| Dashboard, KPI e formule | "KPI configurabili, editor di formule" | Dossier 06, 24 |
| Multi-vendor | "multi-vendor **previa verifica** per modello e versione" | Dossier 19 |
| ERP | "possibile scambio dati **previa verifica tecnica**" | Dossier 24 |

## 2. Claim da validare prima dell'uso

Ventun voci. Nei v5 nessuna è presentata come fatto: o è riformulata in modo prudente, o
porta uno stato esplicito, o è omessa.

| # | Claim | Trattamento nei v5 | Owner |
|---|---|---|---|
| 1 | Un solo modello dati | **Riformulato**: "produzione ed energia nello stesso contesto operativo" | Tecnico |
| 2 | Database condiviso | **Omesso** | Tecnico |
| 3 | PackML, 17 stati | **Qualificato**: "stati PackML dove la macchina li espone · da verificare per modello" | Tecnico |
| 4 | Modello ridotto a due stati | **Qualificato**: "dove lo standard manca, modello ridotto · da verificare" | Tecnico |
| 5 | Logica buffer-aware | **Marcato in sviluppo**, attribuito a Refyn. Deck 06 e dossier 17 | Tecnico |
| 6 | On-premise | **Qualificato**: "assetto previsto, definito in solution design" | Tecnico |
| 7 | Server Linux | **Qualificato**: "PC industriale, sistema operativo da confermare" | Tecnico |
| 8 | Zero internet | **Riformulato**: "nel perimetro concordato con il tuo IT non è previsto traffico verso internet dalla rete di linea" | Tecnico |
| 9 | Dato sempre di proprietà del cliente | **Qualificato**: "policy da confermare in contratto", distinta dalla licenza | Legale |
| 10 | Nessun hardware proprietario | **Qualificato**: "l'assetto previsto non lo richiede · da verificare per impianto" | Tecnico |
| 11 | First signal in due giorni | **Omesso** | Delivery |
| 12 | Multi-site | **Marcato project-dependent** | Tecnico |
| 13 | API | **Marcato project-dependent**, "da definire" | Tecnico |
| 14 | Scope 1 e 2 | **Qualificato**: "dati associabili a fattori emissivi documentati" | Tecnico |
| 15 | Consegna in 60 giorni | **Omesso** | Delivery |
| 16 | 70 casi | **Omesso**. Ambiguità di unità non sciolta | Commerciale |
| 17 | Partnership Siemens | **Omesso** | Direzione + Legale |
| 18 | Seconda generazione | **Omesso** | Tecnico |
| 19 | SAP nativo | **Omesso** il nome; resta "ERP previa verifica" | Tecnico + Legale |
| 20 | Patent Box | **Omesso** | Direzione |
| 21 | Refyn design partner | **Condizionato**: la formula compare a pagina 18 solo come opzione, non come programma attivo | Commerciale |

## 3. Claim da non pubblicare senza prodotto reale

Nessuno compare nei v5. Il dossier li elenca a pagina 18 come **esclusioni esplicite**, che è
diverso dal tacerli: un interlocutore tecnico apprezza sapere cosa il sistema non fa.

| Claim | Nota |
|---|---|
| Intelligenza artificiale | Nessuna funzione AI nel prodotto. La diagnostica prevista è per regole e statistica |
| Manutenzione predittiva | Non offerta, non in sviluppo |
| Qualità predittiva | Non offerta, non in sviluppo |
| Video e streaming da telecamere IP | Non offerto |
| Raccomandazioni automatiche | Non offerte |
| Prescrizione parametri | Non offerta |
| Benchmark cross-client | Richiede modello legale, privacy e anonimizzazione approvati |
| Simulazioni e forecast | Non offerti |
| Digital twin completo | Non offerto |
| Ottimizzazione autonoma | Non offerta |

---

## 4. Claim rimossi rispetto al v4

| Claim v4 | Perché è uscito |
|---|---|
| "Un solo modello dati" come titolo di slide 03 | Da validare tecnicamente. Sostituito da "produzione ed energia nello stesso contesto" |
| "Un solo modello dati" nel diagramma di dossier 03 e 04 | Idem |
| "17 stati PackML" senza qualifica | Ora "dove la macchina li espone · da verificare" |
| Buffer-aware presentato come funzione della capability matrix | Spostato in Refyn, marcato in sviluppo |
| "On-premise, sul tuo server" come rassicurazione di slide 03 | Ora "deployment definito in solution design" |
| "Nessun hardware D.Factory a bordo linea" come fatto | Ora qualificato e verificabile per impianto |
| "Nessun flusso verso internet dalla rete di linea" come proprietà | Ora legato al perimetro concordato con l'IT |
| "Aggiornamento 5 s" come valore fisso | Ora "aggiornamento configurato · da confermare per impianto" |
| Refyn = servizi sul dato | Refyn è il terzo modulo; i servizi sono un livello separato |
| `Insights` | Grafia errata |
| `MAPST 4.0` = "la piattaforma su cui il sistema è costruito" | Ora prodotto legacy |
| "Il dato resta qui" sul server del cliente | Ora "policy da confermare in contratto" |

## 5. Claim aggiunti rispetto al v4

| Claim nuovo | Autorizzazione |
|---|---|
| Connect, Insight e Refyn sono cumulativi | Decisione strategica confermata nel backlog V5 |
| Ogni livello contiene produzione ed energia | Idem |
| Connect e Insight sono in pilot release | Idem |
| Refyn è in sviluppo, non generalmente disponibile | Idem |
| I servizi sono attivabili su tutti i moduli | Idem |
| MAPST 4.0 e MarEnergy restano attivi per l'installato | Idem |
| La migrazione dal legacy è volontaria | Idem |
| Le capability nuove evolvono da MAPST 4.0 e MarEnergy | Backlog V5 §6.2, formula da validare prima dell'uso esterno |
| Operational Performance Index misura processo, turno o area | Backlog V5 §3.3.E. Marcato roadmap |
| Nessuna capacità di AI nel prodotto | Esclusione esplicita, già presente nel v4 |

## 6. Verifica automatica

`work_v5/qa.py` esegue un controllo lessicale su entrambi gli HTML. Termini vietati che
devono restituire zero occorrenze:

```
Insights · Refyn by · MAPST 4.0 come piattaforma corrente · intelligenza artificiale ·
manutenzione predittiva · qualità predittiva · digital twin · benchmark cross-client ·
Siemens · SAP · Patent Box · 70 casi · 60 giorni · un solo modello dati ·
Operator Performance Index · consulenza inclusa · tempo reale (non qualificato)
```

Termini che devono comparire almeno una volta nel dossier: `proven legacy`, `pilot release`,
`in development`, `project-dependent`, `MarEnergy`, `migrazione volontaria`.
