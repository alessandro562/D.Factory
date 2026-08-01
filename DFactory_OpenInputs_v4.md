# D.Factory · Open Inputs v4

Cosa manca per portare i due documenti da "buona base di confronto" a "materiale
commerciale completo". Ordinato per impatto sulla vendita, non per facilità.

---

## 0. Il file che sbloccherebbe più cose

`Marchiani_Assessment_12Marzo.docx` esiste lato committente ma non è stato consegnato nel
workspace di lavorazione. **Consegnarlo è l'azione singola a più alto rendimento**: contiene
Siemens, l'evoluzione MES/MOM, SAP, il numero di casi, i tempi di consegna e i settori. Nessuno
di quei temi è automaticamente pubblicabile, ma con il file in mano la validazione diventa una
verifica voce per voce invece che una ricostruzione. Owner e condizioni di sblocco sono già
mappati in `DFactory_ContentManifest_v4.md` §3.

## 1. Bloccanti · senza questi il deck chiede fiducia

| # | Input | Owner | Dove sbloccherebbe | Cosa cambia |
|---|---|---|---|---|
| 1 | **Durata, costo e partecipanti dell'audit** | Commerciale | `s10_cta` | Oggi la call to action chiede un impegno senza dirne il prezzo. Con questi diventa una proposta concreta |
| 2 | **Un caso cliente autorizzato**: settore, linee, situazione di partenza, intervento, risultato, periodo | Commerciale + cliente finale | `s07`, `d17` | Oggi la prova è una logica di verifica. Con un caso reale diventa una referenza |
| 3 | **Margine per ora di linea** e **forbice di investimento** | Controllo di gestione cliente + Commerciale | `s08`, `a03` | Oggi l'esempio è ricostruibile ma illustrativo. Con questi diventa un business case |
| 4 | **Validazione formale della base installata** (10 clienti, ~70 macchine, ~30 linee, 24 mesi, 0 dismissioni) | Direzione | slide nuova o `s07` | Oggi è omessa. È la prova più economica da produrre e la più immediata da usare |
| 5 | **Screenshot reali del prodotto**, anche con dati anonimizzati | Tecnico | `s04`, `d05`, `d07`, `d08` | Oggi ogni vista è una ricostruzione dichiarata illustrativa. È il singolo asset che alzerebbe di più la credibilità |

## 2. Tecnici · senza questi il dossier non è consegnabile a un IT

| # | Input | Owner | Pagina |
|---|---|---|---|
| 6 | Elenco protocolli e modelli PLC effettivamente verificati | Tecnico | `d03`, `d12` |
| 7 | Porte e flussi di rete | Tecnico | `d03`, `d13` |
| 8 | Sizing del server per fascia di impianto | Tecnico | `d13` |
| 9 | Autenticazione, ruoli e permessi | Tecnico | `d13` |
| 10 | Backup, retention, patching, logging e audit trail | Tecnico | `d13` |
| 11 | Modalità di accesso remoto per il supporto | Tecnico | `d13`, `d18` |
| 12 | Fattori emissivi usati e loro versione; regola di campionamento e gestione dati mancanti | Tecnico | `d11` |
| 13 | API e formati di export | Tecnico | `d15` |
| 14 | Livelli di servizio, orari, severità, canali | Commerciale | `d18` |
| 15 | Ore a carico del cliente per l'avvio | Delivery | `d16` |
| 16 | Frequenza reale di aggiornamento, per qualificare i 5 secondi su tutta l'architettura | Tecnico | `d05` |

## 3. Legali

| # | Input | Owner | Nota |
|---|---|---|---|
| 17 | Diritti di licenza a fine contratto, distinti dalla proprietà del dato | Legale | `d13` lo dichiara aperto, ed è corretto che lo faccia |
| 18 | Autorizzazione all'uso di nomi di clienti | Legale + cliente | Nessun nome nei v4 |
| 19 | Formulazione validata per eventuali riferimenti normativi | Legale | Vedi §5 |

## 4. Asset di brand

| # | Input | Owner | Nota |
|---|---|---|---|
| 20 | **Logo vettoriale, nero su trasparente e bianco su trasparente** | Marketing | Il `.webp` fornito ha il fondo giallo incorporato: non si posa né su chiaro né su scuro. Nei v4 il marchio è composto tipograficamente in Geist. Funziona, ma non è il marchio |
| 21 | Dominio e link di prenotazione | Marketing | Nessun URL è stato inventato. Il deck rimanda all'indirizzo email reale |

