# D.Factory · Content Manifest v4

Fonte di verità per tenere allineati `DFactory_SalesDeck_v4.html` (10 slide + 3 di
appendice) e `DFactory_DossierTecnico_v4.html` (18 pagine). Se un claim cambia qui, cambia
in entrambi.

---

## 1. Gerarchia delle fonti

| Livello | Fonte | Stato e uso ammesso |
|---|---|---|
| 1 | `DFactory_Refyn_Context_Brief.md` · agg. 17/07/2026 | Presente. Decisioni di brand, posizionamento, palette, guardrail, contesto competitivo. **Non** autorizza da solo claim numerici esterni |
| 2 | `DFactory_SalesDeck_v2.html`, `DFactory_DossierTecnico_v2.html`, Content Manifest v2 | Presenti. Base di claim, terminologia, stati |
| 3 | Inferenze editoriali | Titoli, ordine, gerarchia, visualizzazione, scelta dei visual |
| 4 | `Marchiani_Assessment_12Marzo.docx` | **Assente dal workspace.** Nessun contenuto tratto |
| 5 | Ricerca esterna | Non effettuata |

**Regola che il manifest v2 non aveva.** Una fonte interna autorevole cambia il
posizionamento e vieta gli errori; non promuove un numero a claim esterno. Trazione,
prezzi, partnership e tempi restano "da validare" anche quando compaiono in un documento
interno.

---

## 2. Terminologia canonica

| Termine | Forma corretta | Note d'uso |
|---|---|---|
| Prodotto | `D.Factory` | Sempre con il punto |
| Società | `D Factory S.r.l.` | Solo nei rail di copertina e chiusura |
| Piattaforma | `MAPST 4.0` | **Solo nel dossier.** Non compare nel sales deck in nessuna forma |
| Identità | `supervisione 4.0`, "il sistema tra la linea e gli uffici" | Mai MES o MOM come identità di prodotto |
| Livello 1 | `Connect` | Visibilità e supervisione |
| Livello 2 | `Insights` | Analisi, fermi, energia, costo e CO₂ |
| Servizi | `Refyn` | Servizi sul dato, sempre "in definizione". Mai terzo livello di prodotto |
| Efficienza di linea | `OEE di linea` | Sull'intera linea, tiene conto dei polmoni |
| Efficienza di asset | `OEE macchina` | Sul singolo asset. Non intercambiabile con il precedente |
| Fermo | `fermo macchina` / `fermo linea` | Distinti sempre |
| Polmone | `polmone` | `buffer` spiegato una volta sola |
| Costo unitario | `costo energetico per pezzo` | Mai "costo per unità" |
| Emissioni | `CO₂ per pezzo` | Con il pedice corretto |
| Deployment | `on-premise` | Mai "in locale", mai "cloud privato" |
| Compatibilità | `multi-vendor`, `multi-protocollo` | Mai "compatibile con tutto" |
| Impianti esistenti | `brownfield` | Spiegato alla prima occorrenza |
| Milestone | `first signal` · `first usable data` · `pilot live` · `operational go-live` · `scale-up` | Cinque, distinte, `d16` |

### Tre formulazioni vincolate

| Non usare | Usare | Perché |
|---|---|---|
| "tempo reale" da solo | "aggiornamento ogni 5 secondi, storico al minuto"; "in turno, mentre puoi ancora intervenire" | Il deck non promette una frequenza che il dossier non documenta |
| "misurata sul ciclo" ovunque | "misurato" dove è strumentato, "calcolato" dove è ripartito | `d09` e `d11` distinguono le due cose |
| "nessuna uscita verso internet" | "nessun flusso verso internet dalla rete di linea, nel perimetro concordato con il tuo IT" | È il perimetro architetturale previsto, non una proprietà assoluta |

---

## 3. Stato dei temi della Fase A2

| Tema | Stato | Presente nei v4 |
|---|---|---|
| Partnership Siemens | **non pubblicare** · fonte assente | No |
| Origine MES / sviluppo MOM | **non pubblicare** come identità | No |
| Seconda generazione di prodotto | **non pubblicare** · fonte assente | No |
| Almeno 70 casi | **non pubblicare** · confusione di unità già segnalata dal brief | No |
| Settori oltre F&B | **non pubblicare** | No |
| Integrazione SAP | nome **non pubblicare**; funzione **da verificare** | `d15`, come "integrazione ERP · sul progetto", senza nome di prodotto |
| Consegna in circa 60 giorni | **non pubblicare** | No. `d16` lega i tempi a sensoristica e finestre di fermo |
| Pricing facility management | **non pubblicare** | No |
| Patent Box | **non pubblicare** | No |
| Data company, big data, modelli proprietari | **roadmap**, non pubblicare | No |
| Competitor 40 Factory | **non pubblicare** come confronto | No. Nessuna matrice competitiva nei v4 |

