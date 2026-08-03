# D.Factory · Decisioni tecniche V9.1

I tre claim del §6, con la formulazione scelta e il suo stato. Due sono già
applicati ai documenti; il terzo no, e il motivo è scritto.

---

## 1. Sola lettura verso le macchine · §6.1

**Domanda:** il prodotto opera sempre in sola lettura verso le macchine?

| | Formulazione | Scelta |
|---|---|:--:|
| A | Il sistema acquisisce dati in sola lettura e non invia comandi alle macchine. | ☐ |
| **B** | **La configurazione standard privilegia l'acquisizione in sola lettura. Eventuali scambi ulteriori vengono definiti nel solution design.** | ☑ |
| C | Direzione e natura dei flussi vengono definite nel solution design. | ☐ |

**Applicata: B**, come raccomanda il piano — «Usare B, salvo conferma tecnica di A».

| dove | prima | dopo |
|---|---|---|
| dossier 08, sottotitolo | «Verso le macchine il flusso è in sola lettura.» | la formulazione B per esteso |
| dossier 08, pannello | «sola lettura» | «sola lettura, in configurazione standard» |
| dossier 08, diagramma | «normalizzazione e marcatura temporale» | «configurazione standard · normalizzazione e marcatura temporale» |
| deck A4, FAQ | «La lettura dei segnali non richiede scrittura verso le macchine.» | la formulazione B |

**Se arriva la conferma tecnica di A**, si passa ad A e la differenza è di quattro
parole. Fino ad allora B è la sola che non prometta più di quanto sia stato
verificato.

## 2. Residenza dei dati · §6.2

| Domanda | Risposta |
|---|---|
| dove risiede il database? | |
| esistono servizi cloud? | |
| esiste telemetria? | |
| esistono log remoti? | |
| come avvengono aggiornamenti e supporto? | |
| il backup può essere esterno? | |
| chi accede ai dati? | |

**Copy prudente applicata**, dal §6.2:

> Il modello di deployment, la residenza e il trattamento dei dati vengono
> concordati con l'IT e formalizzati nel solution design.

Sostituisce, nel pannello del dossier 08, «Sono decisioni di progetto, non limiti
del prodotto». Dice la stessa cosa senza suggerire che la scelta sia già fatta.

## 3. Proprietà dei dati e licenza · §6.3

| Ambito | Contenuto |
|---|---|
| **dati del cliente** | dati grezzi · storico · export · report generati |
| **proprietà D.Factory** | software · modelli · formule standard · codice · licenza · documentazione |

Copy raccomandata dal piano:

> I dati operativi restano nella disponibilità del cliente. Diritti d'uso del
> software, modalità di accesso ed export a fine contratto sono definiti
> nell'accordo di licenza.

**Non applicata ai documenti.** Il §6.3 dice «Non pubblicare finché non approvato
legalmente», e nessuno l'ha approvata. L'annesso A3 continua a dire che cosa si
decide e chi decide — che è vero oggi — e la formulazione resta qui, in attesa.

| Campo | Stato |
|---|---|
| approvazione legale | ☐ |
| data | |
| approvata da | |

## 4. Le tre verifiche a costo zero

Erano nel registro V9 come T11, T12, T13. Due sono state chiuse dal §6; la terza
resta.

| # | Domanda | Stato |
|---|---|---|
| T11 | sola lettura: regola assoluta o configurazione standard? | **chiusa** con la formulazione B |
| T12 | perimetro dei 38 kW: linea, macchine, ausiliari o stabilimento? | **aperta** — è la domanda 6 del §5.2, e il dossier 11 ora dichiara che si chiude nel solution design |
| T13 | frequenza di aggiornamento reale delle viste operative | **aperta** — «aggiornato 11:33» nella vista Connect deve corrispondere a un comportamento vero |
