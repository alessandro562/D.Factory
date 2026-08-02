# -*- coding: utf-8 -*-
# Dossier tecnico v7 · 19 pagine.
# Grammatica: header sottile, titolo, contenuto quasi a tutta larghezza, piede
# discreto. Nessuna fascia laterale. Scuro solo in copertina.
from _approvati import ARCH, REFYN

def hd(t, n):
    return '  <div class="hd"><b>%s</b><span class="pg">%s / 19</span></div>' % (t, n)

def ft(t):
    return ('  <div class="ft"><span class="wm">D<i>.</i>Factory</span>\n'
            '    <span>%s</span></div>' % t)

P = []

# ---------------------------------------------------------------- 01 cover
P.append('''<div class="slide dk" id="d01_cover" data-kind="dossier">
  <div class="z" style="left:64px;right:64px;position:absolute;top:64px">
    <span class="wm" style="font-size:19px">D<i>.</i>Factory</span>
  </div>
  <div style="position:absolute;left:64px;top:150px;width:900px">
    <div style="font-size:46px;line-height:1.1;letter-spacing:-.03em;font-weight:600">Dossier
      tecnico</div>
    <div style="font-size:20px;line-height:1.5;color:var(--d2);margin-top:22px;max-width:720px">Acquisizione,
      supervisione e analisi integrata di produzione ed energia.</div>
  </div>
  <div style="position:absolute;left:64px;top:392px;width:520px">
    <div class="lbl" style="color:var(--d3)">Destinatari</div>
    <div style="font-size:16px;line-height:1.7;color:var(--d2);margin-top:12px">Operations ·
      Engineering · IT/OT<br>Manutenzione · Energia · Procurement tecnico</div>
    <div class="lbl" style="color:var(--d3);margin-top:32px">Versione</div>
    <div style="font-size:16px;line-height:1.7;color:var(--d2);margin-top:12px">v7 · documento
      di lavoro per il solution design</div>
  </div>
  <div style="position:absolute;left:672px;top:392px;width:544px">
    <div class="lbl" style="color:var(--d3)">Sezioni</div>
    <div style="font-size:16px;line-height:1.9;color:var(--d2);margin-top:12px">
      Soluzione e architettura · pagine 02–05<br>
      Che cosa fa il prodotto · pagine 06–13<br>
      Impianto, deployment e integrazioni · pagine 14–17<br>
      Progetto e continuità · pagine 18–19</div>
  </div>
  <div class="ft"><span></span><span>Le viste di prodotto sono ricostruzioni con dati
    illustrativi, dichiarate pagina per pagina</span></div>
</div>''')

# ---------------------------------------------------------------- 02 soluzione
P.append('''<div class="slide lt" id="d02_soluzione" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Una soluzione modulare, dalla visibilità al miglioramento.</div>

  <svg data-ui="1" class="body" width="1152" height="380" viewBox="0 0 1152 380" style="top:180px"
       role="img" aria-labelledby="s2t s2d">
    <title id="s2t">I tre livelli come una sola finestra che cresce</title>
    <desc id="s2d">Connect mostra lo stato, Insight aggiunge cause e impatto, Refyn aggiunge
      priorità, azioni e verifica. I servizi sono attivabili su tutti i livelli.</desc>
    <rect x="0" y="0" width="1152" height="380" fill="#FFFFFF" stroke="rgba(10,10,10,.16)"/>
    <rect x="1" y="1" width="1150" height="42" fill="#F3F4F0"/>
    <text x="20" y="27" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Linea 1 · Confezionamento</text>
    <g font-family="Geist" font-size="15" font-weight="600" fill="#0A0A0A">
      <text x="20" y="76">01 · Connect</text><text x="20" y="180">02 · Insight</text>
      <text x="20" y="284">03 · Refyn</text>
    </g>
    <text x="180" y="284" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">modulo avanzato in sviluppo</text>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="20" y="108">Supervisione, OEE, dati produttivi, consumi e storico</text>
      <text x="20" y="212">Cause, correlazioni, energia per stato, costo e CO₂</text>
      <text x="20" y="316">Priorità, azioni e verifica dei risultati</text>
    </g>
    <g fill="#0A0A0A">
      <rect x="700" y="60" width="180" height="14"/><rect x="700" y="164" width="300" height="14"/>
    </g>
    <rect x="700" y="268" width="412" height="14" fill="none" stroke="rgba(10,10,10,.34)" stroke-dasharray="4 4"/>
    <g stroke="rgba(10,10,10,.16)">
      <path d="M0 130 L1152 130"/><path d="M0 234 L1152 234"/><path d="M0 338 L1152 338"/>
    </g>
    <text x="20" y="364" font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">Servizi specialistici attivabili su tutti i livelli</text>
  </svg>

  <div class="body" style="top:588px"><div class="bd">Ogni livello comprende il precedente e
    lavora sugli stessi dati: produzione, OEE, energia e utility. Non sono tre prodotti
    separati, ma tre gradi di valore estratto dalla stessa acquisizione.</div></div>
@FT@
</div>'''.replace('@HD@', hd('La soluzione', '02')).replace('@FT@', ft('Vista ricostruita · dati illustrativi')))

