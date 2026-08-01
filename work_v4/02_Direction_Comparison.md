# 02 · Confronto fra le direzioni

Provini: `Prototype_A_contact.png` · `Prototype_B_contact.png` ·
`Prototype_A_small_contact.png` · `Prototype_B_small_contact.png` ·
`Prototype_A_hierarchy.png` · `Prototype_B_hierarchy.png`

Entrambi i prototipi passano il QA tecnico a zero violazioni: nessun overflow, nessuna
collisione, nessun errore console, nessuna richiesta di rete, corpo minimo 12 px.

| | A · parole | A · visual | B · parole | B · visual |
|---|---|---|---|---|
| cover | 57 | 79 % | 39 | 98 % |
| punto cieco | 48 | 55 % | 58 | 98 % |
| prodotto in azione | 54 | 62 % | 59 | 98 % |
| differenziazione / valore | 65 | 50 % | 63 | 98 % |
| dossier · architettura | 91 | 61 % | 119 | 98 % |
| dossier · funzionale | 133 | 38 % | 53 | 98 % |

La percentuale è misurata sull'area utile (1152 × 600), non sul canvas intero.

---

## Direzione A · Industrial signal

**Principio creativo.** Il canvas è la pagina di una rivista tecnica. Nessuna card, nessun
contenitore: l'informazione sta direttamente sul fondo, tenuta insieme da spazio bianco e
filetti. Il visual dominante è sempre una **scena nel tempo** (una linea che si ferma, due
curve che divergono, un evento che si biforca in due leve) e il giallo marca **un solo
evento per canvas**.

**Vantaggi**
- Massima libertà compositiva: ogni slide può avere una silhouette diversa, quindi dieci
  slide possono avere dieci ritmi diversi.
- Il titolo può essere grande davvero (64 px su due o tre righe) perché non è compresso in
  una colonna.
- Lo spazio negativo fa il lavoro della gerarchia: il test in scala di grigi lo supera senza
  bisogno di colore.
- È il registro più lontano dal "SaaS generico" e il più vicino a una brochure industriale.

**Rischi**
- Senza disciplina, tre slide di fila diventano "titolo in alto a sinistra + grafico sotto".
  Nel prototipo il rischio si vede già fra A2, A4 e A5.
- Regge solo se ogni slide ha una scena da mostrare. Dove la scena non c'è (offerta, FAQ,
  contatti) la direzione non aiuta e va compensata a mano.
- Il prodotto resta sullo sfondo: A3 mostra una vista, ma il linguaggio dominante è il
  diagramma, non l'interfaccia.

---

## Direzione B · Data operating system

**Principio creativo.** Il canvas è diviso una volta sola: una fascia editoriale di 336 px
e una vista di prodotto di 944 px che arriva al bordo. La vista è sempre grande, ritagliata,
con al massimo tre callout numerati. Il giallo marca **la scoperta dentro la vista**: la
barra più lunga, la riga ferma, il minuto in cui la linea si è fermata.

**Vantaggi**
- Il prodotto è enorme e credibile. Il 98 % dell'area utile è occupato dalla vista.
- La fascia è una struttura di lettura costante: l'occhio sa sempre dove trovare la tesi.
- Funziona identica su fondo scuro e chiaro, quindi il ritmo dark/light si governa senza
  cambiare impianto.
- I callout numerati legano testo e visual meglio di qualsiasi didascalia.

**Rischi**
- La fascia è rigida. Già a sei canvas si legge come un unico template con la banda che
  rimbalza da sinistra a destra. Su dieci slide diventerebbe monotona.
- La colonna da 336 px comprime i titoli: "Quando la linea si ferma, la bolletta continua"
  va su cinque righe a 40 px. La forza tipografica si perde.
- Richiede una vista di prodotto plausibile per ogni canvas. Dove non c'è (percorso, valore
  economico, call to action) la banda resta e la metà destra si svuota.

---

## Raccomandazione: ibrido, non scelta secca

**Sales deck → grammatica A, con un innesto di B.**
Il deck deve avere ritmo, e il ritmo nasce dalla varietà di silhouette. La direzione A la
consente; la B la impedisce per costruzione. Le viste di prodotto in stile B restano, ma
concentrate sulle due slide dove il prodotto è la tesi (prodotto in azione, decisioni). Il
resto del deck usa scene, non interfacce.

