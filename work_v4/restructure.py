#!/usr/bin/env python3
"""Ristruttura il dossier: 18 -> 23 pagine.

Sdoppia le quattro pagine piu' dense (brownfield, deployment, delivery, supporto),
aggiunge lo schema dei punti di acquisizione e la pagina di specifiche IT voce per
voce, applica la fascia ridotta alle pagine tabellari e rinumera tutto.
"""
import re

SRC = 'work_v4/dossier_body.html'
body = open(SRC, encoding='utf-8').read()

# ---- 1. spezza il file in blocchi pagina indicizzati per id -------------------
parts = re.split(r'(?=<!-- =+ \d+ ·)', body)
head = parts[0]
pages = {}
order_old = []
for blk in parts[1:]:
    m = re.search(r'<div class="slide[^"]*" id="([^"]+)"', blk)
    pages[m.group(1)] = blk.rstrip().rstrip('</div>').rstrip() if False else blk
    order_old.append(m.group(1))
assert len(order_old) == 18, order_old

# la coda "</div>" del .doc sta attaccata all'ultima pagina: staccala
tail = '\n</div>\n'
pages[order_old[-1]] = pages[order_old[-1]].rsplit('</div>', 1)[0]


def band(section, question, answer='', extra='', slim=False):
    cls = 'band band--slim' if slim else 'band'
    a = f'    <div class="band__a">{answer}</div>\n' if answer else ''
    return (f'  <div class="{cls}">\n'
            f'    <div class="band__sec">{section}</div>\n'
            f'    <div class="band__q">{question}</div>\n'
            f'{a}    <div class="spacer"></div>\n{extra}'
            f'    <div class="spacer"></div>\n'
            f'    <div class="band__ft"><span class="wm">d<i>.</i>factory</span>'
            f'<span class="pg">PG</span></div>\n  </div>\n')


def openblk(label, items):
    return ('    <div class="open">\n'
            f'      <div class="open__l">{label}</div>\n'
            f'      <div class="open__i">{items}</div>\n'
            '    </div>\n')


# ---- 2. pagine nuove ---------------------------------------------------------

