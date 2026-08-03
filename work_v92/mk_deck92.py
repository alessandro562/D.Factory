#!/usr/bin/env python3
"""Sales Deck V9.2 · delta sul corpo master V9.1.

Ogni sostituzione corrisponde a una riga della tabella §4 di
DFactory_V9_2_Audit.md. Il design è congelato: qui si cambiano copy, un
contenuto di visual e due geometrie sbagliate, niente altro.
"""
import re
import gates
import ph91

s = open('deck91_master.html', encoding='utf-8').read()

# §21.3 · nota metodologica, testo del master
NOTA_213 = ('In questo scenario la leva principale è la capacità recuperabile. '
            'Il dato energetico completa la lettura e misura il consumo improduttivo '
            'dello stesso evento.')


def sub(old, new, n=1):
    global s
    assert s.count(old) >= n, 'stringa non trovata: %r' % old[:90]
    s = s.replace(old, new, n)


# =====================================================================
# S01 · §10 «aumentare leggermente il sottotitolo». Unica eccezione al
#       congelamento tipografico, e vale solo per la cover.
# =====================================================================
sub('<div class="z" style="top:226px;width:940px"><div class="sup">D.Factory unisce produzione,',
    '<div class="z" style="top:226px;width:940px"><div class="sup" style="font-size:21px">'
    'D.Factory unisce produzione,')

# =====================================================================
# S04 · headline del §10 S04, senza articoli
# =====================================================================
sub('<h2 class="sm">Il fermo si vede. La causa e il costo devono<br>essere leggibili nello stesso momento.</h2>',
    '<h2 class="sm">Il fermo si vede. Causa e costo devono<br>essere leggibili nello stesso momento.</h2>')

# =====================================================================
# S05 · sottotitolo e nota del §10 S05 · e la geometria del viewBox
#       (440 di viewport contro 480 di viewBox: il testo veniva rimpicciolito
#        del 9% e il grafico rientrava di 53 px per lato)
# =====================================================================
sub('<div class="cp">La linea si ferma, l’energia continua a scorrere.</div>',
    '<div class="cp">La linea si ferma. L’energia continua a scorrere.</div>')
sub('<svg data-ui="1" width="1280" height="440" viewBox="0 0 1280 480"\n'
    '       style="position:absolute;left:0;top:186px"',
    '<svg data-ui="1" width="1280" height="480" viewBox="0 0 1280 480"\n'
    '       style="position:absolute;left:0;top:156px"')
sub('>Consumo improduttivo dello stesso evento.</text>',
    '>Il dato energetico completa la lettura e quantifica il consumo improduttivo '
    'dello stesso evento.</text>')

# =====================================================================
# S06 · §7.2 · un costo stimato non si chiama «costo»
# =====================================================================
sub('<text x="1216" y="92" text-anchor="end">Costo</text>',
    '<text x="1216" y="92" text-anchor="end">Costo stimato</text>')

# =====================================================================
# S07 · §10 S07 · dei dieci contenuti obbligatori ne mancavano quattro:
#       produzione, utility, cause e scarti. Microcopy minimo, banda per banda.
# =====================================================================
sub('<text x="104" y="106">stato e fermi</text><text x="104" y="206">OEE e fattori</text>\n'
    '      <text x="104" y="306">energia e costo</text><text x="104" y="406">consumo specifico</text>',
    '<text x="104" y="106">stato, fermi e cause</text><text x="104" y="206">OEE, fattori e qualità</text>\n'
    '      <text x="104" y="306">produzione, energia e utility</text>'
    '<text x="104" y="406">consumo, costo ed emissioni</text>')

# banda 01 · la causa principale del turno
sub('<text x="1216" y="107" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"\n'
    '          text-anchor="end">3 fermi · 26 minuti</text>',
    '<text x="1216" y="97" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"\n'
    '          text-anchor="end">3 fermi · 26 minuti</text>\n'
    '    <text x="1216" y="121" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)"\n'
    '          text-anchor="end">prima causa · mancanza tappi</text>')

# banda 02 · qualità già c'era come fattore, mancavano gli scarti
sub('<text x="1216" y="207" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"\n'
    '          text-anchor="end">tre fattori dichiarati</text>',
    '<text x="1216" y="197" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"\n'
    '          text-anchor="end">tre fattori dichiarati</text>\n'
    '    <text x="1216" y="221" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)"\n'
    '          text-anchor="end">scarti 4,4% del prodotto del turno</text>')

