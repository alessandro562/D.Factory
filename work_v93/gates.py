#!/usr/bin/env python3
"""I cinque gate della V9.1 e il gate del caso cliente.

La V9 aveva 104 P0 indistinti. Il §3 del piano chiede di separare che cosa
blocca davvero, e che cosa e' soltanto utile. Qui i gate sono dati: il build
li legge, il registro li stampa, la client edition li rispetta.

BLOCKING_SCOPE:
  GLOBAL   impedisce la client edition del documento
  SECTION  esclude una sezione o disattiva un contenuto
  PAGE     esclude un singolo canvas
  NONE     non blocca: si pubblica con formulazione prudente
"""

GATES = {
 'G1': dict(
    nome='Identità e CTA',
    blocca='la pubblicazione del Sales Deck',
    scope='GLOBAL',
    effetto='La CTA resta nella client edition (§9.13) ma senza referente non è '
            'inviabile: il deck si presenta dal vivo, non si manda.',
    campi=['PH_COMPANY_LEGAL_NAME', 'PH_CONTACT_NAME', 'PH_CONTACT_ROLE',
           'PH_CONTACT_EMAIL', 'PH_AUDIT_NAME', 'PH_AUDIT_DURATION',
           'PH_AUDIT_PARTICIPANTS', 'PH_AUDIT_INPUTS', 'PH_AUDIT_DELIVERABLES']),
 'G2': dict(
    nome='Modello commerciale',
    blocca="la definizione completa dell'offerta",
    scope='SECTION',
    effetto="L'appendice pricing non entra nella client edition. Il deck mostra "
            'la struttura, non gli importi.',
    campi=['PH_AUDIT_PRICE', 'PH_SETUP_FIRST_LINE', 'PH_CONNECT_ANNUAL_FEE',
           'PH_INSIGHT_ANNUAL_FEE', 'PH_REFYN_PRICING_MODEL', 'PH_ADDITIONAL_LINE_FEE',
           'PH_SERVICES_INCLUDED', 'PH_SERVICES_OPTIONAL', 'PH_CONTRACT_TERM',
           'PH_RENEWAL_TERMS']),
 'G3': dict(
    nome='Dataset',
    blocca='la pubblicazione del business case',
    scope='SECTION',
    effetto='I valori annualizzati escono dalla client edition. Restano la formula, '
            'i dati del turno e della settimana, che sono osservati nello scenario.',
    campi=['PH_DATASET_VALIDATOR', 'PH_DATASET_VALIDATION_DATE', 'PH_DATASET_LINE_TYPE',
           'PH_DATASET_THROUGHPUT', 'PH_DATASET_MARGIN_UNIT', 'PH_DATASET_RUNNING_POWER',
           'PH_DATASET_STOPPED_POWER', 'PH_DATASET_ENERGY_PRICE', 'PH_DATASET_SHIFT_DURATION',
           'PH_DATASET_SHIFTS_PER_YEAR', 'PH_DATASET_STOP_MIN_WEEK',
           'PH_DATASET_RECOVERABLE_SHARE']),
 'G4': dict(
    nome='Requisiti tecnici minimi',
    blocca='la dichiarazione «pronto per IT»',
    scope='SECTION',
    effetto='Il dossier resta «preliminare per assessment e solution design».',
    campi=['PH_DEPLOYMENT_MODEL', 'PH_SUPPORTED_OS', 'PH_MIN_CPU', 'PH_MIN_RAM',
           'PH_MIN_STORAGE', 'PH_SUPPORTED_PROTOCOLS', 'PH_REQUIRED_PORTS',
           'PH_FLOW_DIRECTIONS', 'PH_READ_ONLY_POLICY', 'PH_AUTHENTICATION_MODEL',
           'PH_ROLE_MODEL', 'PH_BACKUP_POLICY', 'PH_RETENTION_DEFAULT',
           'PH_AUDIT_LOGGING', 'PH_REMOTE_SUPPORT_POLICY', 'PH_DATA_OWNERSHIP',
           'PH_LICENSE_RIGHTS', 'PH_END_OF_CONTRACT_DATA']),
 'G5': dict(
    nome='Evidenza commerciale',
    blocca="l'invio a freddo e il passaggio in procurement",
    scope='NONE',
    effetto="Non blocca l'uso dal vivo. Bastano due elementi approvati fra "
            'screenshot, report, schema, foto, fatto aziendale, caso cliente.',
    campi=['PH_REAL_SCREENSHOT_MAPST', 'PH_REAL_SCREENSHOT_MARENERGY',
           'PH_REAL_SCREENSHOT_NEW_UI', 'PH_REAL_REPORT_EXPORT',
           'PH_REAL_INSTALLATION_PHOTO', 'PH_REAL_LINE_DIAGRAM',
           'PH_REAL_SENSOR_PHOTO', 'PH_REAL_SERVER_DIAGRAM'],
    soglia=2),
}

