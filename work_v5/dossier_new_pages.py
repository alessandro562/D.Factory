#!/usr/bin/env python3
"""Le otto pagine nuove del dossier v5, piu' le due riscritte.

03 provenienza legacy · 06 capability matrix · 14 correlazione produzione-energia
15 opportunity prioritization · 16 action management e benefit tracking
17 OEE di linea avanzato · 18 roadmap controllata · 25 catalogo servizi
30 migrazione legacy · 02 architettura commerciale (riscritta)
"""

def band(sec, q, a='', extra='', slim=False):
    cls = 'band band--slim' if slim else 'band'
    ah = f'    <div class="band__a">{a}</div>\n' if a else ''
    return (f'  <div class="{cls}">\n    <div class="band__sec">{sec}</div>\n'
            f'    <div class="band__q">{q}</div>\n{ah}    <div class="spacer"></div>\n{extra}'
            f'    <div class="spacer"></div>\n    <div class="band__ft">'
            f'<span class="wm">d<i>.</i>factory</span><span class="pg">PG</span></div>\n  </div>\n')


def openb(label, items):
    return ('    <div class="open">\n      <div class="open__l">' + label +
            '</div>\n      <div class="open__i">' + items + '</div>\n    </div>\n')


PAGES = {}

# ---------------------------------------------------------------- 02
PAGES['d02_architettura_commerciale'] = '''<!-- ==== 02 · ARCHITETTURA COMMERCIALE — chiara ==== -->
<div class="slide lt" id="d02_architettura_commerciale" data-kind="dossier">
''' + band('Sezione A · prodotto', "Come è fatta l'offerta, e a che punto è.",
           'Tre livelli cumulativi, ognuno con produzione ed energia. I servizi sono un '
           'livello a parte.',
           openb('Da decidere', 'Perimetro di Connect e Insight<br>Primo rilascio di Refyn<br>'
                 'Entitlement dei servizi')) + '''
  <div class="field">
    <div class="field__hd"><span>Architettura commerciale</span><span>Brand · moduli · servizi · legacy</span></div>
    <div class="field__b" style="padding:26px 40px">
      <div class="mx" style="grid-template-columns:132px 1fr 186px">
        <div class="mx__h">Nome</div><div class="mx__h">Che cosa indica</div><div class="mx__h">Stato</div>
        <div style="font-size:19px">D.Factory</div>
        <div>Il brand. Copertina, chiusura, riferimenti societari. Non è un prefisso dei moduli.</div>
        <div><span class="st st--ok">Brand</span></div>
        <div style="font-size:19px">Connect</div>
        <div>Livello 1. Visibilità e baseline: stati, OEE di base, consumi, viste standard.</div>
        <div><span class="st st--opt">Pilot release</span></div>
        <div style="font-size:19px">Insight</div>
        <div>Livello 2, include Connect. Diagnosi: cause, costo, correlazione produzione–energia.</div>
        <div><span class="st st--opt">Pilot release</span></div>
        <div style="font-size:19px">Refyn</div>
        <div>Livello 3, include Connect e Insight. Priorità, azioni e verifica dei benefici.</div>
        <div><span class="st st--ver">In development</span></div>
        <div style="font-size:19px">Servizi</div>
        <div>Livello orizzontale, attivabile su tutti i moduli. Non è Refyn.</div>
        <div><span class="st st--pd">Da definire</span></div>
        <div style="font-size:19px">MAPST 4.0</div>
        <div>Prodotto legacy di produzione. Resta attivo per l'installato.</div>
        <div><span class="st st--ok">Proven legacy</span></div>
        <div style="font-size:19px">MarEnergy</div>
        <div>Prodotto legacy di energia. Resta attivo per l'installato.</div>
        <div><span class="st st--ok">Proven legacy</span></div>
      </div>
      <p class="bd" style="margin-top:16px;font-size:14px">Migrazione volontaria, nessuna
        dismissione prevista: pagina 30.</p>
    </div>
  </div>
</div>
'''

