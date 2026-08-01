# D.Factory · Design QA v4

Il QA tecnico e il QA di design sono due cose diverse. Qui ci sono entrambi, ma è il secondo
che decide se il lavoro è finito.

Strumenti: `work_v4/render.py` (Playwright/Chromium, 1280 × 720, `device_scale_factor=2`),
`work_v4/qa.py` (misure nel DOM, con scalatura del `viewBox` per il testo SVG).

Questa è la revisione **v4.1**, dopo i sei interventi chiesti in review. Il dossier passa da
18 a 23 pagine.

---

## 1. QA tecnico

| Controllo | Sales deck | Dossier |
|---|---|---|
| Canvas renderizzati | 13 · 10 + 3 appendice | 23 |
| Elementi fuori canvas | **0** | **0** |
| Collisioni non intenzionali | **0** | **0** |
| Errori console | **0** | **0** |
| Richieste di rete | **0** | **0** |
| Font incorporati | Geist, Geist Mono, Instrument Serif · base64 | idem |
| Link interni rotti | **0** | **0** · 4 àncore di sezione risolte |
| ID duplicati | **0** | **0** |
| CSS di stampa | `@media print` + `@page 1280×720` | idem |
| PDF generabile | `qa_v4/DFactory_SalesDeck_v4.pdf` | `qa_v4/DFactory_DossierTecnico_v4.pdf` |
| SVG informativi con `role`, `title`, `desc` | 8 su 8 | 11 su 11 |

**Questo non prova che il lavoro sia buono.** Anche i v2 passavano il QA tecnico a zero
violazioni ed erano visivamente insufficienti. Vedi §3.

---

## 2. Densità misurata

Il conteggio include **tutto** il testo visibile: titoli, occhielli, label, numeri, unità,
stati, testo dentro gli SVG (con il corpo effettivo dopo la scalatura del `viewBox`), caption
e note. Esclusi solo numero di pagina, marchio ed elementi `aria-hidden`.

### Sales deck · target 40–60 parole, limite 70

| Slide | Parole | Frammenti | Corpo min | Area visual |
|---|---|---|---|---|
| `s01_promessa` | 53 | 28 | 12,5 px | 79 % |
| `s02_punto_cieco` | 49 | 18 | 12,5 px | 54 % |
| `s03_come_funziona` | 70 | 21 | 12,5 px | 61 % |
| `s04_prodotto` | 53 | 22 | 12,0 px | 98 % |
| `s05_decisioni` | 64 | 18 | 12,5 px | 59 % |
| `s06_perche` | 67 | 19 | 12,5 px | 53 % |
| `s07_ipotesi_misure` | 70 | 19 | 12,5 px | 55 % |
| `s08_valore` | 64 | 23 | 12,5 px | 61 % |
| `s09_percorso` | 70 | 24 | 12,5 px | 55 % |
| `s10_cta` | 65 | 16 | 12,0 px | — |
| **Corpo principale** | **media 62 · max 70** | max 28 | **12,0 px** | **9 su 10 sopra il 50 %** |
| `a01_offerta` | 123 | 24 | 12,5 px | 61 % |
| `a02_faq` | 162 | 19 | 12,5 px | — |
| `a03_ipotesi` | 131 | 23 | 12,5 px | — |

### Dossier · target 95–135 parole, limite 165

| Pagina | Parole | Frammenti | Corpo min | Area visual | Fascia |
|---|---|---|---|---|---|
| 01 `d01_cover` | 104 | 27 | 12,5 px | 23 % | — |
| 02 `d02_architettura_prodotto` | 153 | 29 | 12,0 px | 46 % | piena |
| 03 `d03_architettura_tecnica` | 129 | 29 | 12,0 px | 74 % | piena |
| 04 `d04_acquisizione` | 143 | 32 | 11,5 px | 72 % | piena |
| 05 `d05_capability` | 131 | 36 | 12,0 px | 56 % | ridotta |
| 06 `d06_supervisione` | 78 | 23 | 12,0 px | 73 % | piena |
| 07 `d07_oee_fermi` | 151 | 36 | 12,0 px | 72 % | piena |
| 08 `d08_velocita_qualita` | 118 | 30 | 11,6 px | 72 % | piena |
| 09 `d09_multi_impianto` | 62 | 17 | 11,6 px | 75 % | piena |
| 10 `d10_distribuzione_energia` | 98 | 42 | 12,0 px | 72 % | piena |
| 11 `d11_costo_co2_stato` | 129 | 34 | 12,0 px | 72 % | piena |
| 12 `d12_metodo_misura` | 165 | 35 | 12,0 px | 73 % | piena |
| 13 `d13_brownfield_macchine` | 121 | 28 | 12,0 px | 41 % | ridotta |
| 14 `d14_brownfield_rete` | 139 | 34 | 12,0 px | 60 % | piena |
| 15 `d15_deployment` | 125 | 22 | 12,0 px | 70 % | piena |
| 16 `d16_specifiche_it` | 148 | 49 | 12,5 px | 56 % | ridotta |
| 17 `d17_sensori` | 150 | 32 | 12,0 px | 47 % | ridotta |
| 18 `d18_output_integrazioni` | 122 | 45 | 12,0 px | 56 % | ridotta |
| 19 `d19_milestone` | 137 | 23 | 12,0 px | 48 % | piena |
| 20 `d20_raci` | 89 | 42 | 12,0 px | 54 % | ridotta |
| 21 `d21_criteri_pilot` | 151 | 26 | 12,0 px | 47 % | ridotta |
| 22 `d22_supporto` | 97 | 40 | 12,5 px | 43 % | piena |
| 23 `d23_checklist` | 134 | 31 | 12,0 px | 47 % | ridotta |
| **Totale** | **media 125 · max 165** | max 49 | **11,5 px** | **22 su 23 sopra il 38 %** | 8 ridotte |

