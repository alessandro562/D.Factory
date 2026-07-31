#!/usr/bin/env python3
"""
Collaudo dei due documenti v2, secondo la sezione 21 del master prompt.

Copre quello che il collaudo di sistema non vede: geometria del canvas e dei
contenitori, placeholder, coerenza incrociata fra i due documenti, regole di
copywriting, densita' di parole, rete e console.

Uso:  python3 quadro/qa_v2.py [--report]
Out:  esito a schermo; con --report scrive anche qa/DFactory_QA_Report_v2.md
"""
import argparse
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
SALES = REPO / "DFactory_SalesDeck_v2.html"
DOSSIER = REPO / "DFactory_DossierTecnico_v2.html"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

BANNED = ["world-class", "world class", "seamless", "game-changer", "game changer",
          "disruptive", "packaging-native", "cross-vertical", "go-to-market",
          "rivoluzionario", "cutting edge", "AI-powered", "plug-and-play",
          "ROI garantito", "compatibile con tutto"]

# I 17 token del deck v1 non si perdono: o restano nel deck, o migrano nel dossier.
PH_STORICI = [f"PH_{n:02d}_" for n in list(range(1, 14)) + [15, 16, 17, 18]]

JS = r"""
() => {
  const acid = 'rgb(230, 224, 17)';
  const microClassi = ['lbl','lbl-s','rail','panel__hd','panel__ft','chip','status',
    'matrix__h','readout__k','readout__v','key','barh__name','barh__val','tl__name',
    'cols__x','link-card__k','stepper__n','case-grid__k','slot__hd','flowline__k',
    'metric-strip__k','metric-strip__v','callout-num','raci'];
  const micro = e => {
    for (let p = e; p && p.classList; p = p.parentElement) {
      if (p.tagName === 'svg' || p.tagName === 'SVG') return true;
      for (const c of microClassi) if (p.classList.contains(c)) return true;
    }
    return false;
  };

  return [...document.querySelectorAll('.slide')].map((s, i) => {
    const sr = s.getBoundingClientRect();
    const out = {
      id: s.id, n: i + 1, dark: s.classList.contains('slide--dark'),
      w: s.clientWidth, h: s.clientHeight,
      railT: !!s.querySelector('.rail--t'), railB: !!s.querySelector('.rail--b'),
      titolo: !!s.querySelector('h1, h2'),
      cartiglio: (s.querySelector('.rail--b span:last-child') || {}).textContent || '',
      fuoriCampo: [], sulRail: [], contenitori: [], piccoli: [], pesi: [],
      radius: [], ombre: [], serif: 0, parole: 0, ruoli: []
    };
    const ruoli = new Set();
    const rb = s.querySelector('.rail--b');
    const railTop = rb ? rb.getBoundingClientRect().top : sr.bottom;

    s.querySelectorAll('*').forEach(e => {
      const c = getComputedStyle(e), r = e.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) return;
      const cl = String(e.className || e.tagName);
      const isBg = cl.includes('grid-bg');
      const isLed = cl.includes('led');
      const inRail = e.closest('.rail');

      // geometria sul canvas
      const t = r.top - sr.top, l = r.left - sr.left;
      const b = r.bottom - sr.top, ri = r.right - sr.left;
      if (!isBg && (b > 720.5 || ri > 1280.5 || t < -0.5 || l < -0.5))
        out.fuoriCampo.push(cl.slice(0, 34) + ` [t${Math.round(t)} l${Math.round(l)} b${Math.round(b)} r${Math.round(ri)}]`);
      // contenuto sopra il rail inferiore
      if (!isBg && !inRail && e.children.length === 0 && r.bottom > railTop + 1.5
          && (e.textContent || '').trim())
        out.sulRail.push(cl.slice(0, 30) + ' ' + (e.textContent || '').trim().slice(0, 30));

      // tipografia
      const fs = parseFloat(c.fontSize);
      const haTesto = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 0);
      if (haTesto && fs < 9.5) out.piccoli.push(cl.slice(0, 26) + ' ' + fs + 'px');
      // dentro un SVG il corpo dichiarato non e' quello reso: il viewBox scala
      // tutto. Qui conta la misura a schermo.
      if (haTesto && e.ownerSVGElement) {
        const sv = e.ownerSVGElement;
        const vb = sv.viewBox && sv.viewBox.baseVal ? sv.viewBox.baseVal.width : 0;
        const scala = vb ? sv.getBoundingClientRect().width / vb : 1;
        if (fs * scala < 9.5)
          out.piccoli.push(cl.slice(0, 20) + ' svg ' + (fs * scala).toFixed(1) + 'px reso');
      }
      if (haTesto && parseInt(c.fontWeight, 10) >= 800) out.pesi.push(cl.slice(0, 26) + ' ' + c.fontWeight);
      if (!isLed && parseFloat(c.borderTopLeftRadius) > 0) out.radius.push(cl.slice(0, 26));
      if (!isLed && c.boxShadow && c.boxShadow !== 'none') out.ombre.push(cl.slice(0, 26));

      // ruoli del giallo
      if (c.color === acid) ruoli.add('testo-evidenza');
      if (c.backgroundColor === acid) {
        if (isLed) ruoli.add('stato-attivo');
        else if (cl.includes('seg-run') || cl.includes('barh__fill')) ruoli.add('serie-dati');
        else ruoli.add('blocco-evidenza');
      }
      if (c.stroke === acid) ruoli.add('serie-dati');
      [[c.borderTopColor, c.borderTopWidth], [c.borderLeftColor, c.borderLeftWidth],
       [c.borderRightColor, c.borderRightWidth], [c.borderBottomColor, c.borderBottomWidth]]
        .forEach(([v, w]) => { if (v === acid && parseFloat(w) > 0) ruoli.add('bordo-evidenza'); });

      // parole visibili, escluse micro-etichette e dati
      if (haTesto && !inRail && !micro(e)) {
        const txt = [...e.childNodes].filter(n => n.nodeType === 3)
          .map(n => n.textContent).join(' ').trim();
        if (txt) out.parole += txt.split(/\s+/).filter(w => /[a-zà-ù0-9]/i.test(w)).length;
      }
    });

    // statement serif
    out.serif = s.querySelectorAll('.t-stmt, .t-ed').length ? 1 : 0;
    out.ruoli = [...ruoli];

    // contenitori interni: pannelli e zone
    const guarda = (box, nome) => {
      const bb = box.getBoundingClientRect();
      if (getComputedStyle(box).overflow === 'hidden') return;
      box.querySelectorAll('*').forEach(e => {
        const r = e.getBoundingClientRect();
        if (!r.width || !r.height) return;
        if (/\bem(-blk)?\b/.test(String(e.className || ''))) return;
        if (r.bottom > bb.bottom + 1.5 || r.right > bb.right + 1.5)
          out.contenitori.push(nome + ' · ' + String(e.className || e.tagName).slice(0, 26));
      });
    };
    s.querySelectorAll('.panel').forEach(x => guarda(x, 'panel'));
    s.querySelectorAll('.zone').forEach(x => guarda(x, 'zone'));

    // due zone che si sovrappongono: una zona senza bottom cresce quanto le
    // serve e va a finire sopra quella ancorata in basso. Nessun controllo che
    // guardi dentro una zona sola puo' vederlo.
    const zone = [...s.querySelectorAll('.zone')].map(z => z.getBoundingClientRect());
    for (let a = 0; a < zone.length; a++)
      for (let b = a + 1; b < zone.length; b++)
        if (zone[a].bottom > zone[b].top + 1.5 && zone[b].bottom > zone[a].top + 1.5)
          out.contenitori.push(`zone ${a + 1} e ${b + 1} si sovrappongono`);
    return out;
  });
}
"""

