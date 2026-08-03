#!/usr/bin/env python3
"""Registro degli asset V9.2 · dieci colonne, zero righe.

Il §19.3 impone sette informazioni per ogni file; qui sono dieci perché
scadenza dell'autorizzazione e pagine d'uso servono a chi rinnova. Il registro
è vuoto: nessun asset reale è stato consegnato, e il build fallisce se un file
compare in un canvas senza essere qui.
"""

COLONNE = ['file', 'fonte', 'data', 'prodotto', 'versione', 'autorizzazione',
           'anonimizzazione', 'uso consentito', 'scadenza', 'pagine']

REGISTRO = {}          # file → dict(colonne)

# §19.1 · l'ordine di priorità, e dove ciascuno andrebbe
OBIETTIVO = [
    dict(n=1, asset='Screenshot reale MAPST 4.0', token='PH_REAL_SCREENSHOT_MAPST',
         etichetta='Interfaccia MAPST 4.0 · prodotto legacy',
         dove='deck 04 · dossier 04', stato='mancante'),
    dict(n=2, asset='Screenshot reale MarEnergy', token='PH_REAL_SCREENSHOT_MARENERGY',
         etichetta='Interfaccia MarEnergy · prodotto legacy',
         dove='deck 05 · dossier 05', stato='mancante'),
    dict(n=3, asset='Report reale anonimizzato', token='PH_REAL_REPORT_EXPORT',
         etichetta='Report reale anonimizzato',
         dove='dossier 12', stato='mancante'),
    dict(n=4, asset='Schema di linea o foto di installazione', token='PH_REAL_LINE_DIAGRAM',
         etichetta='Schema di linea anonimizzato',
         dove='dossier 07 · deck 10', stato='mancante'),
    dict(n=5, asset='Screenshot della nuova interfaccia', token='PH_REAL_SCREENSHOT_NEW_UI',
         etichetta='Interfaccia D.Factory',
         dove='deck 03', stato='mancante'),
    dict(n=6, asset='Foto di sensore o contatore', token='PH_REAL_SENSOR_PHOTO',
         etichetta='Punto di misura · foto di campo',
         dove='dossier 07', stato='mancante'),
]

# §19.2 · quanti ne servono per dire «obiettivo raggiunto»
SOGLIA = {'deck': 1, 'dossier': 2}


def raggiunti():
    return {k: 0 for k in SOGLIA}


if __name__ == '__main__':
    print(f'{len(REGISTRO)} asset registrati · {len(OBIETTIVO)} candidati')
    for k, v in SOGLIA.items():
        print(f'  {k}: {raggiunti()[k]}/{v}')
