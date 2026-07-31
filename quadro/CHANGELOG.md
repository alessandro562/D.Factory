# Sales deck e dossier tecnico sul sistema "Quadro"

I due documenti sono stati ricomposti da zero sul sistema di design fornito. Il
**contenuto resta quello validato** con la revisione precedente: narrativa, claim,
guardrail e i 17 placeholder aperti non cambiano. Cambia la forma.

Sorgenti in `quadro/src/`, foglio di sistema in `quadro/dfactory-system.css`,
documenti compilati alla radice del repo.

```bash
python3 quadro/build.py                                   # i due HTML
python3 quadro/qa_deck.py DFactory_SalesDeck.html         # collaudo di sistema
python3 quadro/qa_deck.py DFactory_DossierTecnico.html
python3 quadro/qa_content.py                              # contenuto, stile, contenitori
python3 quadro/render.py --contact-sheet                  # PNG + provino, senza PDF
```

---

## Sales deck · 14 slide

| # | id | Archetipo | Fondo | Nota |
|---|---|---|---|---|
| 01 | `s01_cover` | T0 copertina | scura | Timeline in `zone--hero`, titolo e OEE ancorati |
| 02 | `s02_quadro` | T8 tabella | chiara | Cinque righe, `lbl` in `.c3` e corpo in `.c9` |
| 03 | `s03_trigger` | T3 colonne | chiara | Cinque trigger, il primo in `colr--acc` |
| 04 | `s04_problema` | T3 colonne | chiara | Quattro dati che esistono già, fascia di chiusura |
| 05 | `s05_prodotto` | T4 strumentale | scura | Gauge OEE e costo per vettore, ponte lessicale in `.note` |
| 06 | `s06_ruoli` | T5 canali | chiara | Tre pannelli pari, nessun accento: i tre ruoli non hanno gerarchia |
| 07 | `s07_prova` | T6 prova | chiara | Primo momento editoriale, citazione in `t-ed` |
| 08 | `s08_perche` | T3 colonne | scura | Quattro differenziatori, gruppo e Refyn in coda |
| 09 | `s09_integrazione` | T3 colonne | chiara | Unica costruzione "Non X. Y." di tutto il documento |
| 10 | `s10_obiezioni` | T9 obiezioni | chiara | Cinque pannelli, 3×`.c4` e 2×`.c6`, nessun accento |
| 11 | `s11_prezzo` | T5 canali | chiara | Tre livelli, il terzo in `panel--accent`, fascia condizioni sotto |
| 12 | `s12_ritorno` | T2 statement | scura | Secondo momento editoriale, il metodo dei quattro numeri resta |
| 13 | `s13_audit` | T7 processo | chiara | Audit, pilota, kickoff, poi i campi operativi dell'audit |
| 14 | `s14_parliamone` | T10 chiusura | scura | Contatto, prenotazione, rimando al dossier |

Ritmo `S C C C S C C S C C C S C S`, massimo tre chiare consecutive.

## Dossier tecnico · 16 slide

| # | id | Archetipo | Fondo | Nota |
|---|---|---|---|---|
| 01 | `d01_cover` | T0 ridotta | scura | Senza timeline: destinatario e scopo |
| 02 | `d02_architettura` | T3 | scura | Quattro sorgenti, un solo modello dati |
| 03 | `d03_capability` | T3 | chiara | MAPST 4.0, la colonna roadmap marcata "non disponibile oggi" |
| 04 | `d04_superv` | T4 | scura | Supervisione di linea, timeline stati |
| 05 | `d05_fermi` | T4 | scura | Fermi per causa, Pareto in `.barh` |
| 06 | `d06_velocita` | T4 | scura | Velocità e qualità, area chart in `.spark` |
| 07 | `d07_multi` | T4 | scura | Venti macchine in `.tl--dense`, due righe in evidenza |
| 08 | `d08_distribuzione` | T4 | scura | Diagramma di flusso energia, SVG dedicato |
| 09 | `d09_costo` | T4 | scura | Costo e CO₂ per pezzo, `.barh` per vettore |
| 10 | `d10_stato` | T4 | scura | Energia per stato macchina, colonne impilate in `.cols` |
| 11 | `d11_misura` | T3 | chiara | Misurata non stimata, Scope 1-2, ISO 50001 |
| 12 | `d12_brownfield` | T5 | chiara | Macchine e protocolli misti, tre pannelli e fascia |
| 13 | `d13_report` | T3 | **scura** | Export e sovranità del dato |
| 14 | `d14_attivazione` | T7 | chiara | Quattro passi in colonna, il quinto nella fascia |
| 15 | `d15_sensori` | T5 | chiara | Clamp-on e certificati, due pannelli da `.c6` |
| 16 | `d16_chiusura` | T10 ridotta | scura | Riferimento tecnico e rimando al sales deck |

