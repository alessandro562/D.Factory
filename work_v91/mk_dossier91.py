#!/usr/bin/env python3
"""Dossier tecnico V9.1 · delta sul corpo master V9.

§10 del piano. Il titolo resta «preliminare» finché G4 è aperto. I claim
tecnici passano alle formulazioni approvate al §6; la proprietà dei dati resta
in working edition perché il §6.3 vieta di pubblicarla prima del legale.
"""
import re
import gates
import ph91

s = open('dossier9_master.html', encoding='utf-8').read()
G4_OK = gates.STATO['G4'] == 'APPROVED'
C = gates.CLAIM_APPROVATI


def sub(old, new):
    global s
    assert old in s, f'stringa non trovata: {old[:70]}'
    s = s.replace(old, new, 1)


# =====================================================================
# §10.1 · titolo · «Dossier tecnico» solo dopo G4
# =====================================================================
if G4_OK:
    sub('Dossier tecnico\n      preliminare<br>per assessment e solution design',
        'Dossier tecnico')

# =====================================================================
# §10.2 · overview · la distinzione fra definito e da definire, esplicita
# =====================================================================
sub('<div class="note">Il modello di deployment, le quantit&agrave; e le taglie si definiscono nel\n'
    '      solution design, con IT e OT.</div>',
    '<div class="lbl" style="margin-bottom:8px">Definito nel solution design</div>\n'
    '    <div class="sp">Ambiente e sizing · protocolli e porte · autenticazione ·\n'
    '      backup e retention · integrazioni · supporto remoto.</div>')

# =====================================================================
# §6.1 · sola lettura · formulazione B, approvata dal piano
# =====================================================================
sub('<div class="row"><b>Verso le macchine</b><span data-ed="working">{{PH_READ_ONLY_POLICY}}</span>'
    '<span data-ed="client">sola lettura</span></div>',
    '<div class="row"><b>Verso le macchine</b><span data-ed="working">{{PH_READ_ONLY_POLICY}}</span>'
    '<span data-ed="client">sola lettura, in configurazione standard</span></div>')
sub('<text x="204" y="158" font-family="Geist" font-size="14" font-weight="500" fill="#0A0A0A">Acquisizione in sola lettura</text>\n'
    '    <text x="204" y="180" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)">normalizzazione e marcatura temporale</text>',
    '<text x="204" y="158" font-family="Geist" font-size="14" font-weight="500" fill="#0A0A0A">Acquisizione in sola lettura</text>\n'
    '    <text x="204" y="180" font-family="Geist" font-size="13" fill="rgba(10,10,10,.58)">configurazione standard · normalizzazione e marcatura temporale</text>')
sub('<div class="tt tt--sm">Dove gira, e come parla con la rete di stabilimento.\n'
    '    <div class="sub" style="margin-top:14px">Verso le macchine il flusso &egrave; in sola lettura.</div>',
    '<div class="tt tt--sm">Dove risiede e come comunica con la rete di stabilimento.\n'
    f'    <div class="sub" style="margin-top:14px">{C["read_only"]["testo"]}</div>')
sub('<svg class="diag" style="top:206px" width="800" height="404" viewBox="0 0 800 404"',
    '<svg class="diag" style="top:222px" width="800" height="404" viewBox="0 0 800 404"')
sub('<div class="spec" style="top:206px">\n    <div class="lbl" style="margin-bottom:6px">Definito dal prodotto</div>',
    '<div class="spec" style="top:222px">\n    <div class="lbl" style="margin-bottom:6px">Definito dal prodotto</div>')

# =====================================================================
# §6.2 · residenza dati · copy prudente approvata
# =====================================================================
sub('<div class="note" style="margin-top:22px">Sono decisioni di progetto, non limiti del prodotto: si chiudono con IT e OT prima dell&rsquo;installazione.</div>',
    f'<div class="note" style="margin-top:22px">{C["residenza"]["testo"]}</div>')

# =====================================================================
# §6.3 · proprietà dei dati e licenza · NON entra nei documenti.
#   Il piano dice «non pubblicare finché non approvato legalmente»: la
#   formulazione resta in DFactory_Decisioni_Tecniche_v9_1.md, dove ha il suo
#   stato di approvazione. L'annesso A3 continua a dire che cosa si decide e
#   chi decide, che è vero oggi.
# =====================================================================

# =====================================================================
# §10.9 · contesto · il processo di validazione delle cause, dichiarato
# =====================================================================
sub('<div class="note">Senza queste chiavi il dato grezzo resta un numero: non si attribuisce\n'
    '      una perdita a un formato, né un consumo a uno stato.</div>',
    '<div class="note">La causa è proposta sulla base dello stato e validata da chi la '
    'conosce. Senza queste chiavi il dato grezzo resta un numero: non si attribuisce una '
    'perdita a un formato, n&eacute; un consumo a uno stato.</div>')

# =====================================================================
# §10.11 · energia · perimetro della potenza, dichiarato come da chiudere
# =====================================================================
sub('<div class="box" style="margin-top:24px"><div class="note">Prezzo e fattore di emissione arrivano dal contratto di fornitura, non da noi.</div></div>',
    '<div class="box" style="margin-top:24px"><div class="note">Prezzo e fattore di emissione arrivano dal contratto di fornitura. Il perimetro della potenza a impianto fermo — linea, macchine o ausiliari — si dichiara nel solution design.</div></div>')

open('dossier91_body.html', 'w', encoding='utf-8').write(s)
used = set(re.findall(r'\{\{(PH_[A-Z0-9_]+)\}\}', s))
undeclared = used - set(ph91.BY_ID)
assert not undeclared, f'placeholder non dichiarati: {undeclared}'
n = len(re.findall(r'<div[^>]*class="slide', s))
print(f'dossier91_body.html · {n} canvas · {len(used)} placeholder distinti · G4 {gates.STATO["G4"]}')
