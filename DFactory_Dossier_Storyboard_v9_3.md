# D.Factory · Dossier tecnico · Storyboard V9.3

**Fase B del §18.** 17 pagine core + 4 annessi.

Il conteggio è 17 e non 16 perché il §8 P13 ammette esplicitamente di tenere il
metodo di misura su due pagine se il contenuto non entra su una. OEE ed energia
hanno ciascuna quattro grandezze e una catena di calcolo: non entrano.
Registrato al §5.2 dell'audit.

Per ogni pagina: titolo, messaggio, **paragrafo** (§12.2: 45–100 parole,
obbligatorio su ogni pagina core), copy, visuale, fonte, claim, fallback.

---

## Regole che governano tutte le pagine

| regola | §  | applicazione |
|---|---|---|
| paragrafo esplicativo 45–100 parole | 12.2 | ogni pagina core, verificato dal build |
| titoli descrittivi, non domande | 12.1 | nessun titolo interrogativo nel core |
| ogni schema con frase di lettura, legenda e conclusione | 12.3 | tutte le pagine con diagramma |
| tabelle di raccolta requisiti negli annessi | 12.4 | A1, A2, A3 |
| stati aperti: una nota, non una riga per riga | 12.5 | «solution design» scende da 16 a ≤ 8 occorrenze |
| «chi decide» e «owner» solo negli annessi | 16.3 | zero nel core |

**Nota unica sugli stati aperti**, da usare in fondo alle pagine che dipendono
dal progetto, al posto delle ripetizioni riga per riga:

> I valori di progetto vengono definiti nel solution design e riportati
> nell'annesso tecnico.

---

# P01 · Cover

**Titolo** · Dossier tecnico preliminare

**Sottotitolo** · Architettura funzionale, acquisizione dati, metodi di misura,
deployment e servizi.

**Nota** · Documento per assessment e solution design.

**Copy** · Destinatari su **una sola riga discreta**: «Operations, Engineering e
IT/OT». Non sei reparti in evidenza (§8 P01). Indice delle cinque sezioni,
elenco dei quattro annessi, blocco di emissione.

**Visuale** · Fascia scura, come la V9.2. 15–25%.

**Fonte** · master §8 P01

**Claim** · —

**Fallback** · Titolo «preliminare» finché G4 è aperto — condizione di build
n. 4, invariata dalla V9.2. Working: denominazione, referente, email e data come
`INPUT APERTO`.

---

# P02 · Executive summary

**Titolo** · D.Factory in sintesi

**Messaggio** · Che cos'è la piattaforma, in un paragrafo che si può leggere ad
alta voce.

**Paragrafo** (77 parole)
> D.Factory è una piattaforma modulare per la supervisione e l'analisi integrata
> di produzione ed energia. Acquisisce dati da sorgenti industriali esistenti, li
> contestualizza rispetto a macchina, linea, prodotto, ordine, stato e turno, e
> li rende disponibili attraverso viste operative, KPI, report e analisi
> economiche. L'architettura commerciale è composta da tre livelli cumulativi:
> Connect, Insight e Refyn.

**Copy · cinque punti chiave**
> **Brownfield** — si parte dall'impianto esistente
> **Produzione ed energia integrate** — stesso asse, stesso contesto
> **Un solo modello di contesto** — nove attributi per ogni evento
> **Livelli cumulativi** — Insight comprende Connect, Refyn comprende entrambi
> **Software e servizi** — la piattaforma è accompagnata da competenze

**Visuale** · Pagina editoriale. Nessun diagramma dominante (§8 P02). 20–30%.

**Fonte** · master §8 P02

**Claim** · `cumulativa`, `brownfield`

**Fallback** · —

---

# P03 · Architettura funzionale

**Titolo** · Dal segnale alla decisione

**Messaggio** · I cinque passaggi che il prodotto compie, in ordine.

