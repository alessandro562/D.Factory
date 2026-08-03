#!/usr/bin/env python3
"""Dossier tecnico V9.2 · delta sul corpo master V9.1.

Ogni sostituzione corrisponde a una riga della tabella §5 di
DFactory_V9_2_Audit.md. Il titolo resta «preliminare» finché G4 è aperto.
"""
import re
import gates
import ph91

s = open('dossier91_master.html', encoding='utf-8').read()
G4_OK = gates.STATO['G4'] == 'APPROVED'


def sub(old, new, n=1):
    global s
    assert s.count(old) >= n, 'stringa non trovata: %r' % old[:90]
    s = s.replace(old, new, n)


# =====================================================================
# P01 · il blocco di emissione mostrava quattro token in fila: adesso mostra
#       il nome del campo, e l'etichetta dice che cosa manca (§8.3)
# =====================================================================
sub('<div class="sp" style="margin-top:12px;line-height:1.9" data-ed="working">'
    '{{PH_COMPANY_LEGAL_NAME}}<br>{{PH_CONTACT_NAME}} · {{PH_CONTACT_EMAIL}}<br>'
    '{{PH_VERSION_DATE}}</div>',
    '<div class="sp" style="margin-top:12px;line-height:1.9" data-ed="working">'
    'Denominazione {{PH_COMPANY_LEGAL_NAME}}<br>Referente {{PH_CONTACT_NAME}}<br>'
    'Email {{PH_CONTACT_EMAIL}}<br>Data di emissione {{PH_VERSION_DATE}}</div>')

# =====================================================================
# P02 · §15 · «cosa non presuppone» in tre voci, e la nota che chiude.
#       L'elenco del solution design se ne va: è per intero su P08, e P02
#       era la pagina a 132 parole.
# =====================================================================
sub('<div class="lbl">Che cosa non richiede</div>\n'
    '      <div class="sp">Non presuppone la sostituzione delle macchine. Eventuali adeguamenti ai segnali vengono verificati in audit.</div>',
    '<div class="lbl">Che cosa non presuppone</div>\n'
    '      <div class="sp">Sostituzione delle macchine<br>Rifacimento completo dei PLC<br>Cloud obbligatorio</div>')
sub('<div class="lbl" style="margin-bottom:8px">Definito nel solution design</div>\n'
    '    <div class="sp">Ambiente e sizing · protocolli e porte · autenticazione ·\n'
    '      backup e retention · integrazioni · supporto remoto.</div>',
    '<div class="note">Perimetro e requisiti vengono definiti nel solution design. '
    'Eventuali adeguamenti ai segnali vengono verificati in audit.</div>')
sub('>Lo schema descrive il metodo: perimetro, punti di misura e anagrafiche si definiscono nel solution design.</text>',
    '>Lo schema descrive il metodo di funzionamento, non un impianto specifico.</text>')

# =====================================================================
# P08 · §15 · i due blocchi passano alle voci del master
# =====================================================================
sub('<div class="row"><b>Verso le macchine</b><span data-ed="working">{{PH_READ_ONLY_POLICY}}</span>'
    '<span data-ed="client">sola lettura, in configurazione standard</span></div>\n'
    '    <div class="row"><b>Sensoristica</b><span>solo dove manca il dato</span></div>\n'
    '    <div class="row"><b>Impianto esistente</b><span>nessuna sostituzione</span></div>',
    '<div class="row"><b>Flusso di acquisizione</b><span data-ed="working">{{PH_READ_ONLY_POLICY}}</span>'
    '<span data-ed="client">sola lettura, standard</span></div>\n'
    '    <div class="row"><b>Applicazione</b><span>stati, cause, indicatori</span></div>\n'
    '    <div class="row"><b>Output</b><span>viste, report, export</span></div>\n'
    '    <div class="row"><b>Logica di calcolo</b><span>dizionario KPI</span></div>')
sub('<div class="sp">— Collocazione dell&rsquo;ambiente<br>— Segmentazione e regole di rete<br>'
    '— Autenticazione e ruoli<br>— Orizzonte di conservazione<br>— Formato e frequenza degli export</div>',
    '<div class="sp">— Ambiente<br>— Rete<br>— Autenticazione<br>— Backup<br>— Supporto remoto</div>')

