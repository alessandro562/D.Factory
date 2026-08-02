# D.Factory · Changelog v7

I file precedenti non sono stati toccati. `DFactory_SalesDeck_v6.html` e tutte le
versioni v4 e v5 restano invariate.

| Documento | prima | v7 |
|---|---|---|
| Sales deck | v6 · 9 slide | **12 slide + 4 appendici commerciali** |
| Dossier tecnico | v5 · 31 pagine | **19 pagine** |

---

## 0. La decisione che governa tutte le altre

La grammatica visuale del v6 è **congelata**: prodotto protagonista, interfacce
ricostruite, timeline, un evento evidenziato, relazione fra fermo, causa, energia e
valore, alternanza chiaro/scuro, giallo con significato. Nessuna slide riuscita è stata
ridisegnata.

Il deck non è stato rifatto: è stato **completato**. Il dossier sì, perché il v5 non era
un modello da conservare ma una fonte di contenuti tecnici.

---

## 1. Sales deck · crosswalk

| v6 | v7 | che cosa è successo |
|---|---|---|
| `s01_cover` | **01** | La vista cresce da 356 a 420 px: la dichiarazione di ricostruzione entra nella testata del pannello e libera il piede. `h1` da 64 a 52 px per rientrare nella forbice 40–52 |
| `s02_punto_cieco` | **02** | **Passa su carta.** Il rapporto di fine turno è un documento stampato, non una schermata: su fondo chiaro il contrasto con la copertina nera regge meglio e il ritmo del deck migliora |
| — | **03** `s03_cosa_e` | **Nuova.** Una sola interfaccia composita con tre letture dello stesso turno: stato e produzione, energia per stato, impatto economico. Risponde a «che cos'è il prodotto», che il v6 non chiedeva a nessuna slide |
| `s03_prodotto` | **04** | Invariata. È il benchmark visuale dichiarato dal brief |
| `s04_energia` | **05** | Titolo dal brief: «La linea si ferma. L'energia continua a scorrere.» Aggiunta la riga «Lo stesso minuto pesa su capacità e consumi» |
| `s05_decisione` | **06** | Titolo dal brief: «Un fermo è una causa. Quattordici sono una priorità.» |
| — | **07** `s07_ampiezza` | **Nuova.** Sei riquadri della stessa dashboard, non sei card: stato, OEE e velocità, fermi e micro-fermate, consumi e utility, costo energetico e CO₂, confronti. Serve a non far sembrare D.Factory un software per soli fermi |
| `s06_offerta` | **08** | La domanda di Refyn diventa «Cosa conviene fare e con quale risultato?». Il resto invariato: una sola finestra che si allunga in tre sezioni numerate |
| — | **09** `s09_perche` | **Nuova.** Tre prove in tre fasce: produzione ed energia sulla stessa lettura, brownfield, software e competenze. Nessun cliente, nessun logo, nessun numero non validato. La continuità con MAPST 4.0 e MarEnergy è una nota nel piede |
| `s07_valore` | **10** | **Estesa.** Alla catena aritmetica si aggiungono le due leve chieste dal brief: capacità potenzialmente recuperabile e energia potenzialmente evitabile. Il disclaimer diventa «Scenario illustrativo · non risultato cliente» |
| `s08_pilot` | **11** | **Riscritta.** Dal Gantt a tre momenti — verifica, pilot, decisione di scala — con sotto la struttura economica: avvio, canone annuale, servizi specialistici. Nessun importo |
| `s09_cta` | **12** | **Riscritta.** Il perimetro lascia il posto al blocco operativo: chi coinvolgere, cosa preparare, cosa restituiamo. A destra quanto vale la linea, con la timeline dell'apertura |
| — | **A1** | **Nuova.** Confronto dei tre livelli su otto capacità. È l'unica matrice di tutto il deck, e sta in appendice |
| — | **A2** | **Nuova.** Quattro famiglie di servizi in quattro fasce, non dodici card |
| — | **A3** | **Nuova.** Struttura economica in tre voci e formula di pricing. Nessun importo e **nessun placeholder**: il brief vieta di pubblicare `€ [DA DEFINIRE]` |
| — | **A4** | **Nuova.** Sei domande e sei risposte prudenti |

### Ritmo

`01 scura · 02 chiara · 03 scura · 04 chiara · 05 scura · 06 chiara · 07 scura ·
08 chiara · 09 scura · 10 scura · 11 chiara · 12 scura` · appendici tutte chiare.

Una sola coppia adiacente dello stesso tono, 09–10, ed è voluta: «perché D.Factory» e il
valore economico sono lo stesso blocco argomentativo. Le appendici sono tutte chiare
perché è il segnale che si è usciti dalla presentazione.

---

