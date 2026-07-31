# Mappatura id DOM → destinazione (revisione v2)

Prodotta **prima** di qualsiasi modifica, come richiesto dal master brief §11.
Stato di partenza: 35 slide (18 nucleo + 17 appendice). Tutte le modifiche sono targettate
per id DOM, mai per numero visualizzato.

## Deck core → `DFactory_SalesDeck.html` (14 slide)

| # | Slide target | id DOM di origine | Azione |
|---|---|---|---|
| 01 | Cover | `s01_cover` | Rivista: due righe nuove (cosa si vende, per chi) |
| 02 | Il quadro in una pagina | `s12b_sintesi` | **Spostata in apertura** da posizione 17; occhiello rimosso; "cosa ci distingue" riscritto |
| 03 | È per te se + cinque trigger | **nuova** (`s03_trigger`) | Sostituisce `s02_perche_ora` |
| 04 | Il problema | `s03_problema` | Quasi invariata + una riga dal gap riformulata |
| 05 | Cos'è, con la prima screenshot | `s05_soluzione` **+** `s08_platform` | Fusione: prodotto anticipato a pagina 5 |
| 06 | Cosa ottieni, per ruolo | `s06c_ruoli` | Invariata |
| 07 | La prova | `s26_prova` | Caso cliente e citazione in cima, churn riformulato |
| 08 | Perché noi | `s06_refyn` **+** `s25_differenziatori` **+** 2 righe da `s27_gruppo` | Fusione: solo capacità esistenti oggi |
| 09 | Come entra in casa tua | **nuova** (`s09c_integrazione`), da `s18_brownfield` + `s19_report` + `s20_attivazione` | IT, sovranità del dato, macchine miste, tempi, SLA |
| 10 | Le obiezioni | `s09b_obiezioni` | + quinta obiezione (Power BI / fai da te) |
| 11 | Come si paga e quanto | `s10b_modello` **+** `s22_pacchetti` | Fusione + ancoraggio di prezzo |
| 12 | Il ritorno | `s23_roi` | Due scenari di margine invece di uno |
| 13 | L'audit di linea | `s28_prossimi` | Tutti i `[confermare]` convertiti in token PH |
| 14 | Parliamone | `s29_cta` | + link di prenotazione, + rimando al dossier |

## Slide che escono dal deck core

| id DOM | Titolo attuale | Destinazione | Motivo |
|---|---|---|---|
| `s02_perche_ora` | Quattro forze convergono | **Rimossa** | §6.1: tre argomenti su quattro sono compliance, due forze coincidono, claim falsificabile dal lettore |
| `s04_gap` | Quanto ti costa non saperlo | **Rimossa**, una riga recuperata in slide 04 | §6.2: benchmark OEE 82-85% contestabile nel packaging multi-formato |
| `s22_pacchetti` | Parti da dove ti serve | **Fusa** in slide 11 | Ridondante con la struttura di prezzo |
| `s27_gruppo` | Tra cinque anni siamo ancora qui | **Compressa** in due righe dentro slide 08 | §6.6: argomento valido ma secondario, e il €145M spostava l'attenzione sul gruppo |
| `s06_refyn` | Il software ti dà i dati | **Fusa** in slide 08, non più slide-eroe | §6.4: il differenziale non può essere ciò che è "in via di definizione" |

## Dossier tecnico → `DFactory_DossierTecnico.html` (16 slide)

| # | id DOM | Ex | Azione |
|---|---|---|---|
| 01 | `s00_appendice` | A01 | Copertina riadattata a documento autonomo |
| 02 | `s06_architettura` | A02 | Invariata |
| 03 | `s07_super` | A03 | Invariata |
| 04 | `s09_superv` | A04 | Invariata |
| 05 | `s10_fermi` | A05 | Invariata |
| 06 | `s11_velocita` | A06 | Invariata |
| 07 | `s12_multi` | A07 | Invariata |
| 08 | `s13_oee` | A08 | Invariata |
| 09 | `s14_distrib` | A09 | Invariata |
| 10 | `s15_costo` | A10 | Invariata |
| 11 | `s16_stato` | A11 | Invariata |
| 12 | `s17_misura` | A12 | Invariata (la porta d'ingresso energia viene **portata anche** in core 05) |
| 13 | `s18_brownfield` | A13 | Invariata (contenuto **portato anche** in core 09) |
| 14 | `s19_report` | A14 | Invariata (contenuto **portato anche** in core 09) |
| 15 | `s20_attivazione` | A15 | Invariata (contenuto **portato anche** in core 09) |
| 16 | `s21_sensori` | A16 | Invariata |

## Fuori da entrambi i file

| id DOM | Titolo | Motivo |
|---|---|---|
| `s24_posizionamento` | Tutti monitorano. Nessuno con la nostra architettura packaging | §6.7: sei pallini pieni su sette, criteri scelti dal venditore, un criterio coincide con la propria definizione di sé. Resta materiale interno per situazioni competitive dichiarate |

## Nota sugli id

Gli id restano stabili anche quando la posizione cambia: `s07_super` è ancora l'id storico
della slide MAPST 4.0, `s26_prova` è alla posizione 07 e non 26. La numerazione visualizzata
è generata da `build.py` in base alla posizione, quindi non va mai usata per targettare.
