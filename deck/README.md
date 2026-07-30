# Pipeline sales deck D.Factory

```
python3 deck/build.py      # sorgenti -> DFactory_SalesDeck.html (standalone)
python3 deck/qa.py         # controlli automatici (overflow, palette, termini)
python3 deck/render.py --contact-sheet   # -> PNG per slide + DFactory_SalesDeck.pdf
python3 deck/build_web.py  # -> deck/web/, visualizzatore web (frammento)
python3 deck/standalone.py # -> HTML autonomi da scaricare, a dipendenza zero
```

## Struttura

| Percorso | Cosa contiene |
|---|---|
| `src/00_head.html` | head, token font, design system CSS |
| `src/01_slides_01_10.html` … `src/03_slides_21_30.html` | markup delle slide |
| `src/dash.html` | i 7 mockup di prodotto, come componenti riusabili (`<!--@DASH:NOME@-->`) |
| `assets/` | lockup e marchio, nero e bianco su trasparente |
| `fonts/` | Geist e Geist Mono variable woff2 (dal pacchetto npm `geist`) |
| `web/` | visualizzatore web (frammento, senza doctype/head/body) |
| `review/` | review commerciale del deck (frammento) |
| `out/` | render intermedi, non versionati |

`build.py` concatena i sorgenti, inserisce i mockup sui token `@@DASH_NOME@@` (e
`@@DASH_NOME_MINI@@` per la versione in scala), genera il markup ripetitivo delle chart
(timeline 20 macchine, barre orarie, diagramma di flusso energia) e inlinea font e logo in
base64. L'HTML in uscita è standalone: **nessuna dipendenza CDN**.

## Convenzioni

- **Nucleo e appendice.** `src/10_core.html` contiene le 18 slide che si presentano,
  `src/20_appendice.html` le 17 di dettaglio tecnico. Ogni `<section>` porta
  `data-part="nucleo"` o `data-part="appendice"`.

- **La numerazione e' automatica.** Masthead e cartiglio usano i token `@@N@@` e `@@DOC@@`,
  riempiti da `build.py` in base alla posizione: nucleo `01..18`, appendice `A01..A17`.
  Riordinare o inserire una slide non richiede piu' di toccare i numeri a mano.

- **Editing per id DOM, non per numero visualizzato.** Gli id restano stabili anche quando
  la posizione cambia: `s07_super` e' ancora l'id storico della slide MAPST 4.0, oggi in
  appendice. Per trovare una slide: `grep -n 'id="s..' src/*.html`.

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

## File da consegnare

`standalone.py` chiude i frammenti di `web/` e `review/` in documenti HTML completi, con
doctype, `<head>`, titolo e favicon. Font e immagini sono gia' in base64, quindi i file
funzionano **offline e inoltrati per email**, senza rete e senza cartelle di appoggio:

| File | Cos'e' |
|---|---|
| `DFactory_SalesDeck.html` | il deck, scorrimento verticale semplice |
| `DFactory_SalesDeck_Viewer.html` | il deck col visualizzatore (tastiera, indice a griglia) |
| `DFactory_SalesDeck_Review.html` | la review commerciale, 23 rilievi |
| `DFactory_SalesDeck.pdf` | il deck in PDF, 13.333x7.5in |

I frammenti restano in `web/` e `review/` perche' servono anche alla pubblicazione come
pagina ospitata; `standalone.py` non li modifica, li impacchetta.
