# D.Factory · ChangeLog v9.1

Dalla V9 alla V9.1. Nessuna nuova direzione grafica: palette, font, ritmo,
template e formato 1280×720 sono quelli approvati e congelati al §1.1 del piano.

---

## 1. Un difetto della V9, trovato e corretto

Il blocco contatto della CTA era **tagliato dal viewBox dell'SVG**: elemento alto
400 unità, contatto a y=428. Nel render della V9 il testo è mozzato e l'email non
c'è. Il QA non lo vedeva perché il clipping interno a un `<svg>` non è un
overflow del DOM.

Due cose fatte: il controllo `getBBox()` contro `viewBox` è entrato nella
batteria — e riverificando la V9 lo trova, un canvas su 71 — e la CTA della V9.1
è stata rifatta da zero con l'altezza reale dello spazio disponibile.

---

## 2. §3 · da 104 P0 a 58, e la priorità smette di essere un giudizio

La regola nuova: **un campo è P0 se e solo se appartiene a uno dei cinque gate**.

| Gate | Blocca | Scope | Campi |
|---|---|:--:|--:|
| G1 Identità e CTA | la pubblicazione del deck | `GLOBAL` | 9 |
| G2 Modello commerciale | la definizione completa dell'offerta | `SECTION` | 10 |
| G3 Dataset | il business case | `SECTION` | 12 |
| G4 Requisiti tecnici minimi | la dichiarazione «pronto per IT» | `SECTION` | 18 |
| G5 Evidenza commerciale | l'invio a freddo | `NONE` | 8 |
| CASE | la slide 14 | `PAGE` | 1 |

Aggiunta la colonna **`BLOCKING_SCOPE`** al registro: `GLOBAL` 9 · `SECTION` 40 ·
`PAGE` 5 · `NONE` 167.

**Il caso cliente passa da 28 P0 a uno solo**, `PH_CASE_STUDY_READY`, con gli
otto elementi del §3.2 che lo chiudono. Gli altri 53 campi scendono a `NONE`: non
bloccano nulla, sono il contenuto di una pagina già esclusa.

---

## 3. Sales Deck · le modifiche del §9

| slide | modifica | riferimento |
|---|---|---|
| 05 energia | nota «Consumo improduttivo dello stesso evento.» | §9.5 |
| 09 scelta | Refyn: «Progetto pilota dedicato, con quotazione sul perimetro» | §4.3, raccomandazione |
| 11 valore | con G3 aperto la client edition mostra **la formula e la settimana osservata**, non 309.120 € né 154.560 € | §9.11, §5.3 |
| 11 piede | «In questo scenario il valore principale nasce dalla capacità recuperabile» | §5.4 |
| 12 pilot | aggiunta la riga dei deliverable accanto ai criteri di uscita | §9.12 |
| **13 CTA** | **rientra nella client edition**, SVG rifatto, azione richiesta esplicita: «Una sessione di perimetrazione sulla prima linea» | §9.13 |
| 14 caso | governata dal solo gate `CASE_STUDY_READY` | §3.2 |
| A3 pricing | esclusa finché G2 è aperto | §9.16 |
| A4 FAQ | claim tecnici nelle formulazioni approvate al §6 | §9.17 |

La client edition del deck passa da **16 a 17 canvas**: 13 slide di corpo e 4
appendici. La numerazione torna `NN / 13` — nella V9 era stata compressa a 12
perché la CTA usciva.

### Una deviazione dichiarata · §9.15

Il piano chiede di aggiungere all'appendice servizi la colonna «incluso /
opzionale». **Non l'ho aggiunta.** `PH_SERVICES_INCLUDED` è un campo di G2: la
colonna oggi sarebbe nove righe identiche che dicono «da decidere», cioè rumore.
Entra nel momento in cui la tabella del §4.4 viene compilata. Il campo resta nel
registro e nella scheda commerciale.

---

## 4. Dossier · le modifiche del §10

