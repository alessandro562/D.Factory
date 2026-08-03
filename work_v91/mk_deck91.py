#!/usr/bin/env python3
"""Sales Deck V9.1 · delta sul corpo master V9.

Non ridisegna niente. Applica le modifiche puntuali del §9 del piano e le
conseguenze dei gate del §3:
  - la CTA torna nella client edition (§9.13) e non si esclude più;
  - i valori annualizzati escono finché G3 è aperto (§9.11, §5.3);
  - i claim tecnici usano le formulazioni approvate dal piano (§6);
  - il caso cliente è governato dal solo gate CASE_STUDY_READY (§3.2).
"""
import re
import gates
import ph91

s = open('deck9_master.html', encoding='utf-8').read()

G3_OK = gates.STATO['G3'] == 'APPROVED'
G2_OK = gates.STATO['G2'] == 'APPROVED'
CASE_OK = gates.CASE_STUDY_READY == 'APPROVED'


def sub(old, new, n=1):
    global s
    assert old in s, f'stringa non trovata: {old[:70]}'
    s = s.replace(old, new, n)


# =====================================================================
# §9.5 · slide 05 energia · la nota che dichiara di che cosa è quel numero
# =====================================================================
sub('<text x="987" y="442" font-family="Geist" font-size="15" fill="#FFFFFF"\n'
    '          text-anchor="middle">38 kW a linea ferma</text>',
    '<text x="987" y="442" font-family="Geist" font-size="15" fill="#FFFFFF"\n'
    '          text-anchor="middle">38 kW a linea ferma</text>\n'
    '    <text x="200" y="442" font-family="Geist" font-size="13" fill="rgba(255,255,255,.56)">Consumo improduttivo dello stesso evento.</text>')

# =====================================================================
# §4.3 · Refyn: pilot dedicato con quotazione sul perimetro, nessun listino
# =====================================================================
sub('<text x="864" y="362">Attivazione attraverso</text><text x="864" y="388">un progetto pilota</text>\n'
    '      <text x="864" y="414">dedicato.</text>',
    '<text x="864" y="362">Progetto pilota dedicato,</text><text x="864" y="388">con quotazione</text>\n'
    '      <text x="864" y="414">sul perimetro.</text>')

# =====================================================================
# §9.11 + §5.3 · slide 11 valore · con G3 aperto restano formula e periodo
#                osservato, escono i valori annualizzati
# =====================================================================
OLD11 = s[s.index('    <text x="64" y="34" font-family="Geist" font-size="26" fill="rgba(255,255,255,.74)">96 min'):
          s.index('    <g stroke="rgba(255,255,255,.16)"><path d="M64 310 L592 310"/>')]
NEW11 = '''    <g data-ed="client">
      <text x="64" y="34" font-family="Geist" font-size="26" fill="rgba(255,255,255,.74)">La formula, senza il risultato annualizzato</text>
      <text x="64" y="120" font-family="Geist" font-size="40" font-weight="600" fill="#FFFFFF">minuti di fermo × margine al minuto × settimane produttive</text>
      <text x="64" y="164" font-family="Geist" font-size="17" fill="rgba(255,255,255,.74)">Il risultato si calcola sul dato della vostra linea, durante l’audit.</text>
      <text x="64" y="208" font-family="Geist" font-size="17" fill="rgba(255,255,255,.74)">Nella settimana osservata la prima causa vale 96 minuti e 6.720 €.</text>
    </g>
    <g data-ed="working">
      <text x="64" y="34" font-family="Geist" font-size="26" fill="rgba(255,255,255,.74)">96 min a settimana &#160;×&#160; 70 € al minuto &#160;×&#160; 46 settimane</text>
      <text x="64" y="164" font-family="Geist" font-size="118" font-weight="600" fill="#E6E011"
            letter-spacing="-5">309.120<tspan font-size="38"> €</tspan></text>
      <text x="64" y="208" font-family="Geist" font-size="17" fill="rgba(255,255,255,.74)">il costo annuo di una sola causa non chiusa · pubblicabile solo con G3 approvato</text>
    </g>

    <path d="M64 254 L1216 254" stroke="rgba(255,255,255,.16)"/>
    <text x="64" y="290" font-family="Geist" font-size="13" fill="rgba(255,255,255,.48)"
          letter-spacing="1">LE DUE LEVE DEL VALORE</text>

    <g font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.44)">
      <text x="64" y="336">01</text><text x="672" y="336">02</text>
    </g>
    <g font-family="Geist" font-size="17" fill="rgba(255,255,255,.74)">
      <text x="104" y="336">Capacità recuperabile</text><text x="712" y="336">Energia evitabile</text>
    </g>
    <g font-family="Geist" font-size="40" font-weight="600" fill="#FFFFFF" data-ed="working">
      <text x="64" y="392">154.560 €</text><text x="672" y="392">810 €</text>
    </g>
    <g font-family="Geist" font-size="24" font-weight="600" fill="#FFFFFF" data-ed="client">
      <text x="64" y="386">la leva principale</text><text x="672" y="386">la lettura che la completa</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(255,255,255,.48)">
      <text x="64" y="424">se la causa si dimezza</text><text x="672" y="424">dai 16 kWh per turno a linea ferma</text>
    </g>
'''
s = s.replace(OLD11, NEW11)
# §5.4 · non pareggiare artificialmente le due leve
sub('<span class="nt">Scenario illustrativo · assunzioni in appendice A5</span><span>11 / 13</span>',
    '<span class="nt">In questo scenario il valore principale nasce dalla capacità recuperabile</span><span>11 / 13</span>')

