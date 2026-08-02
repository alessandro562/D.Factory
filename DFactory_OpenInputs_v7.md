# D.Factory · Open Inputs v7

Che cosa manca perché i due documenti siano pubblicabili come sono. Ordinato per impatto,
non per facilità di reperimento.

Nessuno di questi input compare come placeholder nei file client-facing: dove il dato non
c'è, il documento mostra la struttura e dichiara che il valore si compila altrove.

---

## P0 · bloccanti per una versione completa

### Economia · il deck non è sales-ready finché queste non sono chiuse

| # | input | owner | dove serve | che cosa cambia |
|---|---|---|---|---|
| 1 | Prezzo audit | Direzione commerciale | A3, slide 11 | La struttura economica diventa un'offerta |
| 2 | Durata audit | Commerciale | slide 11, 12 | La CTA torna contrattuale |
| 3 | Partecipanti audit | Commerciale | slide 12 | Chi serve in sala determina la fattibilità della data |
| 4 | Output audit | Commerciale + Delivery | slide 12 | Oggi «perimetro, gap, ipotesi pilot» è una promessa generica |
| 5 | Fascia prezzo setup | Delivery + commerciale | A3 | — |
| 6 | Canone Connect per linea | Commerciale | A1, A3 | — |
| 7 | Canone Insight per linea | Commerciale | A1, A3 | Il salto di prezzo fra i due livelli è ciò che rende leggibile la scala |
| 8 | Pricing Refyn | Direzione prodotto | A1, A3 | Oggi «previsto» senza economia |
| 9 | Servizi inclusi nel canone | Commerciale | A2, A3 | Oggi tutti i servizi sono «attivabili»: nessuno sa cosa è compreso |
| 10 | Servizi opzionali e loro prezzo | Commerciale | A2, A3 | — |
| 11 | Durata contrattuale e rinnovo | Legale + commerciale | A3 | — |
| 12 | Supporto e SLA | Delivery | dossier 19 | Oggi «condizioni da formalizzare» |

### Tecnica · il dossier non è pronto per IT finché queste non sono chiuse

| # | input | owner | dove serve |
|---|---|---|---|
| 13 | Modello di deployment | Tecnico | dossier 15 |
| 14 | Requisiti server: CPU, RAM, storage, sistema operativo | Tecnico | dossier 15 |
| 15 | Porte e protocolli | Tecnico | dossier 15 |
| 16 | Autenticazione e ruoli | Tecnico | dossier 15 |
| 17 | Backup, retention e disaster recovery | Tecnico | dossier 15 |
| 18 | Licenza e condizioni di fine contratto | Legale | dossier 15 |
| 19 | Proprietà dei dati | Legale | dossier 15, 19 |

### Identità

| # | input | owner | dove serve |
|---|---|---|---|
| 20 | Denominazione legale e contatto ufficiale | Legale + Direzione | copertine, slide 12 |

**La slide 12 non porta un contatto.** Il brief chiede di indicarlo e vieta i placeholder:
finché la denominazione ufficiale non è confermata, il blocco resta senza recapito. È una
riga da aggiungere, non un ridisegno.

---

## P1 · molto importanti

| # | input | owner | perché pesa |
|---|---|---|---|
| 21 | Screenshot reali del prodotto | Tecnico + Marketing | Tutte le viste dei due documenti sono ricostruzioni dichiarate. Con schermate vere non cambia l'impianto: cambia la credibilità |
| 22 | Un report reale esportato | Tecnico | Dossier 17 |
| 23 | Foto di una linea installata | Marketing | Deck 01 o 09 |
| 24 | Un caso cliente autorizzato | Direzione + Legale | Deck 09 · oggi la credibilità poggia su tre prove strutturali, non su prove sociali |
| 25 | Una citazione cliente | Direzione + Legale | Deck 09 |
| 26 | Base installata validata | Direzione | Deck 09 |
| 27 | Settori approvati | Direzione | Slide 01 · vedi la decisione qui sotto |
| 28 | Compatibilità ERP verificata su un progetto reale | Tecnico | Deck A4, dossier 17 |
| 29 | Fattori emissivi documentati | Tecnico | Dossier 12 · oggi 0,35 kgCO₂e/kWh è un valore illustrativo dichiarato |
| 30 | **Validazione di plausibilità del dataset illustrativo** | Commerciale + Tecnico | Vedi §2 |

---

## 2. Il dataset illustrativo va validato come plausibile

Tutti i numeri dei due documenti discendono da otto parametri dichiarati nel piede della
slide 10. Sono stati scelti per rendere l'aritmetica verificabile, **non presi da un
impianto reale**:

```
500 pz/min · margine 0,14 €/pz · 95 kW in marcia · 38 kW a linea ferma
0,22 €/kWh · 0,35 kgCO₂e/kWh · 46 settimane
disponibilità 94,6 % · prestazione 79 % · qualità 95,6 %
```

Serve che qualcuno che conosce una linea F&B reale dica se sono plausibili. Un esempio non
plausibile è peggio di nessun esempio, perché il primo a notarlo è il controllo di gestione
del cliente — ed è anche il primo a decidere.

---

## 3. Due decisioni di posizionamento, non dati mancanti

### 3.1 «food & beverage» oppure «linee industriali»

La slide 01 dice oggi **«per linee food & beverage»**. È la formulazione ereditata da tutto
il materiale sorgente, dal context brief in avanti, e il brief V7 la ammette a condizione
che sia una scelta deliberata di posizionamento.

Se il mercato è più largo, la riga diventa «per linee industriali»: è una modifica su una
slide sola. Ma è una decisione commerciale, non redazionale, e non la prendo io.

### 3.2 La denominazione legale nei piedi

I due documenti portano la filigrana `D.Factory`. La denominazione legale della società non
compare da nessuna parte, come chiede il brief finché non è verificata. Al momento della
pubblicazione va decisa e inserita, e con essa il contatto della slide 12.

---

## 4. Che cosa i documenti dichiarano di non sapere

Perché non venga scambiato per una dimenticanza:

| dichiarazione | dove |
|---|---|
| «durate da definire in solution design» | slide 11 |
| «importi in corso di approvazione» | appendice A3 |
| «scenario illustrativo · non risultato cliente» | slide 10, 12 |
| «vista ricostruita · dati illustrativi» | ogni canvas con una schermata |
| «valori da compilare in solution design» | dossier 15 |
| «possibile integrazione con ERP, previa verifica tecnica» | dossier 17, deck A4 |
| «la compatibilità si verifica sull'impianto reale» | dossier 14 |
| «CO₂ calcolata o stimata» | dossier 12, deck 07 |
| «fattori da validare» | dossier 12 |
| «condizioni da formalizzare nella proposta e nel contratto» | dossier 19 |

Sono dieci punti in cui i documenti scelgono di dire «non ancora» invece di riempire lo
spazio. Ognuno di essi diventa una frase migliore appena l'input corrispondente arriva.