**Paragrafo** (88 parole)
> L'acquisizione raccoglie i segnali già disponibili in impianto: stati e
> conteggi dai controllori, energia e utility dai contatori, anagrafiche e ordini
> dai sistemi gestionali. La contestualizzazione associa a ogni evento
> l'insieme di attributi che lo rende confrontabile. L'elaborazione applica le
> formule dichiarate e produce indicatori, perdite e costi. La restituzione mette
> il risultato dove viene usato, in dashboard, report ed export. La decisione
> resta alle persone: il sistema fornisce la stessa base a chi la deve prendere.

**Visuale** · Un solo schema orizzontale a cinque stazioni:
**Acquisizione → Contestualizzazione → Elaborazione → Restituzione → Decisione**.
Frase di lettura sopra, legenda sotto, conclusione a chiudere (§12.3). 45–55%.

**Fonte** · master §8 P03

**Claim** · —

**Fallback** · «Che cosa richiede» e «che cosa non presuppone» **escono da qui**
e vanno a P11 deployment (§8 P03).

---

# P04 · Base funzionale comune

**Titolo** · Una sola base dati per produzione, energia e contesto

**Messaggio** · Che cosa è comune a tutti e tre i livelli, così le tre pagine dei
moduli non ripetono le stesse funzioni.

**Paragrafo** (62 parole)
> Tutti i livelli lavorano sulla stessa acquisizione e sullo stesso modello di
> contesto. Cambia la profondità dell'analisi, non la sorgente del dato. Questa
> pagina descrive le capacità presenti fin dal livello di ingresso: sono la base
> su cui Insight aggiunge analisi e Refyn aggiunge governo delle azioni.

**Copy · quattro blocchi**
> **Dati operativi** — stati · conteggi · velocità · qualità · eventi
> **Dati energetici** — energia · potenza · utility · costi · fattori emissivi
> **Contesto** — macchina · linea · turno · prodotto · ordine · causa
> **Output comuni** — dashboard · storico · report · export

**Visuale** · Quattro colonne di uguale peso su una base comune, disegnata come
una fascia continua. 35–45%.

**Fonte** · master §8 P04

**Claim** · `cumulativa`

**Fallback** · —

---

# P05 · Connect

**Titolo** · Connect · Supervisione e baseline operativa

**Messaggio** · Il livello di accesso alla piattaforma, descritto per funzioni.

**Paragrafo** (61 parole)
> Connect costituisce il livello di accesso alla piattaforma. Rende disponibili
> in un unico ambiente lo stato delle macchine e della linea, l'avanzamento
> della produzione, gli eventi, gli indicatori OEE, i consumi e lo storico. Il
> suo obiettivo è costruire una base affidabile e condivisa prima di introdurre
> analisi più profonde.

**Copy · quattro sezioni**
> **Funzioni** — stato macchina e linea in tempo reale · timeline di marcia e
> fermo · eventi e cause associate · avanzamento della produzione · conteggi e
> velocità · OEE di macchina e linea · consumi di energia e utility · storico per
> turno, giorno, prodotto e linea
> **Output** — dashboard operative · report standard · export dati · viste per
> bordo linea e ufficio
> **Configurazioni** — anagrafiche di macchina, linea e prodotto · calendario e
> turni · soglie e stati · utenti e viste
> **Limiti** — non comprende analisi delle cause, correlazioni, costo specifico e
> governo delle azioni: sono di Insight e Refyn

**Visuale** · Una vista di prodotto **grande**, ricostruita: stato di linea,
timeline del turno, elenco eventi. È una delle poche pagine del dossier che
mostra il prodotto. 40–50%.

**Fonte** · master §8 P05 · funzioni identiche a Sales S09

**Claim** · —

**Fallback** · «Chi la usa», «decisione abilitata» e i callout numerati laterali
**escono** (§8 P05). G5 · `PH_REAL_SCREENSHOT_MAPST` come `ASSET RICHIESTO`.

---

# P06 · Insight

**Titolo** · Insight · Analisi delle perdite e quantificazione del valore

**Messaggio** · Che cosa aggiunge, funzione per funzione.

