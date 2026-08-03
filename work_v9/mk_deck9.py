#!/usr/bin/env python3
"""Sales Deck V9 · working edition.

Parte dal corpo V8 e applica le sole modifiche della §6 del master:
  - 16 slide -> 13, unendo evento+prodotto e pilot+struttura economica;
  - servizi e struttura economica dettagliata scendono in appendice;
  - slide caso cliente, solo working, esclusa finche' non e' autorizzata;
  - placeholder dove il master li prescrive.
Il sistema visuale non si tocca.
"""
import re
import ph

V8 = 'deck_body_v8.html'


def slides(path):
    s = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<div class="slide[^>]*id="([^"]+)"[^>]*>', s):
        start = m.start()
        end = s.index('\n</div>', start) + len('\n</div>')
        out[m.group(1)] = s[start:end]
    return out


V = slides(V8)


def rail(html, page, note=None):
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
    return re.sub(r'(<div class="slide[^>]*id=")[^"]+(")', r'\g<1>' + new_id + r'\g<2>',
                  html, count=1)


def band(html, ids, low=False):
    """Banda degli input aperti, solo working edition."""
    for i in ids:
        assert i in ph.BY_ID, f'placeholder non dichiarato: {i}'
    toks = ' '.join('<span class="ph">{{%s}}</span>' % i for i in ids)
    cls = 'phb phb--low' if low else 'phb'
    b = (f'  <div class="{cls}" data-ed="working"><b>INPUT APERTI</b>'
         f'<span>{toks}</span></div>')
    return html.replace('\n</div>', '\n' + b + '\n</div>')


def ph_page(html):
    """Marca il canvas come escluso dalla client edition."""
    return html.replace('<div class="slide', '<div data-ph-page="P0" class="slide', 1)


out = []
add = out.append


# ===================================================================== 01
s = rid(V['s01_cover'], 'v01_cover')
add(band(s, ['PH_COMPANY_BRAND_FORM', 'PH_DATASET_VALIDATOR', 'PH_DATASET_VALIDATION_DATE'],
         low=True))

# ===================================================================== 02
add(rail(rid(V['s02_tensione'], 'v02_tensione'), '02 / 13'))

# ===================================================================== 03
s = rail(rid(V['s03_categoria'], 'v03_categoria'), '03 / 13',
         'Vista ricostruita · dati illustrativi')
s = s.replace('esempio del flusso Refyn, in sviluppo', 'esempio del flusso Refyn')
add(band(s, ['PH_REAL_SCREENSHOT_NEW_UI']))

# ===================================================================== 04
# evento + prodotto in un canvas solo: la vista della V8·05 rispondeva gia'
# a entrambe le domande, la V8·04 la anticipava con meno dettaglio.
s = rid(V['s05_prodotto'], 'v04_evento_prodotto')
s = s.replace('<div class="z" style="top:48px;width:1040px">\n    <h2 class="sm">Il fermo, la causa e il costo<br>nella stessa schermata.</h2>\n  </div>',
              '<div class="z" style="top:48px;width:1152px">\n    <h2 class="sm">Il fermo si vede. La causa e il costo devono<br>essere leggibili nello stesso momento.</h2>\n  </div>')
s = rail(s, '04 / 13', 'Vista ricostruita · dati illustrativi')
add(band(s, ['PH_REAL_SCREENSHOT_MAPST']))

# ===================================================================== 05
s = rail(rid(V['s06_energia'], 'v05_energia'), '05 / 13',
         'Vista ricostruita · dati illustrativi')
add(band(s, ['PH_REAL_SCREENSHOT_MARENERGY', 'PH_DATASET_STOPPED_POWER']))

# ===================================================================== 06
add(rail(rid(V['s07_priorita'], 'v06_priorita'), '06 / 13',
         'Vista ricostruita · dati illustrativi'))

# ===================================================================== 07
add(rail(rid(V['s08_ampiezza'], 'v07_ampiezza'), '07 / 13',
         'Viste ricostruite · dati illustrativi'))

# ===================================================================== 08
s = rid(V['s09_offerta'], 'v08_offerta')
# §13.2: una sola dichiarazione. Resta l'etichetta accanto a Refyn, dove il
# lettore la incontra guardando il livello; la ripetizione in piede esce.
s = s.replace('<div class="cp">Ogni livello comprende il precedente.\n    Refyn è in sviluppo.</div>',
              '<div class="cp">Ogni livello comprende il precedente e lavora sulla stessa base dati.</div>')
s = rail(s, '08 / 13', 'Vista ricostruita · dati illustrativi')
add(band(s, ['PH_SERVICES_INCLUDED', 'PH_SERVICES_OPTIONAL']))

# ===================================================================== 09
s = rid(V['s10_livelli'], 'v09_scelta')
s = s.replace('<text x="64" y="468" font-family="Geist" font-size="15" fill="rgba(10,10,10,.58)">Prezzi, inclusioni e durata contrattuale sono nell’appendice pricing.</text>',
              '<text x="64" y="468" font-family="Geist" font-size="15" fill="rgba(10,10,10,.58)" data-ed="working">Prezzi, inclusioni e durata contrattuale sono nell’appendice pricing.</text>'
              '<text x="64" y="468" font-family="Geist" font-size="15" fill="rgba(10,10,10,.58)" data-ed="client">Prezzi, inclusioni e durata contrattuale arrivano con la proposta economica.</text>')
s = rail(s, '09 / 13')
s = s.replace('<text x="964" y="34" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">in sviluppo</text>',
              '<text x="964" y="34" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">modulo avanzato</text>')
add(band(s, ['PH_AUDIT_DURATION', 'PH_CONTRACT_TERM', 'PH_REFYN_PRICING_MODEL']))

# ===================================================================== 10
s = rail(rid(V['s12_perche'], 'v10_perche'), '10 / 13')
add(band(s, ['PH_COMPANY_YEARS_EXPERIENCE', 'PH_PROJECTS_COMPLETED', 'PH_GROUP_RELATIONSHIP']))

# ===================================================================== 11
s = rail(rid(V['s13_valore'], 'v11_valore'), '11 / 13',
         'Scenario illustrativo · assunzioni in appendice A5')
add(band(s, ['PH_DATASET_THROUGHPUT', 'PH_DATASET_MARGIN_UNIT', 'PH_DATASET_STOP_MIN_WEEK',
             'PH_DATASET_RECOVERABLE_SHARE']))

# ===================================================================== 12
# pilot + struttura economica: la V8 le teneva su due canvas, il master le
# rimette insieme e manda il dettaglio in appendice.
s = rid(V['s15_pilot'], 'v12_pilot')
s = s.replace('width="1280" height="440" viewBox="0 0 1280 440"',
              'width="1280" height="480" viewBox="0 0 1280 480"')
s = s.replace('<path d="M0 439.25 L1280 439.25" stroke="rgba(10,10,10,.16)" stroke-width="1.5"/>',
              '<path d="M0 479.25 L1280 479.25" stroke="rgba(10,10,10,.16)" stroke-width="1.5"/>')
old = s[s.index('    <path d="M0 292 L1280 292"'):s.index('  </svg>')]
s = s.replace(old, '''    <path d="M0 288 L1280 288" stroke="rgba(10,10,10,.16)"/>
    <text x="64" y="318" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Criteri di uscita del pilot</text>
    <g font-family="Geist" font-size="16" fill="#0A0A0A">
      <text x="64" y="350">Dati completi</text><text x="352" y="350">Formule approvate</text>
      <text x="640" y="350">Cause validate</text><text x="928" y="350">Report condiviso</text>
    </g>
    <path d="M0 380 L1280 380" stroke="rgba(10,10,10,.16)"/>
    <text x="64" y="410" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Struttura economica</text>
    <g font-family="Geist" font-size="18" font-weight="600" fill="#0A0A0A">
      <text x="64" y="442">Avvio</text><text x="440" y="442">Canone</text><text x="816" y="442">Servizi</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="64" y="466">audit, setup e configurazione</text>
      <text x="440" y="466">per sito, per linea, per livello</text>
      <text x="816" y="466">review, formazione, supporto</text>
    </g>
''')
s = s.replace('perimetro e criteri concordati prima di partire',
              'perimetro, criteri e struttura economica')
s = s.replace('<text x="64" y="428" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Durata, partecipanti e condizioni economiche si fissano nella proposta di pilot.</text>', '')
s = rail(s, '12 / 13')
add(band(s, ['PH_AUDIT_PRICE', 'PH_PILOT_PRICE', 'PH_CONNECT_ANNUAL_FEE',
             'PH_INSIGHT_ANNUAL_FEE', 'PH_REFYN_PRICING_MODEL']))

# ===================================================================== 13
# CTA: senza contatto approvato non e' pubblicabile. Nella working edition
# porta il blocco contatti coi placeholder; nella client edition esce.
s = rid(V['s16_cta'], 'v13_cta')
s = s.replace('''    <text x="864" y="344" font-family="Geist" font-size="30" font-weight="600" fill="#FFFFFF">309.120 €</text>
    <text x="864" y="368" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">all’anno, da una sola causa</text>''',
'''    <text x="864" y="344" font-family="Geist" font-size="30" font-weight="600" fill="#FFFFFF">309.120 €</text>
    <text x="864" y="368" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">all’anno, da una sola causa</text>
    <g data-ed="working">
      <path d="M64 376 L736 376" stroke="rgba(255,255,255,.12)"/>
      <text x="64" y="404" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">Contatto</text>
      <g font-family="Geist Mono" font-size="14" fill="rgba(255,255,255,.82)">
        <text x="180" y="404">{{PH_CONTACT_NAME}}</text><text x="440" y="404">{{PH_CONTACT_ROLE}}</text>
        <text x="180" y="428">{{PH_CONTACT_EMAIL}}</text><text x="440" y="428">{{PH_CONTACT_PHONE}}</text>
      </g>
    </g>''')
s = s.replace('width="1280" height="440" viewBox="0 0 1280 440"',
              'width="1280" height="460" viewBox="0 0 1280 460"')
s = s.replace('style="position:absolute;left:0;top:240px"', 'style="position:absolute;left:0;top:224px"')
s = s.replace('<div class="z" style="top:182px;width:980px">', '<div class="z" style="top:152px;width:1040px">')
s = rail(s, '13 / 13', 'Scenario illustrativo · non risultato cliente')
s = band(s, ['PH_AUDIT_PARTICIPANTS', 'PH_AUDIT_INPUTS', 'PH_AUDIT_DELIVERABLES',
             'PH_CONTACT_NAME', 'PH_CONTACT_EMAIL'])
add(ph_page(s))

# ===================================================================== 14
# Caso cliente: esiste solo nella working edition. Ogni campo e' un
# placeholder, nessun valore e' stato inventato.
add(ph_page('''<!-- ============= 14 · CASO CLIENTE · SOLO WORKING =====================
     La slide esiste per far vedere che cosa serve, non per suggerire che
     esista già. Finché PH_CASE_APPROVAL_STATUS non e' APPROVED la client
     edition non la contiene. -->
<div class="slide lt" id="v14_caso">
  <div class="z" style="top:48px;width:1152px">
    <h2 class="sm">Da {{PH_CASE_INITIAL_PROBLEM}}<br>a {{PH_CASE_RESULT_1_LABEL}}.</h2>
  </div>

  <svg data-ui="1" width="1280" height="446" viewBox="0 0 1280 446"
       style="position:absolute;left:0;top:172px" role="img" aria-labelledby="c9t c9d">
    <title id="c9t">Struttura del caso cliente, da compilare</title>
    <desc id="c9d">Contesto, problema, intervento e risultati. Ogni campo è un
      segnaposto: nessun valore è stato inventato e la slide non entra nella
      versione destinata al cliente finché il caso non è autorizzato per iscritto.</desc>

    <rect x="0" y="0" width="1280" height="446" fill="#FFFFFF"/>
    <path d="M0 .75 L1280 .75" stroke="rgba(10,10,10,.16)" stroke-width="1.5"/>
    <path d="M0 445.25 L1280 445.25" stroke="rgba(10,10,10,.16)" stroke-width="1.5"/>
    <g stroke="rgba(10,10,10,.12)">
      <path d="M320 0 L320 300"/><path d="M640 0 L640 300"/><path d="M960 0 L960 300"/>
      <path d="M0 300 L1280 300"/>
    </g>

    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.42)">
      <text x="64" y="38">01</text><text x="352" y="38">02</text>
      <text x="672" y="38">03</text><text x="992" y="38">04</text>
    </g>
    <g font-family="Geist" font-size="18" font-weight="600" fill="#0A0A0A">
      <text x="98" y="38">Contesto</text><text x="386" y="38">Problema</text>
      <text x="706" y="38">Intervento</text><text x="1026" y="38">Risultati</text>
    </g>

    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.72)">
      <text x="64" y="86">{{PH_CASE_CLIENT_DISPLAY_NAME}}</text>
      <text x="64" y="116">{{PH_CASE_CLIENT_SECTOR}}</text>
      <text x="64" y="146">{{PH_CASE_LINE_TYPE}}</text>
      <text x="64" y="176">{{PH_CASE_CLIENT_SITE}}</text>

      <text x="352" y="86">{{PH_CASE_INITIAL_PROBLEM}}</text>
      <text x="352" y="116">{{PH_CASE_BASELINE_PERIOD}}</text>
      <text x="352" y="146">{{PH_CASE_BASELINE_DATA}}</text>
      <text x="352" y="176">{{PH_CASE_SCOPE}}</text>

      <text x="672" y="86">{{PH_CASE_SOLUTION_MODULE}}</text>
      <text x="672" y="116">{{PH_CASE_INTERVENTION}}</text>
      <text x="672" y="146">{{PH_CASE_PILOT_DURATION}}</text>
      <text x="672" y="176">{{PH_CASE_TIME_TO_USABLE_DATA}}</text>

      <text x="992" y="86">{{PH_CASE_RESULT_1_LABEL}}</text>
      <text x="992" y="116">{{PH_CASE_RESULT_1_BASELINE}}</text>
      <text x="992" y="146">{{PH_CASE_RESULT_1_AFTER}}</text>
      <text x="992" y="176">{{PH_CASE_RESULT_1_UNIT}}</text>
      <text x="992" y="206">{{PH_CASE_RESULT_2_LABEL}}</text>
      <text x="992" y="236">{{PH_CASE_RESULT_2_AFTER}}</text>
      <text x="992" y="266">{{PH_CASE_RESULT_3_LABEL}}</text>
    </g>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.50)">
      <text x="64" y="216">metodo di misura</text><text x="352" y="216">fonti del dato</text>
      <text x="672" y="216">sensori aggiunti</text>
    </g>
    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.72)">
      <text x="64" y="242">{{PH_CASE_RESULT_1_METHOD}}</text>
      <text x="352" y="242">{{PH_CASE_DATA_SOURCES}}</text>
      <text x="672" y="242">{{PH_CASE_ADDED_SENSORS}}</text>
    </g>

    <text x="64" y="336" font-family="Geist" font-size="13" fill="rgba(10,10,10,.50)">Citazione autorizzata</text>
    <text x="64" y="370" font-family="Geist Mono" font-size="15" fill="rgba(10,10,10,.72)">“{{PH_CASE_QUOTE}}”</text>
    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.60)">
      <text x="64" y="400">{{PH_CASE_QUOTE_AUTHOR}}</text><text x="360" y="400">{{PH_CASE_QUOTE_ROLE}}</text>
      <text x="660" y="400">{{PH_CASE_QUOTE_APPROVAL}}</text>
    </g>
    <text x="64" y="428" font-family="Geist" font-size="13" fill="rgba(10,10,10,.50)">Limiti dichiarati della misura: {{PH_CASE_CONFIDENCE_NOTE}}</text>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span>
    <span class="nt">Slide esclusa dalla client edition finché il caso non è autorizzato</span><span>14 / 13</span></div>
  <div class="phb" data-ed="working"><b>INPUT APERTI</b><span><span class="ph">{{PH_CASE_APPROVAL_STATUS}}</span> <span class="ph">{{PH_CASE_APPROVAL_OWNER}}</span> <span class="ph">{{PH_CASE_CONFIDENTIALITY}}</span> <span class="ph">{{PH_CASE_RESULT_PERIOD}}</span></span></div>
</div>'''))


# ===================================================================== A1
s = rid(V['a1_matrice'], 'a1_matrice')
s = s.replace('Refyn è il modulo avanzato in sviluppo. Il perimetro effettivo dipende dai dati',
              'Il perimetro effettivo dipende dai dati')
# max 8 righe: priorita' e verifica erano due righe della stessa capacita'
s = s.replace('<text x="64" y="340">Priorità e gestione azioni</text>\n      <text x="64" y="384">Verifica dei benefici</text>',
              '<text x="64" y="340">Priorità, azioni e verifica dei benefici</text>')
s = s.replace('''      <text x="836" y="340">Non incluso</text><text x="1000" y="340">Non incluso</text><text x="1164" y="340">Previsto</text>
      <text x="836" y="384">Non incluso</text><text x="1000" y="384">Non incluso</text><text x="1164" y="384">Previsto</text>''',
              '''      <text x="836" y="340">Non incluso</text><text x="1000" y="340">Non incluso</text><text x="1164" y="340">Previsto</text>''')
s = s.replace('<path d="M64 356 L1216 356"/>', '')
s = s.replace('<text x="64" y="428">Cliente ideale</text>', '<text x="64" y="384">Cliente ideale</text>')
s = s.replace('''      <text x="836" y="422">chi non ha ancora</text><text x="836" y="440">una baseline condivisa</text>
      <text x="1000" y="422">chi ha la baseline</text><text x="1000" y="440">e vuole capire le perdite</text>
      <text x="1164" y="422">chi vuole governare</text><text x="1164" y="440">le azioni e verificarle</text>''',
              '''      <text x="836" y="378">chi non ha ancora</text><text x="836" y="396">una baseline condivisa</text>
      <text x="1000" y="378">chi ha la baseline</text><text x="1000" y="396">e vuole capire le perdite</text>
      <text x="1164" y="378">chi vuole governare</text><text x="1164" y="396">le azioni e verificarle</text>''')
s = s.replace('<path d="M64 400 L1216 400" stroke="rgba(10,10,10,.26)"/>',
              '<path d="M64 356 L1216 356" stroke="rgba(10,10,10,.26)"/>')
s = s.replace('width="1280" height="470" viewBox="0 0 1280 436"', 'width="1280" height="440" viewBox="0 0 1280 408"')
s = rail(s, 'A1')
add(band(s, ['PH_SERVICES_INCLUDED', 'PH_REFYN_PRICING_MODEL']))

# ===================================================================== A2
# assorbe la slide «servizi a valore aggiunto» della V8: qui ogni servizio
# ha anche l'obiettivo, non solo l'output.
add(band('''<!-- ============ A2 · SERVIZI · OBIETTIVO, OUTPUT, QUANDO =============== -->
<div class="slide lt" id="a2_servizi">
  <div class="z" style="top:48px;width:1152px">
    <h2 class="sm">Il software rende visibile.<br>Le competenze accelerano il risultato.</h2>
  </div>

  <svg data-ui="1" width="1280" height="416" viewBox="0 0 1280 416"
       style="position:absolute;left:0;top:176px" role="img" aria-labelledby="g2t g2d">
    <title id="g2t">Nove servizi con obiettivo, output e frequenza</title>
    <desc id="g2d">Per ogni servizio l’obiettivo che persegue, il deliverable che
      produce e quando viene erogato.</desc>

    <g font-family="Geist" font-size="13" font-weight="500" fill="rgba(10,10,10,.56)">
      <text x="64" y="22">Servizio</text><text x="420" y="22">Obiettivo</text>
      <text x="800" y="22">Output</text><text x="1216" y="22" text-anchor="end">Quando</text>
    </g>
    <path d="M64 36 L1216 36" stroke="rgba(10,10,10,.26)"/>

    <g font-family="Geist" font-size="15" fill="#0A0A0A">
      <text x="64" y="68">Assessment e perimetrazione</text><text x="64" y="110">Setup e integrazione</text>
      <text x="64" y="152">Configurazione di KPI e formule</text><text x="64" y="194">Data quality review</text>
      <text x="64" y="236">Performance ed energy review</text><text x="64" y="278">Improvement sprint</text>
      <text x="64" y="320">Formazione</text><text x="64" y="362">Supporto</text>
      <text x="64" y="404">Estensione a nuove linee</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="420" y="68">sapere che dato c’è</text><text x="420" y="110">portare il dato a sistema</text>
      <text x="420" y="152">misurare le stesse cose</text><text x="420" y="194">fidarsi del dato</text>
      <text x="420" y="236">trovare dove si perde</text><text x="420" y="278">chiudere una causa</text>
      <text x="420" y="320">far usare lo strumento</text><text x="420" y="362">tenere il sistema in servizio</text>
      <text x="420" y="404">ripetere su altre linee</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="800" y="68">mappa dei dati e dei gap</text><text x="800" y="110">ambiente collegato</text>
      <text x="800" y="152">dizionario delle formule</text><text x="800" y="194">elenco delle anomalie</text>
      <text x="800" y="236">priorità e report del periodo</text><text x="800" y="278">azioni, baseline e verifica</text>
      <text x="800" y="320">referenti abilitati</text><text x="800" y="362">canale e tempi concordati</text>
      <text x="800" y="404">nuova linea attivata</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)" text-anchor="end">
      <text x="1216" y="68">avvio</text><text x="1216" y="110">avvio</text><text x="1216" y="152">avvio</text>
      <text x="1216" y="194">periodica</text><text x="1216" y="236">periodica</text><text x="1216" y="278">a progetto</text>
      <text x="1216" y="320">a progetto</text><text x="1216" y="362">continuativa</text><text x="1216" y="404">a progetto</text>
    </g>
    <g stroke="rgba(10,10,10,.12)">
      <path d="M64 84 L1216 84"/><path d="M64 126 L1216 126"/><path d="M64 168 L1216 168"/>
      <path d="M64 210 L1216 210"/><path d="M64 252 L1216 252"/><path d="M64 294 L1216 294"/>
      <path d="M64 336 L1216 336"/><path d="M64 378 L1216 378"/>
    </g>
  </svg>

  <div class="z" style="top:612px"><div class="note">I servizi sono attivabili su Connect,
    Insight e Refyn. Che cosa è compreso nell’avvio e che cosa resta opzionale è indicato nella
    proposta economica.</div></div>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span><span>A2</span></div>
</div>''', ['PH_SERVICES_INCLUDED', 'PH_SERVICES_OPTIONAL', 'PH_SUPPORT_HOURS']))

# ===================================================================== A3
# pricing: nella working edition ogni voce ha il suo placeholder, nella
# client edition la pagina non esiste finche' i valori non sono approvati.
add(ph_page('''<!-- ================= A3 · PRICING · SOLO WORKING ====================== -->
<div class="slide lt" id="a3_pricing">
  <div class="z" style="top:48px;width:1152px">
    <h2 class="sm">Avvio, canone, servizi.</h2>
  </div>

  <svg data-ui="1" width="1280" height="484" viewBox="0 0 1280 484"
       style="position:absolute;left:0;top:146px" role="img" aria-labelledby="r3t r3d">
    <title id="r3t">Le voci del modello economico</title>
    <desc id="r3d">Una tantum di avvio, canone ricorrente per sito, linea e livello,
      servizi opzionali, condizioni contrattuali. Ogni importo è un segnaposto: nessun
      prezzo è stato inventato.</desc>

    <g font-family="Geist" font-size="13" font-weight="500" fill="rgba(10,10,10,.56)">
      <text x="64" y="22">Voce</text><text x="560" y="22">Che cosa comprende</text>
      <text x="1216" y="22" text-anchor="end">Importo</text>
    </g>
    <path d="M64 36 L1216 36" stroke="rgba(10,10,10,.26)"/>

    <text x="64" y="70" font-family="Geist" font-size="13" fill="rgba(10,10,10,.50)">UNA TANTUM</text>
    <g font-family="Geist" font-size="16" fill="#0A0A0A">
      <text x="64" y="106">Audit e perimetrazione</text><text x="64" y="146">Setup della prima linea</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="560" y="106">mappa dei dati, gap, ipotesi economica</text>
      <text x="560" y="146">connettori, mapping, formule, utenti</text>
    </g>
    <g font-family="Geist Mono" font-size="14" fill="rgba(10,10,10,.72)" text-anchor="end">
      <text x="1216" y="106">{{PH_AUDIT_PRICE}}</text><text x="1216" y="146">{{PH_SETUP_FIRST_LINE}}</text>
    </g>
    <path d="M64 168 L1216 168" stroke="rgba(10,10,10,.12)"/>

    <text x="64" y="200" font-family="Geist" font-size="13" fill="rgba(10,10,10,.50)">RICORRENTE</text>
    <g font-family="Geist" font-size="16" fill="#0A0A0A">
      <text x="64" y="236">Canone base per sito</text><text x="64" y="276">Livello Connect</text>
      <text x="64" y="316">Livello Insight</text><text x="64" y="356">Linee successive</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="560" y="236">ambiente, utenti, supporto standard</text>
      <text x="560" y="276">stato, OEE, produzione, consumi, storico</text>
      <text x="560" y="316">cause, correlazioni, costo energetico, CO₂</text>
      <text x="560" y="356">ogni linea collegata dopo la prima</text>
    </g>
    <g font-family="Geist Mono" font-size="14" fill="rgba(10,10,10,.72)" text-anchor="end">
      <text x="1216" y="236">{{PH_SITE_BASE_FEE}}</text><text x="1216" y="276">{{PH_CONNECT_ANNUAL_FEE}}</text>
      <text x="1216" y="316">{{PH_INSIGHT_ANNUAL_FEE}}</text><text x="1216" y="356">{{PH_ADDITIONAL_LINE_FEE}}</text>
    </g>
    <path d="M64 378 L1216 378" stroke="rgba(10,10,10,.12)"/>

    <text x="64" y="410" font-family="Geist" font-size="13" fill="rgba(10,10,10,.50)">OPZIONALE E CONTRATTO</text>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="64" y="444">Refyn</text><text x="352" y="444">Supporto premium</text>
      <text x="640" y="444">Durata contrattuale</text><text x="928" y="444">Rinnovo</text>
    </g>
    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.72)">
      <text x="64" y="470">{{PH_REFYN_PRICING_MODEL}}</text><text x="352" y="470">{{PH_PREMIUM_SUPPORT_FEE}}</text>
      <text x="640" y="470">{{PH_CONTRACT_TERM}}</text><text x="928" y="470">{{PH_RENEWAL_TERMS}}</text>
    </g>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span>
    <span class="nt">Appendice esclusa dalla client edition finché gli importi non sono approvati</span><span>A3</span></div>
  <div class="phb" data-ed="working"><b>INPUT APERTI</b><span><span class="ph">{{PH_PRICE_VALIDITY}}</span> <span class="ph">{{PH_PAYMENT_TERMS}}</span> <span class="ph">{{PH_AUDIT_CREDIT_POLICY}}</span></span></div>
</div>'''))

# ===================================================================== A4
add(rail(rid(V['a4_faq'], 'a4_faq'), 'A4'))

# ===================================================================== A5
s = rid(V['a5_assunzioni'], 'a5_assunzioni')
s = s.replace('<text x="1216" y="20" text-anchor="end">Origine</text>',
              '<text x="1000" y="20">Origine</text><text x="1216" y="20" text-anchor="end">Stato</text>')
s = s.replace('<g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)" text-anchor="end">\n      <text x="1216" y="70">linea illustrativa</text>',
              '<g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">\n      <text x="1000" y="70">linea illustrativa</text>')
for y in (104, 138, 172, 206, 240, 274, 308, 342):
    s = re.sub(r'<text x="1216" y="%d">([^<]*)</text>' % y,
               r'<text x="1000" y="%d">\1</text>' % y, s)
s = s.replace('''    <path d="M64 366 L1216 366" stroke="rgba(10,10,10,.26)"/>''',
              '''    <g font-family="Geist Mono" font-size="13" fill="rgba(10,10,10,.60)" text-anchor="end">
      <text x="1216" y="70">OPEN</text><text x="1216" y="104">OPEN</text><text x="1216" y="138">OPEN</text>
      <text x="1216" y="172">OPEN</text><text x="1216" y="206">OPEN</text><text x="1216" y="240">OPEN</text>
      <text x="1216" y="274">OPEN</text><text x="1216" y="308">OPEN</text><text x="1216" y="342">OPEN</text>
    </g>
    <path d="M64 366 L1216 366" stroke="rgba(10,10,10,.26)"/>''')
s = rail(s, 'A5')
add(band(s, ['PH_DATASET_VALIDATOR', 'PH_DATASET_VALIDATION_DATE', 'PH_DATASET_ASSUMPTION_OWNER']))


body = '<div class="doc">\n' + '\n\n\n'.join(out) + '\n\n</div>\n'
open('deck9_body.html', 'w', encoding='utf-8').write(body)

used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', body))
undeclared = used - set(ph.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
ntok = len(re.findall(r'\{\{PH_', body))
print(f'deck9_body.html · {len(out)} canvas · {ntok} token · {len(used)} placeholder distinti')
