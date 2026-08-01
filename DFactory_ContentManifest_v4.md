# D.Factory · Content Manifest v4

Fonte di verità per tenere allineati `DFactory_SalesDeck_v4.html` (10 slide + 3 di
appendice) e `DFactory_DossierTecnico_v4.html` (23 pagine). Se un claim cambia qui, cambia
in entrambi.

---

## 1. Gerarchia delle fonti

| Livello | Fonte | Stato e uso ammesso |
|---|---|---|
| 1 | `DFactory_Refyn_Context_Brief.md` · agg. 17/07/2026 | Presente. Decisioni di brand, posizionamento, palette, guardrail, contesto competitivo. **Non** autorizza da solo claim numerici esterni |
| 2 | `DFactory_SalesDeck_v2.html`, `DFactory_DossierTecnico_v2.html`, Content Manifest v2 | Presenti. Base di claim, terminologia, stati |
| 3 | Inferenze editoriali | Titoli, ordine, gerarchia, visualizzazione, scelta dei visual |
| 4 | `Marchiani_Assessment_12Marzo.docx` | **Esiste lato committente, non consegnato nel workspace di lavorazione.** Nessun contenuto ne è stato tratto perché il file non era leggibile. I temi che contiene sono classificati `da validare`, non `fonte assente` |
| 5 | Ricerca esterna | Non effettuata |

**Regola che il manifest v2 non aveva.** Una fonte interna autorevole cambia il
posizionamento e vieta gli errori; non promuove un numero a claim esterno. Trazione,
prezzi, partnership e tempi restano "da validare" anche quando compaiono in un documento
interno.

**Nota sull'assessment.** Il file non è stato consegnato nel workspace di lavorazione, quindi
nessun suo contenuto è stato letto o citato. Esiste però lato committente e contiene i temi
elencati al §3. Per questo **non sono classificati "fonte non disponibile"**, come faceva il
manifest v2: sono `presenti in fonte interna, da validare prima della pubblicazione`. La
differenza è sostanziale. "Fonte assente" significa che il claim non ha origine e va
abbandonato; "da validare" significa che l'origine esiste e serve una conferma formale su chi
la rilascia. Quando il file sarà disponibile, questi temi vanno verificati uno per uno con
l'owner indicato, non promossi in blocco.

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
| Milestone | `first signal` · `first usable data` · `pilot live` · `operational go-live` · `scale-up` | Cinque, distinte, pagina 19 |

### Tre formulazioni vincolate

| Non usare | Usare | Perché |
|---|---|---|
| "tempo reale" da solo | "aggiornamento ogni 5 secondi, storico al minuto"; "in turno, mentre puoi ancora intervenire" | Il deck non promette una frequenza che il dossier non documenta |
| "misurata sul ciclo" ovunque | "misurato" dove è strumentato, "calcolato" dove è ripartito | `d09` e `d11` distinguono le due cose |
| "nessuna uscita verso internet" | "nessun flusso verso internet dalla rete di linea, nel perimetro concordato con il tuo IT" | È il perimetro architetturale previsto, non una proprietà assoluta |

---

## 3. Stato dei temi della Fase A2

Tutti i temi seguenti sono **presenti nell'assessment interno**. Nessuno è pubblicato nei v4,
ma la ragione non è più l'assenza di fonte: è che la fonte è interna e non ancora validata per
l'uso esterno. Owner e condizione di sblocco sono indicati per ciascuno.

| Tema | Stato | Owner della validazione | Condizione per pubblicarlo |
|---|---|---|---|
| Partnership Siemens | presente in fonte interna, **da validare** | Direzione + Legale | Accordo scritto e autorizzazione all'uso del nome. Un logo senza contratto è un rischio legale |
| Origine MES, sviluppo verso MOM | presente in fonte interna, **non pubblicare come identità** | Direzione | Resta utilizzabile per raccontare l'origine, mai come identità di prodotto. Identità canonica: "supervisione 4.0" |
| Seconda generazione di prodotto | presente in fonte interna, **da validare** | Tecnico | Definizione di cosa distingue la seconda generazione dalla prima |
| Almeno 70 casi | presente in fonte interna, **da chiarire prima di validare** | Commerciale | Il Context Brief parla di ~70 **macchine** e 10 **clienti**. Prima di pubblicare va sciolta l'ambiguità di unità: casi, macchine o clienti |
| Settori oltre Food & Beverage | presente in fonte interna, **da validare** | Direzione | Decisione di posizionamento: allargare il perimetro dichiarato cambia il deck, non solo una slide |
| Integrazione SAP | presente in fonte interna, **da validare** | Tecnico + Legale | Verifica tecnica su un progetto reale e autorizzazione all'uso del nome del prodotto ERP. Nei v4 resta "integrazione ERP · sul progetto", senza nome |
| Consegna in circa 60 giorni | presente in fonte interna, **da validare** | Delivery | Va detto a quale milestone si riferisce: `first signal`, `pilot live` o `operational go-live` sono calendari diversi |
| Pricing facility management | presente in fonte interna, **non trasferibile** | Commerciale | Caso di un altro dominio applicativo. Non si trasferisce a linee F&B senza ricalcolo |
| Patent Box | presente in fonte interna, **non pubblicare** | Direzione | È un'agevolazione fiscale, non una prova commerciale. Non ha uso in un deck cliente |
| Scenari data company, big data, modelli proprietari | presente in fonte interna, **roadmap** | Direzione | Il Context Brief vieta di raccontare il moat come asset di dati non provato. Il moat si racconta come radicamento operativo |
| Competitor 40 Factory | presente in fonte interna, **non pubblicare come confronto** | Direzione | Zerynth, Miraitek e 40Factory hanno moduli di monitoraggio energetico: una matrice che li marcasse "assente" sarebbe falsa. Serve un confronto verificato voce per voce |

