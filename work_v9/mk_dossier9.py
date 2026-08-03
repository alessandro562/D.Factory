#!/usr/bin/env python3
"""Dossier tecnico V9 · working edition.

Struttura invariata rispetto alla V8: 14 pagine core + 4 annessi. Cambia il
titolo (§8.1, resta «preliminare» finché A1–A3 non sono compilati) ed entrano
i placeholder che il master prescrive pagina per pagina.
"""
import re
import ph

V8 = 'dossier_body_v8.html'


def slides(path):
    s = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'<div class="slide[^>]*id="([^"]+)"[^>]*>', s):
        start = m.start()
        end = s.index('\n</div>', start) + len('\n</div>')
        out[m.group(1)] = s[start:end]
    return out


V = slides(V8)


def band(html, ids):
    for i in ids:
        assert i in ph.BY_ID, f'placeholder non dichiarato: {i}'
    toks = ' '.join('<span class="ph">{{%s}}</span>' % i for i in ids)
    b = ('  <div class="phb" data-ed="working"><b>INPUT APERTI</b>'
         f'<span>{toks}</span></div>')
    return html.replace('\n</div>', '\n' + b + '\n</div>')


out = []
add = out.append

# ===================================================================== 01
# §8.1: finché A1–A3 non sono compilati il documento si chiama preliminare.
s = V['p01_cover']
s = s.replace('''    <div style="font-size:46px;line-height:1.1;letter-spacing:-.03em;font-weight:600">Dossier
      tecnico</div>
    <div class="sub" style="margin-top:22px;max-width:760px">Acquisizione, supervisione e analisi
      integrata di produzione ed energia.</div>''',
'''    <div style="font-size:42px;line-height:1.12;letter-spacing:-.03em;font-weight:600">Dossier tecnico
      preliminare<br>per assessment e solution design</div>
    <div class="sub" style="margin-top:20px;max-width:760px">Acquisizione, supervisione e analisi
      integrata di produzione ed energia.</div>''')
s = s.replace('''      4 · Delivery e supporto — pagine 13–14</div>
  </div>''',
'''      4 · Delivery e supporto — pagine 13–14</div>
    <div class="lbl" style="margin-top:34px">Emesso da</div>
    <div class="sp" style="margin-top:12px;line-height:1.9" data-ed="working">{{PH_COMPANY_LEGAL_NAME}}<br>{{PH_CONTACT_NAME}} · {{PH_CONTACT_EMAIL}}<br>{{PH_VERSION_DATE}}</div>
    <div class="sp" style="margin-top:12px;line-height:1.9" data-ed="client">Denominazione, referente e data di emissione si compilano prima dell’invio.</div>
  </div>''')
s = s.replace('''    <div class="lbl" style="margin-top:30px">Annessi tecnici</div>
    <div class="sp" style="margin-top:14px;line-height:1.9">A1 verifica di compatibilità ·
      A2 dimensionamento<br>A3 sicurezza e governo del dato · A4 dizionario KPI</div>''',
'''    <div class="lbl" style="margin-top:26px">Annessi tecnici</div>
    <div class="sp" style="margin-top:12px;line-height:1.8">A1 compatibilità · A2 dimensionamento<br>A3 sicurezza e governo · A4 dizionario KPI</div>''')
add(band(s, ['PH_COMPANY_LEGAL_NAME', 'PH_CONTACT_NAME', 'PH_CONTACT_EMAIL', 'PH_VERSION_DATE']))

# ===================================================================== 02
add(band(V['p02_overview'], ['PH_DEPLOYMENT_MODEL', 'PH_DATA_OWNERSHIP']))

# ===================================================================== 03
s = V['p03_livelli'].replace(
    '<text x="766" y="226" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)"\n          text-anchor="end">in sviluppo</text>',
    '<text x="766" y="226" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)"\n          text-anchor="end">modulo avanzato</text>')
add(band(s, ['PH_SERVICES_INCLUDED', 'PH_REFYN_PRICING_MODEL']))

# ===================================================================== 04
s = V['p04_connect'].replace('<text x="520" y="278">causale</text>',
                             '<text x="520" y="278">causa associata</text>')
s = s.replace('Eventi e causali, perch&eacute; e per quanto', 'Causa associata, perch&eacute; e per quanto')
add(band(s, ['PH_CONNECT_EXACT_SCOPE', 'PH_CONNECT_REPORTS', 'PH_CONNECT_ALERTS']))

