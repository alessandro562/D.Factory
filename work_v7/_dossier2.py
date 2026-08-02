# -*- coding: utf-8 -*-
# Dossier tecnico v7 · pagine 09-19.
from _dossier import P, hd, ft

# ---------------------------------------------------------------- 09 OEE
P.append('''<div class="slide lt" id="d09_oee" data-kind="dossier">
@HD@
  <div class="tt tt--sm">OEE macchina e OEE linea non sono la stessa domanda.</div>

  <svg class="body" width="1152" height="360" viewBox="0 0 1152 360" style="top:186px"
       role="img" aria-labelledby="o9t o9d">
    <title id="o9t">Confini di macchina e di linea</title>
    <desc id="o9d">La stessa macchina può essere ferma perché bloccata a valle o in
      mancanza di materiale a monte: il calcolo di linea deve dichiarare come tratta questi
      due stati e come aggrega i confini.</desc>

    <g fill="none" stroke="#0A0A0A" stroke-width="1.5">
      <rect x="0" y="40" width="300" height="72"/><rect x="426" y="40" width="300" height="72"/>
      <rect x="852" y="40" width="300" height="72"/>
    </g>
    <g font-family="Geist" font-size="17" fill="#0A0A0A" text-anchor="middle">
      <text x="150" y="83">Riempitrice</text><text x="576" y="83">Tappatrice</text>
      <text x="1002" y="83">Etichettatrice</text>
    </g>
    <g stroke="#0A0A0A" stroke-width="1.5">
      <path d="M300 76 L414 76"/><path d="M726 76 L840 76"/>
    </g>
    <g fill="#0A0A0A">
      <polygon points="420,76 410,70 410,82"/><polygon points="846,76 836,70 836,82"/>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)" text-anchor="middle">
      <text x="357" y="62">buffer</text><text x="783" y="62">buffer</text>
    </g>

    <path d="M0 152 L1152 152" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="15" font-weight="600" fill="#0A0A0A">
      <text x="0" y="188">Blocking</text><text x="426" y="188">Starvation</text>
      <text x="852" y="188">Aggregazione</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.74)">
      <text x="0" y="216">La macchina potrebbe produrre</text>
      <text x="0" y="238">ma il buffer a valle è pieno.</text>
      <text x="426" y="216">La macchina potrebbe produrre</text>
      <text x="426" y="238">ma manca materiale a monte.</text>
      <text x="852" y="216">Il confine scelto decide</text>
      <text x="852" y="238">quale perdita entra nel calcolo.</text>
    </g>
    <path d="M0 278 L1152 278" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="0" y="312">Disponibilità · prestazione · qualità</text>
      <text x="426" y="312">Planned production time · ideal cycle time</text>
      <text x="852" y="312">Good count · pezzi conformi</text>
      <text x="0" y="344">Le formule e i confini si fissano in configurazione e si scrivono nel dizionario KPI.</text>
    </g>
  </svg>

  <div class="body" style="top:576px"><div class="bd">Il calcolo di linea deve considerare
    confini, blocking, starvation, buffer e regole di aggregazione. Due impianti che dichiarano
    lo stesso OEE possono averlo calcolato su perimetri diversi: per questo il perimetro va
    scritto prima del numero.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Stato macchina e OEE', '09')).replace('@FT@', ft('Schema di calcolo · nessun dato di impianto')))

# ---------------------------------------------------------------- 10 perdite
P.append('''<div class="slide lt" id="d10_perdite" data-kind="dossier">
@HD@
  <div class="tt tt--sm">La perdita non è soltanto il fermo lungo.</div>

  <svg data-ui="1" class="body" width="1152" height="340" viewBox="0 0 1152 340" style="top:186px"
       role="img" aria-labelledby="l10t l10d">
    <title id="l10t">Quattro perdite sulla stessa timeline</title>
    <desc id="l10d">Sulla stessa ora convivono un fermo lungo, alcune micro-fermate, un tratto
      a velocità ridotta e uno scarto: solo il primo si vede nel rapporto di turno.</desc>

    <text x="0" y="20" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Tappatrice · 11:00 – 12:00</text>
    <rect x="0" y="40" width="1152" height="40" fill="rgba(10,10,10,.07)"/>
    <g fill="#0A0A0A">
      <rect x="0" y="40" width="460" height="40"/><rect x="806" y="40" width="346" height="40"/>
    </g>
    <rect x="460" y="40" width="346" height="40" fill="#E6E011"/>
    <g fill="rgba(10,10,10,.44)">
      <rect x="140" y="40" width="10" height="40"/><rect x="238" y="40" width="8" height="40"/>
      <rect x="330" y="40" width="9" height="40"/><rect x="900" y="40" width="8" height="40"/>
      <rect x="1010" y="40" width="10" height="40"/>
    </g>
    <rect x="620" y="40" width="0" height="40"/>
    <g fill="rgba(10,10,10,.20)"><rect x="806" y="40" width="180" height="40"/></g>
    <rect x="1080" y="40" width="14" height="40" fill="none" stroke="#0A0A0A" stroke-width="1.5"/>

    <g stroke="rgba(10,10,10,.34)">
      <path d="M633 80 L633 128"/><path d="M145 80 L145 168"/><path d="M896 80 L896 208"/>
      <path d="M1087 80 L1087 248"/>
    </g>
    <g font-family="Geist" font-size="15" fill="#0A0A0A">
      <text x="633" y="148">Fermo · 18 minuti · causa associata</text>
      <text x="145" y="188">Micro-fermate · sotto la soglia del rapporto</text>
      <text x="633" y="228">Velocità ridotta · sotto il tempo ciclo nominale</text>
      <text x="633" y="268">Scarto · pezzi non conformi</text>
    </g>
    <path d="M0 296 L1152 296" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="0" y="328">Per ognuna: durata, frequenza, causa associata, impatto e confronto con la baseline.</text>
    </g>
  </svg>

  <div class="body" style="top:566px"><div class="bd">Le micro-fermate stanno sotto la soglia
    con cui un rapporto manuale registra un fermo: singolarmente valgono poco, sommate valgono
    un turno. Le regole di validazione decidono che cosa è un fermo e che cosa è rumore.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Fermi, micro-fermate, velocità e qualità', '10')).replace('@FT@', ft('Vista ricostruita · dati illustrativi')))

# ---------------------------------------------------------------- 11 energia
P.append('''<div class="slide lt" id="d11_energia" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Consumo e produzione devono essere letti nello stesso momento.</div>

  <svg data-ui="1" class="body" width="1152" height="352" viewBox="0 0 1152 352" style="top:186px"
       role="img" aria-labelledby="e11t e11d">
    <title id="e11t">Energia per stato e per vettore</title>
    <desc id="e11d">Il consumo del turno diviso fra marcia e linea ferma, e i vettori
      configurabili oltre all’elettricità.</desc>

    <text x="0" y="20" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Elettricità del turno · per stato</text>
    <rect x="0" y="40" width="1128" height="34" fill="#0A0A0A"/>
    <rect x="1103" y="40" width="25" height="34" fill="rgba(10,10,10,.34)"/>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="0" y="102">719 kWh in marcia</text><text x="300" y="102">16 kWh a linea ferma</text>
      <text x="640" y="102">735 kWh nel turno</text>
    </g>
    <path d="M0 128 L1152 128" stroke="rgba(10,10,10,.12)"/>

    <text x="0" y="162" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Vettori configurabili</text>
    <g fill="none" stroke="rgba(10,10,10,.34)">
      <rect x="0" y="180" width="216" height="44"/><rect x="234" y="180" width="216" height="44"/>
      <rect x="468" y="180" width="216" height="44"/><rect x="702" y="180" width="216" height="44"/>
      <rect x="936" y="180" width="216" height="44"/>
    </g>
    <rect x="0" y="180" width="216" height="44" fill="#0A0A0A"/>
    <g font-family="Geist" font-size="15" text-anchor="middle">
      <text x="108" y="208" fill="#FFFFFF">elettricità</text>
      <text x="342" y="208" fill="rgba(10,10,10,.74)">gas</text>
      <text x="576" y="208" fill="rgba(10,10,10,.74)">vapore</text>
      <text x="810" y="208" fill="rgba(10,10,10,.74)">aria compressa</text>
      <text x="1044" y="208" fill="rgba(10,10,10,.74)">acqua</text>
    </g>
    <text x="936" y="248" font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">l’acqua è una utility, non energia</text>
    <path d="M0 278 L1152 278" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="0" y="312">Il consumo si legge per macchina, linea, contatore, turno, periodo e stato.</text>
      <text x="0" y="340">Dove il contatore non esiste, il perimetro di misura si dichiara prima del calcolo.</text>
    </g>
  </svg>

  <div class="body" style="top:576px"><div class="bd">Leggere il consumo sullo stesso asse
    temporale della produzione permette di attribuirlo a uno stato: marcia, fermo, cambio
    formato, sanificazione. È la condizione per passare dal kWh totale al kWh per pezzo.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Energia e utility', '11')).replace('@FT@', ft('Vista ricostruita · dati illustrativi')))

# ---------------------------------------------------------------- 12 costo e CO2
P.append('''<div class="slide lt" id="d12_costo_co2" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Dal consumo al costo energetico del pezzo.</div>

  <svg class="body" width="1152" height="344" viewBox="0 0 1152 344" style="top:186px"
       role="img" aria-labelledby="c12t c12d">
    <title id="c12t">La catena di calcolo</title>
    <desc id="c12d">Consumo, fattore di costo e fattore emissivo si incontrano con la
      quantità prodotta per dare euro, kilowattora e chilogrammi di CO2 per pezzo.</desc>

    <g fill="none" stroke="#0A0A0A" stroke-width="1.5">
      <rect x="0" y="30" width="248" height="64"/><rect x="302" y="30" width="248" height="64"/>
      <rect x="604" y="30" width="248" height="64"/>
    </g>
    <rect x="906" y="30" width="246" height="64" fill="#0A0A0A"/>
    <g font-family="Geist" font-size="16" text-anchor="middle">
      <text x="124" y="68" fill="#0A0A0A">Consumo</text><text x="426" y="68" fill="#0A0A0A">Fattori</text>
      <text x="728" y="68" fill="#0A0A0A">Quantità prodotta</text>
      <text x="1029" y="68" fill="#FFFFFF">Indicatore per pezzo</text>
    </g>
    <g stroke="#0A0A0A" stroke-width="1.5">
      <path d="M248 62 L290 62"/><path d="M550 62 L592 62"/><path d="M852 62 L894 62"/>
    </g>
    <g fill="#0A0A0A">
      <polygon points="296,62 286,56 286,68"/><polygon points="598,62 588,56 588,68"/>
      <polygon points="900,62 890,56 890,68"/>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)" text-anchor="middle">
      <text x="124" y="120">kWh per stato e periodo</text><text x="426" y="120">costo · emissivo</text>
      <text x="728" y="120">pezzi buoni · lotto</text><text x="1029" y="120">per prodotto e periodo</text>
    </g>

    <path d="M0 164 L1152 164" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="26" font-weight="600" fill="#0A0A0A">
      <text x="0" y="216">3,2</text><text x="300" y="216">0,71 €</text>
      <text x="640" y="216">1,13 kg</text>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="0" y="246">kWh per 1.000 pezzi</text><text x="300" y="246">costo energetico per 1.000 pezzi</text>
      <text x="640" y="246">CO₂e calcolata per 1.000 pezzi</text>
    </g>
    <path d="M0 278 L1152 278" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="0" y="310">735 kWh · 0,22 €/kWh · 0,35 kgCO₂e/kWh · 227.000 pezzi nel turno</text>
      <text x="0" y="336">CO₂ calcolata o stimata a partire dai fattori emissivi dichiarati, non misurata.</text>
    </g>
  </svg>

  <div class="body" style="top:568px"><div class="bd">Il costo energetico per pezzo si confronta
    fra formati e periodi: è il modo in cui un consumo diventa un argomento di produzione. I
    fattori di costo e i fattori emissivi vanno dichiarati e rivisti periodicamente.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Costo energetico e CO₂', '12')).replace('@FT@', ft('Esempio ricostruito · fattori da validare')))

# ---------------------------------------------------------------- 13 metodo
P.append('''<div class="slide lt" id="d13_metodo" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Cinque passaggi dal segnale al KPI.</div>

  <svg class="body" width="1152" height="336" viewBox="0 0 1152 336" style="top:186px"
       role="img" aria-labelledby="m13t m13d">
    <title id="m13t">La sequenza di calcolo</title>
    <desc id="m13d">Acquisizione, contestualizzazione, conteggio, normalizzazione e calcolo,
      con i controlli che accompagnano ogni passaggio.</desc>

    <g font-family="Geist" font-size="14" font-weight="500" fill="rgba(10,10,10,.56)">
      <text x="0" y="24">01</text><text x="234" y="24">02</text><text x="468" y="24">03</text>
      <text x="702" y="24">04</text><text x="936" y="24">05</text>
    </g>
    <g fill="none" stroke="#0A0A0A" stroke-width="1.5">
      <rect x="0" y="40" width="192" height="60"/><rect x="234" y="40" width="192" height="60"/>
      <rect x="468" y="40" width="192" height="60"/><rect x="702" y="40" width="192" height="60"/>
    </g>
    <rect x="936" y="40" width="216" height="60" fill="#0A0A0A"/>
    <g font-family="Geist" font-size="16" text-anchor="middle">
      <text x="96" y="76" fill="#0A0A0A">Acquisizione</text>
      <text x="330" y="76" fill="#0A0A0A">Contesto</text>
      <text x="564" y="76" fill="#0A0A0A">Conteggio</text>
      <text x="798" y="76" fill="#0A0A0A">Normalizzazione</text>
      <text x="1044" y="76" fill="#FFFFFF">Calcolo del KPI</text>
    </g>
    <g stroke="#0A0A0A" stroke-width="1.5">
      <path d="M192 70 L222 70"/><path d="M426 70 L456 70"/><path d="M660 70 L690 70"/>
      <path d="M894 70 L924 70"/>
    </g>
    <g fill="#0A0A0A">
      <polygon points="228,70 218,64 218,76"/><polygon points="462,70 452,64 452,76"/>
      <polygon points="696,70 686,64 686,76"/><polygon points="930,70 920,64 920,76"/>
    </g>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="0" y="130">segnali e tag</text><text x="234" y="130">tempo, stato, ordine</text>
      <text x="468" y="130">pezzi e cicli</text><text x="702" y="130">unità e perimetri</text>
      <text x="936" y="130">formule concordate</text>
    </g>

    <path d="M0 176 L1152 176" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="15" font-weight="600" fill="#0A0A0A">
      <text x="0" y="212">Che cosa accompagna ogni passaggio</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="0" y="248">Qualità del dato e completezza delle serie</text>
      <text x="0" y="278">Gestione delle anomalie e dei buchi di acquisizione</text>
      <text x="0" y="308">Validazione delle formule con chi le userà</text>
      <text x="592" y="248">Baseline dichiarata prima di misurare un miglioramento</text>
      <text x="592" y="278">Revisione periodica di fattori, soglie e regole</text>
      <text x="592" y="308">Dizionario KPI condiviso fra produzione, energia e IT</text>
    </g>
  </svg>

  <div class="body" style="top:560px"><div class="bd">Un KPI non è affidabile perché la formula
    è giusta, ma perché ogni passaggio a monte è dichiarato: da quale tag arriva il segnale,
    con quale tempo viene contestualizzato, che cosa conta come pezzo buono.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Metodo di misura', '13')).replace('@FT@', ft('Metodo · nessun dato di impianto')))
