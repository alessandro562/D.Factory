# D.Factory · ChangeLog v9

Dalla V8 (21 canvas deck + 18 dossier, una sola edizione) alla V9 (**quattro
edizioni**: working e client per ciascun documento, con un sistema di placeholder
dichiarati). Il sistema grafico V8 non è stato toccato: palette, font, uso del
bianco e del nero, ruolo del giallo, grammatica delle viste, formato 1280×720.

---

## 1. La cosa nuova: due edizioni da un corpo solo

I due HTML non sono scritti due volte. Esiste un **corpo master** per documento,
in cui i blocchi portano un attributo:

| attributo | significato |
|---|---|
| `data-ed="working"` | impalcatura editoriale e placeholder |
| `data-ed="client"` | la formulazione prudente che li sostituisce |
| `data-ph-page` | canvas che nella client edition non esiste |

`work_v9/edition.py` deriva le due edizioni togliendo fisicamente i blocchi
dell'altra. Alla fine della derivazione client fa una cosa sola ma la fa sempre:
cerca `\{\{PH_[A-Z0-9_]+\}\}` e **fallisce il build** se ne trova uno. Non
avvisa: fallisce. È il modo più semplice per garantire la §11.4.

La banda `INPUT APERTI` della working edition sta sotto il piede del documento,
in monospaziato e con i token in un riquadro tratteggiato: si vede a colpo
d'occhio che non fa parte del documento.

---

## 2. Registro placeholder · `DFactory_PlaceholderRegister_v9.md`

**220 placeholder dichiarati**: 104 P0, 109 P1, 7 P2. Ognuno con ID, descrizione,
owner, fonte richiesta, priorità, documento, canvas, comportamento nelle due
edizioni, stato e data di verifica. Tutti in stato `OPEN`.

Il registro è la fonte unica: i generatori lo importano e **il build fallisce se
un `{{PH_...}}` usato negli HTML non è dichiarato**. Non è possibile aggiungere un
placeholder al volo senza dichiararlo.

Dove si concentra il lavoro:

| owner | P0 | totale |
|---|--:|--:|
| Tecnico | 45 | 91 |
| Commerciale | 30 | 52 |
| Tecnico + IT | 18 | 38 |
| Legale | 9 | 21 |
| Direzione | 1 | 13 |
| Marketing | 1 | 5 |

---

## 3. Sales Deck · da 16 slide V8 a 13 + 5 appendici + caso cliente

### Fusioni e spostamenti

| V9 | slide | da dove viene | che cosa è successo |
|---|---|---|---|
| 04 | Il fermo si vede. La causa e il costo devono essere leggibili nello stesso momento. | **V8 04 + V8 05** | le due slide dicevano la stessa cosa a due livelli di dettaglio. Resta la vista ricca della V8·05 con la headline che unisce le due domande |
| 12 | Una linea. Una baseline. Una decisione di scala. | **V8 15 + V8 14** | il pilot riprende la struttura economica in tre voci: avvio, canone, servizi. Il dettaglio con i moltiplicatori scende in A3 |
| A2 | Il software rende visibile. Le competenze accelerano il risultato. | **V8 11 + V8 A2** | la slide «servizi a valore aggiunto» scende in appendice e si fonde con la tabella dei servizi, che guadagna la colonna **obiettivo** |

### Mappa completa

`V8 01→V9 01` · `02→02` · `03→03` · `04+05→04` · `06→05` · `07→06` · `08→07` ·
`09→08` · `10→09` · `12→10` · `13→11` · `14+15→12` · `16→13` · nuova `14 caso cliente`
· `A1→A1` · `11+A2→A2` · `A3→A3` · `A4→A4` · `A5→A5`

### Nuova slide 14 · caso cliente

Esiste **solo nella working edition**. Quattro colonne numerate — contesto,
problema, intervento, risultati — più citazione e limiti dichiarati della misura.
Ogni campo è un placeholder: **33 token su un canvas solo**, il più denso dei due
documenti. È fatta per far vedere che cosa serve, non per suggerire che esista.

### Ritmo cromatico

`01 D · 02 D · 03 L · 04 L · 05 D · 06 L · 07 D · 08 L · 09 L · 10 D · 11 D · 12 L · 13 D`
Nessuna terna dello stesso colore. Dopo ogni slide astratta o commerciale ne
arriva una con prodotto, dato o interfaccia.

---

## 4. Dossier · struttura invariata, titolo cambiato

14 pagine core + 4 annessi, come la V8. Cambia il titolo, come chiede la §8.1:

> **Dossier tecnico preliminare per assessment e solution design**

Torna «Dossier tecnico» quando A1, A2 e A3 sono compilati. Non è una formula di
cortesia: un documento che non risponde su deployment, sizing e sicurezza non è
un dossier tecnico, è la sua struttura.

### Che cosa è cambiato dentro

