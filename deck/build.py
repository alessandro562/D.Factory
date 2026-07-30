#!/usr/bin/env python3
"""
Assembla il sales deck D.Factory in un singolo HTML standalone.

- concatena i sorgenti in deck/src/
- inserisce i componenti mockup (deck/src/dash.html) sui token @@DASH_*@@
- genera il markup ripetitivo delle chart (timeline 20 macchine, barre orarie)
- inlinea font Geist/Geist Mono e asset logo in base64 (nessuna dipendenza CDN)

Uso:  python3 deck/build.py
Out:  DFactory_SalesDeck.html
"""
import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
SRC = ROOT / "src"
ASSETS = ROOT / "assets"
OUT = REPO / "DFactory_SalesDeck.html"

FONT_DIRS = [
    ROOT / "fonts",
    ROOT.parent / "node_modules" / "geist" / "dist" / "fonts",
    pathlib.Path("/tmp/claude-0/-home-user-D-Factory/15c35d4e-51de-5078-9e06-09dfe323a73d"
                 "/scratchpad/node_modules/geist/dist/fonts"),
]


def find_font(rel: str) -> pathlib.Path:
    for d in FONT_DIRS:
        p = d / rel
        if p.exists():
            return p
    sys.exit(f"font non trovato: {rel} (cercato in {[str(d) for d in FONT_DIRS]})")