NEW_ACQUISIZIONE = '''<!-- ============ 04 · PUNTI DI ACQUISIZIONE — chiara ============ -->
<div class="slide lt" id="d04_acquisizione" data-kind="dossier">
''' + band('Sezione 1 · prodotto', 'Dove il dato viene preso, fisicamente.',
           'Nessun hardware D.Factory entra a bordo linea. Si legge da quello che il tuo '
           'impianto gia’ espone, e si aggiunge misura solo dove non c’e’.',
           openblk('Da verificare in audit',
                   'Quali tag ogni PLC espone davvero<br>Copertura dei contatori per asset<br>'
                   'Punti dove serve aggiungere misura')) + '''
  <div class="field">
    <div class="field__hd"><span>Linea di confezionamento</span><span>Punti di prelievo del dato</span></div>
    <svg width="864" height="576" viewBox="0 0 864 576" style="margin:26px 40px"
         role="img" aria-labelledby="d4t d4d">
      <title id="d4t">Punti di acquisizione del dato su una linea di confezionamento</title>
      <desc id="d4d">Su ogni macchina il dato di stato arriva dal PLC via Ethernet. I pezzi
        arrivano dai sensori di conta gia' presenti. L'energia arriva dai contatori di quadro,
        dove esistono, o da pinze amperometriche aggiunte in audit.</desc>

      <!-- silhouette di linea: cinque macchine e i polmoni fra una e l'altra -->
      <g fill="none" stroke="#0A0A0A" stroke-width="1.8">
        <rect x="0" y="150" width="122" height="96"/><rect x="180" y="150" width="122" height="96"/>
        <rect x="360" y="150" width="122" height="96"/><rect x="540" y="150" width="122" height="96"/>
        <rect x="720" y="150" width="122" height="96"/>
      </g>
      <g font-family="Geist" font-size="15" fill="#0A0A0A" text-anchor="middle">
        <text x="61" y="204">Filler</text><text x="241" y="204">Capper</text>
        <text x="421" y="204">Labeler</text><text x="601" y="204">Case packer</text>
        <text x="781" y="204">Palletizer</text>
      </g>
      <!-- polmoni: il nastro fra due macchine -->
      <g stroke="rgba(10,10,10,.42)" stroke-width="1.4" stroke-dasharray="4 4">
        <line x1="122" y1="198" x2="180" y2="198"/><line x1="302" y1="198" x2="360" y2="198"/>
        <line x1="482" y1="198" x2="540" y2="198"/><line x1="662" y1="198" x2="720" y2="198"/>
      </g>
      <text x="151" y="232" font-family="Geist Mono" font-size="11.5"
            fill="rgba(10,10,10,.42)" text-anchor="middle" letter-spacing="1">POLMONE</text>

      <!-- prelievo 1: stato dal PLC, sopra la linea -->
      <line x1="0" y1="96" x2="864" y2="96" stroke="rgba(10,10,10,.26)"/>
      <g stroke="#0A0A0A" stroke-width="1.4">
        <line x1="61" y1="150" x2="61" y2="96"/><line x1="241" y1="150" x2="241" y2="96"/>
        <line x1="421" y1="150" x2="421" y2="96"/><line x1="601" y1="150" x2="601" y2="96"/>
        <line x1="781" y1="150" x2="781" y2="96"/>
      </g>
      <g fill="#0A0A0A">
        <rect x="54" y="89" width="14" height="14"/><rect x="234" y="89" width="14" height="14"/>
        <rect x="414" y="89" width="14" height="14"/><rect x="594" y="89" width="14" height="14"/>
        <rect x="774" y="89" width="14" height="14"/>
      </g>
      <text x="0" y="74" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)"
            letter-spacing="1.3">STATO MACCHINA · DAL PLC, VIA ETHERNET, IN SOLA LETTURA</text>

      <!-- prelievo 2: pezzi dal sensore di conta, in uscita -->
      <circle cx="852" cy="198" r="9" fill="#E6E011"/>
      <line x1="842" y1="198" x2="864" y2="198" stroke="#E6E011" stroke-width="2"/>
      <text x="864" y="252" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.64)"
            text-anchor="end" letter-spacing="1.2">PEZZI · SENSORE DI CONTA</text>

      <!-- prelievo 3: energia dal quadro, sotto la linea -->
      <line x1="0" y1="330" x2="864" y2="330" stroke="rgba(10,10,10,.26)"/>
      <g stroke="#0A0A0A" stroke-width="1.4">
        <line x1="61" y1="246" x2="61" y2="330"/><line x1="421" y1="246" x2="421" y2="330"/>
        <line x1="781" y1="246" x2="781" y2="330"/>
      </g>
      <g fill="none" stroke="#0A0A0A" stroke-width="1.8">
        <circle cx="61" cy="330" r="8"/><circle cx="421" cy="330" r="8"/><circle cx="781" cy="330"  r="8"/>
      </g>
      <text x="0" y="360" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)"
            letter-spacing="1.3">ENERGIA · CONTATORE DI QUADRO O PINZA AMPEROMETRICA</text>

      <line x1="0" y1="418" x2="864" y2="418" stroke="rgba(10,10,10,.12)"/>
      <g font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.3">
        <text x="0" y="452">GIA’ PRESENTE</text><text x="330" y="452">DA VERIFICARE</text>
        <text x="640" y="452">EVENTUALMENTE DA AGGIUNGERE</text>
      </g>
      <g font-family="Geist" font-size="15" fill="#0A0A0A">
        <text x="0" y="484">PLC e rete OT</text><text x="0" y="510">Sensori di conta</text>
        <text x="330" y="484">Tag effettivamente esposti</text><text x="330" y="510">Contatori per asset</text>
        <text x="640" y="484">Misura di energia dove manca</text>
        <text x="640" y="510">Sensori di conta dove manca</text>
      </g>
      <text x="0" y="558" font-family="Geist" font-size="14" fill="rgba(10,10,10,.64)">Lo schema e’ la struttura tipo di una linea di confezionamento. La mappa della tua linea si costruisce in audit.</text>
    </svg>
  </div>
</div>

'''

