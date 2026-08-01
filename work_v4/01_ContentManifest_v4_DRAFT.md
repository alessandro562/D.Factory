# 01 · Content Manifest v4 — BOZZA

Bozza di lavoro della Fase A. La versione consegnata è `DFactory_ContentManifest_v4.md`.
Questo file registra **come cambia la logica** rispetto al manifest v2 e perché.

---

## 1. Correzione della fonte di verità

Il prompt assume che l'assessment sia disponibile. **Non lo è**: nel workspace non esiste
alcun `.docx`. Esiste invece un documento non previsto e più recente,
`DFactory_Refyn_Context_Brief.md`, aggiornato al 17/07/2026, che dichiara di prevalere sui
materiali precedenti.

Nuova gerarchia applicata:

| Livello | Fonte | Uso ammesso |
|---|---|---|
| 1 | `DFactory_Refyn_Context_Brief.md` | Decisioni di brand, posizionamento, palette, guardrail di stile, contesto competitivo e regolatorio. **Non** autorizza da solo claim numerici esterni |
| 2 | HTML v2 + Content Manifest v2 | Claim, terminologia, stati, placeholder |
| 3 | Inferenze editoriali | Titoli, ordine, gerarchia, visualizzazione |
| 4 | `Marchiani_Assessment_12Marzo.docx` | **Assente.** Nessun contenuto tratto |
| 5 | Ricerca esterna | Non effettuata |

**Regola nuova, che il manifest v2 non aveva.** Una fonte interna cambia il *posizionamento*
e vieta gli errori; non promuove un numero a claim esterno. Trazione, prezzi, partnership e
tempi restano "da validare" anche quando compaiono in un documento interno autorevole.

---

## 2. Stato dei temi elencati nella Fase A2 del prompt

Gli stati ammessi dal prompt sono: `validato e pubblicabile`, `presente in fonte interna, da
validare`, `roadmap`, `non pubblicare`.

| Tema | Stato | Fonte | Motivazione |
|---|---|---|---|
| Partnership con Siemens | **non pubblicare** | nessuna | Assessment assente. Nessuna traccia in altre fonti. Un logo o una partnership dichiarata senza contratto è un rischio legale, non un vantaggio |
| Origine MES, sviluppo verso MOM | **non pubblicare** come identità | Context Brief §3 | Il brief vieta esplicitamente MES/MOM come identità di prodotto. Identità canonica: "Supervisione 4.0", "il sistema tra la linea e gli uffici" |
| Seconda generazione del prodotto | **non pubblicare** | nessuna | Assessment assente |
| Almeno 70 casi | **non pubblicare** | — | Il brief parla di ~70 **macchine** e 10 **clienti**. "70 casi" è una confusione di unità già segnalata dal brief. Da non reintrodurre in nessuna forma |
| Settori oltre Food & Beverage | **non pubblicare** | Context Brief §3 | Il posizionamento resta su linee F&B multi-linea |
| Integrazione SAP | **non pubblicare** il nome; **da verificare** la funzione | HTML v2 `d15` | Nessun nome di prodotto ERP nei documenti. Nel dossier resta "integrazione ERP · da verificare sul progetto", con la lettura oggi solo in ingresso |
| Consegna in circa 60 giorni | **non pubblicare** | nessuna | I tempi restano legati a due variabili dichiarate: sensoristica mancante e finestre di fermo |
| Pricing del caso facility management | **non pubblicare** | nessuna | Non trasferibile a linee F&B |
| Patent Box | **non pubblicare** | nessuna | Non è una prova commerciale |
| Scenari data company, big data, modelli proprietari | **roadmap**, non pubblicare | Context Brief §10 | Il brief vieta di raccontare il moat come asset di dati non provato. Il moat si racconta come radicamento operativo |
| Competitor 40 Factory | **non pubblicare** come confronto | Context Brief §8 | Zerynth, Miraitek e 40Factory **hanno** moduli di monitoraggio energetico. Una matrice competitiva che li marcasse "assente" sarebbe falsa. Nessuna matrice competitiva nei documenti v4 |

---

## 3. Temi aggiunti dal Context Brief, con stato

