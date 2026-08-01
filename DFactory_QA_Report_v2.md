# QA · DFactory Sales Deck v2 e Dossier Tecnico v2

Esito di `python3 quadro/qa_v2.py`. Ogni riga è una verifica eseguita sul
documento compilato, aperto in Chromium a 1280×720 con i font caricati.


## STRUTTURA

- [x] il sales deck ha 12 slide · (12)
- [x] il dossier tecnico ha 18 pagine · (18)
- [x] gli id del sales deck sono quelli previsti
- [x] gli id del dossier sono quelli previsti
- [x] nessun id duplicato
- [x] la numerazione nel rail segue la posizione
- [x] ogni pagina ha un titolo
- [x] gli originali v1 non sono stati sovrascritti

## GEOMETRIA

- [x] sales: ogni pagina è 1280×720 · ({(1280, 720)})
- [x] sales: nessun elemento oltre i bordi · (0)
- [x] sales: nessun contenuto sopra il rail inferiore · (0)
- [x] sales: nessun contenuto fuori da pannelli e zone · (0)
- [x] sales: rail su ogni pagina
- [x] dossier: ogni pagina è 1280×720 · ({(1280, 720)})
- [x] dossier: nessun elemento oltre i bordi · (0)
- [x] dossier: nessun contenuto sopra il rail inferiore · (0)
- [x] dossier: nessun contenuto fuori da pannelli e zone · (0)
- [x] dossier: rail su ogni pagina

## DESIGN SYSTEM

- [x] sales: nessun testo sotto 9,5 px
- [x] sales: nessun peso 800 o 900
- [x] sales: nessun border-radius fuori dal led
- [x] sales: nessuna ombra fuori dal led
- [x] sales: al massimo 2 statement serif · (0)
- [x] sales: nessun colore fuori palette
- [x] dossier: nessun testo sotto 9,5 px
- [x] dossier: nessun peso 800 o 900
- [x] dossier: nessun border-radius fuori dal led
- [x] dossier: nessuna ombra fuori dal led
- [x] dossier: al massimo 2 statement serif · (0)
- [x] dossier: nessun colore fuori palette
- [x] sales: massimo 3 ruoli gialli per slide
- [x] dossier: massimo 2 ruoli gialli per pagina

## DENSITA'

- [x] sales: media sotto le 100 parole · (74)
- [x] sales: nessuna pagina oltre 130 parole · (0)
- [x] dossier: media sotto le 190 parole · (97)
- [x] dossier: nessuna pagina oltre 220 parole · (0)

## PLACEHOLDER

- [x] nessuno dei 17 token storici è andato perso
- [x] nessun placeholder usato come URL
- [x] nessun [confermare] residuo
- [x] token condivisi fra i due documenti · (PH_07_ORE_CLIENTE, PH_17_DOMINIO, PH_18_BOOKING)

## COERENZA INCROCIATA

- [x] nomi dei livelli
- [x] Refyn con lo stesso stato
- [x] PackML a 17 stati
- [x] modello ridotto a 2 stati
- [x] on-premise in entrambi
- [x] dato sul server del cliente
- [x] sensoristica a carico del cliente
- [x] stesso referente
- [x] stesso indirizzo
- [x] stesso caso cliente, in due letture
- [x] cinque vettori in entrambi
- [x] milestone distinte nel dossier
- [x] i link reciproci puntano a pagine esistenti
- [x] entrambi i documenti linkano l'altro · (3 + 4)

## CLAIM E COPYWRITING

- [x] nessun claim di compatibilità universale
- [x] nessun payback numerico senza input validati
- [x] il primo dato non è confuso con il go-live
- [x] nessuna certificazione ISO 50001 attribuita al software
- [x] MID e ISO 50001 non sono presentati come un'unica categoria
- [x] nessuna occorrenza di MES/MOM
- [x] nessuna capacità di roadmap nel sales deck
- [x] il dossier dichiara l'assenza di intelligenza artificiale
- [x] nessun termine vietato
- [x] nessun trattino lungo nella prosa · (0)
- [x] al massimo una costruzione 'Non X. Y.' · (1)
- [x] le schermate dimostrative sono etichettate

## RETE E CONSOLE

- [x] sales: nessun errore in console
- [x] sales: nessuna richiesta di rete non locale
- [x] sales: nessun riferimento esterno nel sorgente · (0)
- [x] sales: il blocco di stampa è presente
- [x] sales: lingua dichiarata
- [x] dossier: nessun errore in console
- [x] dossier: nessuna richiesta di rete non locale
- [x] dossier: nessun riferimento esterno nel sorgente · (0)
- [x] dossier: il blocco di stampa è presente
- [x] dossier: lingua dichiarata

## Densità per pagina

| Documento | Pagina | Parole visibili | Ruoli gialli |
|---|---|---|---|
| Sales deck | `s01_cover` | 15 | 3 |
| Sales deck | `s02_perche_adesso` | 101 | 1 |
| Sales deck | `s03_come_funziona` | 66 | 1 |
| Sales deck | `s04_tre_decisioni` | 73 | 0 |
| Sales deck | `s05_prodotto_in_azione` | 34 | 3 |
| Sales deck | `s06_prova` | 74 | 0 |
| Sales deck | `s07_perche_dfactory` | 75 | 2 |
| Sales deck | `s08_business_case` | 109 | 1 |
| Sales deck | `s09_offerta` | 66 | 0 |
| Sales deck | `s10_audit_scala` | 104 | 1 |
| Sales deck | `s11_faq` | 108 | 0 |
| Sales deck | `s12_cta` | 57 | 2 |
| Dossier | `d01_cover` | 88 | 1 |
| Dossier | `d02_architettura_prodotto` | 160 | 1 |
| Dossier | `d03_architettura_tecnica` | 58 | 1 |
| Dossier | `d04_capability` | 137 | 0 |
| Dossier | `d05_supervisione` | 33 | 2 |
| Dossier | `d06_oee_fermi` | 33 | 2 |
| Dossier | `d07_velocita_qualita` | 41 | 2 |
| Dossier | `d08_multi_impianto` | 20 | 2 |
| Dossier | `d09_distribuzione_energia` | 32 | 1 |
| Dossier | `d10_costo_co2_stato` | 8 | 2 |
| Dossier | `d11_metodo_misura` | 173 | 1 |
| Dossier | `d12_brownfield` | 143 | 1 |
| Dossier | `d13_deployment_security` | 88 | 2 |
| Dossier | `d14_sensori` | 162 | 1 |
| Dossier | `d15_output_integrazioni` | 118 | 0 |
| Dossier | `d16_delivery_raci` | 136 | 2 |
| Dossier | `d17_caso_tecnico` | 178 | 0 |
| Dossier | `d18_supporto_audit` | 141 | 1 |

Le micro-etichette, i valori numerici e il testo dentro gli SVG non entrano nel
conteggio: misurano la densità di lettura, non la quantità di caratteri.