# §3.2 · il caso cliente non genera 28 P0: ne genera uno.
CASE_GATE = 'PH_CASE_STUDY_READY'
CASE_ELEMENTI = ['autorizzazione', 'cliente o anonimizzazione', 'problema', 'baseline',
                 'intervento', 'periodo osservato', 'risultato', 'metodologia']

# Stato dichiarato dei gate. Nessuno è chiuso: i workshop del §11 non si sono
# ancora tenuti. Cambiare qui, non negli HTML.
STATO = {'G1': 'OPEN', 'G2': 'OPEN', 'G3': 'OPEN', 'G4': 'OPEN', 'G5': 'OPEN'}
CASE_STUDY_READY = 'NO'

# §6 · formulazioni approvate dal piano stesso, con la fonte.
CLAIM_APPROVATI = {
 'read_only': dict(
    fonte='piano V9.1 §6.1, opzione B raccomandata',
    testo='La configurazione standard privilegia l’acquisizione in sola lettura. '
          'Eventuali scambi ulteriori vengono definiti nel solution design.',
    breve='sola lettura in configurazione standard'),
 'residenza': dict(
    fonte='piano V9.1 §6.2, copy prudente',
    testo='Il modello di deployment, la residenza e il trattamento dei dati vengono '
          'concordati con l’IT e formalizzati nel solution design.',
    breve='concordata con l’IT'),
 'proprieta': dict(
    fonte='piano V9.1 §6.3 — **non pubblicare finché non approvato legalmente**',
    testo='I dati operativi restano nella disponibilità del cliente. Diritti d’uso del '
          'software, modalità di accesso ed export a fine contratto sono definiti '
          'nell’accordo di licenza.',
    breve='working edition soltanto'),
 'energia': dict(
    fonte='piano V9.1 §5.4, copy raccomandato',
    testo='In questo scenario il valore principale nasce dalla capacità recuperabile. '
          'Il dato energetico completa la lettura e quantifica il consumo improduttivo '
          'dello stesso evento.',
    breve='la leva energia completa, non pareggia'),
 'refyn': dict(
    fonte='piano V9.1 §4.3, raccomandazione di breve periodo',
    testo='Refyn è disponibile attraverso un progetto pilota dedicato, con quotazione '
          'sul perimetro.',
    breve='pilot dedicato, nessun listino'),
}

CAMPI_GATE = {c: g for g, d in GATES.items() for c in d['campi']}


def aperti():
    return [g for g, s in STATO.items() if s != 'APPROVED']


if __name__ == '__main__':
    n = sum(len(d['campi']) for d in GATES.values())
    print(f'{len(GATES)} gate · {n} campi nei gate · caso cliente: {CASE_STUDY_READY}')
    for g, d in GATES.items():
        print(f'  {g} {d["nome"]:28s} {d["scope"]:8s} {len(d["campi"]):2d} campi · {STATO[g]}')