# ---------------------------------------------------------------- 03
PAGES['d03_provenienza'] = '''<!-- ==== 03 · PROVENIENZA DELLE CAPABILITY — chiara ==== -->
<div class="slide lt" id="d03_provenienza" data-kind="dossier">
''' + band('Sezione A · prodotto', 'Da dove vengono le funzioni che vedi.',
           'Quasi tutto ciò che è disponibile oggi nasce in MAPST 4.0 e MarEnergy, prodotti '
           'in esercizio su impianti reali. Il packaging è nuovo; molte capability no.',
           openb('Perché la distinzione conta',
                 'Una funzione può essere matura come capability e nuova come pacchetto. '
                 'Chi valuta il rischio tecnico guarda la prima, chi valuta il contratto '
                 'guarda la seconda.')) + '''
  <div class="field">
    <div class="field__hd"><span>Continuità legacy</span><span>Capability · packaging</span></div>
    <svg width="864" height="560" viewBox="0 0 864 560" style="margin:30px 40px"
         role="img" aria-labelledby="d3pt d3pd">
      <title id="d3pt">Provenienza delle capability dai prodotti legacy</title>
      <desc id="d3pd">Le capability di produzione arrivano da MAPST 4.0, quelle di energia da
        MarEnergy. Confluiscono nel nuovo packaging modulare, che aggiunge funzioni net-new
        ancora in sviluppo.</desc>

      <text x="0" y="14" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.3">PRODOTTI LEGACY · IN ESERCIZIO</text>
      <rect x="0" y="36" width="320" height="84" fill="none" stroke="#0A0A0A" stroke-width="1.6"/>
      <text x="22" y="70" font-family="Geist" font-size="20" fill="#0A0A0A">MAPST 4.0</text>
      <text x="22" y="98" font-family="Geist" font-size="15" fill="rgba(10,10,10,.64)">Produzione, stati, OEE, fermi</text>
      <rect x="0" y="146" width="320" height="84" fill="none" stroke="#0A0A0A" stroke-width="1.6"/>
      <text x="22" y="180" font-family="Geist" font-size="20" fill="#0A0A0A">MarEnergy</text>
      <text x="22" y="208" font-family="Geist" font-size="15" fill="rgba(10,10,10,.64)">Energia, utility, consumi</text>

      <g stroke="rgba(10,10,10,.42)" stroke-width="1.6" fill="none">
        <path d="M320 78 L470 120"/><path d="M320 188 L470 146"/>
      </g>
      <polygon points="476,122 466,117 466,127" fill="rgba(10,10,10,.42)"/>
      <polygon points="476,144 466,139 466,149" fill="rgba(10,10,10,.42)"/>

      <rect x="476" y="90" width="388" height="86" fill="#0A0A0A"/>
      <text x="498" y="126" font-family="Geist" font-size="20" fill="#fff">Connect · Insight</text>
      <text x="498" y="154" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">Packaging nuovo, capability provate</text>

      <text x="476" y="228" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.3">FUNZIONI NET-NEW</text>
      <rect x="476" y="250" width="388" height="72" fill="none" stroke="#0A0A0A" stroke-width="1.6" stroke-dasharray="5 4"/>
      <text x="498" y="284" font-family="Geist" font-size="20" fill="#0A0A0A">Refyn</text>
      <text x="498" y="308" font-family="Geist" font-size="15" fill="rgba(10,10,10,.64)">Priorità, azioni, benefici</text>
      <circle cx="838" cy="278" r="8" fill="#E6E011"/>

      <line x1="0" y1="380" x2="864" y2="380" stroke="rgba(10,10,10,.26)"/>
      <g font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.3">
        <text x="0" y="414">CAPABILITY</text><text x="300" y="414">PACKAGING</text><text x="620" y="414">COSA SIGNIFICA</text>
      </g>
      <g font-family="Geist" font-size="15" fill="#0A0A0A">
        <text x="0" y="446">Proven legacy</text><text x="300" y="446">Pilot release</text>
        <text x="620" y="446">Funziona già, confezionata da poco</text>
        <text x="0" y="478">Legacy estesa</text><text x="300" y="478">Project-dependent</text>
        <text x="620" y="478">Dipende da dati e impianto</text>
        <text x="0" y="510">Net-new</text><text x="300" y="510">In development</text>
        <text x="620" y="510">Non disponibile oggi</text>
      </g>
      <text x="0" y="552" font-family="Geist" font-size="14" fill="rgba(10,10,10,.64)">Il dettaglio funzione per funzione è alla pagina 06 e nella Module Feature Matrix.</text>
    </svg>
  </div>
</div>
'''

