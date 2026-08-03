# D.Factory · Audit narrativo V9.2 → V9.3

**Fase A del §18.** Nessun HTML è stato modificato per produrre questo documento.

Base: `DFactory_SalesDeck_v9_2_client.html` (16 canvas) e
`DFactory_DossierTecnico_v9_2_client.html` (18 canvas).
Specifica: `DFactory_V9_3_Narrative_Commercial_Reset.md`.

---

## 1. La diagnosi, misurata

Il §1 del master descrive due problemi. Sono entrambi verificabili, e i numeri
sono più duri della descrizione.

### 1.1 Nel Sales Deck il messaggio vive dentro i disegni

Ho misurato, per ogni slide, **il blocco di testo più lungo che sta fuori da un
SVG** — cioè quello che il lettore legge come testo del documento e non come
etichetta di una schermata.

| slide | parole fuori dall'SVG | elementi `<text>` dentro l'SVG |
|---|--:|--:|
| `v01_cover` | 11 | 21 |
| `v02_tensione` | 14 | 12 |
| `v03_categoria` | 14 | 18 |
| `v04_evento_prodotto` | 8 | 18 |
| `v05_energia` | 8 | 15 |
| `v06_priorita` | 5 | 25 |
| `v07_ampiezza` | 5 | **45** |
| `v08_offerta` | 11 | 24 |
| `v09_scelta` | 5 | 34 |
| `v10_perche` | **2** | 28 |
| `v11_valore` | 6 | 14 |
| `v12_pilot` | 4 | 28 |
| `v13_cta` | 12 | 17 |
| `a1_matrice` | 17 | 39 |
| `a2_servizi` | 24 | 40 |
| `a4_faq` | 6 | 17 |

Su sedici slide, **il testo più lungo fuori da un disegno è di 24 parole**, e su
dieci slide sta sotto le dodici. Il §11.2 della V9.3 ammette 55 parole sulle
slide narrative: la V9.2 ne usa in media **il venti per cento**.

Non è un deck troppo pieno di testo. È un deck in cui il testo non c'è, e il
messaggio è stato affidato a etichette dentro i grafici.

### 1.2 La regola del 55–70% è stata applicata a tutto

Superficie del visual dominante, misurata da `qa.py` sulla client edition:

| slide | vis% | tipo secondo il §2.2 | intervallo V9.3 | scarto |
|---|--:|---|---|---|
| `v01_cover` | 58,3 | narrativa/promessa | 20–40 | **+18** |
| `v02_tensione` | 58,9 | narrativa | 20–40 | **+19** |
| `v03_categoria` | 59,4 | narrativa (visione) | 20–40 | **+19** |
| `v04_evento_prodotto` | 67,8 | prodotto | 55–70 | ok |
| `v05_energia` | 66,7 | prodotto | 55–70 | ok |
| `v06_priorita` | 65,3 | valore | 30–50 | **+15** |
| `v07_ampiezza` | 62,8 | funzionalità | 30–50 | **+13** |
| `v08_offerta` | 62,8 | pacchetti | 25–45 | **+18** |
| `v09_scelta` | 66,4 | pacchetti | 25–45 | **+21** |
| `v10_perche` | 61,1 | azienda | 25–45 | **+16** |
| `v11_valore` | 65,6 | valore | 30–50 | **+16** |
| `v12_pilot` | 66,7 | valore/CTA | 20–40 | **+27** |
| `v13_cta` | 63,3 | CTA | 20–40 | **+23** |
| `a1_matrice` | 56,7 | appendice | 50–75 | ok |
| `a2_servizi` | 57,8 | appendice | 50–75 | ok |
| `a4_faq` | 61,1 | appendice | 50–75 | ok |

**Dodici slide su sedici sono fuori intervallo, tutte per eccesso.** La banda è
strettissima — da 56,7 a 67,8 — e questo è il sintomo: una regola unica
applicata a tipologie diverse produce sedici slide che si somigliano.

### 1.3 Nel Dossier il problema è opposto, e non è la percentuale

Superficie visuale del dossier client: **da 0 a 37,4%**. Sette pagine su
diciotto non hanno alcun visual dominante — sono tabelle. Il dossier non è
troppo grafico. È troppo interrogativo.

Occorrenze di formule di stato aperto nel **solo testo visibile** della client
edition:

