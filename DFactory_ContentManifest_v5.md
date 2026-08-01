# D.Factory · Content Manifest v5

Fonte di verità per `DFactory_SalesDeck_v5.html` (11 slide + 4 appendici) e
`DFactory_DossierTecnico_v5.html` (31 pagine). Se un claim cambia qui, cambia in entrambi.

Sostituisce il Content Manifest v4. La differenza non è di nomi: cambia l'architettura
commerciale.

---

## 1. Terminologia canonica

| Concetto | Forma corretta | Regola d'uso |
|---|---|---|
| Brand | `D.Factory` | Solo copertina, chiusura e riferimenti societari. Mai come prefisso di modulo |
| Società | `D Factory S.r.l.` | Solo nei rail di copertina e chiusura |
| Livello 1 | `Connect` | Mai "D.Factory Connect" |
| Livello 2 | `Insight` | **Singolare.** Mai `Insights` |
| Livello 3 | `Refyn` | Modulo, non servizio, non azienda. Mai "Refyn by D.Factory" |
| Legacy produzione | `MAPST 4.0` | Prodotto legacy, non piattaforma corrente |
| Legacy energia | `MarEnergy` | Prodotto legacy energetico |
| Servizi | `servizi a valore aggiunto` | Livello orizzontale. Mai sinonimo di Refyn |
| Stato | `stato macchina` / `stato linea` | Distinti |
| Efficienza | `OEE macchina` / `OEE di linea` | Non intercambiabili |
| Energia | `energia e utility` | Acqua inclusa fra le utility |
| Emissioni | `CO₂ calcolata o stimata` | Mai "CO₂ misurata" |
| Costo unitario | `costo energetico per pezzo` | Mai "costo per unità" |
| Migrazione | `migrazione volontaria dal legacy` | Mai "migrazione" senza "volontaria" |
| Impianti esistenti | `brownfield` | Spiegato alla prima occorrenza |
| Polmone | `polmone` | `buffer` spiegato una volta |
| Compatibilità | `multi-vendor`, `multi-protocollo` | Sempre "previa verifica" |

### Architetture di brand vietate

`Refyn by D.Factory` · `D.Factory Refyn` · `Refyn, a D.Factory product` · qualsiasi altra
composizione non approvata. I tre moduli si nominano da soli.

### Correzioni obbligatorie rispetto al v4

| v4 | v5 |
|---|---|
| `Insights` | `Insight` |
| Refyn = servizi sul dato, in definizione | Refyn = terzo modulo cumulativo, in sviluppo |
| `D.Factory` = nome del prodotto, ovunque | `D.Factory` = brand, solo copertina e chiusura |
| `MAPST 4.0` = piattaforma su cui è costruito il sistema | `MAPST 4.0` = prodotto legacy produzione |
| `MarEnergy` assente | `MarEnergy` = prodotto legacy energia |
| Servizi dentro Refyn | Servizi orizzontali su tutti i moduli |
| "Un solo modello dati" come claim | Formulazione prudente finché non confermato, vedi §6 |

---

## 2. Architettura commerciale

**Cumulativa.** Insight include Connect. Refyn include Connect e Insight. Ogni livello
contiene sia produzione/OEE sia energia. I livelli si distinguono per profondità decisionale,
non per tipo di dato.

| Modulo | Domanda a cui risponde | Valore | Stato del packaging |
|---|---|---|---|
| **Connect** | Che cosa sta succedendo? | Visibilità e baseline | Pilot release |
| **Insight** | Perché sta succedendo e quanto pesa? | Diagnosi e quantificazione | Pilot release |
| **Refyn** | Che cosa conviene fare, e ha funzionato? | Priorità, azioni, verifica | In development |

**Segmentazione vietata.** Connect = solo OEE, Insight = solo energia, Refyn = solo
consulenza. Ogni modulo contiene entrambe le anime.

Le tre domande sono una struttura di prodotto interna. Non sono obbligatorie come slogan
pubblico.

### Il livello orizzontale

I **servizi a valore aggiunto** sono attivabili su tutti e tre i moduli. Non sono Refyn.
Refyn può integrarne alcuni, ma il catalogo resta separato: vedi
`DFactory_ServicesCatalogue_v5.md`.

---

