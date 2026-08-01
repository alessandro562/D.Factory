# D.Factory · Changelog v4

Gli originali non sono stati toccati. `DFactory_SalesDeck_v2 (1).html` e
`DFactory_DossierTecnico_v2 (1).html` restano invariati.

| Documento | v2 | v4 |
|---|---|---|
| Sales deck | 12 slide | **10 slide + 3 di appendice** |
| Dossier tecnico | 18 pagine | **18 pagine**, impianto nuovo |

---

## 1. La decisione che governa tutte le altre

Il difetto più grave dei v2 non era la densità: era che **deck e dossier parlavano la stessa
lingua visiva**. Stesso rail, stessa matrice, stessi chip, stessa scala tipografica. Nel
provino a contatto sembravano lo stesso documento tagliato in due.

I v4 assegnano ai due documenti **due grammatiche diverse e una sola identità**.

- **Sales deck · industrial signal.** Nessuna card, nessuna matrice, nessuna tabella nel
  corpo principale. Il visual dominante è sempre una scena nel tempo. L'impianto di pagina
  cambia a ogni slide.
- **Dossier · fascia di consultazione.** Impianto fisso: 336 px di fascia con sezione,
  domanda, risposta breve e voci aperte; 944 px di campo con **un solo** diagramma o una
  sola vista grande.

Condiviso: palette, font Geist, il giallo come segnale unico, il marchio, il canvas
1280 × 720 e lo stesso evento produttivo (il fermo delle 07:18) raccontato nei visual di
entrambi.

Le due direzioni sono state prototipate e confrontate prima di implementare:
`work_v4/Prototype_Direction_A.html`, `work_v4/Prototype_Direction_B.html`,
`work_v4/02_Direction_Comparison.md`.

---

## 2. Crosswalk del sales deck

| v2 | v4 | Che cosa è successo |
|---|---|---|
| `s01_cover` | `s01_promessa` | Stessa timeline, ma il giallo passa da campitura di tutti i segmenti "run" a **un solo segmento**: il fermo. Titolo e KPI hanno colonne proprie |
| `s02_perche_adesso` | `s02_punto_cieco` | **Riscritta.** Tre punti ciechi e tre trigger in sei riquadri diventano **una scena**: due curve sullo stesso asse dei tempi che mostrano la produzione a zero e il consumo che continua. Da 156 a 49 parole |
| `s03_come_funziona` | `s03_come_funziona` | La `flowline` a tre riquadri con due frecce diventa una **convergenza reale**: quattro linee entrano in un nodo, quattro escono. Il diagramma dimostra la tesi invece di elencarla |
| `s04_tre_decisioni` | `s05_decisioni` | Tre card affiancate diventano una **biforcazione** da un evento unico. Ogni ruolo occupa una riga, non un contenitore |
| `s05_prodotto_in_azione` | `s04_prodotto` | **Rifatta da zero.** Le quattro card con quattro numeri sparivano: non c'era prodotto in una slide intitolata "prodotto in azione". Ora una vista di supervisione occupa il 98 % dell'area utile, con tre callout ancorati alle righe che annotano |
| `s06_prova` | `s07_prova` | **Cambiata di funzione.** Era una scheda da compilare con quattro token visibili e i numeri di trazione non validati. Ora è il confronto fra come rispondi oggi e come risponderai dopo il pilot: nessun dato inventato, nessun placeholder |
| `s07_perche_dfactory` | `s06_perche` | Quattro micro-diagrammi di pari peso diventano **uno solo**. Il buffer-aware, che nel v2 occupava un quarto di slide, è l'intera slide. Da 148 a 67 parole |
| `s08_business_case` | `s08_valore` | Era un foglio di input con unità e nessun risultato, 169 parole. Ora due barre proporzionali con gli input dichiarati sopra e la somma: **30.000 € + 9.900 € = 39.900 €/anno**, marcato "esempio ricostruibile". Ipotesi in appendice `a03` |
| `s09_offerta` | `a01_offerta` | **Spostata in appendice.** Senza prezzo, durata e inclusioni non è un'offerta. I quattro placeholder economici spariscono; resta la struttura. Refyn perde il trattamento grafico di terzo livello |
| `s10_audit_scala` | `s09_percorso` | Quattro pannelli diventano una timeline con quattro momenti e i criteri di uscita su una riga sola. I quattro token sulle condizioni dell'audit spariscono |
| `s11_faq` | `a02_faq` | **Spostata in appendice.** Quattro riquadri di prosa interrompevano il racconto |
| `s12_cta` | `s10_cta` | Una sola azione, i quattro token spariscono. Resta il contatto reale |
| — | `a03_ipotesi` | **Nuova.** Gli input dell'esempio economico e cosa manca per farne un business case |

