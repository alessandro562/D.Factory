# D.Factory · Sales Deck · Storyboard V9.3

**Fase B del §18.** 15 slide core + 4 appendici.

Per ogni slide: titolo, messaggio, copy definitivo, visuale, fonte, claim,
fallback. Il copy scritto qui è **quello che va negli HTML**: la fase E lo
esegue, non lo reinterpreta.

Tetti del §11.2 — narrativa 55 parole · pacchetto 70 · prodotto 45 · matrici 90.
Il conteggio è del solo testo fuori dai disegni, come nella V9.2.

Lo scenario illustrativo resta invariante dalla V8 e non viene ricalcolato:

```
un turno al giorno · 5 giorni · 46 settimane = 230 turni all'anno
500 pz/min · 0,14 €/pz → 70 €/min · fermo 18 min → 1.260 € · turno 26 min → 1.820 €
7 giorni · 58 eventi · 224 min → 15.680 € · prima causa 43%
454 min × 95 kW + 26 min × 38 kW → 735 kWh · × 0,22 → 162 € · 227.000 pz
94,6% × 79% × 95,6% → OEE 71,4%
```

---

## Ritmo del deck

| # | slide | tipo | visuale | dashboard |
|--:|---|---|--:|:--:|
| 01 | Promessa | narrativa | 35–40% | sfondo |
| 02 | Il problema di oggi | narrativa | 25–35% | — |
| 03 | Visione di prodotto | narrativa | ≤40% | — |
| 04 | Trasformazione | narrativa | 25–35% | — |
| 05 | Prodotto in azione | prodotto | 55–70% | **sì** |
| 06 | Un evento, quattro letture | prodotto | 55–65% | **sì** |
| 07 | Dall'evento alla priorità | valore | 40–50% | grafico |
| 08 | Mappa delle funzionalità | funzionalità | 30–45% | — |
| 09 | Connect | pacchetto | 25–35% | — |
| 10 | Insight | pacchetto | 25–35% | — |
| 11 | Refyn | pacchetto | 25–35% | — |
| 12 | Confronto e servizi | pacchetti | 30–45% | matrice |
| 13 | Perché D.Factory | azienda | 25–40% | — |
| 14 | Valore e modello | valore | 30–45% | formula |
| 15 | Pilot e CTA | CTA | 20–35% | — |

Quattro slide narrative in apertura, due tecniche consecutive, mai tre. Una sola
matrice nel corpo, una sola formula economica, nessuna dashboard dopo la 07.

---

# S01 · Promessa

**Titolo** · Dalla linea al margine, nello stesso dato.

**Messaggio** · In cinque secondi: industria, produzione, energia, valore.

**Copy** (24 parole)
> D.Factory unisce produzione, energia e costi per trasformare i segnali
> dell'impianto in decisioni operative.

**Visuale** · La vista di turno della V9.2, **ridotta a prova di sfondo**: fascia
inferiore, contrasto abbassato, nessun numero in evidenza tranne il margine del
turno. La headline occupa il terzo superiore e domina. 35–40%.

**Fonte** · master §4 S01 · visual `v01_cover` V9.2 · dataset

**Claim** · —

**Fallback** · Nessun badge, nessun logo cliente, nessun numero aziendale.
Working: `PH_COMPANY_BRAND_FORM` come `INPUT APERTO`.

---

# S02 · Il problema di oggi

**Titolo** · I dati esistono. / Le decisioni restano frammentate.

**Messaggio** · Il problema non è tecnico: è che tre funzioni guardano lo stesso
impianto e non arrivano alla stessa priorità.

**Copy** (52 parole)
> **Produzione** — sa che la linea ha perso capacità, ma non sempre ne conosce il
> costo.
> **Energia** — vede il consumo, ma non sempre sa a quale stato produttivo
> appartiene.
> **Direzione** — riceve indicatori diversi, in tempi diversi, senza una priorità
> comune.
>
> Il problema non è raccogliere altri dati. È dare agli stessi dati un
> significato condiviso.

**Visuale** · Immagine concettuale: tre flussi paralleli che restano separati,
un solo punto di decisione a destra che nessuno dei tre raggiunge da solo.
Linee sottili, niente etichette di sorgente, **niente dashboard**. 25–35%.