| espressione | occorrenze |
|---|--:|
| `solution design` | **16** |
| `da verificare` | **12** |
| `da approvare` | 6 |
| `da nominare` | 6 |
| `da confermare` | 5 |
| `Chi decide` / `Owner` | 4 |
| `Che cosa richiede` / `non presuppone` / `Chi la usa` / `Che decisione abilita` | 5 |

**Cinquantaquattro occorrenze su diciotto pagine**, tre per pagina. È esattamente
la sensazione che il §1.5 descrive: questionario, assessment, documento di
lavoro.

### 1.4 Il Dossier non spiega: elenca

Il §12.2 chiede che ogni pagina core contenga almeno un paragrafo esplicativo di
45–100 parole. Paragrafo contiguo più lungo, pagina per pagina:

| pagina | parole | | pagina | parole |
|---|--:|---|---|--:|
| `p01_cover` | 13 | | `p09_contesto` | 24 |
| `p02_overview` | 16 | | `p10_oee` | 30 |
| `p03_livelli` | 17 | | `p11_energia` | 28 |
| `p04_connect` | 16 | | `p12_output` | **49** |
| `p05_insight` | 13 | | `p13_pilot` | 12 |
| `p06_refyn` | 18 | | `p14_servizi` | 26 |
| `p07_sorgenti` | 41 | | | |

**Una pagina core su quattordici** raggiunge la soglia. Il contenuto c'è — le
pagine stanno fra 52 e 130 parole — ma è frantumato in etichette, celle e
microtesti. Nessuno spiega niente per esteso.

---

## 2. Sales Deck · canvas per canvas

Legenda azione: **K** keep · **R** rewrite · **M** merge · **V** move · **X** remove.