# ===================================================================== 05
add(band(V['p05_insight'], ['PH_INSIGHT_EXACT_SCOPE', 'PH_COST_CALCULATION_METHOD', 'PH_CO2_METHOD']))

# ===================================================================== 06
# La data di rilascio non e' approvata: nella client edition il riquadro esce.
s = V['p06_refyn']
s = s.replace('''    <div class="dev">Modulo avanzato in sviluppo</div>''',
'''    <div class="dev">Modulo avanzato in sviluppo</div>
    <div class="box" style="margin-top:20px" data-ed="working">
      <div class="note">Perimetro del primo rilascio {{PH_REFYN_MVP_SCOPE}}<br>
        Accesso al pilot {{PH_REFYN_PILOT_RULES}}<br>Rilascio previsto {{PH_REFYN_RELEASE_TARGET}}</div>
    </div>''')
s = s.replace('<div class="lbl" style="margin:26px 0 6px">Che cosa porta con sé un’azione</div>',
              '<div class="lbl" style="margin:22px 0 6px">Che cosa porta con sé un’azione</div>')
add(band(s, ['PH_REFYN_MVP_SCOPE', 'PH_REFYN_PILOT_RULES', 'PH_REFYN_RELEASE_TARGET']))

# ===================================================================== 07
add(band(V['p07_sorgenti'], ['PH_STANDARD_SIGNAL_LIST', 'PH_SENSOR_ACCURACY_REQUIREMENTS',
                            'PH_METERING_STANDARDS', 'PH_SENSOR_PRICING_RULE']))

# ===================================================================== 08
s = V['p08_architettura']
s = s.replace('<div class="row"><b>Verso le macchine</b><span>sola lettura</span></div>',
              '<div class="row"><b>Verso le macchine</b><span data-ed="working">{{PH_READ_ONLY_POLICY}}</span>'
              '<span data-ed="client">sola lettura</span></div>')
add(band(s, ['PH_DEPLOYMENT_MODEL', 'PH_SERVER_OWNER', 'PH_SUPPORTED_OS',
             'PH_REQUIRED_PORTS', 'PH_ERP_INTEGRATION_METHODS']))

# ===================================================================== 09
add(band(V['p09_contesto'], ['PH_TIME_SYNC_REQUIREMENT', 'PH_STANDARD_TAG_MODEL',
                             'PH_CAUSE_VALIDATION_PROCESS']))

# ===================================================================== 10
add(band(V['p10_oee'], ['PH_OEE_CALENDAR_RULES', 'PH_IDEAL_CYCLE_TIME_RULE',
                        'PH_GOOD_COUNT_RULE', 'PH_LINE_OEE_AGGREGATION']))

# ===================================================================== 11
s = V['p11_energia'].replace(
    '735 &#247; 227.000 &#215; 1.000, poi &#215; 0,22 &euro;/kWh e &#215; 0,35 kgCO&#8322;e/kWh',
    '735 &#247; 227.000 &#215; 1.000, poi &#215; 0,22 &euro;/kWh · CO&#8322; calcolata o stimata con 0,35 kgCO&#8322;e/kWh')
add(band(s, ['PH_ENERGY_PRICE_SOURCE', 'PH_EMISSION_FACTOR_SOURCE',
             'PH_CO2_METHOD', 'PH_COST_ALLOCATION_RULE']))

# ===================================================================== 12
add(band(V['p12_output'], ['PH_EXPORT_FORMATS', 'PH_API_AVAILABILITY',
                           'PH_REPORT_CATALOGUE', 'PH_ERP_INTEGRATION_METHODS']))

# ===================================================================== 13
add(band(V['p13_pilot'], ['PH_PILOT_DURATION', 'PH_PILOT_SCOPE',
                          'PH_PILOT_SUCCESS_CRITERIA', 'PH_PILOT_PRICE']))

# ===================================================================== 14
s = V['p14_servizi']
s = s.replace('''    <div class="note">Orari, canali, tempi di risposta, manutenzione, aggiornamenti, change
      request ed escalation si formalizzano nella proposta e nel contratto.</div>''',
'''    <div class="note" data-ed="client">Orari, canali, tempi di risposta, manutenzione,
      aggiornamenti, change request ed escalation si formalizzano nella proposta e nel contratto.</div>
    <div class="note" data-ed="working">Orari {{PH_SUPPORT_HOURS}} · canali {{PH_SUPPORT_CHANNELS}} ·
      tempi di risposta {{PH_SLA_RESPONSE_TIMES}} · aggiornamenti {{PH_UPDATE_POLICY}} ·
      supporto remoto {{PH_REMOTE_SUPPORT_POLICY}}</div>''')
