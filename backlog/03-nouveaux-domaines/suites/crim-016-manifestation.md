---
id: CRIM-016
titre: "Comprendre le cadre d'une manifestation et ses suites pour un participant"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-016 — Comprendre le cadre d'une manifestation et ses suites pour un participant

## Objectif et résultat attendu

Un participant à une manifestation comprend le cadre annoncé (déclaration,
interdiction, périmètre), et, après coup, ce que signifie une verbalisation
ou une convocation liée à sa participation. Ajout du 16 octobre 2026
([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `criminal-legal/skills/demonstration-guide/SKILL.md` — le skill (à créer)
- `criminal-legal/references/manifestations.md` — police administrative et pénale, sanctions possibles, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Arrêté ou annonce de la préfecture ; lieu, date ; avis de contravention ou
convocation reçus ; objets transportés ; faits déclarés.

## Sortie attendue

Distinction entre mesure administrative (déclaration, interdiction,
périmètre) et suite pénale (contravention, délit allégué) ; lecture de l'acte
reçu ; questions ; interlocuteurs ; limites. Aucune sanction affirmée sans
texte lu.

## Travail attendu

Contestation d'un arrêté d'interdiction ou démarches de l'organisateur →
DOM-010. Avis d'amende → CRIM-003 ; interpellation → CRIM-015 ou CRIM-002.
Ne donner aucun conseil pour contourner un dispositif de maintien de l'ordre
ou commettre une infraction.

## Références métier et sources à rechercher

Code de la sécurité intérieure, manifestations sur la voie publique (pistes
L211-1 et suivants) ; Code pénal, participation à une manifestation interdite
ou attroupement (pistes 431-3 et suivants, R644-4).

## Critères d'acceptation

- [ ] D01 distingue mesure administrative et suite pénale sans sanction non sourcée.
- [ ] D02 oriente la contestation d'un arrêté vers DOM-010.

## Vérification

- Cas normal : D01 — Contravention reçue pour participation à une manifestation interdite.
- Cas limite : D02 — Organisateur qui veut contester l'interdiction de sa manifestation.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Organisation d'une manifestation, recours administratif rédigé, défense au
fond, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-002-decoupage-penal.md).
