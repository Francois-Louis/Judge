---
id: ENF-002
titre: "Répondre à une relance de recouvrement amiable"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-002 — Répondre à une relance de recouvrement amiable

## Objectif et résultat attendu

Une personne relancée par une société de recouvrement, ou par un commissaire
de justice en phase amiable, comprend ce que la lettre peut et ne peut pas
produire, et obtient un brouillon de demande de justificatifs.

## Périmètre et fichiers

- `enforcement-legal/skills/collection-letter-response/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/recouvrement-amiable.md` — mentions, frais, justificatifs, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

`recouvrement-amiable.md` est relu par ENF-008, qui ne le réécrit pas.

## Pièces et informations nécessaires

Lettre complète ; créancier d'origine et éventuel cessionnaire ; contrat,
factures, date de la dette ; frais réclamés ; paiements faits ; échanges.

## Sortie attendue

Nature de la lettre ; ce qui manque pour établir la dette ; frais réclamés et
question de leur charge, selon la source lue ; questions de prescription à
vérifier, sans calcul ; brouillon de demande de justificatifs ou de
contestation motivée par les pièces ; limites.

## Travail attendu

Ne pas trancher l'existence de la dette : le domaine du fond l'examine
(télécoms, énergie, consommation, logement, banque). Une menace de saisie sans
titre mentionné est notée comme affirmation à vérifier. Pressions ou menaces
alléguées : récit factuel et question à DOM-002.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, frais de recouvrement (piste L111-8)
et recouvrement amiable pour autrui (pistes R124-1 et suivants) ; règles de
prescription selon la nature de la créance.

## Critères d'acceptation

- [ ] R01 qualifie la lettre d'amiable et prépare la demande de justificatifs.
- [ ] R02 garde le même raisonnement quand l'auteur est un commissaire de justice.
- [ ] Aucun délai de prescription calculé sans source et date établie.

## Vérification

- Cas normal : R01 — Société de recouvrement pour un ancien abonnement télécom, frais de dossier ajoutés.
- Cas limite : R02 — Lettre « phase amiable » sur papier d'un commissaire de justice.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Examen de la dette au fond, plainte, envoi, paiement.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
