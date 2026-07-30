#!/usr/bin/env python3
"""
QA automatico sul deck costruito.

1. OVERFLOW  : elementi che escono dall'area di contenuto (.body) o invadono il cartiglio.
2. COLORE    : testo giallo su fondo chiaro (vietato dalle regole brand).
3. PALETTE   : colori fuori palette (solo giallo/nero/bianco + grigi neutri).
4. TERMINI   : termini banditi e residui di brand/palette vecchi.

Uso: python3 deck/qa.py
"""
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
HTML = ROOT.parent / "DFactory_SalesDeck.html"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

ACID = (230, 224, 17)

BANNED = ["world-class", "seamless", "game-changer", "game changer", "disruptive",
          "packaging-native", "cross-vertical", "go-to-market", "MES", "MOM"]
STALE = ["Refyn è la", "Refyn si adatta", "Refyn integra", "Refyn nasce", "Refyn Production",
         "Refyn Energy", "REF-SLS", "cadmio", "#f0ede4", "#f2efe6", "bone"]

JS_OVERFLOW = """
() => {
  const out = [];
  document.querySelectorAll('section.slide').forEach((sl, idx) => {
    const body = sl.querySelector('.body');
    const ft = sl.querySelector('.ft');
    if (!body) return;
    const b = body.getBoundingClientRect();
    const f = ft ? ft.getBoundingClientRect() : null;
    body.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return;
      const cs = getComputedStyle(el);
      if (cs.position === 'fixed' || cs.overflow === 'hidden') return;
      // ignora figli di contenitori con overflow hidden (mockup in scala)
      let p = el.parentElement, clipped = false;
      while (p && p !== body) {
        if (getComputedStyle(p).overflow === 'hidden') { clipped = true; break; }
        p = p.parentElement;
      }
      if (clipped) return;
      const over = [];
      if (r.bottom > b.bottom + 1.5) over.push('bottom +' + (r.bottom - b.bottom).toFixed(0));
      if (r.right > b.right + 1.5) over.push('right +' + (r.right - b.right).toFixed(0));
      if (r.left < b.left - 1.5) over.push('left -' + (b.left - r.left).toFixed(0));
      if (f && r.bottom > f.top + 1.5) over.push('CARTIGLIO');
      if (over.length) {
        out.push({slide: idx + 1, id: sl.id, tag: el.tagName.toLowerCase(),
                  cls: (el.className || '').toString().slice(0, 40),
                  txt: (el.textContent || '').trim().slice(0, 48), over: over.join(' ')});
      }
    });
  });
  return out;
}
"""

JS_COLOR = """
() => {
  const parse = s => (s.match(/[\\d.]+/g) || []).map(Number);
  const lum = ([r, g, b]) => (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;
  const isAcid = ([r, g, b]) => Math.abs(r - 230) < 26 && Math.abs(g - 224) < 26 && Math.abs(b - 17) < 40;
  const out = [];
  document.querySelectorAll('section.slide').forEach((sl, idx) => {
    sl.querySelectorAll('*').forEach(el => {
      if (!(el.textContent || '').trim()) return;
      const hasOwnText = Array.from(el.childNodes)
        .some(n => n.nodeType === 3 && n.textContent.trim());
      if (!hasOwnText) return;
      const cs = getComputedStyle(el);
      const col = parse(cs.color);
      if (!isAcid(col)) return;
      // primo antenato con background opaco
      let p = el, bg = null;
      while (p) {
        const c = parse(getComputedStyle(p).backgroundColor);
        if (c.length >= 3 && (c.length < 4 || c[3] > 0.5)) { bg = c; break; }
        p = p.parentElement;
      }
      if (bg && lum(bg) > 0.5) {
        out.push({slide: idx + 1, id: sl.id, txt: (el.textContent || '').trim().slice(0, 44),
                  color: cs.color, bg: getComputedStyle(p).backgroundColor});
      }
    });
  });
  return out;
}
"""

