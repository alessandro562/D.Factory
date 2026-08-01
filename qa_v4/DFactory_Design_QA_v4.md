# D.Factory · Design QA v4

Il QA tecnico e il QA di design sono due cose diverse. Qui ci sono entrambi, in
quest'ordine, ma è il secondo che decide se il lavoro è finito.

Strumenti: `work_v4/render.py` (Playwright/Chromium, 1280 × 720, `device_scale_factor=2`),
`work_v4/qa.py` (misure nel DOM con scalatura del `viewBox` per il testo SVG).

---

## 1. QA tecnico

| Controllo | Sales deck | Dossier |
|---|---|---|
| Canvas renderizzati | 13 | 18 |
| Elementi fuori canvas | **0** | **0** |
| Collisioni non intenzionali | **0** | **0** |
| Errori console | **0** | **0** |
| Richieste di rete | **0** | **0** |
| Font incorporati | Geist, Geist Mono, Instrument Serif · base64 | idem |
| Link interni rotti | **0** | **0** (4 àncore di sezione, tutte risolte) |
| ID duplicati | **0** | **0** |
| CSS di stampa | `@media print` + `@page 1280×720` | idem |
| PDF generabile | `qa_v4/DFactory_SalesDeck_v4.pdf` | `qa_v4/DFactory_DossierTecnico_v4.pdf` |
| SVG informativi con `role`, `title`, `desc` | 8 su 8 | 9 su 9 |

I callout numerati sovrapposti alle viste di prodotto sono sovrapposizioni **intenzionali**
ed escluse dal controllo collisioni: annotano il visual, è il loro lavoro.

**Questo non prova che il lavoro sia buono.** Anche i v2 passavano il QA tecnico a zero
violazioni ed erano visivamente insufficienti. Vedi §3.

---

## 2. Densità misurata

Il conteggio include **tutto** il testo visibile: titoli, occhielli, label, numeri, unità,
stati, testo dentro gli SVG (con il corpo effettivo dopo la scalatura del `viewBox`),
caption e note. Sono esclusi solo numero di pagina, marchio e elementi `aria-hidden`.

### Sales deck · target 40–60 parole, limite 70

| Slide | Parole | Frammenti | Corpo min | Area visual |
|---|---|---|---|---|
| `s01_promessa` | 52 | 27 | 12,5 px | 79 % |
| `s02_punto_cieco` | 49 | 18 | 12,5 px | 54 % |
| `s03_come_funziona` | 68 | 21 | 12,5 px | 61 % |
| `s04_prodotto` | 60 | 24 | 12,0 px | 98 % |
| `s05_decisioni` | 64 | 18 | 12,5 px | 59 % |
| `s06_perche` | 67 | 19 | 12,5 px | 53 % |
| `s07_prova` | 70 | 19 | 12,5 px | 55 % |
| `s08_valore` | 70 | 23 | 12,5 px | 57 % |
| `s09_percorso` | 70 | 24 | 12,5 px | 55 % |
| `s10_cta` | 65 | 16 | 12,0 px | — |
| **Corpo principale** | **media 64 · max 70** | max 27 | **12,0 px** | **9 slide su 10 sopra il 50 %** |
| `a01_offerta` | 123 | 24 | 12,5 px | 61 % |
| `a02_faq` | 156 | 19 | 12,5 px | — |
| `a03_ipotesi` | 131 | 23 | 12,5 px | — |

### Dossier · target 95–135 parole, limite 165

| Pagina | Parole | Frammenti | Corpo min | Area visual |
|---|---|---|---|---|
| `d01_cover` | 102 | 27 | 12,0 px | 21 % |
| `d02_architettura_prodotto` | 153 | 29 | 12,0 px | 43 % |
| `d03_architettura_tecnica` | 129 | 29 | 12,0 px | 75 % |
| `d04_capability` | 131 | 36 | 12,0 px | 50 % |
| `d05_supervisione` | 78 | 23 | 12,0 px | 73 % |
| `d06_oee_fermi` | 151 | 36 | 12,0 px | 73 % |
| `d07_velocita_qualita` | 118 | 30 | 11,6 px | 72 % |
| `d08_multi_impianto` | 62 | 17 | 11,6 px | 75 % |
| `d09_distribuzione_energia` | 98 | 42 | 12,0 px | 72 % |
| `d10_costo_co2_stato` | 129 | 34 | 12,0 px | 72 % |
| `d11_metodo_misura` | 165 | 35 | 12,0 px | 73 % |
| `d12_brownfield` | 162 | 36 | 12,0 px | 50 % |
| `d13_deployment_security` | 146 | 30 | 12,0 px | 70 % |
| `d14_sensori` | 150 | 32 | 12,0 px | 42 % |
| `d15_output_integrazioni` | 122 | 45 | 12,0 px | 50 % |
| `d16_delivery_raci` | 112 | 41 | 12,0 px | 42 % |
| `d17_criteri_pilot` | 151 | 26 | 12,0 px | 42 % |
| `d18_supporto_audit` | 151 | 34 | 12,0 px | — |
| **Totale** | **media 128 · max 165** | max 45 | **11,6 px** | **16 pagine su 18 sopra il 38 %** |

