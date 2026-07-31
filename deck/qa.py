#!/usr/bin/env python3
"""
QA automatico sui documenti costruiti, secondo la checklist del master brief §12.

Copre struttura, contenuto, placeholder, stile, grafica e tecnica. Ogni controllo che
puo' essere verificato meccanicamente lo e': i conteggi sono misurati, non stimati.

Uso: python3 deck/qa.py
"""
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
SALES = ROOT.parent / "DFactory_SalesDeck.html"
DOSSIER = ROOT.parent / "DFactory_DossierTecnico.html"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

BANNED = ["world-class", "world class", "seamless", "game-changer", "game changer",
          "disruptive", "packaging-native", "cross-vertical", "go-to-market"]

fails = []


def check(ok: bool, label: str, detail: str = "") -> None:
    print(f"  [{'ok' if ok else '!!'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        fails.append(label)


def plain(html: str) -> str:
    s = re.sub(r"<style.*?</style>", " ", html, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s)


JS_OVERFLOW = """
() => {
  const out = [];
  document.querySelectorAll('section.slide').forEach((sl, idx) => {
    const body = sl.querySelector('.body'), ft = sl.querySelector('.ft');
    if (!body) return;
    const b = body.getBoundingClientRect(), f = ft ? ft.getBoundingClientRect() : null;
    body.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) return;
      if (getComputedStyle(el).position === 'fixed') return;
      let p = el.parentElement, clipped = false;
      while (p && p !== body) {
        if (getComputedStyle(p).overflow === 'hidden') { clipped = true; break; }
        p = p.parentElement;
      }
      if (clipped) return;
      const over = [];
      if (r.bottom > b.bottom + 1.5) over.push('sotto +' + (r.bottom - b.bottom).toFixed(0));
      if (r.right > b.right + 1.5) over.push('destra +' + (r.right - b.right).toFixed(0));
      if (r.left < b.left - 1.5) over.push('sinistra -' + (b.left - r.left).toFixed(0));
      if (f && r.bottom > f.top + 1.5) over.push('CARTIGLIO');
      if (over.length) out.push({slide: idx + 1, id: sl.id, over: over.join(' '),
        txt: (el.textContent || '').trim().slice(0, 46)});
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
      if (!Array.from(el.childNodes).some(n => n.nodeType === 3 && n.textContent.trim())) return;
      if (!isAcid(parse(getComputedStyle(el).color))) return;
      let p = el, bg = null;
      while (p) {
        const c = parse(getComputedStyle(p).backgroundColor);
        if (c.length >= 3 && (c.length < 4 || c[3] > 0.5)) { bg = c; break; }
        p = p.parentElement;
      }
      if (bg && lum(bg) > 0.5)
        out.push({slide: idx + 1, id: sl.id, txt: (el.textContent || '').trim().slice(0, 40)});
    });
  });
  return out;
}
"""

JS_PALETTE = """
() => {
  const parse = s => (s.match(/[\\d.]+/g) || []).map(Number);
  const ok = ([r, g, b, a]) => {
    if (a === 0) return true;
    if (Math.abs(r - 230) < 26 && Math.abs(g - 224) < 26 && Math.abs(b - 17) < 40) return true;
    return (Math.max(r, g, b) - Math.min(r, g, b)) <= 14;
  };
  const seen = {};
  document.querySelectorAll('section.slide *').forEach(el => {
    const cs = getComputedStyle(el);
    ['color', 'backgroundColor', 'borderTopColor', 'borderLeftColor', 'fill', 'stroke'].forEach(prop => {
      const raw = cs[prop];
      if (!raw || raw === 'none') return;
      const c = parse(raw);
      if (c.length >= 3 && !ok(c)) seen[raw + prop] = raw + ' (' + prop + ')';
    });
  });
  return Object.values(seen);
}
"""


def render_checks(path: pathlib.Path, label: str) -> None:
    kw = {"executable_path": CHROME} if pathlib.Path(CHROME).exists() else {}
    with sync_playwright() as p:
        br = p.chromium.launch(**kw)
        pg = br.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=1)
        pg.goto(path.as_uri(), wait_until="networkidle")
        pg.evaluate("() => document.fonts.ready")
        pg.wait_for_timeout(600)
        ov = pg.evaluate(JS_OVERFLOW)
        col = pg.evaluate(JS_COLOR)
        pal = pg.evaluate(JS_PALETTE)
        br.close()
    for r in ov:
        print(f"       s{r['slide']:02d} {r['id']:<20} {r['over']:<18} {r['txt']!r}")
    check(not ov, f"{label}: nessun elemento fuori dall'area di contenuto", f"({len(ov)})")
    for r in col:
        print(f"       s{r['slide']:02d} {r['id']} {r['txt']!r}")
    check(not col, f"{label}: nessun testo giallo su fondo chiaro", f"({len(col)})")
    for r in pal:
        print(f"       {r}")
    check(not pal, f"{label}: nessun colore fuori palette", f"({len(pal)})")