def data_uri(path: pathlib.Path, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


# ---------------------------------------------------------------- chart markup
def multirows() -> str:
    """20 righe di timeline stato-per-minuto. Pattern fisso e deterministico."""
    machines = [
        ("A01 Depalletizer", [("run", 46), ("idle", 6), ("run", 34), ("set", 5), ("run", 9)]),
        ("A02 Rinser",       [("run", 62), ("held", 5), ("run", 33)]),
        ("A03 Filler",       [("run", 41), ("idle", 7), ("run", 52)]),
        ("A04 Capper",       [("run", 74), ("set", 6), ("run", 20)]),
        ("A05 Labeler-A",    [("run", 30), ("idle", 8), ("run", 44), ("held", 5), ("run", 13)]),
        ("A06 Labeler-B",    [("run", 22), ("stop", 11), ("held", 9), ("idle", 14), ("run", 44)]),
        ("A07 Inspector",    [("run", 55), ("set", 7), ("run", 38)]),
        ("A08 Dryer",        [("run", 88), ("idle", 12)]),
        ("A09 Shrink Wrap",  [("run", 34), ("set", 9), ("run", 41), ("idle", 6), ("run", 10)]),
        ("B10 Tray Former",  [("run", 18), ("held", 8), ("run", 58), ("idle", 5), ("run", 11)]),
        ("B11 Case Packer",  [("run", 26), ("idle", 5), ("run", 30), ("stop", 8), ("run", 31)]),
        ("B12 Palletizer",   [("run", 44), ("set", 6), ("run", 50)]),
        ("B13 Stretch Wrap", [("run", 66), ("idle", 7), ("run", 27)]),
        ("B14 Riser",        [("idle", 12), ("run", 40), ("held", 6), ("run", 42)]),
        ("C15 Pasteurizer",  [("run", 79), ("set", 5), ("run", 16)]),
        ("C16 Chiller",      [("run", 92), ("idle", 8)]),
        ("C17 CIP Skid",     [("set", 14), ("run", 48), ("idle", 6), ("run", 32)]),
        ("C18 Blow Molder",  [("run", 58), ("held", 5), ("run", 37)]),
        ("C19 Cap Sorter",   [("run", 36), ("idle", 9), ("run", 55)]),
        ("C20 Outfeed",      [("idle", 8), ("run", 47), ("set", 6), ("run", 39)]),
    ]
    alert = {"A06 Labeler-B", "B11 Case Packer"}
    out = []
    for name, segs in machines:
        cls = ' style="color:#f2f3f4"' if name in alert else ""
        bars = "".join(f'<i class="s-{s}" style="width:{w}%"></i>' for s, w in segs)
        out.append(f'<div class="row" style="margin-bottom:0">'
                   f'<div class="nm"{cls}>{name}</div>'
                   f'<div class="tl" style="height:5px">{bars}</div></div>')
    return "\n".join(out)


def hourbars() -> str:
    """24 barre orarie impilate per stato macchina (kWh)."""
    # (execute, idle, held, setup, stopped) in unità relative, 24 ore
    hours = [
        (4, 6, 2, 1, 1), (4, 6, 2, 1, 1), (4, 5, 2, 1, 1), (5, 5, 2, 1, 1),
        (8, 4, 2, 3, 1), (26, 4, 3, 5, 1), (52, 5, 6, 3, 2), (58, 4, 7, 2, 2),
        (61, 4, 5, 2, 1), (57, 5, 8, 2, 3), (49, 6, 9, 4, 2), (38, 9, 6, 6, 2),
        (30, 11, 5, 4, 3), (54, 5, 6, 2, 2), (60, 4, 5, 2, 1), (56, 5, 7, 3, 2),
        (47, 6, 9, 3, 4), (41, 7, 6, 5, 2), (34, 8, 5, 3, 2), (22, 9, 4, 2, 2),
        (14, 8, 3, 2, 1), (9, 7, 3, 1, 1), (5, 6, 2, 1, 1), (4, 6, 2, 1, 1),
    ]
    order = [("run", 0), ("idle", 1), ("held", 2), ("set", 3), ("stop", 4)]
    peak = max(sum(h) for h in hours)
    out = []
    for h in hours:
        total = sum(h)
        col_h = total / peak * 100
        segs = "".join(
            f'<i class="s-{cls}" style="height:{v / total * 100:.1f}%;width:100%;display:block"></i>'
            for cls, i in order if (v := h[i]) > 0
        )
        out.append(f'<div style="flex:1;height:{col_h:.1f}%;display:flex;flex-direction:column-reverse">'
                   f'{segs}</div>')
    return "\n".join(out)


def sankey() -> str:
    """Diagramma di flusso energia: nastri proporzionali ai MWh.

    Totale 408,84 MWh = rete 320,84 + fotovoltaico 88,0.
    Consumi: Filling 112,4 · Mixing 86,1 · Boiler 71,3 · HVAC 58,0 ·
             Chiller 44,7 · Purifier 21,4 · Office 14,9.
    """
    K = 0.4158                      # px per MWh
    XS, XSW = 4, 7                  # sorgenti
    XM, XMW = 205, 7                # nodo fabbrica / uffici
    XD, XDW = 368, 6                # consumi
    ACID, WHITE, GREY = "#e6e011", "#f2f3f4", "#9aa0a7"

    def h(v):
        return v * K

    def ribbon(x1, ya, x2, yb, val, fill, op):
        hh = h(val)
        mx = (x1 + x2) / 2
        return (f'<path d="M{x1:.1f},{ya:.1f} C{mx:.1f},{ya:.1f} {mx:.1f},{yb:.1f} {x2:.1f},{yb:.1f} '
                f'L{x2:.1f},{yb + hh:.1f} C{mx:.1f},{yb + hh:.1f} {mx:.1f},{ya + hh:.1f} '
                f'{x1:.1f},{ya + hh:.1f} Z" fill="{fill}" fill-opacity="{op}"/>')

    p = []
    # --- sorgenti
    rete_y, fv_y = 12.0, 12.0 + h(320.84) + 8
    p.append(f'<rect x="{XS}" y="{rete_y:.1f}" width="{XSW}" height="{h(320.84):.1f}" fill="{GREY}"/>')
    p.append(f'<rect x="{XS}" y="{fv_y:.1f}" width="{XSW}" height="{h(88.0):.1f}" fill="{ACID}"/>')
    # --- nodo fabbrica + uffici
    fac_y = 12.0
    off_y = fac_y + h(393.94) + 6
    p.append(f'<rect x="{XM}" y="{fac_y:.1f}" width="{XMW}" height="{h(393.94):.1f}" fill="{WHITE}"/>')
    p.append(f'<rect x="{XM}" y="{off_y:.1f}" width="{XMW}" height="{h(14.9):.1f}" fill="{GREY}"/>')
    # --- sorgenti -> nodi
    p.append(ribbon(XS + XSW, rete_y, XM, fac_y, 305.94, GREY, ".22"))
    p.append(ribbon(XS + XSW, rete_y + h(305.94), XM, off_y, 14.9, GREY, ".16"))
    p.append(ribbon(XS + XSW, fv_y, XM, fac_y + h(305.94), 88.0, ACID, ".30"))
    # --- fabbrica -> consumi
    consumi = [("Filling", 112.4, ACID, ".36"), ("Mixing", 86.1, WHITE, ".19"),
               ("Boiler", 71.3, WHITE, ".15"), ("HVAC", 58.0, WHITE, ".12"),
               ("Chiller", 44.7, WHITE, ".10"), ("Purifier", 21.4, WHITE, ".08")]
    out_y, dst_y = fac_y, 8.0
    bars, labels = [], []
    for name, val, col, op in consumi:
        p.append(ribbon(XM + XMW, out_y, XD, dst_y, val, col, op))
        bars.append(f'<rect x="{XD}" y="{dst_y:.1f}" width="{XDW}" height="{h(val):.1f}" '
                    f'fill="{ACID if col == ACID else GREY}"/>')
        labels.append(f'<text x="{XD + XDW + 4}" y="{dst_y + h(val) / 2 + 1.7:.1f}" class="axl" '
                      f'style="fill:{"#f2f3f4" if col == ACID else "#8a8e96"}">{name}</text>')
        out_y += h(val)
        dst_y += h(val) + 3
    # --- uffici (consumo terminale)
    p.append(ribbon(XM + XMW, off_y, XD, dst_y, 14.9, GREY, ".16"))
    bars.append(f'<rect x="{XD}" y="{dst_y:.1f}" width="{XDW}" height="{h(14.9):.1f}" fill="{GREY}"/>')
    labels.append(f'<text x="{XD + XDW + 4}" y="{dst_y + h(14.9) / 2 + 1.7:.1f}" class="axl" '
                  f'style="fill:#8a8e96">Office</text>')

    p += bars + labels
    p.append(f'<text x="0" y="8" class="axl" style="fill:#8a8e96">RETE &middot; 320,8 MWh</text>')
    p.append(f'<text x="0" y="199" class="axl" style="fill:#e6e011">FOTOVOLTAICO &middot; 88,0 MWh</text>')
    p.append(f'<text x="{XM}" y="8" class="axl" style="fill:#f2f3f4">FACTORY</text>')
    return ('<svg viewBox="0 0 470 202" style="height:100%">\n' + "\n".join(p) + "\n</svg>")


# ---------------------------------------------------------------- build
def load_dash_components() -> dict:
    raw = (SRC / "dash.html").read_text(encoding="utf-8")
    parts = re.split(r"<!--@DASH:([A-Z_]+)@-->", raw)
    comps = {}
    for i in range(1, len(parts), 2):
        comps[parts[i]] = parts[i + 1].strip()
    return comps


def main() -> None:
    html = "\n".join(
        (SRC / n).read_text(encoding="utf-8")
        for n in ("00_head.html", "01_slides_01_10.html",
                  "02_slides_11_20.html", "03_slides_21_30.html")
    )

    # mockup: prima si riempiono le chart generate, poi si inseriscono i componenti
    comps = load_dash_components()
    charts = {"multirows": multirows(), "hourbars": hourbars()}
    for name in comps:
        comps[name] = comps[name].replace("@@SANKEY@@", sankey())
    for name, markup in comps.items():
        for cid, generated in charts.items():
            marker = f'<div id="{cid}"'
            if marker in markup:
                before, _, rest = markup.partition(marker)
                attrs, _, after = rest.partition("></div>")
                markup = f"{before}<div{attrs}>\n{generated}\n</div>{after}"
        comps[name] = markup

    for name, markup in comps.items():
        html = html.replace(f"@@DASH_{name}_MINI@@",
                            '<div class="mini" style="width:518px;height:296px;position:relative;overflow:hidden">'
                            '<div style="transform:scale(.74);transform-origin:0 0">'
                            + markup + '</div></div>')
        html = html.replace(f"@@DASH_{name}@@", markup)

    # asset e font in base64
    subs = {
        "@@FONT_SANS@@": data_uri(find_font("geist-sans/Geist-Variable.woff2"), "font/woff2"),
        "@@FONT_MONO@@": data_uri(find_font("geist-mono/GeistMono-Variable.woff2"), "font/woff2"),
        "@@LOCK_W@@": data_uri(ASSETS / "asset_lockup_white.png", "image/png"),
        "@@LOCK_B@@": data_uri(ASSETS / "asset_lockup_black.png", "image/png"),
        "@@MARK_W@@": data_uri(ASSETS / "asset_mark_white.png", "image/png"),
        "@@MARK_B@@": data_uri(ASSETS / "asset_mark_black.png", "image/png"),
    }
    for k, v in subs.items():
        html = html.replace(k, v)

    leftover = set(re.findall(r"@@[A-Z_0-9]+@@", html))
    if leftover:
        sys.exit(f"token non risolti: {sorted(leftover)}")

    OUT.write_text(html, encoding="utf-8")
    n = html.count('<section class="slide')
    print(f"{OUT.name}: {n} slide, {len(html) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