## 2. Dossier · da 31 pagine a 19

### Che cosa è stato eliminato e perché

| pagina v5 | motivo |
|---|---|
| `d03_provenienza` | provenienza legacy di ogni capability: product management interno |
| `d06_capability` | matrice a sei colonne con doppio stato di maturità |
| `d15_opportunity` · `d16_action_benefit` | funzioni Refyn non approvate, presentate come schermate |
| `d17_oee_avanzato` | logica buffer-aware dichiarata «in development» |
| `d18_roadmap` | roadmap, con funzioni marcate `not offered` |
| `d27_raci` | organizzazione di progetto, non contenuto tecnico |
| `d30_migrazione` | percorso di migrazione dal legacy |
| `d02_architettura_commerciale` | sette righe di moduli con il loro stato di maturità |
| `d10_multi_impianto` · `d31_checklist` | assorbite in altre pagine |

Con loro sono usciti **tutti gli stati di maturità**, tutte le classificazioni interne e
tutte le decisioni di prodotto non ancora chiuse. Refyn dichiara il proprio stato **una
volta sola**, a pagina 08.

### Che cosa è stato conservato e riscritto

| v7 | fonte | che cosa è cambiato |
|---|---|---|
| **02** soluzione | v5 · 02 | Da sette righe con stato a una finestra che cresce in tre sezioni |
| **03** architettura | **campione v6 approvato** | Invariata |
| **04** acquisizione | v5 · 05 | La classificazione è dell'impianto — già presente, da verificare, da aggiungere — non della maturità del prodotto |
| **05** contestualizzazione | **nuova** | Lo stesso evento allineato su cinque tracce: spiega perché il dato grezzo non basta |
| **06** Connect · **07** Insight | v5 · 07, 08, 14 | Fuse e alleggerite, con la correlazione produzione-energia dentro Insight |
| **08** Refyn | **campione v6 approvato** | Invariata |
| **09** OEE | v5 · 17 | Riscritta senza la frase sul polmone: confini, blocking, starvation, aggregazione |
| **10** perdite | v5 · 09 | Quattro perdite sulla stessa timeline, non quattro paragrafi |
| **11** energia · **12** costo e CO₂ | v5 · 11, 12 | CO₂ **calcolata o stimata**, mai misurata |
| **13** metodo | v5 · 13 | Sequenza a cinque passi invece della tabella |
| **14** brownfield | v5 · 19, 20 | Quattro esiti in quattro righe. Sparisce `project-dependent` |
| **15** deployment e IT/OT | v5 · 21, 22 | Diciannove voci in tre gruppi con un proprietario per gruppo, invece di un elenco di «da concordare» |
| **16** sensoristica | v5 · 23 | Tre casi, con che cosa si fa e che cosa va deciso |
| **17** output | v5 · 24 | Output → destinatari → decisione |
| **18** pilot | v5 · 26, 28 | Quattro deliverable, fasi e criteri di uscita in una pagina |
| **19** servizi | v5 · 25, 29 | Sei servizi. La continuità legacy è **una nota sola**, con la formula del brief |

---

## 3. Claim e formulazioni

| formulazione | stato |
|---|---|
| «un solo modello dati» | **non usata**: non è tecnicamente confermata |
| «causa associata» | usata ovunque: la causa è inserita o validata da una persona |
| «CO₂ calcolata o stimata» | usata; mai «misurata» |
| ISO 50001 | **non citata**: nessuna certificazione da dichiarare |
| ERP | «possibile integrazione, previa verifica tecnica». Mai SAP |
| brownfield | «approccio multi-vendor con compatibilità verificata in audit». Mai «qualsiasi protocollo» |
| «margine perso stimato» | usata: il parametro economico dichiarato è un margine unitario |
| «capacità potenzialmente recuperabile» · «energia potenzialmente evitabile» | usate come leve dello scenario |
| MAPST 4.0 e MarEnergy | citati **una volta sola** nel dossier, a pagina 19, con la formula del brief. Assenti dal corpo del deck |
| Refyn | «modulo avanzato in sviluppo», dichiarato una volta per documento |

---

## 4. Che cosa è cambiato negli strumenti

Il QA misura ora quattro popolazioni di testo con soglie separate — contenuti, metadati di
pagina, diagrammi, viste di prodotto — perché hanno funzioni diverse: il contenuto si legge
in proiezione, le etichette di una schermata si guardano da vicino come in uno screenshot.

Aggiunto `semantic.py`: cerca i termini vietati dal §15.3 **sui testi visibili e sui testi
accessibili**, `title` e `desc` degli SVG compresi. Sono invisibili a schermo ma fanno
parte del documento e li leggono gli screen reader: nella v5 un claim ritirato era
sopravvissuto esattamente lì.
