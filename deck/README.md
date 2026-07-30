# Pipeline sales deck D.Factory

```
python3 deck/build.py      # sorgenti -> DFactory_SalesDeck.html (standalone)
python3 deck/qa.py         # controlli automatici (overflow, palette, termini)
python3 deck/render.py --contact-sheet   # -> PNG per slide + DFactory_SalesDeck.pdf
python3 deck/build_web.py  # -> deck/web/, versione web da pubblicare come link
```

## Struttura

| Percorso | Cosa contiene |
|---|---|
| `src/00_head.html` | head, token font, design system CSS |
| `src/01_slides_01_10.html` … `src/03_slides_21_30.html` | markup delle slide |
| `src/dash.html` | i 7 mockup di prodotto, come componenti riusabili (`<!--@DASH:NOME@-->`) |
| `assets/` | lockup e marchio, nero e bianco su trasparente |
| `fonts/` | Geist e Geist Mono variable woff2 (dal pacchetto npm `geist`) |
| `web/` | visualizzatore web (frammento per Artifact, senza doctype/head/body) |
| `out/` | render intermedi, non versionati |

`build.py` concatena i sorgenti, inserisce i mockup sui token `@@DASH_NOME@@` (e
`@@DASH_NOME_MINI@@` per la versione in scala), genera il markup ripetitivo delle chart
(timeline 20 macchine, barre orarie, diagramma di flusso energia) e inlinea font e logo in
base64. L'HTML in uscita è standalone: **nessuna dipendenza CDN**.

## Convenzioni

- **Editing per id DOM, non per numero visualizzato.** Gli id non seguono la numerazione a
  schermo: l'offset nasce dalle slide inserite prima di `s07_super` (che resta l'id storico
  della slide MAPST 4.0, oggi visualizzata come 08). Mappa completa:

  | id | # | id | # | id | # |
  |---|---|---|---|---|---|
  | `s01_cover` | 01 | `s11_velocita` | 12 | `s21_sensori` | 22 |
  | `s02_perche_ora` | 02 | `s12_multi` | 13 | `s22_pacchetti` | 23 |
  | `s03_problema` | 03 | `s13_oee` | 14 | `s23_roi` | 24 |
  | `s04_gap` | 04 | `s14_distrib` | 15 | `s24_posizionamento` | 25 |
  | `s05_soluzione` | 05 | `s15_costo` | 16 | `s25_differenziatori` | 26 |
  | `s06_refyn` | 06 | `s16_stato` | 17 | `s26_prova` | 27 |
  | `s06_architettura` | 07 | `s17_misura` | 18 | `s27_gruppo` | 28 |
  | `s07_super` | 08 | `s18_brownfield` | 19 | `s28_prossimi` | 29 |
  | `s08_platform` | 09 | `s19_report` | 20 | `s29_cta` | 30 |
  | `s09_superv` | 10 | `s20_attivazione` | 21 | | |
  | `s10_fermi` | 11 | | | | |

- **Modifiche via `str_replace` con guardia di unicità** sui file in `src/`, poi rebuild.
  Non editare `DFactory_SalesDeck.html`: è generato e viene sovrascritto.

  ```python
  s = pathlib.Path("deck/src/02_slides_11_20.html").read_text()
  assert s.count(old) == 1
  pathlib.Path(...).write_text(s.replace(old, new))
  ```

- **Render:** Playwright/Chromium, viewport 1280x720, `device_scale_factor=3`, attesa
  `networkidle` + `document.fonts.ready` + 600 ms, screenshot per slide, PDF via `img2pdf`
  a 13.333" x 7.5" (960 x 540 pt).

- **Se cambi la numerazione delle slide**, aggiorna sia il cartiglio (`DOC nn/30`) sia il
  numero nel masthead: sono scritti a mano nel markup, non calcolati.

## QA

`qa.py` gira sull'HTML costruito e va tenuto a zero problemi. Controlla:

1. **Overflow** geometrico: elementi che escono dall'area `.body` o invadono il cartiglio
   (il caso di rottura più frequente quando si allunga la copy).
2. **Testo giallo su fondo chiaro:** vietato dalle regole brand. Risale al primo antenato
   con background opaco e ne calcola la luminanza.
3. **Colori fuori palette:** ammessi solo `#e6e011` e neutri (differenza max fra i canali
   RGB <= 14).
4. **Termini banditi**, residui di brand/palette vecchi, trattini lunghi in prosa e conteggio
   delle costruzioni "Non X. Y." (massimo una in tutto il deck).

Dopo il render, `--contact-sheet` produce il montaggio di tutte le slide in
`out/contact_sheet.png` per il controllo visivo d'insieme.

## Dipendenze

```
pip install playwright pillow img2pdf numpy scipy pymupdf
npm install geist    # solo per rigenerare i font in deck/fonts/
```

Chromium è già presente in questo ambiente (`/opt/pw-browsers/chromium-1194/`); `render.py`
e `qa.py` lo usano via `executable_path` e ricadono sul default se assente.

## Versione web

`build_web.py` avvolge ogni slide in un contenitore scalabile e aggiunge la cornice del
visualizzatore, riusando i token e il Geist Mono gia' presenti nel deck: nessun font e
nessun colore nuovo. Le slide non si invertono col tema del lettore (sono l'opera), si
adatta solo la cornice, via token, con override per `data-theme`.

- La scala esatta la calcola il JS da `clientWidth` (`100vw` includerebbe la barra di
  scorrimento e produrrebbe overflow orizzontale). Fallback CSS `--s:.72` se il JS non parte.
- **Vista d'insieme:** stesso DOM, sola scala diversa (`body.ov`), quindi nessuna copia
  delle 30 slide in miniatura.
- **Tastiera:** frecce, PageUp/PageDown, spazio, Home, End, `O` indice, `Esc` chiude.
- Il contatore segue la prima slide visibile sotto la barra, non quella "piu' centrata":
  su schermi stretti ne entrano diverse in viewport e il centro non basta a disambiguare.