# ---------------------------------------------------------------- 06
PAGES['d06_capability'] = '''<!-- ==== 06 · CAPABILITY MATRIX — chiara ==== -->
<div class="slide lt" id="d06_capability" data-kind="dossier">
''' + band('Sezione A · prodotto', 'Chi contiene cosa, da dove viene, a che punto è.',
           'Due stati per riga. La <b>provenienza</b> dice se la capability esiste già nel '
           'legacy. Lo <b>stato</b> dice a che punto è nel nuovo packaging.',
           '''    <div class="open">
      <div class="open__l">Legenda</div>
      <div class="open__i" style="font-size:12.5px;line-height:1.75">
        <span class="st st--ok">Proven legacy</span><br>
        <span class="st st--opt">Pilot release</span><br>
        <span class="st st--pd">Project-dependent</span><br>
        <span class="st st--ver">In development</span><br>
        <span class="st st--road">Roadmap</span></div>
    </div>
''', slim=True) + '''
  <div class="field field--wide">
    <div class="field__hd"><span>Capability matrix · estratto</span><span>Completa: Module Feature Matrix v5</span></div>
    <div class="field__b" style="padding:22px 40px">
      <div class="mx mx--tight" style="grid-template-columns:1fr 68px 68px 68px 130px 168px;font-size:13.5px">
        <div class="mx__h">Funzione</div><div class="mx__h">Conn.</div><div class="mx__h">Insight</div>
        <div class="mx__h">Refyn</div><div class="mx__h">Provenienza</div><div class="mx__h">Stato</div>
        <div>Stato macchina e stato linea</div><div>✓</div><div>✓</div><div>✓</div>
        <div>MAPST 4.0</div><div><span class="st st--ok">Proven legacy</span></div>
        <div>Consumo per linea e per vettore</div><div>✓</div><div>✓</div><div>✓</div>
        <div>MarEnergy</div><div><span class="st st--ok">Proven legacy</span></div>
        <div>Pareto delle cause di fermo</div><div>—</div><div>✓</div><div>✓</div>
        <div>MAPST 4.0</div><div><span class="st st--opt">Pilot release</span></div>
        <div>Energia per stato macchina</div><div>Base</div><div>✓</div><div>✓</div>
        <div>Legacy + sviluppo</div><div><span class="st st--pd">Project-dependent</span></div>
        <div>Costo energetico per pezzo</div><div>—</div><div>✓</div><div>✓</div>
        <div>Legacy + sviluppo</div><div><span class="st st--pd">Project-dependent</span></div>
        <div>Ranking economico delle inefficienze</div><div>—</div><div>—</div><div>✓</div>
        <div>Net-new</div><div><span class="st st--ver">In development</span></div>
        <div>Benefit Tracking</div><div>—</div><div>—</div><div>✓</div>
        <div>Net-new</div><div><span class="st st--ver">In development</span></div>
        <div>Operational Performance Index</div><div>—</div><div>—</div><div>✓</div>
        <div>Net-new</div><div><span class="st st--road">Roadmap</span></div>
      </div>
      <p class="bd" style="margin-top:14px;font-size:13.5px">Una riga può essere
        <b>proven legacy</b> come capability e <b>pilot release</b> nel packaging: due maturità
        diverse, non si escludono.</p>
    </div>
  </div>
</div>
'''

