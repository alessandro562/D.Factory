# D.Factory · QA v8

39 canvas: 21 nel Sales Deck (16 slide + 5 appendici), 18 nel Dossier (14 pagine
core + 4 annessi). **Zero flag.**

---

## 1. Sales Deck · soglie `sales`

Copy ≤ 45 parole · superficie visiva ≥ 55% · corpo minimo 18 px per la copy,
12 px dentro le viste, 12,4 px per il testo di servizio.

```
id                          copy vista   cont   meta   diag  vista   vis%  flag
s01_cover                     18    50     19     19      —   12.5   58.3   —
s02_tensione                  21    40     18   12.5      —   12.5   58.9   —
s03_categoria                 24    64     18   12.5      —     13   59.4   —
s04_evento                    25    32     19   12.5      —   12.5   58.3   —
s05_prodotto                  10    37     44   12.5      —   12.5   67.8   —
s06_energia                   16    28     18   12.5      —   12.5   61.1   —
s07_priorita                   9    74     44   12.5      —     13   65.3   —
s08_ampiezza                   7    82     44   12.5      —   12.5   62.8   —
s09_offerta                   15    78     18   12.5      —     13   62.8   —
s10_livelli                    8    91     44   12.5      —     13   66.4   —
s11_servizi                    9    58     44   12.5      —   12.5   59.7   —
s12_perche                     5   100     44   12.5      —   12.5   61.1   —
s13_valore                     9    45     44   12.5      —     13   61.1   —
s14_struttura                 15    65     44   12.5      —     13   56.1   —
s15_pilot                      8    95     44   12.5      —     13   61.1   —
s16_cta                       21    48     19   12.5      —     12   55.6   —
a1_matrice                     5    92     44   12.5      —     14   65.3   —
a2_servizi                     5    83     44   12.5      —     14   62.8   —
a3_pricing                    17    41     22   12.5      —     17   58.3   —
a4_faq                         6   122     44   12.5      —     16   61.1   —
a5_assunzioni                  5    92     44   12.5      —     14   61.1   —
media copy 12 · superficie visiva minima 55,6% · canvas con flag 0/21
```

## 2. Dossier · soglie `dossier`

Copy ≤ 140 parole · corpo minimo 14 px per la copy, 13 px nei diagrammi, 12 px
nelle viste, 12,4 px per il testo di servizio. Soglia visiva 0 per costruzione:
in un dossier la tabella **è** il contenuto.

```
id                          copy vista   cont   meta   diag  vista   vis%  flag
p01_cover                     61     0     14     13      —      —      0   —
p02_overview                 115     0     14     13     13      —     34   —
p03_livelli                   87     0     14     13     13      —   33.3   —
p04_connect                   76    49     14     13      —   12.5   37.4   —
p05_insight                   53    47     14     13      —     13   32.5   —
p06_refyn                     79     0     14     13     14      —   31.3   —
p07_sorgenti                  74     0     14     13      —      —      0   —
p08_architettura             120     0     14     13     13      —   35.1   —
p09_contesto                  52    34     14     13      —   12.5   31.5   —
p10_oee                       95     0     14     13     13      —   26.6   —
p11_energia                  126     0     14     13     13      —   35.6   —
p12_output                    72     0     14     13      —      —      0   —
p13_pilot                     87     0     14     13     13      —     26   —
p14_servizi                  109     0     14     13      —      —      0   —
pa1_compatibilita            115     0     14     13      —      —      0   —
pa2_sizing                    80     0     14     13     13      —     33   —
pa3_governo                  117     0     14     13      —      —      0   —
pa4_kpi                       78     0     14     13      —      —      0   —
media copy 89 · copy massima 126 su 140 · canvas con flag 0/18
```

---

## 3. Controlli passati da tutti e 39 i canvas

