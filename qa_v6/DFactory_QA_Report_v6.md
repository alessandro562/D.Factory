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
| 02 | punto cieco | 13 | 34 | 19 px | 13 px | 55,6 % |
| 03 | prodotto in azione | 10 | 37 | 44 px | 12,5 px | 67,8 % |
| 04 | produzione ed energia | 7 | 28 | 44 px | 12,5 px | 66,7 % |
| 05 | dall'evento alla decisione | 9 | 47 | 44 px | 13 px | 65,3 % |
| 06 | Connect, Insight, Refyn | 17 | 70 | 15 px | 13 px | 65,3 % |
| 07 | valore illustrativo | 35 | — | 15,8 px | — | 58,3 % |
| 08 | pilot | 7 | 39 | 44 px | 13 px | 66,7 % |
| 09 | call to action | 18 | 22 | 19 px | 14 px | 44,4 % |

**Copy: 7–35 parole, media 15.** Tutte sotto il tetto di 45.

**Corpo minimo.** Contenuti ≥ 15 px, viste di prodotto ≥ 11,5 px, metadati 12,5 px.
Le soglie sono separate per popolazione: il contenuto si legge in proiezione, le
etichette di una schermata si guardano da vicino come in uno screenshot.

**Zero flag** su 9 canvas: nessun overflow, nessuna collisione fra blocchi, nessun
id duplicato, nessun ancora rotto, nessun errore console.

---

## 2. Superficie occupata da interfacce, grafici, timeline e numeri

**Media misurata: 59,9 %.** Misurata sull'intero canvas 1280×720, non su un'area utile
ridotta.

Il target del brief è 70 %. Non è raggiunto e vale la pena dire perché, invece di
aggiustare la misura. Un titolo su due righe a 44 px occupa 94 px, il piede altri 50:
sono 144 px di 720, cioè il 20 % del canvas, prima di disegnare qualsiasi cosa. Con
il vincolo dei titoli come affermazioni commerciali — richiesto dallo stesso brief —
il tetto pratico per slide è intorno al 68 %, che è infatti quanto misurano le slide
03, 04, 05 e 08.

Le due slide che abbassano la media sono la cover (49 %) e la call to action (44 %),
dove la headline è il contenuto principale.

**Se il 70 % va raggiunto alla lettera**, la leva è una sola: headline su una riga e
viste a tutta pagina con il titolo sovrapposto. È una scelta di direzione, non un
lavoro di aggiustamento, e la segnalo invece di prenderla da solo.

---

## 3. Ritmo scuro / chiaro

`01 scura · 02 scura · 03 chiara · 04 scura · 05 chiara · 06 chiara · 07 scura ·
08 chiara · 09 scura`

Due coppie adiacenti dello stesso tono, ed è il minimo raggiungibile: la 01 è scura
(copertina), la 03 è chiara (il benchmark approvato) e la 07 deve restare scura
perché il numero giallo su bianco sarebbe illeggibile. Con questi tre vincoli
qualunque disposizione produce almeno due coppie. Le due che restano sono anche le
più difendibili: 01–02 sono la stessa situazione, prima e senza; 05–06 sono la
coppia della decisione.

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
| 06 | il fermo della tappatrice nella sezione Connect | lo stesso evento, una volta sola in tutta la finestra |
| 07 | il numero annuo | il valore |
| 08 | indicatore verticale a fine settimana 8 | l'istante della prima verifica |
| 09 | pallino accanto a «da definire insieme» | la decisione da prendere |

L'indicatore temporale verticale è lo stesso oggetto su 01, 03, 04 e 08: sempre
giallo, sempre su un istante dichiarato, mai a metà di un blocco.

