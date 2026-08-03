# D.Factory · V8 · QA dei dodici prototipi

Fase B del piano di upgrade. Sei prototipi per il sales deck e sei per il dossier,
uno per ogni tipologia richiesta dal §11 del brief. Nessun documento completo è stato
prodotto: la Fase C parte solo dopo l'approvazione.

---

## 1. Che cosa contengono i due file

### Sales deck · `DFactory_Prototipi_Deck_v8.html`

| id | tipologia richiesta | titolo |
|---|---|---|
| p1_cover | nuova cover | Dalla linea al margine, nello stesso dato. |
| p2_tensione | narrativa dati → decisioni | Ogni impianto produce dati. Pochi diventano decisioni. |
| p3_categoria | prodotto / categoria | D.Factory raffina segnali grezzi in evidenze operative. |
| p4_offerta | offerta modulare | Tre livelli, una sola base operativa. |
| p5_pacchetti | pacchetti e prezzo | Il livello giusto dipende dalla decisione che vuoi prendere. |
| p6_perche | perché D.Factory | Tecnologia industriale, non solo reporting. |

`p5_pacchetti` mostra la **struttura** del pacchetto — che cosa è avvio, che cosa è
ricorrente, che cosa è opzionale — senza importi. Gli importi sono la decisione C1–C4
della scheda decisioni: la slide non è pubblicabile finché non arrivano.

### Dossier · `DFactory_Prototipi_Dossier_v8.html`

| id | tipologia richiesta | pagina | template |
|---|---|---|---|
| q1_overview | executive technical overview | 02 | B · prodotto |
| q2_connect | pagina Connect | 04 | B · prodotto |
| q3_architettura | architettura + deployment | 08 | C · architettura |
| q4_oee | OEE e perdite | 10 | **A + C** · apre la sezione 3 |
| q5_energia | energia, costo e CO₂ | 11 | C · architettura |
| q6_annesso | annesso tecnico | A4 | D · specifica |

I quattro template sono tutti rappresentati. Il template A non è una pagina in più:
è la fascia scura in testa alla prima pagina di una sezione, ed è per questo che
`q4_oee` la porta invece di avere un canvas dedicato.

**Perché l'annesso prototipato è A4 e non A1.** A1 (matrice protocolli), A2 (sizing) e
A3 (security e licenza) hanno una struttura pronta e nessun valore verificato. A4 è
l'unico i cui contenuti dipendono dal metodo e non da dati che non ho: le formule sono
scrivibili oggi. Prototipare A1 avrebbe significato inventare versioni testate e
compatibilità.

---

## 2. Misure automatiche

Metrica per canvas. `copy` esclude il testo che appartiene a una vista di prodotto e
il testo di servizio (header, piede, note): conta solo la copy della pagina.

### Deck · soglie `sales`

```
id            copy vista  cont  meta  diag vista  vis%  flag
p1_cover        18    50    19    19     —  12.5  58.3   —
p2_tensione     21    40    18  12.5     —  12.5  58.9   —
p3_categoria    28    60    18  12.5     —    13  59.4   —
p4_offerta      15    79    18  12.5     —    13  62.8   —
p5_pacchetti     9    50    44  12.5     —    14  59.7   —
p6_perche        5    65    44  12.5     —  12.5  56.1   —
media parole 16 · canvas con flag 0/6
```

Le regole del reset V6 restano rispettate: copy ≤ 45 parole, superficie visiva ≥ 55%,
un solo fuoco per slide.

### Dossier · soglie `dossier`

```
id                copy vista  cont  meta  diag vista  vis%  flag
q1_overview        117     0    14    13    13     —  36.7   —
q2_connect          76    49    14    13     —  12.5  37.4   —
q3_architettura    120     0    14    13    13     —  35.1   —
q4_oee              95     0    14    13    13     —  26.6   —
q5_energia         127     0    14    13    13     —  35.6   —
q6_annesso          78     0    14    13     —     —     0   —
media parole 102 · canvas con flag 0/6
```

`q6_annesso` ha superficie visiva 0 perché la tabella **è** il contenuto: la soglia
visiva del dossier è 0 per costruzione, quella del deck è 55%.

### Controlli passati da tutti e dodici i canvas

