# D.Factory · Baseline IT/OT V9.1

**Scheda del workshop G4.** Diciotto campi. Finché non sono compilati il dossier
si chiama *preliminare* e i tre annessi tecnici descrivono il metodo, non l'esito.

Non ci sono valori proposti in questa scheda. Sarebbero specifiche di prodotto
inventate, e il §2.2 le vieta.

---

## 1. I diciotto campi di G4

### Deployment e infrastruttura

| Campo | Valore | Fonte | Approvato da |
|---|---|---|---|
| `PH_DEPLOYMENT_MODEL` on-premise, VM, altro | | scheda tecnica | |
| `PH_SUPPORTED_OS` sistemi operativi | | scheda tecnica | |
| `PH_MIN_CPU` | | scheda tecnica | |
| `PH_MIN_RAM` | | scheda tecnica | |
| `PH_MIN_STORAGE` | | scheda tecnica | |
| `PH_RETENTION_DEFAULT` | | scheda tecnica | |

### Rete e protocolli

| Campo | Valore | Fonte | Approvato da |
|---|---|---|---|
| `PH_SUPPORTED_PROTOCOLS` | | catalogo verificato in campo | |
| `PH_REQUIRED_PORTS` | | scheda tecnica | |
| `PH_FLOW_DIRECTIONS` | | scheda tecnica | |
| `PH_READ_ONLY_POLICY` | **B, §6.1** | piano V9.1 | |

### Sicurezza e dati

| Campo | Valore | Fonte | Approvato da |
|---|---|---|---|
| `PH_AUTHENTICATION_MODEL` | | scheda tecnica | |
| `PH_ROLE_MODEL` | | scheda tecnica | |
| `PH_BACKUP_POLICY` | | scheda tecnica | |
| `PH_AUDIT_LOGGING` | | scheda tecnica | |
| `PH_REMOTE_SUPPORT_POLICY` | | contratto tipo | |
| `PH_DATA_OWNERSHIP` | | contratto tipo | |
| `PH_LICENSE_RIGHTS` | | contratto tipo | |
| `PH_END_OF_CONTRACT_DATA` | | contratto tipo | |

## 2. Sizing · §10.16 · tre fasce

Il piano chiede tre fasce con le grandezze che le determinano. L'annesso A2 già
mostra le cinque grandezze; qui vanno i numeri.

| Grandezza | Small | Medium | Large |
|---|---|---|---|
| numero di tag | | | |
| frequenza di campionamento | | | |
| retention | | | |
| numero di linee | | | |
| CPU | | | |
| RAM | | | |
| storage | | | |

## 3. Compatibilità · §10.15

L'annesso A1 elenca **che cosa si verifica, come e quando**. Qui va l'esito.

| Costruttore | Famiglia PLC | Protocollo | Versione testata | Direzione | Frequenza | Esito | Note |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Il piano al §2.2 vieta di scrivere «qualsiasi protocollo». Finché questa tabella
è vuota, l'annesso A1 resta il metodo di verifica — che è già un contenuto utile
per l'IT del cliente, perché dice esattamente che cosa gli verrà chiesto.

## 4. Che cosa cambia quando G4 si chiude

| dove | oggi | dopo G4 |
|---|---|---|
| titolo del dossier | «Dossier tecnico preliminare per assessment e solution design» | «Dossier tecnico» |
| annesso A1 | metodo di verifica | matrice compilata |
| annesso A2 | cinque grandezze e il metodo | tre fasce con CPU, RAM, storage |
| annesso A3 | ambiti e responsabili | valori |
| pagina 08 | pannello «da chiudere nel solution design» | specifiche |
| criteri §13 | 0 su 10 | 10 su 10 |

La riga del titolo non è cosmetica: **`work_v91/accept.py` fa fallire il build**
se il dossier si chiama «Dossier tecnico» con G4 aperto.
