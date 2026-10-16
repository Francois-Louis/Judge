---
id: CRIM-022
titre: "Préparer une demande relative au fichier TAJ"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-022 — Préparer une demande relative au fichier TAJ

## Objectif et résultat attendu

Une personne distingue TAJ et casier judiciaire, identifie sa demande d'accès, de rectification ou d'effacement, et prépare un dossier adapté sans promesse de suppression.

Besoin issu des points 91–93 de la [matrice des frictions](../dom-002-annexes/dom-002-frictions-utilisateurs.md). Proposition documentaire, sans implémentation ni sélection.

## Périmètre et fichiers

- `criminal-legal/skills/taj-request/SKILL.md` — le skill (à créer)
- `criminal-legal/references/fichier-taj.md` — repères, modèles et sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`qualification-penale.md` (CRIM-001) est relu, pas réécrit. Un relais vers une autre story est une orientation ; aucun autre plugin installé n'est requis.

## Pièces et informations nécessaires

Rôle dans la procédure ; référence des faits ; décision de classement, non-lieu, relaxe ou autre si disponible ; notification et preuve de réception ; demande précédente, destinataire, date et réponse ; objectif (accès, erreur, effacement) ; éventuel contexte d'enquête administrative. Identifiants réduits au nécessaire dans les brouillons.

## Sortie attendue

Fiche distinguant faits de procédure et données supposées du TAJ ; interlocuteur et voie à vérifier ; liste des pièces ; brouillon de demande ; lecture d'un refus ou du silence et questions pour un recours à vérifier avec avocat. Tableau des dates prouvées, déclarées et inconnues ; aucun calcul de délai ni effacement automatique déduit d'un classement.

## Travail attendu

Séparer demande d'accès, rectification, effacement, restrictions et recours ; vérifier destinataire, qualité du demandeur, décision pénale, modalités de saisine et preuve de réception. Un TAJ supposé vide ne se déduit pas d'un bulletin de casier vierge. CRIM-012 reste propriétaire du casier ; CRIM-007 de la suite d'une plainte ; décision défavorable d'emploi public → DOM-037, autre décision administrative → DOM-010. Aucun accès au fichier ni stockage des faits pénaux.

Charger la méthode locale BASE-005. Séparer document lu, fait déclaré, règle vérifiée et inconnue. Aucun droit, aucune durée, aucun délai ni montant établi depuis le seul texte des frictions ; sans source, fournir les questions et pièces utiles.

## Références métier et sources à rechercher

CPP et textes réglementaires du TAJ (pistes 230-6 et suivants, R40-23 et suivants) ; sources officielles du ministère et de la CNIL ; compétence et délais du magistrat ou de la juridiction selon demande et notification. Texte utilisateur seulement comme besoin.

## Critères d'acceptation

- [ ] T01 ne déduit pas l'effacement du classement et prépare la demande adaptée.
- [ ] T02 sépare accès et effacement et relève l'incertitude sur la réception.
- [ ] T03 traite le silence selon la demande et les preuves, sans délai inventé.

## Vérification

- Cas normal : T01 — Classement sans suite, casier vierge et mention TAJ alléguée lors d'une enquête administrative.
- Cas limite : T02 — Refus d'effacement reçu sans enveloppe, demande initiale et date de réception introuvables.
- Cas limite : T03 — Demande d'accès restée sans réponse, preuve d'envoi conservée.
- Sans source lue : questions, pièces et limites ; aucune règle suppléée par le texte utilisateur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Requête contentieuse rédigée, garantie d'effacement ou de recrutement, autres fichiers traités au fond, accès technique au TAJ, envoi.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur. Contrat commun : [découpage](../dom-002-annexes/dom-002-decoupage-penal.md). Aucun fichier de plugin créé par cette intégration.
