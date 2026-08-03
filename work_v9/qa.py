#!/usr/bin/env python3
"""QA tecnico e misure di densita' su un HTML a canvas 1280x720.

Controlla, per ogni .slide:
  - elementi fuori canvas / overflow
  - collisioni fra blocchi di contenuto di primo livello
  - dimensione effettiva minima del testo (inclusi i <text> SVG, scalati dal viewBox)
  - parole visibili e frammenti testuali significativi
  - percentuale di area occupata dal visual dominante
  - errori console e richieste di rete
"""
import sys, json, os
from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

JS = r"""
() => {
  const W = 1280, H = 720;
  const out = [];
  const STOP = new Set(['SCRIPT','STYLE','TITLE','DESC']);

  const visible = el => {
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden' || parseFloat(s.opacity) === 0) return false;
    if (el.getAttribute && el.getAttribute('aria-hidden') === 'true') return false;
    return true;
  };

  for (const slide of document.querySelectorAll('.slide')) {
    const sb = slide.getBoundingClientRect();
    const rec = { id: slide.id, kind: slide.dataset.kind || 'sales', overflow: [],
                  minText: 999, minCont: 999, minMeta: 999, minSvg: 999, minUi: 999,
                  words: 0, wordsUi: 0, wordsMeta: 0, wordsPh: 0, placeholders: 0, fragments: 0,
                  smallText: [], visualPct: 0, collisions: [] };

    // ---- testo: cammina i nodi di testo, misura il corpo effettivo ----
    const seen = [];
    const walk = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walk.nextNode())) {
      const t = n.textContent.replace(/\s+/g, ' ').trim();
      if (!t) continue;
      let p = n.parentElement;
      if (!p || STOP.has(p.tagName.toUpperCase())) continue;
      let hidden = false;
      for (let a = p; a && a !== slide.parentElement; a = a.parentElement) {
        if (!visible(a)) { hidden = true; break; }
      }
      if (hidden) continue;

      // corpo effettivo: per gli SVG applica il fattore di scala del viewBox,
      // cioe' quanto il testo misura davvero sul canvas renderizzato
      let fs = parseFloat(getComputedStyle(p).fontSize);
      const svg = p.ownerSVGElement || (p.tagName.toLowerCase() === 'svg' ? p : null);
      if (svg) {
        const vb = svg.viewBox && svg.viewBox.baseVal;
        if (vb && vb.width) fs = fs * (svg.getBoundingClientRect().width / vb.width);
      }
      fs = Math.round(fs * 10) / 10;

      // quattro popolazioni distinte, con soglie diverse:
      //   ui    testo dentro una vista di prodotto: e' il contenuto della
      //         schermata, non il messaggio della slide. Uno screenshot vero
      //         porta le sue etichette e nessuno le conta come copy.
      //   svg   testo dentro un diagramma, misurato dopo la scala del viewBox
      //   meta  intestazione, piede, numerazione, filigrana, note di margine
      //   cont  tutto il resto, cioe' il testo che parla al lettore
      const isUi = !!p.closest('svg[data-ui]');
      // impalcatura editoriale della working edition: e' metadato sul documento,
      // non testo del documento. Nella client edition non esiste.
      const isPh = !!p.closest('[data-ed="working"]');
      const isMeta = !!(p.closest('.hd, .ft, .rail, .note') ||
                        p.classList.contains('note') || p.classList.contains('pg') ||
                        p.classList.contains('wm'));
      const bucket = isPh ? 'ph' : (isUi ? 'ui' : (svg ? 'svg' : (isMeta ? 'meta' : 'cont')));
      rec.minText = Math.min(rec.minText, fs);
      if (bucket === 'ui')   rec.minUi   = Math.min(rec.minUi, fs);
      if (bucket === 'svg')  rec.minSvg  = Math.min(rec.minSvg, fs);
      if (bucket === 'meta') rec.minMeta = Math.min(rec.minMeta, fs);
      if (bucket === 'cont') rec.minCont = Math.min(rec.minCont, fs);
      // la soglia dipende dal tipo di canvas e dalla popolazione: filtrata lato Python
      if (fs < 15) rec.smallText.push([t.slice(0, 40), fs, bucket]);

      // il copy e' quello che parla al lettore: non il testo di una schermata,
      // non la filigrana e il piede che stanno su ogni slide
      const words = t.split(/\s+/).filter(w => /[\p{L}\p{N}]/u.test(w));
      rec.words += words.length;
      if (bucket === 'ui') rec.wordsUi += words.length;
      if (bucket === 'meta') rec.wordsMeta += words.length;
      if (bucket === 'ph') rec.wordsPh += words.length;
      const ph = t.match(/\{\{PH_[A-Z0-9_]+\}\}/g);
      if (ph) rec.placeholders += ph.length;
      seen.push(t);
    }
    rec.fragments = seen.length;

    // ---- overflow rispetto al canvas ----
    for (const el of slide.querySelectorAll('*')) {
      if (STOP.has(el.tagName.toUpperCase())) continue;
      if (el.ownerSVGElement) continue;            // il clipping SVG e' gestito dal viewBox
      if (!visible(el)) continue;
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) continue;
      const dx = Math.max(0, sb.left - r.left, r.right - sb.right);
      const dy = Math.max(0, sb.top - r.top, r.bottom - sb.bottom);
      if (dx > 1.5 || dy > 1.5) {
        rec.overflow.push({ tag: el.tagName, cls: el.className.baseVal || el.className || '',
                            dx: Math.round(dx), dy: Math.round(dy),
                            txt: (el.textContent || '').replace(/\s+/g,' ').trim().slice(0, 45) });
      }
    }

    // ---- collisioni fra blocchi di primo livello ----
    // .co = callout, sovrapposto alla vista per definizione: non e' una collisione
    // il rail non e' piu' escluso: un blocco che gli finisce sopra e' una
    // collisione come le altre, e nella v8 e' successo davvero
    const blocks = [...slide.children].filter(e => visible(e)
        && !e.classList.contains('co') && !e.classList.contains('co__n'))
      .map(e => ({ e, r: e.getBoundingClientRect() }))
      .filter(b => b.r.width > 2 && b.r.height > 2);
    for (let i = 0; i < blocks.length; i++) {
      for (let j = i + 1; j < blocks.length; j++) {
        const a = blocks[i].r, b = blocks[j].r;
        const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (ox > 4 && oy > 4) {
          // ignora se uno dei due non ha testo proprio (fondali, griglie)
          const at = (blocks[i].e.textContent || '').trim();
          const bt = (blocks[j].e.textContent || '').trim();
          if (at && bt) rec.collisions.push({
            a: blocks[i].e.className.baseVal || blocks[i].e.className || blocks[i].e.tagName,
            b: blocks[j].e.className.baseVal || blocks[j].e.className || blocks[j].e.tagName,
            ox: Math.round(ox), oy: Math.round(oy),
            at: at.replace(/\s+/g,' ').slice(0,30), bt: bt.replace(/\s+/g,' ').slice(0,30) });
        }
      }
    }

    // ---- area del visual dominante ----
    // Nel dossier una matrice conta come visual: e' la forma in cui la pagina
    // presenta l'informazione, non prosa impaginata.
    // Riquadro di ingombro dell'unione: una pagina con due visual impilati
    // (diagramma + matrice) non deve essere misurata sul solo piu' grande.
    let bb = null;
    for (const el of slide.querySelectorAll('svg, .viz, .mx')) {
      // un visual marcato aria-hidden e' comunque visibile all'occhio: qui
      // conta l'area occupata, non l'esposizione agli screen reader
      const s = getComputedStyle(el);
      if (s.display === 'none' || s.visibility === 'hidden') continue;
      if (el.getAttribute('aria-hidden') === 'true' && !el.classList.contains('viz')) {
        if (!el.closest('.viz')) continue;   // svg decorativi solo dentro un .viz
      }
      const r = el.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) continue;
      bb = bb ? { l: Math.min(bb.l, r.left), t: Math.min(bb.t, r.top),
                  r: Math.max(bb.r, r.right), b: Math.max(bb.b, r.bottom) }
              : { l: r.left, t: r.top, r: r.right, b: r.bottom };
    }
    const area = bb ? (bb.r - bb.l) * (bb.b - bb.t) : 0;
    // misurata sull'intero canvas, non su un'area utile ridotta: e' la
    // quota di superficie della slide occupata da interfacce, grafici,
    // timeline o numeri, cioe' la grandezza che il brief mette a target
    rec.visualPct = Math.round(area / (1280 * 720) * 1000) / 10;
    out.push(rec);
  }
  return out;
}
"""


