# -*- coding: utf-8 -*-
# Le slide che la V7 aggiunge o riscrive. Tenute fuori dal corpo per poterle
# rigenerare senza toccare le slide che il committente ha gia' approvato.

S03 = '''
<!-- ==================== 03 · CHE COS’È D.FACTORY =====================
     Una sola interfaccia composita, non un diagramma: stato e produzione,
     energia per stato, impatto economico. Tre callout, un solo giallo. -->
<div class="slide dk" id="s03_cosa_e">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Produzione, energia e costi<br>nello stesso contesto operativo.</h2>
  </div>
  <div class="z" style="top:160px;width:1000px"><div class="cp">D.Factory acquisisce e
    contestualizza dati da PLC, sensori, contatori e gestionali per rendere leggibili
    performance, consumi e perdite.</div></div>

  <svg data-ui="1" width="1280" height="420" viewBox="0 0 1280 420"
       style="position:absolute;left:0;top:236px" role="img" aria-labelledby="c3t c3d">
    <title id="c3t">Vista composita ricostruita</title>
    <desc id="c3d">Una sola schermata con tre letture dello stesso turno: lo stato delle tre
      macchine con l’OEE, l’energia divisa fra marcia e linea ferma, e l’impatto economico
      del fermo e dei consumi.</desc>

    <rect x="0" y="0" width="1280" height="420" fill="#141414"/>
    <path d="M0 .75 L1280 .75" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>
    <text x="64" y="34" font-family="Geist" font-size="15" font-weight="600" fill="#FFFFFF">Linea 1 · Confezionamento</text>
    <text x="1216" y="34" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)"
          text-anchor="end">turno 06:00 – 14:00</text>
    <path d="M0 52 L1280 52" stroke="rgba(255,255,255,.14)"/>
    <path d="M520 52 L520 420" stroke="rgba(255,255,255,.14)"/>
    <path d="M920 52 L920 420" stroke="rgba(255,255,255,.14)"/>

    <!-- 01 · stato e produzione -->
    <text x="64" y="86" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">01 · Stato e produzione</text>
    <g fill="rgba(255,255,255,.09)">
      <rect x="230" y="112" width="270" height="14"/><rect x="230" y="140" width="270" height="14"/>
      <rect x="230" y="168" width="270" height="14"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="230" y="112" width="189" height="14"/><rect x="460" y="112" width="40" height="14"/>
      <rect x="230" y="140" width="189" height="14"/><rect x="460" y="140" width="40" height="14"/>
      <rect x="230" y="168" width="189" height="14"/><rect x="460" y="168" width="40" height="14"/>
    </g>
    <rect x="419" y="168" width="41" height="14" fill="#E6E011"/>
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.72)">
      <text x="64" y="123">Riempitrice</text><text x="64" y="151">Etichettatrice</text>
      <text x="64" y="179">Tappatrice</text>
    </g>
    <text x="64" y="238" font-family="Geist" font-size="30" font-weight="600" fill="#FFFFFF">71,4%</text>
    <text x="64" y="266" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">OEE del turno</text>
    <text x="64" y="320" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">454 min in marcia</text>
    <text x="64" y="346" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">26 min di fermo</text>

    <!-- 02 · energia e utility -->
    <text x="560" y="86" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">02 · Energia e utility</text>
    <text x="560" y="132" font-family="Geist" font-size="30" font-weight="600" fill="#FFFFFF">735<tspan font-size="17"> kWh</tspan></text>
    <text x="560" y="158" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">elettricità del turno</text>
    <rect x="560" y="188" width="313" height="20" fill="rgba(255,255,255,.82)"/>
    <rect x="873" y="188" width="7" height="20" fill="rgba(255,255,255,.40)"/>
    <text x="560" y="232" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">719 kWh in marcia</text>
    <text x="560" y="258" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">16 kWh a linea ferma</text>
    <path d="M560 292 L880 292" stroke="rgba(255,255,255,.14)"/>
    <text x="560" y="320" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">Altri vettori configurabili</text>
    <text x="560" y="346" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">gas · vapore · aria compressa · acqua</text>

    <!-- 03 · impatto economico -->
    <text x="960" y="86" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">03 · Impatto economico</text>
    <text x="960" y="140" font-family="Geist" font-size="34" font-weight="600" fill="#FFFFFF">1.820 €</text>
    <text x="960" y="166" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">margine perso stimato</text>
    <text x="960" y="188" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">26 min × 70 €/min</text>
    <path d="M960 216 L1216 216" stroke="rgba(255,255,255,.14)"/>
    <text x="960" y="262" font-family="Geist" font-size="28" font-weight="600" fill="#FFFFFF">162 €</text>
    <text x="960" y="288" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)">costo energetico del turno</text>
    <text x="960" y="310" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">735 kWh × 0,22 €/kWh</text>
    <path d="M960 338 L1216 338" stroke="rgba(255,255,255,.14)"/>
    <text x="960" y="368" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">Causa associata al fermo</text>
    <text x="960" y="392" font-family="Geist" font-size="15" fill="#FFFFFF">Mancanza tappi a monte</text>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span>
    <span class="nt">Vista ricostruita · dati illustrativi</span><span>03 / 12</span></div>
</div>

'''

