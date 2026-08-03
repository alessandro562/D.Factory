# D.Factory · Decisioni commerciali V9.1

**Scheda da compilare nel workshop del §4.** Novanta minuti, con direzione,
commerciale, delivery, amministrazione e prodotto.

Le colonne «Decisione» sono vuote. Non le ho compilate perché sono decisioni
aziendali, e il piano al §2.2 vieta di inventarle. Le colonne
«Raccomandazione» riportano quello che il piano stesso propone: sono un punto di
partenza per la discussione, non una scelta già fatta.

Quando una riga viene decisa, si aggiorna `work_v91/gates.py` e si rigenera. Non
si toccano gli HTML a mano.

---

## 1. G1 · Identità e CTA · blocca la pubblicazione del deck

| Campo | Raccomandazione del piano | Decisione | Approvata da | Data |
|---|---|---|---|---|
| `PH_COMPANY_LEGAL_NAME` | — | | | |
| `PH_CONTACT_NAME` | — | | | |
| `PH_CONTACT_ROLE` | — | | | |
| `PH_CONTACT_EMAIL` | — | | | |
| `PH_AUDIT_NAME` | «Sessione di perimetrazione» come primo passo gratuito, «Audit tecnico-economico» come passo a pagamento (§4.1) | | | |
| `PH_AUDIT_DURATION` | — | | | |
| `PH_AUDIT_PARTICIPANTS` | produzione · manutenzione · energia · IT/OT (già nel deck) | | | |
| `PH_AUDIT_INPUTS` | schema linea · elenco PLC · contatori · dati già disponibili (già nel deck) | | | |
| `PH_AUDIT_DELIVERABLES` | i nove del §4.2 | | | |

**Finché G1 è aperto** la CTA resta nel deck ma senza referente: il documento si
presenta dal vivo, non si invia. È la conseguenza più costosa dell'intero
registro, e si chiude con quattro righe.

## 2. Primo passo commerciale · §4.1

| Opzione | Che cosa compra il cliente | Scelta |
|---|---|:--:|
| A · audit a pagamento | verifica dati, perimetro, mappa integrazioni, gap, business case, proposta pilot | ☐ |
| B · assessment gratuito limitato | incontro, questionario, valutazione preliminare | ☐ |
| C · pilot diretto | solo con perimetro noto e segnali già verificati | ☐ |
| **Raccomandazione del piano** | **due livelli: sessione di perimetrazione gratuita + audit a pagamento** | ☐ |

Il deck V9.1 chiude già sulla sessione di perimetrazione, come prevede il §4.1.
Se la scelta cade su A o C, cambia la slide 13.

## 3. Deliverable dell'audit · §4.2

I nove raccomandati dal piano. Segnare quelli confermati.

| # | Deliverable | Confermato |
|--:|---|:--:|
| 1 | mappa della linea e delle sorgenti | ☐ |
| 2 | inventario PLC, contatori e sensori | ☐ |
| 3 | gap di misura | ☐ |
| 4 | perimetro del pilot | ☐ |
| 5 | architettura preliminare | ☐ |
| 6 | requisiti IT/OT | ☐ |
| 7 | KPI prioritari | ☐ |
| 8 | business case sul dato del cliente | ☐ |
| 9 | proposta economica | ☐ |

## 4. G2 · Modello di prezzo · §4.3

Struttura raccomandata: **audit + setup + canone annuale per linea + servizi**.

### Setup — che cosa comprende

| Voce | Compresa | Note |
|---|:--:|---|
| prima linea | ☐ | |
| mapping | ☐ | |
| dashboard | ☐ | |
| formazione | ☐ | |
| integrazione con il gestionale | ☐ | |
| sensoristica | ☐ | |
| trasferte | ☐ | |

### Canone

| Decisione | Valore |
|---|---|
| unità di misura | linea · sito · altro |
| canone base per sito | sì · no |
| differenza Connect / Insight | |
| supporto compreso | |
| retention compresa | |
| utenti compresi | |
| aggiornamenti compresi | |
| periodicità del pagamento | annuale · mensile |

### Linee successive

| Decisione | Valore |
|---|---|
| setup ridotto | |
| canone ridotto | |
| soglie di volume | |
| multi-sito | |

### Refyn · §4.3

| Modello | Descrizione | Scelta |
|---|---|:--:|
| 1 | pilot dedicato + quotazione | ☐ |
| 2 | uplift percentuale su Insight | ☐ |
| 3 | canone software + review periodica compresa | ☐ |

**Raccomandazione del piano, già applicata al deck V9.1:** modello 1 — «Progetto
pilota dedicato, con quotazione sul perimetro». Nessun listino Refyn.

### Importi

| Campo | Importo | Approvato da | Data |
|---|---|---|---|
| `PH_AUDIT_PRICE` | | | |
| `PH_SETUP_FIRST_LINE` | | | |
| `PH_SITE_BASE_FEE` | | | |
| `PH_CONNECT_ANNUAL_FEE` | | | |
| `PH_INSIGHT_ANNUAL_FEE` | | | |
| `PH_ADDITIONAL_LINE_FEE` | | | |
| `PH_PREMIUM_SUPPORT_FEE` | | | |

**Finché G2 è aperto** l'appendice pricing non entra nella client edition.

## 5. Servizi compresi · §4.4

| Livello | Raccomandazione del piano | Confermato |
|---|---|:--:|
| Connect | supporto standard · aggiornamenti · onboarding · report standard · una revisione post go-live | ☐ |
| Insight | tutto Connect · configurazione KPI · formule · una performance & energy review iniziale | ☐ |
| Refyn | tutto Insight · setup del ciclo azioni · review periodica · verifica baseline e beneficio | ☐ |

Opzionali raccomandati: assessment · nuove integrazioni · nuovi KPI · report
direzionali · review ricorrenti · improvement sprint · formazione aggiuntiva ·
supporto premium · scale-up.

**Nota sulla §9.15.** Il piano chiede di aggiungere la colonna «incluso /
opzionale» all'appendice servizi. Non l'ho aggiunta: `PH_SERVICES_INCLUDED` è un
campo di G2 e la colonna sarebbe otto righe identiche che dicono «da decidere».
Entra nel momento in cui questa tabella viene compilata.

## 6. Contratto · §4.5

| Campo | Valore | Approvato da |
|---|---|---|
| `PH_CONTRACT_TERM` durata minima | | |
| `PH_RENEWAL_TERMS` rinnovo | | |
| `PH_TERMINATION_TERMS` recesso | | |
| `PH_PAYMENT_TERMS` pagamento | | |
| `PH_INDEXATION` indicizzazione | | |
| `PH_END_OF_CONTRACT_DATA` dati a fine rapporto | | |
| `PH_DATA_EXPORT_AT_EXIT` export | | |
| `PH_LICENSE_RIGHTS` licenza | | |

---

## Come si chiude

Compilata la scheda, in `work_v91/gates.py`:

```python
STATO = {'G1': 'APPROVED', 'G2': 'APPROVED', ...}
```

e si rilancia il build. La CTA prende il referente, l'appendice pricing rientra
nella client edition, e `accept.py` aggiorna i criteri del §13.
