#!/usr/bin/env python3
"""Registro degli asset reali · §7.4 del piano.

Dieci colonne obbligatorie. Il build fallisce se un file compare in un canvas
senza essere qui. Oggi il registro e' vuoto: nessun asset reale esiste.
"""
COLONNE = ['file', 'fonte', 'data', 'prodotto', 'versione', 'autorizzazione',
           'anonimizzazione', 'uso consentito', 'scadenza', 'pagine']

# chiave = href usato negli HTML · valore = dict con le dieci colonne
REGISTRO = {}

# §7.1 · obiettivo minimo della V9.1: almeno due dei quattro
OBIETTIVO = [
    ('screenshot MAPST 4.0 o base software operativa', 'PH_REAL_SCREENSHOT_MAPST',
     'Interfaccia MAPST 4.0 · prodotto legacy'),
    ('screenshot MarEnergy', 'PH_REAL_SCREENSHOT_MARENERGY',
     'Interfaccia MarEnergy · prodotto legacy'),
    ('report reale', 'PH_REAL_REPORT_EXPORT', 'Report reale anonimizzato'),
    ('fotografia o schema reale di linea', 'PH_REAL_LINE_DIAGRAM',
     'Schema di linea anonimizzato'),
]

if __name__ == '__main__':
    print(f'{len(REGISTRO)} asset registrati · obiettivo minimo §7.1: 2 su {len(OBIETTIVO)}')
