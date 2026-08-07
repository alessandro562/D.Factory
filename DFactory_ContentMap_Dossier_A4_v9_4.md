# D.Factory · ContentMap · Dossier tecnico A4 V9.4

Che cosa dice ogni pagina, per chi è, e che cosa deliberatamente non dice.
Ventidue pagine: 18 core più 4 annessi.

---

## 0 · La struttura

| sez. | titolo | pagine |
|---|---|---|
| — | copertina | 01 |
| **0** | Come si legge | 02 |
| **1** | Prodotto | 03 – 08 |
| **2** | Dati | 09 – 12 |
| **3** | Misure | 13 – 15 |
| **4** | Delivery | 16 – 17 |
| — | chiusura | 18 |
| **A** | Annessi | A1 – A4 |

La navigazione in testa a ogni pagina porta tutte e sei le voci e marca quella
attiva. Gli annessi hanno una voce propria: nella V9.3 la navigazione tornava
indietro alla sezione 2 quando si entrava negli annessi, e il lettore aveva
l'impressione di aver perso il segno.

---

## 1 · I quattro percorsi di lettura

Dichiarati a pagina 02. Tre pagine ciascuno.

| ruolo | pagine | la domanda a cui rispondono |
|---|---|---|
| IT di stabilimento | 11 · 12 · 09 | che cosa mettiamo in rete, come, con quali permessi |
| Produzione e plant manager | 13 · 05 · 15 | che cosa vede il reparto e come si valida un numero |
| Energy manager | 14 · 06 · 09 | come l'energia si lega allo stato produttivo |
| Direzione e acquisti | 03 · 08 · 17 | che cosa si compra, in che ordine, con quali servizi |

---

## 2 · Pagina per pagina

### 01 · Copertina — scura
Marchio, filetto giallo, «Dossier tecnico», una riga di sottotitolo, tre voci di
emissione: edizione, uso, formato. Niente indice, niente blocco contatti.
**Non dice:** chi lo manda. Quello sta in chiusura.

### 02 · Come si legge — sezione 0
*Per tutti.* Quattro percorsi da tre pagine, l'elenco dei quattro annessi con il
momento in cui si compilano, e una frase di priorità: «se leggi una pagina sola,
leggi la 03».
**Pagina nuova.** Nel formato slide non poteva esistere.

### 03 · Executive summary — scura, sezione 1
*Direzione.* La definizione del prodotto, tre principi (brownfield first,
produzione ed energia integrate, un modello dati condiviso), i tre livelli in
tabella con promessa e che cosa aggiungono, e i rimandi a 08, 16 e 17.
**Non dice:** i prezzi. **Dichiara:** Refyn è un modulo avanzato in sviluppo.

### 04 · Dal segnale alla decisione — sezione 1
*Per tutti.* Le cinque stazioni della catena funzionale, con la decisione marcata
in giallo perché è l'unica che non appartiene al software. Sotto, la base comune
ai tre livelli in quattro famiglie di dati e la fascia nera che la chiude.
**Fonde** le due pagine V9.3 «architettura funzionale» e «base comune».

### 05 · Connect — sezione 1
*Produzione.* La vista di linea ricostruita: tre macchine sul turno, i fermi già
avvenuti, e l'evento in corso con la causa associata marcata in giallo. Sotto:
che cosa comprende, da dove arriva ogni dato, che cosa si configura.
**Dichiara nel piede:** vista ricostruita, dati illustrativi.
**Non dice:** i limiti di Connect. Stanno nella matrice, a pagina 08.

### 06 · Insight — sezione 1
*Produzione ed energia.* Tre famiglie di analisi, e il report di periodo come
tabella vera: quattro cause ordinate per costo stimato, con eventi, minuti e
totale. La frase di lettura: la prima causa vale il 43% del costo di fermo.
**Dichiara:** il costo è un ordine di grandezza per mettere in fila le priorità,
non un valore contabile.

### 07 · Refyn — sezione 1
*Direzione.* Le tre fasi del ciclo in colonne — priorità, azioni, verifica — e i
cinque campi che accompagnano un'azione, compresa la baseline dichiarata prima
dell'intervento. Il ritorno del ciclo è detto a parole, non disegnato.
**Marca:** modulo avanzato in sviluppo. Unica occorrenza nel dossier.

### 08 · Perimetro dei tre livelli — sezione 1
*Direzione e acquisti.* Quattordici capacità su sette aree, con Connect, Insight
e Refyn in colonna. Il valore è anche un tono: la colonna Refyn si legge più
scura di Connect prima ancora di leggere le parole.
**Marca:** le due righe di miglioramento come previste, non disponibili.

### 09 · Sorgenti, segnali e punti di misura — sezione 2
*Per l'IT.* Cinque sorgenti con quello che forniscono e dove stanno. La fascia
gialla dei segnali aggiuntivi: dove il dato non esiste o non è affidabile.
Il confine di rete in tre righe, con il rimando a pagina 11.
**Dichiara:** la sensoristica è una voce separata dal software.
**Non dice:** la configurazione di una linea specifica. Il censimento è A1.

### 10 · Modello di contesto — scura, sezione 2
*Per l'IT e produzione.* I nove attributi di ogni evento in griglia, con la causa
marcata perché è l'unico che non arriva dal campo. Quattro cose che il contesto
rende possibile.
**Formulazione vincolata:** la causa è *associata e validata*, mai «rilevata
automaticamente».

