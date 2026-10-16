---
id: CRIM-019
titre: "Comprendre une perquisition au domicile et les objets saisis"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-019 — Comprendre une perquisition au domicile et les objets saisis

## Objectif et résultat attendu

Une personne confrontée à une entrée au domicile ou une perquisition identifie le cadre annoncé, les pièces remises et les questions urgentes à poser à un avocat.

Besoin issu des points 29–31 de la [matrice des frictions](../dom-002-annexes/dom-002-frictions-utilisateurs.md). Proposition documentaire, sans implémentation ni sélection.

## Périmètre et fichiers

- `criminal-legal/skills/home-search-reading/SKILL.md` — le skill (à créer)
- `criminal-legal/references/perquisition-domicile.md` — repères, modèles et sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit. Un relais vers une autre story est une orientation ; aucun autre plugin installé n'est requis.

## Pièces et informations nécessaires

Mesure en cours ou achevée ; occupant et qualité ; service ; date et heures ; cadre annoncé (flagrance, enquête préliminaire, instruction ou autre) ; assentiment demandé et écrit éventuel ; décision judiciaire présentée ; PV, inventaire et scellés remis ; objets concernés. Documents limités aux passages utiles.

## Sortie attendue

Si en cours, bloc bref : sécurité, cadre annoncé, avocat et questions ; ensuite fiche des documents, consentement sollicité ou pouvoir imposé à vérifier, objets et références de scellés, pièces manquantes et demande de renseignements sur la restitution. Aucun accord conseillé par défaut ni nullité déduite du seul défaut de consentement.

## Travail attendu

Distinguer invitation à entrer, entrée consentie et perquisition contrainte ; ne pas généraliser les conditions d'une enquête préliminaire à la flagrance ou à une autorisation judiciaire. Vérifier horaires, présence, statut, assentiment, exceptions et inventaire selon la source lue. Ne pas entraver une mesure ni déplacer ou effacer des éléments. Restitution après interpellation → CRIM-015 ; recours et demande judiciaire de restitution → avocat ; visite administrative → DOM-010 ; visite douanière → DOM-009.

Charger la méthode locale BASE-005. Séparer document lu, fait déclaré, règle vérifiée et inconnue. Aucun droit, aucune durée, aucun délai ni montant établi depuis le seul texte des frictions ; sans source, fournir les questions et pièces utiles.

## Références métier et sources à rechercher

CPP, perquisitions, saisies, scellés et restitutions selon le cadre (pistes 56 et suivants, 76, 97, 41-4, 99) ; régimes spéciaux et locaux protégés. Aucun horaire ou pouvoir affirmé depuis le seul mot perquisition.

## Critères d'acceptation

- [ ] D01 distingue assentiment demandé et autorisation judiciaire sans conclure à une irrégularité.
- [ ] D02 relève les objets et documents manquants sans garantir la restitution.

## Vérification

- Cas normal : D01 — Enquête préliminaire : l'occupant n'a pas signé et un agent évoque une décision judiciaire.
- Cas limite : D02 — Ordinateur emporté, numéro de scellé inconnu et aucun inventaire disponible.
- Sans source lue : questions, pièces et limites ; aucune règle suppléée par le texte utilisateur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Opposition physique, tactiques de dissimulation, requête en nullité, défense au fond, restitution judiciaire rédigée, envoi.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur. Contrat commun : [découpage](../dom-002-annexes/dom-002-decoupage-penal.md). Aucun fichier de plugin créé par cette intégration.