# ---------------------------------------------------------------- 03 architettura
P.append(ARCH)

# ---------------------------------------------------------------- 04 acquisizione
P.append('''<div class="slide lt" id="d04_acquisizione" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Partiamo dai segnali già disponibili.</div>

  <svg class="body" width="1152" height="392" viewBox="0 0 1152 392" style="top:180px"
       role="img" aria-labelledby="q4t q4d">
    <title id="q4t">Punti di acquisizione su una linea tipo</title>
    <desc id="q4d">Per ogni macchina della linea sono indicati i segnali già presenti, quelli
      da verificare in audit e quelli eventualmente da aggiungere.</desc>

    <g font-family="Geist" font-size="14" font-weight="500" fill="rgba(10,10,10,.56)">
      <text x="0" y="30">Macchina</text><text x="300" y="30">PLC e stati</text>
      <text x="560" y="30">Conta pezzi</text><text x="820" y="30">Contatore energia</text>
    </g>
    <path d="M0 46 L1152 46" stroke="rgba(10,10,10,.26)"/>
    <g font-family="Geist" font-size="17" fill="#0A0A0A">
      <text x="0" y="92">Riempitrice</text><text x="0" y="164">Etichettatrice</text>
      <text x="0" y="236">Tappatrice</text><text x="0" y="308">Quadro di linea</text>
    </g>
    <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.74)">
      <text x="300" y="92">già presente</text><text x="560" y="92">già presente</text><text x="820" y="92">da verificare</text>
      <text x="300" y="164">già presente</text><text x="560" y="164">da verificare</text><text x="820" y="164">da aggiungere</text>
      <text x="300" y="236">già presente</text><text x="560" y="236">già presente</text><text x="820" y="236">da aggiungere</text>
      <text x="300" y="308">—</text><text x="560" y="308">—</text><text x="820" y="308">già presente</text>
    </g>
    <g fill="#0A0A0A">
      <rect x="272" y="80" width="10" height="10"/><rect x="532" y="80" width="10" height="10"/>
      <rect x="272" y="152" width="10" height="10"/><rect x="272" y="224" width="10" height="10"/>
      <rect x="532" y="224" width="10" height="10"/><rect x="792" y="296" width="10" height="10"/>
    </g>
    <g fill="none" stroke="rgba(10,10,10,.40)">
      <rect x="792" y="80" width="10" height="10"/><rect x="532" y="152" width="10" height="10"/>
    </g>
    <g fill="rgba(10,10,10,.14)">
      <rect x="792" y="152" width="10" height="10"/><rect x="792" y="224" width="10" height="10"/>
    </g>
    <g stroke="rgba(10,10,10,.12)">
      <path d="M0 116 L1152 116"/><path d="M0 188 L1152 188"/><path d="M0 260 L1152 260"/>
    </g>
    <path d="M0 340 L1152 340" stroke="rgba(10,10,10,.26)"/>
    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="26" y="376">già presente</text><text x="246" y="376">da verificare in audit</text>
      <text x="516" y="376">da aggiungere</text>
      <text x="820" y="376">gestionale: integrazione da verificare</text>
    </g>
    <rect x="0" y="366" width="10" height="10" fill="#0A0A0A"/>
    <rect x="220" y="366" width="10" height="10" fill="none" stroke="rgba(10,10,10,.40)"/>
    <rect x="490" y="366" width="10" height="10" fill="rgba(10,10,10,.14)"/>
  </svg>

  <div class="body" style="top:596px"><div class="bd">La classificazione riguarda l’impianto,
    non il prodotto: dice dove il dato c’è già, dove va verificato e dove va misurato. È il
    primo output dell’audit tecnico.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Punti di acquisizione', '04')).replace('@FT@', ft('Schema di linea tipo · dati illustrativi')))

# ---------------------------------------------------------------- 05 contestualizzazione
P.append('''<div class="slide lt" id="d05_contestualizzazione" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Lo stesso evento deve avere lo stesso tempo, stato e prodotto.</div>

  <svg data-ui="1" class="body" width="1152" height="360" viewBox="0 0 1152 360" style="top:186px"
       role="img" aria-labelledby="x5t x5d">
    <title id="x5t">Un evento allineato su cinque tracce</title>
    <desc id="x5d">Lo stesso intervallo delle 11:24 letto su produzione, stato macchina,
      energia, ordine e causa: senza un tempo comune le cinque letture non si incontrano.</desc>

    <g font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">
      <text x="0" y="46">Produzione</text><text x="0" y="106">Stato macchina</text>
      <text x="0" y="166">Energia</text><text x="0" y="226">Ordine e formato</text>
      <text x="0" y="286">Causa</text>
    </g>
    <g fill="rgba(10,10,10,.07)">
      <rect x="220" y="30" width="932" height="22"/><rect x="220" y="90" width="932" height="22"/>
      <rect x="220" y="150" width="932" height="22"/><rect x="220" y="210" width="932" height="22"/>
      <rect x="220" y="270" width="932" height="22"/>
    </g>
    <g fill="#0A0A0A">
      <rect x="220" y="30" width="380" height="22"/><rect x="700" y="30" width="452" height="22"/>
      <rect x="220" y="90" width="380" height="22"/><rect x="700" y="90" width="452" height="22"/>
      <rect x="220" y="210" width="932" height="22"/>
    </g>
    <rect x="220" y="150" width="932" height="22" fill="rgba(10,10,10,.34)"/>
    <rect x="600" y="150" width="100" height="22" fill="rgba(10,10,10,.60)"/>
    <rect x="600" y="270" width="100" height="22" fill="#E6E011"/>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">
      <text x="610" y="66">0 pz/min</text><text x="610" y="126">fermo</text>
      <text x="610" y="186">38 kW</text><text x="240" y="246">ordine 4471 · formato 0,5 L</text>
      <text x="610" y="306">mancanza tappi</text>
    </g>
    <path d="M600 16 L600 316" stroke="#E6E011" stroke-width="1.5"/>
    <text x="600" y="12" font-family="Geist" font-size="13" fill="#0A0A0A" text-anchor="middle">11:24</text>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">
      <text x="220" y="344">10:00</text><text x="686" y="344" text-anchor="middle">11:00</text>
      <text x="1152" y="344" text-anchor="end">12:00</text>
    </g>
  </svg>

  <div class="body" style="top:576px"><div class="bd">Ogni misura porta con sé timestamp,
    macchina, linea, stato, turno, ordine, formato, prodotto, lotto, contatore e vettore.
    Senza queste chiavi il dato grezzo resta un numero: non si può attribuire una perdita a
    un formato, né un consumo a uno stato.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Contestualizzazione del dato', '05')).replace('@FT@', ft('Vista ricostruita · dati illustrativi')))

# ---------------------------------------------------------------- 06 connect
P.append('''<div class="slide lt" id="d06_connect" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Connect rende visibile ciò che sta succedendo.</div>

  <svg data-ui="1" class="body" width="1152" height="352" viewBox="0 0 1152 352" style="top:180px"
       role="img" aria-labelledby="k6t k6d">
    <title id="k6t">Vista di supervisione ricostruita</title>
    <desc id="k6d">Stato delle tre macchine lungo il turno, OEE, conteggi, consumi e allarmi.</desc>
    <rect x="0" y="0" width="1152" height="352" fill="#FFFFFF" stroke="rgba(10,10,10,.16)"/>
    <rect x="1" y="1" width="1150" height="44" fill="#F3F4F0"/>
    <text x="20" y="28" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Linea 1 · turno 06:00 – 14:00</text>
    <text x="1132" y="28" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)"
          text-anchor="end">aggiornamento configurato</text>
    <g fill="rgba(10,10,10,.07)">
      <rect x="180" y="74" width="720" height="20"/><rect x="180" y="110" width="720" height="20"/>
      <rect x="180" y="146" width="720" height="20"/>
    </g>
    <g fill="#0A0A0A">
      <rect x="180" y="74" width="108" height="20"/><rect x="296" y="74" width="380" height="20"/>
      <rect x="705" y="74" width="195" height="20"/>
      <rect x="180" y="110" width="108" height="20"/><rect x="296" y="110" width="380" height="20"/>
      <rect x="705" y="110" width="195" height="20"/>
      <rect x="180" y="146" width="108" height="20"/><rect x="296" y="146" width="380" height="20"/>
      <rect x="705" y="146" width="195" height="20"/>
    </g>
    <rect x="676" y="146" width="29" height="20" fill="#E6E011"/>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.74)">
      <text x="20" y="89">Riempitrice</text><text x="20" y="125">Etichettatrice</text>
      <text x="20" y="161">Tappatrice</text>
    </g>
    <path d="M0 192 L1152 192" stroke="rgba(10,10,10,.16)"/>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">
      <text x="20" y="220">OEE del turno</text><text x="300" y="220">Pezzi buoni</text>
      <text x="580" y="220">Energia</text><text x="860" y="220">Allarmi</text>
    </g>
    <g font-family="Geist" font-size="26" font-weight="600" fill="#0A0A0A">
      <text x="20" y="258">71,4%</text><text x="300" y="258">227.000</text>
      <text x="580" y="258">735 kWh</text><text x="860" y="258">3</text>
    </g>
    <path d="M0 288 L1152 288" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">
      <text x="20" y="316">Storico e viste multi-macchina e multi-linea · report standard programmabili</text>
      <text x="20" y="340">Il calcolo dell’OEE segue le regole concordate in configurazione</text>
    </g>
    <rect x="940" y="230" width="10" height="10" fill="#E6E011"/>
  </svg>

  <div class="body" style="top:560px"><div class="bd">Stato di macchina e linea, conteggio
    pezzi e cicli, OEE di base, velocità, allarmi ed eventi, storico, consumi e utility. Le
    viste sono multi-macchina e multi-linea, i report standard sono programmabili.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Connect', '06')).replace('@FT@', ft('Vista ricostruita · dati illustrativi')))

# ---------------------------------------------------------------- 07 insight
P.append('''<div class="slide lt" id="d07_insight" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Insight spiega dove si perde capacità e valore.</div>

  <svg data-ui="1" class="body" width="1152" height="368" viewBox="0 0 1152 368" style="top:180px"
       role="img" aria-labelledby="n7t n7d">
    <title id="n7t">Ranking delle cause e correlazione con l’energia</title>
    <desc id="n7d">A sinistra le cause di fermo ordinate per costo su sette giorni. A destra
      la stessa finestra letta su produzione ed energia.</desc>
    <text x="0" y="20" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Cause di fermo · 7 giorni · ordinate per costo</text>
    <g font-family="Geist" font-size="15" fill="#0A0A0A">
      <text x="0" y="66">Mancanza tappi</text><text x="0" y="118">Cambio formato</text>
      <text x="0" y="170">Micro-fermate</text><text x="0" y="222">Manutenzione</text>
    </g>
    <rect x="220" y="52" width="200" height="16" fill="#E6E011"/>
    <g fill="#0A0A0A">
      <rect x="220" y="104" width="129" height="16"/><rect x="220" y="156" width="85" height="16"/>
      <rect x="220" y="208" width="52" height="16"/>
    </g>
    <g font-family="Geist" font-size="15" font-weight="600" fill="#0A0A0A" text-anchor="end">
      <text x="560" y="66">6.720 €</text><text x="560" y="118">4.340 €</text>
      <text x="560" y="170">2.870 €</text><text x="560" y="222">1.750 €</text>
    </g>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)" text-anchor="end">
      <text x="560" y="252">totale 15.680 € · 58 eventi · 224 minuti</text>
    </g>
    <path d="M620 0 L620 300" stroke="rgba(10,10,10,.16)"/>
    <text x="672" y="20" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Produzione ed energia nella stessa finestra</text>
    <rect x="672" y="52" width="480" height="18" fill="rgba(10,10,10,.07)"/>
    <rect x="672" y="52" width="300" height="18" fill="#0A0A0A"/>
    <rect x="1010" y="52" width="142" height="18" fill="#0A0A0A"/>
    <rect x="672" y="96" width="480" height="18" fill="rgba(10,10,10,.20)"/>
    <rect x="972" y="96" width="38" height="18" fill="rgba(10,10,10,.44)"/>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">
      <text x="672" y="88">produzione</text><text x="672" y="132">energia</text>
      <text x="672" y="166">L’assorbimento non scende a zero quando la linea si ferma.</text>
    </g>
    <path d="M972 40 L972 150" stroke="#E6E011" stroke-width="1.5"/>
    <path d="M620 300 L1152 300" stroke="rgba(10,10,10,.12)"/>
    <g font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">
      <text x="672" y="216">Energia per stato · costo energetico per pezzo</text>
      <text x="672" y="242">CO₂ calcolata o stimata · confronti fra turni, prodotti e formati</text>
      <text x="672" y="268">KPI e formule concordate in configurazione</text>
    </g>
    <text x="0" y="330" font-family="Geist" font-size="13" fill="rgba(10,10,10,.56)">Micro-fermate e perdite di velocità · scarti e qualità · velocità reale contro nominale</text>
  </svg>

  <div class="body" style="top:576px"><div class="bd">La causa è associata all’evento e
    validata da chi la conosce. Il ranking non ordina per frequenza ma per impatto: quattordici
    fermi brevi possono pesare più di un fermo lungo.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Insight', '07')).replace('@FT@', ft('Vista ricostruita · dati illustrativi')))

# ---------------------------------------------------------------- 08 refyn
P.append(REFYN)
