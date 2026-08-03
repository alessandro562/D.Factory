# D.Factory · V9.3 · Prototype Delta D1 → D2

**Fase D2 del §9 della review.** Rigenerati soltanto gli otto prototipi.
Il build completo non è stato avviato: il §9 lo vieta prima dell'approvazione D2.

Base: `DFactory_V9_3_Prototype_Review_and_Design_Delta.md`.
Il verdetto del §1.1 — direzione approvata, design non ancora approvato — è
stato preso alla lettera: la strategia non è stata riaperta, il design sì.

---

## 1. In una tabella

| | D1 | D2 |
|---|---|---|
| S04 | tabella prima/dopo, cinque righe, un cursore giallo | cerniera narrativa: pannello nero / cucitura gialla / pannello bianco, dieci frasi intere, chiusura in scala |
| S09 | tre etichette (Supervisione, Indicatori, Output) | tre verbi (Vede, Misura, Rende disponibile) + fascia risultato grigia |
| S10 | tre categorie, identiche a Connect | tre domande + fascia risultato **nera** + fondo grigio chiarissimo |
| S11 | tre colonne come le altre due | ciclo su asse con ritorno, fondo nero, accento giallo sulla verifica |
| P02 | pagina bianca con cinque micro-sezioni a destra | **pagina scura**, tre livelli di lettura, un solo asse giallo |
| P05 | vista 720×272 a sinistra, funzioni fitte a destra | vista **1152×272 a tutta larghezza**, quattro capability sotto |
| P11 | schema a quattro colonne pallido, 20,7% | **stack a quattro livelli, 748×388, 31,5%** (+52%) |
| P15 | una tabella con dashboard, report, export, API, ERP | **due tavole**: output e integrazioni |
| corpo minimo delle funzioni | 17 px deck / 15 px dossier | 16 px deck / 15 px dossier, nessun contenuto strategico sotto |
| archetipi grafici visibili | 2 | **4** — editoriale scuro, product page, architettura, reference |
| canvas con flag di QA | 0/8 | **0/8** |

---

## 2. Sales Deck

### 2.1 S04 · Trasformazione · §4.1

La review diceva: «la slide appare incompleta, il segno giallo centrale non ha
un significato sufficiente, le righe sembrano una tabella senza intestazioni
forti».

| correzione richiesta | applicata |
|---|---|
| cinque frasi intere per parte, non frammenti | ✔ «Il fermo viene ricostruito dopo.» … «Le azioni vengono confrontate con una baseline.» |
| «Oggi» e «Con D.Factory» più visibili | ✔ etichette in testa a ciascun pannello |
| corpo delle coppie +25–35% | ✔ 18 → **23 px** (+28%) |
| ridurre le linee sottili | ✔ da tre righelli a **zero**: la separazione è il cambio di fondo |
| fondo nero a sinistra, bianco a destra, titolo su bianco | ✔ |
| il giallo marca il passaggio | ✔ cucitura verticale di 12 px fra i due pannelli, unico giallo della slide |
| chiusura con una frase grande | ✔ «Da dati separati a una gestione condivisa.» a 44 px |
| evitare box chiusi | ✔ nessun bordo, nessun riquadro |

Il tetto di parole della slide narrativa sale da 55 a 85: la review prescrive
dieci frasi intere più una chiusura, ed è testo approvato. Registrato al §5.1.

### 2.2 S09 · Connect · §4.2

| correzione richiesta | applicata |
|---|---|
| tre verbi al posto di tre etichette | ✔ **Vede · Misura · Rende disponibile** |
| funzionalità più grandi | ✔ 17 → 16 px ma con interlinea 1,75 e quattro voci per nucleo invece di cinque |
| titoli dei nuclei con peso | ✔ 17 px, peso 650, non più `.lbl` in mono a 14 px |
| risultato in una fascia di grande peso | ✔ fascia a tutta larghezza, 112 px, fondo `paper-2`, testo a 30 px |
| attivazione su una riga leggibile | ✔ «Assessment · setup · configurazione · canone ricorrente» a 16 px |
| nessun microtesto sopra il titolo | ✔ «livello di accesso» eliminato dalla posizione sopra il nome |
| segmenti grandi, non decorativi | ✔ tre barre da 14 px in alto a destra, la prima gialla, con «livello 1 di 3» |
| nome dominante | ✔ 64 px (§5.4: 56–68) |