Ritmo `S S C S S S S S S S C C S C C S`. La 13 è scura per necessità: senza,
le posizioni 11-15 farebbero cinque chiare consecutive e il collaudo fallirebbe.

**Budget giallo del dossier: 2 ruoli per slide** invece di 3. Su fondo scuro il
punto del marchio ne consuma già uno, quindi resta spazio per la sola serie dati.
Verificato da `qa_content.py`, che i ruoli li conta come `qa_deck.py`.

---

## Modifiche al foglio di sistema

Tutte in coda, marcate come estensioni. Stesso linguaggio: filetto da 1px, nessun
raggio, nessuna ombra, nessun colore nuovo fuori dalla scala già presente.

**Una correzione di base.** Il foglio non dichiarava `box-sizing`. Un `.panel` con
`height:100%` misurava quindi 100% **più** 40px di padding e 2px di bordo, e usciva
dalla zona di 42px esatti finendo sopra il rail inferiore. Riguardava dieci slide e
anche il reference fornito. `box-sizing:border-box` su tutto il canvas.

**Un allineamento.** Su fondo chiaro la card in evidenza porta un filetto superiore
da 3px invece che da 1: due pixel che facevano scendere la sua intestazione sotto
quelle delle card accanto. Il filetto resta, il padding lo compensa.

**Quattro componenti nuovi**, per le viste di prodotto native:

| Componente | Serve a |
|---|---|
| `.tl--dense` | Venti macchine in una schermata: riga a 9px, nome a quota fissa |
| `.spark` | Contenitore per grafici SVG inline, area e trend |
| `.cols` | Colonne impilate, l'orizzontale di `.barh` ruotato |
| `.flow` | Diagramma di flusso dell'energia |
| `.key` | Legenda di serie, con tassello `.sw-acc` per l'accento |

**Tre inversioni d'accento**, dove il giallo pieno riempiva invece di indicare:

- `.tl--dense` · su venti righe il tempo in marcia in giallo diventa un muro. La
  serie resta neutra e l'accento va solo sulle righe che la lettura chiama in
  causa, con `.tl__row--acc`.
- `.cols--fermo` · la vista dell'energia per stato parla del consumo a macchina
  ferma: l'accento sta lì, non sul tempo in marcia. È anche la quota più piccola.
- Diagramma di flusso · un solo soggetto in giallo, il nastro che assorbe di più.
  Il fotovoltaico è tornato neutro, ha già la sua lettura a sinistra.

---

## Collaudo

`qa_deck.py`, regole non toccate, aggiunto solo `executable_path` perché in questo
ambiente il chromium di sistema va indicato: **nessuna violazione** su entrambi.

`qa_content.py`, scritto per questa consegna: struttura, contenuto, placeholder,
stile della prosa, chiamate a CDN, contenitori interni e budget giallo del dossier.
**Tutti i controlli superati.**

Il controllo sui contenitori è la parte che `qa_deck.py` non copre: quello verifica
il canvas 1280×720, questo verifica che niente esca da un pannello o da una zona.
È il controllo che ha fatto emergere il problema del `box-sizing`.

---

## Placeholder ancora aperti

Diciassette, invariati, resi come token letterale dentro un `.chip`. Nessuno è stato
riempito con dati dedotti.

`PH_01_CASO_CLIENTE` · `PH_02_CITAZIONE_CLIENTE` · `PH_03_FORBICE_PREZZO` ·
`PH_04_AUDIT_DURATA` · `PH_05_AUDIT_COSTO` · `PH_06_AUDIT_PARTECIPANTI` ·
`PH_07_ORE_CLIENTE` · `PH_08_SLA` · `PH_09_CONTRATTO` · `PH_10_REVERSIBILITA` ·
`PH_11_AGEVOLAZIONE` · `PH_12_COSTO_SENSORI` · `PH_13_TOYOTA` · `PH_15_ACMI_OK` ·
`PH_16_MARGINE_ORA` · `PH_17_DOMINIO` · `PH_18_BOOKING`

I tre più urgenti restano `PH_04`, `PH_05` e `PH_06`: finché mancano durata, costo
e partecipanti dell'audit, la chiamata all'azione non è completa.

`PH_14_TUV` non compare: la riga sulla certificazione era troppo vaga senza la norma
esatta ed è stata rimossa invece che flaggata.

---

## PDF

Sospeso. `render.py` lo genera solo con `--pdf`, sui documenti approvati:

```bash
python3 quadro/render.py --pdf
```