JS_PALETTE = """
() => {
  const parse = s => (s.match(/[\\d.]+/g) || []).map(Number);
  const ok = ([r, g, b, a]) => {
    if (a !== undefined && a === 0) return true;
    if (Math.abs(r - 230) < 26 && Math.abs(g - 224) < 26 && Math.abs(b - 17) < 40) return true; // acid
    const mx = Math.max(r, g, b), mn = Math.min(r, g, b);
    return (mx - mn) <= 14; // neutro: nero/bianco/grigio
  };
  const seen = {};
  document.querySelectorAll('section.slide *').forEach(el => {
    const cs = getComputedStyle(el);
    ['color', 'backgroundColor', 'borderTopColor', 'borderLeftColor', 'fill', 'stroke']
      .forEach(prop => {
        const raw = cs[prop];
        if (!raw || raw === 'none') return;
        const c = parse(raw);
        if (c.length < 3) return;
        if (!ok(c)) {
          const sl = el.closest('section.slide');
          const k = raw + '|' + prop;
          seen[k] = seen[k] || {color: raw, prop: prop, count: 0, where: sl ? sl.id : '?'};
          seen[k].count++;
        }
      });
  });
  return Object.values(seen);
}
"""


def main() -> None:
    src = HTML.read_text(encoding="utf-8")
    problems = 0

    print("== TERMINI / RESIDUI ==")
    text_only = re.sub(r"<style.*?</style>", "", src, flags=re.S)
    text_only = re.sub(r"<[^>]+>", " ", text_only)
    for w in BANNED + STALE:
        hits = len(re.findall(r"\b" + re.escape(w) + r"\b", text_only, re.I))
        if hits:
            print(f"  ! '{w}' x{hits}")
            problems += hits
    # em-dash in prosa
    for m in re.finditer(r"[^\s>]\s*—\s*[^\s<]", text_only):
        print(f"  ! em-dash: ...{m.group(0)}...")
        problems += 1
    n_non = len(re.findall(r"\bNon\s+(?:è|sono|serve|solo|un|una|il|la|l')[^.!?]*[.!?]\s*(?:È|E|Ma|Il|La)\b",
                           text_only))
    print(f"  costruzioni 'Non X. Y.' rilevate: {n_non} (max consentito 1)")
    if n_non > 1:
        problems += 1
    n_refyn = len(re.findall("Refyn", text_only))
    n_df = len(re.findall(r"D\.Factory", text_only))
    print(f"  occorrenze 'Refyn': {n_refyn} | 'D.Factory': {n_df}")

    kw = {"executable_path": CHROME} if pathlib.Path(CHROME).exists() else {}
    with sync_playwright() as p:
        br = p.chromium.launch(**kw)
        pg = br.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
        pg.goto(HTML.as_uri(), wait_until="networkidle")
        pg.evaluate("() => document.fonts.ready")
        pg.wait_for_timeout(600)

        print("\n== OVERFLOW ==")
        rows = pg.evaluate(JS_OVERFLOW)
        for r in rows:
            print(f"  ! s{r['slide']:02d} {r['id']:<20} {r['over']:<22} "
                  f".{r['cls'][:26]:<26} {r['txt']!r}")
        print(f"  totale: {len(rows)}")
        problems += len(rows)

        print("\n== TESTO GIALLO SU FONDO CHIARO ==")
        rows = pg.evaluate(JS_COLOR)
        for r in rows:
            print(f"  ! s{r['slide']:02d} {r['id']} {r['txt']!r} su {r['bg']}")
        print(f"  totale: {len(rows)}")
        problems += len(rows)

        print("\n== COLORI FUORI PALETTE ==")
        rows = pg.evaluate(JS_PALETTE)
        for r in sorted(rows, key=lambda x: -x["count"]):
            print(f"  ! {r['color']:<26} {r['prop']:<16} x{r['count']:<4} (es. {r['where']})")
        print(f"  totale distinti: {len(rows)}")
        problems += len(rows)
        br.close()

    print(f"\n=== PROBLEMI TOTALI: {problems} ===")
    sys.exit(0)


if __name__ == "__main__":
    main()