### 11 · Architettura e integrazione — sezione 2
*Per l'IT.* La pila dei quattro livelli logici, dal basso verso l'alto, con la
piattaforma marcata in giallo perché è il punto in cui il dato riceve il
contesto. A fianco: che cosa richiede, che cosa non presuppone, e cinque righe di
specifica.
**Dichiara nel piede:** schema logico, non è un disegno di rete.

### 12 · Sicurezza e ciclo di vita del dato — sezione 2
*Per l'IT.* Nove aree con il modello che il prodotto mette a disposizione.
**Reticenza voluta:** la formulazione contrattuale sulla titolarità del dato non
è pubblicata. L'area è dichiarata, il diritto va definito con il legale.
**Non dice:** i valori di progetto. Stanno in A3.

### 13 · OEE di linea — sezione 3
*Produzione.* La scomposizione di un turno a quattro gradini con la capacità
persa in giallo a ogni passaggio, e la catena di calcolo con sorgente e
validazione di ogni passaggio.
**Chiude con:** un OEE senza causa validata è un numero, non una misura.
**Non ripete:** le formule. Stanno in A4.

### 14 · Energia, costo e CO₂ — sezione 3
*Energy manager.* Sette parametri con la loro provenienza, il turno in tre
numeri con il calcolo sotto ciascuno, e la fascia gialla del risultato per mille
pezzi.
**Formulazione vincolata:** mai «costo del pezzo» quando il perimetro è la sola
energia.

### 15 · Output e integrazioni — sezione 3
*Produzione e IT.* Tre output del prodotto e due interfacce verso sistemi
esterni, tenute separate.
**Reticenza voluta:** le interfacce applicative non sono dichiarate disponibili.
È l'unica occorrenza di «da verificare» nel core.

### 16 · Delivery e pilot — scura, sezione 4
*Direzione.* Le sei fasi con che cosa fanno e il deliverable che producono, la
sesta marcata perché è la decisione del cliente. Che cosa serve dal cliente in
ogni fase, e i criteri di uscita dichiarati all'inizio.
**Non dice:** durata, partecipanti e condizioni economiche del pilot.

### 17 · Servizi e continuità operativa — sezione 4
*Acquisti.* Nove servizi raggruppati per momento — avvio, esercizio, estensione
— la struttura di prezzo in quattro voci, e tre righe di continuità operativa.
**G2 aperto:** la struttura si dichiara, gli importi no. La cella che li aspetta
è marcata, non lasciata vuota.

### 18 · Chiusura — scura
Marchio, filetto giallo, «Il passo successivo è un audit sull'impianto reale», e
i tre passaggi con gli annessi che si compilano lungo la strada.
**G1 aperto:** denominazione, referente e data compaiono solo nella working
edition.

---

## 3 · Gli annessi

Non si leggono: si compilano.

| annesso | che cos'è | quando si compila |
|---|---|---|
| **A1** · compatibilità tecnica | otto componenti da censire macchina per macchina, più i quattro esiti ammessi | audit tecnico |
| **A2** · dimensionamento | le cinque grandezze che determinano la taglia e tre fasce dichiarate | audit tecnico |
| **A3** · requisiti IT e security | otto ambiti con modello, valore di progetto e chi decide | solution design |
| **A4** · dizionario KPI | otto indicatori, ognuno con la sua formula scritta | prima del go-live |

**A1** porta una colonna in più nella working edition — «chi risponde» — che
serve a chi prepara l'audit e non a chi riceve il dossier.
**A3** è l'unica pagina del documento dove compaiono «chi decide» e il valore di
progetto: nel core quelle colonne non esistono per scelta.
**A4** non ripete i metodi di 13 e 14: li rende scrivibili.

---

## 4 · Le formulazioni vincolate

Valgono in tutto il documento e il build ne conta le occorrenze.

| si dice | non si dice |
|---|---|
| causa **associata e validata** | causa rilevata automaticamente |
| **consumo specifico**, costo **energetico** per mille pezzi | costo del pezzo |
| **modulo avanzato in sviluppo** | disponibile · in arrivo |
| **da verificare sul perimetro** (una volta sola, P15) | API disponibili |
| **ricostruzione a scopo illustrativo** | schermata del prodotto |
| **ipotesi di lavoro dichiarate** (A2) | requisiti minimi |
| perimetro **da definire in progetto** | perimetro standard |

---

## 5 · Il rapporto con il Sales Deck V9.3

Il deck resta a 1280×720 e non cambia. Le corrispondenze che devono restare
allineate:

| dossier A4 | sales deck |
|---|---|
| 08 · quattordici capacità | S12 · nove capacità nel corpo, A1 · quattordici in appendice |
| 17 · nove servizi | S12 · i nove servizi nel layer orizzontale, A2 · catalogo |
| 06 · report di periodo | S07 · dall'evento alla priorità, stesso dataset |
| 13 · scomposizione OEE | non c'è nel deck: è materia da dossier |
| 16 · sei fasi | S13 · il percorso |

Il dataset illustrativo — quattro cause, 58 eventi, 224 minuti, 15.680 € — è lo
stesso nei due documenti. Se cambia, cambia in entrambi.
