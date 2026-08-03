# D.Factory · Change Log V9.3 · Fase E

Che cosa è cambiato dalla V9.2, canvas per canvas, e perché. Le voci marcate
**D2** applicano una correzione obbligatoria del §17 del Fase E Build Master.

---

## 1. Il cambiamento di fondo

La V9.2 chiudeva due documenti tecnicamente corretti e narrativamente
sbilanciati: entrambi si comportavano da documentazione. Il Sales Deck aveva
quattro slide di prodotto prima di aver detto che cos'era il prodotto, e il
Dossier aveva una pagina su quattordici con un paragrafo di prosa.

La V9.3 non ha ritoccato: ha riscritto il corpo di tutti e due. Sono rimasti la
palette, il canvas, i font e i gate. Sono cambiati l'ordine, il peso, il numero
di canvas e la regola con cui si misura la densità.

| | V9.2 | V9.3 |
|---|--:|--:|
| Sales Deck · canvas working | 19 | 21 |
| Sales Deck · canvas client | 16 | 18 |
| Dossier · canvas | 18 | 21 |
| slide narrative in apertura | 1 | 4 |
| pagine core del dossier con paragrafo | 1 su 14 | 16 su 16 |
| regola del 55–70% su ogni canvas | attiva | **rimossa** |

---

## 2. Sales Deck

| canvas | azione | che cosa cambia |
|---|---|---|
| `s01_promessa` | riscritto | la vista di turno scende a prova di sfondo, la headline domina il terzo superiore. Nella V9.2 la vista competeva con il titolo |
| `s02_problema` | nuovo | tre fratture funzionali al posto dell'elenco di sorgenti tecniche. Nessuna dashboard |
| `s03_visione` | nuovo | quattro stazioni editoriali: segnali → contesto → evidenza → decisione. È la slide che risponde alla domanda «che cos'è» entro la terza |
| `s04_trasformazione` | nuovo · **D2** | non esisteva nella V9.2. Cerniera nero/bianco, cinque coppie in corrispondenza uno-a-uno, corpo delle coppie +28% rispetto al prototipo D1 |
| `s05_prodotto` | mantenuto | la vista di `v04_evento_prodotto` resta invariata nella sostanza. Cambia la headline e la posizione nella sequenza: non è più la seconda slide, è la quinta |
| `s06_quattro_letture` | fuso | `v05_energia` + `v07_ampiezza` diventano una slide sola: una timeline, un imbuto che dichiara che la fascia inferiore è quell'intervallo, quattro letture. Non due dashboard sovrapposte |
| `s07_priorita` | riscritto | da slide di prodotto a slide di **valore**: titolo e paragrafo dominano, il ranking sta sotto ed è un grafico, non una schermata. È così che le slide tecniche consecutive restano due |
| `s08_mappa` | nuovo | cinque fasce editoriali. La quinta area porta il rimando a S11 e non ripete «in sviluppo» |
| `s09` `s10` `s11` | dai prototipi D2 | tre fondi diversi — bianco, grigio chiarissimo, nero — e tre trattamenti diversi della fascia risultato. Nessuna vista di prodotto: è una condizione di build |
| `s12_confronto` | riscritto | la matrice sale dall'appendice al corpo, nove righe, corpo 16 px. I nove servizi diventano un layer orizzontale sotto |
| `s13_perche` | riscritto | tre principi numerati. Escono la timeline e l'asse produzione/energia: quella lettura vive già su S05 e S06 |
| `s14_valore` | fuso | quattro leve e formula a sinistra, modello commerciale a destra. Una sola formula economica nel corpo |
| `s15_pilot_cta` | fuso | `v12_pilot` + `v13_cta`. Tre passi in sequenza, nessuna seconda dashboard |
| `a1_matrice` | riscritto | da otto a quattordici righe, organizzate per area |
| `a2_servizi` | riscritto | cinque colonne: la colonna «che cosa comprende» è nuova |
| `a3_pricing` | mantenuto | invariato nella sostanza, corpo minimo portato a 14 px |
| `a4_faq` | riscritto | sei domande **commerciali**. Le due domande IT — residenza dei dati e integrazione con il gestionale — migrano nel dossier, pagine 11 e 15 |
| `a5_assunzioni` | mantenuto | la formula annuale diventa «perdita di una causa = minuti osservati × margine al minuto», coerente con S14 e con G3 aperto |
| `s16_caso` | mantenuto | rinominato da `v14_caso`, resta fuori dalla client edition |

