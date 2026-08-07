#!/usr/bin/env python3
"""QA del dossier A4 V9.4.

Il QA della V9.3 misurava canvas 1280x720 con contenuto in posizione assoluta:
li' i difetti erano collisioni e sovrapposizioni. Qui il contenuto scorre, e i
difetti sono altri — una pagina che sfora, un blocco che finisce addosso al
piede, un corpo sceso sotto la soglia di leggibilita' alla distanza di lettura
di un A4. Le soglie tipografiche sono piu' basse di quelle del deck e la
ragione e' dichiarata: un dossier si legge a trenta centimetri, un deck si
guarda proiettato a cinque metri.

  qa94.py <file.html> [altri.html ...]
"""
import json
import os
import sys

from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
W, H = 794, 1123

# soglie di corpo, in px effettivi
MIN = {'cont': 12.0, 'meta': 10.4, 'svg': 10.9, 'ui': 10.9, 'ph': 9.9}
# distanza minima fra l'ultimo blocco di contenuto e il piede di pagina
STACCO_PIEDE = 10.0

JS = r"""
() => {
  const out = [];
  const pagine = [...document.querySelectorAll('.page')];
  for (const pg of pagine) {
    const r = pg.getBoundingClientRect();
    const rec = {id: pg.id, w: Math.round(r.width), h: Math.round(r.height),
                 scuro: pg.classList.contains('dk'),
                 sfora: [], corpi: [], staccoPiede: null, skim: false,
                 visivi: 0, parole: {cont: 0, meta: 0, svg: 0, ui: 0, ph: 0}};

    rec.skim = !!pg.querySelector('.skim .who') && !!pg.querySelector('.skim .gist');
    rec.visivi = pg.querySelectorAll('svg, table, .stack, .attr, .seq, .idx, .nums, .fig, .ls').length;

    // 1 · niente deve uscire dalla pagina
    for (const e of pg.querySelectorAll('*')) {
      const b = e.getBoundingClientRect();
      if (b.width === 0 && b.height === 0) continue;
      const st = getComputedStyle(e);
      if (st.visibility === 'hidden' || st.display === 'none') continue;
      const d = Math.max(r.left - b.left, b.right - r.right,
                         r.top - b.top, b.bottom - r.bottom);
      if (d > 0.6) rec.sfora.push({tag: e.tagName.toLowerCase(),
        cls: (e.className.baseVal !== undefined ? e.className.baseVal : e.className) || '',
        px: +d.toFixed(1)});
    }

    // 2 · il contenuto non deve finire addosso al piede
    const piede = pg.querySelector('.ft');
    if (piede) {
      const rp = piede.getBoundingClientRect();
      let giu = r.top;
      for (const e of pg.children) {
        if (e.classList.contains('ft') || e.classList.contains('phb')) continue;
        const b = e.getBoundingClientRect();
        if (b.height === 0) continue;
        giu = Math.max(giu, b.bottom);
      }
      rec.staccoPiede = +(rp.top - giu).toFixed(1);
    }

    // 3 · corpo effettivo di ogni blocco di testo, e conteggio parole
    const scalaSvg = e => {
      const s = e.closest('svg');
      if (!s) return 1;
      const vb = s.viewBox && s.viewBox.baseVal;
      if (!vb || !vb.width) return 1;
      return s.getBoundingClientRect().width / vb.width;
    };
    // un numero d'ordine dentro un elenco non e' testo di contenuto: e'
    // un'ancora. Contarlo come corpo faceva scattare la soglia sbagliata.
    const meta = e => {
      const tag = e.tagName.toLowerCase();
      if (e.closest('.lbl, .pg, .nav, .ft, .note, .who, .dev, .phb')) return true;
      if (e.classList.contains('phv')) return true;
      if (['th', 'u', 'em'].includes(tag)) return true;
      if (e.classList.contains('ar')) return true;
      if (tag === 'b' && e.closest('.ls, .idx, .fig, .nums, .attr')) return true;
      return false;
    };
    for (const e of pg.querySelectorAll('*')) {
      let testo = '';
      for (const n of e.childNodes)
        if (n.nodeType === 3) testo += n.nodeValue;
      testo = testo.trim();
      if (!testo) continue;
      const st = getComputedStyle(e);
      if (st.visibility === 'hidden' || st.display === 'none') continue;
      const dentroSvg = !!e.closest('svg');
      const ui = !!e.closest('svg[data-ui]');
      const px = +(parseFloat(st.fontSize) * (dentroSvg ? scalaSvg(e) : 1)).toFixed(2);
      const bucket = e.closest('.phb') ? 'ph'
                   : ui ? 'ui'
                   : dentroSvg ? 'svg'
                   : meta(e) ? 'meta' : 'cont';
      const n = testo.split(/\s+/).filter(w => /[0-9A-Za-zÀ-ſ]/.test(w)).length;
      rec.parole[bucket] += n;
      rec.corpi.push({px, bucket,
        t: testo.slice(0, 38).replace(/\s+/g, ' ')});
    }
    out.push(rec);
  }
  return out;
}
"""