## 3. Modello di maturità

Ogni funzione dichiara **due stati**, che non si escludono: la maturità della *capability* e
la maturità del *packaging*.

| Stato | Significato |
|---|---|
| `Proven legacy` | Funzione già presente e documentata in MAPST 4.0 o MarEnergy |
| `Pilot release` | Funzione o packaging disponibile sui nuovi clienti pilota |
| `In development` | Funzione net-new, in sviluppo |
| `Roadmap` | Valutata, non pianificata o non avviata |
| `Project-dependent` | Dipende da impianto, sensori, dati, protocolli, ERP, rete o configurazione |
| `Not offered` | Non offerta |

Esempio di lettura corretta:

> Analisi consumi storici · Capability: proven legacy · Modulo Insight: pilot release

Un unico bollino "disponibile" che confonda maturità funzionale e maturità del pacchetto è
vietato.

### Resa grafica

Cinque pesi distinguibili anche in scala di grigi: quadrato pieno (proven legacy), contorno
pieno (pilot release), contorno misto (project-dependent), contorno punteggiato (in
development), contorno sottile (roadmap). La parola accompagna sempre il segno.

---

## 4. Prodotti legacy

- MAPST 4.0 e MarEnergy **restano attivi** per i clienti esistenti che non vogliono migrare.
- Sono la base tecnologica e funzionale da cui evolvono i nuovi moduli.
- **Non** sono il centro della nuova comunicazione commerciale.
- **Non** si afferma che esista già una migrazione tecnica uno-a-uno.
- **Non** si afferma che verranno dismessi.
- **Non** si spinge la migrazione come obbligatoria.

### Dove compaiono

| Documento | Trattamento |
|---|---|
| Sales deck | Fuori dal corpo principale e fuori dal visual di slide 3. Nota discreta in slide 8, pagina dedicata in appendice A4 |
| Dossier | Pagina 03 (provenienza delle capability), pagina 30 (migrazione volontaria), colonna "provenienza" nella capability matrix |

Formula approvata per il deck, da validare prima dell'uso esterno:

> La nuova offerta evolve le capability sviluppate in MAPST 4.0 e MarEnergy in una struttura
> modulare per i nuovi progetti.

---

## 5. Contenuti del sales deck

| # | ID | Tesi | Visual dominante |
|---|---|---|---|
| 01 | `s01_promessa` | Dalla linea al margine, nello stesso dato | Turno di cinque macchine, un fermo marcato |
| 02 | `s02_punto_cieco` | La linea si ferma, l'energia no | Due curve sullo stesso asse dei tempi |
| 03 | `s03_come_funziona` | Produzione ed energia nello stesso contesto | Convergenza delle sorgenti su un ambiente unico |
| 04 | `s04_prodotto` | Un fermo diventa una decisione entro il turno | Tre macchine: anomalia, causa, decisione |
| 05 | `s05_decisioni` | Un evento, tre decisioni che non si somigliano | Biforcazione da un evento |
| 06 | `s06_differenziatore` | Macchina ferma non significa linea ferma | Due scenari a confronto · **marcata Refyn, in sviluppo** |
| 07 | `s07_ipotesi_misure` | Le domande a cui oggi rispondi a memoria | Confronto prima/dopo |
| 08 | `s08_architettura` | Tre livelli cumulativi, servizi trasversali | **Nuova.** Scala a tre livelli con stato |
| 09 | `s09_valore` | Due leve, sullo stesso evento | Due barre proporzionali e la somma |
| 10 | `s10_percorso` | Ogni passo ha un criterio di uscita | Timeline a quattro momenti con stato del modulo |
| 11 | `s11_cta` | Condividiamo il perimetro della prima linea | Tipografico |
| A1 | `a01_offerta` | Dettaglio dei tre moduli e dei servizi | Tabella a tre colonne |
| A2 | `a02_faq` | Sette obiezioni ricorrenti | Due colonne |
| A3 | `a03_ipotesi` | Input dell'esempio economico | Due colonne |
| A4 | `a04_legacy` | Continuità di MAPST 4.0 e MarEnergy | Tre blocchi |

## 6. Contenuti del dossier