# banda 03 · produzione e utility entrano; la barra lascia il posto a tre cifre
sub('<text x="300" y="300" font-family="Geist" font-size="28" font-weight="600" fill="#FFFFFF">735<tspan font-size="16"> kWh</tspan></text>\n'
    '    <text x="300" y="324" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">consumo del turno</text>\n'
    '    <rect x="500" y="288" width="460" height="14" fill="rgba(255,255,255,.82)"/>\n'
    '    <rect x="950" y="288" width="10" height="14" fill="rgba(255,255,255,.34)"/>\n'
    '    <text x="500" y="324" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">719 kWh in marcia · 16 kWh a impianto fermo</text>\n'
    '    <text x="1216" y="307" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"\n'
    '          text-anchor="end">162 € di energia</text>',
    '<g font-family="Geist" font-size="28" font-weight="600" fill="#FFFFFF">\n'
    '      <text x="300" y="296">227.000<tspan font-size="16"> pz</tspan></text>\n'
    '      <text x="560" y="296">735<tspan font-size="16"> kWh</tspan></text>\n'
    '      <text x="800" y="296">162<tspan font-size="16"> €</tspan></text>\n'
    '    </g>\n'
    '    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">\n'
    '      <text x="300" y="320">prodotti nel turno</text>\n'
    '      <text x="560" y="320">energia del turno</text>\n'
    '      <text x="800" y="320">costo dell’energia</text>\n'
    '    </g>\n'
    '    <text x="300" y="342" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">719 kWh in marcia · 16 kWh a impianto fermo · 454 minuti a 500 pz/min</text>\n'
    '    <text x="1216" y="297" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)"\n'
    '          text-anchor="end">utility sui punti di misura</text>\n'
    '    <text x="1216" y="321" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)"\n'
    '          text-anchor="end">disponibili sulla linea</text>')

# =====================================================================
# S08 · base comune del §10 S08 e stato Refyn per esteso.
#       «in sviluppo» resta l'unica occorrenza del deck: condizione di build 8.
# =====================================================================
sub('>Base comune a tutti i livelli · produzione, energia e storico</text>',
    '>Base comune · produzione · OEE · energia · utility · storico</text>')
sub('<text x="332" y="322" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)">in sviluppo</text>\n',
    '')
sub('<text x="64" y="364" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">priorità · azioni · baseline · beneficio</text>',
    '<text x="64" y="346" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)">modulo avanzato in sviluppo</text>\n'
    '    <text x="64" y="372" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">priorità · azioni · baseline · beneficio</text>')

# =====================================================================
# S09 · le tre formulazioni del §10 S09
# =====================================================================
sub('<text x="464" y="258">Cause, correlazioni,</text><text x="464" y="284">costi e priorit&agrave;.</text>',
    '<text x="464" y="258">Cause, correlazioni,</text><text x="464" y="284">costo e priorit&agrave;.</text>')
sub('<text x="864" y="258">Priorit&agrave;, owner,</text><text x="864" y="284">target e verifica.</text>',
    '<text x="864" y="258">Priorit&agrave;, responsabili,</text><text x="864" y="284">target e verifica.</text>')
sub('<text x="464" y="362">Attivazione sullo stesso</text><text x="464" y="388">impianto, con capacità</text>\n'
    '      <text x="464" y="414">analitiche aggiuntive.</text>',
    '<text x="464" y="362">Sul medesimo impianto,</text><text x="464" y="388">con capacità</text>\n'
    '      <text x="464" y="414">analitiche aggiuntive.</text>')
sub('<text x="864" y="362">Progetto pilota dedicato,</text><text x="864" y="388">con quotazione</text>\n'
    '      <text x="864" y="414">sul perimetro.</text>',
    '<text x="864" y="362">Progetto pilota dedicato</text><text x="864" y="388">con perimetro</text>\n'
    '      <text x="864" y="414">concordato.</text>')