s = s.replace('aggiornamenti, change request ed escalation si formalizzano nella proposta e nel contratto.</div>',
              'aggiornamenti, change request ed escalation si formalizzano nella proposta e nel contratto.<br>'
              'Le soluzioni Connect, Insight e Refyn evolvono le competenze e le funzionalità sviluppate con '
              'MAPST 4.0 e MarEnergy, che continuano a essere supportati per l’installato esistente.</div>')
add(band(s, ['PH_SUPPORT_HOURS', 'PH_SLA_RESPONSE_TIMES', 'PH_UPDATE_POLICY',
             'PH_SERVICES_INCLUDED', 'PH_SERVICES_OPTIONAL']))

# ===================================================================== A1
s = V['pa1_compatibilita']
s = s.replace('''    <div><b>Protocollo e versione</b></div>
    <div>Lettura di prova sulla macchina, non su scheda tecnica</div><div>audit tecnico</div>''',
'''    <div><b>Protocollo e versione</b></div>
    <div><span data-ed="working">{{PH_SUPPORTED_PROTOCOLS}} · {{PH_PROTOCOL_VERSIONS}}</span><span data-ed="client">Lettura di prova sulla macchina, non su scheda tecnica</span></div><div>audit tecnico</div>''')
s = s.replace('''    <div><b>Frequenza di lettura sostenibile</b></div>
    <div>Test sul carico reale della rete di stabilimento</div><div>audit tecnico</div>''',
'''    <div><b>Frequenza di lettura sostenibile</b></div>
    <div>Test sul carico reale della rete di stabilimento</div><div>audit tecnico</div>
    <div><b>Gateway e regole firewall</b></div>
    <div><span data-ed="working">{{PH_GATEWAY_REQUIREMENTS}} · {{PH_FIREWALL_RULES}}</span><span data-ed="client">Requisiti concordati con l’IT prima dell’installazione</span></div><div>solution design</div>''')
s = s.replace('style="top:216px;grid-template-columns:380px 532px 240px"',
              'style="top:206px;grid-template-columns:340px 592px 220px"')
s = s.replace('Confronto con la documentazione della macchina e con chi la conduce',
              'Confronto con la documentazione e con chi la conduce')
s = s.replace('Verifica con l’IT del formato e della direzione dello scambio',
              'Verifica con l’IT di formato e direzione dello scambio')
s = s.replace('''<div class="note">Un elenco generico di protocolli non dice se un impianto è leggibile:
      quello che conta è la versione installata su quella macchina e i tag che espone. Per
      questo l’esito di questa verifica è un documento di progetto, non una scheda di prodotto.</div>''',
              '<div class="note">Un elenco generico di protocolli non dice se un impianto è leggibile: conta la versione installata su quella macchina e i tag che espone.</div>')
s = s.replace('<div class="box full" style="top:576px">', '<div class="box full" style="top:602px">')
add(band(s, ['PH_SUPPORTED_PROTOCOLS', 'PH_PROTOCOL_VERSIONS', 'PH_REQUIRED_PORTS',
             'PH_READ_ONLY_POLICY', 'PH_GATEWAY_REQUIREMENTS']))

# ===================================================================== A2
s = V['pa2_sizing']
s = s.replace('<div class="lbl" style="margin-bottom:6px">Che cosa serve per calcolarlo</div>',
              '<div class="lbl" style="margin-bottom:6px" data-ed="client">Che cosa serve per calcolarlo</div>')
for _r in ('Tag', 'Frequenza', 'Conservazione', 'Linee', 'Utenti'):
    s = s.replace(f'<div class="row"><b>{_r}</b>', f'<div class="row" data-ed="client"><b>{_r}</b>')
s = s.replace('''    <div class="box" style="margin-top:24px"><div class="note">Queste cinque risposte arrivano
      dall’audit tecnico e dal vostro IT. Il dimensionamento viene consegnato con la proposta
      di solution design.</div></div>''',
'''    <div class="lbl" style="margin:0 0 6px" data-ed="working">Valori da chiudere</div>
    <div class="row" data-ed="working"><b>CPU minima</b><span>{{PH_MIN_CPU}}</span></div>
    <div class="row" data-ed="working"><b>RAM minima</b><span>{{PH_MIN_RAM}}</span></div>
    <div class="row" data-ed="working"><b>Storage minimo</b><span>{{PH_MIN_STORAGE}}</span></div>
    <div class="row" data-ed="working"><b>Retention</b><span>{{PH_RETENTION_DEFAULT}}</span></div>
    <div class="box" style="margin-top:20px" data-ed="client"><div class="note">Queste cinque
      risposte arrivano dall’audit tecnico e dal vostro IT. Il dimensionamento viene consegnato
      con la proposta di solution design.</div></div>''')