## 4. Claim ereditati dai v2

| ID | Claim | Stato | Sales | Dossier |
|---|---|---|---|---|
| C01–C05 | 10 clienti · ~70 macchine · ~30 linee · 24 mesi · 0 dismissioni | da validare | **omesso** | **omesso** |
| C06–C09 | Referenze e caso cliente | placeholder | **sostituito** da `s07` criteri di prova | **sostituito** da `d17` criteri di accettazione |
| C17 | Intelligenza artificiale | assente dal prodotto | non citata | `d04`, dichiarata assente |
| C18 | Manutenzione e qualità predittive | roadmap senza data | non citata | `d04` |
| C19–C20 | PackML 17 stati · modello ridotto a 2 | pubblicabile | non citato | `d12` |
| C23–C24 | On-premise, PC industriale Linux del cliente | pubblicabile | `s03` | `d13` |
| C31 | Proprietà del dato, con export | pubblicabile | non citato | `d13`, distinto dalla licenza |
| C32 | Licenza a fine contratto | non definita | non citato | `d13`, blocco solution design |
| C33 | Nessun hardware proprietario a bordo linea | pubblicabile **qualificato** | `s03`, con la qualifica nella stessa frase | `d12` |
| C34 | Sensoristica a carico del cliente | pubblicabile | non citato | `d14` |
| C36–C38 | MID · ISO 50001 · Scope 1 e 2 | pubblicabile **qualificato** | non citati | `d11`, `d14` |
| C42 | Report ITA/ENG, PDF, Gantt, vista 3D | pubblicabile | non citato | `d15` |
| C49–C52 | Prezzo, agevolazione, contratto, reversibilità | placeholder | **omessi**; `a01` descrive la struttura senza importi | non citati |
| C56 | Pablo Degl'Innocenti | pubblicabile | `s10` | `d18` |
| C57 | Certificazione TÜV SÜD | **non pubblicare** | No | No |
| C58 | Cinque vettori energetici | pubblicabile | non citato | `d04`, `d10` |

**Nessun token `[[PH_…]]` compare nei due documenti v4.** Dove il v2 esponeva un
placeholder, il v4 fa una di tre cose: omette il contenuto, lo riscrive senza promessa, o
lo raccoglie in un blocco "da definire nel solution design" con testo leggibile.

---

## 5. Contenuti del sales deck

| # | ID | Tesi | Visual dominante |
|---|---|---|---|
| 01 | `s01_promessa` | Dalla linea al margine, nello stesso dato | Turno di cinque macchine, un fermo marcato |
| 02 | `s02_punto_cieco` | La linea si ferma, l'energia no | Due curve sullo stesso asse dei tempi |
| 03 | `s03_come_funziona` | Quattro sorgenti che non si parlano, un solo modello | Convergenza e divergenza attorno a un nodo |
| 04 | `s04_prodotto` | Il turno, mentre puoi ancora cambiarlo | Vista di supervisione quasi a piena pagina, tre callout |
| 05 | `s05_decisioni` | Un evento, tre decisioni che non si somigliano | Biforcazione da un evento a tre letture |
| 06 | `s06_perche` | Macchina ferma non significa linea ferma | Due scenari a confronto, polmone pieno e vuoto |
| 07 | `s07_prova` | Le domande a cui oggi rispondi a memoria | Confronto prima/dopo su tre domande |
| 08 | `s08_valore` | Due leve, sullo stesso evento | Due barre proporzionali e la somma |
| 09 | `s09_percorso` | Ogni passo ha un criterio di uscita | Timeline a quattro momenti con criteri |
| 10 | `s10_cta` | Fissiamo l'audit della prima linea | Tipografico: nessun visual, per scelta |
| A1 | `a01_offerta` | Come si compone la proposta | Progressione a tre livelli, senza importi |
| A2 | `a02_faq` | Le quattro obiezioni che arrivano sempre | Due colonne |
| A3 | `a03_ipotesi` | Da dove viene l'esempio, e cosa manca | Due colonne di input |

## 6. Contenuti del dossier

