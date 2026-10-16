---
id: CRIM-008
titre: "Structurer le récit d'un contrôle ou d'une fouille déjà subis"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-008 — Structurer le récit d'un contrôle ou d'une fouille déjà subis

## Objectif et résultat attendu

Une personne qui a subi un contrôle d'identité, une palpation ou une fouille
et le conteste structure son récit, ses preuves et les canaux de signalement
à vérifier. Le skill n'intervient pas pendant un contrôle en cours.

## Périmètre et fichiers

- `criminal-legal/skills/stop-account/SKILL.md` — le skill (à créer)
- `criminal-legal/references/controles.md` — types de contrôle, canaux, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Date, heure, lieu ; service ; ce qui a été demandé et fait ; durée déclarée ;
témoins ; documents remis ; préjudice déclaré.

## Sortie attendue

Récit chronologique ; distinction des mesures possibles ; canaux à vérifier
(inspection, Défenseur des droits, plainte) ; limites.

## Travail attendu

Ne pas qualifier le contrôle d'illégal. Discrimination alléguée : question
distincte à DOM-029. Pendant un contrôle en cours, rappeler seulement de
garder son calme et de noter les faits, sans consigne d'opposition.

## Références métier et sources à rechercher

Code de procédure pénale, contrôles et vérifications d'identité (pistes 78-2,
78-3) ; Code de la sécurité intérieure, déontologie ; compétences du
Défenseur des droits.

## Critères d'acceptation

- [ ] B01 produit récit et canaux à vérifier sans qualification.
- [ ] B02 isole la question de discrimination.

## Vérification

- Cas normal : B01 — Contrôle avec palpation à la sortie d'une gare.
- Cas limite : B02 — Contrôles répétés que la personne attribue à son origine.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Assistance pendant un contrôle, plainte rédigée, publication de vidéos.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 13–28, 49–54, 76–78 et 81 de la [matrice](../dom-002-frictions-utilisateurs.md). Ajouter motif et cadre annoncés, territoire, corps et qualité, heures de début du contrôle et d'une vérification, consentement demandé ou non, mesure imposée, empreintes ou photographies prises, paroles rapportées et identifiants visibles.

- [ ] B03 — Séparer contrôle/relevé/vérification d'identité, palpation/fouille corporelle/sac/véhicule, agents municipaux/nationaux/privés ; absence d'explication, absence de carte ou refus de nom civil ne suffisent pas à conclure à une illégalité.
- [ ] B04 — Contrôles répétés allégués discriminatoires : tableau date, lieu, motif, termes exacts, comparaisons observées et témoins ; conserver le récit ici et la question de discrimination à DOM-029, sans causalité présumée.
- [ ] B05 — Preuves à risque → CRIM-020 ; signalement à préparer → CRIM-021 ; plainte → CRIM-004 ; domicile → CRIM-019.

Scénarios **attendus, non exécutés** : contrôle municipal suivi de photographies ; refus d'accès après refus de fouille ; contrôles répétés ; numéro visible mais nom refusé. Sources à rechercher : fondements des fouilles, relevé municipal, empreintes et photographie, identification et exceptions. Pour le contrôle en cours, l'orientation détaillée appartient à CRIM-018 ; CRIM-008 garde son périmètre après les faits.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
