# D.Factory · QA Report V9.3

Fase E5. Quattro documenti, 84 canvas misurati, tre livelli di controllo:
tecnico per canvas, editoriale per canvas, di sequenza sul documento intero.

**Esito: 0 difetti su 84 canvas.** Le condizioni di build passano tutte.

---

## 1. Che cosa viene misurato

| livello | strumento | che cosa guarda |
|---|---|---|
| tecnico | `qa93.py` | overflow del canvas, collisioni fra blocchi, clipping dentro il `viewBox`, corpo effettivo del testo, richieste di rete, errori di console, ancore rotte, id duplicati |
| editoriale | `qa93.py` per tipologia | parole fuori dai disegni, parole dentro i disegni, superficie visiva, corpo minimo — con soglie diverse per tipo di canvas |
| sequenza | `audit93.py` | ritmo dei fondi, layout duplicati, slide tecniche consecutive, viste di prodotto nelle slide pacchetto, tono da questionario |
| contenuto | `accept93.py` | placeholder, claim, formulazioni vietate, valori annualizzati, testo interno, asset non registrati |
| struttura | `mk_dossier93.py` | paragrafo esplicativo 45–100 parole, conteggio delle formule di stato aperto |

### 1.1 Due correzioni al metodo di misura

**Il tetto di parole si applica al testo fuori dai disegni.** Lo dice il §11.2
dello storyboard: «il conteggio è del solo testo fuori dai disegni, come nella
V9.2». Nella V9.2 funzionava per caso, perché ogni diagramma era marcato
`data-ui` e finiva nel secchio delle viste di prodotto. Nella V9.3 i diagrammi
non sono viste di prodotto — una matrice di confronto non è una schermata — e
vanno esclusi esplicitamente. Il testo dei disegni non sparisce dal controllo:
ha un tetto suo, più alto, che serve a impedire che un disegno diventi un muro
di parole travestito da grafico. La tabella qui sotto riporta entrambe le
colonne, `copy` e `pdis`.

**Le regole di ritmo non sono le stesse per i due documenti.** «Mai tre fondi
uguali di fila» è una regola del Sales Deck: un deck si sfoglia e il fondo
scandisce il racconto. Un dossier si consulta, e alternare i fondi lo renderebbe
illeggibile: lì valgono le due regole del §9.5, da tre a quattro pagine scure e
mai quattro pagine di fila senza un elemento visivo forte. Applicare al dossier
la regola del deck avrebbe prodotto tredici falsi positivi.

---

## 2. Sales Deck · client edition · 18 canvas

`copy` = parole fuori dai disegni · `pdis` = parole dentro i disegni ·
`pvis` = parole dentro le viste di prodotto · `vis%` = superficie visiva

| canvas | tipo | copy | tetto | pdis | pvis | corpo min | vis% | tetto | flag |
|---|---|--:|--:|--:|--:|--:|--:|--:|:--:|
| `s01_promessa` | narrativa | 21 | 85 | 0 | 26 | 19 | 31,9 | 45 | — |
| `s02_problema` | narrativa | 61 | 85 | 13 | 0 | 17 | 18,8 | 45 | — |
| `s03_visione` | narrativa | 56 | 85 | 39 | 0 | 18 | 24,5 | 45 | — |
| `s04_trasformazione` | narrativa | 67 | 85 | 0 | 0 | 23 | 0 | 45 | — |
| `s05_prodotto` | prodotto | 10 | 45 | 0 | 37 | 44 | 67,8 | 75 | — |
| `s06_quattro_letture` | prodotto | 23 | 45 | 0 | 71 | 18 | 60,6 | 75 | — |
| `s07_priorita` | valore | 55 | 70 | 34 | 0 | 18 | 36,5 | 55 | — |
| `s08_mappa` | funzionalità | 6 | 75 | 55 | 0 | 44 | 54,5 | 55 | — |
| `s09_connect` | pacchetto | 62 | 95 | 0 | 0 | 16 | 0 | 35 | — |
| `s10_insight` | pacchetto | 59 | 95 | 0 | 0 | 16 | 0 | 35 | — |
| `s11_refyn` | pacchetto | 23 | 95 | 31 | 0 | 16 | 32,8 | 35 | — |
| `s12_confronto` | matrice | 30 | 110 | 59 | 0 | 16 | 45,0 | 60 | — |
| `s13_perche` | azienda | 58 | 60 | 0 | 0 | 18 | 0 | 50 | — |
| `s14_valore` | valore | 29 | 70 | 36 | 0 | 16 | 29,3 | 55 | — |
| `s15_pilot_cta` | cta | 21 | 55 | 16 | 0 | 36 | 31,3 | 45 | — |
| `a1_matrice` | appendice | 5 | 120 | 156 | 0 | 44 | 60,0 | 85 | — |
| `a2_servizi` | appendice | 9 | 120 | 133 | 0 | 44 | 52,3 | 85 | — |
| `a4_faq` → A3 | appendice | 6 | 120 | 147 | 0 | 44 | 53,8 | 85 | — |