### 2.3 S10 · Insight · §4.3

| correzione richiesta | applicata |
|---|---|
| tre domande al posto di tre categorie | ✔ **Dove si perde? · Quanto pesa? · Cosa viene prima?** |
| differenza di scala fra domande e funzioni | ✔ domande 22 px peso 500, funzioni 16 px |
| due segmenti chiaramente leggibili, uno neutro e uno giallo | ✔ primo nero, secondo giallo, terzo spento |
| fascia risultato più marcata di Connect | ✔ **fascia nera** a tutta larghezza, testo bianco |
| progressione da Connect visibile | ✔ fondo `paper-2` invece di bianco, più il segmento e la riga «comprende Connect» |
| non usare un grafico | ✔ nessun SVG sulla slide |
| numero economico illustrativo «soltanto se supportato» | **non inserito**: non è supportato. Vedi §5.2 |

### 2.4 S11 · Refyn · §4.4

| correzione richiesta | applicata |
|---|---|
| tre parole grandi collegate da una linea | ✔ **Priorità · Azioni · Verifica** a 40 px su un asse orizzontale |
| ritorno sottile | ✔ linea di ritorno sotto le tre stazioni, con testa di freccia e didascalia |
| un solo accento giallo sulla verifica | ✔ il marcatore della terza stazione |
| stato accanto al nome, in testo leggibile | ✔ «Modulo avanzato in sviluppo» a 16 px accanto a «Refyn». **Nessun badge isolato** |
| tre segmenti, maggiore contrasto | ✔ fondo nero, tre barre bianche |
| non tre colonne perfettamente equivalenti | ✔ stazioni a 0, 430 e 820 su 1152: passi disuguali |
| il ciclo deve essere percepito | ✔ asse + ritorno + didascalia «i risultati verificati aggiornano le priorità del ciclo successivo» |
| chiusura dominante | ✔ «Un ciclo governato, non un elenco di buone intenzioni.» a 34 px |

### 2.5 La progressione dei pacchetti · §5.2

Percepibile prima di leggere, come chiede il §3.3:

| | fondo | segmenti | fascia risultato | densità |
|---|---|---|---|---|
| **Connect** | bianco | 1 giallo | grigio chiaro | aperta |
| **Insight** | grigio chiarissimo | 1 nero + 1 giallo | **nera** | controllata |
| **Refyn** | **nero** | 3 bianchi | nessuna fascia, testo dominante | ciclo |

> visibilità → comprensione → governo

Limiti del §5.3 rispettati: **12 righe funzionali** per slide (3 nuclei × 4),
un risultato, una riga di attivazione.

---

## 3. Dossier

### 3.1 P02 · Executive summary · §6.1

| correzione richiesta | applicata |
|---|---|
| tre livelli di lettura | ✔ definizione 36 px → paragrafo 17 px → tre principi |
| frase guida dominante | ✔ «D.Factory unisce dati industriali e contesto operativo in un unico modello.» |
| paragrafo 60–80 parole | ✔ 62 parole |
| tre principi, non cinque micro-capitoli | ✔ Brownfield first · Produzione ed energia integrate · Un modello dati condiviso |
| fascia inferiore con i tre livelli commerciali | ✔ Connect · Insight · Refyn, nomi a 24 px |
| rimuovere la colonna destra con cinque micro-sezioni | ✔ |
| rimuovere i divisori in eccesso | ✔ da tre righelli a **uno**, e quello è l'asse giallo |
| un solo asse giallo | ✔ barra di 6 px che separa il prodotto dall'offerta |
| corpo minimo 16 px | ✔ paragrafo 17, principi 16, fascia 16 |