### 2.1 Due scostamenti dallo storyboard, dichiarati

**S07 scrive «38 eventi», non «trentotto eventi».** Lo storyboard scriveva il
numero in lettere; la tabella immediatamente sotto scrive 38. Due grafie dello
stesso numero a quattro centimetri di distanza si leggono come due dati.

**S12 è dichiarata di tipo `matrice`, non `pacchetto`.** Il tetto di superficie
visiva del tipo `pacchetto` è il 35%, calibrato sulle tre slide che non portano
tabelle. Una matrice a nove righe ne occupa il 45%. Il tipo `matrice` esiste per
questo, con tetto 60%: la slide resta nella famiglia dei pacchetti e ha la
soglia della sua forma.

---

## 3. Dossier tecnico

| canvas | azione | che cosa cambia |
|---|---|---|
| `p01_cover` | riscritto | destinatari su una riga discreta invece di sei reparti in evidenza. Indice aggiornato a 17 pagine |
| `p02_executive` | **D2** | prosa da `--d2` a bianco all'86%, corpo da 17 a 17,5 px, i tre principi guadagnano peso, la sezione attiva della navigazione passa a 700 e riceve un marcatore sulla riga dell'header |
| `p03_architettura_funzionale` | nuovo | cinque stazioni con frase di lettura, legenda e conclusione. Non duplica P11: qui la catena funzionale, lì i livelli logici |
| `p04_base_comune` | riscritto | quattro colonne su una fascia continua. Esiste perché le tre pagine dei moduli non ripetano le stesse funzioni |
| `p05_connect` | **D2** | la configurazione esce dalle quattro colonne e diventa una fascia tecnica finale; restano tre capability; il visuale cresce dell'8% (272 → 294 px); la causa associata è evidenziata; la dicitura di ricostruzione ha più contrasto. «Limiti» passa alla matrice P08 |
| `p06_insight` | riscritto | tre famiglie a sinistra, un report a destra. Layout diverso da P05 di proposito |
| `p07_refyn` | riscritto | ciclo a tre nodi con ritorno. Terzo layout diverso in tre pagine consecutive |
| `p08_matrice` | nuovo | quattordici righe per area. Passo di griglia `tb--dense` a 28 px per riga: era l'unico modo di tenere quattordici righe e un paragrafo dentro il canvas |
| `p09_acquisizione` | riscritto | schema generico con confine di rete. **La tabella Riempitrice/Etichettatrice/Tappatrice della V9.2 esce dal core**: anche dichiarata come esempio continuava a leggersi come la configurazione standard del prodotto. Il modello di censimento vive nell'annesso A1 |
| `p10_contesto` | riscritto | evento in testa, nove attributi in griglia. Non una timeline: quella lettura è già su P05 e nel deck. È l'unica pagina scura della sezione 2 |
| `p11_architettura` | **D2** | livello 4 → «Output e sistemi esterni» con divisione visiva fra output e sistemi a valle · «Buffer» → «Accodamento e persistenza temporanea» · «Motore KPI» → «Elaborazione KPI» · frecce più spesse · più contrasto sui livelli 1, 2 e 4 · la nota sulla sola lettura diventa nota tecnica |
| `p12_security` | nuovo | nove aree in griglia. Valori di progetto, chi decide e owner stanno in A3 |
| `p13_oee` | riscritto | scomposizione a gradini con frase di lettura, legenda e conclusione. Il ranking delle cause non si ripete: sta su P06 |
| `p14_energia` | riscritto | parametri a sinistra, catena di calcolo a destra: layout speculare a P13 |
| `p15_output` | **D2** | «API» → «Interfacce applicative», modalità «da verificare sul perimetro» · «ERP e gestionale» → «ERP / gestionale» con scopo e modalità prescritti · fascia più chiara per gli output · colonna contenuto più stretta |
| `p16_delivery` | riscritto | sei fasi con i deliverable sotto. Pagina scura |
| `p17_servizi` | riscritto | narrativa più tabella a otto righe, con blocco di continuità operativa |
| `pa1_compatibilita` | riscritto | «chi risponde» solo nella working edition. Nota unica sugli esiti al posto della ripetizione riga per riga |
| `pa2_sizing` | riscritto | le tre fasce entrano **anche nella client edition**: nella V9.2 il cliente riceveva uno schema con frecce e nessun ordine di grandezza |
| `pa3_requisiti` | rinominato e riscritto | da «Sicurezza e governo» a «Requisiti IT e security». La colonna del valore di progetto, nella client edition, è vuota per costruzione: ripetere «solution design» su otto righe non aggiungeva nulla |
| `pa4_kpi` | riscritto | otto indicatori invece di sei, con costo energetico ed emissioni. Le dodici ripetizioni di «da nominare» e «da approvare» escono, sostituite da una nota unica |