# ---------------------------------------------------------------- 14
PAGES['d14_correlazione'] = '''<!-- ==== 14 · CORRELAZIONE PRODUZIONE-ENERGIA — scura ==== -->
<div class="slide dk" id="d14_correlazione" data-kind="dossier">
''' + band('Sezione B · funzioni', 'Che cosa nasce dal leggerle insieme.',
           'È la componente distintiva dell\'offerta: nessuna delle due letture, da sola, '
           'dice quanto costa un minuto di fermo.',
           openb('Prerequisito', 'La misura di energia deve essere associabile allo stato '
                 'macchina sullo stesso asse dei tempi. Dove non lo è, la correlazione non '
                 'si calcola.')) + '''
  <div class="field">
    <div class="field__hd"><span>Analisi congiunta</span><span>Insight · project-dependent</span></div>
    <div class="field__b" style="padding:26px 40px">
      <div class="mx" style="grid-template-columns:1fr 150px 168px">
        <div class="mx__h">Che cosa si ottiene</div><div class="mx__h">Modulo minimo</div><div class="mx__h">Stato</div>
        <div>Energia consumata durante i fermi</div><div>Insight</div>
        <div><span class="st st--pd">Project-dependent</span></div>
        <div>Energia per pezzo buono</div><div>Insight</div>
        <div><span class="st st--pd">Project-dependent</span></div>
        <div>Relazione fra stato macchina e consumo</div><div>Insight</div>
        <div><span class="st st--pd">Project-dependent</span></div>
        <div>Costo della riduzione di velocità</div><div>Insight</div>
        <div><span class="st st--ver">In development</span></div>
        <div>Costo combinato di capacità persa ed energia non produttiva</div><div>Insight</div>
        <div><span class="st st--ver">In development</span></div>
        <div>Ranking economico delle inefficienze</div><div>Refyn</div>
        <div><span class="st st--ver">In development</span></div>
      </div>
      <div class="hr" style="margin:22px 0 16px"></div>
      <p class="bd" style="font-size:15px">Il fermo delle 07:18 costa due volte: i pezzi non
        prodotti e l'energia assorbita mentre non si produce. Finché le due letture stanno in
        sistemi separati, la seconda metà del conto non viene fatta da nessuno.</p>
    </div>
  </div>
</div>
'''

# ---------------------------------------------------------------- 15
PAGES['d15_opportunity'] = '''<!-- ==== 15 · OPPORTUNITY PRIORITIZATION — scura ==== -->
<div class="slide dk" id="d15_opportunity" data-kind="dossier">
''' + band('Sezione C · Refyn', 'Come si decide da dove cominciare.',
           'Non esiste oggi. È il primo dei quattro oggetti previsti da Refyn e serve a '
           'ordinare le inefficienze per valore, non per rumore.',
           openb('Stato', 'In development. Non disponibile, non collaudato, non vendibile '
                 'come funzione presente.')) + '''
  <div class="field">
    <div class="field__hd"><span>Opportunity Prioritization</span><span>Refyn · in development</span></div>
    <svg width="864" height="556" viewBox="0 0 864 556" style="margin:30px 40px"
         role="img" aria-labelledby="d15t d15d">
      <title id="d15t">Criteri di ordinamento delle opportunità</title>
      <desc id="d15d">Ogni inefficienza rilevata viene pesata su nove criteri e restituita
        come elenco ordinato con motivazione, valore stimato e attendibilità del dato.</desc>

      <text x="0" y="14" font-family="Geist Mono" font-size="12" fill="rgba(255,255,255,.44)" letter-spacing="1.3">CRITERI DI PESATURA</text>
      <g font-family="Geist" font-size="16" fill="#fff">
        <text x="0" y="52">Capacità recuperabile</text><text x="300" y="52">Frequenza</text><text x="600" y="52">Affidabilità del dato</text>
        <text x="0" y="88">Energia evitabile</text><text x="300" y="88">Durata</text><text x="600" y="88">Effort indicativo</text>
        <text x="0" y="124">Costo economico</text><text x="300" y="124">Area coinvolta</text><text x="600" y="124">Impatto atteso</text>
      </g>
      <line x1="0" y1="164" x2="864" y2="164" stroke="rgba(255,255,255,.30)"/>

      <text x="0" y="200" font-family="Geist Mono" font-size="12" fill="rgba(255,255,255,.44)" letter-spacing="1.3">OUTPUT · ELENCO ORDINATO</text>
      <g>
        <rect x="0" y="222" width="640" height="30" fill="#E6E011"/>
        <rect x="0" y="268" width="470" height="30" fill="rgba(255,255,255,.62)"/>
        <rect x="0" y="314" width="352" height="30" fill="rgba(255,255,255,.46)"/>
        <rect x="0" y="360" width="228" height="30" fill="rgba(255,255,255,.32)"/>
      </g>
      <g font-family="Geist" font-size="15" fill="#0A0A0A">
        <text x="14" y="243">01 · Outfeed · fermi lunghi ricorrenti</text>
      </g>
      <g font-family="Geist" font-size="15" fill="#0A0A0A">
        <text x="14" y="289">02 · Consumo a macchina ferma, area filling</text>
        <text x="14" y="335">03 · Riduzione di velocità sul formato 1,0 L</text>
        <text x="14" y="381">04 · Micro-fermi al case packer</text>
      </g>
      <g font-family="Geist Mono" font-size="13" fill="rgba(255,255,255,.72)">
        <text x="664" y="243">alta</text><text x="500" y="289">alta</text>
        <text x="382" y="335">media</text><text x="258" y="381">media</text>
      </g>
      <text x="760" y="200" font-family="Geist Mono" font-size="12" fill="rgba(255,255,255,.44)" letter-spacing="1.3" text-anchor="end">ATTENDIBILITÀ</text>

      <line x1="0" y1="428" x2="864" y2="428" stroke="rgba(255,255,255,.14)"/>
      <text x="0" y="462" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">Ogni voce porta con sé la motivazione, il valore stimato, l'attendibilità del dato che la</text>
      <text x="0" y="486" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">sostiene e lo stato di avanzamento. Senza attendibilità dichiarata, una priorità è un'opinione.</text>
      <text x="0" y="534" font-family="Geist Mono" font-size="12" fill="#E6E011" letter-spacing="1.3">RAPPRESENTAZIONE DI CONCETTO · LA FUNZIONE NON È IMPLEMENTATA</text>
    </svg>
  </div>
</div>
'''