# =====================================================================
# S11 · il difetto §3.1 dell'audit: la descrizione accessibile pubblicava
#       i tre valori annualizzati, scritti in lettere, anche nella client
#       edition. La desc diventa client-safe e i valori restano dove sono
#       già governati da G3, cioè nei gruppi data-ed="working".
# =====================================================================
sub('<desc id="x3d">Novantasei minuti a settimana per settanta euro al minuto per\n'
    '      quarantasei settimane fanno trecentonovemilacentoventi euro. Da lì le due leve:\n'
    '      centocinquantaquattromilacinquecentosessanta euro di capacità se la causa si dimezza,\n'
    '      ottocentodieci euro di energia evitabile. Scenario illustrativo.</desc>',
    '<desc id="x3d">Sopra, la formula: minuti di fermo per margine al minuto per settimane\n'
    '      produttive. Sotto, le due leve del valore: la capacità recuperabile, che è la leva\n'
    '      principale, e l’energia evitabile, che completa la lettura. Scenario\n'
    '      illustrativo.</desc>\n'
    '    <desc id="x3w" data-ed="working">Novantasei minuti a settimana per settanta euro al\n'
    '      minuto per quarantasei settimane fanno trecentonovemilacentoventi euro. Da lì le due\n'
    '      leve: centocinquantaquattromilacinquecentosessanta euro di capacità se la causa si\n'
    '      dimezza, ottocentodieci euro di energia evitabile.</desc>')
sub('role="img" aria-labelledby="x3t x3d">', 'role="img" aria-labelledby="x3t x3d x3w">')

# nota metodologica §21.3, dentro il canvas: il rail non la reggeva
sub('<svg data-ui="1" width="1280" height="440" viewBox="0 0 1280 440"\n'
    '       style="position:absolute;left:0;top:176px" role="img" aria-labelledby="x3t x3d x3w">',
    '<svg data-ui="1" width="1280" height="472" viewBox="0 0 1280 472"\n'
    '       style="position:absolute;left:0;top:176px" role="img" aria-labelledby="x3t x3d x3w">')
sub('<g stroke="rgba(255,255,255,.16)"><path d="M64 310 L592 310"/><path d="M672 310 L1200 310"/></g>\n'
    '  </svg>',
    '<g stroke="rgba(255,255,255,.16)"><path d="M64 310 L592 310"/><path d="M672 310 L1200 310"/></g>\n'
    '    <path d="M64 442 L1216 442" stroke="rgba(255,255,255,.16)"/>\n'
    '    <text x="64" y="464" font-family="Geist" font-size="13" fill="rgba(255,255,255,.62)">'
    '%s</text>\n'
    '  </svg>' % NOTA_213)
sub('<span class="nt">In questo scenario il valore principale nasce dalla capacità recuperabile</span>',
    '<span class="nt">Scenario illustrativo · non risultato cliente</span>')

# =====================================================================
# S12 · §10 S12 · il fallback quando il prezzo non è approvato
# =====================================================================
sub('<text x="928" y="318" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)" text-anchor="end">Deliverable: mappa dati · baseline · priorità · proposta</text>',
    '<text x="928" y="318" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)" text-anchor="end">Deliverable: mappa dati · baseline · priorità · proposta</text>\n'
    '    <text x="1216" y="410" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)"\n'
    '          text-anchor="end" data-ed="client">La proposta economica viene costruita sul perimetro validato.</text>\n'
    '    <text x="1216" y="410" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)"\n'
    '          text-anchor="end" data-ed="working">Importi nell’appendice pricing.</text>')

# =====================================================================
# S13 · CTA · headline unica del §6.8, copy e blocco «cosa preparare»
# =====================================================================
sub('<h2 class="sm">Partiamo dalla linea<br>con il maggiore costo nascosto.</h2>',
    '<h2 class="sm">Partiamo dalla prima linea<br>da capire.</h2>')
sub('<div class="sup">Condividiamo il perimetro\n'
    '    della prima linea e verifichiamo dati, integrazione e potenziale economico.</div>',
    '<div class="sup">Condividiamo il perimetro,\n'
    '    verifichiamo i dati disponibili e definiamo il passo successivo.</div>')
sub('<text x="64" y="220">Dati di produzione già disponibili</text>',
    '<text x="64" y="220">Dati di produzione · vincoli IT</text>')
# il blocco contatto mostrava tre token in fila: diventa una riga sola con i
# nomi dei campi, e l'etichetta dice una volta che cosa manca
sub('      <g font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.82)">\n'
    '        <text x="180" y="444">{{PH_CONTACT_NAME}}</text><text x="400" y="444">{{PH_CONTACT_ROLE}}</text>\n'
    '        <text x="580" y="444">{{PH_CONTACT_EMAIL}}</text>\n'
    '      </g>',
    '      <text x="180" y="444" font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.82)">'
    'nome · ruolo · email — {{PH_CONTACT_NAME}}</text>')