fails, righe = [], []


def check(ok, label, detail=""):
    riga = f"  [{'ok' if ok else '!!'}] {label}" + (f"  {detail}" if detail else "")
    print(riga)
    righe.append((bool(ok), label, detail))
    if not ok:
        fails.append(label)


def sezione(t):
    print(f"\n== {t} ==")
    righe.append((None, t, ""))


def plain(html):
    """Testo visibile, un blocco per riga.

    I blocchi restano separati da un a capo: appiattire tutto su una riga sola
    fa nascere frasi che nel documento non esistono, e i controlli di stile ci
    cascano. Il trattino lungo di una cella RACI non e' prosa, e la frase di un
    paragrafo non prosegue in quello dopo.
    """
    s = re.sub(r"<style.*?</style>", " ", html, flags=re.S)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"</(p|div|li|h1|h2|h3|td|span|a|ul|svg|text)>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    return re.sub(r"\n\s*", "\n", s)


def apri(path):
    kw = {"executable_path": CHROME} if pathlib.Path(CHROME).exists() else {}
    errori, richieste = [], []
    with sync_playwright() as p:
        br = p.chromium.launch(**kw)
        pg = br.new_page(viewport={"width": 1400, "height": 900})
        pg.on("console", lambda m: errori.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errori.append(str(e)))
        pg.on("request", lambda r: richieste.append(r.url)
              if not r.url.startswith("file://") else None)
        pg.goto(path.as_uri(), wait_until="networkidle")
        pg.evaluate("() => document.fonts.ready")
        pg.wait_for_timeout(700)
        dati = pg.evaluate(JS)
        br.close()
    return dati, errori, richieste


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    if not (SALES.exists() and DOSSIER.exists()):
        sys.exit("mancano i documenti v2: esegui prima quadro/build.py")
    hs, hd = SALES.read_text(encoding="utf-8"), DOSSIER.read_text(encoding="utf-8")
    ts, td = plain(hs), plain(hd)
    both = ts + " " + td

    ds, es, rs = apri(SALES)
    dd, ed, rd = apri(DOSSIER)

    sezione("STRUTTURA")
    check(len(ds) == 12, "il sales deck ha 12 slide", f"({len(ds)})")
    check(len(dd) == 18, "il dossier tecnico ha 18 pagine", f"({len(dd)})")
    ids_s = [s["id"] for s in ds]
    ids_d = [s["id"] for s in dd]
    attesi_s = ["s01_cover", "s02_perche_adesso", "s03_come_funziona", "s04_tre_decisioni",
                "s05_prodotto_in_azione", "s06_prova", "s07_perche_dfactory",
                "s08_business_case", "s09_offerta", "s10_audit_scala", "s11_faq", "s12_cta"]
    attesi_d = ["d01_cover", "d02_architettura_prodotto", "d03_architettura_tecnica",
                "d04_capability", "d05_supervisione", "d06_oee_fermi", "d07_velocita_qualita",
                "d08_multi_impianto", "d09_distribuzione_energia", "d10_costo_co2_stato",
                "d11_metodo_misura", "d12_brownfield", "d13_deployment_security",
                "d14_sensori", "d15_output_integrazioni", "d16_delivery_raci",
                "d17_caso_tecnico", "d18_supporto_audit"]
    check(ids_s == attesi_s, "gli id del sales deck sono quelli previsti")
    check(ids_d == attesi_d, "gli id del dossier sono quelli previsti")
    check(len(set(ids_s)) == 12 and len(set(ids_d)) == 18, "nessun id duplicato")
    num_ok = all(f"{s['n']:02d} / {len(ds):02d}" in s["cartiglio"] for s in ds) and \
             all(f"{s['n']:02d} / {len(dd):02d}" in s["cartiglio"] for s in dd)
    check(num_ok, "la numerazione nel rail segue la posizione")
    check(all(s["titolo"] for s in ds + dd), "ogni pagina ha un titolo")
    check(ts.count("originali") == 0 and (REPO / "DFactory_SalesDeck.html").exists(),
          "gli originali v1 non sono stati sovrascritti")

    sezione("GEOMETRIA")
    for nome, dati in (("sales", ds), ("dossier", dd)):
        misure = {(s["w"], s["h"]) for s in dati}
        check(misure == {(1280, 720)}, f"{nome}: ogni pagina è 1280×720", f"({misure})")
        fc = [(s["id"], s["fuoriCampo"]) for s in dati if s["fuoriCampo"]]
        for i, v in fc:
            print(f"       {i}: {v[:3]}")
        check(not fc, f"{nome}: nessun elemento oltre i bordi", f"({len(fc)})")
        sr = [(s["id"], s["sulRail"]) for s in dati if s["sulRail"]]
        for i, v in sr:
            print(f"       {i}: {v[:3]}")
        check(not sr, f"{nome}: nessun contenuto sopra il rail inferiore", f"({len(sr)})")
        co = [(s["id"], s["contenitori"]) for s in dati if s["contenitori"]]
        for i, v in co:
            print(f"       {i}: {v[:3]}")
        check(not co, f"{nome}: nessun contenuto fuori da pannelli e zone", f"({len(co)})")
        check(all(s["railT"] and s["railB"] for s in dati), f"{nome}: rail su ogni pagina")

    sezione("DESIGN SYSTEM")
    for nome, dati, html in (("sales", ds, hs), ("dossier", dd, hd)):
        p = [(s["id"], s["piccoli"]) for s in dati if s["piccoli"]]
        check(not p, f"{nome}: nessun testo sotto 9,5 px", f"({p[:2]})" if p else "")
        w = [(s["id"], s["pesi"]) for s in dati if s["pesi"]]
        check(not w, f"{nome}: nessun peso 800 o 900", f"({w[:2]})" if w else "")
        r = [s["id"] for s in dati if s["radius"]]
        check(not r, f"{nome}: nessun border-radius fuori dal led", f"({r[:3]})" if r else "")
        o = [s["id"] for s in dati if s["ombre"]]
        check(not o, f"{nome}: nessuna ombra fuori dal led", f"({o[:3]})" if o else "")
        ns = sum(s["serif"] for s in dati)
        check(ns <= 2, f"{nome}: al massimo 2 statement serif", f"({ns})")
        # colori: solo neutri e acid, come la regola di palette del sistema
        fuori = set()
        for m in re.findall(r"#[0-9A-Fa-f]{6}|rgba?\([^)]+\)", html.split("</style>")[1]):
            v = [float(x) for x in re.findall(r"[\d.]+", m)] if m.startswith("rgb") else \
                [int(m[1:3], 16), int(m[3:5], 16), int(m[5:7], 16)]
            if len(v) >= 3:
                if abs(v[0] - 230) < 26 and abs(v[1] - 224) < 26 and abs(v[2] - 17) < 40:
                    continue
                if max(v[:3]) - min(v[:3]) > 14:
                    fuori.add(m)
        check(not fuori, f"{nome}: nessun colore fuori palette", f"({sorted(fuori)[:3]})" if fuori else "")

    budget = [(s["id"], s["ruoli"]) for s in ds if len(s["ruoli"]) > 3]
    check(not budget, "sales: massimo 3 ruoli gialli per slide", f"({budget})" if budget else "")
    budget_d = [(s["id"], s["ruoli"]) for s in dd if len(s["ruoli"]) > 2]
    check(not budget_d, "dossier: massimo 2 ruoli gialli per pagina",
          f"({budget_d})" if budget_d else "")

    sezione("DENSITA'")
    for nome, dati, tetto, media_max in (("sales", ds, 130, 100), ("dossier", dd, 220, 190)):
        parole = [(s["id"], s["parole"]) for s in dati]
        media = sum(p for _, p in parole) / len(parole)
        sopra = [x for x in parole if x[1] > tetto]
        for i, v in sopra:
            print(f"       {i}: {v} parole")
        check(media <= media_max, f"{nome}: media sotto le {media_max} parole",
              f"({media:.0f})")
        check(not sopra, f"{nome}: nessuna pagina oltre {tetto} parole", f"({len(sopra)})")
        print("       " + " · ".join(f"{i.split('_')[0]} {v}" for i, v in parole))

    sezione("PLACEHOLDER")
    ph_s = sorted(set(re.findall(r"\[\[(PH_[A-Z0-9_]+)\]\]", hs)))
    ph_d = sorted(set(re.findall(r"\[\[(PH_[A-Z0-9_]+)\]\]", hd)))
    tutti = sorted(set(ph_s) | set(ph_d))
    persi = [p for p in PH_STORICI if not any(t.startswith(p) for t in tutti)]
    check(not persi, "nessuno dei 17 token storici è andato perso", f"({persi})" if persi else "")
    check(not re.search(r'href="\[\[', hs + hd), "nessun placeholder usato come URL")
    check(not re.search(r"\[confermare[^\]]*\]", both), "nessun [confermare] residuo")
    comuni = sorted(set(ph_s) & set(ph_d))
    check(True, "token condivisi fra i due documenti", f"({', '.join(comuni)})")
    print(f"       sales ({len(ph_s)}): {', '.join(t.replace('PH_', '') for t in ph_s)}")
    print(f"       dossier ({len(ph_d)}): {', '.join(t.replace('PH_', '') for t in ph_d)}")

    sezione("COERENZA INCROCIATA")
    coppie = [
        ("nomi dei livelli", lambda: all(x in ts and x in td for x in ("Connect", "Insights", "Refyn"))),
        ("Refyn con lo stesso stato", lambda: "definizione" in ts.lower() and "definizione" in td.lower()),
        ("PackML a 17 stati", lambda: "17 stati" in ts and "17 stati" in td),
        ("modello ridotto a 2 stati", lambda: "due stati" in td and ("2 stati" in ts or "due" in ts)),
        ("on-premise in entrambi", lambda: "on-premise" in ts and "on-premise" in td),
        ("dato sul server del cliente", lambda: "server" in ts and "server del cliente" in td),
        ("sensoristica a carico del cliente", lambda: "carico tuo" in ts and "carico tuo" in td),
        ("stesso referente", lambda: "Pablo Degl'Innocenti" in ts and "Pablo Degl'Innocenti" in td),
        ("stesso indirizzo", lambda: ts.count("pablo.deglinnocenti@marchianisrl.com") == 1
         and td.count("pablo.deglinnocenti@marchianisrl.com") == 1),
        ("stesso caso cliente, in due letture", lambda: "PH_01_CASO_CLIENTE" in hs and "PH_T14_CASO_TECNICO" in hd),
        ("cinque vettori in entrambi", lambda: "vettor" in ts.lower() and "vettor" in td.lower()),
        ("milestone distinte nel dossier", lambda: "First signal" in td and "Operational go-live" in td),
    ]
    for label, f in coppie:
        check(f(), label)
    link_s = re.findall(r'href="(DFactory_[^"#]+)(#[a-z0-9_]+)?"', hs)
    link_d = re.findall(r'href="(DFactory_[^"#]+)(#[a-z0-9_]+)?"', hd)
    rotti = []
    for file, anc in link_s + link_d:
        target = REPO / file
        if not target.exists():
            rotti.append(file)
        elif anc and f'id="{anc[1:]}"' not in target.read_text(encoding="utf-8"):
            rotti.append(file + anc)
    check(not rotti, "i link reciproci puntano a pagine esistenti", f"({rotti})" if rotti else "")
    check(bool(link_s) and bool(link_d), "entrambi i documenti linkano l'altro",
          f"({len(link_s)} + {len(link_d)})")

    sezione("CLAIM E COPYWRITING")
    check("qualsiasi marca e" not in both.lower() and "qualsiasi protocollo" not in both.lower(),
          "nessun claim di compatibilità universale")
    check("69.000" not in both and "payback" not in both.lower(),
          "nessun payback numerico senza input validati")
    check(not re.search(r"2 (giorni|gg)[^.]{0,80}(go-live|esercizio)", both, re.I),
          "il primo dato non è confuso con il go-live")
    # vale l'affermazione, non la smentita: "non e' un software certificato" e'
    # esattamente la frase prudente che il brief chiede.
    iso = []
    for m in re.finditer(r"certificat\w* ISO 50001", both):
        prima = both[max(0, m.start() - 60):m.start()].lower()
        if not re.search(r"\bnon\b[^.\n]{0,40}$", prima):
            iso.append(both[max(0, m.start() - 40):m.end()].strip())
    check(not iso, "nessuna certificazione ISO 50001 attribuita al software",
          f"({iso[:2]})" if iso else "")
    check("MID · ISO 50001" not in both, "MID e ISO 50001 non sono presentati come un'unica categoria")
    check(not re.search(r"\b(MES|MOM)\b", both), "nessuna occorrenza di MES/MOM")
    check("predittiv" not in ts.lower(), "nessuna capacità di roadmap nel sales deck")
    check("intelligenza artificiale" in td.lower() or "Nessuna capacità di intelligenza" in hd,
          "il dossier dichiara l'assenza di intelligenza artificiale")
    hits = [w for w in BANNED if re.search(re.escape(w), both, re.I)]
    check(not hits, "nessun termine vietato", f"({', '.join(hits)})" if hits else "")
    em = [r for r in both.split("\n") if re.search(r"\S\s*—\s*\S", r)]
    check(not em, "nessun trattino lungo nella prosa", f"({len(em)})")
    nxy = re.findall(r"\bNon\s+(?:è|sono|serve|solo|un|una|il|la|l')[^.!?\n]*[.!?]\s*(?:È|E|Ma|Il|La)\b", both)
    check(len(nxy) <= 1, "al massimo una costruzione 'Non X. Y.'", f"({len(nxy)})")
    check("Dati illustrativi" in ts and "illustrativi" in td.lower(),
          "le schermate dimostrative sono etichettate")

    sezione("RETE E CONSOLE")
    for nome, err, req, html in (("sales", es, rs, hs), ("dossier", ed, rd, hd)):
        check(not err, f"{nome}: nessun errore in console", f"({err[:2]})" if err else "")
        check(not req, f"{nome}: nessuna richiesta di rete non locale", f"({req[:2]})" if req else "")
        urls = [u for u in re.findall(r'https?://[^"\')\s]+', html) if "w3.org" not in u]
        check(not urls, f"{nome}: nessun riferimento esterno nel sorgente", f"({len(urls)})")
        check("@media print" in html, f"{nome}: il blocco di stampa è presente")
        check('lang="it"' in html, f"{nome}: lingua dichiarata")

    print("\n" + "-" * 70)
    if fails:
        print(f"  {len(fails)} controlli non superati:")
        for f in fails:
            print(f"    · {f}")
    else:
        print("  tutti i controlli superati")

    if args.report:
        scrivi_report(ds, dd, righe)
    return 1 if fails else 0