# ---------------------------------------------------------------- 16
PAGES['d16_action_benefit'] = '''<!-- ==== 16 · ACTION MANAGEMENT E BENEFIT TRACKING — scura ==== -->
<div class="slide dk" id="d16_action_benefit" data-kind="dossier">
''' + band('Sezione C · Refyn', "Dall'opportunità all'azione, e alla verifica.",
           "Due oggetti distinti: uno governa l'intervento, l'altro ne misura l'effetto. "
           'Senza il secondo, il miglioramento resta un\'affermazione.',
           openb('Stato', 'Entrambi in development. Il modello di calcolo del beneficio non '
                 'è ancora fissato.')) + '''
  <div class="field">
    <div class="field__hd"><span>Action Management · Benefit Tracking</span><span>Refyn · in development</span></div>
    <div class="field__b" style="padding:26px 40px">
      <div class="mx" style="grid-template-columns:1fr 1fr">
        <div class="mx__h">Action Management · campi previsti</div>
        <div class="mx__h">Benefit Tracking · misure previste</div>
        <div>Responsabile, data, linea o asset</div><div>Baseline del periodo precedente</div>
        <div>Baseline e target</div><div>Periodo di osservazione successivo</div>
        <div>Scadenza e stato</div><div>Variazione di OEE</div>
        <div>Evidenze e commenti</div><div>Capacità recuperata, energia evitata</div>
        <div>Risultato</div><div>Costo evitato e valore economico</div>
        <div>Beneficio annualizzato</div><div>Qualità del confronto</div>
      </div>
      <div class="hr" style="margin:20px 0 14px"></div>
      <p class="bd" style="font-size:14px">Il campo che decide la credibilità dell'intero
        oggetto è l'ultimo: senza una misura della qualità del confronto, un beneficio
        dichiarato non è distinguibile da una coincidenza stagionale.</p>
    </div>
  </div>
</div>
'''