La fascia ridotta (248 px invece di 336) restituisce 88 px di larghezza al campo sulle otto
pagine tabellari. Su quelle pagine la fascia porta solo sezione, domanda e una frase.

### Confronto con i v2, stesso metodo di conteggio

| | v2 | v4.1 | Delta |
|---|---|---|---|
| Sales · media parole | 135 | **62** (corpo) | **−54 %** |
| Sales · massimo | 169 | **70** | −99 |
| Sales · slide oltre il limite di 70 | 12 su 12 | **0 su 10** | |
| Sales · corpo minimo effettivo | 9,5 px | **12,0 px** | +2,5 px |
| Dossier · media parole | 177 | **125** | **−29 %** |
| Dossier · massimo | 235 | **165** | −70 |
| Dossier · pagine oltre il limite di 165 | 12 su 18 | **0 su 23** | |
| Dossier · corpo minimo effettivo | 9,5 px | **11,5 px** | +2,0 px |
| Dossier · pagine | 18 | **23** | +5, per far respirare le più dense |
| Placeholder visibili | 17 deck + 27 dossier | **0 + 0** | |

---

## 3. QA visuale, canvas per canvas

**3s** = tesi chiara in tre secondi · **640** = leggibile a 640 × 360 · **Gri** = gerarchia
riconoscibile in scala di grigi sfocata.

### Sales deck

| Slide | Tesi | Visual dominante | 3s | 640 | Gri |
|---|---|---|---|---|---|
| `s01` | Produzione e margine nascono dallo stesso dato | Turno di 5 macchine, un fermo in giallo | ✓ | ✓ | ✓ |
| `s02` | La produzione si ferma, il consumo no | Due curve sullo stesso asse | ✓ | ✓ | ✓ |
| `s03` | Quattro sorgenti separate diventano un modello solo | Convergenza attorno a un nodo nero | ✓ | ✓ | ✓ |
| `s04` | Un fermo diventa una decisione entro il turno | Tre macchine · anomalia, causa, decisione | ✓ | ✓ | ✓ |
| `s05` | Un evento genera tre decisioni diverse | Biforcazione da un blocco nero | ✓ | ✓ | ✓ |
| `s06` | Il polmone decide se il fermo macchina è fermo linea | Due scenari a confronto | ✓ | ✓ | ✓ |
| `s07` | Le risposte date a memoria diventano misurate | Confronto oggi/dopo su tre righe | ✓ | ~ | ~ |
| `s08` | Il ritorno nasce da due leve sullo stesso evento | Due barre proporzionali e la somma | ✓ | ✓ | ✓ |
| `s09` | Ogni passo ha un criterio di uscita | Timeline a quattro momenti | ✓ | ✓ | ✓ |
| `s10` | Il prossimo passo è l'audit della prima linea | Tipografico | ✓ | ✓ | ✓ |

**Eccezioni motivate.**

- `s10_cta` non ha visual dominante, per scelta: la call to action deve essere la pagina più
  silenziosa del deck. Il criterio chiede almeno 7 slide su 10 con visual dominante: sono 9.
- `s07` è l'unica slide del corpo con tre colonne di lettura. È il compromesso accettato per
  non trasformare il confronto in una griglia di card.

### Dossier

