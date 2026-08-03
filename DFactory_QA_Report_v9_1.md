# D.Factory · QA V9.1

Quattro edizioni, **72 canvas, zero flag**, e un difetto della V9 trovato e
corretto.

---

## 1. Il difetto della V9 che avevo consegnato

Il blocco contatto della CTA era **tagliato dal viewBox dell'SVG**: l'elemento
era alto 400 unità e il contatto stava a y=428. Nel render della V9 si vede il
testo mozzato a metà e l'email non c'è.

Il QA non lo segnalava perché **il clipping dentro un `<svg>` non è un overflow
del DOM**: il browser lo nasconde e nessuna misura sui rettangoli di layout se ne
accorge.

Ho aggiunto il controllo che mancava — `getBBox()` contro il `viewBox`, per ogni
SVG di ogni canvas — e riverificato la V9 con lo strumento nuovo:

```
deck9_working  v13_cta  CLIP×1
      ! contenuto tagliato dal viewBox z2t z2d dx=0 dy=33 "Contatto"
```

Un canvas su 71. La CTA della V9.1 è stata rifatta da zero con l'altezza giusta,
e il controllo è ora parte della batteria.

---

## 2. Il tabellone

| edizione | canvas | flag | placeholder | copy media |
|---|--:|--:|--:|--:|
| Sales Deck · working | 19 | **0** | 87 | 11 |
| Sales Deck · client | 17 | **0** | **0** | 12 |
| Dossier · working | 18 | **0** | 104 | 88 |
| Dossier · client | 18 | **0** | **0** | 93 |

Il deck client passa da 16 canvas della V9 a **17**: la CTA è rientrata (§9.13).

---

## 3. Le quattro tabelle

### Sales Deck · working

```
id                          copy vista  ph   cont   meta   diag  vista   vis%  flags
v01_cover                     18    50   3     19     19      —   12.5   58.3
v02_tensione                  21    40   0     18   12.5      —   12.5   58.9
v03_categoria                 24    62   1     18   12.5      —     13   59.4
v04_evento_prodotto           15    37   1     44   12.5      —   12.5   67.8
v05_energia                   16    33   2     18   12.5      —   12.5   61.1
v06_priorita                   9    74   0     44   12.5      —     13   65.3
v07_ampiezza                   7    82   0     44   12.5      —   12.5   62.8
v08_offerta                   17    78   2     18   12.5      —     13   62.8
v09_scelta                     8    84   3     44   12.5      —     13   66.4
v10_perche                     5   100   3     44   12.5      —   12.5   61.1
v11_valore                     9    24   4     44   12.5      —     13   61.1
v12_pilot                      8    83   5     44   12.5      —     13   66.7
v13_cta                       21    53   8     19   12.5      —     12   63.3
v14_caso                       4    49  34     44   12.5      —     13   61.9
a1_matrice                     5    86   2     44   12.5      —     14   61.1
a2_servizi                     9   110   3     44   12.5      —     13   57.8
a3_pricing                     3    74  13     44   12.5      —     13   67.2
a4_faq                         6   124   0     44   12.5      —     16   61.1
a5_assunzioni                  5   102   3     44   12.5      —     13   61.1
--- media parole: 11 · canvas con flag: 0/19 · placeholder visibili: 87
```

### Sales Deck · client

```
id                          copy vista  ph   cont   meta   diag  vista   vis%  flags
v01_cover                     18    50   0     19     19      —   12.5   58.3
v02_tensione                  21    40   0     18   12.5      —   12.5   58.9
v03_categoria                 24    62   0     18   12.5      —     13   59.4
v04_evento_prodotto           15    37   0     44   12.5      —   12.5   67.8
v05_energia                   16    33   0     18   12.5      —   12.5   61.1
v06_priorita                   9    74   0     44   12.5      —     13   65.3
v07_ampiezza                   7    82   0     44   12.5      —   12.5   62.8
v08_offerta                   17    78   0     18   12.5      —     13   62.8
v09_scelta                     8    94   0     44   12.5      —     13   66.4
v10_perche                     5   100   0     44   12.5      —   12.5   61.1
v11_valore                     9    68   0     44   12.5      —     13   61.1
v12_pilot                      8    83   0     44   12.5      —     13   66.7
v13_cta                       21    61   0     19   12.5      —     12   63.3
a1_matrice                     5    86   0     44   12.5      —     14   61.1
a2_servizi                     9   110   0     44   12.5      —     13   57.8
a4_faq                         6   124   0     44   12.5      —     16   61.1
a5_assunzioni                  5   102   0     44   12.5      —     13   61.1
--- media parole: 12 · canvas con flag: 0/17 · placeholder visibili: 0
```

### Dossier · working

```
id                          copy vista  ph   cont   meta   diag  vista   vis%  flags
p01_cover                     65     0   8     14     13      —      —      0
p02_overview                 132     0   2     14     13     13      —     34
p03_livelli                   87     0   2     14     13     13      —   33.3
p04_connect                   75    50   3     14     13      —   12.5   37.4
p05_insight                   53    47   3     14     13      —     13   32.5
p06_refyn                     79     0   6     14     13     14      —   31.3
p07_sorgenti                  74     0   4     14     13      —      —      0
p08_architettura             127     0   6     14     13     13      —   35.1
p09_contesto                  52    34   3     14     13      —   12.5   31.5
p10_oee                       95     0   4     14     13     13      —   26.6
p11_energia                  130     0   4     14     13     13      —   35.6
p12_output                    72     0   4     14     13      —      —      0
p13_pilot                     87     0   4     14     13     13      —     26
p14_servizi                  109     0  10     14     13      —      —      0
pa1_compatibilita            109     0   9     14     13      —      —      0
pa2_sizing                    52     0   9     20     13     13      —     33
pa3_governo                  118     0  13     14     13      —      —      0
pa4_kpi                       74     0  10     14     13      —      —      0
--- media parole: 88 · canvas con flag: 0/18 · placeholder visibili: 104
```

