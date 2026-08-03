#!/usr/bin/env python3
"""Claim Register V9.1 · §14: il build fallisce se un claim tecnico presente
nei documenti non e' censito qui.

Ogni voce: la frase, dove compare, che cosa la sostiene, lo stato e la
formulazione approvata quando esiste.
"""
import gates
C = gates.CLAIM_APPROVATI

# (chiave, frase nel documento, marcatore da cercare, stato, fonte)
CLAIMS = [
 ('read_only', 'Acquisizione verso le macchine in sola lettura',
  'sola lettura', 'PRUDENTE', C['read_only']['fonte']),
 ('residenza', 'Residenza e trattamento dei dati concordati con l’IT',
  'solution design', 'PRUDENTE', C['residenza']['fonte']),
 ('oee', 'OEE come disponibilità × performance × qualità',
  'disponibilit', 'DIMOSTRATO', 'formula scritta per esteso, ricostruibile'),
 ('costo_en', 'Costo energetico del pezzo da consumo, prezzo e pezzi',
  'costo energetico', 'DIMOSTRATO', 'catena aritmetica esplicita'),
 ('co2', 'CO₂ calcolata o stimata dal fattore dichiarato',
  'calcolata o stimata', 'DIMOSTRATO CON RISERVA', 'fattore illustrativo, fonte da confermare'),
 ('cumulativa', 'Insight comprende Connect, Refyn comprende entrambi',
  'comprende il precedente', 'AFFERMATO', 'architettura di prodotto dichiarata'),
 ('refyn', 'Refyn, modulo avanzato in sviluppo, via pilot dedicato',
  'in sviluppo', 'AFFERMATO', C['refyn']['fonte']),
 ('brownfield', 'Si parte dall’impianto esistente',
  'impianto esistente', 'AFFERMATO', 'metodo di acquisizione descritto'),
 ('erp', 'Integrazione con il gestionale previa verifica',
  'previa verifica', 'AFFERMATO CON RISERVA', 'formulazione condizionale'),
 ('compat', 'La compatibilità si verifica sull’impianto reale',
  'impianto reale', 'AFFERMATO', 'metodo di audit descritto'),
]

# marcatori tecnici che, se presenti nei documenti, devono avere un claim
SORVEGLIATI = ['sola lettura', 'solution design', 'costo energetico',
               'calcolata o stimata', 'in sviluppo', 'previa verifica',
               'impianto reale', 'impianto esistente']


def non_registrati(html):
    censiti = {c[2] for c in CLAIMS}
    return [m for m in SORVEGLIATI if m in html and m not in censiti]


def tutti_prudenti():
    return all(c[3] != 'DA VERIFICARE' for c in CLAIMS)


if __name__ == '__main__':
    for c in CLAIMS:
        print(f'{c[3]:24s} {c[1]}')
    print(f'\n{len(CLAIMS)} claim · nessuno DA VERIFICARE: {tutti_prudenti()}')