| Pagina | Domanda tecnica | Visual dominante | 3s | 640 | Gri |
|---|---|---|---|---|---|
| 01 | A chi serve e cosa copre | Indice a 4 sezioni | ✓ | ✓ | ✓ |
| 02 | Come si chiamano le cose | Matrice nomenclatura, 5 righe | ✓ | ✓ | ✓ |
| 03 | Da dove arrivano i dati | Flusso su tre zone di rete | ✓ | ✓ | ✓ |
| 04 | Dove il dato viene preso fisicamente | Schema di linea con i punti di prelievo | ✓ | ✓ | ✓ |
| 05 | Cosa è disponibile oggi | Matrice per dominio, 7 righe, 5 stati | ✓ | ✓ | ✓ |
| 06 | Cosa vedo in turno | Vista di supervisione, 3 callout | ✓ | ✓ | ✓ |
| 07 | Perché macchina ferma non è linea ferma | Schema polmone + ranking cause | ✓ | ~ | ✓ |
| 08 | Come si vedono i micro-fermi | Curva con il micro-fermo marcato | ✓ | ✓ | ✓ |
| 09 | Come si legge tutto l'impianto | Timeline a 20 righe | ✓ | ✓ | ✓ |
| 10 | Dove finisce l'energia | Flusso a nastri proporzionali | ✓ | ✓ | ✓ |
| 11 | Quanto costa un pezzo | Barre per vettore + barra per stato | ✓ | ✓ | ✓ |
| 12 | Come si arriva a quei numeri | Sequenza a sei passi | ✓ | ✓ | ✓ |
| 13 | Macchine, PLC e misura | Matrice, 5 righe | ✓ | ✓ | ✓ |
| 14 | Rete, gestionale e tag mapping | Due matrici, 4 + 3 righe | ✓ | ✓ | ✓ |
| 15 | Cosa chiede al mio IT | Tre zone di rete, flussi unidirezionali | ✓ | ✓ | ✓ |
| 16 | Le voci che l'IT deve approvare | Matrice 9 voci × stato, owner, scadenza | ✓ | ~ | ✓ |
| 17 | Clamp-on o strumentazione certificata | Matrice a 6 criteri | ✓ | ✓ | ✓ |
| 18 | In che forma esce il dato | Matrice output, 7 righe | ✓ | ✓ | ✓ |
| 19 | Dal primo segnale al go-live | Le cinque milestone, sequenza verticale | ✓ | ✓ | ✓ |
| 20 | Chi fa cosa | RACI, 7 righe | ✓ | ✓ | ✓ |
| 21 | Quando il pilot è riuscito | Matrice criteri, 6 condizioni | ✓ | ✓ | ✓ |
| 22 | Cosa succede dopo il go-live | Matrice supporto, 6 voci | ✓ | ✓ | ✓ |
| 23 | Cosa portare in sala | Checklist a 3 colonne, 6 righe | ✓ | ✓ | ✓ |

**Eccezioni motivate.** `d01` sta al 23 % di area visual: è una copertina. `d07` a 640 × 360
richiede un secondo sguardo perché impila due blocchi informativi; è accettabile in un
documento che si consulta, non si proietta.

### Cinque stati, leggibili in scala di grigi

`disponibile` · `configurabile` · `dipende dall'infrastruttura` · `da verificare in audit` ·
`roadmap`. Ognuno porta **la parola** e un **peso di bordo diverso**: pieno, contorno pieno,
contorno misto, contorno punteggiato, contorno sottile. Nessuno dipende dal colore.

---

## 4. Test del provino

| Domanda | Esito |
|---|---|
| Il deck ha ritmo o sembra una sequenza di template? | **Ritmo.** Dieci silhouette diverse; nessuno scheletro si ripete due volte di fila |
| Il punto focale cambia in modo intenzionale? | Sì: sinistra, centro-basso, centro, destra, sinistra-centro, basso, griglia, basso-destra, fascia orizzontale, alto-sinistra |
| Il giallo guida lo sguardo? | **Un solo ruolo per slide.** s01 il fermo · s02 la finestra dell'evento · s03 il nodo · s04 il fermo · s05 la biforcazione · s06 la propagazione · s07 la colonna "dopo" · s08 **la cautela**, non il risultato · s09 il punto d'arrivo · s10 la parola "audit" |
| Il deck sembra più semplice e narrativo del dossier? | Sì: 62 parole contro 125, nessuna matrice, titoli 44–64 px contro 25–30 px |
| Il dossier sembra più preciso e consultabile? | Sì: fascia costante con sezione e numero di pagina, cinque stati, blocchi solution design |
| Sembrano lo stesso template? | **No.** Impianto, scala tipografica e componenti sono diversi. Condividono palette, font, marchio e trattamento del giallo |

---

## 5. I sei interventi della revisione