NEW_SPEC_IT = '''<!-- ============ 16 · SPECIFICHE IT — chiara ============ -->
<div class="slide lt" id="d16_specifiche_it" data-kind="dossier">
''' + band('Sezione 3 · integrazione', 'Le voci che il tuo IT deve approvare.',
           'Nessuna di queste voci si dichiara prima di averla concordata. Qui c’e’ '
           'l’elenco completo, con chi la chiude e quando.', slim=True) + '''
  <div class="field field--wide">
    <div class="field__hd"><span>Specifiche IT</span><span>Voce · stato · chi decide · quando si chiude</span></div>
    <div class="field__b" style="padding:24px 40px">
      <div class="mx" style="grid-template-columns:1fr 210px 130px 180px;font-size:13.5px">
        <div class="mx__h">Voce</div><div class="mx__h">Stato oggi</div>
        <div class="mx__h">Chi decide</div><div class="mx__h">Quando si chiude</div>

        <div>Server e sistema operativo</div><div>PC industriale Linux, fornito dal cliente</div>
        <div>Cliente</div><div>Definito</div>
        <div>Sizing del server</div><div>Dipende da linee e frequenza</div>
        <div>Congiunto</div><div>Solution design</div>
        <div>Protocolli e modelli PLC</div><div>Multi-protocollo, per modello e versione</div>
        <div>D.Factory</div><div>Audit</div>
        <div>Porte e direzione dei flussi</div><div>Solo lettura OT verso IT</div>
        <div>IT cliente</div><div>Solution design</div>
        <div>Autenticazione e ruoli</div><div>Da concordare con le policy interne</div>
        <div>IT cliente</div><div>Solution design</div>
        <div>Backup, retention e patching</div><div>Da concordare con le policy interne</div>
        <div>IT cliente</div><div>Solution design</div>
        <div>Logging e audit trail</div><div>Da concordare</div>
        <div>Congiunto</div><div>Solution design</div>
        <div>Accesso remoto per il supporto</div><div>Da concordare, disattivabile</div>
        <div>IT cliente</div><div>Contratto</div>
        <div>Licenza a fine contratto</div><div>Distinta dalla proprieta’ del dato</div>
        <div>Legale</div><div>Contratto</div>
      </div>
      <p class="bd" style="margin-top:16px;font-size:13.5px">Lo storico resta sul tuo server ed
        e’ esportabile in ogni momento. I diritti d’uso del software sono un’altra cosa e si
        definiscono in contratto: dato tuo non significa software per sempre.</p>
    </div>
  </div>
</div>

'''

# ---- 3. split ----------------------------------------------------------------

def split_page(pid, new_pages):
    """Sostituisce una pagina con N pagine nuove."""
    for np in new_pages:
        pages[np[0]] = np[1]
    del pages[pid]


# --- brownfield: due pagine ---
BF_A = '''<!-- ============ 13 · BROWNFIELD · MACCHINE — chiara ============ -->
<div class="slide lt" id="d13_brownfield_macchine" data-kind="dossier">
''' + band('Sezione 3 · integrazione', 'Funziona sul brownfield che hai gia’.',
           'Brownfield: impianti gia’ in esercizio, con macchine di costruttori e '
           'generazioni diverse. Compatibilita’ verificata in audit, non a catalogo.',
           slim=True) + '''
  <div class="field field--wide">
    <div class="field__hd"><span>Macchine, PLC e misura</span><span>1 di 2</span></div>
    <div class="field__b" style="padding:26px 40px">
      <div class="mx" style="grid-template-columns:210px 1fr 200px">
        <div class="mx__h">Categoria</div><div class="mx__h">Come entra nel modello</div><div class="mx__h">Stato</div>

        <div>Macchine PackML</div><div>17 stati nativi, letti dal PLC</div>
        <div><span class="st st--ok">Supportato</span></div>
        <div>Macchine non-PackML</div><div>Modello ridotto a due stati: in marcia e non in marcia</div>
        <div><span class="st st--ok">Supportato</span></div>
        <div>PLC e PC industriali</div><div>Lettura via Ethernet, multi-vendor</div>
        <div><span class="st st--inf">Dipende dal modello</span></div>
        <div>Contatori energia</div><div>Cinque vettori, dove esiste la strumentazione</div>
        <div><span class="st st--inf">Dipende dalla copertura</span></div>
        <div>Macchine legacy</div><div>Solo se espongono uno stato leggibile dal PLC</div>
        <div><span class="st st--ver">Verifica in audit</span></div>
      </div>
      <p class="bd" style="margin-top:20px;font-size:14px">A bordo linea non entra hardware
        proprietario D.Factory. Servono pero’ un server e, dove manca la misura, sensori.</p>
    </div>
  </div>
</div>

'''

