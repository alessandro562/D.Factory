# D.Factory · Changelog v2

Revisione congiunta di sales deck e dossier tecnico. Gli originali non sono stati
toccati: `DFactory_SalesDeck.html` (14 slide) e `DFactory_DossierTecnico.html` (16
pagine) restano compilabili e invariati.

| Documento | Prima | Dopo |
|---|---|---|
| Sales deck | 14 slide | **12 slide** · `DFactory_SalesDeck_v2.html` |
| Dossier tecnico | 16 pagine | **18 pagine** · `DFactory_DossierTecnico_v2.html` |

---

## 1. Crosswalk del Sales Deck

| Prima | Dopo | Che cosa è successo |
|---|---|---|
| `s01_cover` | `s01_cover` | Titolo nuovo. La vista hero perde una dashboard e tiene stati, OEE e costo per pezzo |
| `s02_quadro` | — | **Eliminata.** La pagina di sommario denso anticipava tutto il deck. I contenuti utili sono distribuiti fra `s02` e `s03` |
| `s03_trigger` + `s04_problema` | `s02_perche_adesso` | **Unite.** Cinque trigger diventano tre, quattro silos diventano tre punti ciechi collegati alla stessa origine |
| `s05_prodotto` | `s03_come_funziona` + `s05_prodotto_in_azione` | **Divisa.** Prima la figura del flusso, poi il prodotto in funzione |
| `s06_ruoli` | `s04_tre_decisioni` | Stessa idea, struttura fissa: domanda, dato, decisione |
| `s07_prova` | `s06_prova` | Il caso cliente diventa una scheda dichiaratamente da compilare. Nessuna citazione con aspetto reale |
| `s08_perche` | `s07_perche_dfactory` | Quattro paragrafi diventano quattro micro-diagrammi. Refyn esce da questa slide |
| `s09_integrazione` | `s03` (sintesi) + dossier `d03`, `d13` | **Spostata.** Linux, porte, livelli intermedi, tag mapping, SLA e ore cliente vanno nel dossier |
| `s10_obiezioni` | `s11_faq` | Da cinque a quattro obiezioni, due frasi ciascuna, con il rimando alla pagina tecnica |
| `s11_prezzo` | `s09_offerta` | Titolo senza "e quanto": senza forbice validata non si promette un numero. Refyn perde lo stato di terzo livello |
| `s12_ritorno` | `s08_business_case` | Il risultato numerico sparisce, resta la formula per leva con gli input dichiarati |
| `s13_audit` | `s10_audit_scala` | Da tre a quattro fasi, ognuna con criterio di uscita |
| `s14_parliamone` | `s12_cta` | Una sola azione. "Dossier su richiesta" diventa un link all'allegato tecnico |

**Eliminate:** `s02_quadro`.
**Unite:** `s03_trigger` + `s04_problema`.
**Create:** nessuna slide senza antecedente; `s03` e `s05` nascono dividendo `s05_prodotto`.

## 2. Crosswalk del Dossier

