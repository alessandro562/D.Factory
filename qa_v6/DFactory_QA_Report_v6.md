# D.Factory · Sales Deck v6 · report QA

Nove slide, canvas 1280×720, HTML autonomo. Font Geist incorporati in base64,
nessuna richiesta di rete, nessun riferimento esterno. 257 KB.

---

## 1. Misure per slide

Il tetto di parole vale sul **copy**, cioè il testo che parla al lettore. Il testo
dentro una vista di prodotto è contenuto della schermata — uno screenshot vero porta
le sue etichette e nessuno le conta come copy — e si misura a parte, come la
filigrana e il piede che stanno su ogni slide.

| # | slide | copy | vista | corpo min. contenuti | corpo min. vista | superficie |
|---|---|---|---|---|---|---|
| 01 | cover | 18 | 28 | 19 px | 12,5 px | 49,4 % |
| 02 | punto cieco | 13 | 42 | 19 px | 13 px | 55,6 % |
| 03 | prodotto in azione | 10 | 37 | 44 px | 12,5 px | 67,8 % |
| 04 | produzione ed energia | 7 | 28 | 44 px | 12,5 px | 66,7 % |
| 05 | dall'evento alla decisione | 9 | 47 | 44 px | 13 px | 65,3 % |
| 06 | Connect, Insight, Refyn | 38 | 79 | 15 px | 11,5 px | 55,0 % |
| 07 | valore illustrativo | 32 | — | 15,8 px | — | 58,3 % |
| 08 | pilot | 7 | 38 | 44 px | 13 px | 66,7 % |
| 09 | call to action | 18 | 23 | 19 px | 12,5 px | 46,1 % |

**Copy: 7–38 parole, media 17.** Tutte sotto il tetto di 45. La slide 06 è la più
carica perché le tre domande e le due righe obbligatorie sono contenuto vincolato.

**Corpo minimo.** Contenuti ≥ 15 px, viste di prodotto ≥ 11,5 px, metadati 12,5 px.
Le soglie sono separate per popolazione: il contenuto si legge in proiezione, le
etichette di una schermata si guardano da vicino come in uno screenshot.

**Zero flag** su 9 canvas: nessun overflow, nessuna collisione fra blocchi, nessun
id duplicato, nessun ancora rotto, nessun errore console.

---

## 2. Superficie occupata da interfacce, grafici, timeline e numeri

**Media misurata: 59 %.** Misurata sull'intero canvas 1280×720, non su un'area utile
ridotta.

Il target del brief è 70 %. Non è raggiunto e vale la pena dire perché, invece di
aggiustare la misura. Un titolo su due righe a 44 px occupa 94 px, il piede altri 50:
sono 144 px di 720, cioè il 20 % del canvas, prima di disegnare qualsiasi cosa. Con
il vincolo dei titoli come affermazioni commerciali — richiesto dallo stesso brief —
il tetto pratico per slide è intorno al 68 %, che è infatti quanto misurano le slide
03, 04, 05 e 08.

Le tre slide che abbassano la media sono la cover (49 %), la call to action (46 %) e
la slide dell'offerta (55 %): le prime due perché la headline è il loro contenuto
principale, la terza perché le tre domande e le etichette dei livelli sono testo
obbligato.

**Se il 70 % va raggiunto alla lettera**, la leva è una sola: headline su una riga e
viste a tutta pagina con il titolo sovrapposto. È una scelta di direzione, non un
lavoro di aggiustamento, e la segnalo invece di prenderla da solo.

---

## 3. Ritmo scuro / chiaro

`01 scura · 02 scura · 03 chiara · 04 scura · 05 chiara · 06 chiara · 07 scura ·
08 chiara · 09 scura`

Le due aperture scure sono volute: la cover e il punto cieco sono la stessa
situazione, prima e senza. Dalla 03 il ritmo alterna. Le due chiare adiacenti, 05 e
06, sono la coppia della decisione.

---

## 4. Il giallo

Compare **una volta per slide** e sempre con lo stesso significato: l'evento, la sua
causa quando pesa, il numero economico da guardare.

| slide | dove | che cosa segna |
|---|---|---|
| 01 | blocco sulla tappatrice + indicatore verticale | l'evento delle 11:24 |
| 02 | pallino accanto a «0 cause registrate» | l'anomalia |
| 03 | blocco + indicatore che attraversa timeline e curva OEE | lo stesso evento |
| 04 | tratto della curva energia + indicatore | l'energia consumata a linea ferma |
| 05 | barra della causa principale | l'elemento economico da osservare |
| 06 | tappatrice ferma, causa che pesa di più, esito da verificare | un segnale per riquadro, sempre quello che il livello aggiunge |
| 07 | il numero annuo | il valore |
| 08 | barra della prima verifica | il momento della decisione |
| 09 | blocco + indicatore | l'evento sulla linea da scegliere |

L'indicatore temporale verticale è lo stesso oggetto su 01, 03, 04 e 09: sempre
giallo, sempre sull'istante dichiarato, mai a metà del blocco.