### Confronto con i v2, stesso metodo di conteggio

| | v2 | v4 | Delta |
|---|---|---|---|
| Sales · media parole | 135 | **64** (corpo) | **−53 %** |
| Sales · massimo | 169 | **70** | −99 |
| Sales · slide sopra il limite di 70 | 12 su 12 | **0 su 10** | |
| Sales · corpo minimo effettivo | 9,5 px | **12,0 px** | +2,5 px |
| Dossier · media parole | 177 | **128** | **−28 %** |
| Dossier · massimo | 235 | **165** | −70 |
| Dossier · pagine sopra il limite di 165 | 12 su 18 | **0 su 18** | |
| Placeholder visibili | 17 deck + 27 dossier | **0 + 0** | |

Il corpo minimo non è sceso sotto gli 11,6 px in nessun canvas. Nel v2 tutto il testo SVG
era reso a 10 px e le label mono a 9,5 px.

---

## 3. QA visuale, canvas per canvas

Legenda: **3s** = la tesi si capisce in tre secondi · **640** = leggibile a 640 × 360 ·
**Gri** = gerarchia riconoscibile in scala di grigi sfocata · **>3 pesi** = più di tre pesi
visivi equivalenti sulla pagina.

### Sales deck

| Slide | Tesi in una frase | Visual dominante | 3s | 640 | Gri | >3 pesi |
|---|---|---|---|---|---|---|
| `s01` | Produzione e margine nascono dallo stesso dato | Turno di 5 macchine, un fermo in giallo | ✓ | ✓ | ✓ | no |
| `s02` | La produzione si ferma, il consumo no | Due curve sullo stesso asse | ✓ | ✓ | ✓ | no |
| `s03` | Quattro sorgenti separate diventano un modello solo | Convergenza attorno a un nodo nero | ✓ | ✓ | ✓ | no |
| `s04` | Il turno si vede mentre puoi ancora cambiarlo | Vista di supervisione, 98 % dell'area | ✓ | ✓ | ✓ | no |
| `s05` | Un evento genera tre decisioni diverse | Biforcazione da un blocco nero | ✓ | ✓ | ✓ | no |
| `s06` | Il polmone decide se il fermo macchina è fermo linea | Due scenari a confronto | ✓ | ✓ | ✓ | no |
| `s07` | Le risposte che oggi dai a memoria diventano misurate | Confronto oggi/dopo su tre righe | ✓ | ~ | ~ | no |
| `s08` | Il ritorno nasce da due leve sullo stesso evento | Due barre proporzionali e la somma | ✓ | ✓ | ✓ | no |
| `s09` | Ogni passo del percorso ha un criterio di uscita | Timeline a quattro momenti | ✓ | ✓ | ✓ | no |
| `s10` | Il prossimo passo è l'audit della prima linea | Tipografico | ✓ | ✓ | ✓ | no |

**Eccezioni motivate.**

- `s10_cta` non ha visual dominante. È una scelta: una call to action con un'unica azione
  deve essere la pagina più silenziosa del deck. Il criterio di accettazione chiede almeno
  7 slide su 10 con visual dominante: ne abbiamo 9.
- `s07` è l'unica slide del corpo con tre colonne di lettura. A 640 × 360 la terza colonna
  richiede attenzione. È il compromesso accettato per non trasformare la prova in una griglia
  di card: il confronto oggi/dopo ha bisogno di due colonne più le domande.

### Dossier

