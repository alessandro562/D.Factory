#!/usr/bin/env python3
"""Assembla il dossier v5: 23 pagine v4 + 8 nuove/riscritte = 31, in cinque sezioni."""
import re, sys
sys.path.insert(0, 'work_v5')
from dossier_new_pages import PAGES

src = open('work_v4/dossier_body.html', encoding='utf-8').read()
parts = re.split(r'(?=<!-- =+ \d+ ·)', src)
head = parts[0]
old = {}
for blk in parts[1:]:
    m = re.search(r'<div class="slide[^"]*" id="([^"]+)"', blk)
    old[m.group(1)] = blk
# stacca la chiusura di .doc dall'ultima pagina
last = list(old)[-1]
old[last] = old[last].rsplit('</div>', 1)[0]

# le pagine v4 riutilizzate, con l'id nuovo dove cambia
REUSE = {
    'd01_cover': 'd01_cover',
    'd03_architettura_tecnica': 'd04_architettura_tecnica',
    'd04_acquisizione': 'd05_acquisizione',
    'd06_supervisione': 'd07_supervisione',
    'd07_oee_fermi': 'd08_oee_fermi',
    'd08_velocita_qualita': 'd09_velocita_qualita',
    'd09_multi_impianto': 'd10_multi_impianto',
    'd10_distribuzione_energia': 'd11_distribuzione_energia',
    'd11_costo_co2_stato': 'd12_costo_co2_stato',
    'd12_metodo_misura': 'd13_metodo_misura',
    'd13_brownfield_macchine': 'd19_brownfield_macchine',
    'd14_brownfield_rete': 'd20_brownfield_rete',
    'd15_deployment': 'd21_deployment',
    'd16_specifiche_it': 'd22_specifiche_it',
    'd17_sensori': 'd23_sensori',
    'd18_output_integrazioni': 'd24_output_integrazioni',
    'd19_milestone': 'd26_milestone',
    'd20_raci': 'd27_raci',
    'd21_criteri_pilot': 'd28_criteri_pilot',
    'd22_supporto': 'd29_supporto',
    'd23_checklist': 'd31_checklist',
}
pages = {}
for old_id, new_id in REUSE.items():
    blk = old[old_id]
    if old_id != new_id:
        blk = re.sub(rf'\b{old_id}\b', new_id, blk)
    pages[new_id] = blk
pages.update(PAGES)

ORDER = [
    # A · prodotto e maturità
    'd01_cover', 'd02_architettura_commerciale', 'd03_provenienza',
    'd04_architettura_tecnica', 'd05_acquisizione', 'd06_capability',
    # B · funzioni proven e pilot
    'd07_supervisione', 'd08_oee_fermi', 'd09_velocita_qualita', 'd10_multi_impianto',
    'd11_distribuzione_energia', 'd12_costo_co2_stato', 'd13_metodo_misura',
    'd14_correlazione',
    # C · Refyn in sviluppo
    'd15_opportunity', 'd16_action_benefit', 'd17_oee_avanzato', 'd18_roadmap',
    # D · integrazione e IT
    'd19_brownfield_macchine', 'd20_brownfield_rete', 'd21_deployment',
    'd22_specifiche_it', 'd23_sensori', 'd24_output_integrazioni',
    # E · servizi, delivery e migrazione
    'd25_servizi', 'd26_milestone', 'd27_raci', 'd28_criteri_pilot', 'd29_supporto',
    'd30_migrazione', 'd31_checklist',
]
assert set(ORDER) == set(pages), f'diff: {set(ORDER) ^ set(pages)}'
N = len(ORDER)

# le sezioni cambiano nome: da "Sezione 1..4" a "Sezione A..E"
SEC = {}
for pid in ORDER[1:6]:   SEC[pid] = 'Sezione A · prodotto'
for pid in ORDER[6:14]:  SEC[pid] = 'Sezione B · funzioni'
for pid in ORDER[14:18]: SEC[pid] = 'Sezione C · Refyn'
for pid in ORDER[18:24]: SEC[pid] = 'Sezione D · integrazione'
for pid in ORDER[24:]:   SEC[pid] = 'Sezione E · delivery'

SLIM = {'d06_capability', 'd18_roadmap', 'd19_brownfield_macchine', 'd22_specifiche_it',
        'd23_sensori', 'd24_output_integrazioni', 'd25_servizi', 'd27_raci',
        'd28_criteri_pilot', 'd31_checklist'}

out = [head.rstrip() + '\n\n']
for i, pid in enumerate(ORDER, 1):
    blk = pages[pid]
    blk = re.sub(r'<span class="pg">[^<]*</span>',
                 f'<span class="pg">{i:02d} / {N}</span>', blk)
    blk = blk.replace('>PG<', f'>{i:02d} / {N}<')
    if pid == 'd01_cover':
        blk = re.sub(r'<span class="pg">[^<]*</span>',
                     f'<span class="pg">01 / {N} · D.Factory · D Factory S.r.l.</span>', blk)
    if pid in SEC:
        blk = re.sub(r'<div class="band__sec">[^<]*</div>',
                     f'<div class="band__sec">{SEC[pid]}</div>', blk)
    if pid in SLIM and 'band--slim' not in blk:
        blk = blk.replace('<div class="band">', '<div class="band band--slim">', 1)
        blk = blk.replace('<div class="field">', '<div class="field field--wide">', 1)
    out.append(blk.rstrip() + '\n\n')
out.append('</div>\n')

open('work_v5/dossier_body.html', 'w', encoding='utf-8').write(''.join(out))
print(f'dossier v5 assemblato: {N} pagine')
for i, pid in enumerate(ORDER, 1):
    tag = ' [slim]' if pid in SLIM else ''
    new = ' NUOVA' if pid in PAGES else ''
    print(f'  {i:02d}  {pid}{tag}{new}')