S07 = '''
<!-- ==================== 07 · AMPIEZZA DEL PRODOTTO ====================
     Una sola vista a mosaico: sei riquadri della stessa dashboard, non sei
     card. Ogni riquadro e' una mini-interfaccia con il suo dato. -->
<div class="slide dk" id="s07_ampiezza">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Non solo fermi.<br>La linea, il turno e il pezzo.</h2>
  </div>

  <svg data-ui="1" width="1280" height="452" viewBox="0 0 1280 452"
       style="position:absolute;left:0;top:176px" role="img" aria-labelledby="a7t a7d">
    <title id="a7t">Sei riquadri della stessa dashboard, ricostruiti</title>
    <desc id="a7d">Stato di macchina e linea, OEE e velocità, fermi e micro-fermate, consumi
      e utility, costo energetico e CO2 per mille pezzi, confronti fra le macchine del turno.</desc>

    <rect x="0" y="0" width="1280" height="452" fill="#141414"/>
    <path d="M0 .75 L1280 .75" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>
    <text x="64" y="34" font-family="Geist" font-size="15" font-weight="600" fill="#FFFFFF">Linea 1 · Confezionamento</text>
    <text x="1216" y="34" font-family="Geist" font-size="13" fill="rgba(255,255,255,.44)"
          text-anchor="end">turno 06:00 – 14:00</text>
    <path d="M0 52 L1280 52" stroke="rgba(255,255,255,.14)"/>
    <g stroke="rgba(255,255,255,.14)">
      <path d="M448 52 L448 452"/><path d="M832 52 L832 452"/><path d="M0 252 L1280 252"/>
    </g>

    <!-- 1 · stato macchina e linea -->
    <text x="64" y="84" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">Stato macchina e linea</text>
    <g fill="rgba(255,255,255,.09)">
      <rect x="180" y="108" width="220" height="12"/><rect x="180" y="136" width="220" height="12"/>
      <rect x="180" y="164" width="220" height="12"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="180" y="108" width="154" height="12"/><rect x="367" y="108" width="33" height="12"/>
      <rect x="180" y="136" width="220" height="12"/>
      <rect x="180" y="164" width="154" height="12"/><rect x="367" y="164" width="33" height="12"/>
    </g>
    <g font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.56)">
      <text x="64" y="118">Riempitrice</text><text x="64" y="146">Etichettatrice</text>
      <text x="64" y="174">Tappatrice</text>
    </g>
    <text x="64" y="212" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">3 macchine · 1 linea</text>

    <!-- 2 · OEE e velocità -->
    <text x="480" y="84" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">OEE e velocità</text>
    <text x="480" y="128" font-family="Geist" font-size="34" font-weight="600" fill="#FFFFFF">71,4%</text>
    <g font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.56)">
      <text x="480" y="164">disponibilità</text><text x="480" y="188">prestazione</text>
      <text x="480" y="212">qualità</text>
    </g>
    <g fill="rgba(255,255,255,.09)">
      <rect x="600" y="154" width="200" height="10"/><rect x="600" y="178" width="200" height="10"/>
      <rect x="600" y="202" width="200" height="10"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="600" y="154" width="189" height="10"/><rect x="600" y="178" width="158" height="10"/>
      <rect x="600" y="202" width="191" height="10"/>
    </g>

    <!-- 3 · fermi e micro-fermate -->
    <text x="864" y="84" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">Fermi e micro-fermate</text>
    <rect x="864" y="120" width="352" height="26" fill="rgba(255,255,255,.09)"/>
    <g fill="rgba(255,255,255,.82)">
      <rect x="864" y="120" width="52" height="26"/><rect x="920" y="120" width="118" height="26"/>
      <rect x="1051" y="120" width="107" height="26"/><rect x="1160" y="120" width="56" height="26"/>
    </g>
    <rect x="1038" y="120" width="13" height="26" fill="#E6E011"/>
    <g fill="rgba(255,255,255,.40)">
      <rect x="916" y="120" width="4" height="26"/><rect x="1158" y="120" width="2" height="26"/>
      <rect x="982" y="120" width="3" height="26"/><rect x="1100" y="120" width="3" height="26"/>
    </g>
    <text x="864" y="176" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">3 fermi · 26 minuti</text>
    <text x="864" y="204" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">micro-fermate rilevate a parte</text>

    <!-- 4 · consumi e utility -->
    <text x="64" y="284" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">Consumi e utility</text>
    <text x="64" y="326" font-family="Geist" font-size="28" font-weight="600" fill="#FFFFFF">735<tspan font-size="16"> kWh</tspan></text>
    <rect x="64" y="346" width="336" height="14" fill="rgba(255,255,255,.82)"/>
    <text x="64" y="392" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">vettori configurabili</text>
    <g fill="none" stroke="rgba(255,255,255,.30)">
      <rect x="64" y="404" width="76" height="24"/><rect x="150" y="404" width="76" height="24"/>
      <rect x="236" y="404" width="76" height="24"/><rect x="322" y="404" width="78" height="24"/>
    </g>
    <g font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.56)" text-anchor="middle">
      <text x="102" y="420">gas</text><text x="188" y="420">vapore</text>
      <text x="274" y="420">aria</text><text x="361" y="420">acqua</text>
    </g>

    <!-- 5 · costo energetico e CO2 -->
    <text x="480" y="284" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">Costo energetico e CO₂</text>
    <g font-family="Geist" font-size="22" font-weight="600" fill="#FFFFFF">
      <text x="480" y="326">3,2</text><text x="480" y="366">0,71</text><text x="480" y="406">1,13</text>
    </g>
    <g font-family="Geist" font-size="13" fill="rgba(255,255,255,.56)">
      <text x="560" y="326">kWh / 1.000 pz</text><text x="560" y="366">€ / 1.000 pz</text>
      <text x="560" y="406">kgCO₂e / 1.000 pz</text>
    </g>
    <text x="800" y="428" font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.44)"
          text-anchor="end">CO₂ calcolata</text>

    <!-- 6 · confronti -->
    <text x="864" y="284" font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.44)">Confronti per turno, prodotto e linea</text>
    <g font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.56)">
      <text x="864" y="326">Tappatrice</text><text x="864" y="360">Riempitrice</text>
      <text x="864" y="394">Etichettatrice</text>
    </g>
    <g fill="rgba(255,255,255,.09)">
      <rect x="990" y="314" width="226" height="14"/><rect x="990" y="348" width="226" height="14"/>
      <rect x="990" y="382" width="226" height="14"/>
    </g>
    <g fill="rgba(255,255,255,.82)">
      <rect x="990" y="314" width="226" height="14"/><rect x="990" y="348" width="100" height="14"/>
    </g>
    <g font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.72)">
      <text x="990" y="424">minuti di fermo nel turno · 18 · 8 · 0</text>
    </g>
  </svg>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span>
    <span class="nt">Viste ricostruite · dati illustrativi</span><span>07 / 12</span></div>
</div>

'''

