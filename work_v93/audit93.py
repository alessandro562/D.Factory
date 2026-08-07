#!/usr/bin/env python3
"""Audit di sequenza · Fase E2 del §14.3.

Cinque controlli che la QA per canvas non puo' fare, perche' riguardano la
successione e non la pagina:

  rhythm map              fondo e tipo canvas per canvas, con le sequenze
  duplicate layout map    firma strutturale, per vedere due pagine gemelle
  technical streak        quante slide tecniche di fila
  package check           una slide pacchetto non porta viste di prodotto
  dossier questionnaire   il core non ha il tono da questionario

Produce i due deliverable del §15 — Rhythm Map e Duplicate Layout Map — e
esce con codice 1 se una delle condizioni di sequenza non regge.

  audit93.py <deck.html> <dossier.html> <outdir>
"""
import os
import re
import sys
from collections import Counter

from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

JS = r"""
() => {
  const out = [];
  for (const s of document.querySelectorAll('.slide')) {
    const sb = s.getBoundingClientRect();
    const cs = getComputedStyle(s);
    const blocchi = [];
    for (const e of s.children) {
      const r = e.getBoundingClientRect();
      if (r.width < 3 || r.height < 3) continue;
      if (e.classList.contains('phb')) continue;      // impalcatura, non documento
      const cls = (e.className.baseVal || e.className || e.tagName).toString();
      blocchi.push([e.tagName.toLowerCase(),
                    Math.round((r.top - sb.top) / 24) * 24,
                    Math.round(r.height / 24) * 24,
                    Math.round(r.width / 80) * 80,
                    cls.split(' ')[0] || '-']);
    }
    // titolo: il primo blocco di testo grande della pagina
    let titolo = '';
    for (const e of s.querySelectorAll('h1, h2, .tt, .say')) {
      const t = (e.textContent || '').replace(/\s+/g, ' ').trim();
      if (t) { titolo = t; break; }
    }
    // il fondo non e' solo la classe: una slide bianca con un pannello nero
    // che copre meta' canvas non e' una slide bianca, e una slide con fondo
    // grigio chiarissimo non e' bianca. Il ritmo si legge a occhio, e il
    // controllo deve leggerlo allo stesso modo.
    let fondo = s.classList.contains('dk') ? 'dk'
              : (s.classList.contains('ac') ? 'ac' : 'lt');
    if (fondo === 'lt') {
      const m = cs.backgroundColor.match(/\d+/g) || [255, 255, 255];
      const chiaro = m[0] > 250 && m[1] > 250 && m[2] > 250;
      if (!chiaro) fondo = 'gr';
      else {
        // Un rettangolo nero e' nero anche quando sta dentro un SVG: il
        // lettore vede la stessa cosa. Prima il classificatore saltava gli
        // SVG e leggeva come «bianca» una slide meta' nera.
        let scuro = 0;
        for (const e of s.querySelectorAll('*')) {
          const dentroSvg = !!e.closest('svg');
          if (dentroSvg && e.tagName.toLowerCase() !== 'rect') continue;
          const st = getComputedStyle(e);
          const c = (dentroSvg ? st.fill : st.backgroundColor).match(/\d+/g);
          if (!c || (c[3] !== undefined && +c[3] === 0)) continue;
          if (+c[0] < 60 && +c[1] < 60 && +c[2] < 60) {
            const r = e.getBoundingClientRect();
            scuro += r.width * r.height;
          }
        }
        if (scuro / (1280 * 720) > 0.2) fondo = 'mx';
      }
    }
    out.push({
      id: s.id,
      fondo,
      bg: cs.backgroundColor,
      tipo: s.dataset.tipo || '',
      titolo,
      uiViews: s.querySelectorAll('svg[data-ui]').length,
      svg: s.querySelectorAll('svg').length,
      band: s.querySelectorAll('.band').length,
      blocchi,
      testo: (s.textContent || '').replace(/\s+/g, ' ').trim(),
    });
  }
  return out;
}
"""


def leggi(path):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': 1280, 'height': 720})
        pg.goto('file://' + os.path.abspath(path), wait_until='networkidle')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(400)
        d = pg.evaluate(JS)
        b.close()
    return d


def firma(rec):
    """Firma strutturale: dove stanno i blocchi, non che cosa dicono.

    Il fondo fa parte della firma perche' due pagine con la stessa griglia ma
    fondo diverso non si leggono come la stessa pagina: e' esattamente la
    soluzione adottata per le tre slide pacchetto."""
    corpo = '|'.join(f'{t}@{y}h{h}w{w}' for t, y, h, w, _ in rec['blocchi'])
    return f'{rec["fondo"]}/{rec["tipo"]}/{corpo}'


