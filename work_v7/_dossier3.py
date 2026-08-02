# -*- coding: utf-8 -*-
# Dossier tecnico v7 · pagine 14-19.
from _dossier import P, hd, ft
import _dossier2  # noqa: F401  (popola P fino alla 13)

# ---------------------------------------------------------------- 14 brownfield
P.append('''<div class="slide lt" id="d14_brownfield" data-kind="dossier">
@HD@
  <div class="tt tt--sm">La compatibilità si verifica sull’impianto reale.</div>

  <div class="body" style="top:180px">
    <div class="tb" style="grid-template-columns:280px 1fr">
      <div class="tb__h">Esito</div><div class="tb__h">Che cosa significa</div>
      <div>Supportato</div><div>Configurazione nota, nessuno sviluppo previsto</div>
      <div>Condizionato</div><div>Dipende dalla versione del firmware o dall’assetto di rete</div>
      <div>Da verificare</div><div>Serve l’audit sull’impianto per stabilirlo</div>
      <div>Da aggiungere</div><div>Il dato non esiste: serve un sensore o un contatore</div>
    </div>
  </div>

  <div class="body" style="top:474px">
    <div class="lbl">Che cosa entra nell’inventario</div>
    <div class="cols" style="margin-top:18px">
      <div class="col"><div class="bd">Modello e versione dei PLC<br>Protocolli esposti<br>Tag
        disponibili e loro significato</div></div>
      <div class="col"><div class="bd">Assetto di rete e segmentazione<br>Contatori e sensori
        già installati<br>Direzione dei flussi</div></div>
      <div class="col"><div class="bd">Disponibilità e continuità del dato<br>Lettura senza
        scrittura verso le macchine<br>Punto di innesto del gestionale</div></div>
    </div>
  </div>

  <div class="body" style="top:592px"><div class="bd">L’approccio è multi-vendor e la
    compatibilità si verifica durante l’audit tecnico, macchina per macchina. Nessun impianto
    è dichiarato compatibile prima di essere stato guardato.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Brownfield e compatibilità', '14')).replace('@FT@', ft('Esiti possibili · nessun impianto specifico')))

# ---------------------------------------------------------------- 15 deployment
P.append('''<div class="slide lt" id="d15_deployment" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Requisiti da chiudere nel solution design.</div>

  <div class="body" style="top:176px">
    <div class="cols" style="gap:56px">
      <div class="col">
        <div class="lbl">Ambiente</div>
        <div class="bd" style="margin-top:16px;line-height:2">Modello di deployment<br>Server
          o macchina virtuale<br>Sistema operativo<br>CPU<br>RAM<br>Storage</div>
      </div>
      <div class="col">
        <div class="lbl">Rete e accessi</div>
        <div class="bd" style="margin-top:16px;line-height:2">Porte<br>Protocolli<br>Direzione
          dei flussi<br>Segmentazione di rete<br>Accesso remoto<br>Autenticazione e ruoli</div>
      </div>
      <div class="col">
        <div class="lbl">Dati e continuità</div>
        <div class="bd" style="margin-top:16px;line-height:2">Aggiornamenti e
          patching<br>Logging<br>Backup<br>Retention<br>Disaster recovery<br>Licenza e fine
          contratto</div>
      </div>
    </div>
  </div>

  <div class="body" style="top:566px">
    <div class="hr"></div>
    <div class="bd" style="padding-top:18px">Diciannove voci, tre gruppi, un solo proprietario
      per gruppo. Nessuna è dichiarata qui: si compilano nella riunione tecnica con l’IT del
      cliente, e finché non sono compilate il dossier non si dichiara pronto per IT.</div>
  </div>
@FT@
</div>'''.replace('@HD@', hd('Deployment e IT/OT', '15')).replace('@FT@', ft('Struttura dei requisiti · valori da compilare in solution design')))

# ---------------------------------------------------------------- 16 sensoristica
P.append('''<div class="slide lt" id="d16_sensoristica" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Dove il dato non c’è, va misurato bene.</div>

  <div class="body" style="top:180px">
    <div class="tb" style="grid-template-columns:300px 1fr 300px">
      <div class="tb__h">Caso</div><div class="tb__h">Che cosa si fa</div><div class="tb__h">Che cosa va deciso</div>
      <div>Il segnale esiste già</div>
      <div>Si legge dal PLC o dal contatore esistente, senza aggiungere hardware</div>
      <div>Perimetro e frequenza di lettura</div>
      <div>Esiste ma non è affidabile</div>
      <div>Si verifica la sorgente e si valuta una misura indipendente di controllo</div>
      <div>Chi valida il dato e con quale criterio</div>
      <div>Il segnale non esiste</div>
      <div>Si installa un contatore o un sensore dedicato al punto di misura</div>
      <div>Precisione, installazione, proprietà, calibrazione</div>
    </div>
  </div>

  <div class="body" style="top:480px">
    <div class="hr"></div>
    <div class="cols" style="padding-top:20px">
      <div class="col"><div class="lbl">Installazione</div><div class="bd" style="margin-top:12px">Se
        richiede un fermo linea, va pianificata con la produzione.</div></div>
      <div class="col"><div class="lbl">Manutenzione</div><div class="bd" style="margin-top:12px">Calibrazione
        e verifica periodica restano in capo a chi possiede lo strumento.</div></div>
      <div class="col"><div class="lbl">Costo</div><div class="bd" style="margin-top:12px">La
        sensoristica è una voce separata dal software e viene quotata a parte.</div></div>
    </div>
  </div>
@FT@
</div>'''.replace('@HD@', hd('Sensoristica', '16')).replace('@FT@', ft('Tre casi · la scelta si fa in audit')))

# ---------------------------------------------------------------- 17 output
P.append('''<div class="slide lt" id="d17_output" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Il dato deve uscire nella forma in cui viene usato.</div>

  <svg class="body" width="1152" height="368" viewBox="0 0 1152 368" style="top:186px"
       role="img" aria-labelledby="u17t u17d">
    <title id="u17t">Dagli output ai destinatari alla decisione</title>
    <desc id="u17d">Ogni forma di uscita ha un destinatario e una decisione che rende
      possibile.</desc>

    <g font-family="Geist" font-size="14" font-weight="500" fill="rgba(10,10,10,.56)">
      <text x="0" y="24">Output</text><text x="430" y="24">Chi lo usa</text>
      <text x="820" y="24">Che decisione abilita</text>
    </g>
    <path d="M0 40 L1152 40" stroke="rgba(10,10,10,.26)"/>
    <g font-family="Geist" font-size="16" fill="#0A0A0A">
      <text x="0" y="80">Dashboard a bordo linea</text><text x="0" y="140">Report programmati</text>
      <text x="0" y="200">Export CSV ed Excel</text><text x="0" y="260">PDF di periodo</text>
      <text x="0" y="320">Integrazioni</text>
    </g>
    <g font-family="Geist" font-size="16" fill="rgba(10,10,10,.74)">
      <text x="430" y="80">Operatori e capi turno</text><text x="430" y="140">Produzione ed energia</text>
      <text x="430" y="200">Continuous improvement</text><text x="430" y="260">Direzione</text>
      <text x="430" y="320">IT e sistemi a valle</text>
    </g>
    <g font-family="Geist" font-size="16" fill="rgba(10,10,10,.74)">
      <text x="820" y="80">Intervenire adesso</text><text x="820" y="140">Confrontare i periodi</text>
      <text x="820" y="200">Analizzare fuori dallo strumento</text><text x="820" y="260">Decidere dove investire</text>
      <text x="820" y="320">Portare il dato dove serve</text>
    </g>
    <g stroke="rgba(10,10,10,.12)">
      <path d="M0 100 L1152 100"/><path d="M0 160 L1152 160"/><path d="M0 220 L1152 220"/>
      <path d="M0 280 L1152 280"/>
    </g>
    <text x="820" y="356" font-family="Geist" font-size="14" fill="rgba(10,10,10,.56)">API ed ERP: possibili, previa verifica tecnica</text>
  </svg>

  <div class="body" style="top:580px"><div class="bd">Un output senza destinatario è un file
    che nessuno apre. Per questo la configurazione parte da chi deve decidere, non
    dall’elenco dei formati disponibili.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Output e integrazioni', '17')).replace('@FT@', ft('Struttura degli output · perimetro da confermare')))

# ---------------------------------------------------------------- 18 pilot
P.append('''<div class="slide lt" id="d18_pilot" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Una linea, quattro deliverable.</div>

  <svg class="body" width="1152" height="356" viewBox="0 0 1152 356" style="top:186px"
       role="img" aria-labelledby="p18t p18d">
    <title id="p18t">Deliverable e fasi del pilot</title>
    <desc id="p18d">Quattro deliverable in sequenza, le fasi che li producono e i criteri con
      cui il pilot si chiude.</desc>

    <g fill="none" stroke="#0A0A0A" stroke-width="1.5">
      <rect x="0" y="30" width="264" height="64"/><rect x="296" y="30" width="264" height="64"/>
      <rect x="592" y="30" width="264" height="64"/>
    </g>
    <rect x="888" y="30" width="264" height="64" fill="#0A0A0A"/>
    <g font-family="Geist" font-size="15" text-anchor="middle">
      <text x="132" y="60" fill="#0A0A0A">Mappa dati</text><text x="132" y="80" fill="#0A0A0A">e segnali</text>
      <text x="428" y="60" fill="#0A0A0A">Baseline produzione</text><text x="428" y="80" fill="#0A0A0A">ed energia</text>
      <text x="724" y="60" fill="#0A0A0A">Prime cause</text><text x="724" y="80" fill="#0A0A0A">e priorità</text>
      <text x="1020" y="70" fill="#FFFFFF">Decisione di scala</text>
    </g>
    <g stroke="#0A0A0A" stroke-width="1.5">
      <path d="M264 62 L284 62"/><path d="M560 62 L580 62"/><path d="M856 62 L876 62"/>
    </g>
    <g fill="#0A0A0A">
      <polygon points="290,62 280,56 280,68"/><polygon points="586,62 576,56 576,68"/>
      <polygon points="882,62 872,56 872,68"/>
    </g>

    <path d="M0 138 L1152 138" stroke="rgba(10,10,10,.12)"/>
    <text x="0" y="172" font-family="Geist" font-size="14" font-weight="500" fill="rgba(10,10,10,.56)">Fasi</text>
    <g font-family="Geist" font-size="16" fill="rgba(10,10,10,.74)">
      <text x="0" y="206">Kickoff · raccolta dati · configurazione · validazione · verifica con gli utenti · chiusura</text>
    </g>
    <path d="M0 240 L1152 240" stroke="rgba(10,10,10,.12)"/>
    <text x="0" y="274" font-family="Geist" font-size="14" font-weight="500" fill="rgba(10,10,10,.56)">Criteri di uscita</text>
    <g font-family="Geist" font-size="16" fill="rgba(10,10,10,.74)">
      <text x="0" y="308">Dati completi</text><text x="260" y="308">Formule approvate</text>
      <text x="560" y="308">Cause validate</text><text x="820" y="308">Report condiviso</text>
      <text x="0" y="340">Proposta di estensione discussa con chi dovrà usarla</text>
    </g>
  </svg>

  <div class="body" style="top:576px"><div class="bd">Il pilot non si chiude con una demo ma
    con una decisione: i quattro deliverable esistono perché quella decisione sia informata.
    Le durate si fissano nel solution design.</div></div>
@FT@
</div>'''.replace('@HD@', hd('Delivery e pilot', '18')).replace('@FT@', ft('Struttura del pilot · durate da confermare')))

# ---------------------------------------------------------------- 19 servizi
P.append('''<div class="slide lt" id="d19_servizi" data-kind="dossier">
@HD@
  <div class="tt tt--sm">Il progetto continua dopo il go-live.</div>

  <div class="body" style="top:180px">
    <div class="tb" style="grid-template-columns:340px 1fr 220px">
      <div class="tb__h">Servizio</div><div class="tb__h">Che cosa produce</div><div class="tb__h">Modello</div>
      <div>Assessment e perimetrazione</div><div>Mappa asset, sorgenti, gap, perimetro e ipotesi economica</div><div>una tantum</div>
      <div>Setup e integrazione</div><div>Connettori, mapping, dashboard, formule, utenti e test</div><div>una tantum</div>
      <div>KPI e formule</div><div>Dizionario KPI, fattori, responsabilità e regole di revisione</div><div>una tantum o periodico</div>
      <div>Performance &amp; Energy Review</div><div>Cause principali, energia fuori produzione, costo per pezzo, priorità</div><div>ricorrente</div>
      <div>Formazione e adozione</div><div>Onboarding, procedure, materiali e sessioni di aggiornamento</div><div>una tantum o ricorrente</div>
      <div>Supporto e scale-up</div><div>Supporto, change request, nuove linee e nuovi siti</div><div>ricorrente o a progetto</div>
    </div>
  </div>

  <div class="body" style="top:534px">
    <div class="hr"></div>
    <div class="cols" style="padding-top:18px">
      <div class="col"><div class="bd">Orari, canali, SLA, manutenzione, aggiornamenti, change
        request ed escalation sono condizioni da formalizzare nella proposta e nel
        contratto.</div></div>
      <div class="col"><div class="bd">Le soluzioni Connect, Insight e Refyn evolvono le
        competenze e le funzionalità sviluppate con MAPST 4.0 e MarEnergy, che continuano a
        essere supportati per l’installato esistente.</div></div>
    </div>
  </div>
@FT@
</div>'''.replace('@HD@', hd('Servizi, supporto e continuità', '19')).replace('@FT@', ft('Condizioni da formalizzare nella proposta')))

# ---------------------------------------------------------------- assemblaggio
if __name__ == '__main__':
    open('dossier_body.html', 'w').write('<div class="doc">\n\n' + '\n\n'.join(P) + '\n\n</div>\n')
    print('pagine:', len(P))
