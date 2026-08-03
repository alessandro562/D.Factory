# D.Factory · Registro degli asset V9.2

**Zero righe.** Nessun asset reale è stato consegnato. Il registro non è vuoto
per dimenticanza: è vuoto perché non è arrivato nessun file, e questo documento
serve a dirlo senza girarci intorno.

La cartella `assets_v9_2/` contiene questo file e nient'altro.

---

## 1. Il registro

Dieci colonne. Il §19.3 ne chiede sette; scadenza dell'autorizzazione e pagine
d'uso servono a chi dovrà rinnovare o ritirare un file, e costano niente adesso.

| file | fonte | data | prodotto | versione | autorizzazione | anonimizzazione | uso consentito | scadenza | pagine |
|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — |

**La regola che non si aggira:** `accept92.py`, condizione di build n. 5, fa
fallire il build se un file compare in un canvas e non ha una riga qui.
Oggi passa perché i canvas non contengono nessun `<image>` e nessun `<img>`:
ogni vista di prodotto è un SVG inline ricostruito.

---

## 2. Obiettivo del §19.2 · non raggiunto

| dove | richiesti | disponibili | esito |
|---|--:|--:|---|
| Sales Deck | 1 | 0 | **non raggiunto** |
| Dossier tecnico | 2 | 0 | **non raggiunto** |

Il §8.4 prevede esattamente questo caso — «asset reali mancanti → mantenere
ricostruzioni dichiarate» — ed è quello che i documenti fanno: ogni vista porta
la dicitura *vista ricostruita · dati illustrativi* nel piede della pagina, e la
cover del dossier lo dichiara una volta per tutte.

---

## 3. I sei candidati, in ordine di priorità · §19.1

| # | asset | token | etichetta obbligatoria §19.3 | dove andrebbe | stato |
|--:|---|---|---|---|---|
| 1 | Screenshot reale MAPST 4.0 | `PH_REAL_SCREENSHOT_MAPST` | *Interfaccia MAPST 4.0 · prodotto legacy* | deck 04 · dossier 04 | mancante |
| 2 | Screenshot reale MarEnergy | `PH_REAL_SCREENSHOT_MARENERGY` | *Interfaccia MarEnergy · prodotto legacy* | deck 05 · dossier 05 | mancante |
| 3 | Report reale anonimizzato | `PH_REAL_REPORT_EXPORT` | *Report reale anonimizzato* | dossier 12 | mancante |
| 4 | Schema di linea o foto di installazione | `PH_REAL_LINE_DIAGRAM` | *Schema di linea anonimizzato* | dossier 07 · deck 10 | mancante |
| 5 | Screenshot della nuova interfaccia | `PH_REAL_SCREENSHOT_NEW_UI` | *Interfaccia D.Factory* | deck 03 | mancante |
| 6 | Foto di sensore o contatore | `PH_REAL_SENSOR_PHOTO` | *Punto di misura · foto di campo* | dossier 07 | mancante |

Nella working edition ciascuno di questi token è già visibile come
`ASSET RICHIESTO`, sul canvas che lo aspetta.

---

## 4. Che cosa serve per registrare un file

Le due colonne che nessuno può compilare a memoria sono **autorizzazione** e
**anonimizzazione**.

- Uno screenshot di un prodotto legacy ha bisogno di sapere *di chi è
  l'impianto che si vede*: nomi di linea, codici prodotto e ordini sono dati del
  cliente anche quando l'interfaccia è nostra.
- Un report reale esce solo con l'anonimizzazione fatta **e verificata da
  qualcuno che l'ha guardata riga per riga**.
- Un logo cliente non entra senza autorizzazione scritta: il §18.3 lo vieta, e
  la V9.2 non ne contiene nessuno.

Il file `Logo-D-Factory-cce0b268-1.webp` è nel repository e **non entra nei
documenti**: non ha riga di registro, non ha autorizzazione documentata, e il
wordmark è già composto tipograficamente in Geist. Se serve il logo ufficiale,
va registrato qui prima di essere usato.

---

## 5. Effetto sul gate G5

G5 chiede **due** elementi approvati fra screenshot, report, schema, foto, fatto
aziendale verificato e caso cliente.

Siamo a **zero su due**.

G5 ha `BLOCKING_SCOPE = NONE`: non impedisce di presentare i documenti dal vivo,
dove chi parla è l'evidenza. Impedisce l'invio a freddo e il passaggio in
procurement, dove non c'è nessuno a rispondere alla domanda «questo l'avete
fatto davvero?».