**Dossier → grammatica B, come impianto fisso.**
Nel dossier la rigidità della fascia è un pregio, non un difetto: diventa una colonna di
consultazione persistente che porta sezione, numero di pagina, tesi, stato e voci aperte,
mentre i 944 px restanti ospitano un solo diagramma o una sola vista grande. Un documento
tecnico si sfoglia cercando, e una struttura costante è ciò che rende possibile cercare.

**Perché questo è un ibrido reale e non cosmetico.** I due documenti finiscono con due
impianti di pagina diversi, due scale tipografiche diverse e due modi diversi di trattare il
testo secondario. Condividono palette, font, trattamento del giallo, marchio e canvas: cioè
**identità, non grammatica**, che è esattamente la separazione che il brief chiede. È anche
la correzione diretta del difetto più grave del v2, dove deck e dossier usavano lo stesso
sistema di card e matrici.

### Come cambia il sales deck

- Da 12 slide a 10 + 3 di appendice.
- Nessuna griglia di card nel corpo principale.
- Ogni slide ha una scena: turno, curva, biforcazione, propagazione, timeline.
- Tre slide cambiano natura: "La prova" diventa "Come si costruisce la prova" (criteri del
  pilot, non un caso finto); "Il business case" diventa "Le due leve" con un esempio
  ricostruibile; "L'offerta" esce dal corpo e va in appendice, perché senza prezzo non è
  un'offerta.
- Zero placeholder visibili.

### Come cambia il dossier

- 18 pagine, impianto a fascia costante.
- Le pagine funzionali (`d05`–`d10`) mostrano il prodotto grande: sono già le migliori del
  v2, qui guadagnano spazio.
- Le pagine di sezione 3 e 4, oggi otto matrici consecutive, si spezzano: un diagramma
  dominante per pagina e le voci aperte raccolte in un blocco unico "da definire nel
  solution design" invece di dodici chip sparsi.
- `d17_caso_tecnico`, oggi una pagina vuota, diventa "criteri di accettazione del pilot":
  stessa funzione, contenuto reale.

---

## Asset reali che servono per chiudere bene il lavoro

1. **Screenshot veri del prodotto**, anche con dati anonimizzati. Oggi ogni vista è una
   ricostruzione dichiarata come illustrativa. È il singolo asset che alzerebbe di più la
   credibilità di entrambi i documenti.
2. **Logo in vettoriale nero-su-trasparente e bianco-su-trasparente.** Il `.webp` fornito ha
   il fondo giallo incorporato ed è inutilizzabile: nei v4 il marchio è composto
   tipograficamente.
3. **Un caso cliente autorizzato**, con numeri prima/dopo e periodo.
4. **Durata, costo e partecipanti dell'audit.**
5. **Margine per ora di linea e forbice di investimento**, per passare da esempio a business case.
6. **Elenco protocolli e PLC verificati**, porte, sizing, autenticazione, backup, licenza.

## Slide che non possono essere davvero persuasive senza i dati mancanti

| Slide | Manca | Che cosa si è fatto |
|---|---|---|
| Prova | caso cliente autorizzato | Riscritta come criteri di prova del pilot |
| Valore economico | margine orario, investimento | Esempio con input dichiarati e aritmetica visibile, mai chiamato business case |
| Offerta | prezzo, durata, inclusioni | Spostata in appendice, senza numeri |
| Call to action | durata e costo audit | Mantenuta senza impegno economico dichiarato |
| Base installata | validazione formale | Omessa del tutto |

## Punteggi, 1–5

| Criterio | A | B | Ibrido consigliato |
|---|---|---|---|
| Gerarchia | 5 | 4 | **5** |
| Memorabilità | 4 | 5 | **5** |
| Credibilità | 4 | 5 | **5** |
| Leggibilità | 5 | 4 | **5** |
| Differenziazione | 5 | 3 | **5** |
| Scalabilità su 10 e 18 canvas | 3 | 3 | **5** |
| **Totale** | 26 | 24 | **30** |

A e B perdono entrambe sulla scalabilità, per ragioni opposte: A rischia la ripetizione
perché non ha impianto, B la rischia perché ne ha uno solo. L'ibrido assegna a ciascuna il
documento in cui il suo limite non si manifesta.
