#!/bin/bash
# Catena di build V9.3 · dal sorgente ai quattro HTML consegnati.
set -e
cd "$(dirname "$0")"
R=..
python3 mk_deck93.py
python3 mk_dossier93.py
python3 edition92.py deck93_master.html    deck93_w_body.html    working
python3 edition92.py deck93_master.html    deck93_c_body.html    client
python3 edition92.py dossier93_master.html dossier93_w_body.html working
python3 edition92.py dossier93_master.html dossier93_c_body.html client
python3 build.py deck93.css    deck93_w_body.html    $R/DFactory_SalesDeck_v9_3_working.html      "D.Factory · Sales Deck V9.3 · working edition"
python3 build.py deck93.css    deck93_c_body.html    $R/DFactory_SalesDeck_v9_3_client.html       "D.Factory · Sales Deck V9.3"
python3 build.py dossier93.css dossier93_w_body.html $R/DFactory_DossierTecnico_v9_3_working.html "D.Factory · Dossier tecnico V9.3 · working edition"
python3 build.py dossier93.css dossier93_c_body.html $R/DFactory_DossierTecnico_v9_3_client.html  "D.Factory · Dossier tecnico preliminare V9.3"
