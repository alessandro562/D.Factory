# D.Factory · Open Inputs v8

Che cosa manca ancora, **che effetto ha ogni mancanza** sui due documenti, e chi
può chiuderla. Ordinato per quanto costa lasciarlo aperto, non per area.

I documenti V8 sono completi come struttura e come racconto. Nessuna pagina è stata
riempita con claim generici e nessuna porta placeholder: dove il valore non esiste,
la pagina dice che cosa si decide e chi lo decide.

---

## 1. Le cinque cose che cambiano di più

| # | input | senza | con | chi |
|---|---|---|---|---|
| 1 | **Screenshot reali del prodotto** | tutte le viste restano ricostruzioni dichiarate: 9 canvas del deck e 4 del dossier | il documento smette di descrivere il prodotto e comincia a mostrarlo | Tecnico + Marketing |
| 2 | **Prezzi: audit, setup, canone Connect, canone Insight, modello Refyn** | deck 10, 14 e appendice A3 mostrano la struttura, non gli importi. **Il deck non è un sales deck finale** | il deck si chiude e si può mandare | Commerciale + Direzione |
| 3 | **Validazione del dataset illustrativo** | i numeri sono coerenti fra loro ma nessuno li ha confermati plausibili per un impianto vero | il business case regge a una domanda tecnica in riunione | Commerciale + Tecnico |
| 4 | **Risposte IT/OT: deployment, sizing, autenticazione, backup, retention, licenza** | gli annessi A1–A3 dicono che cosa si verifica e chi decide, non i valori | il dossier passa una due diligence IT senza follow-up | Tecnico + IT |
| 5 | **Dati societari e contatto ufficiale** | la slide 12 prova solo con il prodotto; la 16 non ha un blocco contatti | il deck acquisisce la prova di chi lo firma | Direzione + Legale |

**Il numero 3 è quello che costa meno e vale di più.** Non richiede raccolta dati:
richiede che qualcuno che conosce una linea di confezionamento legga l’appendice A5
e dica se 500 pz/min, 0,14 €/pz, 95 kW in marcia e 38 kW a impianto fermo sono
plausibili. È mezz’ora di lavoro e mette al riparo tredici canvas.

---

## 2. Commerciale

| # | decisione | dove si vede | stato |
|---|---|---|---|
| C1 | prezzo e durata dell’audit | deck 14 · A3 | aperta |
| C2 | prezzo del setup | deck 14 · A3 | aperta |
| C3 | canone Connect | deck 10 · 14 · A3 | aperta |
| C4 | canone Insight | deck 10 · 14 · A3 | aperta |
| C5 | modello economico di Refyn | deck 10 · 14 | aperta |
| C6 | che cosa è compreso nell’avvio e che cosa è opzionale | deck A2 · A3 | aperta |
| C7 | durata contrattuale e rinnovo | deck 10 · A3 | aperta |
| C8 | prezzo e durata del pilot | deck 15 · dossier 13 | aperta |
| C9 | come si quota la sensoristica aggiuntiva | dossier 07 | aperta |
| C10 | livelli di supporto e loro contenuto | deck A2 · dossier 14 | aperta |

Finché C1–C5 restano aperte, l’appendice A3 mostra la struttura senza importi.
**Gli importi vanno inseriti in A3 soltanto quando sono approvati**: non vanno
sostituiti da intervalli, da «a partire da» o da placeholder.

---

## 3. Tecnico

| # | decisione | dove si vede | stato |
|---|---|---|---|
| T1 | modello di deployment: on-premise, VM, cloud privato | dossier 02 · 08 · A2 | aperta |
| T2 | sizing: OS, CPU, RAM, storage per le tre taglie | dossier A2 | aperta |
| T3 | rete: porte, protocolli, direzioni, segmentazione | dossier 08 · A1 | aperta |
| T4 | autenticazione, ruoli, accesso remoto | dossier 08 · A3 | aperta |
| T5 | logging, patching, cifratura | dossier A3 | aperta |
| T6 | backup, retention, restore, disaster recovery | dossier A3 | aperta |
| T7 | proprietà del dato, export, fine contratto | dossier A3 | aperta |
| T8 | licenza e diritti d’uso | dossier A3 | aperta |
| T9 | catalogo di compatibilità PLC verificato | dossier A1 | aperta |
| T10 | API: disponibilità, autenticazione, limiti, formati | dossier 12 · A1 | aperta |
| T11 | la **sola lettura** verso le macchine è regola assoluta o configurazione standard prevista? | dossier 08 · deck A4 | aperta |
| T12 | che cosa copre il **perimetro dei 38 kW**: linea, macchine, ausiliari o stabilimento | dossier 11 · deck 06 | aperta |
| T13 | frequenza di aggiornamento reale delle viste operative | dossier 04 | aperta |