**Fonte** · master §4 S02 · §6.4 V9.2 «Ogni impianto produce dati»

**Claim** · —

**Fallback** · —

---

# S03 · Visione di prodotto

**Titolo** · Un solo contesto operativo per macchina, linea, turno e prodotto.

**Messaggio** · Che cos'è D.Factory. È la slide che il §16.1 verifica: il
prodotto si capisce entro la terza.

**Copy** (46 parole)
> D.Factory acquisisce dati da PLC, sensori, contatori e sistemi gestionali. Li
> allinea nel tempo, li associa a macchina, linea, prodotto, ordine, stato e
> causa, e li restituisce come informazioni operative, indicatori e priorità.

**Visuale** · Schema editoriale a quattro stazioni su una linea orizzontale:
**Segnali → Contesto → Evidenza → Decisione**. Sotto ciascuna, tre parole di
esempio in corpo piccolo. Nessun rettangolo che imiti un'applicazione. ≤ 40%.

**Fonte** · master §4 S03 · definizione estesa §6.2 V9.2

**Claim** · `cumulativa` non ancora; qui nessun claim tecnico.

**Fallback** · G5 · `PH_REAL_SCREENSHOT_NEW_UI` come `ASSET RICHIESTO` in working.

---

# S04 · Trasformazione per il cliente

**Titolo** · Dalla lettura separata a una gestione condivisa.

**Messaggio** · Che cosa cambia nel lavoro di chi compra. È la slide che nella
V9.2 mancava del tutto.

**Copy** (32 parole)
> **Prima** — fermi letti a memoria · consumi separati dalla produzione · cause
> non confrontabili · priorità decise per urgenza percepita · risultati difficili
> da verificare.
>
> **Dopo** — eventi contestualizzati · produzione ed energia sullo stesso tempo ·
> cause ordinate per impatto · KPI condivisi · azioni verificabili.

**Visuale** · Una sola linea di trasformazione da sinistra a destra. A sinistra
cinque voci in grigio, a destra le cinque corrispondenti in nero, collegate una a
una. Il giallo marca il passaggio, non le voci. **Nessuna dashboard.** 25–35%.

**Fonte** · master §4 S04

**Claim** · —

**Fallback** · —

**Regola** · Le cinque coppie sono in corrispondenza uno-a-uno: ogni voce di
«prima» ha la sua di «dopo», sulla stessa riga. Se una coppia non regge, si
tolgono entrambe.

---

# S05 · Prodotto in azione

**Titolo** · Il fermo, la causa e il costo nello stesso momento.

**Messaggio** · La prima vera prova di prodotto, e arriva dopo problema, visione
e trasformazione.

**Copy** (13 parole)
> Fermo 18 minuti · causa associata mancanza tappi a monte · margine perso
> stimato 1.260 €.

**Visuale** · La vista di `v04_evento_prodotto` della V9.2, invariata nella
sostanza: finestra 10:00–12:00 sulle tre macchine, fermo della tappatrice
selezionato, curva OEE sotto, un solo indicatore verticale che attraversa
timeline e curva. 55–70%.

**Fonte** · master §4 S05 · `v04_evento_prodotto` V9.2 · dataset

**Claim** · —

**Fallback** · «Vista ricostruita · dati illustrativi» a piede pagina.
G5 · `PH_REAL_SCREENSHOT_MAPST`.

---

# S06 · Un evento, quattro letture

**Titolo** · Lo stesso evento pesa su capacità, energia, costo e servizio.

**Messaggio** · Un solo fermo, letto su quattro assi: è la sintesi che nella V9.2
occupava due slide e mezzo.

**Copy** (16 parole)
> Le quattro letture escono dallo stesso intervallo, senza ricalcoli e senza
> cambiare strumento.

**Visuale** · Una timeline centrale con l'intervallo 11:24–11:42 marcato in
giallo. Quattro output laterali, uno per lettura:

| lettura | valore |
|---|---|
| **Capacità** | 18 minuti · 9.000 pezzi non prodotti |
| **Energia** | 38 kW a linea ferma · 11,4 kWh nell'intervallo |
| **Costo** | 1.260 € di margine perso · 2,5 € di energia improduttiva |
| **Impatto operativo** | OEE del turno da 74,3% a 71,4% |

