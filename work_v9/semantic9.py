#!/usr/bin/env python3
"""QA editoriale V9 · §2.4 e §13.2.

Controlla il testo visibile e quello accessibile (title/desc) di un HTML:
  - i venti termini vietati della §2.4;
  - le forme obbligatorie della §13.2;
  - «in sviluppo» dichiarato una volta sola per documento;
  - i sub-brand vietati della §3.1;
  - i placeholder residui (§11.4).
"""
import re
import sys
from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

# (etichetta, regex) — case-insensitive salvo dove indicato
VIETATI = [
    ('Insights (plurale)', r'\bInsights\b'),
    ('costo reale del pezzo', r'costo reale del pezzo'),
    ('causa rilevata automaticamente', r'caus\w+ rilevat\w+ automaticamente'),
    ('risparmio garantito', r'risparmi\w* garantit\w*'),
    ('quota attaccabile', r'quota attaccabile'),
    ('qualsiasi protocollo', r'qualsiasi protocoll\w*'),
    ('SAP nativo', r'SAP\s+nativ\w*'),
    ('conforme ISO 50001', r'conform\w+\s+(?:a\s+|alla\s+)?ISO\s*50001'),
    ('CO2 misurata', r'CO.?\s*misurat\w*'),
    ('zero hardware', r'zero\s+hardware'),
    ('Refyn su richiesta', r'Refyn\s+su\s+richiesta'),
    ('AI', r'(?-i:\bAI\b)'),
    ('predictive maintenance', r'predictive\s+maintenance'),
    ('manutenzione predittiva', r'manutenzione\s+predittiv\w*'),
    ('predictive quality', r'predictive\s+quality'),
    ('proven legacy', r'proven\s+legacy'),
    ('pilot release', r'pilot\s+release'),
    ('project-dependent', r'project[-\s]dependent'),
    ('not offered', r'not\s+offered'),
    ('net-new', r'net[-\s]new'),
    ('roadmap', r'\broadmap\b'),
    # §3.1 · nessun sub-brand
    ('sub-brand Refyn by D.Factory', r'Refyn\s+by\s+D\.?Factory'),
    ('sub-brand D.Factory Connect', r'D\.?Factory\s+Connect'),
    ('sub-brand D.Factory Insight', r'D\.?Factory\s+Insight'),
    ('sub-brand D.Factory Refyn', r'D\.?Factory\s+Refyn'),
    # §2.2 · claim assoluti
    ('claim assoluto «nessuna sostituzione richiesta»', r'nessuna sostituzione richiesta'),
    ('claim assoluto «garantito»', r'\bgarantit[oa]\b'),
]

JS = r"""
() => {
  const t = [];
  for (const el of document.querySelectorAll('.slide')) t.push(el.innerText);
  for (const el of document.querySelectorAll('title, desc')) t.push(el.textContent);
  return t.join('\n');
}
"""


def check(path):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': 1320, 'height': 900})
        pg.goto('file://' + __import__('os').path.abspath(path))
        pg.wait_for_timeout(400)
        txt = pg.evaluate(JS)
        b.close()

    print(f'\n=== {path} ===')
    bad = []
    for label, rx in VIETATI:
        for m in re.finditer(rx, txt, re.I):
            ctx = txt[max(0, m.start() - 40):m.end() + 40].replace('\n', ' ')
            bad.append((label, ctx))
    print(f'termini vietati: {len(bad) or "nessuno"}')
    for label, ctx in bad[:10]:
        print(f'      ! {label} — …{ctx}…')

    # §13.2 · forme obbligatorie
    dev = len(re.findall(r'in sviluppo', txt, re.I))
    print(f'«in sviluppo»: {dev} occorrenze' + ('  [§13.2 chiede una sola dichiarazione]'
                                                if dev > 1 else ''))
    for must, label in ((r'causa associata', 'causa associata'),
                        (r'costo energetico', 'costo energetico'),
                        (r'CO.\s*calcolata o stimata|CO. calcolata', 'CO₂ calcolata o stimata')):
        n = len(re.findall(must, txt, re.I))
        print(f'«{label}»: {n}')

    brand = re.findall(r'D\s*\.?\s*Factory', txt)
    forms = set(x.replace(' ', '') for x in brand)
    print(f'grafie del brand: {sorted(forms)} ({len(brand)} occorrenze)')

    left = re.findall(r'\{\{PH_[A-Z0-9_]+\}\}', txt)
    print(f'placeholder visibili: {len(left) or "nessuno"}')
    return bad, left


if __name__ == '__main__':
    for f in sys.argv[1:]:
        check(f)
