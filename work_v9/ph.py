#!/usr/bin/env python3
"""Registro master dei placeholder V9.

Unica fonte di verita': da qui esce il .md del registro, da qui il build
verifica che ogni {{PH_...}} usato negli HTML sia dichiarato, e da qui la
client edition sa che cosa nascondere.

Campi: id, descrizione, owner, fonte richiesta, priorita', documento,
canvas, comportamento working, comportamento client, stato, ultima verifica.
Stati ammessi: OPEN · IN REVIEW · APPROVED · REJECTED · NOT NEEDED.
"""

VERIFICA = '2026-08-03'

# owner sintetici
COM, DIR, TEC, IT, LEG, MKT = ('Commerciale', 'Direzione', 'Tecnico',
                               'Tecnico + IT', 'Legale', 'Marketing')

# (id, descrizione, owner, fonte richiesta, prio, doc, canvas, working, client)
R = []


def g(gruppo, righe):
    for r in righe:
        R.append({'gruppo': gruppo, 'id': r[0], 'desc': r[1], 'owner': r[2],
                  'fonte': r[3], 'prio': r[4], 'doc': r[5], 'canvas': r[6],
                  'working': r[7], 'client': r[8], 'stato': 'OPEN',
                  'verifica': VERIFICA})


D, S, B = 'deck', 'dossier', 'entrambi'
VIS = 'visibile'
NASC = 'blocco nascosto'
OMESSO = 'elemento omesso'
PAG = 'canvas escluso'
PRUD = 'testo prudente'

