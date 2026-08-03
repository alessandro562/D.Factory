# D.Factory · Open Inputs v9

Il registro completo è `DFactory_PlaceholderRegister_v9.md`: 220 voci con owner,
fonte e comportamento nelle due edizioni. Questo file dice un'altra cosa: **in che
ordine conviene chiuderle** e che cosa sblocca ciascuna.

---

## 1. Che cosa manca per pubblicare, in ordine di ritorno

### Blocco 1 · quattro risposte e il deck diventa mandabile

| # | input | placeholder | owner | sblocca |
|---|---|---|---|---|
| 1 | referente commerciale: nome, ruolo, email | `PH_CONTACT_NAME` `PH_CONTACT_ROLE` `PH_CONTACT_EMAIL` | Commerciale | **la slide 13 CTA**, oggi esclusa |
| 2 | prezzo e durata dell'audit | `PH_AUDIT_PRICE` `PH_AUDIT_DURATION` | Commerciale | la slide 12 e metà dell'appendice A3 |
| 3 | canone Connect e canone Insight | `PH_CONNECT_ANNUAL_FEE` `PH_INSIGHT_ANNUAL_FEE` | Commerciale + Direzione | **l'appendice A3**, oggi esclusa |
| 4 | validazione del dataset illustrativo | `PH_DATASET_VALIDATOR` `PH_DATASET_VALIDATION_DATE` | Tecnico | tredici canvas che oggi reggono su nove numeri non confermati |

Chiuse queste quattro, il Sales Deck client-facing passa da **12 slide a 13 + A3**
e smette di essere «un deck senza il finale».

Il numero 4 è quello che costa meno: non serve raccogliere dati, serve che
qualcuno che conosce una linea di confezionamento legga l'appendice A5 e dica se
500 pz/min, 0,14 €/pz, 95 kW in marcia e 38 kW a impianto fermo sono plausibili.
Mezz'ora. E mette al riparo il numero più grande del deck.

### Blocco 2 · sette risposte e il dossier smette di essere preliminare

| # | area | placeholder chiave | owner |
|---|---|---|---|
| 5 | modello di deployment | `PH_DEPLOYMENT_MODEL` `PH_SERVER_OWNER` | Tecnico + IT |
| 6 | sizing | `PH_MIN_CPU` `PH_MIN_RAM` `PH_MIN_STORAGE` `PH_RETENTION_DEFAULT` | Tecnico + IT |
| 7 | protocolli e versioni testate | `PH_SUPPORTED_PROTOCOLS` `PH_PROTOCOL_VERSIONS` | Tecnico |
| 8 | porte e regole firewall | `PH_REQUIRED_PORTS` `PH_FIREWALL_RULES` | Tecnico + IT |
| 9 | autenticazione e ruoli | `PH_AUTHENTICATION_MODEL` `PH_ROLE_MODEL` | Tecnico + IT |
| 10 | backup e ripristino | `PH_BACKUP_POLICY` `PH_BACKUP_FREQUENCY` | Tecnico + IT |
| 11 | proprietà del dato e licenza | `PH_DATA_OWNERSHIP` `PH_LICENSE_RIGHTS` `PH_END_OF_CONTRACT_DATA` | Legale |

Chiuse queste, gli annessi A1, A2 e A3 passano da metodo a esito e il titolo torna
**«Dossier tecnico»** senza «preliminare».

### Blocco 3 · il caso cliente

53 placeholder, 28 dei quali P0. Non si chiude a pezzi: o esiste un caso con
autorizzazione scritta, baseline, risultati, periodo, metodo e asset, o la slide
14 non esiste. **Non c'è una via di mezzo che non sia inventare**, e il master la
vieta esplicitamente al §5.3.

---

## 2. Le due frasi che nessuno ha ancora confermato

Sono le più pericolose del registro, perché suonano tecniche e nessuno le mette in
dubbio finché non arriva una due diligence.

| # | frase nel documento | dove | domanda | costo di chiuderla |
|---|---|---|---|---|
| T11 | «Verso le macchine il flusso è in sola lettura» | dossier 08 · A1 · deck A4 | è una regola tecnica assoluta o la configurazione standard prevista? | una risposta, una parola nel documento |
| T1/T7 | «Il dato resta nell'ambiente di deployment concordato con l'IT» | deck A4 · dossier 02 · 08 · A3 | dipende dal modello di deployment, che non è chiuso | una risposta |

Se la sola lettura non è assoluta, la frase diventa «configurazione standard
prevista in sola lettura». Sono quattro parole e cambiano il rischio contrattuale.

Altre due verifiche a costo zero, già in registro:

- **il perimetro dei 38 kW**: linea, macchine, ausiliari o stabilimento? Senza
  perimetro il consumo specifico non è confrontabile fra siti;
- **la frequenza di aggiornamento reale** delle viste operative: «aggiornato
  11:33» in una vista ricostruita deve corrispondere a un comportamento vero.

---

## 3. Prova aziendale · quattordici voci, zero usate

Anno di fondazione, anni di esperienza, clienti attivi, stabilimenti, linee,
macchine, progetti conclusi, settori autorizzati, retention, dimensione del team,
evidenza del gruppo, partnership, integrazione ERP di riferimento, Patent Box.

**Nessuna compare nei documenti.** La slide 10 «Tecnologia industriale, non solo
reporting» prova con il prodotto: produzione ed energia sullo stesso asse, si
parte dall'impianto esistente, software e competenze insieme. Non dice
«innovazione», «eccellenza» o «leadership».

Quando questi numeri arriveranno, ognuno va aggiunto al
`DFactory_ClaimRegister_v9.md` con la sua fonte **prima** di comparire in una
slide. Un numero in una slide senza una riga nel registro dei claim è un numero
che nessuno può difendere in riunione.

---

## 4. Asset reali · zero su quattro

Il master §10.3 fissa un obiettivo minimo: due screenshot reali, un report reale,
un asset industriale reale. Siamo a zero.

Le tredici viste di prodotto sono ricostruzioni grafiche, dichiarate canvas per
canvas. Funzionano — il QA lo conferma, la grammatica regge — ma un cliente che
chiede «me lo fai vedere davvero?» oggi non ha risposta.

Il registro degli asset è in `assets_v9/README.md`, con le dieci colonne che il
master chiede e nessuna riga da compilare. Ogni file che entrerà deve portarle
tutte **prima** di comparire in un canvas.

---

## 5. Che cosa succede se non arriva niente

Le quattro edizioni restano usabili così come sono, con questi limiti:

- la **working edition del deck** serve a chiudere gli input con D.Factory: mostra
  87 placeholder in chiaro, uno per uno, con il canvas in cui vivono. Non va a un
  cliente;
- la **client edition del deck**, 12 slide + 4 appendici, funziona per una
  presentazione in cui il prezzo si discute a voce e il contatto lo dà chi
  presenta. Non funziona come documento che il cliente riceve e legge da solo;
- la **working edition del dossier** è la lista della spesa per IT e OT: 104
  placeholder che dicono esattamente che cosa verrà chiesto loro;
- la **client edition del dossier** apre il dialogo tecnico e dichiara di essere
  preliminare. Non chiude una due diligence.

Nessuno di questi limiti è un difetto di progettazione. Sono la conseguenza di
104 input P0 che non ci sono — e i documenti lo dicono invece di nasconderlo.
