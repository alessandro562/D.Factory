#!/usr/bin/env python3
"""Convenzione unica per le frecce dei due documenti.

Il difetto trovato in undici frecce su undici era sempre lo stesso: asta e
punta stavano nello stesso <g> con `stroke` **e** `fill`, cosi' la punta
veniva anche contornata, e l'asta arrivava oltre la base della punta. Il
risultato e' una macchia con una coda, che a schermo si legge come un errore.

Regola, valida ovunque:

  1. l'asta e' un <path> con solo stroke, `fill="none"`;
  2. la punta e' un <polygon> con solo fill, `stroke="none"`;
  3. l'asta finisce esattamente sulla base della punta, mai oltre;
  4. la punta e' sempre 12 lunga e 11 larga, in ogni freccia dei due documenti;
  5. le direzioni ammesse sono quattro: su, giu', destra, sinistra. Nessuna
     freccia obliqua, come nessuna linea obliqua.

`freccia()` restituisce il markup corretto: nessuna coordinata viene scritta
a mano.
"""

L = 12      # lunghezza della punta
W = 11      # larghezza della punta


def freccia(x, y, verso, coda, colore='#0A0A0A', spessore=1.5):
    """Freccia con la punta in (x, y) e l'asta lunga `coda` px.

    verso: 'su' | 'giu' | 'dx' | 'sx' — la punta guarda in quella direzione.
    """
    h = W / 2
    if verso == 'giu':
        base = y - L
        asta = f'M{x} {base - coda} L{x} {base}'
        punta = f'{x},{y} {x - h},{base} {x + h},{base}'
    elif verso == 'su':
        base = y + L
        asta = f'M{x} {base + coda} L{x} {base}'
        punta = f'{x},{y} {x - h},{base} {x + h},{base}'
    elif verso == 'dx':
        base = x - L
        asta = f'M{base - coda} {y} L{base} {y}'
        punta = f'{x},{y} {base},{y - h} {base},{y + h}'
    elif verso == 'sx':
        base = x + L
        asta = f'M{base + coda} {y} L{base} {y}'
        punta = f'{x},{y} {base},{y - h} {base},{y + h}'
    else:
        raise ValueError(verso)
    return (f'<path d="{asta}" stroke="{colore}" stroke-width="{spessore}" fill="none"/>'
            f'<polygon points="{punta}" fill="{colore}" stroke="none"/>')


def spezzata(punti, colore='#0A0A0A', spessore=1.5):
    """Percorso ortogonale: ogni segmento e' orizzontale o verticale.

    Solleva un errore se due punti consecutivi differiscono su entrambi gli
    assi, cosi' una diagonale non puo' entrare per distrazione.
    """
    for (x1, y1), (x2, y2) in zip(punti, punti[1:]):
        if x1 != x2 and y1 != y2:
            raise ValueError(f'segmento obliquo da ({x1},{y1}) a ({x2},{y2})')
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in punti)
    return f'<path d="{d}" stroke="{colore}" stroke-width="{spessore}" fill="none"/>'


if __name__ == '__main__':
    print(freccia(300, 32, 'giu'))
    print(freccia(914, 77, 'dx', coda=86))
    print(spezzata([(1002, 80), (1002, 118), (150, 118), (150, 92)]))
