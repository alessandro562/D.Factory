# D.Factory · QA Report V9.2

Quattro file, 71 canvas, **zero flag**.

| file | canvas | flag | placeholder visibili |
|---|--:|--:|--:|
| `DFactory_SalesDeck_v9_2_client.html` | 16 | 0 | 0 |
| `DFactory_SalesDeck_v9_2_working.html` | 19 | 0 | 46 |
| `DFactory_DossierTecnico_v9_2_client.html` | 18 | 0 | 0 |
| `DFactory_DossierTecnico_v9_2_working.html` | 18 | 0 | 69 |

I 115 placeholder della working edition sono voluti: è la sua funzione. I zero
della client edition sono la condizione di build n. 1.

---

## 1. Il controllo che è stato aggiunto, e perché

La V9.1 misurava la dimensione effettiva del testo dentro un SVG moltiplicando
per il rapporto **fra le sole larghezze**:

```js
if (vb && vb.width) fs = fs * (svg.getBoundingClientRect().width / vb.width);
```

È sbagliato. Con `preserveAspectRatio` al valore di default la scala è la
**minore** delle due, e la slide 05 del deck aveva
`width="1280" height="440" viewBox="0 0 1280 480"`: scala reale 0,917, testo a
12,5 px renderizzato a **11,5 px**, e il grafico rientrato di 53 px per lato
rispetto al margine di tutte le altre slide. Il controllo diceva 12,5 e non
vedeva niente.

```js
if (vb && vb.width && vb.height) {
  const r = svg.getBoundingClientRect();
  fs = fs * Math.min(r.width / vb.width, r.height / vb.height);
}
```

Con la formula corretta sono emersi due SVG con viewport e viewBox
disallineati — `v05_energia` e `a1_matrice` — entrambi corretti. Sono le
«due geometrie sbagliate» della tabella §4 dell'audit.

---

## 2. §22.1 · visuale

| controllo | esito | come è misurato |
|---|---|---|
| zero overflow | ✔ 71/71 | ogni blocco contro il rettangolo del canvas, nel DOM |
| zero clipping DOM | ✔ 71/71 | stesso controllo, sui figli |
| zero clipping SVG | ✔ 71/71 | `getBBox()` contro `viewBox`, tolleranza 1 px |
| zero elementi fuori viewBox | ✔ 71/71 | stesso controllo — è la condizione di build n. 7 |
| zero collisioni | ✔ 71/71 | intersezione a coppie fra blocchi fratelli, `.rail` e `.ft` inclusi |
| zero linee sospese | ✔ | verifica visiva sui render singoli: ogni connettore parte e arriva su un blocco |
| zero box vuoti | ✔ | nessun contenitore con bordo e contenuto nullo |
| leggibile a 640×360 | ✔ | provino piccolo generato per tutti e quattro i file |
| note ≥ 11,5 px | ✔ | minimo effettivo 12,0 px, dopo la correzione della scala |
| giallo solo funzionale | ✔ | solo su evento di fermo, perdita, priorità |

### Dimensioni minime effettive

| documento | copy | metadati | diagrammi | UI di prodotto |
|---|--:|--:|--:|--:|
| Sales Deck | 18,0 px | 12,5 px | — | 12,0 px |
| Dossier | 14,0 px | 13,0 px | 13,0 px | 12,5 px |

Soglie: deck copy ≥ 18 · dossier copy ≥ 14 · metadati ≥ 12,4 · diagrammi ≥ 13 ·
UI ≥ 12. Il testo dentro una vista di prodotto è contenuto della schermata, non
messaggio della slide: uno screenshot vero porta le sue etichette e nessuno le
conta come copy.

---

## 3. §14.4 · leggibilità del dossier

Tetto: **130 parole**, escluse UI, metadati e impalcatura.

| pagina | V9.1 | V9.2 | |
|---|--:|--:|---|
| `p02_overview` | 132 | **105** | «cosa non presuppone» in tre voci, l'elenco del solution design resta solo su P08 |
| `p08_architettura` | 132 | **121** | i due blocchi passano da frasi a voci brevi |
| `pa3_governo` | 134 | **125** | dodici ambiti condensati in otto righe |
| `p11_energia` | 130 | **130** | al limite, dentro: nessun intervento |
| media dossier | 93 | **92** | |