| Prima | Dopo | Che cosa è successo |
|---|---|---|
| `d01_cover` | `d01_cover` | Aggiunti destinatari, perimetro, stato del documento e mini-indice cliccabile a quattro sezioni |
| `d03_capability` | `d02_architettura_prodotto` + `d04_capability` | **Divisa.** Prima la nomenclatura con gli stati, poi la matrice per dominio |
| `d02_architettura` + parte di `s09_integrazione` | `d03_architettura_tecnica` | **Unite.** Diagramma completo: sorgenti, connettori, modello dati, server, output, con le zone di rete |
| `d04_superv` | `d05_supervisione` | Aggiunti tre callout numerati: origine del dato, frequenza, decisione supportata |
| `d05_fermi` + buffer-aware da `s08_perche` | `d06_oee_fermi` | **Unite.** Il ranking delle cause affianca il diagramma macchina-polmone-linea |
| `d06_velocita` | `d07_velocita_qualita` | Aggiunti fonte, granularità e la lettura del micro-fermo |
| `d07_multi` | `d08_multi_impianto` | Invariata nella sostanza. Perimetro multi-sito dichiarato "da verificare" |
| `d08_distribuzione` | `d09_distribuzione_energia` | Aggiunti tre callout: cosa è misurato, cosa è calcolato, quale decisione abilita |
| `d09_costo` + `d10_stato` | `d10_costo_co2_stato` | **Unite.** Metà per unità prodotta, metà per stato macchina, con rimando al metodo |
| `d11_misura` | `d11_metodo_misura` | Il processo diventa sei passi. Wording su ISO, MID e Scope riscritto in forma prudente |
| `d12_brownfield` | `d12_brownfield` | Da quattro card a matrice supportato / condizionato / da verificare in audit |
| `d13_report` | `d13_deployment_security` + `d15_output_integrazioni` | **Divisa.** Il perimetro IT diventa una pagina, gli output un'altra |
| `d14_attivazione` | `d16_delivery_raci` | Otto passi, cinque milestone distinte, matrice RACI |
| `d15_sensori` | `d14_sensori` | Da due card a matrice decisionale su otto criteri. MID e ISO 50001 separati |
| caso di `s07_prova` | `d17_caso_tecnico` | **Nuova.** Lo stesso impianto letto dal lato dell'implementazione |
| `d16_chiusura` | `d18_supporto_audit` | Aggiunti supporto, severità, change request e la checklist per l'audit |

**Create:** `d17_caso_tecnico`.
**Divise:** `d03_capability`, `d13_report`.
**Unite:** `d02_architettura` con parte di `s09_integrazione`; `d09_costo` con `d10_stato`;
`d05_fermi` con il differenziatore buffer-aware.

## 3. Contenuti spostati dal deck al dossier

| Contenuto | Da | A |
|---|---|---|
| PC industriale Linux, rete isolata | `s09_integrazione` | `d13_deployment_security` |
| Porte, protocolli, flussi di rete | `s09_integrazione` | `d03`, `d13` |
| Livello intermedio verso il gestionale | `s09_integrazione` | `d03`, `d12` |
| Tag mapping in dettaglio | `s09_integrazione` | `d03`, `d12` |
| SLA e ore a carico cliente | `s09_integrazione` | `d18`, `d16` |
| Export, report, Gantt, vista 3D | `s11_prezzo`, `d13_report` | `d15_output_integrazioni` |
| Sovranità del dato e licenza | `s09_integrazione` | `d13_deployment_security` |

---

## 4. Claim riscritti per precisione

| Prima | Dopo | Perché |
|---|---|---|
| "≈ 69.000 €/anno · payback < 6 mesi" | Formula per leva, con gli input dichiarati e il risultato calcolato in audit | Non era ricostruibile senza margine orario e investimento |
| "Come si paga, e quanto" | "Come si compone l'offerta" | Senza forbice validata il titolo prometteva un numero assente |
| "Indipendentemente dalla marca", "qualsiasi protocollo" | "multi-vendor", "multi-protocollo", compatibilità verificata in audit | Nessun catalogo di compatibilità esiste |
| "Zero hardware proprietario" | "Nessun hardware proprietario D.Factory a bordo linea", con server e sensori dichiarati | Il progetto richiede comunque hardware |
| "Il dato resta tuo" | Dati sul server del cliente, con export; diritti di licenza separati e a placeholder | Dato e licenza non sono la stessa cosa |
| "2 giorni al primo dato" | first signal distinto da first usable data, pilot live e operational go-live | Due giorni non sono un go-live |
| "MID · ISO 50001" come categoria unica | Strumentazione MID e ISO 50001 separate, con la norma riferita all'organizzazione | Sono cose diverse e nessuna certifica il software |
| Refyn come terzo livello di prodotto | Servizi sul dato, opzionali, perimetro da definire | Il perimetro non è scritto |
| Citazione cliente in corsivo, senza nome | Slot marcato "da validare" con token | Una citazione anonima con aspetto reale è una citazione finta |
| Screenshot senza etichetta | Micro-etichetta "Dati illustrativi" su ogni vista dimostrativa | Non devono passare per risultati cliente |

