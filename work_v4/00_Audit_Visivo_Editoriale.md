# 00 · Audit visivo ed editoriale — base v2

Metodo: rendering reale di tutte le 12 slide e delle 18 pagine v2 a 1280×720
(`device_scale_factor=2`), provino a contatto, provino a 640×360 e provino in scala di
grigi con sfocatura 2,4 px per il test di gerarchia. Il giudizio nasce dai render, non
dal DOM.

Materiale prodotto: `work_v4/v2_SalesDeck_contact.png`, `work_v4/v2_SalesDeck_small_contact.png`,
`work_v4/v2_SalesDeck_hierarchy.png`, `work_v4/v2_Dossier_contact.png`,
`work_v4/v2_Dossier_small_contact.png`, `work_v4/v2_Dossier_hierarchy.png`.

---

## 1. Stato degli asset nel workspace

| Atteso dal prompt | Presente | Nota |
|---|---|---|
| `DFactory_SalesDeck_v2.html` | Sì · `DFactory_SalesDeck_v2 (1).html` | 12 slide, 290 KB, font inline |
| `DFactory_DossierTecnico_v2.html` | Sì · `DFactory_DossierTecnico_v2 (1).html` | 18 pagine, 332 KB |
| `DFactory_ContentManifest_v2.md` | Sì · `(2)` | 58 claim mappati |
| `DFactory_ChangeLog_v2.md` | Sì · `(1)` | |
| `Marchiani_Assessment_12Marzo.docx` | **No** | Nessun `.docx` nel repository né fra gli upload |
| `DFactory_SalesDeck_v3.html` / `DossierTecnico_v3.html` | **No** | Nessun v3 da usare come riferimento negativo |
| PNG / PDF / provini / cartelle di render | **No** | Nessun render preesistente |
| Non atteso ma presente | `DFactory_Refyn_Context_Brief.md` | **Fonte interna autorevole**, aggiornata al 17/07/2026 |
| Non atteso ma presente | `Refyn_CompanyDeck.pdf`, `Refyn_SalesDeck.pdf` | Materiale a marchio Refyn, superato dalla decisione di brand |
| Non atteso ma presente | `Logo-D-Factory-cce0b268-1.webp` | Fondo giallo incorporato: inutilizzabile su chiaro e su scuro |
| Font | Geist, Geist Mono, Instrument Serif | Estratti in `work_v4/assets/fonts.css`, riusabili |