def run(html):
    console, requests = [], []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': 1280, 'height': 720})
        pg.on('console', lambda m: console.append(f'{m.type}: {m.text}') if m.type in ('error',) else None)
        pg.on('request', lambda r: requests.append(r.url) if not r.url.startswith(('file://', 'data:')) else None)
        pg.goto('file://' + os.path.abspath(html), wait_until='networkidle')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(500)
        data = pg.evaluate(JS)
        # link interni
        anchors = pg.eval_on_selector_all('a[href^="#"]', 'a => a.map(x => x.getAttribute("href"))')
        ids = pg.eval_on_selector_all('[id]', 'e => e.map(x => x.id)')
        # apostrofi e accenti: il controllo include title e desc degli SVG, che sono
        # invisibili a schermo ma fanno parte del documento e li legge lo screen reader
        texts = pg.evaluate(r"""() => {
          const out = [];
          for (const s of document.querySelectorAll('.slide'))
            for (const n of s.querySelectorAll('title, desc, *'))
              if (n.children.length === 0 && n.textContent.trim())
                out.push([s.id, n.tagName.toLowerCase(), n.textContent.replace(/\s+/g,' ').trim()]);
          return out;
        }""")
        b.close()
    broken = [a for a in anchors if a[1:] not in ids]
    typo = [(sid, tag, t) for sid, tag, t in texts
            if "'" in t or any(x in t for x in ("e' ", "a' ", "i' ", "o' ", "u' "))]
    return data, console, requests, broken, ids, typo