def analizza(path):
    url = 'file://' + os.path.abspath(path)
    console, rete = [], []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': W + 60, 'height': 1000})
        pg.on('console', lambda m: console.append(f'{m.type}: {m.text}')
              if m.type in ('error', 'warning') else None)
        pg.on('request', lambda r: rete.append(r.url)
              if not r.url.startswith(('file://', 'data:')) else None)
        pg.goto(url, wait_until='networkidle')
        pg.wait_for_timeout(350)
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(350)
        dati = pg.evaluate(JS)
        b.close()
    return dati, console, rete


def report(path):
    dati, console, rete = analizza(path)
    nome = os.path.basename(path)
    print(f'\n{"="*78}\n{nome} · {len(dati)} pagine A4')
    difetti = []

    for r in dati:
        prob = []
        if (r['w'], r['h']) != (W, H):
            prob.append(f'formato {r["w"]}x{r["h"]} invece di {W}x{H}')
        for s in r['sfora'][:4]:
            prob.append(f'fuori pagina {s["px"]}px · {s["tag"]}.{s["cls"][:24]}')
        if r['staccoPiede'] is not None and r['staccoPiede'] < STACCO_PIEDE:
            prob.append(f'stacco dal piede {r["staccoPiede"]}px (minimo {STACCO_PIEDE})')
        piccoli = {}
        for c in r['corpi']:
            if c['px'] < MIN[c['bucket']] - .01:
                piccoli.setdefault((c['bucket'], c['px']), c['t'])
        for (bucket, px), t in sorted(piccoli.items())[:4]:
            prob.append(f'corpo {px}px sotto {MIN[bucket]} [{bucket}] «{t}»')
        if r['id'] not in ('p01_cover', 'p18_chiusura') and not r['skim']:
            prob.append('riga di scrematura assente')
        # copertina e chiusura non hanno un visivo: sono la pagina stessa
        if not r['visivi'] and r['id'] not in ('p01_cover', 'p18_chiusura'):
            prob.append('nessun elemento visivo')
        if prob:
            difetti.append((r['id'], prob))

    scure = [r['id'] for r in dati if r['scuro']]
    print(f'  pagine scure: {len(scure)} · {", ".join(scure)}')
    if not 3 <= len(scure) <= 5:
        difetti.append(('sequenza', [f'pagine scure {len(scure)}, fuori 3-5']))

    # §9.5 · mai quattro pagine di fila senza un elemento visivo forte
    secco = 0
    for r in dati:
        secco = 0 if (r['visivi'] or r['scuro']) else secco + 1
        if secco >= 4:
            difetti.append(('sequenza', [f'quattro pagine senza visivo fino a {r["id"]}']))
            secco = 0

    minimo = min(r['staccoPiede'] for r in dati if r['staccoPiede'] is not None)
    print(f'  stacco minimo dal piede: {minimo}px')
    corpi = [c['px'] for r in dati for c in r['corpi'] if c['bucket'] == 'cont']
    print(f'  corpo minimo del testo di contenuto: {min(corpi)}px')
    print(f'  richieste di rete: {len(rete)} · console: {len(console)}')
    if rete:
        difetti.append(('build', [f'{len(rete)} richieste di rete: {rete[:3]}']))
    if console:
        difetti.append(('build', [f'console: {console[:3]}']))

    if difetti:
        print(f'  DIFETTI · {sum(len(p) for _, p in difetti)}')
        for pid, prob in difetti:
            for x in prob:
                print(f'    {pid:22s} {x}')
    else:
        print('  0 difetti')
    return difetti, dati


if __name__ == '__main__':
    tot = 0
    riassunto = {}
    for f in sys.argv[1:]:
        d, dati = report(f)
        tot += sum(len(p) for _, p in d)
        riassunto[os.path.basename(f)] = {'pagine': len(dati),
                                          'difetti': sum(len(p) for _, p in d)}
    print(f'\n{"="*78}\nTOTALE DIFETTI: {tot}')
    print(json.dumps(riassunto, indent=2, ensure_ascii=False))
    sys.exit(1 if tot else 0)