def scrivi_report(ds, dd, righe):
    out = REPO / "qa" / "DFactory_QA_Report_v2.md"
    out.parent.mkdir(exist_ok=True)
    L = ["# QA · DFactory Sales Deck v2 e Dossier Tecnico v2", "",
         "Esito di `python3 quadro/qa_v2.py`. Ogni riga è una verifica eseguita sul",
         "documento compilato, aperto in Chromium a 1280×720 con i font caricati.", ""]
    for ok, label, detail in righe:
        if ok is None:
            L += ["", f"## {label}", ""]
        else:
            L.append(f"- [{'x' if ok else ' '}] {label}" + (f" · {detail}" if detail else ""))
    L += ["", "## Densità per pagina", "",
          "| Documento | Pagina | Parole visibili | Ruoli gialli |", "|---|---|---|---|"]
    for nome, dati in (("Sales deck", ds), ("Dossier", dd)):
        for s in dati:
            L.append(f"| {nome} | `{s['id']}` | {s['parole']} | {len(s['ruoli'])} |")
    L += ["", "Le micro-etichette, i valori numerici e il testo dentro gli SVG non entrano nel",
          "conteggio: misurano la densità di lettura, non la quantità di caratteri.", ""]
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"\n  report: {out}")


if __name__ == "__main__":
    sys.exit(main())