# ---------------------------------------------------------------- 17
PAGES['d17_oee_avanzato'] = '''<!-- ==== 17 · OEE DI LINEA AVANZATO — chiara ==== -->
<div class="slide lt" id="d17_oee_avanzato" data-kind="dossier">
''' + band('Sezione C · Refyn', 'Perché macchina ferma non è linea ferma.',
           'Il polmone, o buffer, a valle continua ad alimentare la linea finché ha '
           'materiale. Se assorbe il fermo, la linea non si ferma e l\'OEE di linea non si '
           'sconta due volte.',
           openb('Stato', 'In development. Oggi la distinzione fra fermo macchina e fermo '
                 'linea non è modellata nel prodotto.')) + '''
  <div class="field">
    <div class="field__hd"><span>Logica buffer-aware</span><span>Refyn · in development</span></div>
    <svg width="864" height="556" viewBox="0 0 864 556" style="margin:30px 40px"
         role="img" aria-labelledby="d17t d17d">
      <title id="d17t">Il polmone assorbe il fermo macchina</title>
      <desc id="d17d">Con il polmone pieno il fermo della macchina non ferma la linea. Con il
        polmone svuotato lo stesso fermo diventa fermo di linea.</desc>

      <text x="0" y="14" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.4">CASO 1 · POLMONE PIENO</text>
      <rect x="0" y="36" width="182" height="62" fill="none" stroke="#0A0A0A" stroke-width="1.6"/>
      <text x="91" y="73" font-family="Geist" font-size="16" fill="#0A0A0A" text-anchor="middle">Macchina ferma</text>
      <path d="M182 67 L240 67" stroke="#0A0A0A" stroke-width="1.6"/>
      <rect x="240" y="36" width="156" height="62" fill="#0A0A0A"/>
      <text x="318" y="73" font-family="Geist" font-size="16" fill="#fff" text-anchor="middle">Polmone pieno</text>
      <path d="M396 67 L454 67" stroke="#0A0A0A" stroke-width="1.6"/>
      <polygon points="454,67 446,62 446,72" fill="#0A0A0A"/>
      <rect x="454" y="36" width="182" height="62" fill="none" stroke="#0A0A0A" stroke-width="1.6"/>
      <text x="545" y="73" font-family="Geist" font-size="16" fill="#0A0A0A" text-anchor="middle">La linea continua</text>

      <text x="0" y="162" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.4">CASO 2 · POLMONE SVUOTATO</text>
      <rect x="0" y="184" width="182" height="62" fill="none" stroke="#0A0A0A" stroke-width="1.6"/>
      <text x="91" y="221" font-family="Geist" font-size="16" fill="#0A0A0A" text-anchor="middle">Macchina ferma</text>
      <path d="M182 215 L240 215" stroke="#0A0A0A" stroke-width="1.6"/>
      <rect x="240" y="184" width="156" height="62" fill="none" stroke="rgba(10,10,10,.42)" stroke-width="1.6" stroke-dasharray="5 4"/>
      <text x="318" y="221" font-family="Geist" font-size="16" fill="rgba(10,10,10,.64)" text-anchor="middle">Polmone vuoto</text>
      <path d="M396 215 L454 215" stroke="#E6E011" stroke-width="2.6"/>
      <polygon points="454,215 446,210 446,220" fill="#E6E011"/>
      <rect x="454" y="184" width="182" height="62" fill="#E6E011"/>
      <text x="545" y="221" font-family="Geist" font-size="16" fill="#0A0A0A" text-anchor="middle">La linea si ferma</text>

      <text x="690" y="70" font-family="Geist" font-size="18" fill="#0A0A0A">La differenza</text>
      <text x="690" y="94" font-family="Geist" font-size="18" fill="#0A0A0A">fra i due OEE</text>
      <text x="690" y="118" font-family="Geist" font-size="18" fill="#0A0A0A">è la capacità</text>
      <text x="690" y="142" font-family="Geist" font-size="18" fill="#0A0A0A">del polmone.</text>

      <line x1="0" y1="300" x2="864" y2="300" stroke="rgba(10,10,10,.26)"/>
      <text x="0" y="334" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.4">FUNZIONI PREVISTE IN QUESTO OGGETTO</text>
      <g font-family="Geist" font-size="15" fill="#0A0A0A">
        <text x="0" y="368">Distinzione fermo macchina / fermo linea</text>
        <text x="440" y="368">Propagazione degli eventi a valle</text>
        <text x="0" y="398">Modellazione della capacità dei polmoni</text>
        <text x="440" y="398">Identificazione del collo di bottiglia</text>
        <text x="0" y="428">Confronto perdita locale / impatto finale</text>
        <text x="440" y="428">Line balancing</text>
      </g>
      <g font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.2">
        <text x="700" y="428">ROADMAP</text>
      </g>
      <line x1="0" y1="462" x2="864" y2="462" stroke="rgba(10,10,10,.12)"/>
      <rect x="0" y="486" width="470" height="28" fill="#E6E011"/>
      <text x="14" y="506" font-family="Geist Mono" font-size="12.5" fill="#0A0A0A" letter-spacing="1.2">IN DEVELOPMENT · NON DISPONIBILE OGGI</text>
      <text x="0" y="546" font-family="Geist" font-size="14" fill="rgba(10,10,10,.64)">La formula OEE si calibra comunque in audit sul modo di misurare del cliente.</text>
    </svg>
  </div>
</div>
'''