BF_B = '''<!-- ============ 14 · BROWNFIELD · RETE — chiara ============ -->
<div class="slide lt" id="d14_brownfield_rete" data-kind="dossier">
''' + band('Sezione 3 · integrazione', 'Rete, gestionale e tag mapping.',
           'Il tag mapping e’ lavoro nostro ed e’ la parte che di solito blocca i progetti.',
           openblk('Quello che non diciamo',
                   'Che funzioni con ogni marca e ogni protocollo. Multi-vendor non significa '
                   'compatibile con tutto.')) + '''
  <div class="field">
    <div class="field__hd"><span>Rete e sistemi</span><span>2 di 2</span></div>
    <div class="field__b" style="padding:26px 40px">
      <div class="mx" style="grid-template-columns:180px 1fr 176px">
        <div class="mx__h">Categoria</div><div class="mx__h">Come entra nel modello</div><div class="mx__h">Stato</div>

        <div>Reti OT e IT</div><div>Segmentate, flussi in sola lettura verso l’alto</div>
        <div><span class="st st--inf">Dipende dalla rete</span></div>
        <div>Gestionale</div><div>Ordini e anagrafiche in sola lettura, tramite livello intermedio</div>
        <div><span class="st st--opt">Caso per caso</span></div>
        <div>Protocolli</div><div>Connettori per modello e versione</div>
        <div><span class="st st--ver">Verifica in audit</span></div>
        <div>Scrittura verso l’ERP</div><div>Oggi la lettura e’ solo in ingresso</div>
        <div><span class="st st--road">Sul progetto</span></div>
      </div>
      <div class="hr" style="margin:24px 0 18px"></div>
      <div class="lbl">Cosa serve dal tuo lato</div>
      <div style="font-size:15px;line-height:2;margin-top:10px">
        Elenco dei PLC per linea, con marca e modello<br>
        Schemi di rete OT e IT, anche parziali<br>
        Modalita’ di accesso al gestionale</div>
    </div>
  </div>
</div>

'''

