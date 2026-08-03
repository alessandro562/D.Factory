#!/usr/bin/env python3
"""Assembla il corpo del Dossier tecnico v8: 14 pagine core + 4 annessi.

I sei prototipi approvati entrano invariati (tranne le correzioni chieste in
Fase C). Le altre pagine usano la V7 come fonte di contenuto ma non come
vincolo di layout: qui i template sono quattro e si alternano.
"""
import re

PROTO = 'proto_dossier_body.html'


def slides(path):
    s = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<div class="slide[^>]*id="([^"]+)"[^>]*>', s):
        start = m.start()
        end = s.index('\n</div>', start) + len('\n</div>')
        out[m.group(1)] = s[start:end]
    return out


P = slides(PROTO)
SEC = ['Prodotto', 'Dati e architettura', 'Misure e analisi', 'Delivery e supporto']


def hd(active, page):
    """Header con la navigazione a quattro sezioni. active 0 = nessuna."""
    ON = ' class="on"'
    n = ''.join('<span%s><i>%d</i>%s</span>' % (ON if i + 1 == active else '', i + 1, t)
                for i, t in enumerate(SEC))
    return f'  <div class="hd">\n    <div class="nav">{n}</div>\n    <div class="pg">{page}</div>\n  </div>'


def ft(note):
    return f'  <div class="ft"><span class="wm">D<i>.</i>Factory</span><span>{note}</span></div>'


def band(active, page, say, h=190):
    return (f'  <div class="band" style="height:{h}px">\n'
            + hd(active, page).replace('  <div class="hd">', '    <div class="hd">')
                              .replace('    <div class="nav">', '      <div class="nav">')
                              .replace('    <div class="pg">', '      <div class="pg">')
                              .replace('\n  </div>', '\n    </div>')
            + f'\n    <div class="lbl" style="position:absolute;left:64px;top:100px">Sezione {active} · {SEC[active-1]}</div>\n'
            + f'    <div class="say" style="top:126px">{say}</div>\n  </div>')


def rid(html, new_id):
    return re.sub(r'(<div class="slide[^>]*id=")[^"]+(")', r'\g<1>' + new_id + r'\g<2>', html, count=1)


out = []
add = out.append


# =====================================================================
# 01 · COVER · template A
# =====================================================================
add(f'''<!-- ======================= 01 · COVER ================================ -->
<div class="slide dk" id="p01_cover" data-kind="dossier">
  <div class="z" style="position:absolute;left:64px;top:64px">
    <span class="wm" style="font-size:19px">D<i>.</i>Factory</span>
  </div>
  <div style="position:absolute;left:64px;top:146px;width:900px">
    <div style="font-size:46px;line-height:1.1;letter-spacing:-.03em;font-weight:600">Dossier
      tecnico</div>
    <div class="sub" style="margin-top:22px;max-width:760px">Acquisizione, supervisione e analisi
      integrata di produzione ed energia.</div>
  </div>

  <div style="position:absolute;left:64px;top:340px;width:520px">
    <div class="lbl">Le quattro sezioni</div>
    <div class="sp" style="margin-top:14px;line-height:1.9">
      1 · Prodotto — pagine 02–06<br>
      2 · Dati e architettura — pagine 07–09<br>
      3 · Misure e analisi — pagine 10–12<br>
      4 · Delivery e supporto — pagine 13–14</div>
  </div>
  <div style="position:absolute;left:672px;top:340px;width:544px">
    <div class="lbl">Destinatari</div>
    <div class="sp" style="margin-top:14px;line-height:1.9">Operations · Engineering · IT/OT<br>
      Manutenzione · Energia · Procurement tecnico</div>
    <div class="lbl" style="margin-top:30px">Annessi tecnici</div>
    <div class="sp" style="margin-top:14px;line-height:1.9">A1 verifica di compatibilità ·
      A2 dimensionamento<br>A3 sicurezza e governo del dato · A4 dizionario KPI</div>
  </div>

{ft('Le viste di prodotto sono ricostruzioni con dati illustrativi, dichiarate pagina per pagina')}
</div>''')


# =====================================================================
# 02 · OVERVIEW · prototipo approvato + correzioni Fase C
# =====================================================================
s = rid(P['q1_overview'], 'p02_overview')
s = s.replace('Un ambiente server dedicato', 'Un ambiente di deployment concordato con IT')
s = s.replace('<div class="sp">Sostituzione delle macchine esistenti<br>Riscrittura dei programmi PLC</div>',
              '<div class="sp">Non presuppone la sostituzione delle macchine. Eventuali adeguamenti '
              'ai segnali vengono verificati in audit.</div>')
add(s)


# =====================================================================
# 03 · I TRE LIVELLI · template C
# =====================================================================
add(f'''<!-- ============= 03 · TRE LIVELLI SULLA STESSA BASE ================== -->
<div class="slide lt" id="p03_livelli" data-kind="dossier">
{hd(1, '03 / 14')}

  <div class="tt tt--sm">Connect, Insight e Refyn sulla stessa base dati.
    <div class="sub" style="margin-top:14px">Tre gradi di valore estratti da una sola
      acquisizione, non tre prodotti separati.</div>
  </div>

  <svg class="diag" style="top:206px" width="800" height="384" viewBox="0 0 800 384"
       role="img" aria-labelledby="b3t b3d">
    <title id="b3t">I tre livelli e la base dati comune</title>
    <desc id="b3d">Connect, Insight e Refyn si appoggiano alla stessa base di produzione,
      energia e storico. Ogni livello comprende il precedente.</desc>

    <path d="M88 40 L88 330" stroke="rgba(10,10,10,.30)" fill="none"/>
    <g stroke="rgba(10,10,10,.30)" fill="none">
      <path d="M88 46 L112 46"/><path d="M88 138 L112 138"/><path d="M88 230 L112 230"/>
      <path d="M88 330 L112 330"/>
    </g>

    <g fill="#F3F4F0">
      <rect x="112" y="8" width="678" height="76"/><rect x="112" y="100" width="678" height="76"/>
      <rect x="112" y="192" width="678" height="76"/>
    </g>
    <g font-family="Geist" font-size="20" font-weight="600" fill="#0A0A0A">
      <text x="136" y="42">Connect</text><text x="136" y="134">+ Insight</text><text x="136" y="226">+ Refyn</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">
      <text x="136" y="66">stato, OEE, produzione, consumi, storico</text>
      <text x="136" y="158">cause, correlazioni, energia per stato, costo e CO₂</text>
      <text x="136" y="250">priorità, azioni, verifica dei benefici</text>
    </g>
    <text x="766" y="226" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)"
          text-anchor="end">in sviluppo</text>

    <rect x="112" y="300" width="678" height="60" fill="#E9EAE5"/>
    <text x="136" y="326" font-family="Geist" font-size="16" font-weight="600" fill="#0A0A0A">Base dati operativa</text>
    <text x="136" y="348" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">una sola acquisizione: produzione, energia, storico</text>
  </svg>

  <div class="spec" style="top:206px">
    <div class="lbl" style="margin-bottom:6px">Che cosa aggiunge ogni livello</div>
    <div class="row"><b>Connect</b><span>vede e misura</span></div>
    <div class="row"><b>Insight</b><span>spiega e quantifica</span></div>
    <div class="row"><b>Refyn</b><span>guida e verifica</span></div>
    <div class="lbl" style="margin:26px 0 12px">Servizi specialistici</div>
    <div class="sp">Attivabili su tutti e tre i livelli: assessment, configurazione dei KPI,
      review, formazione e scale-up.</div>
    <div class="note" style="margin-top:22px">Ogni livello comprende il precedente e lavora
      sugli stessi dati. Il perimetro effettivo dipende dai segnali disponibili.</div>
  </div>

{ft('Schema dei livelli · perimetro da confermare in audit')}
</div>''')


# =====================================================================
# 04 · CONNECT · prototipo approvato
# =====================================================================
add(rid(P['q2_connect'], 'p04_connect'))


# =====================================================================
# 05 · INSIGHT · template B
# =====================================================================
add(f'''<!-- ==================== 05 · INSIGHT ================================= -->
<div class="slide lt" id="p05_insight" data-kind="dossier">
{hd(1, '05 / 14')}

  <div class="tt tt--sm">Insight spiega dove si perde capacità e valore.
    <div class="sub" style="margin-top:14px">Le cause ordinate per impatto economico, non per
      frequenza.</div>
  </div>

  <svg class="hero" data-ui="1" style="top:206px" width="880" height="340" viewBox="0 0 880 340"
       role="img" aria-labelledby="b5t b5d">
    <title id="b5t">Ranking delle cause di fermo, vista ricostruita</title>
    <desc id="b5d">Su sette giorni la mancanza tappi vale quattordici eventi, novantasei
      minuti e seimilasettecentoventi euro: il quarantatré per cento del costo di fermo della
      linea. Dati illustrativi.</desc>

    <rect x="0" y="0" width="880" height="340" fill="#FFFFFF"/>
    <rect x="0" y="0" width="880" height="44" fill="#F3F4F0"/>
    <path d="M0 .75 L880 .75" stroke="rgba(10,10,10,.16)" stroke-width="1.5"/>
    <path d="M0 339.25 L880 339.25" stroke="rgba(10,10,10,.16)" stroke-width="1.5"/>
    <text x="64" y="28" font-family="Geist" font-size="14" font-weight="600" fill="#0A0A0A">Cause di fermo · Linea 1 · ultimi 7 giorni</text>
    <text x="816" y="28" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)"
          text-anchor="end">ordinate per costo</text>
    <path d="M0 44 L880 44" stroke="rgba(10,10,10,.16)"/>

    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)">
      <text x="64" y="76">Causa</text><text x="430" y="76" text-anchor="end">Eventi</text>
      <text x="530" y="76" text-anchor="end">Durata</text><text x="816" y="76" text-anchor="end">Costo</text>
    </g>
    <path d="M64 90 L816 90" stroke="rgba(10,10,10,.26)"/>

    <rect x="64" y="114" width="11" height="11" fill="#E6E011"/>
    <g font-family="Geist" font-size="15" fill="#0A0A0A">
      <text x="88" y="124">Mancanza tappi</text><text x="88" y="168">Cambio formato</text>
      <text x="88" y="212">Micro-fermate</text><text x="88" y="256">Manutenzione</text>
    </g>
    <rect x="560" y="112" width="200" height="14" fill="#E6E011"/>
    <g fill="#0A0A0A">
      <rect x="560" y="156" width="129" height="14"/><rect x="560" y="200" width="85" height="14"/>
      <rect x="560" y="244" width="52" height="14"/>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.74)" text-anchor="end">
      <text x="430" y="124">14</text><text x="530" y="124">96 min</text>
      <text x="430" y="168">4</text><text x="530" y="168">62 min</text>
      <text x="430" y="212">38</text><text x="530" y="212">41 min</text>
      <text x="430" y="256">2</text><text x="530" y="256">25 min</text>
    </g>
    <g font-family="Geist" font-size="15" font-weight="600" fill="#0A0A0A" text-anchor="end">
      <text x="816" y="124">6.720 €</text><text x="816" y="168">4.340 €</text>
      <text x="816" y="212">2.870 €</text><text x="816" y="256">1.750 €</text>
    </g>
    <g stroke="rgba(10,10,10,.12)">
      <path d="M64 142 L816 142"/><path d="M64 186 L816 186"/><path d="M64 230 L816 230"/>
    </g>
    <path d="M64 274 L816 274" stroke="rgba(10,10,10,.26)"/>
    <text x="64" y="306" font-family="Geist" font-size="14" fill="rgba(10,10,10,.74)">Il 43% del costo viene da una causa sola</text>
    <text x="816" y="308" font-family="Geist" font-size="20" font-weight="600" fill="#0A0A0A"
          text-anchor="end">15.680 €</text>
  </svg>

  <div class="aside" style="top:206px">
    <div class="blk">
      <div class="lbl">Che cosa aggiunge</div>
      <div class="sp">Cause associate e validate<br>Correlazione con l’energia<br>Costo
        energetico per pezzo e CO₂<br>Confronti fra turni e formati</div>
    </div>
    <div class="hr" style="margin-bottom:18px"></div>
    <div class="blk">
      <div class="lbl">Come ordina</div>
      <div class="sp">Per impatto economico: quattordici fermi brevi possono pesare più di un
        fermo lungo.</div>
    </div>
    <div class="note">La causa è associata all’evento e validata da chi la conosce.</div>
  </div>

{ft('Vista ricostruita · dati illustrativi')}
</div>''')


# =====================================================================
# 06 · REFYN · template C
# =====================================================================
add(f'''<!-- ===================== 06 · REFYN ================================== -->
<div class="slide lt" id="p06_refyn" data-kind="dossier">
{hd(1, '06 / 14')}

  <div class="tt tt--sm">Un ciclo che si chiude: priorità, azioni, verifica.
    <div class="sub" style="margin-top:14px">I risultati aggiornano le priorità del ciclo
      successivo.</div>
  </div>

  <svg class="diag" style="top:210px" width="800" height="360" viewBox="0 0 800 360"
       role="img" aria-labelledby="b6t b6d">
    <title id="b6t">Il ciclo operativo di Refyn</title>
    <desc id="b6d">Le priorità generano azioni, le azioni vengono verificate contro la
      baseline e i risultati aggiornano le priorità del ciclo successivo. Rappresentazione
      del funzionamento previsto.</desc>

    <path d="M632 62 L632 20 L164 20 L164 56" fill="none" stroke="#0A0A0A" stroke-width="1.8"/>
    <polygon points="164,62 158,52 170,52" fill="#0A0A0A"/>

    <g fill="none" stroke="#0A0A0A" stroke-width="1.5">
      <rect x="64" y="62" width="200" height="68"/><rect x="298" y="62" width="200" height="68"/>
      <rect x="532" y="62" width="200" height="68"/>
    </g>
    <g font-family="Geist" font-size="20" font-weight="600" fill="#0A0A0A" text-anchor="middle">
      <text x="164" y="103">Priorità</text><text x="398" y="103">Azioni</text><text x="632" y="103">Verifica</text>
    </g>
    <g stroke="#0A0A0A" stroke-width="1.5">
      <path d="M264 96 L286 96"/><path d="M498 96 L520 96"/>
    </g>
    <g fill="#0A0A0A">
      <polygon points="292,96 282,90 282,102"/><polygon points="526,96 516,90 516,102"/>
    </g>

    <g stroke="rgba(10,10,10,.13)">
      <path d="M64 158 L264 158"/><path d="M298 158 L498 158"/><path d="M532 158 L732 158"/>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.78)">
      <text x="64" y="188">Impatto potenziale</text><text x="64" y="214">Energia evitabile</text>
      <text x="64" y="240">Impatto economico</text>
      <text x="298" y="188">Responsabile e ambito</text><text x="298" y="214">Baseline e target</text>
      <text x="298" y="240">Scadenza e stato</text>
      <text x="532" y="188">Beneficio verificato</text><text x="532" y="214">Confronto con la baseline</text>
      <text x="532" y="240">Periodo di osservazione</text>
    </g>

    <path d="M64 296 L790 296" stroke="rgba(10,10,10,.13)"/>
    <text x="64" y="326" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">Se il beneficio non è confermato, l’azione viene riesaminata con una baseline aggiornata.</text>
  </svg>

  <div class="spec" style="top:206px">
    <div class="dev">Modulo avanzato in sviluppo</div>
    <div class="lbl" style="margin:26px 0 6px">Che cosa porta con sé un’azione</div>
    <div class="row"><b>Responsabile</b><span>e ambito</span></div>
    <div class="row"><b>Baseline</b><span>e target</span></div>
    <div class="row"><b>Scadenza</b><span>e stato</span></div>
    <div class="row"><b>Beneficio</b><span>verificato o no</span></div>
    <div class="note" style="margin-top:22px">La verifica confronta il periodo osservato con
      la baseline dichiarata all’apertura dell’azione: senza baseline non c’è beneficio
      dimostrabile.</div>
  </div>

{ft('Rappresentazione del funzionamento previsto')}
</div>''')


# =====================================================================
# 07 · SORGENTI · template D + apertura sezione 2
# =====================================================================
add(f'''<!-- ============ 07 · SORGENTI E PUNTI DI MISURA ======================= -->
<div class="slide lt" id="p07_sorgenti" data-kind="dossier">
{band(2, '07 / 14', 'Il dato che non esiste non si analizza: si misura.')}

  <div class="tt tt--sm" style="top:222px">Da dove leggiamo, e dove il dato va aggiunto.</div>

  <div class="tb full" style="top:290px;grid-template-columns:280px 210px 210px 240px 212px">
    <div class="tb__h">Punto di misura</div><div class="tb__h">PLC e stati</div>
    <div class="tb__h">Conta pezzi</div><div class="tb__h">Contatore energia</div>
    <div class="tb__h">Che cosa manca</div>

    <div><b>Riempitrice</b></div><div>già presente</div><div>già presente</div>
    <div>da verificare</div><div>affidabilità del contatore</div>

    <div><b>Etichettatrice</b></div><div>già presente</div><div>da verificare</div>
    <div>da aggiungere</div><div>misura dedicata</div>

    <div><b>Tappatrice</b></div><div>già presente</div><div>già presente</div>
    <div>da aggiungere</div><div>misura dedicata</div>

    <div><b>Quadro di linea</b></div><div>—</div><div>—</div>
    <div>già presente</div><div>—</div>
  </div>

  <div class="box full" style="top:552px">
    <div class="lbl" style="margin-bottom:8px">Quando serve nuova sensoristica</div>
    <div class="note">Quando il segnale non esiste, o esiste e non è affidabile. Precisione,
      installazione, proprietà dello strumento e calibrazione si decidono in audit; la
      sensoristica è una voce separata dal software. Se l’installazione richiede un fermo
      linea, va pianificata con la produzione.</div>
  </div>

{ft('Schema di linea tipo · la classificazione riguarda l’impianto, non il prodotto')}
</div>''')


# =====================================================================
# 08 · ARCHITETTURA · prototipo approvato
# =====================================================================
add(rid(P['q3_architettura'], 'p08_architettura'))


# =====================================================================
# 09 · CONTESTUALIZZAZIONE · template B
# =====================================================================
add(f'''<!-- ========= 09 · CONTESTUALIZZAZIONE E QUALITÀ DEL DATO ============== -->
<div class="slide lt" id="p09_contesto" data-kind="dossier">
{hd(2, '09 / 14')}

  <div class="tt tt--sm">Lo stesso evento, lo stesso tempo, lo stesso prodotto.
    <div class="sub" style="margin-top:14px">Senza un tempo comune le cinque letture non si
      incontrano.</div>
  </div>

  <svg class="hero" data-ui="1" style="top:206px" width="880" height="330" viewBox="0 0 880 330"
       role="img" aria-labelledby="b9t b9d">
    <title id="b9t">Un evento allineato su cinque tracce</title>
    <desc id="b9d">Lo stesso intervallo delle 11:24 letto su produzione, stato macchina,
      energia, ordine e causa. Vista ricostruita, dati illustrativi.</desc>

    <rect x="0" y="0" width="880" height="330" fill="#141414"/>
    <text x="64" y="30" font-family="Geist" font-size="14" font-weight="600" fill="#FFFFFF">Linea 1 · finestra 10:00 – 12:00</text>
    <text x="816" y="30" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.48)"
          text-anchor="end">cinque tracce, un solo asse</text>
    <path d="M0 46 L880 46" stroke="rgba(255,255,255,.16)"/>

    <g font-family="Geist" font-size="13" fill="rgba(255,255,255,.48)">
      <text x="64" y="86">Produzione</text><text x="64" y="134">Stato macchina</text>
      <text x="64" y="182">Energia</text><text x="64" y="230">Ordine e formato</text>
      <text x="64" y="278">Causa</text>
    </g>
    <g fill="rgba(255,255,255,.10)">
      <rect x="230" y="70" width="586" height="20"/><rect x="230" y="118" width="586" height="20"/>
      <rect x="230" y="166" width="586" height="20"/><rect x="230" y="214" width="586" height="20"/>
      <rect x="230" y="262" width="586" height="20"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="230" y="70" width="270" height="20"/><rect x="560" y="70" width="256" height="20"/>
      <rect x="230" y="118" width="270" height="20"/><rect x="560" y="118" width="256" height="20"/>
      <rect x="230" y="214" width="586" height="20"/>
    </g>
    <rect x="230" y="166" width="586" height="20" fill="rgba(255,255,255,.30)"/>
    <rect x="500" y="166" width="60" height="20" fill="rgba(255,255,255,.56)"/>
    <rect x="500" y="262" width="60" height="20" fill="#E6E011"/>
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.74)">
      <text x="572" y="84">0 pz/min</text><text x="572" y="132">fermo</text>
      <text x="572" y="180">38 kW</text><text x="572" y="228">ordine 4471 · formato 0,5 L</text>
      <text x="572" y="276">mancanza tappi</text>
    </g>
    <path d="M500 58 L500 292" stroke="#E6E011" stroke-width="1.5"/>
    <text x="500" y="54" font-family="Geist" font-size="12.5" fill="#FFFFFF" text-anchor="middle">11:24</text>
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.48)">
      <text x="230" y="316">10:00</text><text x="523" y="316" text-anchor="middle">11:00</text>
      <text x="816" y="316" text-anchor="end">12:00</text>
    </g>
  </svg>

  <div class="aside" style="top:206px">
    <div class="blk">
      <div class="lbl">I sette attributi</div>
      <div class="sp">tempo · macchina · prodotto · ordine · stato · causa · turno</div>
    </div>
    <div class="hr" style="margin-bottom:18px"></div>
    <div class="blk">
      <div class="lbl">Tre controlli sulla qualità</div>
      <div class="sp"><b>1</b>&ensp;Completezza della serie<br><br><b>2</b>&ensp;Coerenza fra
        sorgenti diverse<br><br><b>3</b>&ensp;Validazione della causa da parte di chi la
        conosce</div>
    </div>
    <div class="note">Senza queste chiavi il dato grezzo resta un numero: non si attribuisce
      una perdita a un formato, né un consumo a uno stato.</div>
  </div>

{ft('Vista ricostruita · dati illustrativi')}
</div>''')


# =====================================================================
# 10 · OEE · prototipo approvato (porta l'apertura della sezione 3)
# =====================================================================
add(rid(P['q4_oee'], 'p10_oee'))


# =====================================================================
# 11 · ENERGIA · prototipo approvato + correzione del titolo (Fase C)
# =====================================================================
s = rid(P['q5_energia'], 'p11_energia')
s = s.replace('Dal consumo del turno al costo del pezzo.', 'Dal consumo al costo energetico del pezzo.')
s = s.replace('<text x="427" y="282">735 kWh &#215; 0,22 &euro;/kWh</text>',
              '<text x="427" y="282">735 kWh &#215; 0,22 &euro;/kWh</text>')
s = s.replace('<text x="427" y="274">costo del turno</text>', '<text x="427" y="274">costo energetico del turno</text>')
add(s)


# =====================================================================
# 12 · OUTPUT · template D
# =====================================================================
add(f'''<!-- ================= 12 · OUTPUT E INTEGRAZIONI ======================= -->
<div class="slide lt" id="p12_output" data-kind="dossier">
{hd(3, '12 / 14')}

  <div class="tt tt--sm">Il dato esce nella forma in cui viene usato.
    <div class="sub" style="margin-top:14px">Ogni output ha un destinatario e una decisione che
      rende possibile.</div>
  </div>

  <div class="tb full" style="top:216px;grid-template-columns:340px 320px 492px">
    <div class="tb__h">Output</div><div class="tb__h">Chi lo usa</div><div class="tb__h">Che decisione abilita</div>

    <div><b>Dashboard a bordo linea</b></div><div>Operatori e capiturno</div><div>Intervenire adesso</div>
    <div><b>Report programmati</b></div><div>Produzione ed energia</div><div>Confrontare i periodi</div>
    <div><b>Export CSV ed Excel</b></div><div>Continuous improvement</div><div>Analizzare fuori dallo strumento</div>
    <div><b>PDF di periodo</b></div><div>Direzione</div><div>Decidere dove investire</div>
    <div><b>Integrazioni</b></div><div>IT e sistemi a valle</div><div>Portare il dato dove serve</div>
  </div>

  <div class="box full" style="top:520px">
    <div class="note">Un output senza destinatario è un file che nessuno apre: la
      configurazione parte da chi deve decidere, non dall’elenco dei formati. Le integrazioni
      con il gestionale sono possibili previa verifica del punto di innesto — perimetro,
      formato e frequenza si chiudono nel solution design.</div>
  </div>

{ft('Struttura degli output · perimetro da confermare')}
</div>''')


# =====================================================================
# 13 · PILOT · template C + apertura sezione 4
# =====================================================================
add(f'''<!-- ============ 13 · PILOT E CRITERI DI ACCETTAZIONE ================== -->
<div class="slide lt" id="p13_pilot" data-kind="dossier">
{band(4, '13 / 14', 'Il pilot non si chiude con una demo, ma con una decisione.')}

  <div class="tt tt--sm" style="top:222px">Una linea, quattro deliverable, criteri dichiarati.</div>

  <svg class="diag" style="top:300px" width="800" height="300" viewBox="0 0 800 300"
       role="img" aria-labelledby="c3t c3d">
    <title id="c3t">I quattro deliverable del pilot</title>
    <desc id="c3d">Mappa dei dati, baseline di produzione ed energia, prime cause e priorità,
      decisione di scala: quattro deliverable in sequenza.</desc>

    <g fill="none" stroke="#0A0A0A" stroke-width="1.5">
      <rect x="64" y="10" width="166" height="66"/><rect x="256" y="10" width="166" height="66"/>
      <rect x="448" y="10" width="166" height="66"/>
    </g>
    <rect x="640" y="10" width="150" height="66" fill="#0A0A0A"/>
    <g font-family="Geist" font-size="14" text-anchor="middle" fill="#0A0A0A">
      <text x="147" y="38">Mappa dati</text><text x="147" y="58">e segnali</text>
      <text x="339" y="38">Baseline produzione</text><text x="339" y="58">ed energia</text>
      <text x="531" y="38">Prime cause</text><text x="531" y="58">e priorità</text>
    </g>
    <g font-family="Geist" font-size="14" text-anchor="middle" fill="#FFFFFF">
      <text x="715" y="38">Decisione</text><text x="715" y="58">di scala</text>
    </g>
    <g stroke="#0A0A0A" stroke-width="1.5">
      <path d="M230 43 L246 43"/><path d="M422 43 L438 43"/><path d="M614 43 L630 43"/>
    </g>
    <g fill="#0A0A0A">
      <polygon points="252,43 242,37 242,49"/><polygon points="444,43 434,37 434,49"/>
      <polygon points="636,43 626,37 626,49"/>
    </g>

    <path d="M64 116 L790 116" stroke="rgba(10,10,10,.13)"/>
    <text x="64" y="146" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)">Le fasi che li producono</text>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.78)">
      <text x="64" y="178">Kickoff · raccolta dati · configurazione · validazione</text>
      <text x="64" y="204">Verifica con gli utenti · chiusura</text>
    </g>
    <path d="M64 236 L790 236" stroke="rgba(10,10,10,.13)"/>
    <text x="64" y="266" font-family="Geist" font-size="15" fill="rgba(10,10,10,.78)">La proposta di estensione si discute con chi dovrà usarla.</text>
  </svg>

  <div class="spec spec--tight" style="top:300px">
    <div class="lbl" style="margin-bottom:6px">Criteri di uscita</div>
    <div class="row"><b>Dati completi</b><span>serie senza buchi</span></div>
    <div class="row"><b>Formule approvate</b><span>dizionario firmato</span></div>
    <div class="row"><b>Cause validate</b><span>da chi le conosce</span></div>
    <div class="row"><b>Report condiviso</b><span>con gli utenti reali</span></div>
    <div class="note" style="margin-top:20px">Durata, partecipanti e condizioni economiche si
      fissano nella proposta di pilot.</div>
  </div>

{ft('Struttura del pilot · durate da confermare')}
</div>''')


# =====================================================================
# 14 · SERVIZI E CONTINUITÀ · template D
# =====================================================================
add(f'''<!-- ============ 14 · SERVIZI, SUPPORTO E CONTINUITÀ =================== -->
<div class="slide lt" id="p14_servizi" data-kind="dossier">
{hd(4, '14 / 14')}

  <div class="tt tt--sm">Il progetto continua dopo il go-live.
    <div class="sub" style="margin-top:14px">Sei servizi, il deliverable di ciascuno e il
      modello con cui vengono erogati.</div>
  </div>

  <div class="tb full" style="top:216px;grid-template-columns:320px 592px 240px">
    <div class="tb__h">Servizio</div><div class="tb__h">Che cosa produce</div><div class="tb__h">Modello</div>

    <div><b>Assessment e perimetrazione</b></div>
    <div>Mappa di asset, sorgenti e gap, perimetro e ipotesi economica</div><div>una tantum</div>
    <div><b>Setup e integrazione</b></div>
    <div>Connettori, mapping, dashboard, formule, utenti e test</div><div>una tantum</div>
    <div><b>KPI e formule</b></div>
    <div>Dizionario KPI, fattori, responsabilità e regole di revisione</div><div>una tantum o periodico</div>
    <div><b>Performance ed energy review</b></div>
    <div>Cause principali, energia fuori produzione, costo per pezzo, priorità</div><div>ricorrente</div>
    <div><b>Formazione e adozione</b></div>
    <div>Onboarding, procedure, materiali e sessioni di aggiornamento</div><div>una tantum o ricorrente</div>
    <div><b>Supporto e scale-up</b></div>
    <div>Supporto, change request, nuove linee e nuovi siti</div><div>ricorrente o a progetto</div>
  </div>

  <div class="box full" style="top:576px">
    <div class="note">Orari, canali, tempi di risposta, manutenzione, aggiornamenti, change
      request ed escalation si formalizzano nella proposta e nel contratto.</div>
  </div>

{ft('Condizioni da formalizzare nella proposta')}
</div>''')


# =====================================================================
# A1 · VERIFICA DI COMPATIBILITÀ · template D
# =====================================================================
add(f'''<!-- ============== A1 · VERIFICA DI COMPATIBILITÀ ====================== -->
<div class="slide lt" id="pa1_compatibilita" data-kind="appendix">
{hd(2, 'ANNESSO A1')}

  <div class="tt tt--sm">La compatibilità si verifica sull’impianto reale.
    <div class="sub" style="margin-top:14px">Che cosa viene controllato macchina per macchina,
      con quale metodo e in che momento.</div>
  </div>

  <div class="tb full" style="top:216px;grid-template-columns:380px 532px 240px">
    <div class="tb__h">Che cosa si verifica</div><div class="tb__h">Come</div><div class="tb__h">Quando</div>

    <div><b>Costruttore e modello del controllore</b></div>
    <div>Inventario compilato con la manutenzione</div><div>audit tecnico</div>
    <div><b>Protocollo e versione</b></div>
    <div>Lettura di prova sulla macchina, non su scheda tecnica</div><div>audit tecnico</div>
    <div><b>Tag disponibili e loro significato</b></div>
    <div>Confronto con la documentazione della macchina e con chi la conduce</div><div>audit tecnico</div>
    <div><b>Frequenza di lettura sostenibile</b></div>
    <div>Test sul carico reale della rete di stabilimento</div><div>audit tecnico</div>
    <div><b>Punti di misura dell’energia</b></div>
    <div>Verifica del quadro e dei contatori esistenti</div><div>audit tecnico</div>
    <div><b>Punto di innesto verso il gestionale</b></div>
    <div>Verifica con l’IT del formato e della direzione dello scambio</div><div>solution design</div>
  </div>

  <div class="box full" style="top:576px">
    <div class="note">Un elenco generico di protocolli non dice se un impianto è leggibile:
      quello che conta è la versione installata su quella macchina e i tag che espone. Per
      questo l’esito di questa verifica è un documento di progetto, non una scheda di prodotto.</div>
  </div>

{ft('Annesso A1 · esito compilato durante l’audit tecnico')}
</div>''')


# =====================================================================
# A2 · DIMENSIONAMENTO · template C
# =====================================================================
add(f'''<!-- ================ A2 · DIMENSIONAMENTO DELL'AMBIENTE ================ -->
<div class="slide lt" id="pa2_sizing" data-kind="appendix">
{hd(2, 'ANNESSO A2')}

  <div class="tt tt--sm">Il dimensionamento si calcola, non si sceglie a listino.
    <div class="sub" style="margin-top:14px">Cinque grandezze determinano la taglia
      dell’ambiente.</div>
  </div>

  <svg class="diag" style="top:216px" width="800" height="380" viewBox="0 0 800 380"
       role="img" aria-labelledby="z2t z2d">
    <title id="z2t">Dalle cinque grandezze alla taglia dell’ambiente</title>
    <desc id="z2d">Numero di tag, frequenza di campionamento, orizzonte di conservazione,
      numero di linee e utenti concorrenti determinano insieme la taglia dell’ambiente.</desc>

    <g fill="#F3F4F0">
      <rect x="64" y="10" width="230" height="52"/><rect x="64" y="72" width="230" height="52"/>
      <rect x="64" y="134" width="230" height="52"/><rect x="64" y="196" width="230" height="52"/>
      <rect x="64" y="258" width="230" height="52"/>
    </g>
    <g font-family="Geist" font-size="15" fill="#0A0A0A">
      <text x="86" y="42">Numero di tag</text><text x="86" y="104">Frequenza di campionamento</text>
      <text x="86" y="166">Orizzonte di conservazione</text><text x="86" y="228">Numero di linee</text>
      <text x="86" y="290">Utenti concorrenti</text>
    </g>

    <g stroke="rgba(10,10,10,.30)" fill="none">
      <path d="M294 36 L360 36 L360 160"/><path d="M294 98 L360 98"/>
      <path d="M294 160 L440 160"/><path d="M294 222 L360 222 L360 160"/>
      <path d="M294 284 L360 284 L360 160"/>
    </g>

    <rect x="440" y="120" width="230" height="80" fill="#0A0A0A"/>
    <text x="555" y="155" font-family="Geist" font-size="16" font-weight="600" fill="#FFFFFF"
          text-anchor="middle">Taglia dell’ambiente</text>
    <text x="555" y="178" font-family="Geist" font-size="13" fill="rgba(255,255,255,.74)"
          text-anchor="middle">CPU · memoria · storage</text>

    <path d="M670 160 L720 160" stroke="rgba(10,10,10,.30)" fill="none"/>
    <g font-family="Geist" font-size="15" fill="#0A0A0A">
      <text x="736" y="132">S</text><text x="736" y="166">M</text><text x="736" y="200">L</text>
    </g>
    <g stroke="rgba(10,10,10,.30)" fill="none">
      <path d="M720 160 L720 126 L730 126"/><path d="M720 160 L730 160"/><path d="M720 160 L720 194 L730 194"/>
    </g>

    <path d="M64 340 L790 340" stroke="rgba(10,10,10,.13)"/>
    <text x="64" y="366" font-family="Geist" font-size="14" fill="rgba(10,10,10,.58)">Le tre taglie sono la conseguenza delle cinque grandezze, non un catalogo da cui scegliere.</text>
  </svg>

  <div class="spec spec--tight" style="top:216px">
    <div class="lbl" style="margin-bottom:6px">Che cosa serve per calcolarlo</div>
    <div class="row"><b>Tag</b><span>quanti segnali per linea</span></div>
    <div class="row"><b>Frequenza</b><span>ogni quanto si campiona</span></div>
    <div class="row"><b>Conservazione</b><span>per quanto tempo</span></div>
    <div class="row"><b>Linee</b><span>oggi e in prospettiva</span></div>
    <div class="row"><b>Utenti</b><span>quanti in contemporanea</span></div>
    <div class="box" style="margin-top:24px"><div class="note">Queste cinque risposte arrivano
      dall’audit tecnico e dal vostro IT. Il dimensionamento viene consegnato con la proposta
      di solution design.</div></div>
  </div>

{ft('Annesso A2 · metodo di dimensionamento')}
</div>''')


# =====================================================================
# A3 · SICUREZZA E GOVERNO DEL DATO · template D
# =====================================================================
add(f'''<!-- ========= A3 · SICUREZZA, GOVERNO DEL DATO E LICENZA =============== -->
<div class="slide lt" id="pa3_governo" data-kind="appendix">
{hd(2, 'ANNESSO A3')}

  <div class="tt tt--sm">Che cosa si decide, e chi lo decide.
    <div class="sub" style="margin-top:14px">Otto ambiti che si chiudono nel solution design
      insieme al vostro IT.</div>
  </div>

  <div class="tb full" style="top:216px;grid-template-columns:300px 592px 260px">
    <div class="tb__h">Ambito</div><div class="tb__h">Che cosa si definisce</div><div class="tb__h">Chi decide</div>

    <div><b>Autenticazione</b></div><div>Metodo e integrazione con la directory aziendale</div><div>IT del cliente</div>
    <div><b>Ruoli e permessi</b></div><div>Chi vede, chi configura, chi modifica le formule</div><div>Operations e IT</div>
    <div><b>Registro degli accessi</b></div><div>Che cosa viene registrato e per quanto tempo</div><div>IT del cliente</div>
    <div><b>Cifratura</b></div><div>Dati in transito e dati a riposo</div><div>IT del cliente</div>
    <div><b>Backup e ripristino</b></div><div>Frequenza, ritenzione e prova di ripristino</div><div>IT del cliente</div>
    <div><b>Conservazione</b></div><div>Orizzonte per le serie storiche e per gli eventi</div><div>Operations e IT</div>
    <div><b>Proprietà del dato</b></div><div>Titolarità, esportabilità e formati</div><div>Legale</div>
    <div><b>Fine contratto</b></div><div>Export finale e cancellazione</div><div>Legale</div>
  </div>

{ft('Annesso A3 · decisioni di progetto, non parametri fissi del prodotto')}
</div>''')


# =====================================================================
# A4 · DIZIONARIO KPI · prototipo approvato
# =====================================================================
s = rid(P['q6_annesso'], 'pa4_kpi')
s = s.replace('<div class="pg">ANNESSO A4</div>', '<div class="pg">ANNESSO A4</div>')
add(s)


body = '<div class="doc">\n' + '\n\n\n'.join(out) + '\n\n</div>\n'
open('dossier_body_v8.html', 'w', encoding='utf-8').write(body)
print(f'dossier_body_v8.html · {len(out)} canvas · {len(body)//1024} KB')
