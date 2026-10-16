---
id: ENF-007
titre: "S'orienter face à une saisie sur salaire"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-007 — S'orienter face à une saisie sur salaire

## Objectif et résultat attendu

Un salarié dont la rémunération est saisie comprend la procédure, ce qu'il
peut vérifier sur son bulletin et les interlocuteurs ; un employeur tiers
saisi comprend ce qui lui est demandé.

## Périmètre et fichiers

- `enforcement-legal/skills/wage-seizure-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/saisie-remunerations.md` — procédure en vigueur, rôles, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Acte de saisie ou notification ; bulletins de salaire ; titre visé ;
composition du foyer si elle est demandée ; autres saisies.

## Sortie attendue

Procédure et acteurs ; lignes du bulletin à vérifier ; questions ;
interlocuteurs ; limites. Aucune fraction saisissable calculée sans barème
lu à la date.

## Travail attendu

Vérifier d'abord la procédure en vigueur à la date de l'acte : la saisie des
rémunérations a été réformée récemment, le cadrage n'en fixe pas le contenu.
Relation de travail → employment.

## Références métier et sources à rechercher

Code du travail et Code des procédures civiles d'exécution, saisie des
rémunérations, version à la date de l'acte ; barème en vigueur.

## Critères d'acceptation

- [ ] W01 explique la procédure en vigueur sans calcul non sourcé.
- [ ] W02 traite la question de l'employeur tiers saisi sans conseil de gestion de paie.

## Vérification

- Cas normal : W01 — Retenue apparue sur le bulletin, acte reçu un mois plus tôt.
- Cas limite : W02 — Petite entreprise recevant l'acte pour un salarié.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Calcul de paie, contestation rédigée, envoi.

## Complément issu des frictions des commissaires de justice

Points 26–28 de la [matrice utilisateur](../dom-003-annexes/dom-003-frictions-utilisateurs.md).

- [ ] W03 — Commandement récent ou dossier antérieur à la réforme annoncée : qualifier date, titre, état de la procédure et transition ; identifier rôles du commissaire, répartiteur, employeur et JEX selon les sources lues, sans exiger par principe une nouvelle autorisation du juge.
- [ ] W04 — Contestation envisagée : relever date et mode de signification du commandement ; faire vérifier forme, destinataire, représentation et effet selon le moment du recours. Ni simple lettre au cabinet ni négociation ne sont assimilées à l'assignation requise ; celle-ci n'est pas rédigée dans cette story.
- [ ] W05 — Retenue contestée : recueillir assiette, période, bulletins, personnes à charge justifiées, autres retenues et minimum protégé ; identifier barème daté et exceptions pertinentes sans calcul de paie.

Scénarios W03–W05 **attendus, non exécutés** : ancien dossier transféré ; commandement reçu et contestation informelle seule ; retenue sans prise en compte déclarée d'une charge de famille. Vérifier les textes de réforme et leur transition, le premier délai de contestation et ses effets, et le barème à la date pertinente ; les repères du document utilisateur restent à confirmer.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-annexes/dom-003-decoupage-execution.md).