sub('<span class="ph">{{PH_AUDIT_DELIVERABLES}}</span> <span class="ph">{{PH_CONTACT_NAME}}</span>',
    '<span class="ph">{{PH_AUDIT_DELIVERABLES}}</span> <span class="ph">{{PH_CONTACT_NAME}}</span> '
    '<span class="ph">{{PH_CONTACT_ROLE}}</span>')

# =====================================================================
# A1 · §12 · «Base» non è fra i cinque valori ammessi. La riga che lo usava
#      mescolava due cose diverse: l'assegnazione della causa, che Connect fa,
#      e l'analisi delle cause, che è di Insight. Si separano.
# =====================================================================
sub('<text x="64" y="76">Stato macchina e linea</text>',
    '<text x="64" y="76">Stato di linea, con causa associata</text>')
sub('<text x="64" y="208">Cause, micro-fermate e velocità</text>',
    '<text x="64" y="208">Analisi delle cause, micro-fermate e velocità</text>')
sub('<text x="836" y="208">Base</text>', '<text x="836" y="208">Non incluso</text>')
# geometria: viewport 440 contro viewBox 408, contenuto centrato per caso
sub('<svg data-ui="1" width="1280" height="440" viewBox="0 0 1280 408"\n'
    '       style="position:absolute;left:0;top:120px"',
    '<svg data-ui="1" width="1280" height="408" viewBox="0 0 1280 408"\n'
    '       style="position:absolute;left:0;top:136px"')

# =====================================================================
# A2 · §12 · la tabella prende la colonna incluso/opzionale. Esce «Obiettivo»:
#      quattro colonne sono quelle che il master chiede, e cinque non stanno.
# =====================================================================
sub('<title id="g2t">Nove servizi con obiettivo, output e frequenza</title>\n'
    '    <desc id="g2d">Per ogni servizio l’obiettivo che persegue, il deliverable che\n'
    '      produce e quando viene erogato.</desc>',
    '<title id="g2t">Nove servizi con output, momento e regime</title>\n'
    '    <desc id="g2d">Per ogni servizio il deliverable che produce, quando viene erogato\n'
    '      e se è compreso nell’avvio o resta opzionale.</desc>')
sub('<text x="64" y="22">Servizio</text><text x="420" y="22">Obiettivo</text>\n'
    '      <text x="800" y="22">Output</text><text x="1216" y="22" text-anchor="end">Quando</text>',
    '<text x="64" y="22">Servizio</text><text x="440" y="22">Output</text>\n'
    '      <text x="820" y="22">Quando</text>'
    '<text x="1216" y="22" text-anchor="end">Incluso o opzionale</text>')
# via la colonna obiettivo
sub('<g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">\n'
    '      <text x="420" y="68">sapere che dato c’è</text><text x="420" y="110">portare il dato a sistema</text>\n'
    '      <text x="420" y="152">misurare le stesse cose</text><text x="420" y="194">fidarsi del dato</text>\n'
    '      <text x="420" y="236">trovare dove si perde</text><text x="420" y="278">chiudere una causa</text>\n'
    '      <text x="420" y="320">far usare lo strumento</text><text x="420" y="362">tenere il sistema in servizio</text>\n'
    '      <text x="420" y="404">ripetere su altre linee</text>\n'
    '    </g>\n', '')
# output si sposta a sinistra · sostituzione limitata al canvas A2, perche'
# «x=800 y=320» esiste anche nella banda 03 della slide 07
def sub_in(canvas, old, new, n=1):
    global s
    a = s.index('id="%s"' % canvas)
    b = s.index('\n</div>', a)
    seg = s[a:b]
    assert seg.count(old) >= n, 'stringa non trovata in %s: %r' % (canvas, old[:70])
    s = s[:a] + seg.replace(old, new, n) + s[b:]


for y in (68, 110, 152, 194, 236, 278, 320, 362, 404):
    sub_in('a2_servizi', '<text x="800" y="%d">' % y, '<text x="440" y="%d">' % y)
