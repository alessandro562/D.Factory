#!/usr/bin/env python3
"""
QA automatico del sistema di design D.Factory "Quadro".

Uso:
    python3 qa_deck.py percorso/al/deck.html

Controlla, per ogni elemento con classe .slide:
  1. che nessun contenuto esca dal canvas 1280x720
  2. che i ruoli del giallo siano al massimo 3 per slide
  3. che non ci sia mai testo giallo su fondo chiaro
  4. che nessun testo scenda sotto 9.5px
  5. che non esistano border-radius (unica eccezione: .led)
  6. che non esistano ombre (unica eccezione: .led)
  7. che rail superiore e inferiore siano presenti
  8. che il ritmo chiaro/scuro non produca piu di 3 slide chiare consecutive

Esce con codice 1 se trova anche una sola violazione.
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

ACID = "rgb(230, 224, 17)"

JS = r"""
(acid) => {
  const slides = [...document.querySelectorAll('.slide')];
  return slides.map((s, i) => {
    const sr = s.getBoundingClientRect();
    const dark = s.classList.contains('slide--dark');
    const id = s.id || ('slide-' + (i + 1));
    const ruoli = new Set();
    const fuoriCampo = [], gialloSuChiaro = [], radius = [], ombre = [], piccoli = [];

    s.querySelectorAll('*').forEach(e => {
      const c = getComputedStyle(e), r = e.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) return;
      const cl = String(e.className || e.tagName);
      const isLed = cl.includes('led');
      const isBg  = cl.includes('grid-bg');

      // 1. fuori campo
      const t = r.top - sr.top, l = r.left - sr.left;
      const b = r.bottom - sr.top, ri = r.right - sr.left;
      if (!isBg && (b > 720.5 || ri > 1280.5 || t < -0.5 || l < -0.5)) {
        fuoriCampo.push(cl + ` [t${Math.round(t)} l${Math.round(l)} b${Math.round(b)} r${Math.round(ri)}]`);
      }

      // 2-3. giallo
      if (c.color === acid) {
        ruoli.add('testo-evidenza');
        if (!dark && e.textContent.trim().length > 0) gialloSuChiaro.push(cl);
      }
      if (c.backgroundColor === acid) {
        if (isLed) ruoli.add('stato-attivo');
        else if (cl.includes('seg-run') || cl.includes('barh__fill')) ruoli.add('serie-dati');
        else ruoli.add('blocco-evidenza');
      }
      if (c.stroke === acid) ruoli.add('serie-dati');
      [[c.borderTopColor, c.borderTopWidth], [c.borderLeftColor, c.borderLeftWidth],
       [c.borderRightColor, c.borderRightWidth], [c.borderBottomColor, c.borderBottomWidth]]
        .forEach(([v, w]) => { if (v === acid && parseFloat(w) > 0) ruoli.add('bordo-evidenza'); });

      // 4. corpo minimo
      const fs = parseFloat(c.fontSize);
      const haTesto = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 0);
      if (haTesto && fs < 9.5) piccoli.push(cl + ' ' + fs + 'px');

      // 5-6. raggi e ombre
      if (!isLed && parseFloat(c.borderTopLeftRadius) > 0) radius.push(cl);
      if (!isLed && c.boxShadow && c.boxShadow !== 'none') ombre.push(cl);
    });

    // 7. rail
    const railT = !!s.querySelector('.rail--t');
    const railB = !!s.querySelector('.rail--b');

    return { id, dark, ruoli: [...ruoli], fuoriCampo, gialloSuChiaro,
             radius, ombre, piccoli, railT, railB };
  });
}
"""


def main():
    if len(sys.argv) < 2:
        print("uso: python3 qa_deck.py percorso/al/deck.html")
        sys.exit(2)
    path = pathlib.Path(sys.argv[1]).resolve()
    if not path.exists():
        print(f"file non trovato: {path}")
        sys.exit(2)

    with sync_playwright() as p:
        # in questo ambiente il chromium di sistema va indicato esplicitamente:
        # la versione attesa da playwright non e' quella installata. Le regole non cambiano.
        _exe = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
        b = p.chromium.launch(**({"executable_path": _exe} if pathlib.Path(_exe).exists() else {}))
        pg = b.new_page(viewport={"width": 1400, "height": 900})
        pg.goto("file://" + str(path), wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(800)
        slides = pg.evaluate(JS, ACID)
        b.close()

    errori = 0
    print(f"\nQA sistema Quadro · {path.name} · {len(slides)} slide\n" + "-" * 68)

    for s in slides:
        problemi = []
        if s["fuoriCampo"]:
            problemi.append(f"fuori campo: {s['fuoriCampo'][:3]}")
        if len(s["ruoli"]) > 3:
            problemi.append(f"{len(s['ruoli'])} ruoli gialli (max 3): {s['ruoli']}")
        if s["gialloSuChiaro"]:
            problemi.append(f"testo giallo su fondo chiaro: {s['gialloSuChiaro'][:3]}")
        if s["piccoli"]:
            problemi.append(f"corpo sotto 9.5px: {s['piccoli'][:3]}")
        if s["radius"]:
            problemi.append(f"border-radius non ammesso: {s['radius'][:3]}")
        if s["ombre"]:
            problemi.append(f"ombra non ammessa: {s['ombre'][:3]}")
        if not s["railT"]:
            problemi.append("manca il rail superiore")
        if not s["railB"]:
            problemi.append("manca il rail inferiore")

        fondo = "scura" if s["dark"] else "chiara"
        if problemi:
            errori += len(problemi)
            print(f"  {s['id']:<10} [{fondo}]  NON CONFORME")
            for x in problemi:
                print(f"             → {x}")
        else:
            print(f"  {s['id']:<10} [{fondo}]  ok · ruoli gialli: {len(s['ruoli'])}")

    # 8. ritmo chiaro/scuro
    print("-" * 68)
    seq = "".join("S" if s["dark"] else "C" for s in slides)
    print(f"  ritmo: {seq}")
    run = maxrun = 0
    for ch in seq:
        run = run + 1 if ch == "C" else 0
        maxrun = max(maxrun, run)
    if maxrun > 3:
        errori += 1
        print(f"  → NON CONFORME: {maxrun} slide chiare consecutive (max 3)")
    else:
        print(f"  → ok · al massimo {maxrun} slide chiare consecutive")

    print("-" * 68)
    if errori:
        print(f"  {errori} violazioni da risolvere\n")
        sys.exit(1)
    print("  nessuna violazione\n")


if __name__ == "__main__":
    main()
