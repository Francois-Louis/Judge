---
id: BNK-008
titre: "Réagir à une clôture ou à un refus d'ouverture de compte"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-008 — Réagir à une clôture ou à un refus d'ouverture de compte

## Objectif et résultat attendu

Une personne dont le compte est clôturé, ou qui ne parvient pas à ouvrir de
compte, comprend la décision, les démarches possibles et le dispositif de
droit au compte à vérifier.

## Périmètre et fichiers

- `banking-legal/skills/account-closure-access/SKILL.md` — le skill (à créer)
- `banking-legal/references/compte.md` — clôture, droit au compte, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Lettre de clôture ou de refus ; convention ; date ; statut (particulier,
professionnel) ; autres comptes détenus.

## Sortie attendue

Décision lue ; démarches à vérifier (droit au compte, nouvelle banque) ;
brouillon de demande d'explication ; limites.

## Travail attendu

Refus allégué discriminatoire → question à DOM-029. Compte professionnel :
dispositif à vérifier pour ce statut.

## Références métier et sources à rechercher

Code monétaire et financier, droit au compte et clôture (piste L312-1) ;
procédure de la Banque de France.

## Critères d'acceptation

- [ ] A01 explique la décision et la démarche à vérifier.
- [ ] A02 isole la question de discrimination.

## Vérification

- Cas normal : A01 — Lettre de clôture sans motif, préavis indiqué.
- Cas limite : A02 — Trois refus d'ouverture que la personne relie à sa nationalité.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisine de la Banque de France faite à la place de la personne, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
