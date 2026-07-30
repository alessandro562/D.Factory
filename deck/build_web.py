#!/usr/bin/env python3
"""
Genera la versione web del sales deck: un visualizzatore a pagina singola.

Prende DFactory_SalesDeck.html (standalone) e produce un frammento pronto per la
pubblicazione come Artifact: senza doctype/html/head/body, con la cornice del viewer
innestata sopra il design system del deck (nessun font o colore nuovo).

Uso: python3 deck/build_web.py
Out: deck/web/DFactory_SalesDeck_web.html
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT.parent / "DFactory_SalesDeck.html"
OUT = ROOT / "web" / "DFactory_SalesDeck_web.html"

THUMB_W = 232          # larghezza fissa della miniatura in vista d'insieme
THUMB_SCALE = THUMB_W / 1280
THUMB_W_SM = 148       # miniatura su schermi stretti
THUMB_SCALE_SM = THUMB_W_SM / 1280

VIEWER_CSS = """
/* ============ CORNICE VIEWER ============
   Riusa i token del deck. Le slide sono l'opera: non si invertono col tema.
   Si adatta solo la cornice, via token, con override per il toggle del lettore. */
:root{
  --ui-bg:#eef0f3;        /* neutro freddo: le slide vi poggiano come fogli */
  --ui-panel:#f7f8f9;
  --ui-fg:#101114;
  --ui-muted:#6b7079;
  --ui-line:rgba(0,0,0,.14);
  --ui-shadow:0 1px 2px rgba(16,17,20,.10), 0 14px 34px rgba(16,17,20,.13);
  --ui-mark:url("");      /* sostituito a build time */
  --gap:26px;
  --bar:46px;
  --s:.72;                /* scala slide: JS la rende esatta, questo e' il fallback */
}
@media (prefers-color-scheme:dark){
  :root{
    --ui-bg:#16171a; --ui-panel:#1d1f22; --ui-fg:#e7e8ea; --ui-muted:#8c9198;
    --ui-line:rgba(255,255,255,.16);
    --ui-shadow:0 1px 2px rgba(0,0,0,.5), 0 16px 40px rgba(0,0,0,.55);
  }
}
:root[data-theme="dark"]{
  --ui-bg:#16171a; --ui-panel:#1d1f22; --ui-fg:#e7e8ea; --ui-muted:#8c9198;
  --ui-line:rgba(255,255,255,.16);
  --ui-shadow:0 1px 2px rgba(0,0,0,.5), 0 16px 40px rgba(0,0,0,.55);
}
:root[data-theme="light"]{
  --ui-bg:#eef0f3; --ui-panel:#f7f8f9; --ui-fg:#101114; --ui-muted:#6b7079;
  --ui-line:rgba(0,0,0,.14);
  --ui-shadow:0 1px 2px rgba(16,17,20,.10), 0 14px 34px rgba(16,17,20,.13);
}

html{background:var(--ui-bg);scroll-snap-type:y proximity}
body{background:var(--ui-bg);color:var(--ui-fg)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}

/* ---- barra ---- */
.vbar{position:fixed;inset:0 0 auto 0;height:var(--bar);z-index:50;display:flex;
  align-items:center;gap:14px;padding:0 16px;background:var(--ui-panel);
  border-bottom:1px solid var(--ui-line)}
