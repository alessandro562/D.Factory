# D.Factory · Validazione del dataset V9.1

**Scheda da compilare nella sessione del §5.** Trenta-quarantacinque minuti, con
chi conosce una linea di confezionamento, il responsabile energia, il
commerciale e l'autore del dataset.

È il gate **G3**. Finché è aperto, la client edition del deck **non pubblica i
valori annualizzati**: la slide 11 mostra la formula, la slide 13 rimanda al
conto sulla linea del cliente. Non è una scelta editoriale: è il §5.3 applicato.

---

## 1. Gli undici parametri · §5.1

| # | Parametro | Valore V9 | Domanda del piano | Plausibile | Valore corretto |
|--:|---|---:|---|:--:|---|
| 1 | cadenza | 500 pz/min | plausibile per la linea mostrata? | ☐ | |
| 2 | margine unitario | 0,14 €/pz | margine, contribuzione o valore? | ☐ | |
| 3 | potenza in marcia | 95 kW | quale perimetro? | ☐ | |
| 4 | potenza a fermo | 38 kW | include che cosa? | ☐ | |
| 5 | prezzo energia | 0,22 €/kWh | periodo e fonte? | ☐ | |
| 6 | fattore emissivo | 0,35 kgCO₂e/kWh | fonte e anno? | ☐ | |
| 7 | durata turno | 480 min | un turno reale? | ☐ | |
| 8 | turni annui | 230 | uno al giorno? | ☐ | |
| 9 | fermo settimanale | 96 min | plausibile? | ☐ | |
| 10 | settimane produttive | 46 | quale calendario? | ☐ | |
| 11 | quota recuperabile | 50% | su quale base? | ☐ | |

## 2. Le nove domande metodologiche · §5.2

| # | Domanda | Risposta |
|--:|---|---|
| 1 | il margine è il margine di contribuzione del vincolo? | |
| 2 | la produzione persa si recupera in un altro turno? | |
| 3 | il fermo riduce la vendita o solo la capacità? | |
| 4 | la linea è il collo di bottiglia? | |
| 5 | la potenza a fermo è costante? | |
| 6 | i 38 kW includono gli ausiliari? | |
| 7 | l'energia evitabile si calcola sul delta 95−38 o sull'intera potenza a fermo? | |
| 8 | il valore va annualizzato su 46 settimane? | |
| 9 | il 50% recuperabile è una stima prudente? | |

**La domanda 7 cambia un numero pubblicato.** Oggi gli 810 € sono calcolati sui
16 kWh per turno a impianto fermo, cioè sull'intera potenza a fermo × 26 minuti.
Se il criterio corretto è il delta 95−38, il numero cambia. È l'unica delle nove
che ha già un effetto aritmetico su una cifra del deck.

## 3. La catena, se i valori restano

```
scenario: un turno al giorno, 5 giorni, 46 settimane = 230 turni

500 pz/min × 0,14 €/pz              →  70 €/min
fermo 18 min                        →  1.260 €
turno 26 min                        →  1.820 €
7 giorni, 58 eventi, 224 min        →  15.680 €  ·  prima causa 43%
96 min/sett × 70 €/min × 46 sett    →  309.120 €  ·  metà 154.560 €
454 min × 95 kW + 26 min × 38 kW    →  719 + 16 = 735 kWh
735 kWh × 0,22 €/kWh                →  162 €
454 min × 500 pz/min                →  227.000 pezzi
735 ÷ 227.000 × 1.000               →  3,2 kWh · 0,71 € · 1,13 kgCO₂e / 1.000 pz
94,6% × 79% × 95,6%                 →  OEE 71,4%
16 kWh × 230 turni × 0,22 €/kWh     →  810 €
```

Verificata a calcolo: tutti i valori tornano. **Coerenza interna e plausibilità
industriale sono due cose diverse**, e questa scheda serve alla seconda.

## 4. Esito · §5.3

| Esito | Che cosa comporta | Scelta |
|---|---|:--:|
| approvato | si inseriscono validatore e data, i valori restano, si usa «scenario illustrativo validato» | ☐ |
| parzialmente approvato | si sostituiscono i valori dubbi e si rifà la catena in un punto solo, l'appendice A5 | ☐ |
| non approvato | restano formula e periodo osservato, escono 309.120 € e 154.560 € | ☐ |

Oggi il documento si comporta come nel terzo caso, perché è lo stato di fatto.

| Campo | Valore |
|---|---|
| `PH_DATASET_VALIDATOR` | |
| `PH_DATASET_VALIDATION_DATE` | |
| `PH_DATASET_ASSUMPTION_OWNER` | |

## 5. Il messaggio sulla leva energia · §5.4

Copy raccomandato dal piano, **già applicato** alla slide 05 e al piede della
slide 11:

> In questo scenario il valore principale nasce dalla capacità recuperabile. Il
> dato energetico completa la lettura e quantifica il consumo improduttivo dello
> stesso evento.

Le due leve non vengono pareggiate artificialmente: 154.560 € contro 810 € è una
differenza vera, e mostrarla com'è vale più che nasconderla.
