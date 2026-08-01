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
                  minText: 999, words: 0, fragments: 0,
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

      // corpo effettivo: per gli SVG applica il fattore di scala del viewBox
      let fs = parseFloat(getComputedStyle(p).fontSize);
      const svg = p.ownerSVGElement || (p.tagName.toLowerCase() === 'svg' ? p : null);
      if (svg) {
        const vb = svg.viewBox && svg.viewBox.baseVal;
        if (vb && vb.width) fs = fs * (svg.getBoundingClientRect().width / vb.width);
      }
      rec.minText = Math.min(rec.minText, Math.round(fs * 10) / 10);
      // la soglia dipende dal tipo di canvas: filtrata lato Python
      const isNote = !!(p.closest('.note') || p.classList.contains('note'));
      if (fs < 12.5) rec.smallText.push([t.slice(0, 40), Math.round(fs * 10) / 10, isNote]);

      const words = t.split(/\s+/).filter(w => /[\p{L}\p{N}]/u.test(w));
      rec.words += words.length;
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
    const blocks = [...slide.children].filter(e => visible(e)
        && !e.classList.contains('rail')
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
    // "area utile" = canvas meno margini laterali e fasce di rail
    rec.visualPct = Math.round(area / (1152 * 600) * 1000) / 10;
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
        b.close()
    broken = [a for a in anchors if a[1:] not in ids]
    return data, console, requests, broken, ids


# soglie per tipo di canvas:
#   (max parole, target, % visual minima, px minimi, px minimi per label/tabella)
# Sales: label >= 12,5 px · note 11-12 px.
# Dossier: corpo >= 13,5 px · label e tabelle >= 11,5 px.
LIMITS = {'sales':    (70,  '40-60',  50, 11.0, 12.4),
          'dossier':  (165, '95-135', 38, 11.0, 11.4),
          'appendix': (170, '—',       0, 11.0, 11.4)}


def report(html, default='sales'):
    data, console, reqs, broken, ids = run(html)
    print(f'\n=== {os.path.basename(html)} · {len(data)} canvas ===')
    print(f'console errors: {console or "none"} · network requests: {reqs or "none"} '
          f'· broken anchors: {broken or "none"} · duplicate ids: '
          f'{ {i for i in ids if ids.count(i)>1} or "none"}')
    print(f'{"id":34s}{"words":>6}{"frag":>6}{"minpx":>7}{"vis%":>7}  flags')
    tot = 0
    bad = 0
    for r in data:
        wmax, wtarget, vmin, tmin, lmin = LIMITS[r.get('kind', default)]
        # filtra il testo piccolo con la soglia del tipo di canvas
        r['smallText'] = [s for s in r['smallText']
                          if s[1] < (10.9 if s[2] else lmin)]
        flags = []
        if r['overflow']: flags.append(f'OVERFLOW×{len(r["overflow"])}')
        if r['collisions']: flags.append(f'COLLIS×{len(r["collisions"])}')
        if r['words'] > wmax: flags.append(f'words>{wmax}')
        if r['minText'] < tmin: flags.append(f'text<{tmin}')
        if r['smallText']: flags.append(f'small×{len(r["smallText"])}')
        if r['visualPct'] < vmin: flags.append(f'visual<{vmin}%')
        if flags: bad += 1
        tot += r['words']
        print(f'{r["id"]:34s}{r["words"]:>6}{r["fragments"]:>6}{r["minText"]:>7}'
              f'{r["visualPct"]:>7}  {" ".join(flags)}')
        for o in r['overflow'][:4]:
            print(f'      ! overflow {o["tag"]}.{o["cls"]} dx={o["dx"]} dy={o["dy"]} "{o["txt"]}"')
        for c in r['collisions'][:4]:
            print(f'      ! collisione {c["a"]} / {c["b"]} {c["ox"]}×{c["oy"]}px '
                  f'"{c["at"]}" ~ "{c["bt"]}"')
        for s in r['smallText'][:4]:
            print(f'      ! testo {s[1]}px "{s[0]}"')
    print(f'--- media parole: {tot/len(data):.0f} · canvas con flag: {bad}/{len(data)}')
    return data


if __name__ == '__main__':
    d = report(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'sales')
    if len(sys.argv) > 3:
        json.dump(d, open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