**Paragrafo** (57 parole)
> Insight estende Connect con strumenti di analisi delle cause, delle
> micro-fermate, delle perdite di velocità e dei consumi. Le misure di produzione
> ed energia vengono confrontate sullo stesso contesto per quantificare il peso
> operativo ed economico degli eventi e costruire priorità condivise.

**Copy · tre famiglie**
> **Perdite produttive** — analisi cause di fermo · micro-fermate · perdite di
> velocità · blocking e starvation · confronto tra macchine, linee e periodi
> **Energia e costo** — energia per stato produttivo · consumi specifici · costo
> energetico per pezzo · CO₂ calcolata o stimata · confronto per prodotto, ordine
> e turno
> **Analisi avanzate** — KPI e formule configurabili · correlazioni · ranking ·
> priorità economiche · report periodici e direzionali

**Output** · ranking · confronti · report · costi specifici · KPI avanzati.

**Visuale** · Un ranking o un report, **non due micro-dashboard** (§8 P06).
40–50%.

**Fonte** · master §8 P06 · funzioni identiche a Sales S10

**Claim** · `costo_en`, `co2`

**Fallback** · G5 · `PH_REAL_REPORT_EXPORT` come `ASSET RICHIESTO`.

---

# P07 · Refyn

**Titolo** · Refyn · Governo delle azioni e verifica dei benefici

**Stato** · **Modulo avanzato in sviluppo** — unica occorrenza nel Dossier.

**Paragrafo** (60 parole)
> Refyn è il livello dedicato alla gestione del miglioramento. Le opportunità
> individuate attraverso Connect e Insight vengono trasformate in priorità,
> azioni, responsabilità, target e periodi di verifica. Il beneficio viene
> confrontato con una baseline dichiarata e alimenta il ciclo successivo.

**Copy · tre famiglie**
> **Priorità** — backlog delle opportunità · ordinamento per impatto · selezione
> delle iniziative · baseline e target
> **Azioni** — attività · responsabile · scadenza · stato · evidenze ·
> avanzamento
> **Verifica** — confronto con la baseline · periodo di osservazione · beneficio
> verificato · storico dei risultati · revisione delle priorità

**Visuale** · Un ciclo semplice a tre nodi con ritorno alle priorità. 35–45%.

**Fonte** · master §8 P07 · funzioni identiche a Sales S11

**Claim** · `refyn`

**Fallback** · Escono le domande, la tabella «che cosa porta con sé un'azione» e
le note metodologiche sparse (§8 P07). Nessuna funzione futura aggiunta.

---

# P08 · Matrice funzionale

**Titolo** · Perimetro funzionale dei tre livelli

**Messaggio** · La pagina che chiarisce con precisione dove finisce un livello e
comincia il successivo.

**Paragrafo** (48 parole)
> La matrice riporta le capacità della piattaforma e il livello a cui ciascuna è
> disponibile. I livelli sono cumulativi: ogni colonna comprende quella alla sua
> sinistra. I servizi professionali non compaiono nella matrice perché sono
> orizzontali e attivabili su tutti e tre i livelli.

**Copy · matrice**, per aree, massimo quattordici righe:

| Area | Capacità | Connect | Insight | Refyn |
|---|---|---|---|---|
| Supervisione | Stato macchina e linea | Incluso | Incluso | Incluso |
| Supervisione | Eventi e cause associate | Raccolta | Analisi | Analisi |
| Produzione | Conteggi, velocità e avanzamento | Incluso | Incluso | Incluso |
| Produzione | Storico per turno, prodotto e ordine | Incluso | Incluso | Incluso |
| OEE | Disponibilità, performance, qualità | Incluso | Incluso | Incluso |
| OEE | Aggregazione di linea e regole | Standard | Avanzato | Avanzato |
| Fermi | Micro-fermate e perdite di velocità | — | Incluso | Incluso |
| Energia | Consumi e utility | Incluso | Incluso | Incluso |
| Energia | Energia per stato e consumo specifico | Base | Avanzato | Avanzato |
| Energia | Costo energetico e CO₂ | — | Incluso | Incluso |
| Analisi | KPI e formule configurabili | Standard | Avanzato | Avanzato |
| Analisi | Priorità economiche e ranking | — | Incluso | Incluso |
| Miglioramento | Azioni, responsabili e target | — | — | Previsto |
| Miglioramento | Verifica dei benefici | — | — | Previsto |

