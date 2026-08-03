#!/bin/sh
# Catena di build V9.2, dall'inizio alla fine.
#   ./build_all.sh
# Per rigenerare tutto dopo l'approvazione di un gate basta cambiare
# gates.STATO e rilanciare: i documenti si aggiornano da soli.
set -e
cd "$(dirname "$0")"
R=..

echo '--- corpo master (delta sul V9.1) ---'
python3 mk_deck92.py
python3 mk_dossier92.py

echo '--- edizioni ---'
python3 edition92.py deck92_master.html    deck92_w_body.html    working
python3 edition92.py deck92_master.html    deck92_c_body.html    client
python3 edition92.py dossier92_master.html dossier92_w_body.html working
python3 edition92.py dossier92_master.html dossier92_c_body.html client

echo '--- HTML autonomi ---'
python3 build.py deck92.css    deck92_w_body.html    $R/DFactory_SalesDeck_v9_2_working.html      "D.Factory · Sales Deck V9.2 · working edition"
python3 build.py deck92.css    deck92_c_body.html    $R/DFactory_SalesDeck_v9_2_client.html       "D.Factory · Sales Deck V9.2"
python3 build.py dossier92.css dossier92_w_body.html $R/DFactory_DossierTecnico_v9_2_working.html "D.Factory · Dossier tecnico V9.2 · working edition"
python3 build.py dossier92.css dossier92_c_body.html $R/DFactory_DossierTecnico_v9_2_client.html  "D.Factory · Dossier tecnico preliminare V9.2"

echo '--- render, provini, PDF ---'
rm -rf $R/render/v92 && mkdir -p $R/render/v92
python3 render.py $R/DFactory_SalesDeck_v9_2_client.html       $R/render/v92/deck_client     $R/DFactory_SalesDeck_v9_2_client
python3 render.py $R/DFactory_SalesDeck_v9_2_working.html      $R/render/v92/deck_working    $R/DFactory_SalesDeck_v9_2_working
python3 render.py $R/DFactory_DossierTecnico_v9_2_client.html  $R/render/v92/dossier_client  $R/DFactory_DossierTecnico_v9_2_client
python3 render.py $R/DFactory_DossierTecnico_v9_2_working.html $R/render/v92/dossier_working $R/DFactory_DossierTecnico_v9_2_working

echo '--- registri ---'
python3 mk_register92.py

echo '--- QA ---'
python3 qa.py $R/DFactory_SalesDeck_v9_2_client.html sales
python3 qa.py $R/DFactory_SalesDeck_v9_2_working.html sales
python3 qa.py $R/DFactory_DossierTecnico_v9_2_client.html dossier
python3 qa.py $R/DFactory_DossierTecnico_v9_2_working.html dossier
python3 semantic9.py $R/DFactory_SalesDeck_v9_2_client.html $R/DFactory_DossierTecnico_v9_2_client.html

echo '--- le dieci condizioni di build ---'
python3 accept92.py