| V9.2 | funzione oggi | problema | az. | nuovo ruolo V9.3 | tipo | visuale |
|---|---|:--:|:--:|---|---|--:|
| `v01_cover` | promessa + vista di turno | la dashboard compete con la headline, 58% di superficie | **R** | **S01 Promessa** · la vista scende a prova di sfondo, la headline domina | narrativa | 35–40% |
| `v02_tensione` | quattro sorgenti tecniche non allineate | il problema è raccontato con nomi di sorgenti (PLC, contatori), non con i tre attori che lo subiscono | **R** | **S02 Il problema di oggi** · tre fratture — Produzione, Energia, Direzione | narrativa | 25–35% |
| `v03_categoria` | una schermata con tre annotazioni | è già una dashboard alla terza slide, prima che il lettore sappia che cos'è il prodotto | **R** | **S03 Visione di prodotto** · schema editoriale Segnali → Contesto → Evidenza → Decisione | narrativa | ≤ 40% |
| — | — | **manca del tutto la slide del cambiamento** (§4 S04) | **+** | **S04 Trasformazione** · prima/dopo, cinque righe per parte | narrativa | 25–35% |
| `v04_evento_prodotto` | fermo, causa, costo | nessuno: è la migliore prova di prodotto del deck | **K** | **S05 Prodotto in azione** · invariata nella sostanza, arriva dopo la visione | prodotto | 55–70% |
| `v05_energia` | produzione ed energia sulla stessa finestra | duplica l'asse temporale di S04 e di `v10_perche`: tre slide con lo stesso grafico | **M** | confluisce in **S06** | — | — |
| `v07_ampiezza` | quattro bande macchina/linea/turno/pezzo | 45 elementi di testo dentro un SVG: è la slide più densa del deck e non spiega le funzionalità, mostra numeri | **M** | la lettura a quattro livelli confluisce in **S06**; la funzione «che cosa comprende il prodotto» passa a **S08** | — | — |
| — | — | — | **+** | **S06 Un evento, quattro letture** · una timeline centrale, quattro output laterali (capacità, energia, costo, impatto operativo) | prodotto | 55–65% |
| `v06_priorita` | ranking cause per costo | quattro cause vanno bene; manca il copy narrativo che dica perché il ranking è il valore | **R** | **S07 Dall'evento alla priorità** · ranking semplificato + copy narrativo | valore | 40–50% |
| `v07_ampiezza` *(seconda vita)* | — | — | **R** | **S08 Mappa delle funzionalità** · cinque aree, composizione editoriale, nessuna mini-dashboard | funzionalità | 30–45% |
| `v08_offerta` | «la stessa finestra che acquisisce funzioni» | è la vista UI che il §19 chiede di eliminare dalle slide pacchetto; i verbi «vede/spiega/guida» non dicono che cosa si compra | **X** | eliminata. La progressione cumulativa resta in **S12** | — | — |
| `v09_scelta` | tre colonne quando serve / cosa ottieni / come si attiva | tre livelli in una slide sola: nessuno dei tre ha spazio per le proprie funzionalità | **X** | sostituita da **S09**, **S10**, **S11** | — | — |
| — | — | — | **+** | **S09 Connect** · promessa, tre blocchi funzionali, risultato, attivazione | pacchetto | 25–35% |
| — | — | — | **+** | **S10 Insight** · perdite produttive, energia e costo, analisi avanzate | pacchetto | 25–35% |
| — | — | — | **+** | **S11 Refyn** · priorità, azioni, verifica · unica occorrenza di «in sviluppo» | pacchetto | 25–35% |
| `a1_matrice` | otto capacità × tre livelli | è in appendice: la domanda commerciale principale sta dietro alle FAQ | **V** | sale nel corpo come **S12 Confronto dei livelli e servizi**, nove righe, più i nove servizi orizzontali | pacchetti | 30–45% |
| `v10_perche` | tre callout + asse produzione/energia | il visual è la terza copia dello stesso grafico; la slide parla di prodotto, non di azienda | **R** | **S13 Perché D.Factory** · brownfield first, un solo contesto, software e competenze. Nessuna timeline | azienda | 25–40% |
| `v11_valore` | formula + due leve | corretta nel metodo, ma il modello commerciale non compare nel corpo | **M** | **S14 Valore e modello commerciale** · formula + avvio/ricorrente/opzionale | valore | 30–45% |
| `v12_pilot` | tre momenti + struttura economica | la struttura economica migra in S14; restano i tre momenti | **M** | confluisce in **S15** | — | — |
| `v13_cta` | quattro blocchi + vista di turno | la vista di turno a destra è la quarta ripetizione del grafico di linea | **M** | **S15 Pilot e CTA** · percorso a tre passi + azione + contatto, senza seconda dashboard | CTA | 20–35% |
| `a2_servizi` | nove servizi × output/quando/incluso | va bene, ma manca la colonna «cosa comprende» | **R** | **A2 Catalogo servizi** · cinque colonne | appendice | 50–75% |
| `a4_faq` | sei domande | due delle sei sono domande IT («dove risiedono i dati», «serve fermare la linea») | **R** | **A4 FAQ** · solo domande commerciali; le due IT migrano nel dossier | appendice | 50–70% |
| `a3_pricing` *(working)* | dieci importi segnaposto | nessuno | **K** | **A3 Struttura economica** · resta condizionata a G2 | appendice | 50–75% |
| `a5_assunzioni` *(working)* | dieci parametri | il §6 della V9.3 elenca quattro appendici, non cinque | **K** | resta **working only**, condizionata a G3 · vedi conflitto §5.3 | appendice | — |
| `v14_caso` *(working)* | struttura del caso cliente | nessuno | **K** | invariata, governata da `CASE_STUDY_READY` | — | — |

### 2.1 Bilancio

| | V9.2 | V9.3 |
|---|--:|--:|
| slide core client | 13 | **15** |
| appendici client | 3 | **3** *(A3 pricing esclusa con G2 aperto)* |
| slide narrative | 2 | **5** — S01, S02, S03, S04, S13 |
| slide di forte prova UI | ~9 | **3** — S01 (sfondo), S05, S06 |
| slide dedicate ai pacchetti | 2 in una | **3 autonome** + 1 confronto |
| ripetizioni dell'asse produzione/energia | 4 | **1** |

---

## 3. Dossier · canvas per canvas