**Visuale** · Tabella piena pagina, corpo ≥ 14 px. **Nessuna mini-interfaccia**
(§8 P08). 55–70%.

**Fonte** · master §8 P08 · coerente con Sales S12 e con l'appendice A1 del deck

**Claim** · `cumulativa`

**Fallback** · Nota unica: «I servizi professionali sono attivabili su tutti e
tre i livelli.»

---

# P09 · Acquisizione dati

**Titolo** · Sorgenti, segnali e punti di misura

**Messaggio** · Da dove arrivano i dati, in generale — non su una linea
specifica.

**Paragrafo** (65 parole)
> La configurazione parte dai dati già disponibili sull'impianto. Durante
> l'assessment vengono censiti controllori, contatori, sensori, anagrafiche e
> sistemi gestionali. I segnali mancanti vengono classificati in base alla loro
> rilevanza per KPI, analisi e business case: alcuni sono necessari, altri
> migliorano la precisione, altri ancora possono essere rinviati a una fase
> successiva.

**Copy · sei aree di sorgente**
> **PLC e controllori** — stati, conteggi, allarmi, ricette
> **Sensori** — velocità, temperatura, pressione, presenza
> **Contatori** — energia elettrica, aria compressa, acqua, gas
> **Gestionale** — ordini, articoli, distinte, calendari
> **Anagrafiche** — macchina, linea, prodotto, formato, turno
> **Segnali aggiuntivi** — dove il dato non esiste o non è affidabile

**Visuale** · Schema di linea generico: sorgenti in campo, confine di rete,
acquisizione. 40–50%.

**Fonte** · master §8 P09

**Claim** · `compat`

**Fallback** · La tabella Riempitrice/Etichettatrice/Tappatrice della V9.2
**diventa un esempio dichiarato**, marcato «esempio di censimento su una linea
tipo», oppure passa in annesso. Non deve sembrare la configurazione standard del
prodotto (§8 P09).

---

# P10 · Modello di contesto

**Titolo** · Tempo, asset, prodotto e stato nello stesso modello

**Messaggio** · Perché il dato grezzo non basta. È il cuore tecnico del prodotto.

**Paragrafo** (84 parole)
> Un conteggio senza contesto non si può confrontare. Lo stesso numero di pezzi
> può appartenere a un formato veloce o a uno lento, a un turno pieno o a uno
> interrotto, a un ordine in tolleranza o a uno fuori specifica. Per questo ogni
> evento acquisito riceve un insieme fisso di attributi prima di essere
> archiviato. Sono quegli attributi a rendere possibili l'aggregazione, il
> confronto e l'attribuzione di un costo: senza di loro il dato resta un numero.

**Copy · nove attributi**
> timestamp · sito · linea · macchina · prodotto · ordine · turno · stato · causa

**Visuale** · Un evento al centro, i nove attributi disposti attorno. **Non una
timeline**: quella lettura è già su Connect e nel deck (§8 P10). 45–55%.

**Fonte** · master §8 P10

**Claim** · —

**Fallback** · La causa è **associata** e validata da chi la conosce, mai
«rilevata automaticamente» (§7.1 V9.2).

---

# P11 · Architettura e deployment

**Titolo** · Architettura applicativa e integrazione con la rete di stabilimento

**Messaggio** · Che cosa è definito dal prodotto e che cosa si decide nel
progetto.

**Paragrafo** (80 parole)
> L'architettura è organizzata su quattro livelli logici: le sorgenti in campo,
> il livello di acquisizione, l'applicazione con il proprio archivio, gli utenti
> e i sistemi a valle. Fra impianto e acquisizione esiste un confine di rete che
> viene definito con l'IT. La configurazione standard privilegia l'acquisizione
> in sola lettura; eventuali scambi ulteriori vengono definiti nel solution
> design insieme all'ambiente, alla segmentazione e alle politiche di accesso.