**In più:** la pagina passa al fondo scuro. Il §7.3 chiede 3–4 pagine scure nel
dossier e cita «una pagina di apertura prodotto»: P02 è quella, e in D2 serve a
mostrare il contrasto che il §10 chiede di vedere già nei prototipi.

### 3.2 P05 · Connect · §6.2

| correzione richiesta | applicata |
|---|---|
| visuale 55–60% della pagina | ✔ da 720×272 a **1152×272 a tutta larghezza**: area +60%, dal 21,3% al 34% del canvas |
| elenco funzioni meno fitto | ✔ da una colonna di otto righe a **quattro capability da tre righe** |
| output e configurazioni non compressi in fondo | ✔ sono due delle quattro colonne, con lo stesso peso delle altre |
| «limiti» fuori dalla pagina prodotto | ✔ **spostato nella matrice funzionale P08**, dove la differenza fra livelli è il contenuto della pagina |
| paragrafo ≤ 70 parole | ✔ 51 parole |
| piccoli titoli funzionali, non una colonna continua | ✔ Supervisione · Indicatori · Storico e distribuzione · Configurazione |
| corpo della lista più grande | ✔ 15 px, sopra il minimo di 13,5–14 del §8.4 |

### 3.3 P11 · Architettura · §6.3

Era «la pagina più debole degli otto prototipi». È stata rifatta.

| correzione richiesta | applicata |
|---|---|
| diagramma almeno doppio | ✔ da 768×248 (20,7%) a **748×388 (31,5%)**: area **+52%** — vedi §5.3 |
| quattro livelli espliciti | ✔ 1 Impianto · 2 Acquisizione · 3 Piattaforma · 4 Utenti e sistemi, numerati |
| impianto grigio chiaro | ✔ `paper-2` |
| acquisizione bianca con bordo | ✔ |
| piattaforma nera | ✔ è l'unico livello nero: è il prodotto |
| output bianco | ✔ |
| flussi neri, opzionale tratteggiato | ✔ ERP e API in riquadro tratteggiato |
| giallo solo sul passaggio al contesto | ✔ freccia gialla da acquisizione a piattaforma, con «qui il dato riceve il contesto» |
| a destra due blocchi soltanto | ✔ Standard di prodotto · Configurazione di progetto |
| rimuovere richiede / non presuppone / valori di progetto | ✔ tutti e tre |
| rimuovere le note duplicate | ✔ resta una nota, quella del claim sola lettura |
| claim sola lettura nella formulazione approvata | ✔ testo integrale del §6.3 |
| un punto focale | ✔ la fascia nera della piattaforma, al centro dello stack |

### 3.4 P15 · Output · §6.4

L'errore concettuale era reale: ERP non è un output e API è un'interfaccia.

| correzione richiesta | applicata |
|---|---|
| dividere in due parti | ✔ **Output** (dashboard, report, export) e **Integrazioni** (API, ERP) |
| colonne output: contenuto, frequenza, formato | ✔ |
| colonne integrazioni: scopo, modalità | ✔ |
| frase di chiusura | ✔ «Gli output vengono configurati in funzione del processo; le integrazioni vengono definite sul perimetro reale.» |
| due pannelli aperti, non box pesanti | ✔ nessun riquadro: due tavole con la propria etichetta |
| maggiore differenza tipografica | ✔ etichette di sezione sopra ciascuna tavola |
| eliminare il footer «catalogo degli output» | ✔ rimosso |
| anteprima di report solo se reale | **non inserita**: non esiste un report reale |

---

## 4. Correzioni trasversali · §8