| # | ID | Domanda tecnica | Sez. | Visual dominante |
|---|---|---|---|---|
| 01 | `d01_cover` | A chi serve, cosa copre | — | Indice a quattro sezioni |
| 02 | `d02_architettura_prodotto` | Come si chiamano le cose | 1 | Matrice nomenclatura, 5 righe |
| 03 | `d03_architettura_tecnica` | Da dove arrivano i dati e dove restano | 1 | Diagramma di flusso su tre zone |
| 04 | `d04_capability` | Cosa è disponibile, cosa è roadmap | 1 | Matrice per dominio, 7 righe |
| 05 | `d05_supervisione` | Cosa vedo mentre il turno è aperto | 2 | Vista di supervisione, 3 callout |
| 06 | `d06_oee_fermi` | Perché macchina ferma non è linea ferma | 2 | Schema polmone + ranking cause |
| 07 | `d07_velocita_qualita` | Come si vedono i micro-fermi | 2 | Curva velocità con micro-fermo marcato |
| 08 | `d08_multi_impianto` | Come si legge tutto l'impianto | 2 | Timeline a 20 righe |
| 09 | `d09_distribuzione_energia` | Dove finisce l'energia che entra | 2 | Diagramma di flusso a nastri |
| 10 | `d10_costo_co2_stato` | Quanto costa un pezzo, quanto spendi da fermo | 2 | Barre per vettore + barra per stato |
| 11 | `d11_metodo_misura` | Come si arriva a quei numeri | 3 | Sequenza a sei passi |
| 12 | `d12_brownfield` | Funziona sul parco che ho già | 3 | Matrice compatibilità, 7 righe |
| 13 | `d13_deployment_security` | Cosa chiede al mio IT | 3 | Tre zone di rete, flussi in sola lettura |
| 14 | `d14_sensori` | Dove serve misurare bene | 3 | Matrice clamp-on / certificata, 6 criteri |
| 15 | `d15_output_integrazioni` | In che forma esce il dato | 3 | Matrice output, 7 righe |
| 16 | `d16_delivery_raci` | Chi fa cosa e in quanto tempo | 4 | Cinque milestone + RACI |
| 17 | `d17_criteri_pilot` | Quando il pilot si può dire riuscito | 4 | Matrice criteri di accettazione, 6 righe |
| 18 | `d18_supporto_audit` | Cosa serve per partire e restare in esercizio | 4 | Checklist a due colonne |

---

## 7. Ripartizione fra i due documenti

| Contenuto | Sales deck | Dossier |
|---|---|---|
| `MAPST 4.0` | mai | `d02`, `d03` |
| Protocolli, porte, sizing, autenticazione, backup, logging | mai | `d03`, `d13` |
| Connect / Insights | solo appendice `a01` | `d02`, `d04` |
| Refyn | solo appendice `a01`, come servizio in definizione | `d02`, `d04` |
| Numeri di trazione | mai | mai |
| Prezzi e importi | mai | mai |
| RACI, milestone, SLA | mai | `d16`, `d18` |
| Metodo di misura, fattori emissivi | mai | `d11` |
| Criteri di prova | `s07`, versione commerciale | `d17`, versione tecnica verificabile |

## 8. Coerenza incrociata

| Elemento | Sales | Dossier | Verifica |
|---|---|---|---|
| Frequenza di aggiornamento | "aggiornamento 5 s" nella vista `s04` | "aggiornamento 5 s" in `d05` | Stessa formulazione |
| Polmone | `s06` | `d06` | Stesso schema, stesso lessico |
| Fermo delle 07:18 | `s01`, `s02`, `s04`, `s05` | `d05`, `d07`, `d08` | Stesso evento in tutti i visual dei due documenti |
| On-premise | `s03` | `d13` | Il deck non aggiunge dettagli di rete |
| Nessun hardware a bordo linea | `s03`, qualificato | `d12`, qualificato | Stessa qualifica |
| Sensoristica a carico cliente | `a01` | `d14` | Stessa attribuzione |
| Criteri di prova | `s07` | `d17` | Il deck pone le domande, il dossier le rende verificabili |
| Contatto | `s10` | `d18` | Una sola occorrenza per documento |
| Link reciproci | 4 rimandi al dossier per pagina | 1 rimando al deck | Testuali, nessun URL inventato |
| Cinque vettori | non citati | `d04`, `d10` | Sempre gli stessi cinque |

## 9. Grammatica visiva: cosa NON è condiviso

Deliberatamente diverso fra i due documenti, per evitare che sembrino lo stesso template:

| | Sales deck | Dossier |
|---|---|---|
| Impianto di pagina | Libero, asimmetrico, una silhouette diversa per slide | Fisso: fascia 336 px + campo 944 px |
| Titolo | 44–64 px, è una conclusione | 30 px nella fascia, è una domanda |
| Corpo | 17–19 px | 13,5–15 px |
| Componenti | Nessuna card, nessuna matrice, nessuna tabella | Matrici, stati, blocchi solution design |
| Numero di aree di lettura | Massimo due oltre al visual | Fascia + campo, sempre |
| Rail | Una riga in basso | Fascia laterale con sezione e pagina |

Condiviso: palette, font Geist, trattamento del giallo come segnale unico, marchio, canvas
1280 × 720, lo stesso evento produttivo raccontato nei visual.