# =====================================================================
# P09 · §15 · la riga di decisione del master, accanto alla validazione
# =====================================================================
sub('<div class="note">La causa è proposta sulla base dello stato e validata da chi la conosce. '
    'Senza queste chiavi il dato grezzo resta un numero: non si attribuisce una perdita a un formato, '
    'n&eacute; un consumo a uno stato.</div>',
    '<div class="note">Il dato diventa leggibile soltanto quando condivide tempo e contesto. '
    'La causa è proposta sulla base dello stato e validata da chi la conosce.</div>')

# =====================================================================
# P10 · §15 · headline con il punto fermo, e la nota che dichiara il perimetro
# =====================================================================
sub('L&rsquo;OEE dice quanto, le perdite dicono dove.',
    'L&rsquo;OEE dice quanto. Le perdite dicono dove.')
sub('<div class="note" style="margin-top:20px">La prima causa vale il 43% del costo: &egrave; da l&igrave; che parte la priorit&agrave;.</div>',
    '<div class="note" style="margin-top:20px">La prima causa vale il 43% del costo: &egrave; da l&igrave; che parte la priorit&agrave;. '
    'Perimetro, calendario, tempo ciclo ideale e conteggio dei pezzi conformi si dichiarano prima del calcolo.</div>')

# =====================================================================
# P12 · §15 · manca la riga API. Cinque righe diventano sei, il tetto del §14.4
# =====================================================================
sub('<div><b>PDF di periodo</b></div><div>Direzione</div><div>Decidere dove investire</div>',
    '<div><b>PDF di periodo</b></div><div>Direzione</div><div>Decidere dove investire</div>\n'
    '    <div><b>API</b></div><div>IT e sistemi a valle</div><div>Alimentare un altro sistema</div>')
sub('<div><b>Integrazioni</b></div><div>IT e sistemi a valle</div><div>Portare il dato dove serve</div>',
    '<div><b>Integrazioni</b></div><div>Continuous improvement</div><div>Portare il dato dove serve</div>')
sub('formato e frequenza si chiudono nel solution design.</div>',
    'formato e frequenza si chiudono nel solution design. Disponibilità delle API da confermare.</div>')
sub('<div class="box full" style="top:520px">', '<div class="box full" style="top:566px">')

# =====================================================================
# P14 · la nota di working elencava cinque token in fila. Gli stessi cinque
#       sono nel pannello in fondo alla pagina, che parla al registro: la
#       nota se ne va invece di diventare cinque etichette identiche.
# =====================================================================
sub('    <div class="note" data-ed="working">Orari {{PH_SUPPORT_HOURS}} · canali {{PH_SUPPORT_CHANNELS}} ·\n'
    '      tempi di risposta {{PH_SLA_RESPONSE_TIMES}} · aggiornamenti {{PH_UPDATE_POLICY}} ·\n'
    '      supporto remoto {{PH_REMOTE_SUPPORT_POLICY}}</div>\n', '')
sub('<span class="ph">{{PH_SUPPORT_HOURS}}</span> <span class="ph">{{PH_SLA_RESPONSE_TIMES}}</span> '
    '<span class="ph">{{PH_UPDATE_POLICY}}</span>',
    '<span class="ph">{{PH_SUPPORT_HOURS}}</span> <span class="ph">{{PH_SUPPORT_CHANNELS}}</span> '
    '<span class="ph">{{PH_SLA_RESPONSE_TIMES}}</span> <span class="ph">{{PH_UPDATE_POLICY}}</span> '
    '<span class="ph">{{PH_REMOTE_SUPPORT_POLICY}}</span>')

# il pannello di p14 arrivava a sette token e andava a capo sul piede pagina:
# i servizi sono già censiti su P03 e nell'appendice A2 del deck
sub(' <span class="ph">{{PH_SERVICES_INCLUDED}}</span> <span class="ph">{{PH_SERVICES_OPTIONAL}}</span></span></div>\n</div>\n',
    '</span></div>\n</div>\n')