DEPLOY = '''<!-- ============ 15 · DEPLOYMENT · ZONE DI RETE — chiara ============ -->
<div class="slide lt" id="d15_deployment" data-kind="dossier">
''' + band('Sezione 3 · integrazione', 'Cosa chiede al tuo IT.',
           'Il dato di produzione resta in fabbrica, su un server tuo. Le tre zone restano '
           'separate e i flussi fra loro vanno in una direzione sola.',
           '    <div class="note">Le voci che il tuo IT deve approvare, una per una,\n'
           '      sono nella pagina seguente.</div>\n') + '''
  <div class="field">
    <div class="field__hd"><span>Zone di rete</span><span>On-premise · PC industriale Linux del cliente</span></div>
    <svg width="864" height="560" viewBox="0 0 864 560" style="margin:36px 40px"
         role="img" aria-labelledby="d15t d15d">
      <title id="d15t">Segmentazione delle zone di rete</title>
      <desc id="d15d">Rete OT, livello intermedio e rete IT restano separati. I flussi fra le
        zone sono solo in lettura e non esiste un percorso verso internet dalla rete di linea.</desc>

      <rect x="0" y="0" width="864" height="132" fill="#F2F3EF"/>
      <text x="24" y="36" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.4">ZONA 1 · RETE OT</text>
      <text x="24" y="72" font-family="Geist" font-size="20" fill="#0A0A0A">PLC di linea · sensori · contatori energia</text>
      <text x="24" y="102" font-family="Geist" font-size="15" fill="rgba(10,10,10,.64)">Nessun flusso in scrittura verso le macchine</text>

      <path d="M432 132 L432 172" stroke="#E6E011" stroke-width="2.4"/>
      <polygon points="432,180 424,169 440,169" fill="#E6E011"/>
      <text x="452" y="164" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.64)" letter-spacing="1.2">SOLO LETTURA</text>

      <rect x="0" y="188" width="864" height="132" fill="#F2F3EF"/>
      <text x="24" y="224" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.42)" letter-spacing="1.4">ZONA 2 · LIVELLO INTERMEDIO</text>
      <text x="24" y="260" font-family="Geist" font-size="20" fill="#0A0A0A">Connettori · tag mapping · normalizzazione</text>
      <text x="24" y="290" font-family="Geist" font-size="15" fill="rgba(10,10,10,.64)">A carico D.Factory</text>

      <path d="M432 320 L432 360" stroke="#E6E011" stroke-width="2.4"/>
      <polygon points="432,368 424,357 440,357" fill="#E6E011"/>
      <text x="452" y="352" font-family="Geist Mono" font-size="12" fill="rgba(10,10,10,.64)" letter-spacing="1.2">SOLO LETTURA</text>

      <rect x="0" y="376" width="864" height="132" fill="#0A0A0A"/>
      <text x="24" y="412" font-family="Geist Mono" font-size="12" fill="rgba(255,255,255,.44)" letter-spacing="1.4">ZONA 3 · RETE IT · SERVER DEL CLIENTE</text>
      <text x="24" y="448" font-family="Geist" font-size="20" fill="#fff">Applicazione · database · modello dati</text>
      <text x="24" y="478" font-family="Geist" font-size="15" fill="rgba(255,255,255,.72)">Postazioni utente e bordo linea</text>

      <text x="0" y="546" font-family="Geist" font-size="15" fill="rgba(10,10,10,.64)">Nessun flusso verso internet dalla rete di linea, nel perimetro concordato con il tuo IT.</text>
    </svg>
  </div>
</div>

'''

MILESTONE = '''<!-- ============ 19 · MILESTONE E TEMPI — chiara ============ -->
<div class="slide lt" id="d19_milestone" data-kind="dossier">
''' + band('Sezione 4 · delivery', 'Dal primo segnale al go-live.',
           'I tempi dipendono da due cose sole: quanta sensoristica manca e quando si aprono '
           'le tue finestre di fermo. Il calendario reale si scrive in audit.',
           openblk('Da definire nel solution design',
                   'Ore a carico del cliente per l’avvio<br>Calendario delle finestre di fermo')) + '''
  <div class="field">
    <div class="field__hd"><span>Le cinque milestone</span><span>Da non confondere fra loro</span></div>
    <div class="field__b" style="padding:40px">
      <svg width="864" height="380" viewBox="0 0 864 380" role="img" aria-labelledby="d19t d19d">
        <title id="d19t">Le cinque milestone del progetto</title>
        <desc id="d19d">First signal, first usable data, pilot live, operational go-live e
          scale-up sono cinque momenti distinti, con condizioni diverse.</desc>
        <line x1="10" y1="30" x2="10" y2="330" stroke="rgba(10,10,10,.26)"/>
        <g fill="rgba(10,10,10,.82)">
          <circle cx="10" cy="30" r="8"/><circle cx="10" cy="105" r="8"/>
          <circle cx="10" cy="180" r="8"/><circle cx="10" cy="255" r="8"/></g>
        <circle cx="10" cy="330" r="8" fill="#E6E011"/>
        <g font-family="Geist" font-size="20" fill="#0A0A0A">
          <text x="44" y="24">First signal</text><text x="44" y="99">First usable data</text>
          <text x="44" y="174">Pilot live</text><text x="44" y="249">Operational go-live</text>
          <text x="44" y="324">Scale-up</text></g>
        <g font-family="Geist" font-size="15" fill="rgba(10,10,10,.64)">
          <text x="44" y="50">Primo segnale acquisito da una macchina</text>
          <text x="44" y="125">Primo dato contestualizzato e verificato con te</text>
          <text x="44" y="200">Una linea con viste e KPI concordati</text>
          <text x="44" y="275">Utenti formati, formule validate, supporto attivo</text>
          <text x="44" y="350">Estensione ad altre linee o ad altri siti</text></g>
      </svg>
      <div class="hr" style="margin:22px 0 16px"></div>
      <p class="bd" style="font-size:15px">Su una linea gia’ strumentata il primo segnale puo’
        arrivare in un paio di giorni. Il go-live operativo ha un altro calendario: le due cose
        non vanno confuse in offerta.</p>
    </div>
  </div>
</div>

'''

