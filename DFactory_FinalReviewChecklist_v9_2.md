# D.Factory · Final Review Checklist V9.2

Il 10% che resta. Nient'altro.

Questa lista è chiusa: se una revisione finale chiede qualcosa che non è qui
dentro, sta chiedendo un rifacimento, non una revisione. Il §26 lo dice
esplicitamente — al 10% finale non deve restare redesign, riscrittura
narrativa, nuova struttura, nuove pagine, nuova offerta, nuove tassonomie.

**Come si usa:** ogni riga ha il campo del registro, chi risponde, dove finisce
nei documenti e che cosa si sblocca quando è spuntata. Compilato il gruppo, si
cambia lo stato in `gates.py` e si rilancia il build: i documenti si aggiornano
da soli.

---

## Commerciale · 11 voci

| ✓ | voce | campo | owner | dove finisce |
|:-:|---|---|---|---|
| ☐ | referente | `PH_CONTACT_NAME` `PH_CONTACT_ROLE` | Commerciale | deck 13 · dossier 01 |
| ☐ | email | `PH_CONTACT_EMAIL` | Commerciale | deck 13 · dossier 01 |
| ☐ | sessione iniziale | `PH_AUDIT_DURATION` `PH_AUDIT_PARTICIPANTS` | Commerciale | deck 13 |
| ☐ | audit | `PH_AUDIT_NAME` `PH_AUDIT_INPUTS` `PH_AUDIT_DELIVERABLES` | Commerciale + Tecnico | deck 12, 13 |
| ☐ | prezzo audit | `PH_AUDIT_PRICE` | Direzione | deck A3 |
| ☐ | setup | `PH_SETUP_FIRST_LINE` | Direzione | deck A3 |
| ☐ | Connect | `PH_CONNECT_ANNUAL_FEE` | Direzione | deck A3 |
| ☐ | Insight | `PH_INSIGHT_ANNUAL_FEE` | Direzione | deck A3 |
| ☐ | Refyn | `PH_REFYN_PRICING_MODEL` | Direzione | deck 09, 12, A1, A3 · dossier 03 |
| ☐ | servizi inclusi | `PH_SERVICES_INCLUDED` `PH_SERVICES_OPTIONAL` | Commerciale | deck 08, A1, A2 · dossier 03 |
| ☐ | durata contratto | `PH_CONTRACT_TERM` `PH_RENEWAL_TERMS` | Legale + Direzione | deck 09, A3 |

**Sblocca:** G1 → la client edition del deck diventa inviabile.
G2 → l'appendice A3 rientra, la quarta colonna di A2 si compila, la slide 12
mostra le voci con importo.

---

## Dataset · 8 voci

| ✓ | voce | campo | valore illustrativo oggi | owner |
|:-:|---|---|---|---|
| ☐ | throughput | `PH_DATASET_THROUGHPUT` | 500 pz/min | Tecnico |
| ☐ | margine | `PH_DATASET_MARGIN_UNIT` | 0,14 €/pz | Direzione |
| ☐ | potenze | `PH_DATASET_RUNNING_POWER` `PH_DATASET_STOPPED_POWER` | 95 kW · 38 kW | Tecnico |
| ☐ | fermo | `PH_DATASET_STOP_MIN_WEEK` | 96 min/settimana | Tecnico |
| ☐ | settimane | `PH_DATASET_SHIFTS_PER_YEAR` | 46 settimane · 230 turni | Tecnico |
| ☐ | quota recuperabile | `PH_DATASET_RECOVERABLE_SHARE` | 50% | Tecnico |
| ☐ | prezzo energia | `PH_DATASET_ENERGY_PRICE` | 0,22 €/kWh | Acquisti |
| ☐ | fattore emissivo | `PH_EMISSION_FACTOR_SOURCE` | 0,35 kgCO₂e/kWh | Acquisti |

Più i due campi che dicono chi ha validato e quando:
`PH_DATASET_VALIDATOR`, `PH_DATASET_VALIDATION_DATE`.

**Sblocca:** G3 → tornano 309.120 €, 154.560 € e 810 € nella client edition,
rientra l'appendice A5, la slide 13 mostra il costo annuo. L'etichetta diventa
*«Scenario illustrativo validato · non risultato cliente»* — resta uno scenario,
non diventa un risultato di cliente.

**Attenzione a due coerenze**, che la V9.2 ha già dovuto correggere una volta:

- 230 turni all'anno = 46 settimane × 5 giorni × **un turno al giorno**. Se il
  calendario cambia, cambiano gli 810 € e va rifatto tutto il capitolo energia.
- 70 €/min = 500 pz/min × 0,14 €/pz. Se cambia uno dei due, cambia anche il
  margine al minuto, e con lui i 1.260 €, i 6.720 € e i 15.680 €.

---

## Tecnico · 13 voci