| # | Richiesta | Cosa è cambiato | Verifica |
|---|---|---|---|
| 1 | La slide 7 non deve chiamarsi "la prova" | Occhiello da "La prova" a "Dalle ipotesi alle misure"; `id` da `s07_prova` a `s07_ipotesi_misure` | Il titolo resta "Le domande a cui oggi rispondi a memoria" |
| 2 | Numeri non-cliente inequivocabilmente illustrativi | `s01`: etichetta "Valori illustrativi" **sopra** i due KPI, non nel rail. `s04`: "OEE di linea · valore illustrativo" sotto il numero. `s08`: badge giallo pieno **accanto** al risultato, e il risultato passa da giallo a bianco | Il giallo di `s08` ora marca la cautela, non la cifra: la gerarchia si inverte a favore del disclaimer |
| 3 | Semplificare la slide 4 | Da 6 macchine e 2 KPI a **3 macchine e 1 KPI**. I callout diventano anomalia → causa → decisione, con le ancore dentro l'SVG | Da 60 a 53 parole; non è più una dashboard |
| 4 | Almeno due asset reali | **Uno consegnato**: schema di linea con i punti di prelievo (`d04`), disegnato. **Uno non consegnabile**: lo screenshot reale del prodotto. Vedi §7 | |
| 5 | Dividere le pagine più dense del dossier | Brownfield → 13 e 14 · Deployment → 15 e 16 · Delivery → 19 e 20 · Supporto → 22 e 23. Fascia ridotta su 8 pagine tabellari. Corpo delle matrici da 13,5 a 14 px | Media 128 → 125 su 5 pagine in più; nessuna pagina oltre 165 |
| 6 | Completare la parte IT/OT | Nuova pagina 16: **9 voci × stato oggi, chi decide, quando si chiude**. Sostituisce l'elenco puntato indistinto | Vedi §7 per il limite che resta |

## 6. Criteri di accettazione

| # | Criterio | Esito |
|---|---|---|
| 1 | Nessun placeholder visibile nel sales deck | **Sì** · 0, contro 17 nel v2 |
| 2 | Nessuna slide sembra un modulo da compilare | **Sì** |
| 3 | Nessuna slide con quattro pannelli equivalenti | **Sì** · 0, contro 4 |
| 4 | Almeno 7 slide su 10 con visual dominante | **Sì** · 9 su 10 |
| 5 | Testo leggibile a 1280 × 720 senza zoom | **Sì** · minimo 12,0 px nel deck, 11,5 px nel dossier |
| 6 | Cover, prodotto e differenziazione più forti dei v2 | **Sì** |
| 7 | Struttura di consultazione chiara nel dossier | **Sì** · fascia costante, due larghezze secondo la densità |
| 8 | Pagine funzionali con il prodotto in grande | **Sì** · 06 al 73 %, 08 al 72 %, 09 al 75 %, 10 al 72 %, 11 al 72 % |
| 9 | Claim dell'assessment non pubblicati senza validazione | **Sì** · nessuno pubblicato; riclassificati "da validare" con owner, manifest §3 |
| 10 | Il manifest distingue fonte, stato, owner e uso | **Sì** |
| 11 | Deck e dossier coordinati ma non lo stesso template | **Sì** |
| 12 | Il report QA contiene giudizi visuali | **Sì** · §3 e §4 |
| 13 | I file originali restano intatti | **Sì** |
| 14 | Tutti gli output esistono e si aprono | **Sì** |

## 7. Cosa questo QA **non** può dichiarare

Due limiti restano aperti e nessuna metrica in questo documento li copre.

**Lo screenshot reale del prodotto non c'è.** Tutte le viste di `s04`, `d06`, `d08`, `d09`
sono ricostruzioni, etichettate come tali. Sono coerenti con il prodotto descritto, ma un
interlocutore tecnico distingue una ricostruzione da una schermata vera alla prima occhiata.
Non è un problema risolvibile disegnando meglio: serve l'asset. Finché manca, i due documenti
mostrano *cosa il sistema calcola*, non *com'è fatto il sistema*.

**Il dossier non è ancora approvabile da un reparto IT.** La pagina 16 elenca le nove voci
decisive con stato, owner e scadenza, ed è molto più utile dell'elenco indistinto che c'era
prima. Ma "da concordare secondo le policy interne" resta una riga di solution design, non
una specifica. Diventa specifica quando arrivano i valori: protocolli verificati, porte,
sizing, schema di autenticazione, politica di backup e retention, finestra di patching,
formato dei log. Sono gli input 6–16 di `DFactory_OpenInputs_v4.md`.

Formulazione corretta dello stato attuale: **il dossier è pronto per la riunione tecnica in
cui quelle voci si compilano, non per l'approvazione che viene dopo.**