| V9.2 | funzione oggi | problema | az. | nuovo ruolo V9.3 | tipo | visuale |
|---|---|:--:|:--:|---|---|--:|
| `p01_cover` | titolo, quattro sezioni, sei destinatari, annessi | sei reparti in evidenza; il sottotitolo non dice che cosa contiene il documento | **R** | **P01 Cover** · sottotitolo funzionale, destinatari su una riga discreta | apertura | 15–25% |
| `p02_overview` | flusso a tre passi + «che cosa richiede / non presuppone» | è la pagina che dà il tono da questionario fin dalla seconda pagina; paragrafo più lungo: 16 parole | **R** | **P02 Executive summary** · paragrafo di 70–90 parole + cinque punti chiave | spiegazione | 20–30% |
| — | — | — | **+** | **P03 Architettura funzionale** · dal segnale alla decisione, uno schema orizzontale, 70–100 parole | architettura | 45–55% |
| `p03_livelli` | base comune + tre livelli | contenuto giusto, ma serve prima la base funzionale comune | **R** | **P04 Base funzionale comune** · dati operativi, energetici, contesto, output | funzionale | 35–45% |
| `p04_connect` | UI grande + tre insight + «chi la usa» + «decisione abilitata» | i due blocchi finali sono forma da questionario; le funzioni di Connect non sono elencate | **R** | **P05 Connect** · paragrafo + funzioni/output/configurazioni/limiti + una vista grande | funzionale | 40–50% |
| `p05_insight` | ranking + «che cosa aggiunge» + «come ordina» | idem | **R** | **P06 Insight** · paragrafo + le tre famiglie di funzioni + output | funzionale | 40–50% |
| `p06_refyn` | ciclo + «che cosa porta con sé un'azione» + tre note | tre note metodologiche sparse, una tabella di domande | **R** | **P07 Refyn** · paragrafo + priorità/azioni/verifica + ciclo semplice | funzionale | 35–45% |
| — | — | **manca la matrice funzionale nel dossier** | **+** | **P08 Matrice funzionale** · perimetro dei tre livelli, completa | tabella | 55–70% |
| `p07_sorgenti` | tabella Riempitrice/Etichettatrice/Tappatrice | sembra la configurazione standard del prodotto, non un esempio | **R** | **P09 Acquisizione dati** · aree di sorgente generiche; l'esempio di linea è dichiarato tale o va in annesso | architettura | 40–50% |
| `p09_contesto` | cinque tracce sullo stesso asse | ridimostra il fermo già dimostrato tre volte nel deck e una nel dossier | **R** | **P10 Modello di contesto** · evento centrale con i nove attributi, non una timeline | architettura | 45–55% |
| `p08_architettura` | quattro livelli + «definito dal prodotto» / «da chiudere» | il blocco «da chiudere» va bene, ma la security ci è dentro e non ha pagina propria | **R** | **P11 Architettura e deployment** · architettura standard + parametri di progetto | architettura | 50–60% |
| — | — | **la security esiste solo come annesso-questionario** | **+** | **P12 Sicurezza e governo dei dati** · nove aree nel core, valori in annesso | architettura | 35–45% |
| `p10_oee` | scomposizione OEE + ranking cause | il ranking duplica `p05_insight` | **R** | **P13 Metodo di misura · produzione** · disponibilità, performance, qualità, OEE, perdite | metodo | 45–55% |
| `p11_energia` | potenza per stato + tre numeri + parametri | buona pagina, resta | **K** | **P14 Metodo di misura · energia** · kWh, potenza, consumo specifico, costo, CO₂ | metodo | 45–55% |
| `p12_output` | output × chi lo usa × che decisione abilita | organizzata per reparto e per decisione: è la forma che il §8 P14 chiede di sostituire | **R** | **P15 Output e integrazioni** · catalogo output/contenuto/frequenza/modalità | tabella | 35–45% |
| `p13_pilot` | quattro deliverable + criteri di uscita | va bene, ma il percorso completo va da perimetrazione a scala | **R** | **P16 Delivery e pilot** · sei fasi, deliverable, criteri di uscita scritti una volta | delivery | 30–45% |
| `p14_servizi` | sei servizi × cosa produce × modello | manca la narrativa; il supporto è una nota | **R** | **P17 Servizi e supporto** · paragrafo + catalogo a nove voci + blocco supporto | delivery | 25–40% |
| `pa1_compatibilita` | otto elementi, esiti tutti «da verificare», colonna Owner | «Owner» nel client; otto «da verificare» identici | **R** | **A1 Compatibilità tecnica** · componente/requisito/verifica/esito/nota, senza owner nel client | annesso | 60–80% |
| `pa2_sizing` | cinque grandezze → una scatola | il §9 chiede di non usare solo frecce verso una scatola | **R** | **A2 Dimensionamento** · parametri + tre fasce anche nel client | annesso | 60–75% |
| `pa3_governo` | otto ambiti × modello × valore × chi decide | è la sede *corretta* per «chi decide»: qui resta | **R** | **A3 Requisiti IT e security** · rinominato, tono da checklist ammesso | annesso | 60–80% |
| `pa4_kpi` | sei KPI × otto colonne | sei «da nominare» e sei «da approvare» ripetuti | **R** | **A4 Dizionario KPI** · una nota unica al posto delle dodici ripetizioni | annesso | 60–80% |