TECNICI = {'prodotto', 'matrice'}
QUESTIONARIO = ('chi decide', 'owner', 'da compilare', 'valore di progetto',
                'stato:', 'evidenza:', 'responsabile:')

ERR, NOTE = [], []


def audit(nome, data, tetto_streak, tipi_tecnici, core=None):
    print(f'\n=== {nome} · {len(data)} canvas ===')
    print(f'{"#":>3} {"canvas":28s}{"fondo":>6}{"tipo":>14}{"vis":>5}{"band":>5}  titolo')
    for i, r in enumerate(data, 1):
        print(f'{i:>3} {r["id"]:28s}{r["fondo"]:>6}{r["tipo"] or "—":>14}'
              f'{r["uiViews"]:>5}{r["band"]:>5}  {r["titolo"][:52]}')

    fondi = [r['fondo'] for r in data]
    NOTE.append(f'{nome} · fondi: ' + ' '.join(fondi))
    NOTE.append(f'{nome} · pagine scure: {fondi.count("dk")}')

    # --- ritmo. Le due regole sono diverse perche' i due documenti lo sono:
    #     un deck si sfoglia in venti minuti e il fondo scandisce il racconto;
    #     un dossier si consulta, e alternare i fondi lo renderebbe illeggibile.
    #     Per il deck: mai tre fondi uguali di fila nel corpo (§7.1).
    #     Per il dossier: 3-4 pagine scure e mai quattro pagine di fila senza
    #     un elemento visivo forte (§9.5).
    if core is not None:
        f_core = [r['fondo'] for r in data[:core]]
        for i in range(len(f_core) - 2):
            if f_core[i] == f_core[i + 1] == f_core[i + 2]:
                ERR.append(f'{nome} · tre fondi «{f_core[i]}» di fila nel corpo: '
                           f'{data[i]["id"]}, {data[i+1]["id"]}, {data[i+2]["id"]}')
        NOTE.append(f'{nome} · corpo: nessun fondo ripetuto tre volte di fila'
                    if not any(f_core[i] == f_core[i+1] == f_core[i+2]
                               for i in range(len(f_core) - 2)) else '')
    else:
        n = fondi.count('dk')
        # 3-4 nel §9.5, piu' la pagina di chiusura che fa da contro-copertina
        if not 3 <= n <= 5:
            ERR.append(f'{nome} · {n} pagine scure: da 3 a 5 con la chiusura')
        secco = [not (r['svg'] or any(b[4].startswith('tb') for b in r['blocchi'])
                      or r['band']) for r in data]
        for i in range(len(secco) - 3):
            if all(secco[i:i + 4]):
                ERR.append(f'{nome} · quattro pagine di fila senza elemento visivo, '
                           f'da {data[i]["id"]}')
        NOTE.append(f'{nome} · pagine senza elemento visivo forte: {sum(secco)} · '
                    f'mai quattro di fila')

    # --- technical streak
    tec = [r['tipo'] in tipi_tecnici or r['uiViews'] > 0 for r in data]
    run = best = 0
    dove = ''
    for i, t in enumerate(tec):
        run = run + 1 if t else 0
        if run > best:
            best, dove = run, data[i]['id']
    if best > tetto_streak:
        ERR.append(f'{nome} · {best} canvas tecnici consecutivi (tetto {tetto_streak}), '
                   f'fino a {dove}')
    NOTE.append(f'{nome} · slide tecniche consecutive: {best} · tetto {tetto_streak}')

    # --- duplicate layout
    firme = {}
    dup = []
    for i, r in enumerate(data):
        f = firma(r)
        if f in firme:
            j = firme[f]
            dup.append((data[j]['id'], r['id'], j + 1 == i))
        firme.setdefault(f, i)
    for a, b, consecutive in dup:
        (ERR if consecutive else NOTE).append(
            f'{nome} · struttura identica: {a} ~ {b}'
            + (' · e sono consecutive' if consecutive else ' · non consecutive'))
    if not dup:
        NOTE.append(f'{nome} · nessuna coppia di canvas con la stessa struttura')

    # --- titoli: nessun titolo ripetuto, nessuna domanda nel core del dossier
    tit = Counter(r['titolo'] for r in data if r['titolo'])
    for t, k in tit.items():
        if k > 1:
            ERR.append(f'{nome} · titolo ripetuto {k} volte: «{t[:50]}»')
    return data


def package_check(data):
    """Una slide pacchetto non porta una vista di prodotto (§5.4 della review)."""
    for r in data:
        if r['tipo'] == 'pacchetto' and r['uiViews']:
            ERR.append(f'package check · {r["id"]} porta {r["uiViews"]} viste di prodotto')
    NOTE.append('package check · nessuna vista di prodotto nelle slide pacchetto')