Una sola timeline, quattro caselle. **Non due dashboard sovrapposte.** 55–65%.

**Fonte** · master §4 S06 · fusione di `v05_energia` e `v07_ampiezza` V9.2 ·
dataset

**Claim** · `costo_en`

**Fallback** · G3 · nessun valore annualizzato. G5 ·
`PH_REAL_SCREENSHOT_MARENERGY`.

**Verifica aritmetica** · 18 min × 500 pz/min = 9.000 pz · 18 min × 38 kW ÷ 60 =
11,4 kWh · 11,4 × 0,22 = 2,5 € · disponibilità senza il fermo:
(454+18)/480 = 98,3%, con il fermo 94,6% → OEE 74,3% → 71,4%.

---

# S07 · Dall'evento alla priorità

**Titolo** · Il valore non è vedere un fermo. / È sapere quale problema chiudere
per primo.

**Messaggio** · La lista di priorità è il prodotto, non il grafico.

**Copy** (40 parole)
> D.Factory aggrega frequenza, durata, perdita di capacità e consumo per
> trasformare gli eventi in una lista di priorità leggibile.
>
> La prima causa vale il 43% del costo di fermo della settimana. Le micro-fermate
> sono trentotto eventi e valgono meno della metà.

**Visuale** · Ranking a **quattro cause**, ordinate per costo stimato, con barra
proporzionale e totale. Nessuna intestazione di applicazione, nessun chrome da
interfaccia: è un grafico, non una schermata. 40–50%.

| causa | eventi | durata | costo stimato |
|---|--:|--:|--:|
| Mancanza tappi | 14 | 96 min | 6.720 € |
| Cambio formato | 4 | 62 min | 4.340 € |
| Micro-fermate | 38 | 41 min | 2.870 € |
| Manutenzione | 2 | 25 min | 1.750 € |
| **totale** | **58** | **224 min** | **15.680 €** |

**Fonte** · master §4 S07 · `v06_priorita` V9.2 · dataset

**Claim** · —

**Fallback** · «Scenario illustrativo · non risultato cliente».

**Regola §5.1 dell'audit** · Questa slide è di tipo **valore**, non prodotto: il
titolo e il paragrafo dominano, il grafico sta sotto. È così che le slide
tecniche consecutive restano due.

---

# S08 · Mappa delle funzionalità

**Titolo** · Una piattaforma, cinque aree di capacità.

**Messaggio** · Che cosa comprende il prodotto, prima di parlare di pacchetti.

**Copy** (54 parole, in cinque fasce)

> **Supervisione** — stato macchina e linea · produzione · avanzamento · eventi ·
> storico
> **Performance** — OEE · disponibilità · velocità · micro-fermate · qualità e
> scarti
> **Energia e utility** — consumi · energia per stato · costo energetico ·
> consumi specifici · CO₂
> **Analisi e priorità** — cause · confronti · correlazioni · impatto economico ·
> ranking
> **Miglioramento** — priorità · azioni · owner · target · verifica dei benefici

**Visuale** · Composizione editoriale: cinque fasce orizzontali, una linea
continua che le attraversa da sinistra a destra, un microsegno per area.
**Nessuna mini-dashboard, nessun grafico.** 30–45%.

**Fonte** · master §4 S08

**Claim** · —

**Fallback** · La quinta area è di Refyn e porta il rimando a S11, non lo stato
«in sviluppo»: l'unica occorrenza del deck è su S11.

---

# S09 · Connect

**Titolo** · Connect. / Rende affidabile ciò che sta succedendo.

**Messaggio** · La base operativa condivisa. Prima riga della progressione.

**Copy** (68 parole)

> La base operativa condivisa per vedere, misurare e storicizzare produzione ed
> energia.
>
> **Supervisione** — stato macchina e linea in tempo reale · timeline di marcia e
> fermo · eventi e cause associate · avanzamento della produzione · conteggi e
> velocità
> **Indicatori** — OEE di macchina e linea · disponibilità, performance e
> qualità · consumi di energia e utility · storico per turno, giorno, prodotto e
> linea
> **Output** — dashboard operative · report standard · export dati · viste per
> bordo linea e ufficio