# =====================================================================
# §9.12 · slide 12 pilot · i deliverable, accanto ai criteri di uscita
# =====================================================================
sub('<text x="64" y="410" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Struttura economica</text>',
    '<text x="64" y="410" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Struttura economica</text>\n'
    '    <text x="928" y="318" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)" text-anchor="end">Deliverable: mappa dati · baseline · priorità · proposta</text>')

# =====================================================================
# §9.13 · la CTA torna nella client edition e non si esclude più.
#   La V9 aveva il blocco contatto tagliato dal viewBox: l'SVG era alto 400 e
#   il contatto stava a y=428. Qui l'SVG e' rifatto per intero a 456, che e'
#   lo spazio reale fra il sottotitolo e il piede.
# =====================================================================
s = s.replace('<div data-ph-page="P0" class="slide dk" id="v13_cta">',
              '<div class="slide dk" id="v13_cta">')

CTA_OLD = s[s.index('  <svg data-ui="1" width="1280" height="400" viewBox="0 0 1280 400"'):
            s.index('  <div class="rail"><span class="wm">D<i>.</i>Factory</span>\n    <span class="nt">Scenario illustrativo · non risultato cliente</span><span>13 / 13</span></div>')]
CTA_NEW = """  <svg data-ui="1" width="1280" height="456" viewBox="0 0 1280 456"
       style="position:absolute;left:0;top:196px" role="img" aria-labelledby="z2t z2d">
    <title id="z2t">Che cosa serve al primo incontro e quanto vale la linea</title>
    <desc id="z2d">A sinistra chi coinvolgere, che cosa preparare, che cosa restituiamo e
      l\u2019azione richiesta. A destra la vista di turno della linea con il costo di fermo
      del periodo osservato.</desc>

    <rect x="0" y="0" width="1280" height="456" fill="#141414"/>
    <path d="M0 .75 L1280 .75" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>
    <text x="64" y="32" font-family="Geist" font-size="15" font-weight="600" fill="#FFFFFF">Il primo incontro</text>
    <text x="1216" y="32" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)"
          text-anchor="end">Linea 1 · potenziale</text>
    <path d="M0 48 L1280 48" stroke="rgba(255,255,255,.14)"/>
    <path d="M800 48 L800 456" stroke="rgba(255,255,255,.14)"/>

    <g font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">
      <text x="64" y="84">Chi coinvolgere</text><text x="64" y="164">Cosa preparare</text>
      <text x="64" y="268">Cosa restituiamo</text><text x="64" y="372">Azione richiesta</text>
    </g>
    <g font-family="Geist" font-size="16" fill="rgba(255,255,255,.82)">
      <text x="64" y="114">Produzione · manutenzione · energia · IT/OT</text>
      <text x="64" y="194">Schema linea · elenco PLC · contatori</text>
      <text x="64" y="220">Dati di produzione gi\u00e0 disponibili</text>
      <text x="64" y="298">Perimetro · gap · ipotesi pilot</text>
      <text x="64" y="324">Proposta economica</text>
    </g>
    <text x="64" y="402" font-family="Geist" font-size="18" font-weight="600" fill="#FFFFFF">Una sessione di perimetrazione sulla prima linea.</text>
    <g stroke="rgba(255,255,255,.12)">
      <path d="M64 136 L736 136"/><path d="M64 240 L736 240"/><path d="M64 344 L736 344"/>
    </g>

    <g data-ed="working">
      <path d="M64 416 L736 416" stroke="rgba(255,255,255,.12)"/>
      <text x="64" y="444" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">Contatto</text>
      <g font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.82)">
        <text x="180" y="444">{{PH_CONTACT_NAME}}</text><text x="400" y="444">{{PH_CONTACT_ROLE}}</text>
        <text x="580" y="444">{{PH_CONTACT_EMAIL}}</text>
      </g>
    </g>

    <g fill="rgba(255,255,255,.09)">
      <rect x="864" y="88" width="352" height="12"/><rect x="864" y="108" width="352" height="12"/>
      <rect x="864" y="128" width="352" height="12"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="864" y="88" width="53" height="12"/><rect x="921" y="88" width="176" height="12"/>
      <rect x="1110" y="88" width="106" height="12"/>
      <rect x="864" y="108" width="53" height="12"/><rect x="921" y="108" width="176" height="12"/>
      <rect x="1110" y="108" width="106" height="12"/>
      <rect x="864" y="128" width="53" height="12"/><rect x="921" y="128" width="176" height="12"/>
      <rect x="1110" y="128" width="106" height="12"/>
    </g>
    <rect x="1097" y="128" width="13" height="12" fill="#E6E011"/>
    <text x="864" y="164" font-family="Geist" font-size="12" fill="rgba(255,255,255,.44)">turno 06:00 \u2013 14:00</text>

    <text x="864" y="248" font-family="Geist" font-size="30" font-weight="600" fill="#FFFFFF">15.680 \u20ac</text>
    <text x="864" y="272" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">costo di fermo · periodo osservato di sette giorni</text>

    <g data-ed="working">
      <text x="864" y="344" font-family="Geist" font-size="30" font-weight="600" fill="#FFFFFF">309.120 \u20ac</text>
      <text x="864" y="368" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">all\u2019anno, da una sola causa · pubblicabile solo con G3 approvato</text>
    </g>
    <g data-ed="client">
      <text x="864" y="344" font-family="Geist" font-size="17" fill="rgba(255,255,255,.82)">Lo stesso conto, sulla vostra</text>
      <text x="864" y="368" font-family="Geist" font-size="17" fill="rgba(255,255,255,.82)">linea, nella sessione.</text>
    </g>
  </svg>

"""
s = s.replace(CTA_OLD, CTA_NEW)