### 3.1 Bilancio

| | V9.2 | V9.3 |
|---|--:|--:|
| pagine core | 14 | **17** |
| annessi | 4 | **4** |
| pagine con paragrafo ≥ 45 parole | 1 | **17** *(obiettivo)* |
| occorrenze di stato aperto nel core | 54 | **≤ 12** *(una nota per pagina, non una per riga)* |
| «Chi decide» / «Owner» nel core | 4 | **0** — solo in A3 |
| ripetizioni della timeline del fermo | 2 | **0** nel dossier core |

> **Nota sul conteggio delle pagine.** Il §8 propone «16 pagine core». Il §8 P13
> ammette però esplicitamente di tenere metodo di misura su **due** pagine
> («P13 OEE e perdite; P14 Energia, costo e CO₂») se il contenuto non entra su
> una. Con quella opzione — che è necessaria, perché OEE ed energia hanno
> ciascuna quattro grandezze e una catena di calcolo — il core diventa **17**.
> Registrato al §5.2.

---

## 4. Le due nuove sequenze

### 4.1 Sales Deck · 15 core + 4 appendici

| # | slide | tipo | visuale | provenienza |
|--:|---|---|--:|---|
| 01 | Promessa | narrativa | 35–40% | `v01_cover`, riequilibrata |
| 02 | Il problema di oggi | narrativa | 25–35% | `v02_tensione`, riscritta |
| 03 | Visione di prodotto | narrativa | ≤ 40% | `v03_categoria`, riscritta |
| 04 | Trasformazione per il cliente | narrativa | 25–35% | **nuova** |
| 05 | Prodotto in azione | prodotto | 55–70% | `v04_evento_prodotto` |
| 06 | Un evento, quattro letture | prodotto | 55–65% | `v05_energia` + `v07_ampiezza` |
| 07 | Dall'evento alla priorità | valore | 40–50% | `v06_priorita`, semplificata |
| 08 | Mappa delle funzionalità | funzionalità | 30–45% | **nuova**, eredita da `v07_ampiezza` |
| 09 | Connect | pacchetto | 25–35% | **nuova** |
| 10 | Insight | pacchetto | 25–35% | **nuova** |
| 11 | Refyn | pacchetto | 25–35% | **nuova** |
| 12 | Confronto dei livelli e servizi | pacchetti | 30–45% | `a1_matrice` promossa nel corpo |
| 13 | Perché D.Factory | azienda | 25–40% | `v10_perche`, rifatta |
| 14 | Valore e modello commerciale | valore | 30–45% | `v11_valore` + struttura di `v12_pilot` |
| 15 | Pilot e CTA | CTA | 20–35% | `v12_pilot` + `v13_cta` |
| A1 | Matrice completa delle funzionalità | appendice | 50–75% | espansione di `a1_matrice` |
| A2 | Catalogo servizi | appendice | 50–75% | `a2_servizi` + colonna «cosa comprende» |
| A3 | Struttura economica | appendice | 50–75% | `a3_pricing`, condizionata a G2 |
| A4 | FAQ commerciali | appendice | 50–70% | `a4_faq`, ripulita |

**Ritmo verificato contro il §11.3:** le uniche due slide con una dashboard
ricostruita in sequenza sono 05 e 06 — il tetto è due. La 07 è un grafico di
ranking, non una ricostruzione di interfaccia. Dopo la 07 non compare più
nessuna dashboard fino alla fine del deck. Una sola matrice nel corpo (12), una
sola formula economica nel corpo (14).

### 4.2 Dossier · 17 core + 4 annessi