g('5.1 Identità e contatti', [
 ('PH_COMPANY_LEGAL_NAME', 'Denominazione legale corretta', DIR, 'visura o carta intestata', 'P0', B, 'deck 13 · dossier 01', VIS, NASC),
 ('PH_COMPANY_BRAND_FORM', 'Grafia ufficiale del brand', MKT, 'manuale di identità', 'P0', B, 'tutti i canvas', VIS, 'resta la grafia D.Factory in uso'),
 ('PH_COMPANY_VAT', 'Partita IVA', DIR, 'visura', 'P1', B, 'piede legale', VIS, OMESSO),
 ('PH_COMPANY_ADDRESS', 'Sede legale o operativa', DIR, 'visura', 'P1', B, 'deck 13 · dossier 01', VIS, OMESSO),
 ('PH_COMPANY_WEBSITE', 'URL ufficiale', MKT, 'conferma marketing', 'P1', B, 'deck 13', VIS, OMESSO),
 ('PH_CONTACT_NAME', 'Referente commerciale', COM, 'nomina interna', 'P0', D, 'deck 13', VIS, PAG),
 ('PH_CONTACT_ROLE', 'Ruolo del referente', COM, 'nomina interna', 'P0', D, 'deck 13', VIS, PAG),
 ('PH_CONTACT_EMAIL', 'Email ufficiale', COM, 'nomina interna', 'P0', B, 'deck 13 · dossier 01', VIS, PAG),
 ('PH_CONTACT_PHONE', 'Numero di telefono', COM, 'nomina interna', 'P1', D, 'deck 13', VIS, OMESSO),
 ('PH_GROUP_RELATIONSHIP', 'Relazione con Gruppo Clevertech', DIR, 'conferma societaria', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_LEGAL_FOOTER', 'Formula legale del piede', LEG, 'ufficio legale', 'P1', B, 'piede di tutti i canvas', VIS, OMESSO),
 ('PH_VERSION_DATE', 'Data di emissione del documento', DIR, 'processo interno', 'P1', S, 'dossier 01', VIS, OMESSO),
])

g('5.2 Prova aziendale', [
 ('PH_COMPANY_FOUNDING_YEAR', 'Anno di avvio', DIR, 'visura', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_COMPANY_YEARS_EXPERIENCE', 'Anni di esperienza', DIR, 'conferma direzione', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_ACTIVE_CLIENTS', 'Numero clienti attivi', DIR, 'CRM validato', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_ACTIVE_SITES', 'Numero stabilimenti', TEC, 'installato validato', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_ACTIVE_LINES', 'Numero linee collegate', TEC, 'installato validato', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_ACTIVE_MACHINES', 'Numero macchine collegate', TEC, 'installato validato', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_PROJECTS_COMPLETED', 'Numero progetti o casi conclusi', DIR, 'CRM validato', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_SECTORS_APPROVED', 'Settori autorizzati alla citazione', LEG, 'autorizzazione clienti', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_RETENTION_METRIC', 'Retention o tasso di rinnovo', DIR, 'contratti', 'P2', D, 'deck 10', VIS, OMESSO),
 ('PH_TEAM_SIZE', 'Dimensione del team dedicato', DIR, 'organigramma', 'P2', D, 'deck 10', VIS, OMESSO),
 ('PH_GROUP_PROOF', 'Evidenza del gruppo industriale', DIR, 'conferma societaria', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_PARTNERSHIP_SIEMENS_APPROVAL', 'Claim di partnership autorizzato', LEG, 'lettera del partner', 'P1', D, 'deck 10', VIS, OMESSO),
 ('PH_SAP_INTEGRATION_PROOF', 'Fonte verificabile per il claim ERP', TEC, 'progetto di riferimento', 'P1', B, 'deck A4 · dossier 12', VIS, OMESSO),
 ('PH_PATENT_BOX_APPROVAL', 'Claim Patent Box autorizzato', LEG, 'parere fiscale', 'P2', D, 'deck 10', VIS, OMESSO),
])

CASE_W = 'visibile nella slide 14'
CASE_C = 'slide 14 esclusa'
g('5.3 Caso cliente · identificativi', [
 ('PH_CASE_CLIENT_DISPLAY_NAME', 'Nome cliente o forma anonima', LEG, 'autorizzazione scritta', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_CLIENT_LEGAL_NAME', 'Nome legale, uso interno', LEG, 'contratto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_CLIENT_SECTOR', 'Settore', COM, 'scheda cliente', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_CLIENT_SITE', 'Stabilimento o paese', COM, 'scheda cliente', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_LINE_TYPE', 'Tipo di linea', TEC, 'scheda impianto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_PROCESS', 'Processo osservato', TEC, 'scheda impianto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_CONFIDENTIALITY', 'Pubblico, anonimo o confidenziale', LEG, 'autorizzazione scritta', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_APPROVAL_STATUS', 'Stato autorizzazione alla pubblicazione', LEG, 'autorizzazione scritta', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_APPROVAL_OWNER', 'Chi ha autorizzato', LEG, 'autorizzazione scritta', 'P0', D, 'deck 14', CASE_W, CASE_C),
])
g('5.3 Caso cliente · problema e contesto', [
 ('PH_CASE_INITIAL_PROBLEM', 'Problema iniziale', COM, 'verbale di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_BUSINESS_IMPACT', 'Impatto percepito dal cliente', COM, 'verbale di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_BASELINE_PERIOD', 'Periodo della baseline', TEC, 'dati di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_BASELINE_DATA', 'Dati della baseline', TEC, 'dati di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_DATA_SOURCES', 'PLC, contatori, gestionale, sensori', TEC, 'mappa dati di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_SCOPE', 'Macchine, linea, sito', TEC, 'perimetro di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_PRECONDITIONS', 'Prerequisiti presenti', TEC, 'audit di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_GAPS', 'Gap di dati o di misura', TEC, 'audit di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
])
g('5.3 Caso cliente · intervento', [
 ('PH_CASE_SOLUTION_MODULE', 'Connect, Insight o Refyn', COM, 'contratto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_IMPLEMENTATION_SCOPE', 'Perimetro implementato', TEC, 'documento di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_INTERVENTION', 'Attività svolte', TEC, 'documento di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_ADDED_SENSORS', 'Sensori o contatori aggiunti', TEC, 'documento di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_ERP_INTEGRATION', 'Integrazione con il gestionale', TEC, 'documento di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_TIME_TO_FIRST_SIGNAL', 'Tempo al primo segnale', TEC, 'diario di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_TIME_TO_USABLE_DATA', 'Tempo al dato utilizzabile', TEC, 'diario di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_PILOT_DURATION', 'Durata del pilot', COM, 'contratto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_USERS', 'Utenti coinvolti', COM, 'documento di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
])
_res = []
for i, prio in ((1, 'P0'), (2, 'P0'), (3, 'P1')):
    _res += [(f'PH_CASE_RESULT_{i}_LABEL', f'Nome del risultato {i}', TEC, 'misura di progetto', prio, D, 'deck 14', CASE_W, CASE_C),
             (f'PH_CASE_RESULT_{i}_BASELINE', f'Baseline del risultato {i}', TEC, 'misura di progetto', prio, D, 'deck 14', CASE_W, CASE_C),
             (f'PH_CASE_RESULT_{i}_AFTER', f'Valore dopo, risultato {i}', TEC, 'misura di progetto', prio, D, 'deck 14', CASE_W, CASE_C),
             (f'PH_CASE_RESULT_{i}_UNIT', f'Unità di misura, risultato {i}', TEC, 'misura di progetto', prio, D, 'deck 14', CASE_W, CASE_C),
             (f'PH_CASE_RESULT_{i}_METHOD', f'Metodo di misura, risultato {i}', TEC, 'metodo di progetto', prio, D, 'deck 14', CASE_W, CASE_C)]
g('5.3 Caso cliente · risultati', _res + [
 ('PH_CASE_RESULT_PERIOD', 'Periodo osservato', TEC, 'misura di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_ANNUALIZED_VALUE', 'Valore annualizzato', COM, 'calcolo verificato', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_PAYBACK', 'Payback verificato', COM, 'calcolo verificato', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_CONFIDENCE_NOTE', 'Limiti e attendibilità della misura', TEC, 'metodo di progetto', 'P0', D, 'deck 14', CASE_W, CASE_C),
])
g('5.3 Caso cliente · testimonial e asset', [
 ('PH_CASE_QUOTE', 'Citazione del cliente', LEG, 'autorizzazione scritta', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_QUOTE_AUTHOR', 'Autore della citazione', LEG, 'autorizzazione scritta', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_QUOTE_ROLE', 'Ruolo dell’autore', LEG, 'autorizzazione scritta', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_QUOTE_APPROVAL', 'Autorizzazione alla citazione', LEG, 'autorizzazione scritta', 'P0', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_LOGO_ASSET', 'Logo cliente autorizzato', LEG, 'autorizzazione scritta', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_SCREENSHOT_ASSET', 'Screenshot reale del caso', TEC, 'ambiente di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_PHOTO_ASSET', 'Foto reale del caso', MKT, 'autorizzazione scritta', 'P1', D, 'deck 14', CASE_W, CASE_C),
 ('PH_CASE_DIAGRAM_ASSET', 'Schema anonimizzato del caso', TEC, 'documento di progetto', 'P1', D, 'deck 14', CASE_W, CASE_C),
])

g('5.4 Audit e pilot', [
 ('PH_AUDIT_NAME', 'Nome commerciale del primo passo', COM, 'decisione commerciale', 'P0', D, 'deck 12 · 13 · A3', VIS, PRUD),
 ('PH_AUDIT_DURATION', 'Durata dell’audit', COM, 'decisione commerciale', 'P0', D, 'deck 09 · 12', VIS, OMESSO),
 ('PH_AUDIT_PRICE', 'Prezzo dell’audit', COM, 'listino approvato', 'P0', D, 'deck 12 · A3', VIS, PAG),
 ('PH_AUDIT_CREDIT_POLICY', 'Accredito dell’audit sul progetto', COM, 'decisione commerciale', 'P1', D, 'deck A3', VIS, OMESSO),
 ('PH_AUDIT_PARTICIPANTS', 'Partecipanti richiesti', COM, 'metodo di delivery', 'P0', D, 'deck 13', VIS, 'resta la formulazione V8, già verificata'),
 ('PH_AUDIT_CLIENT_HOURS', 'Ore richieste al cliente', COM, 'metodo di delivery', 'P1', D, 'deck 13', VIS, OMESSO),
 ('PH_AUDIT_INPUTS', 'Materiali richiesti al cliente', TEC, 'metodo di delivery', 'P0', D, 'deck 13', VIS, 'resta la formulazione V8, già verificata'),
 ('PH_AUDIT_DELIVERABLES', 'Output dell’audit', TEC, 'metodo di delivery', 'P0', D, 'deck 13', VIS, 'resta la formulazione V8, già verificata'),
 ('PH_AUDIT_VALIDITY', 'Validità dell’offerta', COM, 'decisione commerciale', 'P1', D, 'deck A3', VIS, OMESSO),
 ('PH_PILOT_DURATION', 'Durata del pilot', COM, 'decisione commerciale', 'P0', B, 'deck 12 · dossier 13', VIS, OMESSO),
 ('PH_PILOT_SCOPE', 'Perimetro del pilot', TEC, 'metodo di delivery', 'P0', B, 'deck 12 · dossier 13', VIS, 'resta «una linea», già dichiarato'),
 ('PH_PILOT_SUCCESS_CRITERIA', 'Criteri di successo', TEC, 'metodo di delivery', 'P0', B, 'deck 12 · dossier 13', VIS, 'restano i criteri di uscita V8'),
 ('PH_PILOT_EXIT_CRITERIA', 'Criteri di uscita', TEC, 'metodo di delivery', 'P0', B, 'deck 12 · dossier 13', VIS, 'restano i criteri di uscita V8'),
 ('PH_PILOT_PRICE', 'Prezzo del pilot', COM, 'listino approvato', 'P0', D, 'deck 12 · A3', VIS, PAG),
 ('PH_PILOT_CONVERSION_POLICY', 'Conversione del pilot a contratto', COM, 'decisione commerciale', 'P1', D, 'deck 12', VIS, OMESSO),
 ('PH_PILOT_REVERSIBILITY', 'Reversibilità del pilot', COM, 'decisione commerciale', 'P1', D, 'deck 12', VIS, OMESSO),
])

g('5.5 Pricing e contratto', [
 ('PH_SITE_BASE_FEE', 'Canone base per sito', COM, 'listino approvato', 'P0', D, 'deck 12 · A3', VIS, PAG),
 ('PH_SETUP_FIRST_LINE', 'Setup della prima linea', COM, 'listino approvato', 'P0', D, 'deck A3', VIS, PAG),
 ('PH_CONNECT_ANNUAL_FEE', 'Canone Connect', COM, 'listino approvato', 'P0', D, 'deck 12 · A3', VIS, PAG),
 ('PH_INSIGHT_ANNUAL_FEE', 'Canone Insight', COM, 'listino approvato', 'P0', D, 'deck 12 · A3', VIS, PAG),
 ('PH_REFYN_PRICING_MODEL', 'Modello economico di Refyn', COM, 'decisione commerciale', 'P0', B, 'deck 09 · 12 · A1 · A3 · dossier 03', VIS, PAG),
 ('PH_ADDITIONAL_LINE_FEE', 'Canone per linee successive', COM, 'listino approvato', 'P0', D, 'deck A3', VIS, PAG),
 ('PH_SENSOR_PRICING_RULE', 'Regola di quotazione della sensoristica', COM, 'decisione commerciale', 'P1', B, 'deck A3 · dossier 07', VIS, OMESSO),
 ('PH_SERVICES_INCLUDED', 'Servizi compresi nell’avvio', COM, 'decisione commerciale', 'P0', B, 'deck 08 · A1 · A2 · dossier 03 · 14', VIS, OMESSO),
 ('PH_SERVICES_OPTIONAL', 'Servizi opzionali', COM, 'decisione commerciale', 'P0', B, 'deck 08 · A2 · dossier 14', VIS, OMESSO),
 ('PH_PERFORMANCE_REVIEW_FEE', 'Prezzo della performance review', COM, 'listino approvato', 'P1', D, 'deck A3', VIS, PAG),
 ('PH_ENERGY_REVIEW_FEE', 'Prezzo della energy review', COM, 'listino approvato', 'P1', D, 'deck A3', VIS, PAG),
 ('PH_PREMIUM_SUPPORT_FEE', 'Prezzo del supporto premium', COM, 'listino approvato', 'P1', D, 'deck A3', VIS, PAG),
 ('PH_CONTRACT_TERM', 'Durata contrattuale', COM, 'contratto tipo', 'P0', D, 'deck 09 · A3', VIS, OMESSO),
 ('PH_RENEWAL_TERMS', 'Condizioni di rinnovo', COM, 'contratto tipo', 'P0', D, 'deck A3', VIS, PAG),
 ('PH_TERMINATION_TERMS', 'Condizioni di recesso', LEG, 'contratto tipo', 'P1', D, 'deck A3', VIS, PAG),
 ('PH_PAYMENT_TERMS', 'Termini di pagamento', COM, 'contratto tipo', 'P1', D, 'deck A3', VIS, PAG),
 ('PH_PRICE_VALIDITY', 'Validità dei prezzi', COM, 'listino approvato', 'P1', D, 'deck A3', VIS, PAG),
 ('PH_INDEXATION', 'Indicizzazione', COM, 'contratto tipo', 'P2', D, 'deck A3', VIS, PAG),
])

g('5.6 Supporto e SLA', [
 ('PH_SUPPORT_HOURS', 'Orari del supporto', COM, 'contratto tipo', 'P0', B, 'deck A2 · dossier 14', VIS, OMESSO),
 ('PH_SUPPORT_CHANNELS', 'Canali del supporto', COM, 'contratto tipo', 'P1', S, 'dossier 14', VIS, OMESSO),
 ('PH_SLA_SEVERITY_LEVELS', 'Livelli di severità', TEC, 'contratto tipo', 'P0', S, 'dossier 14', VIS, OMESSO),
 ('PH_SLA_RESPONSE_TIMES', 'Tempi di risposta', COM, 'contratto tipo', 'P0', S, 'dossier 14', VIS, OMESSO),
 ('PH_SLA_RESOLUTION_TARGETS', 'Obiettivi di risoluzione', COM, 'contratto tipo', 'P1', S, 'dossier 14', VIS, OMESSO),
 ('PH_ESCALATION_PROCESS', 'Processo di escalation', TEC, 'contratto tipo', 'P1', S, 'dossier 14', VIS, OMESSO),
 ('PH_MAINTENANCE_WINDOWS', 'Finestre di manutenzione', TEC, 'contratto tipo', 'P1', S, 'dossier 14', VIS, OMESSO),
 ('PH_UPDATE_POLICY', 'Politica di aggiornamento', TEC, 'contratto tipo', 'P0', S, 'dossier 14', VIS, OMESSO),
 ('PH_CHANGE_REQUEST_POLICY', 'Politica delle change request', COM, 'contratto tipo', 'P1', S, 'dossier 14', VIS, OMESSO),
 ('PH_REMOTE_SUPPORT_POLICY', 'Politica di supporto remoto', IT, 'contratto tipo', 'P0', S, 'dossier 14 · A3', VIS, OMESSO),
])

g('5.7 Deployment e infrastruttura', [
 ('PH_DEPLOYMENT_MODEL', 'On-premise, VM o altro', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 02 · 08 · A2', VIS, PRUD),
 ('PH_SERVER_OWNER', 'Proprietà dell’ambiente', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08 · A2', VIS, PRUD),
 ('PH_SUPPORTED_OS', 'Sistemi operativi supportati', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08 · A2', VIS, OMESSO),
 ('PH_MIN_CPU', 'CPU minima', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A2', VIS, OMESSO),
 ('PH_MIN_RAM', 'RAM minima', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A2', VIS, OMESSO),
 ('PH_MIN_STORAGE', 'Storage minimo', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A2', VIS, OMESSO),
 ('PH_STORAGE_GROWTH_RULE', 'Regola di crescita dello storage', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A2', VIS, OMESSO),
 ('PH_RETENTION_DEFAULT', 'Retention di default', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A2 · A3', VIS, OMESSO),
 ('PH_HIGH_AVAILABILITY', 'Alta disponibilità', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A2', VIS, OMESSO),
 ('PH_VIRTUALIZATION_SUPPORT', 'Virtualizzazione supportata', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A2', VIS, OMESSO),
 ('PH_CONTAINER_SUPPORT', 'Container supportati', IT, 'scheda tecnica di prodotto', 'P2', S, 'dossier A2', VIS, OMESSO),
 ('PH_TIME_SYNC_REQUIREMENT', 'Requisito di sincronizzazione oraria', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier 09', VIS, OMESSO),
 ('PH_INTERNET_REQUIREMENT', 'Accesso a internet richiesto', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08', VIS, OMESSO),
 ('PH_CLOUD_OPTION', 'Opzione cloud', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier 02 · 08', VIS, OMESSO),
])

g('5.8 Rete e protocolli', [
 ('PH_SUPPORTED_PROTOCOLS', 'Protocolli supportati', TEC, 'catalogo verificato in campo', 'P0', S, 'dossier 08 · A1', VIS, OMESSO),
 ('PH_PROTOCOL_VERSIONS', 'Versioni testate', TEC, 'catalogo verificato in campo', 'P1', S, 'dossier A1', VIS, OMESSO),
 ('PH_REQUIRED_PORTS', 'Porte richieste', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08 · A1', VIS, OMESSO),
 ('PH_FLOW_DIRECTIONS', 'Direzioni dei flussi', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08', VIS, 'resta lo schema logico V8'),
 ('PH_READ_ONLY_POLICY', 'Regola di sola lettura verso le macchine', TEC, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08 · A1', VIS, PRUD),
 ('PH_NETWORK_SEGMENTATION', 'Segmentazione di rete richiesta', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier 08', VIS, OMESSO),
 ('PH_FIREWALL_RULES', 'Regole firewall', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08 · A1', VIS, OMESSO),
 ('PH_GATEWAY_REQUIREMENTS', 'Requisiti del gateway', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier A1', VIS, OMESSO),
 ('PH_BANDWIDTH_REQUIREMENT', 'Banda richiesta', IT, 'scheda tecnica di prodotto', 'P2', S, 'dossier A2', VIS, OMESSO),
 ('PH_LATENCY_REQUIREMENT', 'Latenza richiesta', IT, 'scheda tecnica di prodotto', 'P2', S, 'dossier A2', VIS, OMESSO),
 ('PH_ERP_INTEGRATION_METHODS', 'Modalità di integrazione con il gestionale', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier 08 · 12', VIS, PRUD),
 ('PH_API_AVAILABILITY', 'Disponibilità delle API', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier 12', VIS, OMESSO),
 ('PH_API_AUTHENTICATION', 'Autenticazione delle API', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier 12', VIS, OMESSO),
 ('PH_EXPORT_FORMATS', 'Formati di export', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier 12', VIS, 'restano i formati già dichiarati'),
])

g('5.9 Security, dati e licenza', [
 ('PH_AUTHENTICATION_MODEL', 'Modello di autenticazione', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier 08 · A3', VIS, OMESSO),
 ('PH_ROLE_MODEL', 'Modello dei ruoli', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_PASSWORD_POLICY', 'Politica delle password', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_SSO_SUPPORT', 'Supporto SSO', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_AUDIT_LOGGING', 'Registro degli accessi', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_LOG_RETENTION', 'Retention dei log', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_PATCHING_POLICY', 'Politica di patching', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_VULNERABILITY_POLICY', 'Vulnerability management', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_BACKUP_POLICY', 'Politica di backup', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_BACKUP_FREQUENCY', 'Frequenza di backup', IT, 'scheda tecnica di prodotto', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_RPO', 'RPO', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_RTO', 'RTO', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_DISASTER_RECOVERY', 'Disaster recovery', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_DATA_ENCRYPTION_AT_REST', 'Cifratura a riposo', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_DATA_ENCRYPTION_IN_TRANSIT', 'Cifratura in transito', IT, 'scheda tecnica di prodotto', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_DATA_OWNERSHIP', 'Proprietà dei dati', LEG, 'contratto tipo', 'P0', S, 'dossier 02 · A3', VIS, PRUD),
 ('PH_LICENSE_RIGHTS', 'Diritti di licenza', LEG, 'contratto tipo', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_END_OF_CONTRACT_DATA', 'Dati a fine contratto', LEG, 'contratto tipo', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_END_OF_CONTRACT_ACCESS', 'Accesso a fine contratto', LEG, 'contratto tipo', 'P1', S, 'dossier A3', VIS, OMESSO),
 ('PH_DATA_EXPORT_AT_EXIT', 'Export a fine rapporto', LEG, 'contratto tipo', 'P0', S, 'dossier A3', VIS, OMESSO),
 ('PH_DATA_DELETION_POLICY', 'Cancellazione dei dati', LEG, 'contratto tipo', 'P1', S, 'dossier A3', VIS, OMESSO),
])

g('5.10 Dataset illustrativo', [
 ('PH_DATASET_LINE_TYPE', 'Tipo di linea dello scenario', TEC, 'validazione interna', 'P0', D, 'deck 01 · 11 · A5', VIS, 'resta «linea di confezionamento»'),
 ('PH_DATASET_VALIDATOR', 'Chi ha validato il dataset', TEC, 'validazione interna', 'P0', D, 'deck 01 · A5', VIS, OMESSO),
 ('PH_DATASET_VALIDATION_DATE', 'Data della validazione', TEC, 'validazione interna', 'P0', D, 'deck 01 · A5', VIS, OMESSO),
 ('PH_DATASET_THROUGHPUT', 'Pezzi al minuto', TEC, 'validazione interna', 'P0', D, 'deck 11 · A5', VIS, 'resta 500 pz/min, dichiarato illustrativo'),
 ('PH_DATASET_MARGIN_UNIT', 'Margine per pezzo', COM, 'validazione interna', 'P0', D, 'deck 11 · A5', VIS, 'resta 0,14 €/pz, dichiarato illustrativo'),
 ('PH_DATASET_RUNNING_POWER', 'Potenza in marcia', TEC, 'validazione interna', 'P0', D, 'deck 11 · A5', VIS, 'resta 95 kW, dichiarato illustrativo'),
 ('PH_DATASET_STOPPED_POWER', 'Potenza a impianto fermo', TEC, 'validazione interna', 'P0', D, 'deck 11 · A5', VIS, 'resta 38 kW, dichiarato illustrativo'),
 ('PH_DATASET_ENERGY_PRICE', 'Prezzo dell’energia', COM, 'contratto di fornitura', 'P0', D, 'deck A5', VIS, 'resta 0,22 €/kWh, dichiarato illustrativo'),
 ('PH_DATASET_EMISSION_FACTOR', 'Fattore di emissione', TEC, 'mix dichiarato dal fornitore', 'P0', D, 'deck A5', VIS, 'resta 0,35 kgCO₂e/kWh, dichiarato illustrativo'),
 ('PH_DATASET_SHIFT_DURATION', 'Durata del turno', TEC, 'validazione interna', 'P0', D, 'deck A5', VIS, 'resta 480 min, dichiarato illustrativo'),
 ('PH_DATASET_SHIFTS_PER_YEAR', 'Turni produttivi in un anno', TEC, 'validazione interna', 'P0', D, 'deck A5', VIS, 'resta 230, dichiarato illustrativo'),
 ('PH_DATASET_STOP_MIN_WEEK', 'Minuti di fermo a settimana', TEC, 'validazione interna', 'P0', D, 'deck 11 · A5', VIS, 'resta 96 min, dichiarato illustrativo'),
 ('PH_DATASET_RECOVERABLE_SHARE', 'Quota potenzialmente recuperabile', COM, 'validazione interna', 'P0', D, 'deck 11', VIS, 'resta la metà, dichiarata ipotesi'),
 ('PH_DATASET_ASSUMPTION_OWNER', 'Owner delle assunzioni', COM, 'nomina interna', 'P0', D, 'deck A5', VIS, OMESSO),
])

g('8 Perimetro dei moduli', [
 ('PH_CONNECT_EXACT_SCOPE', 'Perimetro esatto di Connect', TEC, 'scheda funzionale', 'P0', S, 'dossier 04', VIS, 'resta il perimetro già dichiarato'),
 ('PH_CONNECT_REPORTS', 'Report inclusi in Connect', TEC, 'scheda funzionale', 'P1', S, 'dossier 04', VIS, OMESSO),
 ('PH_CONNECT_ALERTS', 'Notifiche e allarmi di Connect', TEC, 'scheda funzionale', 'P1', S, 'dossier 04', VIS, OMESSO),
 ('PH_INSIGHT_EXACT_SCOPE', 'Perimetro esatto di Insight', TEC, 'scheda funzionale', 'P0', S, 'dossier 05', VIS, 'resta il perimetro già dichiarato'),
 ('PH_COST_CALCULATION_METHOD', 'Metodo di calcolo del costo', TEC, 'scheda funzionale', 'P1', S, 'dossier 05 · 11', VIS, 'resta il metodo già scritto in A4'),
 ('PH_CO2_METHOD', 'Metodo di calcolo della CO₂', TEC, 'scheda funzionale', 'P1', S, 'dossier 05 · 11', VIS, 'resta «CO₂ calcolata o stimata»'),
 ('PH_REFYN_MVP_SCOPE', 'Perimetro del primo rilascio di Refyn', TEC, 'piano di prodotto', 'P0', S, 'dossier 06', VIS, NASC),
 ('PH_REFYN_PILOT_RULES', 'Regole di accesso al pilot Refyn', COM, 'decisione commerciale', 'P0', S, 'dossier 06', VIS, NASC),
 ('PH_REFYN_RELEASE_TARGET', 'Data obiettivo di rilascio', DIR, 'piano di prodotto', 'P1', S, 'dossier 06', VIS, NASC),
 ('PH_STANDARD_SIGNAL_LIST', 'Elenco standard dei segnali', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier 07', VIS, OMESSO),
 ('PH_SENSOR_ACCURACY_REQUIREMENTS', 'Requisiti di precisione della sensoristica', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier 07', VIS, OMESSO),
 ('PH_METERING_STANDARDS', 'Standard di misura adottati', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier 07', VIS, OMESSO),
 ('PH_STANDARD_TAG_MODEL', 'Modello standard dei tag', TEC, 'scheda tecnica di prodotto', 'P1', S, 'dossier 09', VIS, 'restano i sette attributi'),
 ('PH_CAUSE_VALIDATION_PROCESS', 'Processo di validazione della causa', TEC, 'metodo di delivery', 'P1', S, 'dossier 09', VIS, 'resta «validata da chi la conosce»'),
 ('PH_REPORT_CATALOGUE', 'Catalogo dei report', TEC, 'scheda funzionale', 'P1', S, 'dossier 12', VIS, OMESSO),
])

g('9 Dizionario KPI e definizioni OEE', [
 ('PH_OEE_DEFINITION_OWNER', 'Owner della definizione di OEE', TEC, 'nomina interna', 'P1', S, 'dossier 10 · A4', VIS, OMESSO),
 ('PH_OEE_CALENDAR_RULES', 'Regole di calendario e tempo pianificato', TEC, 'metodo concordato', 'P0', S, 'dossier 10 · A4', VIS, 'resta «si concordano prima del go-live»'),
 ('PH_IDEAL_CYCLE_TIME_RULE', 'Regola del tempo ciclo ideale', TEC, 'metodo concordato', 'P0', S, 'dossier 10 · A4', VIS, 'resta la formula di A4'),
 ('PH_GOOD_COUNT_RULE', 'Regola del conteggio dei pezzi conformi', TEC, 'metodo concordato', 'P0', S, 'dossier 10 · A4', VIS, 'resta la formula di A4'),
 ('PH_LINE_OEE_AGGREGATION', 'Regola di aggregazione dell’OEE di linea', TEC, 'metodo concordato', 'P0', S, 'dossier 10', VIS, 'resta «collo di bottiglia»'),
 ('PH_ENERGY_PRICE_SOURCE', 'Fonte del prezzo dell’energia', COM, 'contratto di fornitura', 'P1', S, 'dossier 11', VIS, 'resta «contratto di fornitura»'),
 ('PH_EMISSION_FACTOR_SOURCE', 'Fonte del fattore di emissione', TEC, 'mix dichiarato dal fornitore', 'P1', S, 'dossier 11', VIS, 'resta «mix dichiarato»'),
 ('PH_COST_ALLOCATION_RULE', 'Regola di allocazione del costo', TEC, 'metodo concordato', 'P1', S, 'dossier 11', VIS, OMESSO),
 ('PH_KPI_OWNER', 'Owner del dizionario KPI', TEC, 'nomina interna', 'P1', S, 'dossier A4', VIS, OMESSO),
 ('PH_KPI_VERSION', 'Versione del dizionario KPI', TEC, 'processo interno', 'P1', S, 'dossier A4', VIS, OMESSO),
 ('PH_KPI_APPROVAL_DATE', 'Data di approvazione del dizionario', TEC, 'processo interno', 'P1', S, 'dossier A4', VIS, OMESSO),
])

g('10 Asset reali', [
 ('PH_REAL_SCREENSHOT_MAPST', 'Screenshot reale MAPST 4.0', TEC, 'ambiente reale', 'P1', B, 'deck 04 · dossier 04', VIS, 'resta la vista ricostruita dichiarata'),
 ('PH_REAL_SCREENSHOT_MARENERGY', 'Screenshot reale MarEnergy', TEC, 'ambiente reale', 'P1', B, 'deck 05 · dossier 11', VIS, 'resta la vista ricostruita dichiarata'),
 ('PH_REAL_SCREENSHOT_NEW_UI', 'Screenshot della nuova interfaccia', TEC, 'ambiente reale', 'P1', B, 'deck 03 · dossier 04', VIS, 'resta la vista ricostruita dichiarata'),
 ('PH_REAL_REPORT_EXPORT', 'Report reale esportato', TEC, 'ambiente reale', 'P1', S, 'dossier 12', VIS, OMESSO),
 ('PH_REAL_INSTALLATION_PHOTO', 'Foto di un’installazione', MKT, 'autorizzazione scritta', 'P1', B, 'deck 10 · dossier 01', VIS, OMESSO),
 ('PH_REAL_LINE_DIAGRAM', 'Schema di linea reale anonimizzato', TEC, 'documento di progetto', 'P1', S, 'dossier 07', VIS, 'resta lo schema tipo dichiarato'),
 ('PH_REAL_SENSOR_PHOTO', 'Foto di sensore o contatore', MKT, 'autorizzazione scritta', 'P1', S, 'dossier 07', VIS, OMESSO),
 ('PH_REAL_SERVER_DIAGRAM', 'Schema di deployment reale', IT, 'documento di progetto', 'P1', S, 'dossier 08', VIS, 'resta lo schema logico dichiarato'),
])

BY_ID = {r['id']: r for r in R}
P0 = [r['id'] for r in R if r['prio'] == 'P0']
P1 = [r['id'] for r in R if r['prio'] == 'P1']
P2 = [r['id'] for r in R if r['prio'] == 'P2']

if __name__ == '__main__':
    import collections
    print(f'{len(R)} placeholder · P0 {len(P0)} · P1 {len(P1)} · P2 {len(P2)}')
    dup = [k for k, v in collections.Counter(r['id'] for r in R).items() if v > 1]
    print('duplicati:', dup or 'nessuno')
