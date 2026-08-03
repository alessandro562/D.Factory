# D.Factory · Claim Register V9.2

Dieci claim tecnici. La regola è quella del §25: **se una frase tecnica
compare nei documenti e non è qui, il build fallisce.** Il controllo è in
`accept92.py`, condizione 6, e passa.

Gli stati:

- **DIMOSTRATO** — la frase è verificabile dal documento stesso, perché la
  formula o la catena aritmetica sono scritte per esteso.
- **DIMOSTRATO CON RISERVA** — il metodo è scritto, un parametro è dichiarato
  illustrativo.
- **PRUDENTE** — la formulazione è stata approvata come prudente, la verifica
  tecnica è aperta.
- **AFFERMATO** — è un'affermazione sul prodotto o sul metodo, non una misura.
- **AFFERMATO CON RISERVA** — affermazione condizionale, con la condizione scritta.


| # | claim | stato | marcatore | deck | dossier | fonte |
|--:|---|---|---|:--:|:--:|---|
| 1 | Acquisizione verso le macchine in sola lettura | **PRUDENTE** | `sola lettura` | 1 | 4 | piano V9.1 §6.1, opzione B raccomandata |
| 2 | Residenza e trattamento dei dati concordati con l’IT | **PRUDENTE** | `solution design` | 2 | 16 | piano V9.1 §6.2, copy prudente |
| 3 | OEE come disponibilità × performance × qualità | **DIMOSTRATO** | `disponibilit` | 1 | 3 | formula scritta per esteso, ricostruibile |
| 4 | Costo energetico del pezzo da consumo, prezzo e pezzi | **DIMOSTRATO** | `costo energetico` | 1 | 1 | catena aritmetica esplicita |
| 5 | CO₂ calcolata o stimata dal fattore dichiarato | **DIMOSTRATO CON RISERVA** | `calcolata o stimata` | 1 | 1 | fattore illustrativo, fonte da confermare |
| 6 | Insight comprende Connect, Refyn comprende entrambi | **AFFERMATO** | `comprende il precedente` | 2 | 2 | architettura di prodotto dichiarata |
| 7 | Refyn, modulo avanzato in sviluppo, via pilot dedicato | **AFFERMATO** | `in sviluppo` | 1 | 1 | piano V9.1 §4.3, raccomandazione di breve periodo |
| 8 | Si parte dall’impianto esistente | **AFFERMATO** | `impianto esistente` | 1 | — | metodo di acquisizione descritto |
| 9 | Integrazione con il gestionale previa verifica | **AFFERMATO CON RISERVA** | `previa verifica` | 1 | 1 | formulazione condizionale |
| 10 | La compatibilità si verifica sull’impianto reale | **AFFERMATO** | `impianto reale` | 1 | 1 | metodo di audit descritto |

---

## Le formulazioni approvate


### `read_only`

> La configurazione standard privilegia l’acquisizione in sola lettura. Eventuali scambi ulteriori vengono definiti nel solution design.

*Fonte:* piano V9.1 §6.1, opzione B raccomandata · *in breve:* sola lettura in configurazione standard


### `residenza`

> Il modello di deployment, la residenza e il trattamento dei dati vengono concordati con l’IT e formalizzati nel solution design.

*Fonte:* piano V9.1 §6.2, copy prudente · *in breve:* concordata con l’IT


### `proprieta`

> I dati operativi restano nella disponibilità del cliente. Diritti d’uso del software, modalità di accesso ed export a fine contratto sono definiti nell’accordo di licenza.

*Fonte:* piano V9.1 §6.3 — **non pubblicare finché non approvato legalmente** · *in breve:* working edition soltanto


### `energia`

> In questo scenario il valore principale nasce dalla capacità recuperabile. Il dato energetico completa la lettura e quantifica il consumo improduttivo dello stesso evento.

*Fonte:* piano V9.1 §5.4, copy raccomandato · *in breve:* la leva energia completa, non pareggia


### `refyn`

> Refyn è disponibile attraverso un progetto pilota dedicato, con quotazione sul perimetro.

*Fonte:* piano V9.1 §4.3, raccomandazione di breve periodo · *in breve:* pilot dedicato, nessun listino


---

## Il claim che non viene pubblicato

`proprieta` — proprietà dei dati e diritti di licenza. Il §25 è esplicito:
«proprietà dati: non pubblicare senza approvazione legale». La formulazione
esiste, è scritta qui sopra, e **non compare in nessuno dei quattro HTML**.
L'annesso A3 del dossier continua a dichiarare che cosa si decide e chi decide,
che è vero oggi e non richiede il legale.

`accept92.py` verifica che la frase non sia finita nel dossier: criterio
«proprietà dei dati non pubblicata», §26.

---

## Espressioni sorvegliate

Ogni marcatore di questa lista, se compare nei documenti, deve avere un claim.


- `sola lettura` — deck 1 · dossier 4
- `solution design` — deck 2 · dossier 16
- `costo energetico` — deck 1 · dossier 1
- `calcolata o stimata` — deck 1 · dossier 1
- `in sviluppo` — deck 1 · dossier 1
- `previa verifica` — deck 1 · dossier 1
- `impianto reale` — deck 1 · dossier 1
- `impianto esistente` — deck 1 · dossier 0

---

## Formulazioni vietate, e che cosa si usa al loro posto · §7

| non si usa | si usa | dove vale |
|---|---|---|
| causa rilevata automaticamente | **causa associata** | deck 03, 04, 06 · dossier 04, 05, 09 |
| costo reale del pezzo | **margine perso stimato**, **costo della perdita** | deck 04, 06 |
| risparmio garantito · valore certo | **capacità potenzialmente recuperabile**, **energia potenzialmente evitabile** | deck 11 |
| costo del pezzo (per il solo perimetro energia) | **costo energetico del pezzo** | deck 07 · dossier 11 |
| la differenza fra OEE macchina e linea è il polmone | **il calcolo di linea considera confini, blocking, starvation, buffer e regole di aggregazione** | dossier 10 |
| software certificato ISO 50001 | **supporta dati e processi coerenti con ISO 50001** | non pubblicato in V9.2 |
| qualsiasi marca e protocollo | **multi-vendor, con compatibilità verificata in audit** | dossier annesso A1 |
| integrazione con ERP | **integrazione con ERP o gestionale, previa verifica tecnica** | dossier 12 · deck A4 |
