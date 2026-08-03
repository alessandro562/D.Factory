# D.Factory · Registro degli asset V9.1

Dieci colonne, come chiede il §7.4. **Zero righe**: nessun asset reale è stato
consegnato, e il build fallisce se un file compare in un canvas senza essere qui.

---

## 1. Il registro

| file | fonte | data | prodotto | versione | autorizzazione | anonimizzazione | uso consentito | scadenza | pagine |
|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — |

## 2. Obiettivo minimo · §7.1 · ne bastano due

| # | Asset | Placeholder | Etichetta obbligatoria §7.3 | Stato |
|--:|---|---|---|---|
| 1 | screenshot MAPST 4.0 o base software operativa | `PH_REAL_SCREENSHOT_MAPST` | *Interfaccia MAPST 4.0 · prodotto legacy* | mancante |
| 2 | screenshot MarEnergy | `PH_REAL_SCREENSHOT_MARENERGY` | *Interfaccia MarEnergy · prodotto legacy* | mancante |
| 3 | report reale | `PH_REAL_REPORT_EXPORT` | *Report reale anonimizzato* | mancante |
| 4 | fotografia o schema reale di linea | `PH_REAL_LINE_DIAGRAM` | *Schema di linea anonimizzato* | mancante |

**Zero su quattro.** Ne bastano due per il primo rilascio.

## 3. Dove vanno · §7.2

### Sales Deck · un solo asset reale

| candidato | slide | che cosa sostituisce |
|---|---|---|
| screenshot nuova interfaccia | 03 · categoria | la vista ricostruita con le tre annotazioni |
| foto di installazione | 10 · perché D.Factory | nulla: si aggiunge come terza prova |
| qualunque | appendice | nessuna sostituzione |

Uno solo. Il §7.2 è esplicito, e ha ragione: un deck con un asset vero e dodici
ricostruzioni dichiarate è credibile; uno con tredici asset misti è confuso.

### Dossier · tre inserimenti

| candidato | pagina | che cosa sostituisce |
|---|---|---|
| screenshot reale | 04 Connect o 05 Insight | la vista ricostruita |
| report reale | 12 Output | la tabella degli output |
| schema reale | 07 Sorgenti o 08 Architettura | lo schema di linea tipo o lo schema logico |

## 4. La regola che non si aggira

Il §7.3 impone un'etichetta a ogni asset legacy. Non è una didascalia: è la
differenza fra mostrare una capability esistente e lasciar credere che sia
l'interfaccia del prodotto nuovo.

Le due colonne che non si compilano a memoria sono **autorizzazione** e
**anonimizzazione**. Uno schema di linea o un report di un cliente reale escono
solo con l'anonimizzazione fatta e verificata da qualcuno che l'ha guardata.

## 5. Effetto sul gate G5

G5 chiede due elementi approvati fra screenshot, report, schema, foto, fatto
aziendale verificato e caso cliente. Siamo a **zero**.

G5 **non blocca l'uso dal vivo** del deck: blocca l'invio a freddo e il passaggio
in procurement. È l'unico dei cinque gate con scope `NONE`.