- nessun elemento fuori dal canvas 1280×720;
- nessuna collisione fra blocchi di primo livello — il rail non è più escluso dal
  controllo, dopo il falso negativo trovato sui prototipi deck;
- corpo del testo sopra la soglia della sua popolazione (copy 14, diagramma 13,
  vista 12, servizio 12,4);
- zero richieste di rete, zero errori di console, zero id duplicati, zero ancore rotte;
- zero apostrofi diritti e zero accenti scritti con apostrofo, anche nei testi
  accessibili `<title>` e `<desc>`;
- lista semantica §15.3: **nessuno dei 23 termini vietati** compare né nel testo
  visibile né in quello accessibile.

---

## 3. Correzioni fatte prima di consegnare

Cinque problemi trovati leggendo i PNG renderizzati, non dal QA automatico.

1. **`p5_pacchetti` · fascia economica sopra il rail.** Il QA non l'aveva vista perché
   `.rail` era escluso dal rilevamento collisioni. Ho tolto l'esclusione e spostato la
   fascia dentro l'SVG. Il controllo ora vede anche questo caso.

2. **`q1_overview` e `q3_architettura` · connettori che finivano nel vuoto.** In
   entrambi un blocco della riga centrale non aveva alcuna gamba verso il bus, e in
   `q3` la discesa dall'acquisizione atterrava nello spazio *fra* i due riquadri
   dell'applicazione invece che sui riquadri. Rifatti come distributore esplicito:
   ogni gamba parte da un centro di riquadro e termina su un centro di riquadro.

3. **`q4_oee` · le barre non misuravano il numero scritto accanto.** La barra
   «Performance» era lunga il 74,7% ma portava scritto 79%: il primo è il cumulato,
   il secondo il fattore. Un lettore che misura la barra trovava un numero diverso da
   quello stampato. Ora la barra è lunga quanto il valore a destra (100 · 94,6 · 74,7 ·
   71,4) e il fattore sta nella riga piccola sotto l'etichetta. La cascata è
   ricostruibile: 94,6% × 79% × 95,6% = 71,4%.

4. **`q5_energia` · una catena che affermava un calcolo falso.** I tre riquadri erano
   collegati da frecce, e leggerli in fila diceva «735 kWh → 162 € → 227.000 pezzi»:
   ma i pezzi non derivano dal costo. Tolte le frecce; i tre numeri sono ora i totali
   del turno, ognuno con il proprio calcolo scritto sotto, e la normalizzazione per
   1.000 pezzi è una fascia separata con la sua derivazione.

5. **`q3_architettura` · l'etichetta «confine di rete» sedeva sulla linea.** Spostata
   nella colonna delle etichette a sinistra, con la riga che parte dal margine dei
   riquadri.

Tutti i numeri restano quelli del dataset illustrativo già usato nel deck: nessun dato
nuovo è stato introdotto in questa fase.

---

## 4. Che cosa resta aperto

Il QA misura la forma, non la verità dei contenuti. Restano vere le tre limitazioni già
dichiarate:

- **Non esistono screenshot reali di prodotto.** `q2_connect` e le viste del deck sono
  ricostruzioni grafiche, dichiarate come tali in piede e nel testo accessibile. Se
  esistono schermate reali, sostituirle cambia la credibilità della pagina più di
  qualunque altra correzione.
- **Il dataset è illustrativo e non validato.** Turno, settimana, potenze, prezzo
  energia e fattore di emissione sono coerenti fra loro e ricostruibili, ma nessuno li
  ha confermati come plausibili per un impianto reale (decisione V1).
- **I prezzi non ci sono.** `p5_pacchetti` mostra la struttura commerciale; senza C1–C4
  il deck non è un sales deck finale, ed è la stessa conclusione del §12 del brief.

---

## 5. Come guardarli

- `DFactory_Prototipi_Deck_v8.png` e `DFactory_Prototipi_Dossier_v8.png` — contact
  sheet, due colonne, per giudicare il ritmo;
- i due `.html` — versione a schermo, autonoma, nessuna richiesta di rete;
- i due `.pdf` — per la stampa e per l'annotazione.

Il passo successivo è la Fase C, e parte solo su approvazione.