| controllo | esito |
|---|---|
| elementi fuori dal canvas 1280×720 | nessuno |
| collisioni fra blocchi di primo livello — piede incluso | nessuna |
| corpo del testo sotto soglia | nessuno |
| richieste di rete | **zero** — i due HTML sono autonomi, font incorporati in base64 |
| errori di console | nessuno |
| id duplicati | nessuno |
| ancore rotte | nessuna |
| apostrofi diritti e accenti scritti con apostrofo | nessuno, anche nei testi accessibili `<title>` e `<desc>` |
| lista semantica §15.3 · 23 termini vietati | **nessuno**, né nel testo visibile né in quello accessibile |

Ogni vista di prodotto ha `role="img"` con `<title>` e `<desc>`: chi legge con uno
screen reader riceve la stessa informazione di chi guarda il grafico, inclusa la
dichiarazione che si tratta di una ricostruzione.

---

## 4. Verifica delle correzioni chieste

Ricerca testuale su entrambi i documenti completi:

```
"da approvare"                   deck 0 · dossier 0
"C1–C4"                          deck 0 · dossier 0
"canone superiore"               deck 0 · dossier 0
"modello economico da approvare" deck 0 · dossier 0
"costo del pezzo"                deck 0 · dossier 0
"in corso di approvazione"       deck 0 · dossier 0
"in approvazione"                deck 0 · dossier 0
```

`h1` nel deck: **uno solo**, la cover. La ex-cover V7 riusata come slide 04 e la
call to action sono state portate a `h2`.

---

## 5. Le regole di ritmo, verificate a mano sul contact sheet

**Deck · alternanza cromatica**
`D D L D L D L D L L D D D L L D` + appendici chiare. Le tre coppie adiacenti sono
quelle previste dallo storyboard: 01–02 aprono con la tensione, 11–12–13 sono il
blocco «che cosa compri e quanto vale», 14–15 il blocco commerciale.

**Deck · mai più di due canvas consecutivi costruiti su tabelle, schemi o testo.**
Le sequenze più a rischio sono 10–11 (scelta + servizi) e 14–15 (struttura +
pilot); in entrambi i casi la terza slide è una vista con un dato: la 12 porta il
grafico produzione–energia, la 16 la timeline di turno con il potenziale.

**Dossier · alternanza dei template**
`A B C B B C D C B C C D C D` · annessi `D C D D`. Mai tre pagine di seguito con
lo stesso template.

**Dossier · una sola domanda per pagina.** Le due pagine che unificavano contenuti
V7 sono state controllate una per una: la 07 risponde «da dove leggiamo», la 10
«come si calcola l’OEE e dove si perde». Nessuna pagina porta due domande.

---

## 6. Che cosa il QA non misura

Il QA misura la forma. Restano vere, e non si risolvono con il design:

1. **Non esistono screenshot reali di prodotto.** Le viste sono ricostruzioni
   grafiche, dichiarate in piede su ogni canvas che ne contiene una. Sostituirle con
   schermate vere cambia la credibilità dei due documenti più di qualunque altra
   correzione possibile.
2. **Il dataset è illustrativo e non validato.** Turno, settimana, potenze, prezzo
   dell’energia e fattore di emissione sono coerenti fra loro e ricostruibili a mano
   — l’appendice A5 li elenca tutti — ma nessuno li ha confermati plausibili per un
   impianto reale.
3. **Senza prezzi il deck non è un sales deck finale.** La 10, la 14 e l’appendice A3
   mostrano la struttura commerciale; gli importi arrivano con la proposta economica.
4. **Il dossier non è ancora IT-ready.** Gli annessi A1, A2 e A3 dicono che cosa si
   verifica e chi decide: è contenuto vero e utile, ma non sostituisce le risposte.
5. **Nessuna prova aziendale.** Anno, sede, gruppo, base installata e referenze non
   compaiono, perché non sono validati. La slide 12 prova con il prodotto.

Tutte e cinque sono censite in `DFactory_OpenInputs_v8.md` con l’effetto puntuale
di ogni mancanza.