**Eliminate dal corpo:** nessuna. **Spostate in appendice:** 3. **Cambiate di funzione:** 2.

## 3. Crosswalk del dossier

| v2 | v4 | Che cosa è successo |
|---|---|---|
| `d01_cover` | `d01_cover` | Indice a quattro sezioni conservato, matrice di intestazione ridotta da 5 a 4 voci |
| `d02_architettura_prodotto` | `d02` | Il token sulla relazione societaria diventa una voce leggibile nel blocco "da definire" della fascia |
| `d03_architettura_tecnica` | `d03` | Il diagramma guadagna spazio e perde il vuoto centrale. I due token su protocolli e porte passano nella fascia |
| `d04_capability` | `d04` | Da 9 a 7 righe. Le funzioni di roadmap escono dalla matrice e vanno nel blocco "non presente nel prodotto attuale" |
| `d05_supervisione` | `d05` | I tre callout escono dalla vista ed entrano nella fascia: la vista resta pulita, i callout leggibili a 13,5 px |
| `d06_oee_fermi` | `d06` | Invariata nella sostanza, ricomposta: schema polmone sopra, ranking cause sotto |
| `d07_velocita_qualita` | `d07` | Il micro-fermo diventa il punto focale con un marcatore giallo e una didascalia, invece di essere citato in nota |
| `d08_multi_impianto` | `d08` | Le venti righe restano, la legenda scende sotto l'asse |
| `d09_distribuzione_energia` | `d09` | I nastri restano proporzionali; le tre utenze minori guadagnano etichette spaziate con linee di richiamo |
| `d10_costo_co2_stato` | `d10` | Le due metà diventano due blocchi impilati, con la conclusione in chiaro: "il 42 % è consumato a macchina ferma" |
| `d11_metodo_misura` | `d11` | Sei passi su una linea verticale. I tre token passano nella fascia |
| `d12_brownfield` | `d12` | Da 8 a 7 righe. Gli stati diventano leggibili in scala di grigi |
| `d13_deployment_security` | `d13` | **Rifatta.** Era una tabella con nove token. Ora tre zone di rete con i flussi unidirezionali marcati in giallo, e gli otto punti aperti raccolti in **un blocco unico** nella fascia |
| `d14_sensori` | `d14` | Da 8 a 6 criteri. MID e ISO 50001 restano separati, nella fascia |
| `d15_output_integrazioni` | `d15` | Da 7 righe con token sparsi a 7 righe con tre stati e un blocco aperto unico |
| `d16_delivery_raci` | `d16` | Gli otto passi spariscono: restavano ridondanti con le cinque milestone. Milestone sopra, RACI a 6 righe sotto |
| `d17_caso_tecnico` | `d17_criteri_pilot` | **Cambiata di funzione.** Era una pagina intenzionalmente vuota con nove voci da compilare. Ora sei criteri di accettazione verificabili, con il metodo di verifica accanto. La ragione per cui non c'è un caso cliente resta scritta, nella fascia |
| `d18_supporto_audit` | `d18` | I sei token sul supporto passano nel blocco "da definire in contratto". La checklist si divide in documenti e persone |

---

## 4. Claim riscritti per precisione

