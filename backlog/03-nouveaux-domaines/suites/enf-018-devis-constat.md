---
id: ENF-018
titre: "Préparer une demande de devis pour un constat"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-018 — Préparer une demande de devis pour un constat

## Objectif et résultat attendu

Une personne qui envisage de commander un constat prépare une demande de devis et sait quelles composantes du prix et de la mission faire préciser.

## Périmètre et fichiers

- `enforcement-legal/skills/bailiff-report-quote-request/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/devis-constat.md` — qualification, pièces, modèle de sortie et sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

Le paquet et `qualification-acte.md` sont créés par ENF-001. Chaque référence consommée est embarquée dans le paquet ; aucun plugin voisin n'est requis. Appliquer le contrat commun du [découpage](../dom-003-decoupage-execution.md).

## Pièces et informations nécessaires

Faits à constater, objectif, lieu, urgence, accès et personnes concernées ; devis ou échanges existants ; annexes et livrables souhaités ; identité du demandeur ; éventuel litige en cours.

## Sortie attendue

Mission factuelle proposée et limites ; brouillon de demande de devis ; tableau prix ou calcul, déplacement, durée, majorations, taxes, annexes et remise des documents, annulation éventuelle ; questions sur les conditions d'accès et l'utilité de la preuve.

## Travail attendu

Distinguer commande d'un constat, signification d'un acte et acte d'exécution. Vérifier si la prestation et ses composantes relèvent d'un tarif réglementé ou d'honoraires libres selon la situation, sans supposer que tout constat est libre. Ne pas promettre que le constat prouvera la responsabilité ni autoriser un accès aux lieux d'autrui. Facture déjà contestée : ENF-014 ; constat reçu : ENF-016.

## Références métier et sources à rechercher

Code de commerce, tarifs et prestations concernées ; obligations d'information sur le prix et modalités de calcul selon la qualité du client ; textes encadrant mission et accès du commissaire de justice. Vérifier le régime du constat demandé.

## Critères d'acceptation

- [ ] Le cas normal produit la sortie utile avec chaque fait attribué à sa pièce ou marqué comme déclaré.
- [ ] Le cas limite explicite les manques et distingue les procédures sans promettre d'issue favorable.
- [ ] Aucune règle, somme, compétence ou échéance n'est affirmée sans source lue et faits nécessaires ; un point réservé garde une action utile.
- [ ] Le résultat est compréhensible sans formation juridique ; le paquet installé seul contient les références et la méthode BASE-005 nécessaires.

## Vérification

- Cas normal : V01 — Constat d'une dégradation avant travaux : demande de devis avec déplacement, temps, annexes et délai de remise.
- Cas limite : V02 — Forfait attractif sans majoration d'urgence indiquée et accès chez un tiers envisagé : faire préciser prix et autorisation nécessaire avant commande.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Commande, prise de rendez-vous, conseil d'intrusion, négociation ou comparaison commerciale de professionnels, envoi.

## État de la proposition — 16 octobre 2026

Issue des points 43 de la [matrice des frictions](../dom-003-frictions-utilisateurs.md). Exigence de backlog, sans sélection ni implémentation.