**Copy · due blocchi**
> **Architettura standard** — sorgenti · acquisizione · applicazione · database ·
> output
> **Parametri di progetto** — ambiente · rete · autenticazione · backup ·
> retention · accesso remoto

**Copy · che cosa richiede / che cosa non presuppone** *(migrato da P02)*
> **Richiede** — accesso in lettura ai controllori · punti di misura per le
> utility · anagrafiche di prodotto e ordine · un ambiente concordato con IT
> **Non presuppone** — sostituzione delle macchine · rifacimento completo dei
> PLC · cloud obbligatorio

**Visuale** · Schema logico a quattro livelli, con il confine di rete e il
collegamento tratteggiato verso il gestionale. 50–60%.

**Fonte** · master §8 P11 · §7.8 e §7.9 V9.2

**Claim** · `read_only`, `residenza`, `brownfield`

**Fallback** · **Non si usa «chi decide»** (§8 P11): si usa «definito nel
prodotto» e «definito nel solution design». Nota unica in fondo, non una per
riga. G4 · `PH_DEPLOYMENT_MODEL`, `PH_SUPPORTED_OS`, `PH_REQUIRED_PORTS`.

---

# P12 · Sicurezza e governo dei dati

**Titolo** · Sicurezza, accessi e ciclo di vita del dato

**Messaggio** · Le aree da coprire, nel core. I valori di progetto, nell'annesso.

**Paragrafo** (54 parole)
> I requisiti di sicurezza vengono allineati alle policy del cliente e
> formalizzati nel solution design. Il dossier descrive le aree da coprire e il
> modello che il prodotto mette a disposizione; i valori di progetto — parametri,
> responsabilità e scadenze — vengono riportati nell'annesso tecnico.

**Copy · nove aree**
> **Autenticazione** — integrazione con la directory aziendale o utenze locali
> **Ruoli** — profili di lettura, configurazione e amministrazione
> **Logging** — registro degli accessi e delle modifiche alle formule
> **Cifratura** — dati in transito e dati a riposo
> **Backup** — frequenza, ritenzione e prova di ripristino
> **Retention** — orizzonte per serie storiche ed eventi
> **Accesso remoto** — modalità e tracciamento degli interventi di supporto
> **Proprietà ed export** — formati e tempi di restituzione del dato
> **Aggiornamenti** — versioni, patch e finestre concordate

**Visuale** · Nove aree in griglia, senza tabella di responsabilità. 35–45%.

**Fonte** · master §8 P12

**Claim** · —

**Fallback** · **La formulazione sulla proprietà dei dati non viene pubblicata**
finché il legale non approva (§25 V9.2): la voce dichiara l'area, non il diritto.
«Chi decide», valore di progetto e owner stanno in **A3**.

---

# P13 · Metodo di misura · produzione

**Titolo** · OEE e perdite: perimetri dichiarati

**Messaggio** · Come si calcola quello che il prodotto misura, sul lato
produzione.

**Paragrafo** (72 parole)
> Un OEE senza perimetro non è confrontabile fra due stabilimenti. Prima del
> calcolo vengono dichiarati il tempo pianificato, le fermate programmate, la
> cadenza di riferimento di ogni formato e il criterio di conteggio dei pezzi
> conformi. Le tre componenti vengono calcolate separatamente e moltiplicate; le
> perdite vengono attribuite alla componente che le ha generate, così che il
> risultato dica non solo quanto si è perso ma dove.

**Copy · quattro grandezze**
> **Disponibilità** — tempo di marcia ÷ tempo pianificato
> **Performance** — pezzi × tempo ciclo ideale ÷ tempo di marcia
> **Qualità** — pezzi conformi ÷ pezzi totali
> **OEE** — disponibilità × performance × qualità

**Visuale** · Scomposizione a gradini 100 → 94,6 → 74,7 → 71,4, con la capacità
persa in giallo a ogni passaggio. Frase di lettura, legenda, conclusione. 45–55%.