Nessuna pagina sopra 130. Le tre che sforavano sono rientrate senza perdere
contenuto: la condensazione dell'annesso A3 copre dodici ambiti in otto righe.

### Righe delle tabelle principali

| pagina | righe | tetto |
|---|--:|--:|
| `p07_sorgenti` | 4 | 6 |
| `p12_output` | 6 | 6 |
| `p14_servizi` | 6 | 6 |
| `pa1_compatibilita` | 8 | 8 (§16) |
| `pa2_sizing` | 3 | 3 (§16) |
| `pa3_governo` | 8 | 8 (§16) |
| `pa4_kpi` | 6 | 8 (§16) |

> **Conflitto registrato.** Il §14.4 fissa «max 6 righe tabella principale», il
> §16 chiede otto campi in A1, otto ambiti in A3 e ammette otto righe in A4.
> Risoluzione: il tetto di sei vale per le **pagine core**, che lo rispettano
> tutte; gli annessi seguono il tetto del §16. Un annesso è una tabella per
> definizione — il §14.2 lo chiama template D — e comprimerlo a sei righe
> avrebbe significato perdere ambiti.

---

## 4. §22.2 · contenuto

| controllo | deck client | dossier client |
|---|---|---|
| placeholder | **0** | **0** |
| note interne | nessuna | nessuna |
| termini vietati | nessuno | nessuno |
| «in sviluppo» | 1 · slide 08 | 1 · pagina 06 |
| «Insight» al singolare | sempre | sempre |
| «causa associata» | 3 | 2 |
| «costo energetico» | 2 | 2 |
| «CO₂ calcolata o stimata» | 1 | 1 |
| grafie del brand | solo `D.Factory` · 19 | solo `D.Factory` · 20 |
| MAPST 4.0 / MarEnergy | **0** (§5.4) | 1 · pagina 14 |
| apostrofi diritti, `e'`, `gia'`, `perche'` | nessuno | nessuno |

Ventisette pattern vietati dal filtro semantico, incluso `\bAI\b` con
distinzione fra maiuscole e minuscole: nessuna occorrenza in nessuno dei
quattro file.

---

## 5. §22.3 · commerciale

| controllo | esito |
|---|---|
| CTA sempre presente | ✔ `v13_cta` in entrambe le edizioni |
| quattro blocchi della CTA | ✔ chi coinvolgere · cosa preparare · cosa restituiamo · azione richiesta |
| contatto o warning globale | ⚠ **warning globale**: G1 aperto, la CTA non porta il referente |
| servizi coerenti | ✔ nove nell'appendice A2 del deck, sei nella pagina 14 del dossier, stessa tassonomia |
| matrice coerente | ✔ otto capacità, cinque valori ammessi, «Base» eliminato |
| pricing solo se approvato | ✔ `a3_pricing` esclusa dalla client edition, G2 aperto |
| business case solo con G3 | ✔ esclusi 309.120 €, 154.560 €, 810 € e l'appendice A5 |

**Il warning globale è la condizione di consegna, non un difetto:** il §8.4
prevede che senza contatto approvato la client edition non sia mandabile. Il
deck si presenta dal vivo. Non si invia.

---

## 6. §22.4 · tecnico

| controllo | esito |
|---|---|
| dossier preliminare con G4 aperto | ✔ «Dossier tecnico preliminare per assessment e solution design» |
| read-only con stato corretto | ✔ formulazione approvata del §7.8, stato *COPY APPROVED · TECHNICAL VALIDATION OPEN* |
| residenza dati prudente | ✔ formulazione del §7.9, pagina 08 |
| proprietà dei dati non pubblicata | ✔ resta nel Claim Register, §25 |
| annessi coerenti | ✔ A1 esiti · A2 metodo in client, fasce in working · A3 raccolta requisiti · A4 dizionario |

---

## 7. §22.5 · asset

| controllo | esito |
|---|---|
| ogni asset registrato | ✔ **zero asset usati, zero righe di registro** |
| ogni screenshot etichettato | n/a |
| nessun asset non autorizzato | ✔ incluso il logo presente nel repository, che non entra |