**Sezione A · prodotto e maturità** — 01 cover · 02 architettura commerciale · 03 provenienza
delle capability · 04 architettura tecnica · 05 mappa di acquisizione · 06 capability matrix

**Sezione B · funzioni proven e pilot** — 07 supervisione · 08 OEE e fermi · 09 velocità,
qualità, micro-fermi · 10 multi-linea e multi-sito · 11 distribuzione energia · 12 costo e
CO₂ · 13 metodo di misura · 14 correlazione produzione–energia

**Sezione C · Refyn in sviluppo** — 15 opportunity prioritization · 16 action management e
benefit tracking · 17 OEE di linea avanzato · 18 roadmap controllata

**Sezione D · integrazione e IT** — 19 brownfield macchine · 20 brownfield rete · 21
deployment · 22 specifiche IT/OT · 23 sensoristica · 24 output e integrazioni

**Sezione E · servizi, delivery e migrazione** — 25 catalogo servizi · 26 milestone · 27
RACI · 28 criteri del pilot · 29 supporto · 30 migrazione legacy · 31 checklist audit

---

## 7. Claim: formulazioni vincolate

Il dettaglio completo sta in `DFactory_ClaimConformity_v5.md`. Le regole che governano il
copy:

| Non usare | Usare | Perché |
|---|---|---|
| "un solo modello dati" | "produzione ed energia nello stesso contesto", "una lettura integrata" | Claim da validare tecnicamente |
| "database condiviso" | — | Non pubblicare finché non confermato |
| "on-premise" come fatto | "deployment definito in solution design; on-premise è l'assetto previsto" | Da validare |
| "nessuna uscita verso internet" | "nel perimetro concordato con il tuo IT non è previsto traffico verso internet dalla rete di linea" | Da validare |
| "17 stati PackML" | "stati PackML dove la macchina li espone · da verificare per modello" | Da validare |
| "buffer-aware" come funzione disponibile | "logica buffer-aware · Refyn · in sviluppo" | Non implementata |
| "nessun hardware proprietario" | "l'assetto previsto non richiede hardware proprietario a bordo linea · da verificare per impianto" | Da validare |
| "first signal in due giorni" | — | Non pubblicare finché non validato |
| "tempo reale" da solo | "aggiornamento configurato, tipicamente pochi secondi · da confermare per impianto" | Frequenza non documentata |
| "CO₂ misurata" | "CO₂ calcolata o stimata" | Il metodo è di calcolo |
| "intelligenza artificiale" | "regole, statistica, deviazioni, pattern" | Nessuna funzione AI esiste |
| "Operator Performance Index" | "Operational Performance Index" | Misura processo, non persone. Riduce rischio HR |
| "consulenza inclusa" | Nome del servizio + deliverable + frequenza | Formula generica vietata |

## 8. Ripartizione fra i due documenti

| Contenuto | Sales deck | Dossier |
|---|---|---|
| `D.Factory` come brand | copertina e chiusura | copertina e chiusura |
| Connect / Insight / Refyn | slide 08, appendice A1 | pagine 02, 06 e sezione C |
| `MAPST 4.0`, `MarEnergy` | nota in slide 08, appendice A4 | pagine 03, 06, 30 |
| Catalogo servizi | appendice A1, sintesi | pagina 25, completo |
| Protocolli, porte, sizing, auth, backup | mai | pagine 21 e 22 |
| Stati di maturità | slide 08 e 10, sintetici | ovunque, per funzione |
| Prezzi e importi | mai | mai |
| Numeri di trazione | mai | mai |
| Migrazione legacy | appendice A4 | pagina 30 |

## 9. Grammatica visiva: cosa NON è condiviso

| | Sales deck | Dossier |
|---|---|---|
| Impianto | Libero, una silhouette diversa per slide | Fisso: fascia di consultazione + campo |
| Titolo | 40–64 px, è una conclusione | 25–30 px nella fascia, è una domanda |
| Corpo | 16–19 px | 14–15 px |
| Componenti | Nessuna card, nessuna matrice | Matrici, stati, blocchi solution design |
| Stati | Sintetici, solo dove servono | Su ogni funzione |

Condiviso: palette nero / bianco / `#E6E011`, font Geist, il giallo come segnale unico,
canvas 1280 × 720, lo stesso evento produttivo raccontato nei visual.