**Fonte** · master §8 P13 · `p10_oee` V9.2 · dataset

**Claim** · `oee`

**Fallback** · Il ranking delle cause **non si ripete** qui: sta su P06 Insight.
G4 · `PH_OEE_CALENDAR_RULES`, `PH_IDEAL_CYCLE_TIME_RULE`, `PH_GOOD_COUNT_RULE`.

---

# P14 · Metodo di misura · energia

**Titolo** · Energia, costo e CO₂ per unità prodotta

**Messaggio** · Come si passa dal contatore al costo energetico del pezzo.

**Paragrafo** (76 parole)
> Il consumo viene misurato per stato produttivo, non solo per periodo: la stessa
> ora pesa in modo diverso se la linea è in marcia o ferma. L'energia del periodo
> viene divisa per i pezzi conformi dello stesso periodo per ottenere il consumo
> specifico; da lì, applicando il prezzo di fornitura e il fattore di emissione
> dichiarati, si ottengono il costo energetico e le emissioni per mille pezzi.

**Copy · cinque grandezze**
> **kWh** — energia del periodo, per stato
> **Potenza** — assorbimento in marcia e a impianto fermo
> **Consumo specifico** — kWh per mille pezzi
> **Costo** — € per mille pezzi, dal prezzo di fornitura
> **CO₂** — kgCO₂e per mille pezzi, calcolata o stimata

**Visuale** · Potenza per stato sopra; sotto, la catena 735 kWh → 162 € →
227.000 pz → 3,2 kWh / 0,71 € / 1,13 kgCO₂e per mille pezzi. 45–55%.

**Fonte** · master §8 P13 (opzione a due pagine) · `p11_energia` V9.2 · dataset

**Claim** · `costo_en`, `co2`

**Fallback** · Mai «costo del pezzo» quando il perimetro è la sola energia
(§7.3 V9.2). Prezzo e fattore di emissione arrivano dal contratto di fornitura.
Il perimetro della potenza a impianto fermo si dichiara nel solution design.

---

# P15 · Output e integrazioni

**Titolo** · Dashboard, report, export e integrazioni

**Messaggio** · Che cosa esce dal sistema, in che forma e con che frequenza.

**Paragrafo** (58 parole)
> Gli output vengono configurati in funzione del processo e del livello
> acquistato. Le informazioni possono essere consultate in dashboard, distribuite
> attraverso report, esportate in formati strutturati o rese disponibili a
> sistemi esterni. Perimetro, formato e frequenza di ogni canale vengono definiti
> nel solution design insieme ai punti di innesto verso i sistemi a valle.

**Copy · catalogo**

| Output | Contenuto | Frequenza | Modalità |
|---|---|---|---|
| Dashboard | stato, KPI, eventi | continuo | web |
| Report | KPI e confronti | programmata | PDF/Excel |
| Export | dati e aggregati | su richiesta | CSV/Excel |
| API | dati selezionati | da definire | integrazione |
| ERP | ordini e anagrafiche | da verificare | progetto |

**Visuale** · Tabella a cinque righe, senza colonne di reparto. 35–45%.

**Fonte** · master §8 P14

**Claim** · `erp`

**Fallback** · **Escono «reparto», «chi lo usa» e «che decisione abilita»**
(§8 P14). Le due domande IT migrate dalle FAQ del deck — residenza dei dati e
integrazione con il gestionale — trovano risposta qui e su P11.

---

# P16 · Delivery e pilot

**Titolo** · Dall'assessment alla decisione di scala

**Messaggio** · Il percorso completo, non solo il pilot.

**Paragrafo** (69 parole)
> Il percorso comincia con la perimetrazione della prima linea e si chiude con
> una decisione di scala presa sui risultati. L'audit censisce dati e segnali, la
> configurazione porta il dato a sistema, il pilot costruisce la baseline e le
> prime priorità, la validazione confronta i risultati con i criteri dichiarati
> all'inizio. Ogni fase produce un deliverable verificabile.

**Copy · sei fasi**
> perimetrazione · audit · configurazione · pilot · validazione · scala