# ---------------------------------------------------------------- 18
PAGES['d18_roadmap'] = '''<!-- ==== 18 · ROADMAP CONTROLLATA — chiara ==== -->
<div class="slide lt" id="d18_roadmap" data-kind="dossier">
''' + band('Sezione C · Refyn', 'Cosa non facciamo, e non promettiamo.',
           'Un elenco di esclusioni è più utile di un elenco di intenzioni. Queste funzioni '
           'non esistono, non sono in sviluppo e non entrano in un contratto.',
           openb('Sulla diagnostica',
                 'La prima fase prevista usa regole, statistica, deviazioni e pattern. '
                 'Nessun modello di apprendimento.'), slim=True) + '''
  <div class="field field--wide">
    <div class="field__hd"><span>Roadmap controllata</span><span>Stato dichiarato per ciascuna voce</span></div>
    <div class="field__b" style="padding:24px 40px">
      <div class="mx mx--tight" style="grid-template-columns:1fr 1fr 176px">
        <div class="mx__h">Funzione</div><div class="mx__h">Condizione per valutarla</div><div class="mx__h">Stato</div>
        <div>Benchmarking interno fra linee, turni, siti</div>
        <div>Perimetro multi-sito consolidato</div><div><span class="st st--road">Roadmap</span></div>
        <div>Operational Performance Index</div>
        <div>Definizione delle componenti e verifica HR</div><div><span class="st st--road">Roadmap</span></div>
        <div>Line balancing</div><div>Modellazione dei polmoni completata</div>
        <div><span class="st st--road">Roadmap</span></div>
        <div>Manutenzione e qualità predittive</div><div>Nessuna</div>
        <div><span class="st st--no">Not offered</span></div>
        <div>Raccomandazioni automatiche, simulazioni, forecast</div><div>Nessuna</div>
        <div><span class="st st--no">Not offered</span></div>
        <div>Benchmark cross-client</div><div>Modello legale, privacy e anonimizzazione</div>
        <div><span class="st st--no">Not offered</span></div>
        <div>Intelligenza artificiale, assistente in linguaggio naturale</div><div>Nessuna</div>
        <div><span class="st st--no">Not offered</span></div>
        <div>Video e streaming da telecamere IP</div><div>Nessuna</div>
        <div><span class="st st--no">Not offered</span></div>
      </div>
      <p class="bd" style="margin-top:14px;font-size:13.5px">Se una di queste funzioni è
        determinante per il tuo progetto, va detto adesso e non in fase di collaudo.</p>
    </div>
  </div>
</div>
'''

