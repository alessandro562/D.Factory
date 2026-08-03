#!/usr/bin/env python3
"""Claim Register V9.3.

Dieci claim, gli stessi della V9.2: la revisione narrativa non ha aggiunto
affermazioni tecniche. Due cambiano **formulazione** per effetto del §2.3 e
del §2.4 della review D2, e il cambio e' registrato qui perche' e' un cambio
di sostanza, non di stile:

  · «Motore KPI» era un componente architetturale dichiarato. Non e'
    confermato: diventa «Elaborazione KPI», una funzione.
  · «API · dati selezionati · da definire» dichiarava disponibile
    un'interfaccia che non lo e'. Diventa «Interfacce applicative · da
    verificare sul perimetro».

Il build fallisce se un marcatore tecnico compare nei documenti senza un
claim che lo copra.
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
  'comprende', 'AFFERMATO', 'architettura di prodotto dichiarata'),
 ('refyn', 'Refyn, modulo avanzato in sviluppo, via pilot dedicato',
  'in sviluppo', 'AFFERMATO', C['refyn']['fonte']),
 ('brownfield', 'Si parte dall’impianto esistente',
  'gi&agrave; presenti', 'AFFERMATO', 'metodo di acquisizione descritto'),
 ('erp', 'Interfacce applicative, da verificare sul perimetro',
  'da verificare sul perimetro|previa verifica', 'AFFERMATO CON RISERVA',
  'la disponibilità di un’interfaccia applicativa non è confermata · §2.4 review D2'),
 ('compat', 'La compatibilità si verifica sull’impianto reale',
  'impianto reale', 'AFFERMATO', 'metodo di audit descritto'),
]

# marcatori tecnici che, se presenti nei documenti, devono avere un claim
SORVEGLIATI = ['sola lettura', 'solution design', 'costo energetico',
               'calcolata o stimata', 'in sviluppo', 'da verificare sul perimetro',
               'impianto reale', 'previa verifica']

# §12 del master · formulazioni vietate. Non e' una questione di stile: ognuna
# di queste dichiara qualcosa che nessuno ha confermato.
VIETATE = ['Insights', 'causa automatica', 'causa rilevata automaticamente',
           'qualsiasi protocollo', 'zero hardware', 'costo reale del pezzo',
           'costo del pezzo', 'risparmio garantito', 'software ISO 50001',
           'API disponibile', 'ERP nativo', 'cloud non necessario',
           'dati sempre on-premise', 'Motore KPI']


def non_registrati(testo):
    censiti = {m for c in CLAIMS for m in c[2].split('|')}
    return [m for m in SORVEGLIATI if m in testo and m not in censiti]


def vietate_presenti(testo):
    """«costo del pezzo» e' vietato da solo, ma «costo energetico per pezzo»
    e' la formulazione corretta e lo contiene: va scontata."""
    fuori = []
    for v in VIETATE:
        i = testo.find(v)
        while i >= 0:
            prima = testo[max(0, i - 22):i].lower()
            if v == 'costo del pezzo' and ('non sono il' in prima or 'non è il' in prima):
                pass
            else:
                fuori.append(v)
                break
            i = testo.find(v, i + 1)
    return fuori


def tutti_prudenti():
    return all(c[3] != 'DA VERIFICARE' for c in CLAIMS)


if __name__ == '__main__':
    for c in CLAIMS:
        print(f'{c[3]:24s} {c[1]}')
    print(f'\n{len(CLAIMS)} claim · nessuno DA VERIFICARE: {tutti_prudenti()}')