.vbar .mk{width:15px;height:16px;background:var(--ui-mark) no-repeat center/contain;flex:0 0 15px}
@media (prefers-color-scheme:dark){.vbar .mk{filter:invert(1)}}
:root[data-theme="dark"] .vbar .mk{filter:invert(1)}
:root[data-theme="light"] .vbar .mk{filter:none}
.vbar .id{font:700 9px/1 "Geist Mono",monospace;letter-spacing:.16em;text-transform:uppercase}
.vbar .sub{font:400 9px/1 "Geist Mono",monospace;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ui-muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.vbar .sp{flex:1}
.vbar .n{font:700 10px/1 "Geist Mono",monospace;letter-spacing:.1em;
  font-variant-numeric:tabular-nums;white-space:nowrap}
.vbar .n i{font-style:normal;color:var(--ui-muted);font-weight:400}
.vbtn{font:600 9px/1 "Geist Mono",monospace;letter-spacing:.13em;text-transform:uppercase;
  color:var(--ui-fg);background:transparent;border:1px solid var(--ui-line);border-radius:2px;
  padding:7px 10px;cursor:pointer}
.vbtn:hover{border-color:var(--ui-fg)}
.vbtn:focus-visible{outline:2px solid #e6e011;outline-offset:2px}
.vbtn[aria-pressed="true"]{background:#e6e011;border-color:#e6e011;color:#000}
/* avanzamento nel documento */
.vprog{position:fixed;top:var(--bar);left:0;height:2px;background:#e6e011;z-index:51;width:0}

/* ---- piano di lettura ---- */
.deck{display:flex;flex-direction:column;align-items:center;gap:var(--gap);
  padding:calc(var(--bar) + var(--gap)) 0 var(--gap)}
.slot{position:relative;flex:0 0 auto;width:calc(1280px * var(--s));height:calc(720px * var(--s));
  box-shadow:var(--ui-shadow);scroll-snap-align:start;
  scroll-margin-top:calc(var(--bar) + 12px);outline:none}
.slot>.slide{position:absolute;top:0;left:0;transform:scale(var(--s));transform-origin:0 0}
.slot::after{content:attr(data-n);position:absolute;top:0;right:-34px;
  font:400 9px/1 "Geist Mono",monospace;letter-spacing:.1em;color:var(--ui-muted);
  font-variant-numeric:tabular-nums}
@media (max-width:1420px){.slot::after{display:none}}

/* ---- vista d'insieme: stesso DOM, sola scala diversa ---- */
body.ov .deck{display:grid;justify-content:center;gap:16px;
  grid-template-columns:repeat(auto-fill,__THUMB_W__px);
  padding:calc(var(--bar) + 22px) 22px 40px}
body.ov{--s:__THUMB_SCALE__}
body.ov .slot{cursor:pointer;box-shadow:0 1px 2px rgba(16,17,20,.12);scroll-snap-align:none;
  transition:box-shadow .12s ease}
body.ov .slot:hover,body.ov .slot:focus-visible{box-shadow:0 0 0 2px #e6e011}
body.ov .slot::after{display:block;top:auto;bottom:-15px;right:auto;left:0}
body.ov .vprog{display:none}
@media (prefers-reduced-motion:reduce){body.ov .slot{transition:none}}

/* ---- schermi stretti: barra ridotta, miniature piu' piccole ---- */
@media (max-width:720px){
  :root{--gap:14px}
  .vbar{gap:10px;padding:0 11px}
  .vbar .sub{display:none}
  body.ov{--s:__THUMB_SCALE_SM__}
  body.ov .deck{grid-template-columns:repeat(auto-fill,__THUMB_W_SM__px);gap:12px;
    padding:calc(var(--bar) + 18px) 12px 34px}
  body.ov .slot{width:calc(1280px * var(--s));height:calc(720px * var(--s))}
}

@media print{
  .vbar,.vprog{display:none}
  html{scroll-snap-type:none}
  .deck{gap:0;padding:0}
  .slot{box-shadow:none;break-after:page;page-break-after:always}
  @page{size:1280px 720px;margin:0}
}
"""

VIEWER_JS = """
(() => {
  const slots = [...document.querySelectorAll('.slot')];
  const stage = document.querySelector('.deck');
  const nEl = document.getElementById('v-n');
  const secEl = document.getElementById('v-sec');
  const prog = document.getElementById('v-prog');
  const ovBtn = document.getElementById('v-ov');
  let current = 0;

  /* scala esatta: clientWidth esclude la barra di scorrimento, 100vw no */
  const fit = () => {
    if (document.body.classList.contains('ov')) return;
    const pad = window.innerWidth > 720 ? 96 : 24;
    const w = Math.min(stage.clientWidth - pad, 1560);
    document.documentElement.style.setProperty('--s', Math.max(w, 280) / 1280);
  };
  const clearFit = () => document.documentElement.style.removeProperty('--s');

  const show = i => {
    current = Math.max(0, Math.min(slots.length - 1, i));
    const s = slots[current];
    nEl.firstChild.textContent = s.dataset.n;
    secEl.textContent = s.dataset.sec || '';
    prog.style.width = ((current + 1) / slots.length * 100) + '%';
  };

  /* slide corrente = quella col centro piu' vicino al centro del viewport.
     Deterministico anche quando ne sono visibili piu' di una (schermi stretti). */
  let queued = false, navLock = 0;
  const track = () => {
    /* dopo una navigazione esplicita il conteggio non si fa dettare dallo scorrimento */
    if (queued || document.body.classList.contains('ov') || performance.now() < navLock) return;
    queued = true;
    requestAnimationFrame(() => {
      queued = false;
      const doc = document.documentElement;
      if (innerHeight + scrollY >= doc.scrollHeight - 4) { show(slots.length - 1); return; }
      const line = parseFloat(getComputedStyle(doc).getPropertyValue('--bar') || 46) + 16;
      let best = 0;
      for (let i = 0; i < slots.length; i++) {
        if (slots[i].getBoundingClientRect().bottom > line) { best = i; break; }
      }
      show(best);
    });
  };
  addEventListener('scroll', track, {passive: true});

  const goto = i => {
    show(i);
    navLock = performance.now() + 800;
    slots[current].scrollIntoView({block: 'start'});
  };

  addEventListener('resize', track, {passive: true});

  const overview = on => {
    document.body.classList.toggle('ov', on);
    ovBtn.setAttribute('aria-pressed', String(on));
    ovBtn.textContent = on ? 'Chiudi indice' : 'Indice';
    if (on) { clearFit(); slots[current].scrollIntoView({block: 'start'}); }
    else { fit(); requestAnimationFrame(() => slots[current].scrollIntoView({block: 'center'})); }
  };

  ovBtn.addEventListener('click', () => overview(!document.body.classList.contains('ov')));
  document.getElementById('v-prev').addEventListener('click', () => goto(current - 1));
  document.getElementById('v-next').addEventListener('click', () => goto(current + 1));

  slots.forEach((s, i) => {
    s.tabIndex = 0;
    s.addEventListener('click', () => {
      if (document.body.classList.contains('ov')) { show(i); overview(false); }
    });
    s.addEventListener('keydown', e => {
      if (e.key === 'Enter' && document.body.classList.contains('ov')) { show(i); overview(false); }
    });
  });

  addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const ov = document.body.classList.contains('ov');
    switch (e.key) {
      case 'ArrowRight': case 'ArrowDown': case 'PageDown': case ' ':
        e.preventDefault(); goto(current + 1); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp':
        e.preventDefault(); goto(current - 1); break;
      case 'Home': e.preventDefault(); goto(0); break;
      case 'End': e.preventDefault(); goto(slots.length - 1); break;
      case 'o': case 'O': overview(!ov); break;
      case 'Escape': if (ov) overview(false); break;
    }
  });

  addEventListener('resize', fit);
  fit();
  show(0);
  track();
})();
"""


def main() -> None:
    if not SRC.exists():
        sys.exit(f"manca {SRC}: esegui prima deck/build.py")
    html = SRC.read_text(encoding="utf-8")

    style = re.search(r"<style>(.*?)</style>", html, re.S)
    if not style:
        sys.exit("blocco <style> non trovato")
    deck_css = style.group(1)

    # marchio per la barra: riuso il data URI del marchio nero gia' embeddato
    mark = re.search(r'\.lk-mb\{background-image:url\("([^"]+)"\)\}', deck_css)
    if not mark:
        sys.exit("data URI del marchio non trovato")

    # ogni <section class="slide"> in un contenitore scalabile
    chunks = re.findall(r'<section data-part=.*?</section>', html, re.S)
    if not chunks:
        sys.exit("nessuna slide trovata nel deck costruito")
    slots = []
    for i, c in enumerate(chunks, start=1):
        m = re.search(r'DOC (A?\d+)/A?\d+</div>\s*<div class="c">([^<]+)</div>', c)
        num = m.group(1) if m else f"{i:02d}"
        sec = m.group(2).strip() if m else ""
        part = re.search(r'data-part="(\w+)"', c).group(1)
        slots.append(f'<div class="slot" data-n="{num}" data-sec="{sec}" data-part="{part}" '
                     f'aria-label="Slide {num}, {sec}">{c}</div>')

    viewer_css = (VIEWER_CSS
                  .replace('--ui-mark:url("");', f'--ui-mark:url("{mark.group(1)}");')
                  .replace("__THUMB_W__", str(THUMB_W))
                  .replace("__THUMB_SCALE__", f"{THUMB_SCALE:.5f}")
                  .replace("__THUMB_W_SM__", str(THUMB_W_SM))
                  .replace("__THUMB_SCALE_SM__", f"{THUMB_SCALE_SM:.5f}"))

    out = f"""<style>{deck_css}</style>
<style>{viewer_css}</style>

<header class="vbar">
  <span class="mk" aria-hidden="true"></span>
  <span class="id">D.Factory &middot; Sales Deck</span>
  <span class="sub" id="v-sec">Cover</span>
  <span class="sp"></span>
  <span class="n" id="v-n">01<i>&thinsp;/&thinsp;30</i></span>
  <button class="vbtn" id="v-prev" type="button" title="Slide precedente (&larr;)">Prec</button>
  <button class="vbtn" id="v-next" type="button" title="Slide successiva (&rarr;)">Succ</button>
  <button class="vbtn" id="v-ov" type="button" aria-pressed="false"
          title="Vista d'insieme (O)">Indice</button>
</header>
<div class="vprog" id="v-prog"></div>

<main class="deck">
{chr(10).join(slots)}
</main>

<script>{VIEWER_JS}</script>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(out, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT.parent)}: {len(chunks)} slide, {len(out) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