# =====================================================================
# §3.2 · il caso cliente dipende da un gate solo
# =====================================================================
if not CASE_OK:
    s = s.replace('<div data-ph-page="P0" class="slide lt" id="v14_caso">',
                  '<div data-ph-page="CASE_STUDY_READY" class="slide lt" id="v14_caso">')
sub('<span class="ph">{{PH_CASE_APPROVAL_STATUS}}</span>',
    '<span class="ph">{{PH_CASE_STUDY_READY}}</span> <span class="ph">{{PH_CASE_APPROVAL_STATUS}}</span>')

# =====================================================================
# §9.16 · l'appendice pricing entra solo con G2 chiuso
# =====================================================================
if not G2_OK:
    s = s.replace('<div data-ph-page="P0" class="slide lt" id="a3_pricing">',
                  '<div data-ph-page="G2" class="slide lt" id="a3_pricing">')

# =====================================================================
# §9.17 · FAQ · i claim tecnici nelle formulazioni approvate dal §6
# =====================================================================
sub('''      <text x="560" y="30">La lettura dei segnali non richiede scrittura verso le macchine.</text>
      <text x="560" y="56">Eventuali interventi si pianificano con la produzione. → Dossier 08</text>''',
'''      <text x="560" y="30">La configurazione standard privilegia l’acquisizione in sola lettura.</text>
      <text x="560" y="56">Eventuali scambi ulteriori si definiscono nel solution design. → Dossier 08</text>''')
sub('''      <text x="560" y="258">Nell’ambiente di deployment concordato con il vostro IT.</text>
      <text x="560" y="284">Modello, sicurezza e retention: → Dossier 08 · annesso A3</text>''',
'''      <text x="560" y="258">Modello di deployment, residenza e trattamento dei dati vengono</text>
      <text x="560" y="284">concordati con l’IT nel solution design. → Dossier 08 · annesso A3</text>''')

open('deck91_body.html', 'w', encoding='utf-8').write(s)
used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', s))
undeclared = used - set(ph91.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
n = len(re.findall(r'<div[^>]*class="slide', s))
print(f'deck91_body.html · {n} canvas · {len(used)} placeholder distinti · '
      f'G2 {gates.STATO["G2"]} · G3 {gates.STATO["G3"]} · caso {gates.CASE_STUDY_READY}')