# =====================================================================
# A1 · §16 · Elemento · Cosa si verifica · Esito · Owner, otto campi
# =====================================================================
A1_RIGHE = [
    ('PLC', 'Costruttore, modello e stato del controllore', None, 'Manutenzione'),
    ('Protocollo', 'Protocollo esposto e interfaccia disponibile', 'PH_SUPPORTED_PROTOCOLS', 'Audit tecnico'),
    ('Versione', 'Versione installata su quella macchina', 'PH_PROTOCOL_VERSIONS', 'Audit tecnico'),
    ('Accesso', 'Tag leggibili e frequenza sostenibile', 'PH_REQUIRED_PORTS', 'Audit tecnico'),
    ('Gateway', 'Segmento di rete, gateway e regole firewall', 'PH_GATEWAY_REQUIREMENTS', 'IT del cliente'),
    ('Contatore', 'Punti di misura dell’energia già presenti', 'PH_METERING_STANDARDS', 'Audit tecnico'),
    ('ERP', 'Punto di innesto, formato e direzione', 'PH_ERP_INTEGRATION_METHODS', 'IT del cliente'),
    ('Lettura e scrittura', 'Direzione del flusso verso le macchine', 'PH_READ_ONLY_POLICY', 'Solution design'),
]


def a1_riga(nome, cosa, tok, owner):
    if tok:
        esito = ('<span data-ed="working" style="font-family:var(--mono);font-size:13px">'
                 '{{%s}}</span><span data-ed="client">da verificare</span>' % tok)
    else:
        esito = 'da verificare'
    return (f'    <div><b>{nome}</b></div><div>{cosa}</div>'
            f'<div>{esito}</div><div>{owner}</div>')


A1_START = s.index('<div class="tb full" style="top:206px;grid-template-columns:340px 592px 220px">')
A1_END = s.index('</div>\n\n  <div class="box full" style="top:602px">', A1_START)
s = s[:A1_START] + (
    '<div class="tb full tb--tight" style="top:206px;grid-template-columns:220px 470px 250px 212px">\n'
    '    <div class="tb__h">Elemento</div><div class="tb__h">Cosa si verifica</div>'
    '<div class="tb__h">Esito</div><div class="tb__h">Owner</div>\n\n'
    + '\n'.join(a1_riga(*r) for r in A1_RIGHE) + '\n  ') + s[A1_END:]
sub('<div class="tt tt--sm">La compatibilità si verifica sull’impianto reale.\n'
    '    <div class="sub" style="margin-top:14px">Che cosa viene controllato macchina per macchina,\n'
    '      con quale metodo e in che momento.</div>',
    '<div class="tt tt--sm">La compatibilità si verifica sull’impianto reale.\n'
    '    <div class="sub" style="margin-top:14px">Otto elementi, il metodo di verifica e chi\n'
    '      risponde di ciascuno.</div>')
sub('<div class="note">Un elenco generico di protocolli non dice se un impianto è leggibile: conta la versione installata su quella macchina e i tag che espone.</div>',
    '<div class="note">Esiti ammessi: supportato · condizionato · da verificare · da aggiungere. '
    'Prima dell’audit ogni riga è da verificare: un elenco generico di protocolli non dice se un '
    'impianto è leggibile.</div>')

# =====================================================================
# A2 · §16 · la tabella delle tre fasce entra nella sola working edition.
#      La client preliminare continua a mostrare il metodo, non i valori.
# =====================================================================
FASCE = [('Piccola', 'fino a 500', '1', '1 s', '12 mesi'),
         ('Media', '500 – 2.000', '2 – 4', '1 s', '24 mesi'),
         ('Grande', 'oltre 2.000', '5 e oltre', '≤ 1 s', '36 mesi')]
CELLE_IT = [('PH_MIN_CPU', 'da definire'), ('PH_MIN_RAM', 'da definire'),
            ('PH_MIN_STORAGE', 'da definire')]


def fascia(nome, tag, linee, freq, ret):
    celle = ''.join('<div data-placeholder="%s">%s</div>' % c for c in CELLE_IT)
    return (f'    <div><b>{nome}</b></div><div>{tag}</div><div>{linee}</div>'
            f'<div>{freq}</div><div data-placeholder="PH_RETENTION_DEFAULT">{ret}</div>{celle}')


