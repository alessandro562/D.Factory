# D.Factory · Open Inputs V9.3

Che cosa manca, chi lo può chiudere, che cosa si sblocca quando è chiuso.

**Cinque gate aperti su cinque, più il caso cliente.** Nessuno è cambiato dalla
V9.2: la Fase E ha riscritto i documenti, non ha ottenuto informazioni.

---

## 1. I sei blocchi, in ordine di impatto

### G1 · Identità e CTA · `BLOCKING_SCOPE: GLOBAL`

**Che cosa manca** · denominazione legale, referente, ruolo, email, e i cinque
campi che descrivono l'audit: nome, durata, partecipanti, input, deliverable.

**Effetto oggi** · il blocco contatto di S15 esiste solo nella working edition.
Nella client edition esce, e il build emette un warning globale: **il deck si
presenta dal vivo, non si invia da solo.** La copertina del dossier dice che
denominazione, referente e data si compilano prima dell'invio.

**Chi lo chiude** · direzione commerciale. È l'unico gate che si chiude senza
lavoro tecnico: sono quattro righe di anagrafica.

**Che cosa si sblocca** · il deck diventa inviabile. È il passo con il rapporto
sforzo/risultato più alto dei sei.

---

### G2 · Modello commerciale · `SECTION`

**Che cosa manca** · dieci importi: audit, setup della prima linea, canone base
per sito, canone Connect, canone Insight, linee successive, modello di prezzo
Refyn, supporto premium, durata contrattuale, condizioni di rinnovo. Più la
distinzione fra servizi compresi nell'avvio e servizi opzionali.

**Effetto oggi** · l'appendice A3 del deck non entra nella client edition, e le
appendici si rinumerano. S14 mostra il **modello** — avvio, ricorrente,
opzionale — e non gli importi. A2 dice «in proposta» su tutte e nove le righe.

**Chi lo chiude** · direzione commerciale, con il controllo di gestione.

**Che cosa si sblocca** · A3 entra nella client edition, A2 dice davvero che
cosa è compreso, S14 può portare un ordine di grandezza.

---

### G3 · Dataset · `SECTION`

**Che cosa manca** · la validazione dei dieci parametri dello scenario: cadenza
nominale, margine unitario, potenza in marcia, potenza a impianto fermo, prezzo
dell'energia, fattore di emissione, settimane produttive, durata del turno,
turni all'anno, quota di perdita recuperabile. Serve un nome, una data e una
firma: non valori nuovi, la conferma che quelli sono plausibili.

**Effetto oggi** · nessun risultato annualizzato viene pubblicato, né in cifre
né in lettere, nemmeno nel testo alternativo delle figure — è una condizione di
build. L'appendice A5 resta fuori dalla client edition. S14 mostra la formula e
dice che il risultato si calcola sui dati del cliente durante l'audit.

**Chi lo chiude** · chi conosce una linea reale di riferimento, con il
contratto di fornitura dell'energia alla mano.

**Che cosa si sblocca** · il business case. È il gate che vale di più
commercialmente e costa meno tecnicamente.

---

### G4 · Requisiti IT e OT · `SECTION`

**Che cosa manca** · modello di deployment, sistemi operativi supportati, porte
richieste, politica di sola lettura, protocolli e versioni supportate,
requisiti di gateway, CPU, RAM, storage, retention, RPO, RTO, modello di
autenticazione, modello dei ruoli, logging, cifratura a riposo, politica di
backup, politica di patching, titolarità dei dati, export a fine contratto.

**Effetto oggi** · il dossier si presenta come **preliminare** — è una
condizione di build — e gli annessi A1, A2 e A3 sono moduli di raccolta, non
dichiarazioni. A2 pubblica le fasce di dimensionamento come ipotesi dichiarate e
lascia CPU, RAM e storage «da definire in audit». Le due righe su titolarità e
fine contratto rimandano al legale.

**Chi lo chiude** · engineering di prodotto per i primi otto campi, IT del
cliente per l'ambiente, legale per le ultime due righe.

**Che cosa si sblocca** · il dossier diventa **IT-ready** e può essere
sottoposto a un ufficio IT come documento di riferimento, non come base di
discussione.

---

### G5 · Evidenza commerciale · `NONE`

**Che cosa manca** · zero asset reali consegnati. Il registro degli asset ha
dieci colonne e nessuna riga. Servirebbero, in ordine: uno screenshot MAPST 4.0,
uno MarEnergy, un report reale anonimizzato, uno schema di linea, uno screenshot
della nuova interfaccia, una foto di un punto di misura.

**Effetto oggi** · ogni vista di prodotto dei due documenti è una ricostruzione
grafica e lo dichiara nel piede. Su S13 non compare nessun numero aziendale:
niente anno di fondazione, niente progetti completati, niente rapporto con il
gruppo. La slide regge sui tre principi.

**Chi lo chiude** · chi ha accesso agli ambienti reali e può autorizzare per
iscritto l'uso di uno screenshot anonimizzato.

**Che cosa si sblocca** · la differenza fra «vi facciamo vedere come sarebbe» e
«ve lo facciamo vedere». È il gate che cambia di più la credibilità del deck e
l'unico che questa Fase E non ha potuto compensare in alcun modo.

---

### CASE · Caso cliente · `PAGE`

**Che cosa manca** · tutto. Nome utilizzabile, settore, tipo di linea, problema
iniziale, periodo di baseline, intervento, durata del pilot, risultati con
metodo di misura, citazione autorizzata, limiti dichiarati della misura,
autorizzazione scritta.

**Effetto oggi** · `s16_caso` esiste nella sola working edition e mostra quali
campi servono, non un caso. Nessun risultato cliente è pubblicato da nessuna
parte nei due documenti.

**Chi lo chiude** · un cliente disposto a firmare.

---

## 2. Riepilogo

| gate | scope | campi aperti | canvas esclusi dalla client edition |
|---|:--:|--:|---|
| G1 identità e CTA | GLOBAL | 9 | nessuno · blocco contatto e warning globale |
| G2 modello commerciale | SECTION | 10 | `a3_pricing` |
| G3 dataset | SECTION | 10 | `a5_assunzioni` |
| G4 requisiti IT/OT | SECTION | 20 | nessuno · il dossier resta preliminare |
| G5 evidenza | NONE | 6 asset | nessuno · tutte le viste sono dichiarate ricostruzioni |
| CASE caso cliente | PAGE | 20 | `s16_caso` |

---

## 3. Se se ne potesse chiudere uno solo

**G1.** Sono quattro righe di anagrafica e trasformano un documento che si
presenta in un documento che si manda. Nessuno degli altri cinque ha lo stesso
rapporto fra sforzo richiesto e vincolo rimosso.

**Se se ne potessero chiudere due:** G1 e G5. Il primo rende il deck inviabile,
il secondo lo rende credibile.