add(band(s, ['PH_MIN_CPU', 'PH_MIN_RAM', 'PH_MIN_STORAGE', 'PH_STORAGE_GROWTH_RULE',
             'PH_HIGH_AVAILABILITY']))

# ===================================================================== A3
s = V['pa3_governo']
s = s.replace('<div class="tb full" style="top:216px;grid-template-columns:300px 592px 260px">',
              '<div class="tb full" style="top:212px;grid-template-columns:264px 396px 300px 192px">')
s = s.replace('<div class="tb__h">Ambito</div><div class="tb__h">Che cosa si definisce</div><div class="tb__h">Chi decide</div>',
              '<div class="tb__h">Ambito</div><div class="tb__h">Che cosa si definisce</div>'
              '<div class="tb__h">Valore</div><div class="tb__h">Chi decide</div>')
for amb, phid in (('Autenticazione', 'PH_AUTHENTICATION_MODEL'),
                  ('Ruoli e permessi', 'PH_ROLE_MODEL'),
                  ('Registro degli accessi', 'PH_AUDIT_LOGGING'),
                  ('Cifratura', 'PH_DATA_ENCRYPTION_AT_REST'),
                  ('Backup e ripristino', 'PH_BACKUP_POLICY'),
                  ('Conservazione', 'PH_RETENTION_DEFAULT'),
                  ('Proprietà del dato', 'PH_DATA_OWNERSHIP'),
                  ('Fine contratto', 'PH_END_OF_CONTRACT_DATA')):
    s = re.sub(r'(<div><b>%s</b></div><div>[^<]*</div>)(<div>)' % re.escape(amb),
               r'\1<div><span data-ed="working" style="font-family:var(--mono);font-size:13px">'
               r'{{%s}}</span><span data-ed="client">solution design</span></div>\2' % phid, s)
add(band(s, ['PH_PATCHING_POLICY', 'PH_RPO', 'PH_RTO', 'PH_LICENSE_RIGHTS',
             'PH_DATA_EXPORT_AT_EXIT']))

# ===================================================================== A4
s = V['pa4_kpi']
s = s.replace('style="position:absolute;left:64px;width:1152px;top:206px;\n       grid-template-columns:196px 372px 118px 296px 170px"',
              'style="position:absolute;left:64px;width:1152px;top:202px;\n       grid-template-columns:180px 340px 108px 260px 128px 136px"')
s = s.replace('<div class="tb__h">Sorgente</div><div class="tb__h">Frequenza</div>',
              '<div class="tb__h">Sorgente</div><div class="tb__h">Frequenza</div><div class="tb__h">Owner</div>')
s = s.replace('pezzi &#215; tempo ciclo ideale &#247; tempo di marcia',
              'pezzi &#215; tempo ciclo ideale &#247; marcia')
for _a, _b in (('stati macchina, calendario', 'stati, calendario'),
               ('conteggi, cadenza nominale', 'conteggi, cadenza'),
               ('eventi, parametri economici', 'eventi, parametri')):
    s = s.replace(_a, _b)
s = re.sub(r'(<div>(?:turno|evento)</div>)',
           r'\1<div><span data-ed="working" style="font-family:var(--mono);font-size:13px">'
           r'{{PH_KPI_OWNER}}</span><span data-ed="client">da nominare</span></div>', s)
s = s.replace('<div class="box" style="position:absolute;left:64px;width:1152px;top:566px">',
              '<div class="box" style="position:absolute;left:64px;width:1152px;top:556px">')
add(band(s, ['PH_KPI_OWNER', 'PH_KPI_VERSION', 'PH_KPI_APPROVAL_DATE', 'PH_OEE_DEFINITION_OWNER']))


body = '<div class="doc">\n' + '\n\n\n'.join(out) + '\n\n</div>\n'
open('dossier9_body.html', 'w', encoding='utf-8').write(body)

used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', body))
undeclared = used - set(ph.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
ntok = len(re.findall(r'\{\{PH_', body))
print(f'dossier9_body.html · {len(out)} canvas · {ntok} token · {len(used)} distinti')