| v2 | v4 | Perché |
|---|---|---|
| `10 · ~70 · ~30 · 24 · 0` resi come KPI | **Omessi** | Marcati "da validare" nel manifest ma resi con lo stesso peso tipografico dei numeri veri. La micro-etichetta non neutralizza la forma |
| "OEE di linea · tempo reale" | "aggiornamento 5 s" nel deck e nel dossier | Il deck non promette una frequenza che il dossier non documenta |
| "Nessuna uscita verso internet" | "nessun flusso verso internet dalla rete di linea, nel perimetro concordato con il tuo IT" | È il perimetro architetturale previsto, non una proprietà assoluta del prodotto |
| "Cinque vettori, misurati sul ciclo" | "misurato" dove è strumentato, "calcolato" dove è ripartito | `d09` e `d11` distinguono le due cose |
| "Il ritorno si misura su due leve" senza risultato | Esempio con input dichiarati e aritmetica visibile | Una formula senza risultato non è un business case; un risultato senza input non è verificabile |
| Refyn accanto a Connect e Insights, stesso trattamento | Riga separata, sotto i due livelli, solo in appendice | Il v2 scriveva "mai terzo livello di prodotto" e poi lo disegnava come terzo livello |
| `MAPST 4.0` in `s03` del deck | **Assente dal deck** | La regola del manifest v2 diceva "solo nel dossier" e la sua stessa tabella la violava |
| 44 token `[[PH_…]]` visibili | **0** | Un placeholder visibile in un documento destinato al cliente è un difetto, non un pregio |

## 5. Sistema di design

I commenti dei v2 dichiaravano QUADRO fonte di verità e vietavano modifiche ai token.
L'autorizzazione a superare quel vincolo è stata usata.

**Preservato:** palette nero / bianco / giallo `#E6E011`, font Geist e Geist Mono
incorporati, canvas 1280 × 720, sobrietà industriale, riconoscibilità del marchio.

**Sostituito:**

| Componente v2 | Sorte |
|---|---|
| `.panel`, `.card`, `.chip` | Eliminati. Erano la fonte principale della densità |
| `.matrix` | Solo nel dossier, con padding di riga aumentato e massimo 7 righe |
| `.flowline` | Eliminata. Era una lista dentro rettangoli con frecce |
| `.metric-strip` | Eliminata. Dava forma di dato certo a numeri da validare |
| `.slot`, `.case-grid` | Eliminati con le pagine che li usavano |
| `.stepper` | Sostituito da timeline disegnate, diverse nei due documenti |
| `.rail` a due righe | Deck: una riga in basso. Dossier: fascia laterale |
| `--t-lbl:10,5px`, `--t-lbl-s:9,5px` | Eliminati. Minimo 12,5 px nel deck, 11,5 px nel dossier |
| `.slide svg text{font-size:10px}` | Eliminato. Il testo SVG è dimensionato caso per caso e misurato dopo la scalatura del `viewBox` |

**Nuovi:** `.band` (fascia di consultazione del dossier), `.field`, `.st` (stati leggibili
in scala di grigi), `.open` (blocco unico delle voci aperte), `.co` (callout numerati),
`.viz` (marcatore di area visual per il QA).

## 6. Strumenti

| File | Cosa fa |
|---|---|
| `work_v4/build.py` | Assembla un HTML autonomo da CSS + body + font base64, verifica riferimenti esterni e ID duplicati |
| `work_v4/render.py` | Render per canvas a 1280 × 720, provino a contatto, provino a 640 × 360, provino in scala di grigi sfocata, PDF |
| `work_v4/qa.py` | Overflow, collisioni, corpo effettivo del testo (con scalatura `viewBox`), parole visibili, frammenti, area del visual dominante, link rotti, ID duplicati, richieste di rete |

Tre difetti che il QA ha trovato durante il lavoro e che l'occhio aveva lasciato passare:

1. Le viste di prodotto marcate `aria-hidden` venivano escluse dalla misura dell'area
   visual: `d08` risultava allo 0 % mentre occupa il 75 %.
2. La soglia del corpo minimo era unica per i due documenti, mentre il dossier ammette
   11,5 px per label e tabelle e il deck no.
3. Su una pagina con due visual impilati la misura prendeva solo il più grande. Corretta con
   il riquadro di ingombro dell'unione.

## 7. Limiti ancora aperti

Dettagliati in `DFactory_OpenInputs_v4.md`. In sintesi: audit senza durata e costo, nessun
caso cliente autorizzato, nessun margine orario, nessuno screenshot reale del prodotto,
base installata non validata, e la definizione di Refyn ancora contesa fra due fonti interne.
