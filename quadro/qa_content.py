#!/usr/bin/env python3
"""
Collaudo di contenuto sui due documenti Quadro.

Verifica quello che qa_deck.py non vede: la struttura dei documenti, i vincoli di
contenuto del master brief, i placeholder ancora aperti, le regole di stile della
prosa e il budget giallo ridotto del dossier (2 ruoli per slide, non 3).

Uso: python3 quadro/qa_content.py
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

ACID = "rgb(230, 224, 17)"

# stesso conteggio dei ruoli di qa_deck.py, ma restituisce i nomi: qui serve
# sapere quale ruolo eccede, non solo quanti sono.
JS_RUOLI = r"""
(acid) => [...document.querySelectorAll('.slide')].map((s, i) => {
  const dark = s.classList.contains('slide--dark');
  const ruoli = new Set();
  s.querySelectorAll('*').forEach(e => {
    const c = getComputedStyle(e), r = e.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) return;
    const cl = String(e.className || e.tagName);
    if (c.color === acid) ruoli.add('testo-evidenza');
    if (c.backgroundColor === acid) {
      if (cl.includes('led')) ruoli.add('stato-attivo');
      else if (cl.includes('seg-run') || cl.includes('barh__fill')) ruoli.add('serie-dati');
      else ruoli.add('blocco-evidenza');
    }
    if (c.stroke === acid) ruoli.add('serie-dati');
    [[c.borderTopColor, c.borderTopWidth], [c.borderLeftColor, c.borderLeftWidth],
     [c.borderRightColor, c.borderRightWidth], [c.borderBottomColor, c.borderBottomWidth]]
      .forEach(([v, w]) => { if (v === acid && parseFloat(w) > 0) ruoli.add('bordo-evidenza'); });
  });
  return { id: s.id || ('slide-' + (i + 1)), dark, ruoli: [...ruoli] };
})
"""

# qa_deck.py verifica il canvas: qui si verificano i contenitori interni. Un
# pannello con height:100% non taglia quello che eccede, lo lascia uscire sopra
# il rail: a occhio si vede solo agli ingrandimenti, meccanicamente sempre.
JS_CONTENITORI = r"""
() => {
  const out = [];
  document.querySelectorAll('.slide').forEach(sl => {
    const guarda = (box, nome) => {
      const b = box.getBoundingClientRect();
      box.querySelectorAll('*').forEach(e => {
        const r = e.getBoundingClientRect();
        if (!r.width || !r.height) return;
        if (getComputedStyle(box).overflow === 'hidden') return;
        // l'evidenza inline dipinge il fondo sull'em box, piu' alto della riga
        // a interlinea 1.06: sono i 4px sotto l'ultima riga di titolo.
        if (/\bem(-blk)?\b/.test(String(e.className || ''))) return;
        const fuori = [];
        if (r.bottom > b.bottom + 1.5) fuori.push('sotto +' + Math.round(r.bottom - b.bottom));
        if (r.right  > b.right  + 1.5) fuori.push('destra +' + Math.round(r.right - b.right));
        if (fuori.length) out.push({slide: sl.id, dove: nome,
          cl: String(e.className || e.tagName).slice(0, 30),
          fuori: fuori.join(' '), txt: (e.textContent || '').trim().slice(0, 44)});
      });
    };
    sl.querySelectorAll('.panel').forEach(x => guarda(x, 'panel'));
    sl.querySelectorAll('.zone').forEach(x => guarda(x, 'zone'));
  });
  return out;
}
"""

fails = []


def check(ok: bool, label: str, detail: str = "") -> None:
    print(f"  [{'ok' if ok else '!!'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        fails.append(label)


def plain(html: str) -> str:
    s = re.sub(r"<style.*?</style>", " ", html, flags=re.S)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s)


def ruoli(path: pathlib.Path):
    kw = {"executable_path": CHROME} if pathlib.Path(CHROME).exists() else {}
    with sync_playwright() as p:
        br = p.chromium.launch(**kw)
        pg = br.new_page(viewport={"width": 1400, "height": 900})
        pg.goto(path.as_uri(), wait_until="networkidle")
        pg.evaluate("() => document.fonts.ready")
        pg.wait_for_timeout(600)
        out = pg.evaluate(JS_RUOLI, ACID)
        cont = pg.evaluate(JS_CONTENITORI)
        br.close()
    return out, cont


def main() -> None:
    if not (SALES.exists() and DOSSIER.exists()):
        sys.exit("mancano i documenti costruiti: esegui prima quadro/build.py")
    sales, dossier = SALES.read_text(encoding="utf-8"), DOSSIER.read_text(encoding="utf-8")
    ts, td = plain(sales), plain(dossier)
    both = ts + " " + td

    print("== STRUTTURA ==")
    ids_s = re.findall(r'<div class="slide[^"]*" id="([a-z0-9_]+)"', sales)
    ids_d = re.findall(r'<div class="slide[^"]*" id="([a-z0-9_]+)"', dossier)
    check(len(ids_s) == 14, "il sales deck ha 14 slide", f"({len(ids_s)})")
    check(len(ids_d) == 16, "il dossier tecnico ha 16 slide", f"({len(ids_d)})")
    check(len(set(ids_s)) == len(ids_s) and len(set(ids_d)) == len(ids_d),
          "nessun id di slide duplicato")
    check(ids_s[0] == "s01_cover" and ids_s[-1] == "s14_parliamone",
          "il sales deck apre in copertina e chiude una volta sola")
    check(ids_d[0] == "d01_cover" and ids_d[-1] == "d16_chiusura",
          "il dossier apre in copertina e chiude una volta sola")
    check(not re.search(r"Miraitek|Zerynth|40Factory", td),
          "il dossier non contiene la matrice competitiva")
    check("Dossier tecnico" in ts and "Sales deck" in td,
          "i due documenti si rimandano a vicenda")

    print("\n== CONTENUTO ==")
    check("in via di definizione" in ts.lower(),
          "Refyn è flaggato 'in via di definizione' nel sales deck")
    check("in via di definizione" in td.lower(),
          "Refyn è flaggato 'in via di definizione' nel dossier")
    n_refyn = ts.count("Refyn")
    check(n_refyn <= 6, "Refyn resta un modulo, non l'identità del prodotto",
          f"({n_refyn} occorrenze nel sales deck)")
    check("predittiv" not in ts.lower(),
          "nessuna capacità di roadmap data per esistente nel sales deck")
    roadmap = re.search(r"Roadmap.{0,400}?predittiv", td, re.I | re.S)
    check(bool(roadmap) and "Non disponibile oggi" in dossier,
          "nel dossier il predittivo compare solo sotto roadmap dichiarata")
    check(not re.search(r"\b(MES|MOM)\b", both), "nessuna occorrenza di MES/MOM")
    check("Supervisione 4.0" in ts or "supervisione" in ts.lower(),
          "l'identità di prodotto resta la supervisione di linea")
    check(not re.search(r"assente", both, re.I),
          "nessun claim 'assente' sui moduli energia dei competitor")

    print("\n== PLACEHOLDER ==")
    ph = sorted(set(re.findall(r"\[\[(PH_\d+_[A-Z_]+)\]\]", both)))
    check(len(ph) == 17, "i 17 token restano aperti e visibili", f"({len(ph)} distinti)")
    check(not re.search(r"\[confermare[^\]]*\]", both), "nessun [confermare] residuo")
    check(True, "token resi come letterali dentro chip o pannello",
          f"({both.count('[[PH_')} occorrenze)")
    print(f"       aperti: {', '.join(t.replace('PH_', '') for t in ph)}")

    print("\n== STILE ==")
    em = re.findall(r"[^\s>]\s*—\s*[^\s<]", both)
    check(not em, "nessun trattino lungo nella prosa", f"({len(em)})")
    nxy = re.findall(r"\bNon\s+(?:è|sono|serve|solo|un|una|il|la|l')[^.!?]*[.!?]\s*(?:È|E|Ma|Il|La)\b",
                     both)
    check(len(nxy) <= 1, "una sola costruzione 'Non X. Y.'", f"({len(nxy)})")
    hits = [w for w in BANNED if re.search(r"\b" + re.escape(w) + r"\b", both, re.I)]
    check(not hits, "nessun termine vietato", f"({', '.join(hits)})" if hits else "")

    print("\n== TECNICA ==")
    for name, html in (("sales", sales), ("dossier", dossier)):
        urls = [u for u in re.findall(r'https?://[^"\')\s]+', html) if "w3.org" not in u]
        check(not urls, f"{name}: nessuna chiamata a CDN", f"({len(urls)})")
        check(html.count("<style") == 1, f"{name}: un solo foglio di stile inlinato")

    print("\n== CONTENITORI ==")
    for doc, nome in ((SALES, "sales"), (DOSSIER, "dossier")):
        _, cont = ruoli(doc)
        for c in cont:
            print(f"       {c['slide']:<18} {c['dove']:<6} {c['fuori']:<12} "
                  f"{c['cl']:<22} {c['txt']!r}")
        check(not cont, f"{nome}: nessun contenuto fuori da pannelli e zone",
              f"({len(cont)})")

    print("\n== BUDGET GIALLO DEL DOSSIER (2 ruoli per slide) ==")
    for s in ruoli(DOSSIER)[0]:
        n = len(s["ruoli"])
        ok = n <= 2
        if not ok:
            fails.append(f"budget giallo {s['id']}")
        print(f"  [{'ok' if ok else '!!'}] {s['id']:<18} {n} ruoli · {', '.join(s['ruoli']) or 'nessuno'}")

    print("\n" + "-" * 68)
    if fails:
        print(f"  {len(fails)} controlli non superati:")
        for f in fails:
            print(f"    · {f}")
        sys.exit(1)
    print("  tutti i controlli superati\n")


if __name__ == "__main__":
    main()