**Conseguenza sulla Fase A2.** L'assessment non c'è. La premessa del prompt ("l'assessment
adesso è presente") non è verificata nel workspace. Tutti i temi che gli erano attribuiti
restano quindi non pubblicabili per assenza di fonte, non per prudenza editoriale. Il
Context Brief **non** è un sostituto: copre in parte gli stessi temi ma è un documento di
consulenza interno, e i suoi numeri di trazione sono già marcati "da validare" nel
manifest v2.

---

## 2. Dieci problemi prioritari del sales deck

1. **Nove slide su dodici hanno la stessa silhouette.** Titolo in alto a sinistra, filetto,
   fila di tre o quattro riquadri di pari peso, nota in basso. Il provino a contatto si
   legge come un'unica pagina ripetuta dodici volte. Nessun ritmo, nessuna variazione, nessuna
   sorpresa.
2. **Il test di gerarchia fallisce su dieci slide su dodici.** In scala di grigi e sfocato,
   sotto il titolo resta una fascia grigia indifferenziata. Non esiste un punto focale: solo
   `s01_cover` e `s12_cta` sopravvivono al test.
3. **`s05_prodotto_in_azione` non mostra il prodotto.** La slide che dovrebbe essere il cuore
   del deck è composta da quattro card di pari peso contenenti quattro numeri. Nessuna vista,
   nessuna schermata, nessun callout. Il titolo promette un'azione, il visual consegna una
   tabella scomposta.
4. **`s06_prova` è un modulo da compilare esposto al cliente.** Contiene i token letterali
   `[[PH_01_CASO_CLIENTE]]`, `[[PH_02_CITAZIONE_CLIENTE]]`, `[[PH_15_ACMI_OK]]`,
   `[[PH_13_TOYOTA]]` e le frasi "Da compilare con…". Una slide intitolata "La prova" che
   dichiara di non avere prove è peggio dell'assenza della slide.
5. **`s08_business_case` è un foglio di calcolo vuoto.** Due colonne di input con unità e
   nessun risultato. 169 parole visibili, la slide più densa del deck, per non dire un numero.
6. **Il giallo non guida lo sguardo.** In copertina riempie tutti i segmenti "run" di cinque
   macchine: è la campitura di fondo, non un segnale. Su `s02`, `s07`, `s09` è ridotto a
   filetti di 2 px sopra le card, quindi decorativo. Non c'è una pagina in cui il giallo
   indichi una cosa sola.
7. **Densità reale molto oltre il dichiarato.** Il changelog v2 dichiara "media 74 parole,
   massimo 109" *escludendo* micro-etichette, dati e testo SVG. Contando tutto il testo
   visibile: media 135, massimo 169 (`s08`). Il budget del prompt è 40–60 con limite 70. Il
   deck sta a più del doppio.
8. **Corpo e label troppo piccoli a 1280×720.** `--t-lbl:10,5px` e `--t-lbl-s:9,5px` sono i
   corpi delle etichette mono, cioè della maggior parte del testo delle card. Il testo SVG è
   forzato a 10 px. A dimensione reale su proiettore è illeggibile; il render 4K inganna.
9. **Quattro slide su dodici sono quattro pannelli equivalenti** (`s05`, `s07`, `s09`, `s10`),
   tre sono tre pannelli equivalenti (`s02`, `s03`, `s04`). È esattamente l'anti-pattern
   dichiarato.
10. **I titoli sono conclusioni, i visual no.** "Quello che succede in linea diventa una
    decisione", "Il ritorno si misura su due leve", "Macchina ferma non significa linea ferma"
    sono ottimi titoli. Sotto ognuno c'è una griglia che non dimostra niente. Il copy porta
    tutto il peso; il disegno non ne porta nessuno.

### Cosa funziona meglio, e perché

- `s01_cover`: la timeline delle cinque macchine è l'unico visual del deck che comunica
  informazione per forma e non per etichetta. Il readout 68,4 % accanto a 0,029 € è la tesi
  del prodotto in due numeri.
- `s12_cta`: una sola azione, fondo scuro, titolo con una parola in giallo. Ha gerarchia
  perché ha meno cose.
- `s07`, micro-diagramma 02 (buffer-aware): l'unico disegno del deck che spiega un concetto
  che le parole spiegherebbero peggio. È sprecato a un quarto di slide.

### Cosa funziona peggio, e perché

- `s08_business_case`: chiede al lettore di fare i conti a mente su input che non ha.
- `s06_prova`: espone il processo interno di compilazione a chi deve comprare.
- `s09_offerta`: quattro placeholder economici in fila sotto un titolo che promette la
  composizione di un'offerta.
- `s11_faq`: quattro paragrafi in quattro riquadri, zero visual, 159 parole.

---

## 3. Cinque problemi prioritari del dossier

1. **Le sezioni 3 e 4 sono otto pagine consecutive di sole matrici** (`d11`→`d18`). Nessun
   diagramma dominante, testo di tabella al minimo consentito, placeholder distribuiti in
   dodici chip separati. È il punto in cui il documento smette di essere consultabile.
2. **Ventisette token `[[PH_…]]` visibili**, di cui dodici concentrati su `d13` e `d18`,
   cioè proprio le pagine che un reparto IT apre per prime. Il prompt chiede un blocco unico
   "da definire nel solution design": qui sono polverizzati.
3. **`d17_caso_tecnico` è una pagina intenzionalmente vuota** con nove voci "da compilare".
   La scelta di non inventare è corretta; tenerne una pagina intera nel documento consegnato
   no.
4. **Ritmo dark/light a blocchi lunghi**: 1–3 scure, 4 chiara, 5–10 scure, 11–18 chiare. Sei
   pagine scure di fila e poi otto chiare di fila. La monotonia si vede nel provino.
5. **Il dossier e il deck parlano la stessa lingua visiva.** Stesso rail, stessa `.matrix`,
   stessi `.chip`, stesse card, stessa scala tipografica, stesso filetto. Sfogliando i due
   provini in sequenza sembrano lo stesso documento tagliato in due. Devono condividere
   identità, non grammatica.

### Cosa funziona meglio nel dossier

`d05`, `d06`, `d07`, `d08`, `d09`, `d10`. Sono le pagine con un diagramma vero: la timeline
per macchina, lo schema polmone, la curva di velocità con il micro-fermo, la griglia a venti
righe, il Sankey dell'energia. Il Sankey di `d09` è il singolo visual migliore dei due
documenti. Queste pagine dimostrano che il team sa costruire diagrammi informativi: il
problema del deck non è capacità, è allocazione.

### Cosa funziona peggio

`d13_deployment_security`, `d15_output_integrazioni`, `d18_supporto_audit`: tre tabelle con
molte righe corte, nessun punto d'ingresso visivo, il contenuto più richiesto e la resa più
povera.

---

## 4. Anti-pattern del prompt, riscontrati

| Anti-pattern | Riscontro |
|---|---|
| Quattro card o microdiagrammi di pari peso | `s05`, `s07`, `s09`, `s10` |
| Diagrammi che sono liste dentro rettangoli con frecce | `s03` (flowline: tre riquadri e due `→`) |
| Titoli forti seguiti da visual deboli | `s02`, `s04`, `s05`, `s07`, `s08` |
| Pannelli di compilazione esposti come slide commerciali | `s06`, `s08`, `s09` |
| Griglie con troppi microtesti | `s10`, `s11`, `d11`, `d13`, `d15`, `d18` |
| Font leggibile solo in 4K | label 10,5 px e 9,5 px, testo SVG 10 px, ovunque |
| Densità misurata escludendo label e SVG | dichiarato nel changelog v2, §8 |
| Stesso linguaggio di matrici e chip nei due documenti | sistematico |
| Visualizzazione senza punto focale | 10 slide su 12 al test di gerarchia |
| Pagine bilanciate ma senza tensione | `s02`, `s04`, `s09`, `s11` |
| Placeholder visibili in documento cliente | 17 nel deck, 27 nel dossier |
| Claim non confermati con l'aspetto di dati reali | `s06`: `10 · ~70 · ~30 · 24 · 0` in `metric-strip`, formato identico ai KPI veri |
| Layout ripetuti per più di due pagine consecutive | `s02`→`s05`, `s09`→`s11`, `d11`→`d18` |
| Troppo testo per compensare l'assenza di prove | `s06`, `s08`, `s11` |

---

## 5. Densità reale misurata

Conteggio di tutto il testo visibile: titoli, occhielli, label, chip, numeri, unità, stati,
testo SVG, caption e note. Esclusi solo il numero di pagina e il marchio nel rail inferiore.

| Documento | Media | Max | Budget prompt | Esito |
|---|---|---|---|---|
| Sales deck v2 | **135** parole/slide | 169 (`s08`) | 40–60, limite 70 | fuori su **12 slide su 12** |
| Dossier v2 | **177** parole/pagina | 235 (`d17`) | 95–135, limite 165 | fuori su **12 pagine su 18** |

Corpo minimo effettivo misurato a schermo: **9,5 px** (label mono corte), **10 px** (tutto il
testo dentro gli SVG). Il prompt vieta testo importante fra 9,5 e 10,5 px.

---

## 6. Affermazioni più precise di quanto le fonti consentano

| Dove | Affermazione | Problema |
|---|---|---|
| `s06` | `10 clienti · ~70 macchine · ~30 linee · 24 mesi · 0 dismissioni` | Marcati "da confermare" nel manifest, ma resi con lo stesso peso tipografico dei KPI di prodotto. La micro-etichetta non neutralizza la forma |
| `s01`, `s05` | "OEE di linea · tempo reale" | "Tempo reale" non è qualificato nel deck. Il dossier dichiara refresh 5 s: il deck deve essere coerente o più prudente |
| `s05` | "Cinque vettori, misurati sul ciclo" | "Misurato sul ciclo" promette una precisione che `d11` non documenta (fattori emissivi e campionamento sono placeholder) |
| `d03`, `d13` | "Nessuna uscita verso internet" | Reso come assoluto. È il perimetro architetturale previsto, non una proprietà universale del prodotto |
| `s03` | "Nessun hardware nostro a bordo linea" | Corretto solo con la qualifica, che nel deck sta nel rail inferiore a 10,5 px |
| `d11` | "Misurata sul ciclo, non stimata a coefficiente" come titolo di pagina | Il metodo sotto ha due placeholder proprio su fattori emissivi e campionamento |
| `d10` | `0,029 €` e `358,8 g` | Numeri illustrativi resi con la stessa forma dei numeri veri, con la sola micro-etichetta "dati illustrativi" nel rail |
| `s08` | "Esempio illustrativo, non una promessa contrattuale" | Non c'è nessun esempio: c'è solo la formula. La nota difende un contenuto assente |

---

## 7. Decisioni che richiedono validazione

**Commerciale (Pablo / Direzione)**
- Base installata: 10 clienti, ~70 macchine, ~30 linee, 24 mesi, 0 dismissioni — pubblicabili?
- Referenze citabili per nome (testo, mai logo).
- Durata, costo e partecipanti dell'audit: senza, la call to action chiede un impegno senza dirne il prezzo.
- Forbice di prezzo, costo sensoristica, durata e rinnovo contratto.
- Range plausibili per l'esempio economico ricostruibile.

**Tecnica (Matteo De Simone)**
- Elenco protocolli e modelli PLC effettivamente supportati.
- Porte e flussi di rete, sizing del server, autenticazione e ruoli, backup e retention,
  patching, logging, supporto remoto.
- Frequenza reale di aggiornamento, per qualificare "tempo reale".
- Fattori emissivi usati e loro versione; regola di campionamento e gestione dei dati mancanti.
- API e formati di export.

**Legale**
- Diritti di licenza a fine contratto, distinti dalla proprietà del dato.
- Uso di nomi di clienti e di eventuali marchi terzi.
- Se si vuole citare il quadro normativo (Omnibus, iperammortamento L.199/2025): formulazione
  da validare, oppure si resta fuori dalla normativa.

**Di posizionamento (aperta, va chiusa da chi commissiona)**
- Il manifest v2 e il prompt definiscono **Refyn** come *servizio sul dato in definizione, non
  un livello di prodotto*. Il Context Brief del 17/07/2026 lo definisce **modulo di punta**,
  fascia alta "Performance". Le due definizioni non coincidono. In questo lavoro vale la regola
  del prompt; la divergenza è registrata in `DFactory_OpenInputs_v4.md`.