**Perché nessuno di questi è nei v4.** Non perché siano falsi, ma perché un documento
client-facing non può contenere un claim la cui unica origine è un documento interno non
validato. Il passaggio da "da validare" a "pubblicabile" richiede una persona che se ne
assuma la responsabilità: è la colonna owner.

## 4. Claim ereditati dai v2

| ID | Claim | Stato | Sales | Dossier |
|---|---|---|---|---|
| C01–C05 | 10 clienti · ~70 macchine · ~30 linee · 24 mesi · 0 dismissioni | da validare | **omesso** | **omesso** |
| C06–C09 | Referenze e caso cliente | placeholder | **sostituito** da `s07` criteri di prova | **sostituito** da pagina 21, criteri di accettazione |
| C17 | Intelligenza artificiale | assente dal prodotto | non citata | pagina 05, dichiarata assente |
| C18 | Manutenzione e qualità predittive | roadmap senza data | non citata | pagina 05 |
| C19–C20 | PackML 17 stati · modello ridotto a 2 | pubblicabile | non citato | pagina 13 |
| C23–C24 | On-premise, PC industriale Linux del cliente | pubblicabile | `s03` | pagine 15 e 16 |
| C31 | Proprietà del dato, con export | pubblicabile | non citato | pagina 16, distinto dalla licenza |
| C32 | Licenza a fine contratto | non definita | non citato | pagina 16 |
| C33 | Nessun hardware proprietario a bordo linea | pubblicabile **qualificato** | `s03`, con la qualifica nella stessa frase | pagine 04 e 13 |
| C34 | Sensoristica a carico del cliente | pubblicabile | non citato | pagina 17 |
| C36–C38 | MID · ISO 50001 · Scope 1 e 2 | pubblicabile **qualificato** | non citati | pagine 12 e 17 |
| C42 | Report ITA/ENG, PDF, Gantt, vista 3D | pubblicabile | non citato | pagina 18 |
| C49–C52 | Prezzo, agevolazione, contratto, reversibilità | placeholder | **omessi**; `a01` descrive la struttura senza importi | non citati |
| C56 | Pablo Degl'Innocenti | pubblicabile | `s10` | `d18` |
| C57 | Certificazione TÜV SÜD | **non pubblicare** | No | No |
| C58 | Cinque vettori energetici | pubblicabile | non citato | pagine 05 e 11 |

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
| 04 | `s04_prodotto` | Il turno, mentre puoi ancora cambiarlo | Tre macchine: anomalia, causa, decisione |
| 05 | `s05_decisioni` | Un evento, tre decisioni che non si somigliano | Biforcazione da un evento a tre letture |
| 06 | `s06_perche` | Macchina ferma non significa linea ferma | Due scenari a confronto, polmone pieno e vuoto |
| 07 | `s07_ipotesi_misure` | Le domande a cui oggi rispondi a memoria | Confronto prima/dopo su tre domande |
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
| 03 | `d03_architettura_tecnica` | Da dove arrivano i dati e dove restano | 1 | Flusso su tre zone di rete |
| 04 | `d04_acquisizione` | Dove il dato viene preso, fisicamente | 1 | Schema di linea con i punti di prelievo |
| 05 | `d05_capability` | Cosa è disponibile, cosa è roadmap | 1 | Matrice per dominio, 7 righe, 5 stati |
| 06 | `d06_supervisione` | Cosa vedo mentre il turno è aperto | 2 | Vista di supervisione, 3 callout |
| 07 | `d07_oee_fermi` | Perché macchina ferma non è linea ferma | 2 | Schema polmone + ranking cause |
| 08 | `d08_velocita_qualita` | Come si vedono i micro-fermi | 2 | Curva con il micro-fermo marcato |
| 09 | `d09_multi_impianto` | Come si legge tutto l'impianto | 2 | Timeline a 20 righe |
| 10 | `d10_distribuzione_energia` | Dove finisce l'energia che entra | 2 | Flusso a nastri proporzionali |
| 11 | `d11_costo_co2_stato` | Quanto costa un pezzo, quanto spendi da fermo | 2 | Barre per vettore + barra per stato |
| 12 | `d12_metodo_misura` | Come si arriva a quei numeri | 3 | Sequenza a sei passi |
| 13 | `d13_brownfield_macchine` | Macchine, PLC e misura | 3 | Matrice, 5 righe |
| 14 | `d14_brownfield_rete` | Rete, gestionale e tag mapping | 3 | Due matrici, 4 + 3 righe |
| 15 | `d15_deployment` | Cosa chiede al mio IT | 3 | Tre zone di rete, flussi unidirezionali |
| 16 | `d16_specifiche_it` | Le voci che l'IT deve approvare | 3 | Matrice 9 voci × stato, owner, scadenza |
| 17 | `d17_sensori` | Dove serve misurare bene | 3 | Matrice clamp-on / certificata, 6 criteri |
| 18 | `d18_output_integrazioni` | In che forma esce il dato | 3 | Matrice output, 7 righe |
| 19 | `d19_milestone` | Dal primo segnale al go-live | 4 | Le cinque milestone |
| 20 | `d20_raci` | Chi fa cosa | 4 | RACI, 7 righe |
| 21 | `d21_criteri_pilot` | Quando il pilot si può dire riuscito | 4 | Matrice criteri, 6 condizioni |
| 22 | `d22_supporto` | Cosa succede dopo il go-live | 4 | Matrice supporto, 6 voci |
| 23 | `d23_checklist` | Cosa portare in sala | 4 | Checklist a 3 colonne |

