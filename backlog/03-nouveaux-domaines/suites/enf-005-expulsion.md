---
id: ENF-005
titre: "S'orienter face à une procédure d'expulsion"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-005 — S'orienter face à une procédure d'expulsion

## Objectif et résultat attendu

Un occupant qui reçoit un acte d'expulsion identifie l'étape de la
procédure, ce qui est urgent et les interlocuteurs à contacter, sans date
d'expulsion calculée ni promesse de maintien.

## Périmètre et fichiers

- `enforcement-legal/skills/eviction-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/expulsion.md` — étapes, dispositifs à identifier, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Décision ordonnant l'expulsion ; commandement de quitter les lieux ; autres
actes ; composition du foyer ; démarches de relogement et d'aide engagées.

## Sortie attendue

Étape identifiée ; bloc d'urgence ; interlocuteurs et dispositifs à vérifier ;
demandes possibles à vérifier (délais devant le juge) ; questions ; limites.

## Travail attendu

Dette locative et bail → DOM-006 ; concours de la force publique → DOM-010.
Ne pas annoncer de période protégée ni de délai sans texte lu et dates
établies. Ne jamais conseiller d'empêcher physiquement l'exécution.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, expulsion (pistes L411-1 et
suivants, L412-1 à L412-6) ; dispositifs départementaux de prévention à
identifier.

## Critères d'acceptation

- [ ] X01 identifie l'étape et les urgences sans date calculée.
- [ ] X02 sépare la dette locative (DOM-006) et l'acte d'expulsion.

## Vérification

- Cas normal : X01 — Commandement de quitter les lieux reçu après un jugement.
- Cas limite : X02 — Locataire qui veut contester le montant de l'arriéré.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisine du juge, demande de logement, contestation du bail, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