---

## 5. Placeholder

**Preservati, tutti e 17.** Sedici restano nel deck, quattro sono condivisi con il
dossier (`PH_07`, `PH_08`, `PH_17`, `PH_18`), `PH_08_SLA` vive solo nel dossier
perché lì sta il dettaglio del supporto.

**Aggiunti, 15 token tecnici:**

`PH_T01_ARCHITETTURA_PRODOTTO` · `PH_T02_PROTOCOLLI_SUPPORTATI` ·
`PH_T03_PORTE_FLUSSI_RETE` · `PH_T04_SIZING_SERVER` · `PH_T05_AUTENTICAZIONE_RUOLI` ·
`PH_T06_BACKUP_RETENTION` · `PH_T07_UPDATE_PATCHING` · `PH_T08_LOGGING_AUDIT_TRAIL` ·
`PH_T09_SUPPORTO_REMOTO` · `PH_T10_API_FORMATI_EXPORT` · `PH_T11_METODO_FATTORI_GHG` ·
`PH_T12_CAMPIONAMENTO_DATI_MANCANTI` · `PH_T13_LICENZA_FINE_CONTRATTO` ·
`PH_T14_CASO_TECNICO` · `PH_T15_ORARI_SEVERITA_SUPPORTO`

Resi come token letterale dentro un `.chip`, oppure dentro uno `.slot` con
intestazione "da validare" e la descrizione di cosa serve. Nessun token è usato come
`href`: dove manca l'URL resta il chip.

---

## 6. Componenti CSS aggiunti

Blocco `ESTENSIONI v2.0` in coda al foglio di sistema, identico nei due documenti
perché entrambi lo inlinano dalla stessa sorgente. Solo token esistenti, filetto da
1 px, nessun raggio, nessuna ombra, nessun colore nuovo.

| Componente | Serve a | Usato in |
|---|---|---|
| `.flowline` · `__node` · `__arrow` · `__k` | Catena di nodi con frecce | `s03` |
| `.matrix` · `__h` · `--tight` | Righe di tabella senza tabella | `d02`, `d04`, `d06`…`d16` |
| `.status` · `--ok` `--opt` `--road` | Disponibile, opzionale, roadmap, con parola e peso del bordo | `d02`, `d04`, `d12`, `d15`, `s09` |
| `.stepper` · `__item` · `__n` | Passi in fila, anche cinque o otto su dodici colonne | `s10`, `d11`, `d16` |
| `.metric-strip` | Fila di numeri a pari peso | `s06` |
| `.callout` · `.callout-num` | Rimandi numerati su una vista | `d05`, `d07`, `d09` |
| `.link-card` | Rimando all'altro documento | `s03`, `s06`, `s12`, `d01`, `d15`, `d17`, `d18` |
| `.raci` | Chi esegue, approva, è consultato | `d16` |
| `.case-grid` | Scheda di caso, commerciale o tecnica | `s06`, `d17` |
| `.slot` · `__hd` · `__need` | Contenuto che il committente deve ancora fornire | `s06`, `d02`, `d17` |

**Tre correzioni al foglio**, oltre ai componenti:

1. `.slide svg text` con corpo dichiarato a 10 px. Senza, il testo dei diagrammi
   ereditava il corpo della slide e sfondava i riquadri.
2. `.stepper__n` con `min-height`. Senza, un'etichetta che va a capo faceva scendere
   il corpo di quel passo sotto quello degli altri.
3. Correzioni già introdotte nella versione precedente e qui mantenute:
   `box-sizing: border-box` sul canvas e compensazione del padding sulla card in
   evidenza su fondo chiaro.