---

## 5. Dati illustrativi: sono tutti ricostruibili

Nessun risultato di cliente. I parametri sono dichiarati per esteso nel piede della
slide 07 e ogni numero del deck discende da lì.

```
500 pz/min · margine 0,14 €/pz            ->  70 € al minuto
fermo 11:24-11:42, 18 min                 ->  18 × 70 = 1.260 €
7 giorni, per causa (minuti × 70):
  mancanza tappi     14 eventi ·  96 min  ->   6.720 €
  cambio formato      4 eventi ·  62 min  ->   4.340 €
  micro-fermate      38 eventi ·  41 min  ->   2.870 €
  manutenzione        2 eventi ·  25 min  ->   1.750 €
  totale             58 eventi · 224 min  ->  15.680 €
quota della prima causa       6.720 / 15.680  =  43 %
anno                    96 × 70 × 46 settimane  =  309.120 €
ipotesi di dimezzamento                         =  154.560 €
energia   95 kW in marcia · 38 kW a linea ferma · 0,22 €/kWh
turno     ((60-n)·95 + n·38)/60 per ogni ora    =  720 kWh  ->  158 €
```

Il turno vale **720 kWh e non 760**: 760 sarebbe otto ore piene a 95 kW, ma la linea
si ferma 42 minuti. Il numero è calcolato dai fermi dichiarati, ora per ora.

I cinque fermi della cover sono **gli stessi cinque** elencati sulla slide 02, alle
loro ore e con le loro durate: 07:12 · 6 min, 09:03 · 4 min, 11:24 · 18 min,
12:40 · 9 min, 13:15 · 5 min, totale 42 minuti.

---

## 6. Che cosa ha trovato la verifica avversariale

Undici revisori indipendenti hanno guardato i render, non il codice. Sei rilievi
confermati e corretti.

| slide | rilievo | correzione |
|---|---|---|
| 01 | nella fascia energia l'ora del fermo era **la barra più alta**: il fermo sembrava far salire i consumi, l'opposto della tesi del deck | altezze ricalcolate ora per ora da 95 e 38 kW, base a zero, tacche 95 e 0, l'ora del fermo quotata «78 kWh» |
| 01 | l'indicatore stava a 11:33, cioè a metà del blocco giallo, e giallo su giallo lo tagliava in due fermi da nove minuti | portato a 11:24, sul bordo dell'evento, come dichiara il pannello a fianco |
| 02 | la cover mostra la causa del fermo delle 11:24, la 02 dice «0 cause registrate» per **lo stesso** fermo | la 02 non è più una schermata: è il rapporto che il cliente ha oggi, dichiarato «come arriva oggi» |
| 02 | il pannello aveva l'identità grafica del prodotto: sembrava che fosse D.Factory a non registrare le cause | tolto il riquadro dell'applicazione e la barra di testata, restano i filetti di un elenco stampato |
| 02 | la colonna Causa era mezzo metro di vuoto con un trattino invisibile, e le durate erano solo numeri | campi vuoti da compilare al posto dei trattini, e una barra proporzionale accanto a ogni durata |
| 03 | «OEE nella finestra 71,4 %» non era ricostruibile: 71,4 % è l'OEE del turno, non della finestra 10–12 | il numero esce, la curva prende un asse quotato 80 / 60 |
| 04 | «38 kW», il numero che regge la slide, era scritto in nero dentro una campitura gialla al 34 % su fondo scuro | portato fuori dall'area, in bianco, sotto la linea dello zero |
| 04 | l'indicatore non portava né ora né durata e si fermava prima dell'asse dei tempi | ora porta «11:24 · 18 minuti» e arriva all'asse |

Scartato un rilievo sul ritmo (01 e 02 entrambe scure): la ripetizione è voluta, ed è
stata comunque attenuata togliendo alla 02 lo scheletro della schermata.

---

## 7. Quello che resta aperto

Non è QA, ma va detto insieme al resto.

1. **Nessuno screenshot reale.** Tutte le viste sono ricostruzioni, dichiarate come
   tali in ogni piede. Con schermate vere il deck non cambia impianto, cambia
   credibilità.
2. **Durata, costo e partecipanti dell'audit** restano indefiniti: per questo la
   slide 08 dichiara «durate indicative, da confermare in solution design» e la 09
   non è una CTA contrattuale.
3. **«food & beverage»** è ereditato dal materiale sorgente, dal context brief in
   avanti. Se il posizionamento è più largo, è una riga da cambiare su una slide
   sola.
4. **Il dataset illustrativo va validato come plausibile** per una linea F&B reale:
   500 pz/min e 0,14 €/pz di margine sono valori scelti per rendere l'aritmetica
   verificabile, non presi da un impianto. Un esempio non plausibile è peggio di
   nessun esempio, perché il primo a notarlo è il controllo di gestione del cliente.
5. **Il dossier tecnico non è stato toccato**, come richiesto.