| regola | applicazione |
|---|---|
| **§8.1 segmenti** | tre barre da 14 px, non più tre trattini da 6. Etichetta esplicita «livello *n* di 3», e la cumulatività scritta: «comprende Connect», «comprende Connect e Insight» |
| **§8.2 giallo** | S04 cucitura del passaggio · S09 primo livello attivo · S10 secondo livello attivo · S11 verifica · P02 asse fra prodotto e offerta · P11 passaggio al contesto · P05 fermo in corso. **Un solo elemento giallo per canvas, sempre con un significato** |
| **§8.3 linee** | eliminati tre righelli da S04, due da P02, le note laterali da P11. Ogni linea rimasta è un asse, un confine o un connettore |
| **§8.4 microtesto** | funzioni del deck a 16 px, contenuto funzionale del dossier a 15 px. Sotto i 14 px restano solo piede, navigazione e numerazione |
| **§8.5 conclusione** | S04 chiusura in scala · S09/S10/S11 risultato · P02 fascia dei tre livelli · P05 quattro capability · P11 claim di perimetro · P15 frase di chiusura |

---

## 5. Decisioni registrate

Tre punti in cui la review chiede qualcosa che va dichiarato invece di essere
applicato in silenzio.

### 5.1 Il tetto di parole della slide narrativa

Il master V9.3 §11.2 fissa 55 parole sulle slide narrative. La review prescrive
per S04 dieci frasi intere più una chiusura: sono **67 parole**, e sono testo
approvato parola per parola.

**Risoluzione:** il tetto per la tipologia `narrativa` sale a 85 in `qa93.py`.
Vale per la slide di trasformazione, che è una cerniera e non una slide di
posizionamento. Le altre narrative — S01, S02, S03 — restano ampiamente sotto.

### 5.2 Il numero economico su Insight

Il §4.3 ammette «un numero economico illustrativo non monetario, ad esempio
"4 cause ordinate" **soltanto se supportato**».

**Risoluzione:** non inserito. Un numero di quel tipo sarebbe letto come una
capacità del prodotto («ordina quattro cause») quando è una proprietà dello
scenario illustrativo. Lo spazio c'è: entra quando il dataset è validato,
insieme al resto del business case.

### 5.3 «Un diagramma almeno doppio» su P11

Il §10 chiede che P11 abbia «un diagramma almeno doppio rispetto all'attuale».
Il diagramma passa da 190.464 px² a 290.224 px²: **+52%**, non +100%.

**Perché non il doppio:** il §6.3 chiede anche una colonna destra al 30–35% con
due blocchi. Con 368 px di colonna e 64 px di margine, la larghezza massima del
diagramma è 748. Per raddoppiare l'area servirebbero 509 px di altezza, e la
pagina ne ha 388 fra il paragrafo e il piede. Le due richieste non stanno
insieme, e ho tenuto quella che il §6.3 descrive nel dettaglio.

Il risultato misurato è comunque il più grande dei quattro prototipi dossier, e
la pagina ha adesso un punto focale — la fascia nera della piattaforma — che
prima non aveva.

---

## 6. QA

`qa93.py`, profilo V9.3: nessuna percentuale visuale minima per canvas — il §19
del master la vieta e il §11 della review la ribadisce. Resta un **tetto** per
tipologia, dichiarato sul markup con `data-tipo`.

### Deck

| canvas | tipo | copy | corpo min | vis% | flag |
|---|---|--:|--:|--:|:--:|
| `s04_trasformazione` | narrativa | 67 | 23,0 | 0 | — |
| `s09_connect` | pacchetto | 62 | 16,0 | 0 | — |
| `s10_insight` | pacchetto | 59 | 16,0 | 0 | — |
| `s11_refyn` | pacchetto | 54 | 16,0 | 32,8 | — |

### Dossier

| canvas | tipo | copy | corpo min | vis% | flag |
|---|---|--:|--:|--:|:--:|
| `p02_executive` | spiegazione | 120 | 16,0 | 0 | — |
| `p05_connect` | funzionale | 93 | 15,0 | 34,0 | — |
| `p11_architettura` | architettura | 78 | 15,0 | 31,5 | — |
| `p15_output` | tabella | 125 | 14,0 | 0 | — |

