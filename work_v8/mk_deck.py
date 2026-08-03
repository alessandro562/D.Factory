#!/usr/bin/env python3
"""Assembla il corpo del Sales Deck v8: 16 slide + 5 appendici.

Non riscrive i prototipi approvati e non tocca il sistema visuale: prende i sei
prototipi dalla Fase B, le slide riuscite della V7, e aggiunge soltanto i canvas
che non esistevano. Le correzioni della Fase C sono applicate qui, in un punto
solo, cosi' si vedono tutte insieme.
"""
import re, sys

PROTO = 'proto_deck_body.html'
V7 = '../work_v7/deck_body.html'


def slides(path):
    s = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<div class="slide[^>]*id="([^"]+)"[^>]*>', s):
        start = m.start()
        end = s.index('\n</div>', start) + len('\n</div>')
        out[m.group(1)] = s[start:end]
    return out


P = slides(PROTO)
V = slides(V7)


def rail(html, page, note=None):
    """Riscrive il rail: numero di pagina su 16 e nota di piede."""
    if note is None:
        new = ('<div class="rail"><span class="wm">D<i>.</i>Factory</span>'
               f'<span>{page}</span></div>')
    else:
        new = ('<div class="rail"><span class="wm">D<i>.</i>Factory</span>\n'
               f'    <span class="nt">{note}</span><span>{page}</span></div>')
    if 'class="rail"' in html:
        return re.sub(r'<div class="rail">.*?</div>', new, html, flags=re.S)
    return html.replace('\n</div>', '\n  ' + new + '\n</div>')


def rid(html, new_id):
    return re.sub(r'(<div class="slide[^>]*id=")[^"]+(")', r'\g<1>' + new_id + r'\g<2>', html, count=1)


out = []
def add(html):
    out.append(html)


# =====================================================================
# 01 · COVER · prototipo approvato, invariato
# =====================================================================
add(rid(P['p1_cover'], 's01_cover'))

# =====================================================================
# 02 · TENSIONE · prototipo approvato, invariato
# =====================================================================
add(rail(rid(P['p2_tensione'], 's02_tensione'), '02 / 16'))

# =====================================================================
# 03 · CATEGORIA · «evidenze» -> «informazioni operative» (Fase C)
# =====================================================================
s = rid(P['p3_categoria'], 's03_categoria')
s = s.replace('in evidenze operative.', 'in informazioni operative.')
add(rail(s, '03 / 16', 'Vista ricostruita · dati illustrativi'))

# =====================================================================
# 04 · L'EVENTO · la cover V7 diventa la prima dimostrazione
# =====================================================================
s = rid(V['s01_cover'], 's04_evento')
s = s.replace('  <div class="z" style="top:52px"><span class="wm" style="font-size:19px">D<i>.</i>Factory</span></div>\n\n', '')
s = s.replace('<div class="z" style="top:88px;width:1040px">\n    <h1>',
              '<div class="z" style="top:48px;width:1040px">\n    <h2 class="sm">')
s = s.replace('E un costo.</h1>', 'E un costo.</h2>')
s = s.replace('<div class="z" style="top:218px"><div class="sup">Supervisione di produzione ed energia\n'
              '    per le linee food &amp; beverage.</div></div>',
              '<div class="z" style="top:152px;width:980px"><div class="sup">Un fermo di diciotto minuti\n'
              '    sulla tappatrice, la sua causa e il suo costo, nella stessa vista.</div></div>')
s = s.replace('style="position:absolute;left:0;top:264px"', 'style="position:absolute;left:0;top:220px"')
add(rail(s, '04 / 16', 'Vista ricostruita · dati illustrativi'))

# =====================================================================
# 05 · PRODOTTO · benchmark visuale, invariato
# =====================================================================
add(rail(rid(V['s04_prodotto'], 's05_prodotto'), '05 / 16', 'Vista ricostruita · dati illustrativi'))

# =====================================================================
# 06 · ENERGIA · headline a una riga, la seconda riga era gia' il titolo
# =====================================================================
s = rid(V['s05_energia'], 's06_energia')
s = s.replace('<h2 class="sm">La linea si ferma.<br>L’energia continua a scorrere.</h2>',
              '<h2 class="sm">Lo stesso minuto pesa su capacità e consumi.</h2>')
s = s.replace('  <div class="z" style="top:152px"><div class="cp">Lo stesso minuto pesa su capacità e consumi.</div></div>\n\n',
              '  <div class="z" style="top:120px;width:1000px"><div class="cp">La linea si ferma, '
              'l’energia continua a scorrere.</div></div>\n\n')
s = s.replace('style="position:absolute;left:0;top:206px"', 'style="position:absolute;left:0;top:186px"')
add(rail(s, '06 / 16', 'Vista ricostruita · dati illustrativi'))

# =====================================================================
# 07 · PRIORITA' · titolo dello storyboard + micro-riga di decisione
# =====================================================================
s = rid(V['s06_decisione'], 's07_priorita')
s = s.replace('<h2 class="sm">Un fermo è una causa.<br>Quattordici sono una priorità.</h2>',
              '<h2 class="sm">Un fermo è un evento.<br>Quattordici diventano una priorità.</h2>')
s = s.replace('''<text x="1216" y="418" font-family="Geist" font-size="22" font-weight="600" fill="#0A0A0A"
          text-anchor="end">15.680 €</text>''',
              '''<text x="1216" y="418" font-family="Geist" font-size="22" font-weight="600" fill="#0A0A0A"
          text-anchor="end">15.680 €</text>
    <text x="64" y="452" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">La prima priorità è la causa che costa di più, non quella che si ripete di più: le micro-fermate sono 38 eventi e valgono meno della metà.</text>''')
add(rail(s, '07 / 16', 'Vista ricostruita · dati illustrativi'))

# =====================================================================
# 08 · AMPIEZZA · rifatta: quattro aree guidate, non sei riquadri
# =====================================================================
add('''<!-- ============ 08 · DALLA MACCHINA AL PEZZO ==========================
     La V7 aveva sei riquadri equivalenti. Qui la stessa finestra e' letta
     dall'alto in basso in quattro passaggi che seguono il titolo: macchina,
     linea, turno, pezzo. Ogni banda porta un dato solo. -->
<div class="slide dk" id="s08_ampiezza">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Dalla macchina al pezzo,<br>senza cambiare contesto.</h2>
  </div>

  <svg data-ui="1" width="1280" height="452" viewBox="0 0 1280 452"
       style="position:absolute;left:0;top:176px" role="img" aria-labelledby="w8t w8d">
    <title id="w8t">La stessa finestra letta in quattro passaggi</title>
    <desc id="w8d">Dallo stato delle tre macchine all&rsquo;OEE della linea, al consumo del
      turno, al consumo, costo ed emissioni per mille pezzi. Vista ricostruita, dati
      illustrativi.</desc>

    <rect x="0" y="0" width="1280" height="452" fill="#141414"/>
    <path d="M0 .75 L1280 .75" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>
    <text x="64" y="34" font-family="Geist" font-size="15" font-weight="600" fill="#FFFFFF">Linea 1 · Confezionamento</text>
    <text x="1216" y="34" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)"
          text-anchor="end">turno 06:00 – 14:00</text>
    <g stroke="rgba(255,255,255,.14)">
      <path d="M0 52 L1280 52"/><path d="M0 152 L1280 152"/><path d="M0 252 L1280 252"/><path d="M0 352 L1280 352"/>
    </g>

    <g font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.44)">
      <text x="64" y="82">01</text><text x="64" y="182">02</text>
      <text x="64" y="282">03</text><text x="64" y="382">04</text>
    </g>
    <g font-family="Geist" font-size="19" font-weight="600" fill="#FFFFFF">
      <text x="104" y="82">Macchina</text><text x="104" y="182">Linea</text>
      <text x="104" y="282">Turno</text><text x="104" y="382">Pezzo</text>
    </g>
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">
      <text x="104" y="106">stato e fermi</text><text x="104" y="206">OEE e fattori</text>
      <text x="104" y="306">energia e costo</text><text x="104" y="406">consumo specifico</text>
    </g>

    <!-- 01 · macchina -->
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.56)">
      <text x="300" y="85">Riempitrice</text><text x="300" y="107">Etichettatrice</text><text x="300" y="129">Tappatrice</text>
    </g>
    <g fill="rgba(255,255,255,.09)">
      <rect x="420" y="74" width="500" height="14"/><rect x="420" y="96" width="500" height="14"/>
      <rect x="420" y="118" width="500" height="14"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="420" y="74" width="322" height="14"/><rect x="768" y="74" width="152" height="14"/>
      <rect x="420" y="96" width="322" height="14"/><rect x="768" y="96" width="152" height="14"/>
      <rect x="420" y="118" width="322" height="14"/><rect x="768" y="118" width="152" height="14"/>
    </g>
    <rect x="742" y="118" width="26" height="14" fill="#E6E011"/>
    <text x="1216" y="107" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"
          text-anchor="end">3 fermi · 26 minuti</text>

    <!-- 02 · linea -->
    <text x="300" y="200" font-family="Geist" font-size="34" font-weight="600" fill="#FFFFFF">71,4%</text>
    <text x="300" y="224" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">OEE del turno</text>
    <g font-family="Geist" font-size="13" fill="rgba(255,255,255,.56)">
      <text x="500" y="182">disponibilità</text><text x="500" y="206">performance</text><text x="500" y="230">qualità</text>
    </g>
    <g fill="rgba(255,255,255,.09)">
      <rect x="660" y="172" width="200" height="11"/><rect x="660" y="196" width="200" height="11"/>
      <rect x="660" y="220" width="200" height="11"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="660" y="172" width="189" height="11"/><rect x="660" y="196" width="158" height="11"/>
      <rect x="660" y="220" width="191" height="11"/>
    </g>
    <g font-family="Geist" font-size="13" fill="rgba(255,255,255,.72)" text-anchor="end">
      <text x="960" y="182">94,6%</text><text x="960" y="206">79%</text><text x="960" y="230">95,6%</text>
    </g>
    <text x="1216" y="207" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"
          text-anchor="end">tre fattori dichiarati</text>

    <!-- 03 · turno -->
    <text x="300" y="300" font-family="Geist" font-size="28" font-weight="600" fill="#FFFFFF">735<tspan font-size="16"> kWh</tspan></text>
    <text x="300" y="324" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">consumo del turno</text>
    <rect x="500" y="288" width="460" height="14" fill="rgba(255,255,255,.82)"/>
    <rect x="950" y="288" width="10" height="14" fill="rgba(255,255,255,.34)"/>
    <text x="500" y="324" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">719 kWh in marcia · 16 kWh a impianto fermo</text>
    <text x="1216" y="307" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"
          text-anchor="end">162 € di energia</text>

    <!-- 04 · pezzo -->
    <g font-family="Geist" font-size="24" font-weight="600" fill="#FFFFFF">
      <text x="300" y="404">3,2</text><text x="600" y="404">0,71</text><text x="900" y="404">1,13</text>
    </g>
    <g font-family="Geist" font-size="13" fill="rgba(255,255,255,.56)">
      <text x="360" y="404">kWh / 1.000 pz</text><text x="676" y="404">€ / 1.000 pz</text>
      <text x="960" y="404">kgCO₂e / 1.000 pz</text>
    </g>
    <text x="300" y="432" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">735 kWh ÷ 227.000 pezzi × 1.000 · CO₂ calcolata o stimata</text>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span>
    <span class="nt">Viste ricostruite · dati illustrativi</span><span>08 / 16</span></div>
</div>''')

# =====================================================================
# 09 · OFFERTA · prototipo approvato + micro-correzioni della review
# =====================================================================
s = rid(P['p4_offerta'], 's09_offerta')
# Refyn non e' un workflow gia' attivo: stesso trattamento della slide 03
s = s.replace('''<text x="1216" y="322" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)"
          text-anchor="end">in corso</text>''',
              '''<text x="1216" y="322" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)"
          text-anchor="end">azione proposta</text>''')
s = s.replace('''<g font-family="Geist" font-size="14" fill="rgba(10,10,10,.78)">
      <text x="470" y="374">Baseline 96 min</text><text x="700" y="374">4 settimane osservate</text>
      <text x="990" y="374">risultato da leggere</text>
    </g>''',
              '''<rect x="470" y="362" width="240" height="14" fill="#0A0A0A"/>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.78)">
      <text x="730" y="374">Baseline 96 min</text><text x="990" y="374">verifica proposta a 4 settimane</text>
    </g>''')
# le due righe di base erano troppo chiare per essere lette
s = s.replace('''<text x="64" y="434" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">Base comune a tutti i livelli · produzione, energia e storico</text>
    <text x="1216" y="434" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)"
          text-anchor="end">servizi specialistici attivabili su ogni livello</text>''',
              '''<text x="64" y="434" font-family="Geist" font-size="15" fill="rgba(10,10,10,.78)">Base comune a tutti i livelli · produzione, energia e storico</text>
    <text x="1216" y="434" font-family="Geist" font-size="15" fill="rgba(10,10,10,.78)"
          text-anchor="end">servizi specialistici attivabili su ogni livello</text>''')
add(rail(s, '09 / 16', 'Vista ricostruita · dati illustrativi'))

# =====================================================================
# 10 · LIVELLI · «come si attiva», niente stati di approvazione
# =====================================================================
s = rid(P['p5_pacchetti'], 's10_livelli')
s = s.replace('>COME SI ACQUISTA<', '>COME SI ATTIVA<')
s = s.replace('''<text x="64" y="362">Avvio, poi canone</text><text x="64" y="388">ricorrente.</text>
      <text x="464" y="362">Canone superiore</text><text x="464" y="388">a Connect, da approvare.</text>
      <text x="864" y="362">Modello economico</text><text x="864" y="388">da approvare.</text>''',
              '''<text x="64" y="362">Audit, configurazione</text><text x="64" y="388">e canone ricorrente.</text>
      <text x="464" y="362">Attivazione sullo stesso</text><text x="464" y="388">impianto, con capacità</text>
      <text x="464" y="414">analitiche aggiuntive.</text>
      <text x="864" y="362">Attivazione attraverso</text><text x="864" y="388">un progetto pilota</text>
      <text x="864" y="414">dedicato.</text>''')
s = s.replace('<path d="M64 424 L1216 424" stroke="rgba(10,10,10,.30)"/>',
              '<path d="M64 442 L1216 442" stroke="rgba(10,10,10,.30)"/>')
s = s.replace('<text x="64" y="450" font-family="Geist" font-size="15" fill="rgba(10,10,10,.58)">Importi, inclusioni e durata contrattuale: appendice commerciale.</text>',
              '<text x="64" y="468" font-family="Geist" font-size="15" fill="rgba(10,10,10,.58)">Prezzi, inclusioni e durata contrattuale sono nell’appendice pricing.</text>')
s = s.replace('width="1280" height="460" viewBox="0 0 1280 460"', 'width="1280" height="478" viewBox="0 0 1280 478"')
s = s.replace('<path d="M440 0 L440 400"/><path d="M840 0 L840 400"/>',
              '<path d="M440 0 L440 424"/><path d="M840 0 L840 424"/>')
s = s.replace('Nessun\n      importo: il modello economico non è ancora approvato.',
              'I prezzi\n      sono nell’appendice pricing.')
add(rail(s, '10 / 16'))

# =====================================================================
# 11 · SERVIZI · nuova
# =====================================================================
add('''<!-- ================= 11 · SERVIZI A VALORE AGGIUNTO ===================
     Una fascia software al centro e quattro interventi attorno, ognuno con
     l'output che produce: il nome di un servizio non dice niente, il suo
     deliverable si'. -->
<div class="slide dk" id="s11_servizi">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Il software rende visibile.<br>Le competenze accelerano il risultato.</h2>
  </div>

  <svg data-ui="1" width="1280" height="430" viewBox="0 0 1280 430"
       style="position:absolute;left:0;top:190px" role="img" aria-labelledby="v1t v1d">
    <title id="v1t">Quattro interventi attorno alla piattaforma</title>
    <desc id="v1d">Assessment, configurazione dei KPI, review di performance ed energia,
      formazione e scale-up. Ogni intervento produce un output concreto e si appoggia alla
      stessa piattaforma.</desc>

    <g fill="none" stroke="rgba(255,255,255,.30)">
      <rect x="64" y="0" width="548" height="104"/><rect x="668" y="0" width="548" height="104"/>
      <rect x="64" y="316" width="548" height="104"/><rect x="668" y="316" width="548" height="104"/>
    </g>
    <g stroke="rgba(255,255,255,.30)" fill="none">
      <path d="M338 104 L338 154"/><path d="M942 104 L942 154"/>
      <path d="M338 266 L338 316"/><path d="M942 266 L942 316"/>
    </g>

    <rect x="64" y="154" width="1152" height="112" fill="rgba(255,255,255,.10)"/>
    <text x="88" y="196" font-family="Geist" font-size="22" font-weight="600" fill="#FFFFFF">D.Factory · la piattaforma</text>
    <text x="88" y="228" font-family="Geist" font-size="15" fill="rgba(255,255,255,.74)">misura, contestualizza e restituisce lo stesso dato a tutti i livelli</text>
    <text x="1192" y="196" font-family="Geist" font-size="15" fill="rgba(255,255,255,.74)"
          text-anchor="end">Connect · Insight · Refyn</text>

    <g font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.44)">
      <text x="88" y="34">01</text><text x="692" y="34">02</text>
      <text x="88" y="350">03</text><text x="692" y="350">04</text>
    </g>
    <g font-family="Geist" font-size="19" font-weight="600" fill="#FFFFFF">
      <text x="128" y="34">Assessment e perimetrazione</text><text x="732" y="34">Configurazione di KPI e formule</text>
      <text x="128" y="350">Performance ed energy review</text><text x="732" y="350">Formazione, supporto e scale-up</text>
    </g>
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">
      <text x="88" y="76">OUTPUT</text><text x="692" y="76">OUTPUT</text>
      <text x="88" y="392">OUTPUT</text><text x="692" y="392">OUTPUT</text>
    </g>
    <g font-family="Geist" font-size="16" fill="rgba(255,255,255,.82)">
      <text x="168" y="76">mappa dei dati e dei gap</text><text x="772" y="76">dizionario delle formule</text>
      <text x="168" y="392">priorità e report del periodo</text><text x="772" y="392">nuova linea attivata</text>
    </g>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span><span>11 / 16</span></div>
</div>''')

# =====================================================================
# 12 · PERCHE' · prototipo approvato, invariato
# =====================================================================
add(rail(rid(P['p6_perche'], 's12_perche'), '12 / 16'))

# =====================================================================
# 13 · VALORE · rifatta come canvas: qui il numero E' il visual, e classificarlo
#      come copy avrebbe gonfiato il conteggio di una slide fatta di due cifre
# =====================================================================
add('''<!-- ================== 13 · IL VALORE DELLE DUE LEVE ==================
     La catena aritmetica, il costo annuo di una causa, e le due leve alla
     pari. Le assunzioni non stanno qui: stanno in A5. -->
<div class="slide dk" id="s13_valore">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Il valore nasce da due leve:<br>capacità e consumi.</h2>
  </div>

  <svg data-ui="1" width="1280" height="440" viewBox="0 0 1280 440"
       style="position:absolute;left:0;top:176px" role="img" aria-labelledby="x3t x3d">
    <title id="x3t">Il costo annuo di una causa e le due leve del valore</title>
    <desc id="x3d">Novantasei minuti a settimana per settanta euro al minuto per
      quarantasei settimane fanno trecentonovemilacentoventi euro. Da lì le due leve:
      centocinquantaquattromilacinquecentosessanta euro di capacità se la causa si dimezza,
      ottocentodieci euro di energia evitabile. Scenario illustrativo.</desc>

    <text x="64" y="34" font-family="Geist" font-size="26" fill="rgba(255,255,255,.74)">96 min a settimana &#160;×&#160; 70 € al minuto &#160;×&#160; 46 settimane</text>
    <text x="64" y="164" font-family="Geist" font-size="118" font-weight="600" fill="#E6E011"
          letter-spacing="-5">309.120<tspan font-size="38"> €</tspan></text>
    <text x="64" y="208" font-family="Geist" font-size="17" fill="rgba(255,255,255,.74)">il costo annuo di una sola causa non chiusa</text>

    <path d="M64 254 L1216 254" stroke="rgba(255,255,255,.16)"/>
    <text x="64" y="290" font-family="Geist" font-size="13" fill="rgba(255,255,255,.48)"
          letter-spacing="1">LE DUE LEVE DEL VALORE</text>

    <g font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.44)">
      <text x="64" y="336">01</text><text x="672" y="336">02</text>
    </g>
    <g font-family="Geist" font-size="17" fill="rgba(255,255,255,.74)">
      <text x="104" y="336">Capacità recuperabile</text><text x="712" y="336">Energia evitabile</text>
    </g>
    <g font-family="Geist" font-size="40" font-weight="600" fill="#FFFFFF">
      <text x="64" y="392">154.560 €</text><text x="672" y="392">810 €</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(255,255,255,.48)">
      <text x="64" y="424">se la causa si dimezza</text><text x="672" y="424">dai 16 kWh per turno a linea ferma</text>
    </g>
    <g stroke="rgba(255,255,255,.16)"><path d="M64 310 L592 310"/><path d="M672 310 L1200 310"/></g>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span>
    <span class="nt">Scenario illustrativo · assunzioni in appendice A5</span><span>13 / 16</span></div>
</div>''')

# =====================================================================
# 14 · STRUTTURA ECONOMICA · nuova, nessun importo
# =====================================================================
add('''<!-- ============ 14 · SI PARTE DA UNA LINEA ============================
     Le tre voci del modello e i loro moltiplicatori. Nessun importo: i
     prezzi entrano nell'appendice pricing quando sono approvati. -->
<div class="slide lt" id="s14_struttura">
  <div class="z" style="top:48px;width:1140px">
    <h2 class="sm">Si parte da una linea. Il canone cresce<br>con il perimetro e con il livello.</h2>
  </div>

  <svg data-ui="1" width="1280" height="404" viewBox="0 0 1280 404"
       style="position:absolute;left:0;top:200px" role="img" aria-labelledby="y4t y4d">
    <title id="y4t">Le tre voci del modello economico</title>
    <desc id="y4d">Avvio una tantum, canone ricorrente che cresce con il perimetro
      attivato, servizi opzionali. I moltiplicatori del canone sono il numero di siti,
      il numero di linee e il livello.</desc>

    <rect x="64" y="0" width="1152" height="300" fill="#F3F4F0"/>
    <g stroke="rgba(10,10,10,.13)"><path d="M448 24 L448 276"/><path d="M832 24 L832 276"/></g>

    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.42)">
      <text x="88" y="48">01</text><text x="472" y="48">02</text><text x="856" y="48">03</text>
    </g>
    <g font-family="Geist" font-size="22" font-weight="600" fill="#0A0A0A">
      <text x="88" y="82">Avvio</text><text x="472" y="82">Canone</text><text x="856" y="82">Servizi</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">
      <text x="180" y="82">una tantum</text><text x="600" y="82">ricorrente</text><text x="960" y="82">opzionali</text>
    </g>
    <g stroke="rgba(10,10,10,.13)">
      <path d="M88 102 L424 102"/><path d="M472 102 L808 102"/><path d="M856 102 L1192 102"/>
    </g>

    <g font-family="Geist" font-size="16" fill="#0A0A0A">
      <text x="88" y="136">Audit e perimetrazione</text><text x="88" y="166">Setup e integrazione</text>
      <text x="88" y="196">Configurazione dei KPI</text>
      <text x="472" y="136">Per sito</text><text x="472" y="166">Per linea collegata</text>
      <text x="472" y="196">Per livello attivato</text>
      <text x="856" y="136">Review periodiche</text><text x="856" y="166">Formazione e supporto</text>
      <text x="856" y="196">Estensione a nuove linee</text>
    </g>

    <!-- il canone cresce a gradini con il perimetro: la forma, non l'importo -->
    <g fill="rgba(10,10,10,.20)">
      <rect x="472" y="242" width="72" height="12"/><rect x="556" y="230" width="72" height="24"/>
      <rect x="640" y="214" width="72" height="40"/>
    </g>
    <text x="472" y="274" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)">una linea · più linee · più siti</text>

    <path d="M64 340 L1216 340" stroke="rgba(10,10,10,.30)"/>
    <text x="64" y="374" font-family="Geist" font-size="17" fill="rgba(10,10,10,.78)">Si comincia da una linea sola. Il canone segue il perimetro attivato e il livello scelto; gli importi arrivano con la proposta economica.</text>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span><span>14 / 16</span></div>
</div>''')

# =====================================================================
# 15 · PILOT · la struttura economica esce (ora e' la 14), entrano i criteri
# =====================================================================
s = rid(V['s11_pilot'], 's15_pilot')
old = s[s.index('    <path d="M0 292 L1280 292"'):s.index('  </svg>')]
s = s.replace(old, '''    <path d="M0 292 L1280 292" stroke="rgba(10,10,10,.16)"/>
    <text x="64" y="322" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Criteri di accettazione del pilot</text>
    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.42)">
      <text x="64" y="366">01</text><text x="482" y="366">02</text><text x="900" y="366">03</text>
    </g>
    <g font-family="Geist" font-size="17" fill="#0A0A0A">
      <text x="104" y="366">La baseline è ricostruibile</text><text x="522" y="366">Le cause sono associate</text>
      <text x="940" y="366">Il consumo è leggibile</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.74)">
      <text x="104" y="396">dai dati raccolti sulla linea</text><text x="522" y="396">e validate da chi le conosce</text>
      <text x="940" y="396">per stato e per pezzo</text>
    </g>
    <text x="64" y="428" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Durata, partecipanti e condizioni economiche si fissano nella proposta di pilot.</text>
''')
s = s.replace('durate da definire in solution design', 'perimetro e criteri concordati prima di partire')
add(rail(s, '15 / 16'))

# =====================================================================
# 16 · CALL TO ACTION
# =====================================================================
s = rid(V['s12_cta'], 's16_cta')
s = s.replace('<div class="z" style="top:56px;width:1100px">\n    <h1>Partiamo dalla linea<br>che costa di più.</h1>\n  </div>',
              '<div class="z" style="top:48px;width:1140px">\n    <h2 class="sm">Partiamo dalla linea<br>con il maggiore costo nascosto.</h2>\n  </div>')
s = s.replace('<div class="z" style="top:190px;width:980px">', '<div class="z" style="top:182px;width:980px">')
s = s.replace('style="position:absolute;left:0;top:250px"', 'style="position:absolute;left:0;top:240px"')
add(rail(s, '16 / 16', 'Scenario illustrativo · non risultato cliente'))

# =====================================================================
# A1 · MATRICE · aggiunta la riga «cliente ideale», contrasto alzato
# =====================================================================
s = rid(V['a1_pacchetti'], 'a1_matrice')
s = s.replace('width="1280" height="440" viewBox="0 0 1280 392"', 'width="1280" height="470" viewBox="0 0 1280 436"')
s = s.replace('<text x="64" y="384">Verifica dei benefici</text>',
              '<text x="64" y="384">Verifica dei benefici</text>\n      <text x="64" y="428">Cliente ideale</text>')
s = s.replace('''      <text x="836" y="384">Non incluso</text><text x="1000" y="384">Non incluso</text><text x="1164" y="384">Previsto</text>
    </g>''',
              '''      <text x="836" y="384">Non incluso</text><text x="1000" y="384">Non incluso</text><text x="1164" y="384">Previsto</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.78)" text-anchor="middle">
      <text x="836" y="422">chi non ha ancora</text><text x="836" y="440">una baseline condivisa</text>
      <text x="1000" y="422">chi ha la baseline</text><text x="1000" y="440">e vuole capire le perdite</text>
      <text x="1164" y="422">chi vuole governare</text><text x="1164" y="440">le azioni e verificarle</text>
    </g>''')
s = s.replace('<path d="M64 356 L1216 356"/>', '<path d="M64 356 L1216 356"/><path d="M64 400 L1216 400" stroke="rgba(10,10,10,.26)"/>')
s = s.replace('<g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)" text-anchor="middle">',
              '<g font-family="Geist" font-size="15" fill="#0A0A0A" text-anchor="middle">')
s = s.replace('style="position:absolute;left:0;top:132px"', 'style="position:absolute;left:0;top:120px"')
s = s.replace('''  <div class="z" style="top:596px"><div class="cp">Insight comprende Connect. Refyn comprende
    Connect e Insight. Refyn è il modulo avanzato in sviluppo. Il perimetro effettivo dipende
    dai dati disponibili e dalla configurazione dell’impianto.</div></div>''',
              '''  <div class="z" style="top:614px"><div class="note">Insight comprende Connect, Refyn comprende
    entrambi. Refyn è il modulo avanzato in sviluppo. Il perimetro effettivo dipende dai dati
    disponibili e dalla configurazione dell’impianto.</div></div>''')
add(rail(s, 'A1'))

# =====================================================================
# A2 · SERVIZI · da elenco a tabella: servizio, output, quando
# =====================================================================
add('''<!-- ===================== A2 · SERVIZI E DELIVERABLE ===================
     La colonna «incluso / opzionale» non c'e': le inclusioni sono una
     decisione commerciale non ancora chiusa e stanno nella proposta. -->
<div class="slide lt" id="a2_servizi">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Ogni servizio produce un deliverable.</h2>
  </div>

  <svg data-ui="1" width="1280" height="452" viewBox="0 0 1280 452"
       style="position:absolute;left:0;top:140px" role="img" aria-labelledby="g2t g2d">
    <title id="g2t">Nove servizi con il loro output</title>
    <desc id="g2d">Per ogni servizio il deliverable che produce e la frequenza con cui
      viene erogato.</desc>

    <g font-family="Geist" font-size="14" font-weight="500" fill="rgba(10,10,10,.56)">
      <text x="64" y="24">Servizio</text><text x="560" y="24">Output</text><text x="1216" y="24" text-anchor="end">Quando</text>
    </g>
    <path d="M64 40 L1216 40" stroke="rgba(10,10,10,.26)"/>

    <g font-family="Geist" font-size="16" fill="#0A0A0A">
      <text x="64" y="76">Assessment e perimetrazione</text><text x="64" y="122">Setup e integrazione</text>
      <text x="64" y="168">Configurazione di KPI e formule</text><text x="64" y="214">Data quality review</text>
      <text x="64" y="260">Performance ed energy review</text><text x="64" y="306">Improvement sprint</text>
      <text x="64" y="352">Formazione</text><text x="64" y="398">Supporto</text>
      <text x="64" y="444">Estensione a nuove linee</text>
    </g>
    <g font-family="Geist" font-size="16" fill="rgba(10,10,10,.78)">
      <text x="560" y="76">mappa dei dati e dei gap</text><text x="560" y="122">ambiente configurato e collegato</text>
      <text x="560" y="168">dizionario delle formule</text><text x="560" y="214">elenco delle anomalie e delle correzioni</text>
      <text x="560" y="260">priorità e report del periodo</text><text x="560" y="306">azioni, baseline e verifica</text>
      <text x="560" y="352">operatori e referenti abilitati</text><text x="560" y="398">canale e tempi concordati</text>
      <text x="560" y="444">nuova linea o nuovo sito attivato</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)" text-anchor="end">
      <text x="1216" y="76">avvio</text><text x="1216" y="122">avvio</text><text x="1216" y="168">avvio</text>
      <text x="1216" y="214">periodica</text><text x="1216" y="260">periodica</text><text x="1216" y="306">a progetto</text>
      <text x="1216" y="352">a progetto</text><text x="1216" y="398">continuativa</text><text x="1216" y="444">a progetto</text>
    </g>
    <g stroke="rgba(10,10,10,.12)">
      <path d="M64 94 L1216 94"/><path d="M64 140 L1216 140"/><path d="M64 186 L1216 186"/>
      <path d="M64 232 L1216 232"/><path d="M64 278 L1216 278"/><path d="M64 324 L1216 324"/>
      <path d="M64 370 L1216 370"/><path d="M64 416 L1216 416"/>
    </g>
  </svg>

  <div class="z" style="top:614px"><div class="note">I servizi sono attivabili su Connect,
    Insight e Refyn. Che cosa è compreso nell’avvio e che cosa resta opzionale è indicato
    nella proposta economica.</div></div>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span><span>A2</span></div>
</div>''')

# =====================================================================
# A3 · PRICING · struttura, senza importi e senza stati interni
# =====================================================================
s = rid(V['a3_pricing'], 'a3_pricing')
add(rail(s, 'A3'))

# =====================================================================
# A4 · FAQ · risposte piu' brevi, rimando puntuale al dossier
# =====================================================================
s = rid(V['a4_faq'], 'a4_faq')
s = s.replace('''      <text x="560" y="106">Si parte da quello che c’è. Dove il dato manca o non è affidabile,</text>
      <text x="560" y="132">il progetto può prevedere contatori o sensori aggiuntivi.</text>''',
              '''      <text x="560" y="106">Si parte da quello che c’è. Dove il dato manca, il progetto può</text>
      <text x="560" y="132">prevedere contatori o sensori aggiuntivi. → Dossier 07</text>''')
s = s.replace('''      <text x="560" y="182">L’approccio è multi-vendor e la compatibilità viene verificata</text>
      <text x="560" y="208">durante l’audit tecnico, impianto per impianto.</text>''',
              '''      <text x="560" y="182">La compatibilità viene verificata sull’impianto reale, durante</text>
      <text x="560" y="208">l’audit tecnico. → Dossier · annesso A1</text>''')
s = s.replace('''      <text x="560" y="258">Nell’ambiente di deployment concordato con il vostro IT.</text>
      <text x="560" y="284">Modello, sicurezza e retention si chiudono nel solution design.</text>''',
              '''      <text x="560" y="258">Nell’ambiente di deployment concordato con il vostro IT.</text>
      <text x="560" y="284">Modello, sicurezza e retention: → Dossier 08 · annesso A3</text>''')
s = s.replace('''      <text x="560" y="334">È possibile un’integrazione con ERP o gestionale, previa</text>
      <text x="560" y="360">verifica tecnica del punto di innesto.</text>''',
              '''      <text x="560" y="334">È possibile un’integrazione con il gestionale, previa verifica</text>
      <text x="560" y="360">del punto di innesto. → Dossier 12</text>''')
s = s.replace('''      <text x="560" y="30">La lettura dei segnali non richiede scrittura verso le macchine.</text>
      <text x="560" y="56">Eventuali interventi si pianificano con la produzione.</text>''',
              '''      <text x="560" y="30">La lettura dei segnali non richiede scrittura verso le macchine.</text>
      <text x="560" y="56">Eventuali interventi si pianificano con la produzione. → Dossier 08</text>''')
s = s.replace('<text x="560" y="410">Il pilot chiude con risultati, gap e proposta di estensione.</text>',
              '<text x="560" y="410">Il pilot chiude con risultati, gap e proposta di estensione. → Dossier 13</text>')
add(rail(s, 'A4'))

# =====================================================================
# A5 · ASSUNZIONI DEL BUSINESS CASE · nuova
# =====================================================================
add('''<!-- ============= A5 · ASSUNZIONI DEL BUSINESS CASE ====================
     Esiste per liberare la slide 13: il numero grande non deve portarsi
     dietro sei righe di note. -->
<div class="slide lt" id="a5_assunzioni">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Le assunzioni dietro i numeri.</h2>
  </div>

  <svg data-ui="1" width="1280" height="440" viewBox="0 0 1280 440"
       style="position:absolute;left:0;top:150px" role="img" aria-labelledby="u5t u5d">
    <title id="u5t">Parametri e formule dello scenario illustrativo</title>
    <desc id="u5d">I nove parametri usati in tutto il deck, con la loro origine, e le due
      formule che li combinano.</desc>

    <g font-family="Geist" font-size="14" font-weight="500" fill="rgba(10,10,10,.56)">
      <text x="64" y="20">Parametro</text><text x="620" y="20">Valore</text><text x="1216" y="20" text-anchor="end">Origine</text>
    </g>
    <path d="M64 36 L1216 36" stroke="rgba(10,10,10,.26)"/>

    <g font-family="Geist" font-size="16" fill="#0A0A0A">
      <text x="64" y="70">Cadenza nominale</text><text x="64" y="104">Margine unitario</text>
      <text x="64" y="138">Margine al minuto</text><text x="64" y="172">Potenza in marcia</text>
      <text x="64" y="206">Potenza a impianto fermo</text><text x="64" y="240">Prezzo dell’energia</text>
      <text x="64" y="274">Fattore di emissione</text><text x="64" y="308">Settimane produttive</text>
      <text x="64" y="342">Durata del turno</text>
    </g>
    <g font-family="Geist" font-size="16" font-weight="600" fill="#0A0A0A">
      <text x="620" y="70">500 pz/min</text><text x="620" y="104">0,14 €/pz</text>
      <text x="620" y="138">70 €/min</text><text x="620" y="172">95 kW</text>
      <text x="620" y="206">38 kW</text><text x="620" y="240">0,22 €/kWh</text>
      <text x="620" y="274">0,35 kgCO₂e/kWh</text><text x="620" y="308">46</text>
      <text x="620" y="342">480 min</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)" text-anchor="end">
      <text x="1216" y="70">linea illustrativa</text><text x="1216" y="104">da confermare con il cliente</text>
      <text x="1216" y="138">500 × 0,14</text><text x="1216" y="172">linea illustrativa</text>
      <text x="1216" y="206">linea illustrativa</text><text x="1216" y="240">contratto di fornitura</text>
      <text x="1216" y="274">mix dichiarato dal fornitore</text><text x="1216" y="308">calendario illustrativo</text>
      <text x="1216" y="342">tre turni al giorno</text>
    </g>
    <g stroke="rgba(10,10,10,.12)">
      <path d="M64 86 L1216 86"/><path d="M64 120 L1216 120"/><path d="M64 154 L1216 154"/>
      <path d="M64 188 L1216 188"/><path d="M64 222 L1216 222"/><path d="M64 256 L1216 256"/>
      <path d="M64 290 L1216 290"/><path d="M64 324 L1216 324"/>
    </g>

    <path d="M64 366 L1216 366" stroke="rgba(10,10,10,.26)"/>
    <g font-family="Geist" font-size="17" fill="#0A0A0A">
      <text x="64" y="400">Perdita di un fermo &#61; durata × cadenza nominale × margine unitario</text>
      <text x="64" y="430">Perdita annua di una causa &#61; minuti a settimana × margine al minuto × settimane produttive</text>
    </g>
  </svg>

  <div class="z" style="top:614px"><div class="note">Tutti i valori sono illustrativi e servono
    a mostrare il metodo di calcolo. Nel progetto reale arrivano dai dati della linea e dal
    contratto di fornitura dell’energia.</div></div>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span><span>A5</span></div>
</div>''')


body = '<div class="doc">\n' + '\n\n\n'.join(out) + '\n\n</div>\n'
open('deck_body_v8.html', 'w', encoding='utf-8').write(body)
print(f'deck_body_v8.html · {len(out)} canvas · {len(body)//1024} KB')
