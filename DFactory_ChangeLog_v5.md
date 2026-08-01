# D.Factory · Changelog v5

I file v4 non sono stati toccati. `DFactory_SalesDeck_v4.html` e
`DFactory_DossierTecnico_v4.html` restano invariati.

| Documento | v4 | v5 |
|---|---|---|
| Sales deck | 10 slide + 3 appendici | **11 slide + 4 appendici** |
| Dossier tecnico | 23 pagine, quattro sezioni | **31 pagine, cinque sezioni** |

---

## 0. La modifica che governa tutte le altre

Il v4 aveva due livelli di prodotto (Connect, Insights) e trattava Refyn come *servizi sul
dato*, mentre `MAPST 4.0` era descritta come la piattaforma su cui il sistema è costruito.

Il v5 riscrive l'architettura commerciale:

- **Tre moduli cumulativi.** Connect, Insight, Refyn. Insight include Connect; Refyn include
  entrambi. Ogni livello contiene sia produzione sia energia. La distinzione non è per tipo
  di dato ma per livello decisionale: cosa sta succedendo, perché e quanto pesa, cosa
  conviene fare.
- **I servizi diventano un livello orizzontale**, attivabile su tutti e tre. Non sono Refyn.
- **MAPST 4.0 e MarEnergy diventano prodotti legacy**, attivi per l'installato, base da cui
  evolvono le capability nuove. Escono dal corpo del deck.
- **Ogni funzione dichiara due stati**: la maturità della capability e quella del packaging.
  Non coincidono, e confonderle era il difetto principale del v4.

## 1. Sales deck · crosswalk

| v4 | v5 | Che cosa è successo |
|---|---|---|
| `s01_promessa` | `s01_promessa` | Invariata |
| `s02_punto_cieco` | `s02_punto_cieco` | Il rail dichiara "andamento illustrativo, non un caso reale" |
| `s03_come_funziona` | `s03_come_funziona` | **Claim riformulato.** "Un solo modello dati" era un claim da validare: diventa "produzione ed energia nello stesso contesto operativo". Le sorgenti distinguono produzione ed energia. La rassicurazione on-premise diventa rimando al solution design |
| `s04_prodotto` | `s04_prodotto` | Etichetta "vista illustrativa del nuovo packaging" |
| `s05_decisioni` | `s05_decisioni` | Invariata |
| `s06_perche` | `s06_differenziatore` | **Marcata.** La logica buffer-aware non è disponibile: l'occhiello porta "Refyn · in sviluppo" in giallo. Nel v4 sembrava una funzione standard |
| `s07_ipotesi_misure` | `s07_ipotesi_misure` | Invariata |
| — | **`s08_architettura`** | **Nuova.** Scala a tre gradini cumulativi, con lo stato di ciascuno e le due righe che tengono insieme l'architettura: produzione ed energia in ogni livello, servizi su ogni livello |
| `s08_valore` | `s09_valore` | Rinumerata |
| `s09_percorso` | `s10_percorso` | Le descrizioni dei passi portano ora lo stato del modulo: "Connect e Insight, in pilot", "Refyn su richiesta" |
| `s10_cta` | `s11_cta` | **Riscritta.** Da "Fissiamo l'audit della prima linea" a "Condividiamo il perimetro della prima linea": la CTA non è contrattuale finché durata, costo e partecipanti dell'audit non sono definiti |
| `a01_offerta` | `a01_offerta` | **Riscritta.** Da tre blocchi verticali a matrice tre colonne per domanda, produzione, energia, inclusione e stato, più la riga orizzontale dei dodici servizi |
| `a02_faq` | `a02_faq` | **Estesa da 4 a 7 obiezioni.** Aggiunte: rapporto con il legacy, stato pilot dei moduli, proprietà dei dati, sensoristica. Formato a matrice per rientrare nel budget |
| `a03_ipotesi` | `a03_ipotesi` | Invariata |
| — | **`a04_legacy`** | **Nuova.** Continuità del legacy, migrazione volontaria, e l'elenco esplicito di quello che non facciamo: nessuna dismissione forzata, nessuna scadenza, nessun aumento automatico |

## 2. Dossier · crosswalk

Da quattro sezioni numeriche a cinque sezioni lettera.

