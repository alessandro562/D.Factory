# D.Factory · Claim Register V9.3

10 claim tecnici. Nessuno nuovo rispetto alla V9.2: la revisione narrativa non ha aggiunto affermazioni tecniche, le ha tolte.

Due claim cambiano **formulazione**, e il cambio è di sostanza:

| claim | prima | dopo | perché |
|---|---|---|---|
| — | «Motore KPI» come componente dell'architettura | «Elaborazione KPI» come funzione | il §2.3 della review D2: non si dichiara un componente architetturale che non è confermato |
| `erp` | «API · dati selezionati · da definire» | «Interfacce applicative · da verificare sul perimetro» | il §2.4: la presenza di un'interfaccia applicativa è un claim di prodotto, e non è confermata |

Il build fallisce se un marcatore tecnico compare nei documenti senza un claim
che lo copra: `accept93.py` condizione 6.

| claim | stato | frase | marcatore | fonte |
|---|:--:|---|---|---|
| `read_only` | PRUDENTE | Acquisizione verso le macchine in sola lettura | `sola lettura` | piano V9.1 §6.1, opzione B raccomandata |
| `residenza` | PRUDENTE | Residenza e trattamento dei dati concordati con l’IT | `solution design` | piano V9.1 §6.2, copy prudente |
| `oee` | DIMOSTRATO | OEE come disponibilità × performance × qualità | `disponibilit` | formula scritta per esteso, ricostruibile |
| `costo_en` | DIMOSTRATO | Costo energetico del pezzo da consumo, prezzo e pezzi | `costo energetico` | catena aritmetica esplicita |
| `co2` | DIMOSTRATO CON RISERVA | CO₂ calcolata o stimata dal fattore dichiarato | `calcolata o stimata` | fattore illustrativo, fonte da confermare |
| `cumulativa` | AFFERMATO | Insight comprende Connect, Refyn comprende entrambi | `comprende` | architettura di prodotto dichiarata |
| `refyn` | AFFERMATO | Refyn, modulo avanzato in sviluppo, via pilot dedicato | `in sviluppo` | piano V9.1 §4.3, raccomandazione di breve periodo |
| `brownfield` | AFFERMATO | Si parte dall’impianto esistente | `gi&agrave; presenti` | metodo di acquisizione descritto |
| `erp` | AFFERMATO CON RISERVA | Interfacce applicative, da verificare sul perimetro | `da verificare sul perimetro|previa verifica` | la disponibilità di un’interfaccia applicativa non è confermata · §2.4 review D2 |
| `compat` | AFFERMATO | La compatibilità si verifica sull’impianto reale | `impianto reale` | metodo di audit descritto |

## Dove compaiono

| marcatore | deck client | dossier client |
|---|--:|--:|
| `sola lettura` | 1 | 1 |
| `solution design` | 1 | 7 |
| `disponibilit` | 1 | 4 |
| `costo energetico` | 2 | 3 |
| `calcolata o stimata` | 1 | 2 |
| `comprende` | 11 | 2 |
| `in sviluppo` | 1 | 1 |
| `gi&agrave; presenti` | 1 | 1 |
| `da verificare sul perimetro` | 0 | 1 |
| `previa verifica` | 0 | 1 |
| `impianto reale` | 3 | 2 |

## Formulazioni vietate dal §12

14 espressioni. Nessuna compare nei quattro documenti; il controllo è una condizione di build, non una raccomandazione.

- ~~Insights~~
- ~~causa automatica~~
- ~~causa rilevata automaticamente~~
- ~~qualsiasi protocollo~~
- ~~zero hardware~~
- ~~costo reale del pezzo~~
- ~~costo del pezzo~~
- ~~risparmio garantito~~
- ~~software ISO 50001~~
- ~~API disponibile~~
- ~~ERP nativo~~
- ~~cloud non necessario~~
- ~~dati sempre on-premise~~
- ~~Motore KPI~~