---

## 4. Claim: due riformulazioni di sostanza

| claim | prima | dopo | ragione |
|---|---|---|---|
| — | «Motore KPI», componente dell'architettura | «Elaborazione KPI», funzione | §2.3 della review D2: non si dichiara un componente architetturale non confermato |
| `erp` | «API · dati selezionati · da definire» | «Interfacce applicative · da verificare sul perimetro» | §2.4: la presenza di un'interfaccia applicativa è un claim di prodotto, e non è confermata |

Nessun claim nuovo. La revisione narrativa non ha aggiunto affermazioni
tecniche: ne ha tolte.

---

## 5. Strumenti di build

| file | azione | perché |
|---|---|---|
| `qa93.py` | il tetto di parole esclude il testo dei disegni | §11.2 dello storyboard. Nella V9.2 succedeva per caso perché ogni diagramma era `data-ui`; nella V9.3 i diagrammi non sono viste di prodotto e vanno esclusi esplicitamente. Il testo dei disegni ha un tetto suo, più alto |
| `qa93.py` | nuovo tipo `matrice`, tetti `tabella` e `delivery` da 150 a 185 parole | in una pagina tabellare il testo **è** la tabella: i tetti erano tarati in fase C su pagine con meno righe di quelle che il §8 P08 prescrive |
| `qa93.py` | conteggio delle viste di prodotto per canvas | serve al package check |
| `audit93.py` | nuovo | i cinque controlli di sequenza del §14.3, e i due deliverable Rhythm Map e Duplicate Layout Map |
| `accept93.py` | nuovo | condizioni di build V9.3, precisione terminologica del §12, criteri di approvazione del §16 |
| `claims93.py` | nuovo | claim con più formulazioni per lo stesso marcatore, e le quattordici espressioni vietate dal §12 |
| `mk_dossier93.py` | nuovo | verifica il paragrafo 45–100 parole su ogni pagina core e conta le formule di stato aperto |
| `dossier93.css` | `tb--dense`, `cfg`, `par--hi`, `pr__t`, marcatore di navigazione | i componenti che le correzioni D2 richiedono |
| `deck93.css` | componenti editoriali V9.3 | già introdotti in fase C e D |

### 5.1 Un falso positivo corretto

Il controllo sui valori annualizzati cercava la parola «annuo» in tutto il testo
visibile, e ha segnalato la frase di S14 che dice: «qui non compare nessun
importo annuo». Cerca ora i valori e le locuzioni che li introducono, non la
parola isolata.

---

## 6. Rinumerazione automatica

Con G2 aperto l'appendice del pricing esce dalla client edition e la FAQ, che
nella working edition è A4, diventa **A3**. Un buco nella numerazione si legge
come un errore: la sostituzione è dichiarata in `edition92.py` ed è la stessa
regola già usata nella V9.2.

---

## 7. Che cosa non è cambiato

Palette, canvas 1280×720, Geist e Geist Mono incorporati, zero richieste di
rete, i cinque gate, i 221 token del registro placeholder — il §8.1 vieta di
rinominarli e nessuno è stato rinominato — e lo scenario illustrativo, che
resta invariante dalla V8 e non è stato ricalcolato.