Obiettivo del §19.2 — un asset reale nel deck, due nel dossier — **non
raggiunto**: zero su tre. Il §8.4 ammette il fallback («mantenere ricostruzioni
dichiarate») e i documenti lo applicano, dichiarando la ricostruzione nel piede
di ogni canvas che ne contiene una.

---

## 8. §25 · le dieci condizioni di build

`accept92.py` esce con codice 1 se una cade. Esce **0**.

| # | condizione | esito |
|--:|---|---|
| 1 | placeholder residuo nella client edition | ✔ zero, in entrambi i documenti |
| 2 | CTA mancante | ✔ presente, con i quattro blocchi |
| 3 | business case annualizzato con G3 aperto | ✔ zero, **in cifre e in lettere** |
| 4 | «Dossier tecnico» senza «preliminare» con G4 aperto | ✔ titolo coerente |
| 5 | asset non registrato | ✔ zero asset, zero righe |
| 6 | claim fuori dal Claim Register | ✔ dieci claim, otto marcatori sorvegliati |
| 7 | elementi SVG fuori dal viewBox | ✔ zero su 71 canvas |
| 8 | «in sviluppo» più di una volta per documento | ✔ una per documento, in tutte e quattro le edizioni |
| 9 | testo interno in una nota client | ✔ nessuno |
| 10 | canvas con clipping o overflow | ✔ zero su 71 canvas |

La 3 è la condizione che la V9.1 superava su un documento non conforme, perché
cercava solo `309.120` e non `trecentonovemilacentoventi`. Adesso cerca
entrambe le forme, e prima di correggere la slide 11 **falliva** — che è la
prova che il controllo funziona.

La 9 ha trovato un caso reale in corso d'opera: il piede dell'annesso A3 diceva
«per la raccolta dei requisiti, **finché G4 è aperto**». Il nome di un gate
interno in un documento destinato al cliente. Rimosso.

---

## 9. §26 · criterio di completamento al 90%

### Sales Deck — 7/7

✔ narrativa completa, 13 slide core · ✔ CTA presente · ✔ quattro appendici
· ✔ fallback sicuri sul pricing · ✔ zero placeholder client · ✔ offerta a tre
livelli comprensibile · ✔ valore metodologicamente corretto

### Dossier — 7/7

✔ 14 pagine core + 4 annessi · ✔ annessi strutturati · ✔ gap tecnici espliciti
· ✔ claim tecnici prudenti · ✔ proprietà dei dati non pubblicata · ✔ zero
placeholder client · ✔ pronto per assessment e solution design

---

## 10. Livello raggiunto · dichiarazione esplicita richiesta dal §25

| livello | stato | perché |
|---|:--:|---|
| **90% ready** | **✔ raggiunto** | struttura, narrativa, prodotto, offerta, annessi, fallback e QA sono chiusi |
| commercial final | ✗ | G1 e G2 aperti: manca il referente, mancano gli importi |
| IT-ready | ✗ | G4 aperto: il dossier è preliminare per assessment e solution design |

**La client edition non è dichiarata «finale».** Il §25 lo vieta con G1 o G2
aperti, e sono aperti entrambi.

---

## 11. Che cosa questo report non può dire

Per onestà, e perché è la stessa lista da quattro versioni.

- **Nessuna vista di prodotto è uno screenshot.** Sono ricostruzioni SVG,
  dichiarate pagina per pagina. Il QA verifica che siano leggibili e coerenti;
  non può verificare che assomiglino al prodotto, perché non ha il prodotto.
- **Lo scenario illustrativo è internamente coerente, non validato.** Ogni
  numero discende dagli altri per aritmetica verificabile a mano — è la ragione
  per cui l'incoerenza dei «tre turni al giorno» in appendice A5 è stata
  trovata. Coerente non vuol dire vero.
- **Gli annessi A1, A2 e A3 descrivono un metodo, non dei valori.** Sono
  strutturati e pronti da compilare. Non sono compilati, e finché G4 è aperto
  non possono esserlo.
- **Il deck non è pronto per essere inviato.** È pronto per essere presentato.
  La differenza è una riga di contatto, e non è una riga che si possa inventare.