Media 33 parole di copy per canvas. Zero placeholder visibili. Nessun canvas
con flag.

### 2.1 Le tre slide con più superficie visiva

S05 al 67,8%, S06 al 60,6%, S08 al 54,5%. Sono le sole tre sopra il 50%, e sono
esattamente le tre che il §16 ammette come «fortemente UI». La regola del
55–70% su ogni canvas, che la V9.2 applicava a tutte e diciannove le slide, non
esiste più: il §19 della V9.3 ordinava di rimuoverla, ed è stata rimossa senza
sostituirla con un'altra soglia minima.

---

## 3. Dossier tecnico · client edition · 21 canvas

| canvas | archetipo | copy | tetto | pdis | corpo min | vis% | flag |
|---|---|--:|--:|--:|--:|--:|:--:|
| `p01_cover` | apertura | 60 | 60 | 0 | 15 | 0 | — |
| `p02_executive` | spiegazione | 121 | 150 | 0 | 16 | 0 | — |
| `p03_architettura_funzionale` | architettura | 76 | 150 | 73 | 17 | 28,5 | — |
| `p04_base_comune` | funzionale | 81 | 150 | 29 | 15 | 16,3 | — |
| `p05_connect` | funzionale | 103 | 150 | 0 | 15 | 36,8 | — |
| `p06_insight` | funzionale | 127 | 150 | 0 | 15 | 22,8 | — |
| `p07_refyn` | funzionale | 100 | 150 | 31 | 15 | 22,0 | — |
| `p08_matrice` | tabella | 177 | 185 | 0 | 14,5 | 0 | — |
| `p09_acquisizione` | architettura | 67 | 150 | 89 | 17 | 31,5 | — |
| `p10_contesto` | spiegazione | 108 | 150 | 26 | 15 | 22,1 | — |
| `p11_architettura` | architettura | 116 | 150 | 38 | 15 | 31,5 | — |
| `p12_security` | tabella | 114 | 185 | 0 | 15 | 0 | — |
| `p13_oee` | metodo | 96 | 150 | 31 | 15 | 16,1 | — |
| `p14_energia` | metodo | 107 | 150 | 76 | 15 | 27,2 | — |
| `p15_output` | tabella | 124 | 185 | 0 | 14 | 0 | — |
| `p16_delivery` | delivery | 85 | 185 | 43 | 15 | 31,0 | — |
| `p17_servizi` | delivery | 176 | 185 | 0 | 14,5 | 0 | — |
| `pa1_compatibilita` | annesso | 137 | 170 | 0 | 14,5 | 0 | — |
| `pa2_sizing` | annesso | 141 | 170 | 0 | 14,5 | 0 | — |
| `pa3_requisiti` | annesso | 151 | 170 | 0 | 14,5 | 0 | — |
| `pa4_kpi` | annesso | 132 | 170 | 0 | 14,5 | 0 | — |