| # | pagina | tipo | visuale | provenienza |
|--:|---|---|--:|---|
| 01 | Cover | apertura | 15–25% | `p01_cover`, semplificata |
| 02 | Executive summary | spiegazione | 20–30% | `p02_overview`, riscritta |
| 03 | Architettura funzionale | architettura | 45–55% | **nuova** |
| 04 | Base funzionale comune | funzionale | 35–45% | `p03_livelli`, riscritta |
| 05 | Connect | funzionale | 40–50% | `p04_connect` |
| 06 | Insight | funzionale | 40–50% | `p05_insight` |
| 07 | Refyn | funzionale | 35–45% | `p06_refyn` |
| 08 | Matrice funzionale | tabella | 55–70% | **nuova** |
| 09 | Acquisizione dati | architettura | 40–50% | `p07_sorgenti`, resa generica |
| 10 | Modello di contesto | architettura | 45–55% | `p09_contesto`, trasformata |
| 11 | Architettura e deployment | architettura | 50–60% | `p08_architettura` |
| 12 | Sicurezza e governo dei dati | architettura | 35–45% | **nuova**, dal contenuto di `pa3` |
| 13 | Metodo di misura · produzione | metodo | 45–55% | `p10_oee` |
| 14 | Metodo di misura · energia | metodo | 45–55% | `p11_energia` |
| 15 | Output e integrazioni | tabella | 35–45% | `p12_output`, riorganizzata |
| 16 | Delivery e pilot | delivery | 30–45% | `p13_pilot` |
| 17 | Servizi e supporto | delivery | 25–40% | `p14_servizi` |
| A1 | Compatibilità tecnica | annesso | 60–80% | `pa1`, senza owner nel client |
| A2 | Dimensionamento | annesso | 60–75% | `pa2`, con le tre fasce nel client |
| A3 | Requisiti IT e security | annesso | 60–80% | `pa3`, rinominato |
| A4 | Dizionario KPI | annesso | 60–80% | `pa4`, senza ripetizioni |

---

## 5. Conflitti registrati

Il metodo delle versioni precedenti vale anche qui: un conflitto si registra, non
si risolve in silenzio.

### 5.1 Tre slide di forte prova UI contro due slide tecniche consecutive

- Il **§17.13** ammette «soltanto tre slide di forte prova UI».
- Il **§11.3** e il **§16.1** vietano «più di due slide tecniche consecutive».
- La sequenza del §4 mette S05, S06 e S07 una dopo l'altra, e tutte e tre
  contengono una rappresentazione di dati.

**Risoluzione:** le tre slide di forte prova UI sono **S01** (la vista di turno
ridotta a prova di sfondo, come chiede il §4 S01), **S05** e **S06**. **S07 non
è una ricostruzione di interfaccia**: è un grafico di ranking a quattro barre
con un titolo narrativo e un paragrafo. Le slide tecniche consecutive restano
due — S05 e S06 — e il tetto è rispettato in entrambe le letture.

Conseguenza operativa: S07 deve essere costruita come **slide di valore**, con il
copy narrativo del §4 S07 in evidenza e il ranking sotto, non come la quarta
schermata di prodotto di fila.

### 5.2 Sedici pagine core contro il contenuto di metodo

Il **§8** propone 16 pagine core; il **§8 P13** ammette esplicitamente di tenere
il metodo di misura su due pagine se il contenuto non entra. OEE ed energia hanno
ciascuna quattro grandezze, una catena di calcolo e una tavola di parametri: su
una sola pagina violerebbero il §12.2 (paragrafo esplicativo) o il tetto di
leggibilità.

**Risoluzione:** due pagine di metodo, **17 pagine core**. È l'opzione che il
master stesso prevede.

### 5.3 Quattro appendici del deck contro l'appendice delle assunzioni

Il **§6** elenca quattro appendici del Sales Deck: matrice, servizi, struttura
economica, FAQ. La V9.2 ne ha cinque, perché A5 raccoglie i dieci parametri dello
scenario illustrativo. Il **§15** conferma che la validazione del dataset resta
nel 10% finale.

**Risoluzione:** A5 **esce dalla client edition** — dove peraltro già non
compariva, essendo condizionata a G3 — e **resta nella working edition** come
strumento interno. Le quattro appendici client sono quelle del §6. Nessun
parametro va perso: il registro dei parametri è comunque in
`DFactory_FinalReviewChecklist_v9_2.md`.

### 5.4 «Owner» vietato nel core, ma presente nel dizionario KPI

Il **§16.3** chiede che «owner» non domini una pagina core, e il **§9 A4**
mantiene la colonna *owner* fra quelle del dizionario KPI — che nella V9.3 è un
annesso.

