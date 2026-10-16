---
id: LOG-007
titre: "Préparer le congé d'un locataire en location vide"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-007 — Préparer le congé d'un locataire en location vide

## Objectif et résultat attendu

Un locataire d'un logement privé vide, résidence principale en France
métropolitaine, prépare son départ et un brouillon de congé, avec les
conditions de préavis à vérifier pour sa situation.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/tenant-notice-preparation/SKILL.md` — tâche (à créer)
- `housing-legal/references/conge-locataire-vide.md` — notification, préavis et sources (à créer)
- `housing-legal/skills/tenant-notice-preparation/references/conge.md` — modèle (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale de LOG-001 ; aucun autre plugin requis.

## Pièces et informations nécessaires

Bail, commune, cotitulaires et qualité de l'auteur, départ souhaité,
notification déjà faite ou envisagée, motif d'une réduction invoquée et
justificatif strictement utile. Si fait de santé, ne pas demander un dossier
médical ; préciser seulement la pièce nécessaire après recherche.

## Sortie attendue

Conditions de notification et de préavis avec sources lues ou réserves ;
pièces manquantes ; brouillon avec champs non établis visibles ; départ
souhaité distinct de l'effet juridique ; préparation clés/état des lieux.

## Travail attendu

Vérifier territoire et motif avant une éventuelle réduction, puis réception
et cotitularité. Pas de date d'effet déterminée par le seul souhait de départ.
Dépôt après départ → LOG-001 ; congé reçu du bailleur meublé → LOG-006 ;
protection face aux violences → DOM-038 sur question et canal sûrs distincts.

## Références métier et sources à rechercher

Textes locatifs du régime vide, notification, préavis, motifs de réduction,
cotitularité ; textes territoriaux exacts si pertinents ; ANIL/ADIL. Vérifier
champ, versions, exceptions et transitions, sans tableau de durées de mémoire.

## Critères d'acceptation

- [ ] T01 sépare date souhaitée, notification et effet à vérifier.
- [ ] T02 ne présume pas une réduction depuis le seul nom de la commune.
- [ ] Sans source, brouillon factuel avec champs réservés ; paquet seul et références locales vérifiés selon BASE-006.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si délai, acte ou enjeu irréversible (BASE-013).

## Vérification

- Cas normal : T01 — Projet de départ, bail complet, aucune notification ; brouillon et liste des vérifications, aucune réception inventée.
- Cas limite : T02 — Préavis réduit allégué pour un territoire non confirmé ; demander commune et source exacte.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Autres régimes locatifs, désolidarisation ou départ d'un seul cotitulaire au
fond, transmission du congé, signature et envoi.

## Complément des frictions logement — 16 octobre 2026

Points 28–31 ; section 8 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

Distinguer courriel, accord informel, dépôt postal, présentation et réception prouvée. Un recommandé non retiré ne reçoit pas une date de réception inventée ; vérifier autre voie de notification. Réduction alléguée : motif, territoire et pièce utile, sans dossier de santé. Relocation anticipée : demander date d'occupation et accord du bailleur avant d'expliquer les sommes ; aucun effet déduit de la seule remise des clés. LOG-020 garde le meublé et LOG-018 la solidarité du sortant.

- [ ] Le scénario complémentaire produit les distinctions, pièces et réserves ci-dessous, dans la borne de la story.

Scénario **attendu, non exécuté** : Congé par courriel puis recommandé non retiré, nouveau locataire annoncé : frise des faits et preuves à demander, sans fixer fin de préavis depuis l'envoi.
Les montants et délais du texte utilisateur ne sont pas validés ; appliquer
les sources locales et la recette de la story avant toute livraison.