# soglie per tipo di canvas:
#   (max parole, target, % visual minima, min contenuti, min metadati, min SVG)
# Il corpo minimo si misura su tre popolazioni distinte, perche' hanno funzioni
# diverse: il contenuto si legge in proiezione, i metadati si consultano da vicino,
# il testo SVG va misurato dopo la scala del viewBox e non come e' scritto nel file.
# (max parole di copy, target, % visual minima, min contenuti, min metadati,
#  min diagrammi, min viste di prodotto)
# Il tetto di parole vale sul copy: il testo dentro una vista di prodotto e'
# parte della schermata, come in uno screenshot vero, e si misura a parte.
# Deck: contenuti >= 15 px, diagrammi >= 14 px, viste >= 11,5 px, metadati >= 12,4 px.
# Dossier: contenuti >= 14 px come da brief, diagrammi >= 13 px.
LIMITS = {'sales':    (45,  '<=45',  55, 18.0, 12.4, 14.0, 12.0),
          'dossier':  (140, '<=140',  0, 14.0, 12.4, 13.0, 12.0),
          'appendix': (140, '<=140',  0, 14.0, 12.4, 13.0, 12.0)}


def report(html, default='sales'):
    data, console, reqs, broken, ids, typo = run(html)
    print(f'\n=== {os.path.basename(html)} · {len(data)} canvas ===')
    print(f'console errors: {console or "none"} · network requests: {reqs or "none"} '
          f'· broken anchors: {broken or "none"} · duplicate ids: '
          f'{ {i for i in ids if ids.count(i)>1} or "none"}')
    print(f'apostrofi diritti o accenti scritti con apostrofo: {len(typo) or "nessuno"}')
    for sid, tag, t in typo[:6]:
        print(f'      ! {sid} <{tag}> "{t[:70]}"')
    print(f'{"id":26s}{"copy":>6}{"vista":>6}{"ph":>4}{"cont":>7}{"meta":>7}{"diag":>7}'
          f'{"vista":>7}{"vis%":>7}  flags')
    tot = 0
    bad = 0
    for r in data:
        wmax, wtarget, vmin, cmin, mmin, smin, umin = LIMITS[r.get('kind', default)]
        # l'impalcatura working non ha soglia: non e' testo del documento
        floor = {'cont': cmin, 'meta': mmin, 'svg': smin, 'ui': umin, 'ph': 0}
        # filtra il testo piccolo con la soglia della sua popolazione
        r['smallText'] = [s for s in r['smallText'] if s[1] < floor[s[2]]]
        copy = r['words'] - r['wordsUi'] - r['wordsMeta'] - r['wordsPh']
        flags = []
        if r['overflow']: flags.append(f'OVERFLOW×{len(r["overflow"])}')
        if r['collisions']: flags.append(f'COLLIS×{len(r["collisions"])}')
        if copy > wmax: flags.append(f'copy>{wmax}')
        if r['minCont'] < cmin: flags.append(f'cont<{cmin}')
        if r['minMeta'] < mmin: flags.append(f'meta<{mmin}')
        if r['minSvg'] < smin: flags.append(f'diag<{smin}')
        if r['minUi'] < umin: flags.append(f'vista<{umin}')
        if r['visualPct'] < vmin: flags.append(f'visual<{vmin}%')
        if flags: bad += 1
        tot += copy
        fmt = lambda v: '—' if v == 999 else f'{v}'
        print(f'{r["id"]:26s}{copy:>6}{r["wordsUi"]:>6}{r["placeholders"]:>4}{fmt(r["minCont"]):>7}'
              f'{fmt(r["minMeta"]):>7}{fmt(r["minSvg"]):>7}{fmt(r["minUi"]):>7}'
              f'{r["visualPct"]:>7}  {" ".join(flags)}')
        for o in r['overflow'][:4]:
            print(f'      ! overflow {o["tag"]}.{o["cls"]} dx={o["dx"]} dy={o["dy"]} "{o["txt"]}"')
        for c in r['collisions'][:4]:
            print(f'      ! collisione {c["a"]} / {c["b"]} {c["ox"]}×{c["oy"]}px '
                  f'"{c["at"]}" ~ "{c["bt"]}"')
        for s in r['smallText'][:4]:
            print(f'      ! testo {s[2]} {s[1]}px "{s[0]}"')
    nph = sum(r['placeholders'] for r in data)
    print(f'--- media parole: {tot/len(data):.0f} · canvas con flag: {bad}/{len(data)} '
          f'· placeholder visibili: {nph}')
    return data


if __name__ == '__main__':
    d = report(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'sales')
    if len(sys.argv) > 3:
        json.dump(d, open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
