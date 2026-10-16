---
id: ENF-015
titre: "Préparer une réclamation contre un commissaire de justice"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-015 — Préparer une réclamation contre un commissaire de justice

## Objectif et résultat attendu

Une personne décrit un comportement contesté, rassemble les preuves et obtient un brouillon de réclamation adressé au destinataire professionnel à vérifier, en conservant séparément les recours urgents.

## Périmètre et fichiers

- `enforcement-legal/skills/professional-complaint-preparation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/reclamation-professionnelle.md` — qualification, pièces, modèle de sortie et sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

Le paquet et `qualification-acte.md` sont créés par ENF-001. Chaque référence consommée est embarquée dans le paquet ; aucun plugin voisin n'est requis. Appliquer le contrat commun du [découpage](../dom-003-decoupage-execution.md).

## Pièces et informations nécessaires

Identité et étude à vérifier par un canal officiel ; actes ; échanges, messages, relevé d'appels ou visites ; réclamations antérieures ; réponse ; mesure en cours et dommage déclaré.

## Sortie attendue

Chronologie datée et attribuée ; faits prouvés, déclarés et contestés ; pièces numérotées ; brouillon sobre ; destinataire et canal officiels à confirmer ; démarches distinctes pour saisie, frais, indemnisation ou faits potentiellement pénaux.

## Travail attendu

Vérifier la procédure professionnelle en vigueur, la qualité du professionnel et les possibilités de réclamation ou de conciliation. Distinguer ce circuit d'un signalement de recouvrement trompeur, de la voie pénale DOM-002 et d'un dommage civil DOM-035. Une société de recouvrement n'est pas un commissaire de justice. Ne pas présumer faute, sanction ni effet suspensif ; une négociation ou réclamation ne remplace pas le recours requis contre la mesure.

## Références métier et sources à rechercher

Statut et déontologie des commissaires de justice ; textes disciplinaires et procédure de réclamation ; informations officielles sur le litige avec le professionnel et canaux de signalement selon les faits. Vérifier les coordonnées du destinataire sans réutiliser un contact non authentifié.

## Critères d'acceptation

- [ ] Le cas normal produit la sortie utile avec chaque fait attribué à sa pièce ou marqué comme déclaré.
- [ ] Le cas limite explicite les manques et distingue les procédures sans promettre d'issue favorable.
- [ ] Aucune règle, somme, compétence ou échéance n'est affirmée sans source lue et faits nécessaires ; un point réservé garde une action utile.
- [ ] Le résultat est compréhensible sans formation juridique ; le paquet installé seul contient les références et la méthode BASE-005 nécessaires.

## Vérification

- Cas normal : R03 — Appels insistants attribués à une étude et échanges conservés : chronologie, formulation factuelle et brouillon professionnel sans qualification pénale automatique.
- Cas limite : R04 — Réclamation envoyée pendant une saisie bancaire : faire apparaître la voie judiciaire distincte ENF-019 et son urgence sans déduire de suspension.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Dépôt ou envoi, plainte pénale rédigée, action indemnitaire, contestation judiciaire de la mesure, sanction annoncée.

## État de la proposition — 16 octobre 2026

Issue des points 8 et 47 de la [matrice des frictions](../dom-003-frictions-utilisateurs.md). Exigence de backlog, sans sélection ni implémentation.