**T11, T12 e T13 costano zero e cambiano una parola ciascuno.** Sono affermazioni
che oggi stanno nei documenti e che nessuno ha ancora confermato: se la sola lettura
non è una regola tecnica assoluta, la frase diventa «configurazione standard prevista
in sola lettura», e la differenza fra le due la nota solo chi fa una due diligence.

**T9 è la più costosa e la più preziosa.** Un catalogo di compatibilità verificata è
l’unica cosa che trasforma l’approccio multi-vendor da affermazione a prova. Finché
non esiste, l’annesso A1 resta il metodo di verifica e non il suo esito.

---

## 4. Aziendale e legale

| # | input | dove entrerebbe | stato |
|---|---|---|---|
| A1 | denominazione legale completa | cover dei due documenti | aperta |
| A2 | sede e recapito ufficiale | deck 16 | aperta |
| A3 | anno di fondazione | deck 12 | aperta |
| A4 | ruolo del Gruppo Clevertech, se dichiarabile | deck 12 | aperta |
| A5 | numero di clienti attivi | deck 12 | aperta |
| A6 | linee o macchine connesse | deck 12 | aperta |
| A7 | settori serviti | deck 12 | aperta |
| A8 | referenze autorizzate per iscritto | deck 12 | aperta |
| A9 | un caso cliente pubblicabile | deck 12 · dossier | aperta |
| A10 | logo ufficiale nella versione corretta | tutti i canvas | aperta |
| A11 | nota legale e classificazione del documento | piede di entrambi | aperta |

Nessuna di queste è stata compensata con parole. La slide 12 non dice
«innovazione», «eccellenza» o «leadership»: prova con il prodotto, e quando A3–A9
arrivano, prova anche con l’azienda.

---

## 5. Asset

| # | asset | dove | stato |
|---|---|---|---|
| S1 | screenshot reali del prodotto | deck 01, 03, 04, 05, 06, 07, 08, 09, 12 · dossier 04, 05, 09 | aperta |
| S2 | foto di un impianto o di un quadro | deck 01, 12 · dossier 01 | aperta |
| S3 | un report reale esportato | dossier 12 | aperta |
| S4 | schema di rete reale anonimizzato | dossier 08 | aperta |
| S5 | un caso tecnico autorizzato | deck 12 | aperta |
| S6 | logo ufficiale | tutti | aperta |
| S7 | eventuali loghi cliente autorizzati | deck 12 | aperta |

---

## 6. Validazione del dataset · V1

Questi sono i parametri che tengono in piedi tredici canvas. Sono elencati
nell’appendice A5 del deck. Non servono dati reali per validarli: serve che qualcuno
dica se sono plausibili.

| parametro | valore usato | plausibile? |
|---|---|---|
| cadenza nominale | 500 pz/min | da confermare |
| margine unitario | 0,14 €/pz | da confermare |
| margine al minuto | 70 €/min | conseguenza dei due sopra |
| potenza in marcia | 95 kW | da confermare |
| potenza a impianto fermo | 38 kW | da confermare · vedi anche T12 |
| prezzo dell’energia | 0,22 €/kWh | dal contratto di fornitura |
| fattore di emissione | 0,35 kgCO₂e/kWh | dal mix dichiarato dal fornitore |
| settimane produttive | 46 | da confermare |
| durata del turno | 480 min · un turno al giorno | da confermare |
| turni produttivi in un anno | 230 | conseguenza dei due sopra |

Sono coerenti fra loro e ogni numero del deck si ricostruisce a mano da questi:
735 kWh nel turno, 162 €, 227.000 pezzi, 3,2 kWh e 0,71 € per 1.000 pezzi, 71,4% di
OEE, 15.680 € su sette giorni, 309.120 € all’anno. Se uno di questi cambia, cambiano
tutti gli altri — e vanno rifatti in un punto solo, l’appendice A5.

---

## 7. Che cosa succede se non arriva niente

I due documenti restano usabili così come sono, con questi limiti dichiarati:

- il **deck** funziona per una presentazione tecnico-commerciale in cui il prezzo si
  discute a voce; non funziona come documento che il cliente riceve e legge da solo
  per decidere un budget;
- il **dossier** funziona per aprire il dialogo con IT e OT — dice esattamente che
  cosa verrà chiesto loro — ma non chiude una due diligence;
- entrambi vanno accompagnati dalla frase che già portano in piede: le viste sono
  ricostruzioni e i dati sono illustrativi.

Nessuna di queste limitazioni è un difetto di progettazione: è la conseguenza di
input che non ci sono. Compensarle con copy generico le renderebbe invisibili senza
renderle false — e questo è esattamente ciò che i due documenti non fanno.
