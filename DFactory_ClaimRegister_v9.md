# D.Factory · Registro dei claim V9

Ogni affermazione che i due documenti fanno sul prodotto, sul metodo o
sull'economia, con la prova che oggi la sostiene. Serve a una cosa sola: sapere
quali frasi reggono a una domanda e quali no.

**14 claim censiti.** Nessuno è stato rimosso per prudenza: sono tutti nel
documento, e quelli senza prova sono formulati in modo da non promettere più di
quanto si possa dimostrare.

## Scala usata

| stato | significato |
|---|---|
| `DIMOSTRATO` | il documento contiene la prova |
| `DIMOSTRATO CON RISERVA` | la prova c’è, un parametro no |
| `DIMOSTRATO IN RICOSTRUZIONE` | mostrato in una vista dichiarata ricostruita |
| `ILLUSTRATIVO` | dichiarato come scenario, non come risultato |
| `AFFERMATO` | dichiarato senza prova allegata |
| `AFFERMATO CON RISERVA` | dichiarato in forma condizionale |
| `DA VERIFICARE` | nessuno ha ancora confermato che sia vero |

`DA VERIFICARE` non vuol dire falso: vuol dire che la frase è nel documento e
nessuno l'ha ancora confermata. Sono le due righe più pericolose del registro,
perché sembrano tecniche e nessuno le mette in dubbio finché non arriva una due
diligence.

---

## Il registro

| # | Claim | Dove | Tipo | Che cosa lo sostiene oggi | Stato | Che cosa serve |
|--:|---|---|---|---|---|---|
| 1 | Produzione ed energia si leggono sullo stesso asse dei tempi | deck 05 · 07 · 10 · dossier 11 | funzionale | ricostruzione grafica coerente con il metodo dichiarato | `DIMOSTRATO IN RICOSTRUZIONE` | uno screenshot reale della vista con le due tracce · S1 |
| 2 | Si parte dall’impianto esistente, senza sostituire le macchine | deck 10 · dossier 02 · 07 | metodologico | descrizione del metodo di acquisizione | `AFFERMATO` | un caso reale con l’elenco di che cosa è stato aggiunto · A9 |
| 3 | Verso le macchine il flusso è in sola lettura | dossier 08 · A1 · deck A4 | tecnico | nessuna: è la configurazione descritta, non una regola verificata | `DA VERIFICARE` | conferma tecnica se sia regola assoluta o standard previsto · T11 |
| 4 | La compatibilità si verifica sull’impianto reale | dossier A1 · deck A4 | metodologico | descrizione del metodo di audit | `AFFERMATO` | nulla: è una descrizione di processo, non una prestazione |
| 5 | L’OEE si calcola come disponibilità × performance × qualità | deck 07 · dossier 10 · A4 | metodologico | formula standard, scritta per esteso e ricostruibile | `DIMOSTRATO` | nulla: la formula è verificabile sul documento |
| 6 | Il costo energetico del pezzo si ottiene da consumo, prezzo e pezzi | deck 07 · dossier 11 · A4 | metodologico | catena aritmetica esplicita e ricostruibile a mano | `DIMOSTRATO` | validazione dei parametri di partenza · V1 |
| 7 | CO₂ calcolata o stimata dal fattore di emissione dichiarato | deck 07 · dossier 11 | metodologico | metodo dichiarato, fattore dichiarato illustrativo | `DIMOSTRATO CON RISERVA` | fonte del fattore di emissione del fornitore · T-fonte |
| 8 | Una causa non chiusa costa 309.120 € all’anno | deck 11 · 12 | economico | scenario illustrativo con nove parametri dichiarati in A5 | `ILLUSTRATIVO` | validazione di plausibilità dei nove parametri · V1 |
| 9 | Insight comprende Connect; Refyn comprende entrambi | deck 08 · 09 · A1 · dossier 03 | architetturale | architettura di prodotto dichiarata | `AFFERMATO` | perimetro funzionale firmato per ciascun livello · PH_CONNECT_EXACT_SCOPE, PH_INSIGHT_EXACT_SCOPE |
| 10 | Refyn è un modulo avanzato in sviluppo | deck 08 · dossier 06 | stato di prodotto | dichiarazione interna | `AFFERMATO` | perimetro del primo rilascio · PH_REFYN_MVP_SCOPE |
| 11 | Il pilot si chiude con quattro deliverable e criteri di uscita dichiarati | deck 12 · dossier 13 | metodologico | metodo di delivery descritto | `AFFERMATO` | durata, partecipanti e condizioni economiche · C8 |
| 12 | Integrazione con il gestionale possibile previa verifica del punto di innesto | deck A4 · dossier 08 · 12 | tecnico | formulazione condizionale, nessun sistema nominato | `AFFERMATO CON RISERVA` | modalità supportate e un caso di riferimento · T10, PH_SAP_INTEGRATION_PROOF |
| 13 | Il dato resta nell’ambiente di deployment concordato con l’IT del cliente | deck A4 · dossier 02 · 08 · A3 | contrattuale | nessuna: dipende dal modello di deployment, non ancora chiuso | `DA VERIFICARE` | modello di deployment e proprietà del dato · T1, T7 |
| 14 | I servizi specialistici sono attivabili su tutti e tre i livelli | deck 08 · A2 · dossier 03 · 14 | commerciale | architettura dell’offerta dichiarata | `AFFERMATO` | che cosa è compreso e che cosa è opzionale · C6 |

---

## Riepilogo

| stato | claim |
|---|--:|
| `DIMOSTRATO` | 2 |
| `DIMOSTRATO CON RISERVA` | 1 |
| `DIMOSTRATO IN RICOSTRUZIONE` | 1 |
| `ILLUSTRATIVO` | 1 |
| `AFFERMATO` | 6 |
| `AFFERMATO CON RISERVA` | 1 |
| `DA VERIFICARE` | 2 |

**Due claim sono `DA VERIFICARE`** e sono entrambi tecnici: la sola lettura verso
le macchine e la residenza del dato. Costano una risposta ciascuno e sono già in
`DFactory_OpenInputs_v9.md` come T11 e T1/T7.

**Nessun claim aziendale è nel registro**, perché nel documento non ce n'è
nessuno: anni, clienti, linee, gruppo e referenze non compaiono. Quando i
placeholder della §5.2 verranno chiusi, ogni numero che entra va aggiunto qui con
la sua fonte prima di comparire in una slide.