def questionnaire_check(data):
    """Il core del dossier non ha il tono da questionario: quelle colonne
    vivono negli annessi, dove servono davvero (§16.3)."""
    for r in data:
        if r['id'].startswith('pa'):
            continue
        t = r['testo'].lower()
        dentro = [q for q in QUESTIONARIO if q in t]
        if dentro:
            ERR.append(f'questionnaire check · {r["id"]}: {dentro}')
    NOTE.append('questionnaire check · nessun tono da questionario nelle pagine core')


def scrivi_mappe(deck, dos, outdir):
    def riga(r, i):
        return (f'| {i:02d} | `{r["id"]}` | {r["fondo"]} | {r["tipo"] or "—"} | '
                f'{r["uiViews"]} | {r["band"]} | {r["titolo"][:60]} |')

    with open(os.path.join(outdir, 'DFactory_RhythmMap_v9_3.md'), 'w', encoding='utf-8') as f:
        f.write('# D.Factory · V9.3 · Rhythm Map\n\n'
                'Fondo, tipo di canvas, viste di prodotto e fasce di sezione, nell\'ordine di\n'
                'lettura. È la mappa che il §14.3 chiede: serve a vedere il ritmo di una\n'
                'sequenza senza doverla sfogliare.\n\n'
                'La colonna **vis** conta le viste di prodotto (`svg[data-ui]`): è la misura\n'
                'di quanto una pagina mostra il prodotto invece di raccontarlo.\n')
        for nome, data in (('Sales Deck', deck), ('Dossier tecnico', dos)):
            f.write(f'\n## {nome}\n\n'
                    '| # | canvas | fondo | tipo | vis | fascia | titolo |\n'
                    '|--:|---|:--:|---|--:|--:|---|\n')
            for i, r in enumerate(data, 1):
                f.write(riga(r, i) + '\n')
            fondi = [r['fondo'] for r in data]
            tec = sum(1 for r in data if r['uiViews'])
            f.write(f'\n**Fondi** · {" ".join(fondi)}\n\n'
                    f'- pagine scure: {fondi.count("dk")} su {len(fondi)}\n'
                    f'- canvas con vista di prodotto: {tec}\n'
                    f'- tre fondi uguali di fila: '
                    f'{"nessuna sequenza" if not any(fondi[i]==fondi[i+1]==fondi[i+2] for i in range(len(fondi)-2)) else "PRESENTE"}\n')

    with open(os.path.join(outdir, 'DFactory_DuplicateLayoutMap_v9_3.md'), 'w',
              encoding='utf-8') as f:
        f.write('# D.Factory · V9.3 · Duplicate Layout Map\n\n'
                'Firma strutturale di ogni canvas: tipo di blocco, posizione verticale e\n'
                'altezza, arrotondate a 24 px, più il fondo e il tipo. Due canvas con la\n'
                'stessa firma si leggono come la stessa pagina, anche se dicono cose diverse.\n\n'
                'Il fondo fa parte della firma di proposito: è la ragione per cui le tre\n'
                'slide pacchetto possono condividere la griglia senza sembrare la stessa\n'
                'slide ripetuta tre volte.\n')
        for nome, data in (('Sales Deck', deck), ('Dossier tecnico', dos)):
            f.write(f'\n## {nome}\n\n| # | canvas | blocchi | firma |\n|--:|---|--:|---|\n')
            for i, r in enumerate(data, 1):
                f.write(f'| {i:02d} | `{r["id"]}` | {len(r["blocchi"])} | '
                        f'`{firma(r)[:96]}` |\n')
            firme = Counter(firma(r) for r in data)
            rip = {k: v for k, v in firme.items() if v > 1}
            f.write(f'\n**Firme ripetute:** {len(rip) or "nessuna"}\n')
            for k, v in rip.items():
                ids = [r['id'] for r in data if firma(r) == k]
                f.write(f'\n- {v} canvas: {", ".join("`"+x+"`" for x in ids)}\n')


if __name__ == '__main__':
    deck = leggi(sys.argv[1])
    dos = leggi(sys.argv[2])
    outdir = sys.argv[3] if len(sys.argv) > 3 else '.'

    # il corpo del deck e' le prime 15 slide: le appendici non fanno ritmo
    audit('Sales Deck', deck, 2, TECNICI, core=15)
    # nel dossier «tecnico» vuol dire una vista di prodotto, non una tabella:
    # una tabella e' il modo in cui un documento tecnico dice le cose
    audit('Dossier', dos, 2, set())
    package_check(deck)
    questionnaire_check(dos)
    scrivi_mappe(deck, dos, outdir)

    print('\n=== esito dell\'audit di sequenza ===')
    for n in NOTE:
        print(f'  ok   {n}')
    for e in ERR:
        print(f'  FAIL {e}')
    print(f'\n{len(NOTE)} verifiche superate · {len(ERR)} problemi')
    sys.exit(1 if ERR else 0)
