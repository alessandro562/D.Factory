# D.Factory · Final Review Checklist V9.3

Da leggere prima di usare i due documenti con un cliente. Ogni riga è
verificata: dove c'è una crocetta, il controllo è automatico e fallisce il
build; dove c'è un rombo, è un giudizio e serve una persona.

---

## 1. Livello dichiarato

| livello | stato | che cosa significa |
|---|:--:|---|
| **narrative ready** | ✅ | il Sales Deck racconta il prodotto, la trasformazione e il valore prima di mostrare l'interfaccia, e la sequenza regge i criteri del §16 |
| **assessment ready** | ✅ | il Dossier è utilizzabile per un assessment e un solution design: descrive metodo, architettura e perimetro |
| **commercial ready** | ❌ | G1 e G2 aperti: manca il referente e mancano gli importi |
| **IT-ready** | ❌ | G4 aperto: gli annessi raccolgono requisiti, non li dichiarano |

Il livello non è dedotto: è calcolato da `accept93.py` dallo stato dei gate e
dai criteri del §16.

---

## 2. Sales Deck · criteri del §16

| criterio | esito | verifica |
|---|:--:|---|
| prodotto chiaro entro S03 | ✅ | S03 dice che cos'è D.Factory in 46 parole |
| trasformazione chiara in S04 | ✅ | cinque coppie prima/dopo in corrispondenza uno-a-uno |
| massimo tre slide fortemente UI | ✅ | tre: S05, S06, S01 come sfondo |
| pacchetti funzionali e distinti | ✅ | tre fondi, tre trattamenti del risultato, nessuna struttura duplicata |
| confronto leggibile | ✅ | matrice a nove righe nel corpo, corpo 16 px |
| servizi visibili | ✅ | nove servizi su S12, catalogo completo in A2 |
| ragione per scegliere D.Factory | ✅ | tre principi su S13, senza numeri non verificati |
| modello commerciale | ✅ | avvio, ricorrente, opzionale su S14 |
| CTA | ✅ | S15 con perimetrazione, pilot, decisione |
| ritmo variato | ✅ | nessun fondo ripetuto tre volte di fila nel corpo |
| nessun eccesso tecnico | ✅ | quattro slide narrative in apertura, due tecniche consecutive |

---

## 3. Dossier · criteri del §16

| criterio | esito | verifica |
|---|:--:|---|
| executive summary autorevole | ✅ | P02, con le correzioni di contrasto e corpo del §2.1 |
| prosa in ogni pagina core | ✅ | 16 su 16, fra 45 e 100 parole |
| moduli spiegati | ✅ | P05, P06, P07 con tre layout diversi |
| matrice completa | ✅ | quattordici righe per area su P08 |
| acquisizione e contesto distinti | ✅ | P09 le sorgenti, P10 il modello |
| architettura e deployment distinti | ✅ | P03 la catena funzionale, P11 i livelli logici |
| security nel core, requisiti in annesso | ✅ | P12 le aree, A3 i valori |
| OEE ed energia metodologicamente chiari | ✅ | P13 e P14, con catene aritmetiche verificabili |
| output e integrazioni separati | ✅ | due tavole distinte su P15 |
| delivery e supporto spiegati | ✅ | P16 le sei fasi, P17 i servizi |
| nessun tono da questionario | ✅ | zero «chi decide» e zero «owner» nel core |

---

## 4. Verifiche tecniche

| controllo | esito |
|---|:--:|
| zero richieste di rete sui quattro documenti | ✅ |
| zero errori di console | ✅ |
| zero id duplicati, zero ancore rotte | ✅ |
| zero overflow del canvas | ✅ |
| zero collisioni fra blocchi | ✅ |
| zero contenuti tagliati dal `viewBox` | ✅ |
| corpo minimo rispettato su tutte le popolazioni | ✅ |
| zero placeholder visibili nelle client edition | ✅ |
| zero testo interno nelle client edition | ✅ |
| font incorporati, canvas 1280×720 | ✅ |

---

## 5. Verifiche di contenuto

| controllo | esito |
|---|:--:|
| nessun valore annualizzato con G3 aperto | ✅ |
| nessun claim tecnico fuori registro | ✅ |
| nessuna delle 14 formulazioni vietate dal §12 | ✅ |
| «in sviluppo» una sola volta per documento | ✅ |
| MAPST e MarEnergy fuori dal corpo del deck | ✅ |
| nessun asset non registrato | ✅ |
| titolo del dossier «preliminare» con G4 aperto | ✅ |
| aritmetica dello scenario rifatta a mano | ✅ · 14 verifiche nel QA Report |

---

## 6. Quello che serve una persona

| verifica | chi | perché non è automatica |
|---|---|---|
| ◆ lo scenario illustrativo è plausibile per il cliente che riceverà il deck | commerciale | 500 pz/min e 0,14 €/pz vengono da una linea tipo. Su una linea molto diversa i numeri sembrano sbagliati anche se sono dichiarati illustrativi |
| ◆ la promessa di S01 è quella giusta per questo cliente | commerciale | «Dalla linea al margine» funziona con chi ha un problema di costo, meno con chi ha un problema di servizio |
| ◆ le funzioni elencate esistono davvero come descritte | prodotto | il perimetro dei tre livelli è dichiarato, non verificato riga per riga contro il backlog |
| ◆ Refyn è descritto come qualcosa che si può vendere oggi | prodotto e commerciale | è marcato «modulo avanzato in sviluppo» una volta per documento, e si attiva via pilot dedicato. Se la disponibilità cambia, cambia S11 e P07 |
| ◆ le tre fasce di dimensionamento sono ordini di grandezza sensati | engineering | sono ipotesi dichiarate, e il cliente le leggerà come ipotesi solo se lo sono |
| ◆ la formulazione su titolarità ed export a fine contratto | legale | non è pubblicata: A3 dichiara l'ambito e rimanda. Va scritta prima che qualcuno la chieda |

---

## 7. Prima di mandare il deck

1. **Non si manda.** G1 è aperto: la client edition non porta il referente e il
   build emette un warning globale. Il deck si presenta dal vivo.
2. Se lo si presenta, S05 e S06 sono ricostruzioni: dirlo a voce, non lasciare
   che lo dica solo il piede pagina.
3. S14 mostra il modello, non gli importi. Se qualcuno chiede un numero, la
   risposta è che si calcola sui suoi dati durante l'audit — ed è vero, non è
   una scappatoia.
4. Il caso cliente non esiste. Se qualcuno chiede referenze, la risposta è che
   non ce ne sono di pubblicabili.

## 8. Prima di mandare il dossier

1. Si può mandare. È preliminare e lo dichiara in copertina.
2. Gli annessi A1, A2 e A3 sono moduli da compilare insieme all'IT del cliente:
   mandarli come se fossero specifiche li fa sembrare incompleti invece che
   aperti.
3. P15 non dichiara disponibile un'interfaccia applicativa. Se il cliente ha già
   un'integrazione in mente, quella conversazione comincia da lì.