| ✓ | voce | campo | owner | dove finisce |
|:-:|---|---|---|---|
| ☐ | deployment | `PH_DEPLOYMENT_MODEL` | Tecnico + IT | dossier 02, 08 |
| ☐ | OS | `PH_SUPPORTED_OS` | Tecnico | dossier 08 |
| ☐ | CPU | `PH_MIN_CPU` | Tecnico | dossier A2 |
| ☐ | RAM | `PH_MIN_RAM` | Tecnico | dossier A2 |
| ☐ | storage | `PH_MIN_STORAGE` `PH_STORAGE_GROWTH_RULE` | Tecnico | dossier A2 |
| ☐ | protocolli | `PH_SUPPORTED_PROTOCOLS` `PH_PROTOCOL_VERSIONS` | Tecnico | dossier A1 |
| ☐ | porte | `PH_REQUIRED_PORTS` `PH_FIREWALL_RULES` | Tecnico + IT | dossier 08, A1 |
| ☐ | autenticazione | `PH_AUTHENTICATION_MODEL` `PH_ROLE_MODEL` | Tecnico + IT | dossier A3 |
| ☐ | backup | `PH_BACKUP_POLICY` `PH_RPO` `PH_RTO` | Tecnico + IT | dossier A3 |
| ☐ | retention | `PH_RETENTION_DEFAULT` | Tecnico + IT | dossier A2, A3 |
| ☐ | dati | `PH_DATA_OWNERSHIP` `PH_DATA_EXPORT_AT_EXIT` | Legale | dossier A3 |
| ☐ | licenza | `PH_LICENSE_RIGHTS` | Legale | dossier A3 |
| ☐ | remoto | `PH_REMOTE_SUPPORT_POLICY` `PH_PATCHING_POLICY` | Tecnico + IT | dossier 14, A3 |

**Sblocca:** G4 → il dossier perde «preliminare», l'annesso A2 mostra i valori
per fascia, l'annesso A3 diventa «specifica concordata», gli esiti dell'annesso
A1 passano da «da verificare» a supportato / condizionato / da aggiungere.

---

## Credibilità · 4 voci

| ✓ | voce | campo | vincolo |
|:-:|---|---|---|
| ☐ | asset reale deck | uno fra `PH_REAL_SCREENSHOT_MAPST` `PH_REAL_SCREENSHOT_NEW_UI` `PH_REAL_INSTALLATION_PHOTO` | **uno solo**: un deck con un asset vero e dodici ricostruzioni dichiarate è credibile, uno con tredici asset misti è confuso |
| ☐ | asset reali dossier | due fra `PH_REAL_SCREENSHOT_MARENERGY` `PH_REAL_REPORT_EXPORT` `PH_REAL_LINE_DIAGRAM` `PH_REAL_SENSOR_PHOTO` | ciascuno con etichetta, autorizzazione e anonimizzazione |
| ☐ | fatto aziendale | uno fra `PH_GROUP_RELATIONSHIP` `PH_COMPANY_FOUNDING_YEAR` `PH_PROJECTS_COMPLETED` `PH_ACTIVE_LINES` | **massimo due** in slide 10; nessun numero ereditato non validato |
| ☐ | eventuale caso cliente | `PH_CASE_STUDY_READY` + gli otto elementi | o tutti e otto, o la slide non esiste |

**Sblocca:** G5 → l'invio a freddo e il passaggio in procurement.

Ogni file va registrato in `assets_v9_2/AssetRegister.md` **prima** di essere
usato: la condizione di build n. 5 fa fallire il build su un asset non
registrato.

---

## Legale · 6 voci

| ✓ | voce | che cosa serve | dove finisce |
|:-:|---|---|---|
| ☐ | denominazione | ragione sociale come in visura | dossier 01 |
| ☐ | footer | dicitura legale, sede, P.IVA | deck e dossier, piede |
| ☐ | privacy | informativa se i documenti circolano via email | fuori documento |
| ☐ | proprietà dati | approvazione della formulazione del Claim Register | dossier A3 |
| ☐ | licenza | diritti d'uso, accesso, export | dossier A3 |
| ☐ | fine contratto | export finale e cancellazione | dossier A3 |

**La riga che vale la pena leggere due volte:** la formulazione sulla proprietà
dei dati **esiste già**, è scritta nel Claim Register sotto la chiave
`proprieta`, e **non è pubblicata in nessuno dei quattro HTML**. Il §25 lo
vieta senza approvazione legale. Quando il legale approva, si sposta dal
registro all'annesso A3 e basta.

---

## Che cosa la revisione finale non deve fare

- Non riaprire la struttura: 13 + 4 nel deck, 14 + 4 nel dossier.
- Non aggiungere pagine, template, tassonomie, roadmap, matrici di maturità.
- Non trasformare lo scenario illustrativo in un caso cliente.
- Non pubblicare numeri aziendali non validati per riempire la slide 10.
- Non chiamare «Dossier tecnico» il dossier finché G4 è aperto: il build
  fallisce, ed è giusto così.
- Non dichiarare «finale» la client edition finché G1 o G2 sono aperti.

---

## Stato alla consegna V9.2

| gate | stato | voci da spuntare |
|---|---|--:|
| G1 identità e CTA | `OPEN` | 4 |
| G2 modello commerciale | `OPEN` | 7 |
| G3 dataset | `OPEN` | 8 |
| G4 IT/OT | `OPEN` | 13 |
| G5 evidenze | `OPEN` | 3 |
| CASE caso cliente | `NO` | 1 |
| legale | — | 6 |
| **totale** | | **42** |

Quarantadue caselle. Nessuna di loro è un lavoro di design.