---

## 7. Accessibilità

- `lang="it"` su entrambi i documenti
- ID unici e verificati: 12 nel deck, 18 nel dossier
- Gerarchia `h1` in copertina, `h2` per i titoli di pagina, `h3` nelle card
- Ogni SVG di diagramma ha `role="img"`, `<title>` e `<desc>`; gli SVG puramente
  decorativi restano `aria-hidden`
- Link con testo descrittivo, mai "clicca qui"
- Nessun contenuto essenziale affidato al solo colore: gli stati portano la parola
  (disponibile, opzionale, in definizione), non solo il peso del bordo
- Nessun testo sotto 9,5 px, misurato anche dentro gli SVG dove il `viewBox` scala

---

## 8. Esito del QA

Tre collaudi, tutti a zero violazioni. Il dettaglio è in
`qa/DFactory_QA_Report_v2.md`.

| Collaudo | Copre | Esito |
|---|---|---|
| `quadro/qa_deck.py` | Regole del sistema Quadro | Nessuna violazione su entrambi |
| `quadro/qa_v2.py` | Sezione 21 del brief | Tutti i controlli superati |
| `quadro/render_v2.py` | 30 PNG a 3840×2160, due provini, due PDF | Completato |

Densità misurata, escluse micro-etichette, dati e testo degli SVG:

- **Sales deck**: media 74 parole per slide, massimo 109. Obiettivo: media sotto 100,
  nessuna slide sopra 130.
- **Dossier**: media 97 parole per pagina, massimo 178. Obiettivo: media 120-190,
  nessuna pagina sopra 220.

Il dossier sta sotto la forchetta indicata: la differenza sta nelle matrici, dove il
contenuto è in celle brevi che il conteggio esclude come dati. La densità percepita a
schermo è quella di una pagina tecnica piena.

Controlli che hanno fatto emergere un difetto reale durante il lavoro:

1. **Zone sovrapposte.** Una zona senza `bottom` cresce quanto le serve e finisce
   sopra quella ancorata in basso. Nessun controllo che guardi dentro una zona sola
   può vederlo: aggiunto un confronto fra i riquadri delle zone. Trovava due
   collisioni reali su `d16` e `d18`.
2. **Corpo del testo negli SVG.** Il corpo dichiarato non è quello reso, perché il
   `viewBox` scala tutto: aggiunta la misura effettiva a schermo.
3. **Contenuto sopra il rail inferiore.** Verificato per ogni foglia di testo contro
   il riquadro del rail, non contro il bordo del canvas.

---

## 9. Limiti ancora aperti

1. **L'assessment interno non è nel workspace.** Nessun file `.docx` esiste nel
   repository né fra i materiali caricati. Tutti i temi che il brief attribuiva a
   quella fonte (Siemens, seconda generazione, settori, consegna in 60 giorni,
   pricing facility management, SAP, Patent Box) **non compaiono nei documenti** e
   sono registrati nel manifest come "fonte non disponibile". Non sono stati dedotti.
2. **La prova è una struttura vuota** in entrambi i documenti. Finché mancano
   `PH_01`, `PH_02` e `PH_T14`, il deck chiede fiducia sulla sola base installata,
   che a sua volta è "da validare".
3. **La call to action non è completa.** Senza durata, costo e partecipanti
   dell'audit, `s12` chiede un impegno senza dirne il prezzo.
4. **Il dossier non è consegnabile a un IT così com'è.** Dodici token tecnici aperti
   su deployment, rete, sicurezza e licenza: sono esattamente le domande che un
   reparto IT pone per prime.
5. **Il business case non produce un numero.** È una scelta: con il margine orario e
   l'investimento mancanti, qualsiasi risultato sarebbe inventato.
6. **I PDF in `qa/` sono materiale di verifica**, non il consegnabile. Gli HTML
   restano gli artefatti principali.