| Pagina | Domanda tecnica | Visual dominante | 3s | 640 | Gri | >3 pesi |
|---|---|---|---|---|---|---|
| `d01` | A chi serve e cosa copre | Indice a 4 sezioni | ✓ | ✓ | ✓ | no |
| `d02` | Come si chiamano le cose | Matrice a 5 righe con stati | ✓ | ✓ | ✓ | no |
| `d03` | Da dove arrivano i dati | Flusso su tre zone di rete | ✓ | ✓ | ✓ | no |
| `d04` | Cosa è disponibile oggi | Matrice a 7 righe con stati | ✓ | ✓ | ✓ | no |
| `d05` | Cosa vedo in turno | Vista di supervisione, 3 callout | ✓ | ✓ | ✓ | no |
| `d06` | Perché macchina ferma non è linea ferma | Schema polmone + ranking cause | ✓ | ~ | ✓ | no |
| `d07` | Come si vedono i micro-fermi | Curva con il micro-fermo marcato | ✓ | ✓ | ✓ | no |
| `d08` | Come si legge tutto l'impianto | Timeline a 20 righe | ✓ | ✓ | ✓ | no |
| `d09` | Dove finisce l'energia | Flusso a nastri proporzionali | ✓ | ✓ | ✓ | no |
| `d10` | Quanto costa un pezzo | Barre per vettore + barra per stato | ✓ | ✓ | ✓ | no |
| `d11` | Come si arriva a quei numeri | Sequenza a sei passi | ✓ | ✓ | ✓ | no |
| `d12` | Funziona sul mio parco macchine | Matrice a 7 righe | ✓ | ✓ | ✓ | no |
| `d13` | Cosa chiede al mio IT | Tre zone di rete, flussi unidirezionali | ✓ | ✓ | ✓ | no |
| `d14` | Clamp-on o strumentazione certificata | Matrice a 6 criteri | ✓ | ~ | ✓ | no |
| `d15` | In che forma esce il dato | Matrice a 7 righe con stati | ✓ | ✓ | ✓ | no |
| `d16` | Chi fa cosa e in quanto tempo | Milestone + RACI | ✓ | ~ | ✓ | no |
| `d17` | Quando il pilot è riuscito | Matrice a 6 condizioni | ✓ | ✓ | ✓ | no |
| `d18` | Cosa serve per partire | Checklist a due colonne | ✓ | ✓ | ~ | no |

**Eccezioni motivate.**

- `d18` non ha un visual: è una checklist e una pagina di chiusura. Trasformarla in
  diagramma sarebbe decorazione.
- `d01` sta al 21 % di area visual: è una copertina.
- `d06`, `d14`, `d16` a 640 × 360 richiedono un secondo sguardo. Sono le tre pagine con due
  blocchi informativi impilati. È accettabile in un documento che si consulta, non si
  proietta.

### Stati leggibili in scala di grigi

I quattro stati del dossier (`disponibile`, `configurabile`, `da verificare`,
`roadmap`) portano **la parola** e un **peso di bordo diverso**: pieno, contorno pieno,
contorno punteggiato, contorno sottile. Nessuno dipende dal colore. Verificato nel provino
in scala di grigi.

---

## 4. Test del provino

Provini: `qa_v4/DFactory_SalesDeck_v4_contact.png` ·
`qa_v4/DFactory_DossierTecnico_v4_contact.png` · relative varianti `_small_contact` e
`_hierarchy`.

| Domanda | Esito |
|---|---|
| Il deck ha ritmo e variazione, o sembra una sequenza di template? | **Ritmo.** Dieci silhouette diverse: split asimmetrico, curva a piena larghezza, convergenza, fascia + vista, biforcazione, due scenari, tre colonne, due barre, timeline, tipografico. Nessuno scheletro si ripete due volte di fila |
| Il punto focale cambia in modo intenzionale? | Sì. Sinistra (s01), centro-basso (s02), centro (s03), destra (s04), sinistra-centro (s05), basso (s06), griglia (s07), basso-destra (s08), fascia orizzontale (s09), alto-sinistra (s10) |
| Il giallo guida lo sguardo o è distribuito ovunque? | **Un solo ruolo per slide.** s01 il fermo · s02 la finestra dell'evento · s03 il nodo del modello · s04 il fermo · s05 il punto di biforcazione · s06 la propagazione · s07 la colonna "dopo" · s08 il totale · s09 il punto d'arrivo · s10 la parola "audit" |
| Le silhouette delle slide sono distinguibili? | Sì, nel provino a 640 × 360 e nel provino in scala di grigi |
| Il sales deck sembra più semplice e narrativo del dossier? | Sì: 64 parole contro 128, nessuna matrice, titoli da 44–64 px contro 30 px |
| Il dossier sembra più preciso e consultabile del deck? | Sì: fascia di consultazione costante con sezione e numero di pagina, matrici con stati, blocchi "da definire nel solution design" |
| I due documenti sembrano lo stesso template? | **No.** Impianto di pagina, scala tipografica e componenti sono diversi. Condividono palette, font, marchio e il trattamento del giallo |