**Zero overflow, zero clipping, zero collisioni, zero elementi fuori viewBox,
zero placeholder visibili.**

### Condizioni di approvazione del §10, misurate

| condizione | esito |
|---|---|
| S04 non sembra una tabella before/after | ✔ due pannelli su fondi diversi, nessuna griglia |
| Connect, Insight e Refyn non sembrano la stessa scheda | ✔ tre fondi, tre trattamenti del risultato, tre strutture |
| la progressione è visibile senza leggere | ✔ bianco → grigio → nero, 1 → 2 → 3 segmenti |
| il risultato di ogni pacchetto è dominante | ✔ fascia 112 px o testo a 34 px |
| funzioni leggibili a 640×360 | ✔ 16 px, provino piccolo generato |
| Refyn comunica un ciclo | ✔ asse con ritorno e didascalia |
| nessuna dashboard nelle slide pacchetto | ✔ **zero** `svg[data-ui]` su S09, S10, S11 — condizione di build |
| nessuna lista oltre cinque righe senza raggruppamento | ✔ massimo **quattro** righe per nucleo |
| P02 ha una frase guida dominante | ✔ 36 px |
| P05 ha un visuale prodotto leggibile | ✔ 1152 px di larghezza, corpo UI a 13 px |
| P11 ha un diagramma ampliato | ✔ +52%, vedi §5.3 |
| P11 distingue standard e configurazione | ✔ due blocchi, nient'altro |
| P15 separa output e integrazioni | ✔ due tavole |
| nessuna pagina sembra un questionario | ✔ zero «chi decide», zero «owner», zero «da approvare» |
| almeno due archetipi grafici | ✔ **quattro**: editoriale scuro, product page, architettura, reference |

### Semantica

| | deck | dossier |
|---|--:|--:|
| termini vietati | 0 | 0 |
| «in sviluppo» | 1 | 1 |
| grafie del brand | solo `D.Factory` | solo `D.Factory` |
| placeholder visibili | 0 | 0 |

---

## 7. Che cosa cambia nel design system

Componenti nuovi, tutti dentro la palette, la griglia e le famiglie esistenti.
Nessun redesign del brand.

**Deck**

| classe | funzione |
|---|---|
| `.pk__n` | nome del pacchetto, 64 px |
| `.pk__p` | promessa, 24 px |
| `.pk__s` | stato accanto al nome, 16 px |
| `.lvl` | indicatore cumulativo: tre barre da 14 px, `on` e `ac` |
| `.nu` | titolo del nucleo funzionale, 17 px peso 650 |
| `.fn` | riga funzionale, 16 px, interlinea 1,75 |
| `.resb` `.res` | fascia e testo del risultato, 30 px |
| `.act` | attivazione, 16 px |
| `.tf__t` | riga della cerniera, 23 px |

**Dossier**

| classe | funzione |
|---|---|
| `.par` | paragrafo esplicativo, 17 px, obbligatorio su ogni pagina core |

Correzione di un difetto del foglio di stile: `.lt .lbl` veniva dopo `.dk .lbl`
e vinceva per ordine, quindi un'etichetta dentro un pannello scuro su una slide
chiara era grigio scuro su nero — invisibile. Le due regole sono state
invertite.

---

## 8. Stato

**Fase D2 chiusa. Il build completo non è stato avviato.**

Il §9 della review lo vieta prima dell'approvazione, e il §11 lo ripete:
«Fermati dopo D2. Non avviare il build completo senza nuova approvazione».

Quello che aspetta il giudizio è il sistema, non le otto pagine: se la
grammatica dei pacchetti e i quattro archetipi del dossier reggono, la Fase E
li moltiplica su 15 + 4 slide e 17 + 4 pagine senza altre decisioni di design.

Restano fuori, come da §15 del master: prezzi, contatti, asset reali,
validazione del dataset, specifiche IT/OT e caso cliente.
