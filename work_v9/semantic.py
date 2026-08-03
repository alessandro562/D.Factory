#!/usr/bin/env python3
"""QA semantico: i termini che il brief V7 §15.3 vieta nei documenti client-facing.
Cerca sul testo visibile e sui testi accessibili, non sul sorgente: quello che conta
e' cio' che il lettore o lo screen reader ricevono."""
import re, sys, os
from playwright.sync_api import sync_playwright

VIETATI = [
    (r'\bInsights\b',            'grafia errata di Insight'),
    (r'proven legacy',           'classificazione interna'),
    (r'pilot release',           'stato di maturita interno'),
    (r'project.dependent',       'etichetta interna'),
    (r'\broadmap\b',             'roadmap di prodotto'),
    (r'not offered',             'classificazione interna'),
    (r'net.new',                 'classificazione interna'),
    (r'quota attaccabile',       'linguaggio economico non ammesso'),
    (r'costo reale del pezzo',   'si dispone del solo dato energetico'),
    (r'CO₂ misurata|CO2 misurata', 'la CO2 e calcolata o stimata'),
    (r'conforme a? ?ISO 50001|certificat\w+ ISO 50001', 'nessuna certificazione'),
    (r'SAP nativ|connettore SAP|certificato SAP', 'nessuna integrazione SAP dichiarata'),
    (r'qualsiasi protocollo|qualsiasi marca', 'compatibilita verificata in audit'),
    (r'Refyn su richiesta',      'formulazione non ammessa'),
    (r'(?<!non )risultato cliente', 'gli scenari non sono risultati cliente'),
    (r'(?-i:\bAI\b)|intelligenza artificiale', 'non dichiarare AI'),
    (r'manutenzione predittiva', 'funzione non approvata'),
    (r'qualita predittiva|qualità predittiva', 'funzione non approvata'),
    (r'risparmio garantito|payback garantito|margine perso certo', 'linguaggio economico non ammesso'),
    (r'plug.and.play',           'nessuna integrazione garantita'),
]

def testo(html):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                              args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': 1280, 'height': 720})
        pg.goto('file://' + os.path.abspath(html), wait_until='networkidle')
        out = pg.evaluate("""() => [...document.querySelectorAll('.slide')].map(s => {
            const t = [...s.querySelectorAll('title, desc')].map(n => n.textContent).join(' ');
            return [s.id, (s.innerText + ' ' + s.textContent + ' ' + t).replace(/\\s+/g,' ')];
        })""")
        b.close()
    return out

n = 0
for f in sys.argv[1:]:
    print('\n=== %s ===' % os.path.basename(f))
    for sid, t in testo(f):
        for pat, perche in VIETATI:
            for m in re.finditer(pat, t, re.I):
                a = max(0, m.start() - 45)
                print('  ! %-24s %-22s "…%s…"' % (sid, m.group(0), t[a:m.end() + 45]))
                n += 1
print('\ntermini vietati trovati: %s' % (n or 'nessuno'))
sys.exit(1 if n else 0)