def main() -> None:
    if not (SALES.exists() and DOSSIER.exists()):
        sys.exit("mancano i documenti costruiti: esegui prima deck/build.py")
    sales, dossier = SALES.read_text(encoding="utf-8"), DOSSIER.read_text(encoding="utf-8")
    ts, td = plain(sales), plain(dossier)
    both = ts + " " + td

    print("== STRUTTURA ==")
    n_sales = sales.count("<section data-part=")
    n_dos = dossier.count("<section data-part=")
    check(n_sales == 14, "il sales deck ha esattamente 14 slide", f"({n_sales})")
    check(n_dos == 16, "il dossier tecnico e' un file separato", f"({n_dos} slide)")
    check("Miraitek" not in td and "Zerynth" not in td,
          "il dossier non contiene la matrice competitiva")
    ids = re.findall(r'<section data-part="\w+" class="slide[^"]*" id="([a-z0-9_]+)"', sales)
    check(ids[1] == "s12b_sintesi", "la sintesi e' in posizione 02, non in fondo", f"({ids[1]})")
    first_dash = next((i for i, x in enumerate(ids, 1) if f'id="{x}"' in sales
                       and "dash" in sales.split(f'id="{x}"')[1].split("</section>")[0]), 99)
    check(first_dash <= 5, "la prima screenshot compare entro la slide 05", f"(slide {first_dash})")
    check(ids[-1] == "s29_cta" and ids.count("s29_cta") == 1,
          "il sales deck chiude una volta sola")

    print("\n== CONTENUTO ==")
    check("in via di definizione" in ts and ts.count("Refyn") <= 6,
          "Refyn solo come strato di servizi, sempre flaggato", f"({ts.count('Refyn')} occorrenze)")
    check("s06_refyn" not in sales, "Refyn non ha piu' una slide dedicata")
    check("Quattro forze" not in ts, "la slide 'quattro forze macro' non esiste piu'")
    check("82" not in ts or "85%" not in ts, "nessun benchmark OEE world class")
    check(ts.count("+55%") <= 1, "il dato +55% compare al massimo una volta", f"({ts.count('+55%')})")
    check("Power BI" in ts, "la quinta obiezione (Power BI / fai da te) e' presente")
    check("restano dove sono" in ts or "resta sul tuo server" in ts.lower(),
          "la riga sullo storico che resta al cliente e' presente")
    check("È per te se" in ts, "la qualificazione 'e' per te se' e' esplicita")
    check(ts.count("monitoraggio energetico") == 1,
          "ponte lessicale presente una volta sola", f"({ts.count('monitoraggio energetico')})")
    check("predittiv" not in ts.lower(),
          "nessuna capacita' di roadmap presentata come esistente nel sales deck")
    check("NON DISPONIBILE OGGI" in dossier or "ROADMAP" in dossier,
          "nel dossier la roadmap resta dichiarata come tale")

    print("\n== PLACEHOLDER ==")
    ph = sorted(set(re.findall(r'data-ph="(PH_\d+_[A-Z_]+)"', sales + dossier)))
    check(len(ph) >= 17, "i token PH sono visibili con lo stile placeholder", f"({len(ph)} distinti)")
    check("[[PH_" not in sales and "[[PH_" not in dossier, "nessun token grezzo non renderizzato")
    resid = re.findall(r"\[confermare[^\]]*\]", both)
    check(not resid, "nessun [confermare] residuo fuori dai token PH", f"({len(resid)})")
    print(f"       aperti: {', '.join(t.replace('PH_', '') for t in ph)}")

    print("\n== STILE ==")
    em = re.findall(r"[^\s>]\s*—\s*[^\s<]", both)
    check(not em, "nessun trattino lungo nella prosa", f"({len(em)})")
    nxy = re.findall(r"\bNon\s+(?:è|sono|serve|solo|un|una|il|la|l')[^.!?]*[.!?]\s*(?:È|E|Ma|Il|La)\b", both)
    check(len(nxy) <= 1, "una sola costruzione 'Non X. Y.'", f"({len(nxy)})")
    hits = [w for w in BANNED if re.search(r"\b" + re.escape(w) + r"\b", both, re.I)]
    check(not hits, "nessun termine vietato", f"({', '.join(hits)})" if hits else "")
    mes = re.findall(r"\b(MES|MOM)\b", both)
    check(not mes, "nessuna occorrenza di MES/MOM", f"({len(mes)})")

    print("\n== TECNICA ==")
    for name, html in (("sales", sales), ("dossier", dossier)):
        urls = [u for u in re.findall(r'https?://[^"\')\s]+', html) if "w3.org" not in u]
        check(not urls, f"{name}: nessuna chiamata a CDN", f"({len(urls)})")
        check(html.count("data:font/woff2;base64") == 2, f"{name}: font embeddati")

    print("\n== RENDER ==")
    render_checks(SALES, "sales")
    render_checks(DOSSIER, "dossier")

    print(f"\n=== {'TUTTO OK' if not fails else str(len(fails)) + ' CONTROLLI FALLITI'} ===")
    for f in fails:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