| pagina | modifica |
|---|---|
| 01 cover | titolo preliminare · blocco «Emesso da» con denominazione, referente e data |
| 04 Connect | «causale» → **«causa associata»**, come impone la §2.4 |
| 06 Refyn | riquadro working con perimetro del primo rilascio, regole di accesso al pilot e data di rilascio. Nella client edition il riquadro esce: **nessuna data non approvata** |
| 08 architettura | la riga «verso le macchine» porta il placeholder nella working, «sola lettura» nella client |
| 11 energia | **«CO₂ calcolata o stimata»**, come impone la §2.4 |
| 14 servizi | orari, canali, tempi di risposta e aggiornamenti diventano placeholder. La citazione di MAPST 4.0 e MarEnergy rientra, **una volta sola**, nella formula esatta della §3.4 |
| A1 compatibilità | aggiunta la riga gateway e regole firewall · protocolli e versioni sono placeholder |
| A2 sizing | nella working i quattro valori da chiudere (CPU, RAM, storage, retention); nella client resta il metodo |
| A3 governo | nuova colonna **Valore**: nella working ogni riga ha il suo placeholder, nella client dice «solution design» |
| A4 dizionario KPI | nuova colonna **Owner** |

---

## 5. Regole editoriali applicate

### §2.4 · termini vietati

Ricerca su tutte e quattro le edizioni, testo visibile e accessibile: **zero
occorrenze** dei 27 pattern controllati, che includono i venti della §2.4, i
quattro sub-brand vietati della §3.1 e tre claim assoluti.

### §13.2 · forme obbligatorie

| regola | prima | dopo |
|---|---|---|
| «in sviluppo» una volta sola per documento | deck 5 · dossier 2 | **deck 1 · dossier 1** |
| «causa associata» presente | deck 2 · dossier 0 | deck 2 · **dossier 2** |
| «CO₂ calcolata o stimata» presente | deck 1 · dossier 0 | deck 1 · **dossier 1** |
| grafia del brand unica | `D.Factory` | `D.Factory`, unica forma in 39 occorrenze |

**Sulla regola «in sviluppo una volta» ho fatto una scelta che va saputa.** Nel
deck la dichiarazione resta sulla slide 08, dove i tre livelli vengono presentati
e il lettore si forma l'idea di che cosa esiste. Le altre quattro occorrenze —
slide 03, la ripetizione in piede alla 08, la slide 09 e la nota di A1 — sono
state tolte. Chi guardasse **solo** la slide 09 non troverebbe la dicitura: la
trova la riga «Attivazione attraverso un progetto pilota dedicato», che dice la
stessa cosa in forma commerciale. Se preferisci tenerla anche lì, è una riga.

---

## 6. Che cosa contiene la client edition di oggi

Con tutti i 220 placeholder in stato `OPEN`:

| documento | canvas | esclusi | perché |
|---|--:|---|---|
| Sales Deck | **16** | slide 13 CTA · slide 14 caso · appendice A3 pricing | contatto P0 aperto · caso non autorizzato · nessun importo approvato |
| Dossier | **18** | nessun canvas | i blocchi con placeholder hanno tutti una formulazione prudente che li sostituisce |

Il deck client-facing ha quindi **12 slide di corpo e 4 appendici**. La
numerazione è stata rifatta di conseguenza — `12 / 12` e `A1–A4` — perché un buco
nella numerazione si legge come un errore. La mappa di rinumerazione è esplicita
in `work_v9/edition.py` e vale solo per la client edition:

```
02–12 / 13   →   02–12 / 12
A4           →   A3
A5           →   A4
«assunzioni in appendice A5»  →  «appendice A4»
```

---

## 7. QA

| edizione | canvas | flag | placeholder |
|---|--:|--:|--:|
| Sales Deck working | 19 | **0** | 87 |
| Sales Deck client | 16 | **0** | **0** |
| Dossier working | 18 | **0** | 104 |
| Dossier client | 18 | **0** | **0** |

Nei due PDF client-facing la ricerca di `PH_[A-Z0-9_]+` **sul binario** restituisce
zero: non è solo il testo estratto a essere pulito, è il file.

Dettaglio in `DFactory_QA_Report_v9.md`.

---

## 8. Strumenti aggiunti

| file | che cosa fa |
|---|---|
| `work_v9/ph.py` | il registro come dato: 220 voci, fonte unica di verità |
| `work_v9/mk_register.py` | genera il registro in markdown dal dato |
| `work_v9/edition.py` | deriva working e client, rinumera, fa fallire il build se un placeholder resta |
| `work_v9/semantic9.py` | i 27 pattern vietati, le forme obbligatorie, il conteggio di «in sviluppo», la grafia del brand |
| `work_v9/qa.py` | aggiunta la popolazione `ph`: l'impalcatura working è metadato sul documento, non testo del documento, e viene contata a parte |