**Copy · deliverable**
> mappa dati · architettura · baseline · KPI · cause · business case · proposta

**Copy · criteri di uscita** *(scritti una sola volta)*
> dati completi · formule approvate · cause validate · report condiviso

**Visuale** · Sei fasi in sequenza orizzontale, con i deliverable sotto. 30–45%.

**Fonte** · master §8 P15 · allineato a Sales S15

**Claim** · —

**Fallback** · G2 · durata, partecipanti e condizioni economiche si fissano nella
proposta di pilot.

---

# P17 · Servizi e supporto

**Titolo** · Servizi professionali e continuità operativa

**Messaggio** · Che cosa accompagna il software, prima e dopo il go-live.

**Paragrafo** (56 parole)
> Il software viene accompagnato da attività di assessment, configurazione,
> validazione e review. I servizi possono essere inclusi nell'avvio, erogati
> periodicamente o attivati su richiesta. La continuità operativa è garantita da
> un canale di supporto concordato, da finestre di aggiornamento e da revisioni
> periodiche dei KPI e delle formule.

**Copy · catalogo a nove voci**
> assessment · setup · KPI e formule · data quality review · Performance & Energy
> Review · improvement sprint · formazione · supporto · scale-up

**Copy · supporto**
> canale · orari · SLA · aggiornamenti · manutenzione · review

**Visuale** · Tabella dei servizi con «che cosa produce» e «modello», più un
blocco supporto. Ogni riga ha la sua spiegazione (§8 P16, regola). 25–40%.

**Fonte** · master §8 P16

**Claim** · —

**Fallback** · G4 · «Condizioni di supporto e SLA si formalizzano nella proposta
e nel contratto.» Unica citazione consentita di MAPST 4.0 e MarEnergy nel
dossier, se resta.

---

# Annessi

## A1 · Compatibilità tecnica

**Colonne** · componente · requisito · modalità di verifica · esito · nota.

**Contenuto** · Otto componenti: PLC · protocollo · versione · accesso ·
gateway · contatore · ERP · lettura e scrittura.

**Fallback** · **La colonna «owner» esce dalla versione client** (§9 A1). Gli
esiti restano «da verificare» finché l'audit non è svolto, ma con **una nota
unica**, non ripetuta riga per riga.

## A2 · Dimensionamento

**Contenuto** · parametri di sizing (tag, frequenza, retention, linee, utenti) e
**le tre fasce — piccola, media, grande — anche nella client edition** (§9 A2).

**Fallback** · G4 · CPU, RAM e storage restano da definire; i parametri di fascia
sono ipotesi dichiarate. Non usare soltanto frecce verso una scatola.

## A3 · Requisiti IT e security

**Contenuto** · È la sede corretta per **chi decide, valore di progetto, stato,
evidenza e owner** (§9 A3). Tono da checklist ammesso.

**Colonne** · ambito · modello · valore di progetto · chi decide · stato.

**Fallback** · Rinominato da «Sicurezza e governo». La proprietà dei dati resta
non pubblicata finché il legale non approva.

## A4 · Dizionario KPI

**Colonne** · indicatore · formula · unità · sorgente · frequenza · versione.

**Fallback** · **Escono le dodici ripetizioni** di «da nominare» e «da
approvare» (§9 A4). Al loro posto, una nota unica:

> Owner e approvazione vengono formalizzati nel dizionario KPI di progetto.

---

## Conteggio delle formule di stato aperto

Obiettivo misurabile del §12.5, verificato dal build.

| espressione | V9.2 | V9.3 |
|---|--:|--:|
| `solution design` | 16 | ≤ 8 — una per pagina, mai per riga |
| `da verificare` | 12 | ≤ 2 — solo in A1, con nota unica |
| `da approvare` | 6 | **0** — sostituito dalla nota di A4 |
| `da nominare` | 6 | **0** — idem |
| `Chi decide` / `Owner` nel core | 4 | **0** — solo in A3 |
| pagine core con paragrafo ≥ 45 parole | 1 su 14 | **17 su 17** |