| Tema | Stato | Uso nei documenti v4 |
|---|---|---|
| D.Factory brand madre, Refyn modulo/servizio | vedi §4 | Conflitto aperto, registrato in OpenInputs |
| 10 clienti · ~70 macchine · ~30 linee · 24 mesi · churn 0 | **presente in fonte interna, da validare** | **Fuori** da entrambi i documenti. Il prompt lo vieta esplicitamente finché non validati |
| Ricavi ricorrenti solo sui nuovi clienti, esistenti su legacy | **presente in fonte interna, da validare** | Fuori dai documenti cliente. È politica commerciale interna |
| Prezzi indicativi per tier (2.500→5.000 ecc.) | **non pubblicare** | Il brief li dichiara ipotesi non validate. Nessun numero economico nei documenti |
| ROI ≈ €69.000/anno, payback < 6 mesi | **non pubblicare come risultato** | Non ricostruibile senza margine orario e investimento. Sostituito da un esempio con input dichiarati e aritmetica visibile |
| Sensori clamp-on (errore 1–5%) vs certificati MID | **validato e pubblicabile** | Dossier `d14`. Coerente con HTML v2. Il trade-off precisione/costo/fermo è già dichiarato |
| Air-gapped / nessuna uscita internet dalla linea | **da qualificare** | Si dichiara come perimetro architetturale previsto e concordato con l'IT, mai come proprietà assoluta |
| Omnibus I, CSRD ridotta, iperammortamento L.199/2025 | **presente in fonte interna, da validare (legale)** | **Fuori** dai documenti. Citare normativa in un deck commerciale richiede validazione legale. Registrato in OpenInputs |
| Fatturato di gruppo ~€145M, gruppo Clevertech | **presente in fonte interna, da validare** | Solo l'appartenenza al gruppo resta nel rail, come già in v2. Nessuna cifra |
| Sede Collecchio (PR) | **validato e pubblicabile** | Rail di copertina e chiusura |
| Pablo Degl'Innocenti, referente commerciale | **validato e pubblicabile** | Una sola occorrenza per documento |

---

## 4. Incongruenze del manifest v2 corrette

1. **Riga 2 della gerarchia delle fonti.** Il v2 dichiarava l'assessment "non presente" e al
   tempo stesso classificava undici claim con fonte "assessment" (C10–C16). Una fonte assente
   non può essere la fonte di un claim. In v4 quei claim hanno fonte `nessuna` e stato
   `non pubblicare`.
2. **`MAPST 4.0`.** Il v2 scrive nella terminologia "Solo nel dossier. Non compare nel sales
   deck" e poi nella tabella §2 lo assegna a `s03` del deck. La regola vince sull'assegnazione:
   **`MAPST 4.0` non compare nel sales deck v4**, in nessuna forma, nemmeno nei rail.
3. **`Refyn`.** Il v2 lo assegna a `s09` del deck come terzo blocco accanto a Connect e
   Insights, con lo stesso trattamento grafico, e contemporaneamente scrive "mai terzo livello
   di prodotto". La forma contraddiceva la regola. In v4 Refyn esce dal corpo principale del
   deck e compare solo nell'appendice sulla struttura dell'offerta, con trattamento
   tipograficamente distinto da Connect e Insights.
4. **Densità.** Il v2 fissa il budget escludendo label, dati e testo SVG, cioè escludendo la
   maggior parte del testo effettivamente presente. In v4 il conteggio include tutto il testo
   visibile; si escludono solo numero di pagina, marchio del rail e elementi `aria-hidden`.
5. **Placeholder.** Il v2 li considerava un pregio ("preservati, tutti e 17"). In v4 un
   placeholder visibile in un documento destinato al cliente è un difetto. I token spariscono
   dal deck; nel dossier diventano voci leggibili raccolte in blocchi "da definire nel solution
   design", non chip sparsi.
6. **`C57 · TÜV SÜD`.** Confermato `non pubblicare`, invariato.
7. **`C17 · intelligenza artificiale`.** Il v2 la dichiara "assente dal prodotto attuale". In
   v4 resta dichiarata assente nel dossier, con manutenzione e qualità predittive in roadmap
   senza data. Nessuna menzione nel deck: non si vende dichiarando cosa non si ha.

---

## 5. Regole di ripartizione fra i due documenti

| Contenuto | Sales deck | Dossier |
|---|---|---|
| `MAPST 4.0` | mai | `d02`, `d03` |
| Protocolli, porte, sizing, autenticazione, backup, logging | mai | `d03`, `d13`, blocco solution design |
| Nomi dei livelli Connect / Insights | appendice | `d02`, `d04` |
| Refyn | solo appendice, come servizio in definizione | `d02`, `d04` |
| Numeri di trazione | mai, finché non validati | mai |
| Caso cliente | sostituito da criteri di prova | sostituito da criteri di accettazione |
| Prezzi | mai | mai |
| RACI, milestone, SLA | mai | `d16`, `d18` |
| Metodo di misura, fattori emissivi | mai | `d11` |

---

## 6. Terminologia canonica — invariata, con tre precisazioni

Resta valida la tabella §1 del manifest v2. Tre precisazioni operative:

- **"tempo reale"** non si usa da solo. Forma ammessa: "aggiornamento ogni 5 secondi,
  storico al minuto", oppure "in turno, mentre puoi ancora intervenire". Il deck non
  promette una frequenza che il dossier non documenta.
- **"misurata sul ciclo"** si usa solo dove la misura è strumentata. Dove la ripartizione è
  calcolata, si scrive "calcolato", come già fa `d09`.
- **"nessuna uscita verso internet"** diventa "nessun flusso verso internet dalla rete di
  linea, nel perimetro concordato con il tuo IT".