Media 114 parole per pagina. Zero placeholder visibili. Nessun canvas con flag.

### 3.1 Il corpo minimo

Il brief chiede 14 px sul dossier. Il valore più basso misurato è **14 px**
(`p15_output`) e il secondo più basso 14,5 px, sulle cinque pagine con tabella
a otto o quattordici righe. Quel mezzo pixel è la ragione per cui esiste il
passo `tb--dense`: con quattordici righe e un paragrafo di tre righe, il passo
precedente portava la matrice di P08 a 627 px di altezza e la faceva uscire dal
canvas. La scelta è stata stringere il passo, non togliere righe: il §8 P08
prescrive quattordici righe e quattordici sono.

---

## 4. Controlli di sequenza

| controllo | Sales Deck | Dossier |
|---|---|---|
| fondi | `dk lt lt mx lt dk lt dk lt gr dk lt dk lt dk` | `dk dk lt lt lt lt lt lt mx dk lt lt mx lt lt dk lt lt lt lt lt` |
| tre fondi uguali di fila nel corpo | nessuna sequenza | regola non applicabile |
| pagine scure | 6 su 18 | 4 su 21 · il §9.5 ne chiede 3–4 |
| pagine senza elemento visivo forte | — | 3, mai quattro di fila |
| slide tecniche consecutive | 2 · tetto 2 | 2 · tetto 2 |
| canvas con struttura identica | nessuno | nessuno |
| viste di prodotto in slide pacchetto | 0 | — |
| tono da questionario nel core | — | 0 |
| titoli ripetuti | 0 | 0 |

Due note sul ritmo rilevato.

**S04 e S10 non sono slide bianche.** Il classificatore le legge `mx` e `gr`
perché S04 porta un pannello nero su metà canvas e S10 ha il fondo grigio
chiarissimo. È la ragione per cui il corpo non ha mai tre fondi uguali di fila:
se le si contasse entrambe come bianche, S02–S05 sarebbe una sequenza di quattro.

**P09 e P13 risultano `mx` e non `lt`.** La E0 Build Map le dichiarava chiare;
portano una fascia scura di apertura di sezione alta 190 px, e il controllo la
vede. La mappa dichiarata era imprecisa, non il documento: la Rhythm Map
consegnata riporta il valore misurato.

---

## 5. Condizioni di build

| # | condizione | esito |
|--:|---|---|
| 1 | zero placeholder nelle client edition | ok · deck 0, dossier 0 |
| 2 | CTA presente con i tre passi | ok · **warning globale**: G1 aperto, la CTA non porta il referente |
| 3 | nessun valore annualizzato con G3 aperto | ok · né in cifre né in lettere |
| 4 | titolo del dossier coerente con G4 | ok · «preliminare» |
| 5 | nessun asset non registrato | ok · 0 asset usati, registro a 0 righe |
| 6 | nessun claim tecnico fuori registro | ok · 10 claim censiti |
| §12 | nessuna delle 14 formulazioni vietate | ok · nei quattro documenti |
| 7/10 | zero clipping, overflow, collisioni, microtesto | ok · sui quattro documenti |
| 8 | «in sviluppo» al massimo una volta per documento | ok · 1 nel deck, 1 nel dossier |
| 9 | nessun testo interno nelle client edition | ok |
| §5.4 | MAPST e MarEnergy fuori dal deck | ok · zero nel deck |
| §14.3 | audit di sequenza | ok · 12 verifiche superate, 0 problemi |
| §12.2 | paragrafo 45–100 parole su ogni pagina core | ok · 16 su 16 |
| §12.5 | formule di stato aperto sotto i tetti | ok · vedi §6 |

### 5.1 Un controllo corretto durante la Fase E