### Confronto diretto con i v2 sulle tre slide chiave

| Slide | v2 | v4 |
|---|---|---|
| Cover | Timeline con tutti i segmenti "run" in giallo: il giallo era campitura, non segnale | Stessa timeline, un solo segmento giallo. Il titolo occupa una colonna dedicata, i due KPI hanno spazio proprio |
| Prodotto in azione | Quattro card di pari peso con quattro numeri. Nessuna vista di prodotto | Vista di supervisione al 98 % dell'area utile, tre callout ancorati alle righe che annotano |
| Differenziazione | Quattro micro-diagrammi di pari peso, 148 parole | Un solo diagramma causa-effetto su due scenari, 67 parole. Il differenziatore buffer-aware, che nel v2 era un quarto di slide, è l'intera slide |

---

## 5. Criteri di accettazione della Fase B

| # | Criterio | Esito |
|---|---|---|
| 1 | Nessun placeholder visibile nel sales deck | **Sì** · 0 token, contro 17 nel v2 |
| 2 | Nessuna slide sales sembra un modulo da compilare | **Sì** · `s06` e `s08` del v2 sono state riscritte |
| 3 | Nessuna slide sales usa quattro pannelli equivalenti | **Sì** · 0, contro 4 nel v2 |
| 4 | Almeno 7 slide su 10 con visual dominante evidente | **Sì** · 9 su 10 |
| 5 | Testo sales leggibile a 1280 × 720 senza zoom | **Sì** · minimo 12,0 px, contro 9,5 px |
| 6 | Cover, prodotto e differenziazione più forti dei v2 | **Sì** · vedi §4 |
| 7 | Struttura di consultazione chiara nel dossier | **Sì** · fascia costante con sezione, domanda, pagina |
| 8 | Le pagine funzionali del dossier mostrano il prodotto in grande | **Sì** · `d05` 73 %, `d07` 72 %, `d08` 75 %, `d09` 72 %, `d10` 72 % |
| 9 | I claim dell'assessment non sono pubblicati senza validazione | **Sì** · l'assessment non è nel workspace: nessun contenuto tratto |
| 10 | Il manifest distingue fonte, stato, owner e uso | **Sì** · `DFactory_ContentManifest_v4.md` §1, §3, §4, §7 |
| 11 | Deck e dossier coordinati ma non lo stesso template | **Sì** · manifest §9 |
| 12 | Il report QA contiene giudizi visuali, non solo controlli automatici | **Sì** · §3 e §4 |
| 13 | I file originali restano intatti | **Sì** · i v2 non sono stati toccati |
| 14 | Tutti gli output indicati esistono e si aprono | **Sì** · vedi §6 |

## 6. File prodotti

```
DFactory_SalesDeck_v4.html            256 KB · 13 canvas · self-contained
DFactory_DossierTecnico_v4.html       279 KB · 18 canvas · self-contained
DFactory_ContentManifest_v4.md
DFactory_ChangeLog_v4.md
DFactory_OpenInputs_v4.md
qa_v4/DFactory_Design_QA_v4.md
qa_v4/sales/            13 PNG a 2560×1440
qa_v4/dossier/          18 PNG a 2560×1440
qa_v4/DFactory_SalesDeck_v4_contact.png · _small_contact.png · _hierarchy.png · .pdf
qa_v4/DFactory_DossierTecnico_v4_contact.png · _small_contact.png · _hierarchy.png · .pdf
work_v4/00_Audit_Visivo_Editoriale.md
work_v4/01_ContentManifest_v4_DRAFT.md
work_v4/02_Direction_Comparison.md
work_v4/Prototype_Direction_A.html · Prototype_Direction_B.html + provini
work_v4/render.py · qa.py · build.py · assets/fonts.css
work_v4/v2_SalesDeck_*.png · v2_Dossier_*.png   (provini della base v2)
```