**Risultato** · Una baseline affidabile e condivisa.

**Attivazione** · Assessment, setup, configurazione e canone ricorrente.

**Visuale** · Nome molto grande a sinistra, tre blocchi funzionali a destra, una
riga di risultato in fondo. Il giallo marca solo la riga risultato.
**Nessuno screenshot, nessun grafico, nessuna timeline.** 25–35%.

**Fonte** · master §5 e §4 S09

**Claim** · `cumulativa`

**Fallback** · G2 · `PH_SERVICES_INCLUDED` in working; in client l'attivazione
resta descrittiva, senza importi.

---

# S10 · Insight

**Titolo** · Insight. / Spiega dove si perde capacità, energia e valore.

**Messaggio** · Comprende Connect e aggiunge analisi, confronto e
quantificazione.

**Copy** (70 parole)

> Aggiunge analisi, confronto e quantificazione alla base Connect.
>
> **Perdite produttive** — analisi cause di fermo · micro-fermate · perdite di
> velocità · blocking e starvation · confronto tra macchine, linee e periodi
> **Energia e costo** — energia per stato produttivo · consumi specifici · costo
> energetico per pezzo · CO₂ calcolata o stimata · confronto per prodotto, ordine
> e turno
> **Analisi avanzate** — KPI e formule configurabili · correlazioni · ranking per
> frequenza, durata, costo o impatto · priorità economiche · report periodici e
> direzionali

**Risultato** · Sapere dove intervenire e perché.

**Attivazione** · Comprende Connect e aggiunge capacità analitiche e review
specialistiche.

**Visuale** · Stessa griglia di S09. Sopra il nome, un segmento che mostra
Connect già acquisito. 25–35%.

**Fonte** · master §5 e §4 S10

**Claim** · `cumulativa`, `costo_en`, `co2`

**Fallback** · —

---

# S11 · Refyn

**Titolo** · Refyn. / Trasforma le priorità in un processo di miglioramento
verificabile.

**Stato** · **Modulo avanzato in sviluppo** — unica occorrenza nel Sales Deck.

**Messaggio** · Comprende Connect e Insight e aggiunge governo delle azioni e
verifica del beneficio.

**Copy** (66 parole)

> Aggiunge governo delle azioni e verifica del beneficio alla base Connect e
> Insight.
>
> **Priorità** — backlog delle opportunità · ordinamento per impatto · selezione
> delle iniziative · baseline e target
> **Azioni** — attività · responsabile · scadenza · stato · evidenze · note e
> avanzamento
> **Verifica** — confronto con la baseline · periodo di osservazione · beneficio
> verificato · storico dei risultati · revisione delle priorità

**Risultato** · Rendere il miglioramento un ciclo governato, non un elenco di
buone intenzioni.

**Attivazione** · Progetto pilota dedicato, con perimetro e modello economico
concordati.

**Visuale** · Stessa griglia di S09 e S10, con il segmento che mostra Connect e
Insight già acquisiti. 25–35%.

**Fonte** · master §5 e §4 S11

**Claim** · `refyn`, `cumulativa`

**Fallback** · Nessuna funzione futura oltre a queste quindici (§4 S11, regola).
G2 · `PH_REFYN_PRICING_MODEL`.

---

# S12 · Confronto dei livelli e servizi

**Titolo** · Ogni livello contiene il precedente. / I servizi accelerano il
risultato.

**Messaggio** · La risposta alla domanda commerciale principale, nel corpo e non
in appendice.

**Copy · parte 1** · matrice a nove righe (§4 S12)

| Capacità | Connect | Insight | Refyn |
|---|---|---|---|
| Stato, produzione e storico | Base | Base | Base |
| OEE e KPI standard | Incluso | Incluso | Incluso |
| Energia e utility | Incluso | Incluso | Incluso |
| Cause, micro-fermate e velocità | Raccolta | Analisi | Analisi |
| Energia per stato e costo specifico | Base | Avanzato | Avanzato |
| KPI, formule e confronti | Standard | Avanzato | Avanzato |
| Priorità economiche | — | Incluso | Incluso |
| Azioni e owner | — | — | Previsto |
| Verifica dei benefici | — | — | Previsto |