RACI = '''<!-- ============ 20 · RESPONSABILITA’ — chiara ============ -->
<div class="slide lt" id="d20_raci" data-kind="dossier">
''' + band('Sezione 4 · delivery', 'Chi fa cosa.',
           'La riga che genera piu’ sorprese e’ la seconda: i sensori li installa il tuo '
           'personale tecnico o una terza parte, non noi.', slim=True) + '''
  <div class="field field--wide">
    <div class="field__hd"><span>Matrice di responsabilita’</span><span>R esegue · A approva · C consultato</span></div>
    <div class="field__b" style="padding:30px 40px">
      <div class="mx" style="grid-template-columns:1fr 140px 140px 150px">
        <div class="mx__h">Attivita’</div><div class="mx__h">D.Factory</div>
        <div class="mx__h">Cliente</div><div class="mx__h">Terza parte</div>
        <div>Accessi di rete e autorizzazioni</div><div>C</div><div>R</div><div>—</div>
        <div>Installazione sensori e contatori</div><div>C</div><div>A</div><div>R</div>
        <div>Tag mapping e connettori</div><div>R</div><div>C</div><div>—</div>
        <div>Definizione e validazione KPI</div><div>R</div><div>A</div><div>—</div>
        <div>Formazione degli utenti</div><div>R</div><div>C</div><div>—</div>
        <div>Go-live operativo</div><div>R</div><div>A</div><div>—</div>
        <div>Supporto in esercizio</div><div>R</div><div>C</div><div>—</div>
      </div>
      <p class="note" style="margin-top:14px">— non coinvolto</p>
    </div>
  </div>
</div>

'''

SUPPORTO = '''<!-- ============ 22 · SUPPORTO IN ESERCIZIO — chiara ============ -->
<div class="slide lt" id="d22_supporto" data-kind="dossier">
''' + band('Sezione 4 · delivery', 'Cosa succede dopo il go-live.',
           'Nessun livello di servizio si dichiara prima di averlo concordato: un SLA scritto '
           'a caso e’ peggio che non averlo.') + '''
  <div class="field">
    <div class="field__hd"><span>Supporto</span><span>Voce · stato · quando si chiude</span></div>
    <div class="field__b" style="padding:30px 40px">
      <div class="mx" style="grid-template-columns:1fr 230px 170px">
        <div class="mx__h">Voce</div><div class="mx__h">Stato oggi</div><div class="mx__h">Quando si chiude</div>
        <div>Livelli di servizio</div><div>Da concordare</div><div>Contratto</div>
        <div>Orari, severita’ e canali</div><div>Da concordare</div><div>Contratto</div>
        <div>Manutenzione software e patching</div><div>Da concordare con l’IT</div><div>Solution design</div>
        <div>Accesso remoto</div><div>Da concordare, disattivabile</div><div>Contratto</div>
        <div>Change request</div><div>Modalita’ definite in contratto</div><div>Contratto</div>
      </div>
      <div class="hr" style="margin:26px 0 18px"></div>
      <div class="lbl">Referente</div>
      <div style="font-size:19px;margin-top:8px">Pablo Degl’Innocenti</div>
      <div class="bd" style="font-size:14px">pablo.deglinnocenti@marchianisrl.com</div>
    </div>
  </div>
</div>

'''