**Risoluzione:** nessun conflitto reale. A4 è un annesso, e il §9 A3 dichiara che
gli annessi sono la sede corretta per owner, valore di progetto e stato. Nel
**core** del dossier la parola non compare più.

---

## 6. Che cosa non cambia

Il §13 elenca il design system da preservare, e va preso alla lettera.

| elemento | stato |
|---|---|
| palette nero / bianco / giallo funzionale | invariata |
| Geist e Geist Mono, incorporate base64 | invariate |
| canvas 1280 × 720 | invariato |
| griglia, margini, footer discreto | invariati |
| titoli forti, spaziatura ampia | invariati |
| assi temporali e linee sottili | invariati dove restano |
| ricostruzioni SVG inline, zero raster | invariate |
| meccanica working/client e i cinque gate | invariata |
| 221 placeholder, nessuno rinominato | invariati |
| autonomia del file, zero richieste di rete | invariata |

Cambiano soltanto le cinque cose che il §13 elenca sotto «modificare»:
percentuale visuale obbligatoria, numero di dashboard, eccesso di microtesti,
dipendenza da tabelle, uso delle domande e ripetizione di etichette tecniche.

---

## 7. Che cosa resta aperto · §15

Invariato rispetto alla V9.2, e questa iterazione non deve chiuderlo:

prezzi · durata contrattuale · SLA · protocolli · porte · sizing · proprietà dei
dati · licenza · caso cliente · risultati · contatto · asset reali.

Il compito della V9.3 su questi punti è uno solo: **creare lo spazio giusto**
perché entrino senza ridisegnare niente. Lo spazio è già mappato — S12 per le
inclusioni, A3 per gli importi, S13 per la prova aziendale, A1/A2/A3 del dossier
per i valori tecnici, S15 per il contatto.

---

## 8. Ordine di lavoro e punto di fermata

Il §18 e il §19 stabiliscono un processo esplicito, con un'approvazione in mezzo.

| fase | oggetto | stato |
|---|---|---|
| **A** | questo audit | ✔ prodotto, nessun HTML toccato |
| **B** | `DFactory_SalesDeck_Storyboard_v9_3.md` · `DFactory_Dossier_Storyboard_v9_3.md` | prossima |
| **C** | quattro prototipi Sales: S04 trasformazione, S09 Connect, S10 Insight, S11 Refyn | poi |
| **D** | quattro prototipi Dossier: P02 executive summary, P05 Connect, P11 architettura, P15 output | poi |
| **E** | build completo | **soltanto dopo verifica dei prototipi** (§18 Fase E) |
| **F** | QA e consegna | dopo E |

> Il §19 è esplicito: «Non costruire subito tutti i documenti… 5. Build completo
> **dopo approvazione**». Le fasi B, C e D vengono consegnate insieme, e il
> lavoro si ferma lì.

### 8.1 Le undici condizioni di build della V9.3

Da implementare in fase E, elencate qui perché guidano già i prototipi.

| # | il build fallisce se | come si misura |
|--:|---|---|
| 1 | una slide pacchetto contiene una dashboard | nessun `svg[data-ui]` nei canvas S09, S10, S11 |
| 2 | più di due slide tecniche consecutive | sequenza dei tipi dichiarati nello storyboard |
| 3 | il prodotto non è definito entro la terza slide | S03 contiene la definizione estesa |
| 4 | manca la slide di trasformazione | esiste il canvas S04 |
| 5 | manca una slide per uno dei tre pacchetti | esistono S09, S10, S11 |
| 6 | «chi decide» appare nel core del dossier | testo visibile delle pagine 01–17 |
| 7 | «owner» domina una pagina core | occorrenze per pagina core |
| 8 | una pagina core del dossier non ha un paragrafo di 45–100 parole | blocco contiguo più lungo |
| 9 | «in sviluppo» compare più di una volta per documento | già attiva dalla V9.2 |
| 10 | restano placeholder nella client edition | già attiva dalla V9 |
| 11 | overflow, clipping o testo sotto il minimo | già attiva, con la scala del viewBox corretta |

Le dieci condizioni della V9.2 restano tutte: le nuove si aggiungono, non
sostituiscono.

---

*Fase A chiusa. Nessun file HTML è stato modificato.*