| pagina | modifica | riferimento |
|---|---|---|
| titolo | resta «preliminare per assessment e solution design» | §10.1, G4 aperto |
| 02 overview | blocco esplicito «Definito nel solution design»: ambiente, sizing, protocolli, porte, autenticazione, backup, retention, integrazioni, supporto remoto | §10.2 |
| 08 architettura | titolo «Dove **risiede** e come **comunica** con la rete di stabilimento»; sottotitolo con la formulazione B della sola lettura; pannello «sola lettura, in configurazione standard»; nota con la copy sulla residenza dei dati | §6.1, §6.2, §10.8 |
| 09 contesto | dichiarato che la causa è **proposta e validata da chi la conosce**, mai rilevata automaticamente | §10.9 |
| 11 energia | dichiarato che il **perimetro della potenza a impianto fermo** si chiude nel solution design | §10.11 |

---

## 5. §6 · i tre claim tecnici

| claim | scelta | stato |
|---|---|---|
| sola lettura | **B**, come raccomanda il §6.1 | applicata a dossier 08 e deck A4 |
| residenza dati | copy prudente del §6.2 | applicata a dossier 08 |
| proprietà dati e licenza | copy del §6.3 | **non applicata** |

La terza non entra nei documenti perché il §6.3 dice «non pubblicare finché non
approvato legalmente», e nessuno l'ha approvata. Vive in
`DFactory_Decisioni_Tecniche_v9_1.md` con il suo stato. L'annesso A3 continua a
dire che cosa si decide e chi decide, che è vero oggi.

**T11 si chiude qui**: la domanda «la sola lettura è regola assoluta o
configurazione standard?» aveva la risposta nel piano stesso.

---

## 6. §14 · sei controlli che fanno fallire il build

`work_v91/accept.py` esce con codice 1 se:

1. resta un placeholder nella client edition;
2. manca la CTA, o la CTA non ha partecipanti, output e azione richiesta;
3. un valore annualizzato compare con G3 aperto;
4. il dossier si chiama «Dossier tecnico» con G4 aperto;
5. un `<image>` compare in un canvas senza essere in `assets91.py`;
6. un marcatore tecnico sorvegliato compare senza un claim nel Claim Register.

Oggi passano tutti e sei.

---

## 7. §7 · asset reali

**Zero su quattro.** Il registro `DFactory_AssetRegister_v9_1.md` ha le dieci
colonne del §7.4 e nessuna riga. Il controllo 5 del build vale anche a registro
vuoto: se domani un file entra in un canvas senza essere registrato, il build si
ferma.

---

## 8. Che cosa si può fare oggi con questi documenti

| documento | stato §13 | uso |
|---|---|---|
| **Dossier client** | **approvato come preliminare, 5/5** | si condivide con Operations, Engineering e IT/OT per preparare il solution design |
| **Deck client** | 5/10 | si presenta dal vivo; **non si invia**, perché G1 è aperto e non porta il referente |
| Dossier per IT | 0/10 | serve G4 |

Le cinque righe che mancano al deck — contatto, audit, prezzi, servizi compresi,
un asset reale — sono i due workshop del §11 e mezza giornata di raccolta asset.
Nessuna si risolve disegnando.

---

## 9. Strumenti aggiunti

| file | che cosa fa |
|---|---|
| `work_v91/gates.py` | i cinque gate come dato, con stato e formulazioni approvate |
| `work_v91/ph91.py` | il registro V9 riclassificato: priorità derivata dai gate, `BLOCKING_SCOPE` |
| `work_v91/claims.py` | Claim Register eseguibile: il build verifica che ogni marcatore tecnico abbia un claim |
| `work_v91/assets91.py` | registro asset con le dieci colonne del §7.4 |
| `work_v91/accept.py` | i sei controlli del §14 e i criteri del §13 |
| `work_v91/qa.py` | aggiunto il controllo di clipping SVG che mancava |