---

## 7. Ripartizione fra i due documenti

| Contenuto | Sales deck | Dossier |
|---|---|---|
| `MAPST 4.0` | mai | pagine 02 e 03 |
| Punti di acquisizione del dato | mai | pagina 04 |
| Protocolli, porte, sizing, autenticazione, backup, logging | mai | pagine 03, 15 e **16** |
| Connect / Insights | solo appendice `a01` | pagine 02 e 05 |
| Refyn | solo appendice `a01`, come servizio in definizione | pagine 02 e 05 |
| Numeri di trazione | mai | mai |
| Prezzi e importi | mai | mai |
| RACI, milestone, SLA | mai | pagine 19, 20 e 22 |
| Metodo di misura, fattori emissivi | mai | pagina 12 |
| Criteri di prova | `s07`, versione commerciale | pagina 21, versione tecnica verificabile |

## 8. Coerenza incrociata

| Elemento | Sales | Dossier | Verifica |
|---|---|---|---|
| Frequenza di aggiornamento | "aggiornamento 5 s" nella vista `s04` | "aggiornamento 5 s" a pagina 06 | Stessa formulazione |
| Polmone | `s06` | pagina 07 | Stesso schema, stesso lessico |
| Fermo delle 07:18 | `s01`, `s02`, `s04`, `s05` | pagine 06, 08, 09 | Stesso evento nei visual dei due documenti |
| On-premise | `s03` | pagine 15 e 16 | Il deck non aggiunge dettagli di rete |
| Nessun hardware a bordo linea | `s03`, qualificato | pagine 04 e 13, qualificato | Stessa qualifica |
| Sensoristica a carico cliente | `a01` | pagina 17 | Stessa attribuzione |
| Criteri di prova | `s07` | pagina 21 | Il deck pone le domande, il dossier le rende verificabili |
| Contatto | `s10` | pagina 22 | Una sola occorrenza per documento |
| Link reciproci | 6 rimandi al dossier | 1 rimando al deck | Testuali, nessun URL inventato |
| Cinque vettori | non citati | pagine 05 e 11 | Sempre gli stessi cinque |

## 9. Grammatica visiva: cosa NON è condiviso

Deliberatamente diverso fra i due documenti, per evitare che sembrino lo stesso template:

| | Sales deck | Dossier |
|---|---|---|
| Impianto di pagina | Libero, asimmetrico, una silhouette diversa per slide | Fisso: fascia 336 px, ridotta a 248 px sulle 8 pagine tabellari |
| Titolo | 44–64 px, è una conclusione | 25–30 px nella fascia, è una domanda |
| Corpo | 17–19 px | 14–15 px |
| Componenti | Nessuna card, nessuna matrice, nessuna tabella | Matrici, cinque stati, blocchi solution design |
| Aree di lettura | Massimo due oltre al visual | Fascia + campo, sempre |
| Rail | Una riga in basso | Fascia laterale con sezione e pagina |

Condiviso: palette, font Geist, trattamento del giallo come segnale unico, marchio, canvas
1280 × 720, lo stesso evento produttivo raccontato nei visual.