S09 = '''
<!-- ====================== 09 · PERCHÉ D.FACTORY ======================
     Tre prove in tre fasce, non tre card. Nessun cliente, nessun logo,
     nessun numero non validato. -->
<div class="slide dk" id="s09_perche">
  <div class="z" style="top:48px;width:1100px">
    <h2 class="sm">Nato sull’impianto,<br>non in una dashboard.</h2>
  </div>

  <svg width="1280" height="392" viewBox="0 0 1280 392"
       style="position:absolute;left:0;top:184px" role="img" aria-labelledby="p9t p9d">
    <title id="p9t">Tre prove</title>
    <desc id="p9d">Produzione ed energia sulla stessa lettura temporale, partenza dai
      segnali già presenti sull’impianto, piattaforma affiancata da assessment,
      configurazione e review.</desc>
    <g stroke="rgba(255,255,255,.14)">
      <path d="M0 130 L1280 130"/><path d="M0 260 L1280 260"/>
    </g>

    <!-- 1 · produzione ed energia sulla stessa lettura -->
    <g fill="rgba(255,255,255,.82)">
      <rect x="700" y="36" width="180" height="12"/><rect x="920" y="36" width="296" height="12"/>
    </g>
    <rect x="880" y="36" width="40" height="12" fill="#E6E011"/>
    <rect x="700" y="62" width="516" height="12" fill="rgba(255,255,255,.30)"/>
    <rect x="880" y="62" width="40" height="12" fill="rgba(255,255,255,.60)"/>
    <g font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.44)">
      <text x="620" y="46">produzione</text><text x="620" y="72">energia</text>
    </g>
    <text x="700" y="98" font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.44)">stesso asse dei tempi, stesso evento</text>

    <!-- 2 · brownfield -->
    <g fill="none" stroke="rgba(255,255,255,.40)">
      <rect x="700" y="166" width="118" height="34"/><rect x="830" y="166" width="118" height="34"/>
      <rect x="960" y="166" width="118" height="34"/><rect x="1090" y="166" width="126" height="34"/>
    </g>
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.72)" text-anchor="middle">
      <text x="759" y="187">PLC</text><text x="889" y="187">sensori</text>
      <text x="1019" y="187">contatori</text><text x="1153" y="187">gestionale</text>
    </g>
    <text x="700" y="226" font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.44)">quello che c’è già, verificato in audit</text>

    <!-- 3 · software e competenze -->
    <rect x="700" y="296" width="200" height="34" fill="rgba(255,255,255,.82)"/>
    <text x="800" y="318" font-family="Geist" font-size="13" fill="#0A0A0A" text-anchor="middle">piattaforma</text>
    <g fill="none" stroke="rgba(255,255,255,.40)">
      <rect x="912" y="296" width="98" height="34"/><rect x="1022" y="296" width="98" height="34"/>
      <rect x="1132" y="296" width="84" height="34"/>
    </g>
    <g font-family="Geist" font-size="12.5" fill="rgba(255,255,255,.72)" text-anchor="middle">
      <text x="961" y="318">assessment</text><text x="1071" y="318">configura</text><text x="1174" y="318">review</text>
    </g>
    <text x="700" y="356" font-family="Geist" font-size="11.5" fill="rgba(255,255,255,.44)">il software da solo non chiude una causa</text>
  </svg>

  <div style="position:absolute;left:64px;top:210px;width:500px">
    <div style="font-size:19px;font-weight:600">Produzione ed energia</div>
    <div class="cp" style="margin-top:6px">La stessa lettura temporale, non due strumenti.</div>
  </div>
  <div style="position:absolute;left:64px;top:340px;width:500px">
    <div style="font-size:19px;font-weight:600">Brownfield</div>
    <div class="cp" style="margin-top:6px">Si parte da PLC, sensori e contatori esistenti, previa verifica.</div>
  </div>
  <div style="position:absolute;left:64px;top:470px;width:500px">
    <div style="font-size:19px;font-weight:600">Software e competenze</div>
    <div class="cp" style="margin-top:6px">La piattaforma con assessment, configurazione e review.</div>
  </div>

  <div class="z" style="top:596px"><div class="note">Evolve le competenze sviluppate con
    MAPST 4.0 e MarEnergy.</div></div>

  <div class="rail"><span class="wm">D<i>.</i>Factory</span><span>09 / 12</span></div>
</div>

'''