# «quando» diventa una colonna allineata a sinistra, e nasce la quarta colonna
sub('<g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)" text-anchor="end">\n'
    '      <text x="1216" y="68">avvio</text><text x="1216" y="110">avvio</text><text x="1216" y="152">avvio</text>\n'
    '      <text x="1216" y="194">periodica</text><text x="1216" y="236">periodica</text><text x="1216" y="278">a progetto</text>\n'
    '      <text x="1216" y="320">a progetto</text><text x="1216" y="362">continuativa</text><text x="1216" y="404">a progetto</text>\n'
    '    </g>',
    '<g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">\n'
    '      <text x="820" y="68">avvio</text><text x="820" y="110">avvio</text><text x="820" y="152">avvio</text>\n'
    '      <text x="820" y="194">periodica</text><text x="820" y="236">periodica</text><text x="820" y="278">a progetto</text>\n'
    '      <text x="820" y="320">a progetto</text><text x="820" y="362">continuativa</text><text x="820" y="404">a progetto</text>\n'
    '    </g>\n'
    '    <g font-family="Geist Mono" font-size="12.5" fill="rgba(10,10,10,.58)" text-anchor="end" data-ed="working">\n'
    + '\n'.join('      <text x="1216" y="%d">{{PH_SERVICES_INCLUDED}}</text>' % y
                for y in (68, 110, 152, 194, 236, 278, 320, 362, 404)) + '\n'
    '    </g>\n'
    '    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)" text-anchor="end" data-ed="client">\n'
    + '\n'.join('      <text x="1216" y="%d">in proposta</text>' % y
                for y in (68, 110, 152, 194, 236, 278, 320, 362, 404)) + '\n'
    '    </g>')

# =====================================================================
# A5 · §12 · presente soltanto se il business case è pubblicato, quindi
#      condizionata a G3. E l'origine del turno era in contraddizione con
#      gli 810 € (audit §3.2).
# =====================================================================
sub('<div class="slide lt" id="a5_assunzioni">',
    '<!-- §12 · A5 entra nella client edition solo con il business case pubblicato. -->\n'
    '<div data-ph-page="G3" class="slide lt" id="a5_assunzioni">')
sub('<svg data-ui="1" width="1280" height="440" viewBox="0 0 1280 440"\n'
    '       style="position:absolute;left:0;top:150px" role="img" aria-labelledby="u5t u5d">',
    '<svg data-ui="1" width="1280" height="480" viewBox="0 0 1280 480"\n'
    '       style="position:absolute;left:0;top:130px" role="img" aria-labelledby="u5t u5d">')
sub('<desc id="u5d">I nove parametri usati in tutto il deck, con la loro origine, e le due\n'
    '      formule che li combinano.</desc>',
    '<desc id="u5d">I dieci parametri usati in tutto il deck, con la loro origine, e le due\n'
    '      formule che li combinano.</desc>')
sub('<text x="64" y="342">Durata del turno</text>',
    '<text x="64" y="342">Durata del turno</text><text x="64" y="376">Turni all’anno</text>')
sub('<text x="620" y="342">480 min</text>',
    '<text x="620" y="342">480 min</text><text x="620" y="376">230</text>')
sub('<text x="1000" y="342">tre turni al giorno</text>',
    '<text x="1000" y="342">un turno al giorno</text>'
    '<text x="1000" y="376">46 settimane × 5 giorni</text>')
sub('<text x="1216" y="308">OPEN</text><text x="1216" y="342">OPEN</text>',
    '<text x="1216" y="308">OPEN</text><text x="1216" y="342">OPEN</text>'
    '<text x="1216" y="376">OPEN</text>')
sub('<path d="M64 290 L1216 290"/><path d="M64 324 L1216 324"/>',
    '<path d="M64 290 L1216 290"/><path d="M64 324 L1216 324"/><path d="M64 358 L1216 358"/>')
sub('<path d="M64 366 L1216 366" stroke="rgba(10,10,10,.26)"/>',
    '<path d="M64 400 L1216 400" stroke="rgba(10,10,10,.26)"/>')
sub('<text x="64" y="400">Perdita di un fermo', '<text x="64" y="434">Perdita di un fermo')
sub('<text x="64" y="430">Perdita annua di una causa', '<text x="64" y="464">Perdita annua di una causa')

open('deck92_master.html', 'w', encoding='utf-8').write(s)
used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', s))
undeclared = used - set(ph91.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
n = len(re.findall(r'<div[^>]*class="slide', s))
cond = re.findall(r'data-ph-page="([^"]+)"[^>]*id="([^"]+)"', s)
print(f'deck92_master.html · {n} canvas · {len(used)} placeholder distinti')
print('  condizionali: ' + ' · '.join(f'{i} ⟵ {g}' for g, i in cond))