---

## 5. Decisioni aperte, non semplici dati mancanti

### 5.1 Refyn: servizio o modulo

Le due fonti disponibili non coincidono.

- Il **Content Manifest v2** e il prompt di questo lavoro definiscono Refyn come *servizio
  sul dato in definizione, non un livello di prodotto*.
- Il **Context Brief del 17/07/2026** lo definisce *modulo di punta*, fascia alta
  "Performance", con Operator Performance Index e advisory, sul modello dei moduli
  Zucchetti.

In questo lavoro ha prevalso la regola del prompt: Refyn compare solo nell'appendice `a01`
del deck e in `d02`/`d04` del dossier, sempre come servizio in definizione, tipograficamente
distinto da Connect e Insights.

**Va deciso**, perché cambia la struttura dell'offerta: se Refyn è un modulo, `a01` diventa
una scala a tre livelli; se è un servizio, resta una riga separata sotto i due livelli.

### 5.2 Quadro normativo

Il Context Brief indica che la narrativa "perché ora" dovrebbe riflettere l'Omnibus I di
marzo 2026 (scope CSRD ridotto) e la sostituzione di Transizione 5.0 con
l'iperammortamento (L.199/2025).

**Nei v4 non compare nessun riferimento normativo.** Citare norme in un documento
commerciale è un claim che richiede validazione legale e invecchia in fretta. La slide
`s02` costruisce l'urgenza sul dato operativo (l'energia consumata durante un fermo), che
non ha scadenza.

Se si vuole aggiungere una slide sul contesto normativo, serve una formulazione validata da
chi risponde di quel testo.

### 5.3 Il caso cliente e la sua doppia lettura

Il v2 prevedeva lo stesso impianto raccontato due volte: `s06` commerciale, `d17` tecnico.
La struttura era pronta e vuota in entrambi. Nei v4 le due pagine hanno cambiato funzione
(criteri di prova e criteri di accettazione) e **funzionano da sole**.

Quando il caso arriverà, la decisione da prendere è se sostituire quelle due pagine o
aggiungerne due. Il consiglio è **aggiungerne due**: i criteri di accettazione sono
contenuto utile anche in presenza di una referenza, perché è quello che un capo
manutenzione chiede subito dopo.

### 5.4 L'esempio economico di `s08`

I valori usati (4.000 h/anno · 3 punti di OEE · 250 €/h · 180.000 €/anno · 22 % · 25 %)
sono stati scelti per rendere l'aritmetica verificabile a mente, non presi da un impianto
reale. Sono dichiarati come tali sulla slide e dettagliati in `a03`.

**Va validato commercialmente** che le forbici siano plausibili per una linea F&B tipo. Se
non lo sono, l'esempio va ricalibrato: un esempio non plausibile è peggio di nessun esempio,
perché il primo a notarlo è il controllo di gestione del cliente.

---

## 6. Cosa è stato deliberatamente omesso, e perché

| Contenuto | Perché non c'è |
|---|---|
| 10 clienti · ~70 macchine · ~30 linee · 24 mesi · 0 dismissioni | Non validati formalmente. Il prompt lo vieta esplicitamente |
| Siemens, SAP, Patent Box, 70 casi, consegna in 60 giorni, settori oltre F&B | **Presenti nell'assessment interno, non validati per l'uso esterno.** Il file non è stato consegnato nel workspace, quindi non è stato letto: i temi restano "da validare" con owner assegnato, vedi manifest §3 |
| Qualsiasi importo, forbice o listino | Il Context Brief li dichiara ipotesi non validate |
| ROI ≈ 69.000 €/anno, payback < 6 mesi | Non ricostruibile senza margine orario e investimento |
| Matrice competitiva | Zerynth, Miraitek e 40Factory hanno moduli di monitoraggio energetico: una matrice che li marcasse "assente" sarebbe falsa |
| Citazioni cliente | Nessuna autorizzata |
| Loghi di terzi | Nessuno autorizzato |
| Riferimenti normativi | Vedi §5.2 |