Il controllo sugli annualizzati cercava la parola «annuo» ovunque nel testo
visibile, e ha segnalato questa frase di S14: «Il risultato si calcola sui dati
della vostra linea, durante l'audit: qui non compare nessun importo annuo».
Cioè la negazione esatta di quello che cercava. Un controllo che segnala la
propria negazione non è severo, è rumoroso: adesso cerca i valori e le
locuzioni che li introducono — «costo annuo», «perdita annua», «settimane
produttive» — non la parola isolata.

---

## 6. Formule di stato aperto · §12.5

| espressione | V9.2 | tetto V9.3 | misurato |
|---|--:|--:|--:|
| `solution design` | 16 | 8 | **8** — una per pagina, mai per riga |
| `da verificare` nel core | — | 1 | **1** — la formulazione prescritta dal §2.4 per P15 |
| `da verificare` negli annessi | 12 | 2 | **2** |
| `da approvare` | 6 | 0 | **0** |
| `da nominare` | 6 | 0 | **0** |
| `chi decide` nel core | 4 | 0 | **0** |
| `owner` nel core | — | 0 | **0** |

Il tetto sul `da verificare` è scomposto in due perché due regole si
sovrappongono: il §12.5 lo vuole solo negli annessi, il §2.4 della review D2
prescrive «da verificare sul perimetro» per le interfacce applicative di P15.
Contarli insieme avrebbe costretto a violarne una.

---

## 7. Verifiche aritmetiche

Rifatte a mano sui numeri pubblicati.

| affermazione | dove | verifica |
|---|---|---|
| fermo 18 min → 9.000 pezzi | deck S06 | 18 × 500 pz/min = 9.000 ✔ |
| 38 kW per 18 min → 11,4 kWh | deck S06 | 38 × 18 ÷ 60 = 11,4 ✔ |
| 11,4 kWh → 2,5 € | deck S06 | 11,4 × 0,22 = 2,51 ✔ |
| fermo 18 min → 1.260 € | deck S05 · S06 | 18 × 70 €/min = 1.260 ✔ |
| OEE da 74,3% a 71,4% | deck S06 | (454+18)/480 = 98,3% · 94,6% × 79% × 95,6% = 71,45% ✔ |
| 58 eventi, 224 min, 15.680 € | deck S07 · dossier P06 | 14+4+38+2 = 58 · 96+62+41+25 = 224 · somma dei costi = 15.680 ✔ |
| prima causa 43% | deck S07 · dossier P06 | 6.720 ÷ 15.680 = 42,9% ✔ |
| OEE 71,4% | dossier P13 | 0,946 × 0,79 × 0,956 = 0,7145 ✔ |
| 735 kWh nel turno | dossier P14 | 454 min × 95 kW ÷ 60 = 719 · 26 × 38 ÷ 60 = 16,5 → 719 + 16 = 735 ✔ |
| 162 € | dossier P14 | 735 × 0,22 = 161,7 ✔ |
| 227.000 pz | dossier P14 | 454 × 500 = 227.000 ✔ |
| 3,2 kWh / 1.000 pz | dossier P14 | 735 ÷ 227.000 × 1.000 = 3,24 ✔ |
| 0,71 € / 1.000 pz | dossier P14 | 3,24 × 0,22 = 0,71 ✔ |
| 1,13 kgCO₂e / 1.000 pz | dossier P14 | 3,24 × 0,35 = 1,13 ✔ |

Tutti i numeri appartengono allo stesso scenario illustrativo, invariante dalla
V8 e non ricalcolato. **Nessuno è un risultato cliente**, e ogni canvas che li
mostra lo dichiara nel piede.

---

## 8. Che cosa questa QA non può dire

- che i numeri siano veri: sono illustrativi, e G3 è aperto;
- che le viste somiglino al prodotto: nessuno screenshot reale è stato consegnato;
- che le specifiche IT siano corrette: G4 è aperto e gli annessi raccolgono
  requisiti, non li dichiarano;
- che il deck sia inviabile: G1 è aperto e senza referente il deck si presenta
  dal vivo.

Quello che può dire è che i due documenti sono tecnicamente puliti, misurati e
coerenti con quello che dichiarano di essere.