**Il punto giallo della filigrana `D.Factory` nel piede è stato neutralizzato** —
bianco sulle slide scure, nero su quelle chiare. Era l'unico giallo decorativo del
deck e sulla 02 aveva lo stesso peso ottico dell'unico giallo semantico, sulla stessa
riga. Se la filigrana deve restare com'è nel marchio, è una riga di CSS da togliere.

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
turno     ((60-n)·95 + n·38)/60 per ogni ora    =  735 kWh  ->  162 €
OEE       disponibilità 94,6 % × prestazione 79 % × qualità 95,6 %  =  71,4 %
```

**Il turno mostrato è compatibile con la settimana dichiarata.** Le quattro cause della
slide 05 valgono 58 eventi e 224 minuti in sette giorni; togliendo le micro-fermate,
che un rapporto manuale non registra, restano 20 eventi e 183 minuti, cioè **2,9
eventi e 26,1 minuti al giorno**. Il turno delle slide 01, 02 e 03 ne mostra tre per
26 minuti: 07:12 · 5 min, 11:24 · 18 min, 13:15 · 3 min.

**Il turno vale 735 kWh e non 760**: 760 sarebbe otto ore piene a 95 kW, ma la linea
si ferma 26 minuti. Il numero è calcolato ora per ora dai fermi dichiarati.

**L'OEE 71,4 % è ora ricostruibile**: senza dichiarare prestazione e qualità restava
un numero campato in aria, perché 26 minuti di fermo su 480 danno una disponibilità
del 94,6 %, non del 71,4 %. Le tre componenti sono nel piede della slide 07.

---

## 6. Che cosa ha trovato la verifica avversariale

Undici revisori indipendenti hanno guardato i render, non il codice, e hanno prodotto
**66 rilievi**. La fase di confutazione automatica ne ha esaminati 12 e respinti 12,
ma il dato è ingannevole e va detto: quei dodici erano i primi arrivati, cioè proprio
quelli già corretti mentre i revisori ancora giravano, e i confutatori hanno aperto
PNG già sistemati. La selezione vera l'ho fatta io, rilievo per rilievo, sui render.

**Diciotto rilievi accolti.** I dodici strutturali:

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
| 01 03 04 06 09 | **le timeline contraddicevano il calcolo energetico**: si fermava una macchina su tre, ma «0 pz/min», «38 kW» e i kWh orari presuppongono la linea intera ferma | le tre tracce si interrompono insieme, e il giallo dice quale macchina ha causato il fermo |
| 01 02 | **il turno non si riconciliava con la settimana**: 42 min × 7 = 294 contro i 224 dichiarati, e 5 eventi × 7 = 35 contro 58 | turno riportato a 3 fermi e 26 minuti, cioè la media giornaliera dei fermi non-micro |
| 06 | **erano ancora tre colonne equivalenti**: stessa larghezza, stesso passo, stessa grammatica interna, cioè la scala a tre livelli da slide di consulenza | una sola finestra a tutta larghezza che si allunga in tre sezioni numerate — non tre artefatti affiancati ma un artefatto che cresce |
| 06 | la riga «Baseline — 4 settimane — ▪ risultato» era una legenda senza grafico, e il giallo finiva su un segnaposto: una promessa di esito su un modulo «in sviluppo» | testo semplice, nessun marcatore: «Baseline 96 min · verifica a 4 settimane · risultato da leggere» |
| 06 | l'energia di turno stava dentro il blocco delle cause a 7 giorni, sotto la stessa intestazione e incolonnata sugli stessi importi: invitava a sommare periodi diversi | separata da un filetto, con il proprio periodo dichiarato |
| 05 | le barre stavano a 400 px dalla colonna Costo e a 70 px da Eventi: si leggevano come frequenza, e «Micro-fermate» ha 38 eventi con la terza barra più corta | barre spostate a ridosso degli importi |
| 05 | il titolo argomentava per frequenza mentre il pannello ordina per costo: 38 micro-fermate smentivano il titolo due righe più sotto | «Quattordici fermi, una causa sola. Il 43% del costo» |
| 09 | **la 09 era la 01 ristampata**, 91,6 % di superficie identica: il deck si chiudeva tornando all'immagine di apertura | rifatta guardando avanti: il perimetro del pilot, con i campi vuoti che rimano con quelli della 02 |
| 08 | la barra gialla aveva la stessa forma delle barre-costo delle slide 05 e 06 ma polarità opposta: il deliverable letto come il costo maggiore | tutte le barre nere, e la prima verifica marcata dall'indicatore verticale usato altrove |
| 08 | il rettangolo di plot non era chiuso: non si vedeva dove comincia la settimana 1 né dove finisce la 8 | plot chiuso ai due estremi |
| 07 | «Se si dimezza» restava sospesa a 228 px dal numero per una larghezza fissa, e la frase non diceva cosa si dimezza | larghezza fissa tolta, frase completata |

Non accolti, in sostanza, i rilievi sulla superficie e sul ritmo: sono vincoli
aritmetici già spiegati ai punti 2 e 3, non difetti da correggere.

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