CHECKLIST = '''<!-- ============ 23 · CHECKLIST PER L’AUDIT — chiara ============ -->
<div class="slide lt" id="d23_checklist" data-kind="dossier">
''' + band('Sezione 4 · delivery', 'Cosa portare in sala.',
           'Con questo materiale l’audit si chiude in una sessione. Senza, servono due giri.',
           '    <div class="note">Documento gemello: sales deck, il percorso dall’audit\n'
           '      alla scala.</div>\n', slim=True) + '''
  <div class="field field--wide">
    <div class="field__hd"><span>Checklist per l’audit</span><span>Documenti · decisioni · persone</span></div>
    <div class="field__b" style="padding:30px 40px">
      <div style="display:flex;gap:56px">
        <div style="flex:1">
          <div class="lbl">Documenti</div>
          <div style="font-size:15.5px;line-height:2.3;margin-top:14px">
            Elenco dei PLC per linea, con marca e modello<br>
            Schemi di rete OT e IT, anche parziali<br>
            Elenco dei contatori energia e posizione<br>
            Sensori gia’ presenti a bordo linea<br>
            Turni e calendario di produzione<br>
            Finestre di fermo disponibili nell’anno</div>
        </div>
        <div style="flex:1">
          <div class="lbl">Decisioni e persone</div>
          <div style="font-size:15.5px;line-height:2.3;margin-top:14px">
            Referenti IT e OT che possono decidere<br>
            Le formule OEE che usi oggi, se ne usi<br>
            Come conti i pezzi buoni<br>
            Requisiti di reportistica, se ce ne sono<br>
            Modalita’ di accesso al gestionale<br>
            Chi usera’ le viste, per ruolo</div>
        </div>
      </div>
    </div>
  </div>
</div>
'''

split_page('d12_brownfield', [('d13_brownfield_macchine', BF_A), ('d14_brownfield_rete', BF_B)])
split_page('d13_deployment_security', [('d15_deployment', DEPLOY), ('d16_specifiche_it', NEW_SPEC_IT)])
split_page('d16_delivery_raci', [('d19_milestone', MILESTONE), ('d20_raci', RACI)])
split_page('d18_supporto_audit', [('d22_supporto', SUPPORTO), ('d23_checklist', CHECKLIST)])
pages['d04_acquisizione'] = NEW_ACQUISIZIONE

# ---- 4. nuovo ordine ---------------------------------------------------------
ORDER = [
    'd01_cover', 'd02_architettura_prodotto', 'd03_architettura_tecnica',
    'd04_acquisizione', 'd04_capability',
    'd05_supervisione', 'd06_oee_fermi', 'd07_velocita_qualita', 'd08_multi_impianto',
    'd09_distribuzione_energia', 'd10_costo_co2_stato',
    'd11_metodo_misura', 'd13_brownfield_macchine', 'd14_brownfield_rete',
    'd15_deployment', 'd16_specifiche_it', 'd14_sensori', 'd15_output_integrazioni',
    'd19_milestone', 'd20_raci', 'd17_criteri_pilot', 'd22_supporto', 'd23_checklist',
]
assert set(ORDER) == set(pages), (set(ORDER) ^ set(pages))
N = len(ORDER)

# ---- 5. rinumerazione e fascia ridotta ---------------------------------------
SLIM = {'d04_capability', 'd13_brownfield_macchine', 'd16_specifiche_it', 'd14_sensori',
        'd15_output_integrazioni', 'd20_raci', 'd17_criteri_pilot', 'd23_checklist'}

out = [head.rstrip() + '\n\n']
for i, pid in enumerate(ORDER, 1):
    blk = pages[pid]
    blk = re.sub(r'<span class="pg">[^<]*</span>',
                 f'<span class="pg">{i:02d} / {N}</span>', blk)
    blk = blk.replace('>PG<', f'>{i:02d} / {N}<')
    if pid == 'd01_cover':
        blk = re.sub(r'<span class="pg">[^<]*</span>',
                     f'<span class="pg">01 / {N} · D Factory S.r.l. · gruppo Clevertech</span>', blk)
    if pid in SLIM and 'band--slim' not in blk:
        blk = blk.replace('<div class="band">', '<div class="band band--slim">', 1)
        blk = blk.replace('<div class="field">', '<div class="field field--wide">', 1)
    out.append(blk)
out.append('\n</div>\n')

open(SRC, 'w', encoding='utf-8').write(''.join(out))
print(f'dossier ristrutturato: {N} pagine')
for i, pid in enumerate(ORDER, 1):
    print(f'  {i:02d}  {pid}{"  [slim]" if pid in SLIM else ""}')