### Dossier · client

```
id                          copy vista  ph   cont   meta   diag  vista   vis%  flags
p01_cover                     75     0   0     14     13      —      —      0
p02_overview                 132     0   0     14     13     13      —     34
p03_livelli                   87     0   0     14     13     13      —   33.3
p04_connect                   75    50   0     14     13      —   12.5   37.4
p05_insight                   53    47   0     14     13      —     13   32.5
p06_refyn                     79     0   0     14     13     14      —   31.3
p07_sorgenti                  74     0   0     14     13      —      —      0
p08_architettura             132     0   0     14     13     13      —   35.1
p09_contesto                  52    34   0     14     13      —   12.5   31.5
p10_oee                       95     0   0     14     13     13      —   26.6
p11_energia                  130     0   0     14     13     13      —   35.6
p12_output                    72     0   0     14     13      —      —      0
p13_pilot                     87     0   0     14     13     13      —     26
p14_servizi                  109     0   0     14     13      —      —      0
pa1_compatibilita            124     0   0     14     13      —      —      0
pa2_sizing                    80     0   0     14     13     13      —     33
pa3_governo                  134     0   0     14     13      —      —      0
pa4_kpi                       86     0   0     14     13      —      —      0
--- media parole: 93 · canvas con flag: 0/18 · placeholder visibili: 0
```

---

## 4. §14 · i sei controlli di build

`work_v91/accept.py` esce con codice 1 se uno fallisce. Oggi passano tutti.

```
  ok   1 · client edition deck: zero placeholder
  ok   1 · client edition dossier: zero placeholder
  ok   2 · CTA presente con partecipanti, output e azione richiesta
  ok   2 · G1 aperto: la CTA non porta il referente, il deck si presenta dal vivo ma non si invia
  ok   3 · nessun valore annualizzato con G3 aperto
  ok   4 · titolo del dossier coerente con G4 OPEN
  ok   5 · asset usati: 0 · tutti registrati
  ok   6 · 10 claim censiti, nessuno fuori registro

```

Il controllo 5 vale anche a registro vuoto: se domani qualcuno mette un `<image>`
in un canvas senza registrarlo in `work_v91/assets91.py`, il build si ferma.

---

## 5. §13 · criteri di accettazione

```
§13 · Sales Deck — 5/10
  ✓ CTA presente
  ✗ contatto presente
  ✗ audit definito
  ✓ struttura economica coerente
  ✗ prezzi o formula approvata
  ✗ servizi inclusi
  ✓ dataset validato o numeri rimossi
  ✗ almeno un asset reale
  ✓ nessun placeholder
  ✓ nessuna nota interna

§13 · Dossier, come preliminare — 5/5
  ✓ claim tecnici prudenti
  ✓ deployment dichiarato da chiudere
  ✓ annessi strutturati
  ✓ proprietà dati prudente
  ✓ nessun placeholder

§13 · Dossier, pronto per IT — 0/10
  ✗ protocolli
  ✗ porte
  ✗ sizing
  ✗ autenticazione
  ✗ backup
  ✗ retention
  ✗ logging
  ✗ supporto remoto
  ✗ licenza
  ✗ dati a fine contratto

=== stato dei gate ===
  G1 Identità e CTA               GLOBAL   OPEN
  G2 Modello commerciale          SECTION  OPEN
  G3 Dataset                      SECTION  OPEN
  G4 Requisiti tecnici minimi     SECTION  OPEN
  G5 Evidenza commerciale         NONE     OPEN
  CASE caso cliente                 PAGE     NO

Sales Deck approvato: NO
Dossier approvato come preliminare: sì
Dossier pronto per IT: NO
```

**Il dossier è approvato come preliminare: 5 su 5.** È il risultato più
significativo della V9.1 — il documento tecnico può andare a Operations,
Engineering e IT così com'è, perché dichiara con precisione che cosa è definito e
che cosa si decide nel solution design.

**Il Sales Deck è a 5 su 10**, e le cinque righe mancanti sono tutte fuori dal
design: contatto, audit, prezzi, servizi compresi, un asset reale. Nessuna si
risolve disegnando.

**Il dossier per IT è a 0 su 10**, che è la definizione di G4 aperto.

---

## 6. Controllo semantico

27 pattern vietati (§2.4 e §3.1) su testo visibile e accessibile, quattro
edizioni: **zero occorrenze**. «in sviluppo» resta una dichiarazione sola per
documento. Grafia del brand unica: `D.Factory`.

## 7. §11.4 · placeholder nei PDF client

```
DFactory_SalesDeck_v9_1_client.pdf       · PH_ nel binario = 0
DFactory_DossierTecnico_v9_1_client.pdf  · PH_ nel binario = 0
```

## 8. Dataset

Catena rieseguita a calcolo: tutti i valori tornano. Con G3 aperto, la client
edition **non pubblica** 309.120 €, 154.560 € e 810 €: la slide 11 mostra la
formula, la 13 rimanda al conto sulla linea del cliente. Il controllo 3 del build
lo verifica cercando le cifre nel corpo client.