**Copy · parte 2** · i nove servizi orizzontali, su una riga sola sotto la
matrice: assessment e perimetrazione · setup e integrazione · KPI e formule ·
data quality review · Performance & Energy Review · improvement sprint ·
formazione · supporto · scale-up.

**Visuale** · Matrice grande, non compressa, senza note minuscole. Corpo ≥ 15 px,
intestazioni ≥ 14 px. Leggibile a 640×360 (§16.4). 30–45%.

**Fonte** · master §4 S12

**Claim** · `cumulativa`

**Fallback** · Nota unica: «I servizi sono attivabili su tutti e tre i livelli.
Che cosa è compreso nell'avvio è indicato nella proposta economica.»

**Nota sui valori** · La scala di questa matrice è quella del master, che
introduce *Base*, *Raccolta*, *Analisi* e *Standard* accanto a *Incluso*,
*Avanzato* e *Previsto*. Sostituisce la scala a cinque valori della V9.2, che
resta valida per l'appendice A1.

---

# S13 · Perché D.Factory

**Titolo** · Costruito per l'impianto reale. / Non per una demo isolata.

**Messaggio** · Perché sceglierci come azienda. Tre principi, nessun grafico.

**Copy** (55 parole)

> **Brownfield first** — Si parte da PLC, sensori, contatori e sistemi già
> presenti. Compatibilità e gap vengono verificati sull'impianto reale.
> **Un solo contesto** — Produzione, energia, prodotto, ordine, stato e causa
> vengono letti sullo stesso asse.
> **Software e competenze** — La piattaforma viene accompagnata da assessment,
> configurazione, review e supporto al miglioramento.

**Visuale** · Composizione editoriale a tre colonne, numerate, con un dettaglio
industriale come sfondo o un asset reale se disponibile. **Nessuna timeline,
nessun asse produzione/energia**: quella lettura vive già su S05 e S06. 25–40%.

**Fonte** · master §4 S13 · §6.5, §6.6, §6.7 V9.2

**Claim** · `brownfield`

**Fallback** · **G5 aperto: nessun numero aziendale.** Il §4 S13 ammette al
massimo due elementi reali fra rapporto con il gruppo, anno, progetti, linee,
screenshot, report — nessuno è approvato. La slide regge sui tre principi, come
il master stesso prevede. Working: `PH_GROUP_RELATIONSHIP`,
`PH_COMPANY_FOUNDING_YEAR`, `PH_PROJECTS_COMPLETED` come `INPUT APERTO`.

---

# S14 · Valore e modello commerciale

**Titolo** · Il valore nasce dal dato. / Il contratto cresce con il perimetro.

**Messaggio** · Come si crea valore e come si compra, sulla stessa slide.

**Copy · parte 1 · valore** (34 parole)

> Quattro leve: capacità potenzialmente recuperabile · energia potenzialmente
> evitabile · qualità e scarti · tempo decisionale ridotto.
>
> **minuti di perdita × valore unitario × frequenza**
>
> Il risultato si calcola sui dati della vostra linea, durante l'audit.

**Copy · parte 2 · modello commerciale** (30 parole)

> **Avvio** — assessment · setup · integrazione · configurazione
> **Ricorrente** — modulo · sito o linea · supporto · aggiornamenti
> **Opzionale** — review · improvement sprint · formazione · scale-up

**Visuale** · A sinistra le quattro leve e la formula in grande; a destra le tre
voci del modello, incolonnate. Una sola formula economica nel corpo del deck
(§11.3). 30–45%.

**Fonte** · master §4 S14 · §21.3 V9.2 per la nota metodologica

**Claim** · `costo_en`

**Fallback** · **G3 aperto: nessun risultato annualizzato**, né in cifre né in
lettere — vale anche per il testo alternativo delle figure. Nota: «In questo
scenario la leva principale è la capacità recuperabile. Il dato energetico
completa la lettura e misura il consumo improduttivo dello stesso evento.»
G2 aperto: gli importi restano in appendice A3, il **modello** resta nel corpo,
come chiede il §4 S14.

---

# S15 · Pilot e CTA

**Titolo** · Partiamo da una linea e decidiamo sui risultati.

**Messaggio** · Il passo successivo, azionabile.

**Copy** (44 parole)