TAB_FASCE = (
    '  <div class="tb full" data-ed="working" style="top:206px;'
    'grid-template-columns:150px 160px 130px 120px 140px 150px 150px 152px">\n'
    '    <div class="tb__h">Fascia</div><div class="tb__h">Tag</div><div class="tb__h">Linee</div>'
    '<div class="tb__h">Frequenza</div><div class="tb__h">Retention</div>'
    '<div class="tb__h">CPU</div><div class="tb__h">RAM</div><div class="tb__h">Storage</div>\n\n'
    + '\n'.join(fascia(*f) for f in FASCE) + '\n  </div>\n\n'
    '  <div class="box full" data-ed="working" style="top:406px"><div class="note">'
    'Tag, linee, frequenza e retention sono ipotesi di fascia, da confermare con l’IT. '
    'CPU, RAM e storage restano input aperti: si chiudono con l’audit tecnico e non prima. '
    'La client edition preliminare mostra il metodo, non questi valori.</div></div>\n\n'
    '  <div class="full" data-ed="working" style="top:492px">\n'
    '    <div class="lbl" style="margin-bottom:14px">Le cinque grandezze che determinano la fascia</div>\n'
    '    <div class="tb" style="grid-template-columns:repeat(5,1fr)">\n'
    '      <div><b>Tag</b><br>quanti segnali per linea</div>\n'
    '      <div><b>Frequenza</b><br>ogni quanto si campiona</div>\n'
    '      <div><b>Conservazione</b><br>per quanto tempo</div>\n'
    '      <div><b>Linee</b><br>oggi e in prospettiva</div>\n'
    '      <div><b>Utenti</b><br>quanti in contemporanea</div>\n'
    '    </div>\n  </div>\n\n')

# il metodo, cioè quello che vede il cliente, viene racchiuso in un blocco client
A2_START = s.index('  <svg class="diag" style="top:216px" width="800" height="380" viewBox="0 0 800 380"')
A2_END = s.index('  <div class="ft"><span class="wm">D<i>.</i>Factory</span><span>Annesso A2', A2_START)
s = (s[:A2_START] + TAB_FASCE + '  <div data-ed="client">\n' + s[A2_START:A2_END]
     + '  </div>\n\n' + s[A2_END:])
# dentro il blocco client i data-ed interni non servono più
for tok, _ in CELLE_IT:
    sub('    <div class="row" data-ed="working"><b>%s</b><span>{{%s}}</span></div>\n'
        % ({'PH_MIN_CPU': 'CPU minima', 'PH_MIN_RAM': 'RAM minima',
            'PH_MIN_STORAGE': 'Storage minimo'}[tok], tok), '')
sub('    <div class="lbl" style="margin:0 0 6px" data-ed="working">Valori da chiudere</div>\n', '')
sub('    <div class="row" data-ed="working"><b>Retention</b><span>{{PH_RETENTION_DEFAULT}}</span></div>\n', '')

# =====================================================================
# A3 · §16 · dodici ambiti in otto righe, colonna «Modello», stato del §16
# =====================================================================
sub('<div class="tb full" style="top:212px;grid-template-columns:264px 396px 300px 192px">',
    '<div class="tb full tb--tight" style="top:212px;grid-template-columns:290px 370px 300px 192px">')
sub('<div class="tb__h">Ambito</div><div class="tb__h">Che cosa si definisce</div>',
    '<div class="tb__h">Ambito</div><div class="tb__h">Modello</div>')
sub('<div>Chi vede, chi configura, chi modifica le formule</div>',
    '<div>Chi vede, chi configura, chi modifica</div>')
sub('<div>Che cosa viene registrato e per quanto tempo</div>',
    '<div>Eventi registrati e per quanto tempo</div>')
sub('<div>Dati in transito e dati a riposo</div>', '<div>In transito e a riposo</div>')
sub('<div class="sub" style="margin-top:14px">Otto ambiti che si chiudono nel solution design\n'
    '      insieme al vostro IT.</div>',
    '<div class="sub" style="margin-top:14px">Dodici punti in otto ambiti, da chiudere con il\n'
    '      vostro IT.</div>')