# ---------------------------------------------------------------- 25
PAGES['d25_servizi'] = '''<!-- ==== 25 · CATALOGO SERVIZI — chiara ==== -->
<div class="slide lt" id="d25_servizi" data-kind="dossier">
''' + band('Sezione E · servizi', 'Cosa si può attivare, su qualsiasi modulo.',
           'I servizi sono un livello orizzontale. Non sono Refyn e non ne sono un sinonimo: '
           'si attivano su Connect, su Insight e su Refyn.',
           openb('Da definire', 'Che cosa è compreso nel canone di ciascun modulo. '
                 'Finché non è deciso, i servizi si presentano come attivabili, mai come '
                 'inclusi.'), slim=True) + '''
  <div class="field field--wide">
    <div class="field__hd"><span>Catalogo servizi</span><span>Deliverable · frequenza · modello</span></div>
    <div class="field__b" style="padding:22px 40px">
      <div class="mx mx--tight" style="grid-template-columns:210px 1fr 150px 116px;font-size:13.5px">
        <div class="mx__h">Servizio</div><div class="mx__h">Deliverable</div>
        <div class="mx__h">Frequenza</div><div class="mx__h">Modello</div>
        <div>Data Readiness Assessment</div><div>Mappa dati, gap, prerequisiti, perimetro</div>
        <div>Una tantum</div><div>Progetto</div>
        <div>Setup &amp; Integration</div><div>Connessioni, mapping, configurazione, validazione</div>
        <div>Una tantum</div><div>Progetto</div>
        <div>KPI &amp; Formula Design</div><div>KPI, formule, baseline, fattori</div>
        <div>Una tantum, rivedibile</div><div>Progetto</div>
        <div>Data Quality Review</div><div>Completezza, coerenza, anomalie di segnale</div>
        <div>Mensile o trimestrale</div><div>Recurring</div>
        <div>Performance Review</div><div>OEE, fermi, velocità, scarti, priorità</div>
        <div>Mensile o trimestrale</div><div>Recurring</div>
        <div>Energy Review</div><div>Consumi, fuori produzione, costo per pezzo</div>
        <div>Mensile o trimestrale</div><div>Recurring</div>
        <div>Improvement Sprint</div><div>Analisi, piano d'azione, verifica</div>
        <div>Periodico</div><div>Progetto</div>
        <div>Executive Report</div><div>Sintesi direzionale e priorità</div>
        <div>Mensile o trimestrale</div><div>Recurring</div>
      </div>
      <p class="bd" style="margin-top:12px;font-size:13px">Altri quattro servizi — Training
        &amp; Adoption, Premium Support, Scale-up, Legacy Migration — nel Services Catalogue v5.</p>
    </div>
  </div>
</div>
'''

# ---------------------------------------------------------------- 30
PAGES['d30_migrazione'] = '''<!-- ==== 30 · MIGRAZIONE LEGACY — chiara ==== -->
<div class="slide lt" id="d30_migrazione" data-kind="dossier">
''' + band('Sezione E · delivery', 'Chi ha già MAPST 4.0 o MarEnergy.',
           'Il legacy resta attivo e supportato. La migrazione è volontaria, si valuta per '
           'impianto e non ha una scadenza imposta.',
           openb('Da verificare per progetto',
                 'Preservazione dello storico<br>Mapping funzionale uno-a-uno<br>'
                 'Proposta economica del passaggio')) + '''
  <div class="field">
    <div class="field__hd"><span>Migrazione volontaria</span><span>Nessuna dismissione prevista</span></div>
    <div class="field__b" style="padding:26px 40px">
      <div class="mx" style="grid-template-columns:200px 1fr 168px">
        <div class="mx__h">Passo</div><div class="mx__h">Che cosa comporta</div><div class="mx__h">Stato</div>
        <div>Mantenimento del legacy</div>
        <div>MAPST 4.0 e MarEnergy restano in esercizio e supportati. Nessuna scadenza.</div>
        <div><span class="st st--ok">Garantito</span></div>
        <div>Assessment dell'installato</div>
        <div>Rilievo di macchine, tag, contatori e viste in uso oggi.</div>
        <div><span class="st st--opt">Servizio</span></div>
        <div>Mapping funzionale</div>
        <div>Corrispondenza fra le funzioni in uso e i moduli nuovi.</div>
        <div><span class="st st--pd">Per progetto</span></div>
        <div>Preservazione dello storico</div>
        <div>Trasferimento dei dati pregressi nel nuovo impianto di lettura.</div>
        <div><span class="st st--ver">Da verificare</span></div>
        <div>Proposta economica</div>
        <div>Condizioni del passaggio, senza aumento automatico sul legacy.</div>
        <div><span class="st st--pd">Da definire</span></div>
      </div>
      <div class="hr" style="margin:20px 0 14px"></div>
      <p class="bd" style="font-size:14px"><b>Quello che non facciamo:</b> nessuna dismissione
        forzata, nessuna scadenza imposta, nessun aumento automatico di canone per chi resta
        sul legacy.</p>
    </div>
  </div>
</div>
'''

if __name__ == '__main__':
    for k, v in PAGES.items():
        print(f'{k:32s} {len(v):6d} char')
