#!/bin/bash
# Catena di build V9.4 · dal sorgente ai due HTML A4 consegnati.
set -e
cd "$(dirname "$0")"
R=..
python3 mk_dossier94.py
python3 edition94.py dossier94_master.html dossier94_w_body.html working
python3 edition94.py dossier94_master.html dossier94_c_body.html client
python3 build94.py dossier94.css dossier94_w_body.html \
  $R/DFactory_DossierTecnico_A4_v9_4_working.html \
  "D.Factory · Dossier tecnico A4 V9.4 · working edition"
python3 build94.py dossier94.css dossier94_c_body.html \
  $R/DFactory_DossierTecnico_A4_v9_4_client.html \
  "D.Factory · Dossier tecnico preliminare A4 V9.4"