sub('<div><b>Autenticazione</b></div><div>Metodo e integrazione con la directory aziendale</div>',
    '<div><b>Autenticazione e identità</b></div><div>Metodo, password e directory aziendale</div>')
sub('<div><b>Backup e ripristino</b></div><div>Frequenza, ritenzione e prova di ripristino</div>',
    '<div><b>Backup e conservazione</b></div><div>Frequenza, prova di ripristino e orizzonte</div>')
sub('<div><b>Conservazione</b></div><div>Orizzonte per le serie storiche e per gli eventi</div>'
    '<div><span data-ed="working" style="font-family:var(--mono);font-size:13px">{{PH_RETENTION_DEFAULT}}</span>'
    '<span data-ed="client">solution design</span></div><div>Operations e IT</div>',
    '<div><b>Aggiornamenti e accesso remoto</b></div><div>Patch, versioni e accesso da remoto</div>'
    '<div><span data-ed="working" style="font-family:var(--mono);font-size:13px">{{PH_PATCHING_POLICY}}</span>'
    '<span data-ed="client">solution design</span></div><div>IT del cliente</div>')
sub('<div><b>Proprietà del dato</b></div><div>Titolarità, esportabilità e formati</div>',
    '<div><b>Proprietà e licenza</b></div><div>Titolarità, diritti d’uso ed export</div>')
sub('<span>Annesso A3 · decisioni di progetto, non parametri fissi del prodotto</span>',
    '<span>Annesso A3 · per la raccolta dei requisiti</span>'
    if not G4_OK else '<span>Annesso A3 · specifica concordata</span>')
sub('<span class="ph">{{PH_PATCHING_POLICY}}</span> <span class="ph">{{PH_RPO}}</span>',
    '<span class="ph">{{PH_RETENTION_DEFAULT}}</span> <span class="ph">{{PH_RPO}}</span>')

# =====================================================================
# A4 · §16 · versione e data di approvazione entrano come colonne
# =====================================================================
sub('<div class="tb" style="position:absolute;left:64px;width:1152px;top:202px;\n'
    '       grid-template-columns:180px 340px 108px 260px 128px 136px">\n'
    '    <div class="tb__h">Indicatore</div><div class="tb__h">Formula</div><div class="tb__h">Unit&agrave;</div>\n'
    '    <div class="tb__h">Sorgente</div><div class="tb__h">Frequenza</div><div class="tb__h">Owner</div>',
    '<div class="tb tb--tight" style="position:absolute;left:64px;width:1152px;top:202px;\n'
    '       grid-template-columns:148px 266px 118px 148px 110px 150px 98px 114px">\n'
    '    <div class="tb__h">Indicatore</div><div class="tb__h">Formula</div><div class="tb__h">Unit&agrave;</div>\n'
    '    <div class="tb__h">Sorgente</div><div class="tb__h">Frequenza</div><div class="tb__h">Owner</div>\n'
    '    <div class="tb__h">Versione</div><div class="tb__h">Approvato</div>')
sub('<div><span data-ed="working" style="font-family:var(--mono);font-size:13px">{{PH_KPI_OWNER}}</span>'
    '<span data-ed="client">da nominare</span></div>',
    '<div><span data-ed="working" style="font-family:var(--mono);font-size:13px">{{PH_KPI_OWNER}}</span>'
    '<span data-ed="client">da nominare</span></div>'
    '<div data-placeholder="PH_KPI_VERSION">in bozza</div>'
    '<div data-placeholder="PH_KPI_APPROVAL_DATE">da approvare</div>', 6)
sub('<div class="sub" style="margin-top:14px">Dizionario KPI: formula, unit&agrave;, sorgente e frequenza.</div>',
    '<div class="sub" style="margin-top:14px">Formula, unit&agrave;, sorgente, frequenza, owner e stato\n'
    '      di approvazione.</div>')

open('dossier92_master.html', 'w', encoding='utf-8').write(s)
used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', s))
undeclared = used - set(ph91.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
n = len(re.findall(r'<div[^>]*class="slide', s))
print(f'dossier92_master.html · {n} canvas · {len(used)} placeholder distinti · G4 {gates.STATO["G4"]}')