| v4 | v5 | Che cosa è successo |
|---|---|---|
| `d02_architettura_prodotto` | **02** `d02_architettura_commerciale` | **Riscritta.** Sette righe: brand, tre moduli, servizi, due legacy. Ogni riga con il suo stato |
| — | **03** `d03_provenienza` | **Nuova.** Da dove vengono le capability: MAPST 4.0 e MarEnergy confluiscono nel packaging nuovo, Refyn è net-new. Con la tabella che spiega come si legge il doppio stato |
| `d03_architettura_tecnica` | **04** | Claim riformulato: "contesto operativo unico" |
| `d04_acquisizione` | **05** | Invariata |
| `d05_capability` | **06** `d06_capability` | **Riscritta.** Sei colonne: funzione, Connect, Insight, Refyn, provenienza, stato. Legenda a cinque stati nella fascia |
| `d06`–`d12` | **07**–**13** | Rinumerate. `d08` **riscritta**: teneva la logica polmone che ora sta a pagina 17, resta il ranking delle cause |
| — | **14** `d14_correlazione` | **Nuova.** L'analisi congiunta produzione–energia, componente distintiva, con lo stato di ciascuna capability |
| — | **15** `d15_opportunity` | **Nuova.** Opportunity Prioritization: nove criteri di pesatura, output ordinato, badge "rappresentazione di concetto, la funzione non è implementata" |
| — | **16** `d16_action_benefit` | **Nuova.** Action Management e Benefit Tracking, campi previsti per entrambi |
| parte di `d07_oee_fermi` | **17** `d17_oee_avanzato` | **Spostata e marcata.** La logica buffer-aware esce dalle funzioni disponibili ed entra in Refyn, con badge "in development, non disponibile oggi" |
| — | **18** `d18_roadmap` | **Nuova.** Roadmap controllata: tre funzioni `roadmap` con la condizione per valutarle, cinque `not offered` con la ragione |
| `d13`–`d18` | **19**–**24** | Rinumerate |
| — | **25** `d25_servizi` | **Nuova.** Catalogo con deliverable, frequenza e modello economico |
| `d19`–`d22` | **26**–**29** | Rinumerate |
| — | **30** `d30_migrazione` | **Nuova.** Cinque passi della migrazione volontaria, ciascuno con stato, più l'elenco di quello che non facciamo |
| `d23_checklist` | **31** | Rinumerata |

## 3. Claim rimossi

| Claim v4 | Perché |
|---|---|
| "Un solo modello dati" — titolo di slide 03, diagramma, `<title>` e `<desc>` degli SVG | Da validare tecnicamente. Sopravviveva nei testi accessibili, invisibili ma parte del documento |
| "17 stati PackML nativi" | Ora "stati PackML dove la macchina li espone · da verificare per modello" |
| "On-premise · PC industriale Linux del cliente" come fatto | Ora "assetto previsto, da confermare in solution design"; il sistema operativo è "da confermare" |
| "Nessun flusso verso internet dalla rete di linea" come proprietà | Ora "nel perimetro concordato con il tuo IT non è previsto traffico verso internet" |
| "Aggiornamento 5 s" come valore fisso | Ora "aggiornamento configurato" |
| "Il dato resta qui" | Ora "storico sul server del progetto"; la policy si scrive in contratto |
| Buffer-aware fra le capability disponibili | Spostato in Refyn, marcato in development |
| Refyn = servizi sul dato | Refyn è il terzo modulo |
| `Insights` | Grafia errata |
| `MAPST 4.0` come piattaforma corrente | Prodotto legacy |

## 4. Claim aggiunti

| Claim | Autorizzazione |
|---|---|
| Connect, Insight e Refyn sono cumulativi | Backlog V5 §1.2 |
| Ogni livello contiene produzione ed energia | §1.2 |
| Connect e Insight sono in pilot release | §3.1, §3.2 |
| Refyn è in development, non generalmente disponibile | §3.3 |
| I servizi sono attivabili su tutti i moduli | §1.7 |
| MAPST 4.0 e MarEnergy restano attivi per l'installato | §1.3 |
| La migrazione è volontaria, senza dismissione forzata | §1.3, §9.8 |
| Le capability nuove evolvono dal legacy | §6.2, formula da validare |
| Operational Performance Index, non Operator | §3.3.E |
| Otto funzioni dichiarate `not offered` con la ragione | §3.3, §10.3 |

## 5. Decisioni ancora aperte

Le quattordici bloccanti P0 del backlog restano aperte. Le tre che pesano di più sui
documenti appena consegnati:

1. **Perimetro esatto di Connect e Insight.** L'appendice A1 e la pagina 06 descrivono una
   proposta ragionata, non una decisione. Fino all'approvazione sono materiale di
   discussione interna, non un listino da mostrare.
2. **Refyn MVP.** Le pagine 15, 16 e 17 mostrano quattro oggetti. Se il primo rilascio ne
   contiene due, quelle pagine promettono più di quanto verrà consegnato.
3. **Durata, costo e partecipanti dell'audit.** Per questo la CTA è stata riscritta come non
   contrattuale. Quando i tre dati arrivano, slide 11 torna a essere una proposta.

L'elenco completo, con owner e priorità, è in `DFactory_OpenInputs_v5.md`.

## 6. Nota di processo

Il backlog §15 prevede uno stop dopo la Fase 2, con le tre pagine campione da approvare
prima di propagare. Le tre pagine sono state costruite e verificate per prime — slide
architettura, dossier 02 e dossier 06 — ma **non c'è stata approvazione esplicita** prima
della Fase 3: la richiesta era di consegnare i due HTML completi. La direzione è quindi da
considerarsi ancora da validare, e le tre pagine campione restano il punto in cui
intervenire per primo se non convince.