> **Perimetrazione** — dati · linea · obiettivi · vincoli
> **Pilot** — baseline · prime cause · consumi · priorità
> **Decisione** — risultati · gap · proposta · scala
>
> Condividiamo la prima linea, i dati disponibili e la decisione che vuoi
> migliorare.

**Contatto** · nome · ruolo · email · sito o telefono.

**Visuale** · Tre passi in sequenza orizzontale, generosi di spazio bianco.
**Nessuna seconda dashboard** (§4 S15). 20–35%.

**Fonte** · master §4 S15

**Claim** · —

**Fallback** · **G1 aperto: il blocco contatto non porta il referente.** Working:
`nome · ruolo · email — INPUT APERTO`. Client: il blocco esce e il build emette
il warning globale — il deck si presenta dal vivo, non si invia da solo.

---

# Appendici

## A1 · Matrice completa delle funzionalità

**Titolo** · Perimetro funzionale, area per area.

**Contenuto** · Massimo 14 righe, organizzate per area: supervisione ·
produzione · OEE · fermi · energia · qualità · analisi · miglioramento · output ·
integrazioni.

**Visuale** · Tabella piena pagina, corpo leggibile, nessuna nota minuscola.
50–75%.

**Fallback** · Valori della scala V9.2 — incluso, configurabile, avanzato,
previsto, non incluso.

## A2 · Catalogo servizi

**Titolo** · Il software rende visibile. Le competenze accelerano il risultato.

**Colonne** · servizio · cosa comprende · deliverable · frequenza ·
incluso/opzionale.

**Contenuto** · I nove servizi del §5. La colonna «cosa comprende» è nuova
rispetto alla V9.2.

**Fallback** · G2 aperto: la colonna incluso/opzionale dice «in proposta» su
tutte le righe, con una nota unica.

## A3 · Struttura economica *(condizionata a G2)*

**Contenuto** · assessment · setup · canone Connect · canone Insight · Refyn ·
linee successive · servizi.

**Fallback** · G2 aperto: **appendice esclusa dalla client edition**, presente
nella working con gli importi come `DECISIONE COMMERCIALE`.

## A4 · FAQ commerciali

**Contenuto** · Sei domande, tutte commerciali:

1. Quanto tempo serve per vedere i primi risultati?
2. Serve fermare la linea per partire?
3. Funziona su macchine di marche diverse?
4. Che cosa comprende l'avvio?
5. Come si passa dal pilot alla scala?
6. Che cosa succede se mancano dei dati?

**Fallback** · Le due domande IT della V9.2 — residenza dei dati e integrazione
con il gestionale — **migrano nel dossier**, pagine 11 e 15 (§6 A4).

---

## Appendice di lavoro · A5 assunzioni *(working only)*

Resta fuori dalla client edition, condizionata a G3, come registrato nel §5.3
dell'audit. Dieci parametri con valore, origine e stato.

---

## Placeholder e gate, per slide

| slide | gate | token |
|---|---|---|
| S01 | G1 · G3 | `PH_COMPANY_BRAND_FORM`, `PH_DATASET_VALIDATOR` |
| S03 | G5 | `PH_REAL_SCREENSHOT_NEW_UI` |
| S05 | G5 | `PH_REAL_SCREENSHOT_MAPST` |
| S06 | G3 · G5 | `PH_DATASET_STOPPED_POWER`, `PH_REAL_SCREENSHOT_MARENERGY` |
| S09 · S10 · S11 | G2 | `PH_SERVICES_INCLUDED`, `PH_SERVICES_OPTIONAL`, `PH_REFYN_PRICING_MODEL` |
| S12 | G2 | `PH_SERVICES_INCLUDED` |
| S13 | G5 | `PH_GROUP_RELATIONSHIP`, `PH_COMPANY_FOUNDING_YEAR`, `PH_PROJECTS_COMPLETED` |
| S14 | G2 · G3 | `PH_AUDIT_PRICE`, `PH_CONNECT_ANNUAL_FEE`, `PH_DATASET_*` |
| S15 | G1 | `PH_CONTACT_NAME`, `PH_CONTACT_ROLE`, `PH_CONTACT_EMAIL` |
| A3 | G2 · PAGE | dieci importi |
