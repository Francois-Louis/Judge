---
id: INS-009
titre: "Contester un refus de complémentaire santé ou de prévoyance"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-009 — Contester un refus de complémentaire santé ou de prévoyance

## Objectif et résultat attendu

Un adhérent dont la complémentaire santé ou la prévoyance refuse un
remboursement ou une prestation comprend le motif selon le régime de
l'organisme et prépare une demande.

## Périmètre et fichiers

- `insurance-legal/skills/health-cover-claim/SKILL.md` — le skill (à créer)
- `insurance-legal/references/sante-prevoyance.md` — régimes, garanties, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

`motifs-refus.md` (INS-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Tableau des garanties ; notice ; organisme (mutuelle, institution de
prévoyance, assureur) ; contrat individuel ou collectif ; décompte de
remboursement ; refus.

## Sortie attendue

Régime identifié ; garantie lue ; motif ; brouillon ; limites. Aucun
remboursement recalculé.

## Travail attendu

Part de l'assurance maladie → DOM-012. Obligations de l'employeur sur un
contrat collectif → employment. Soins → DOM-007.

## Références métier et sources à rechercher

Code de la mutualité ; Code de la sécurité sociale pour les institutions de
prévoyance ; règles des contrats responsables.

## Critères d'acceptation

- [ ] S01 identifie le régime de l'organisme avant de lire le refus.
- [ ] S02 sépare la part de l'assurance maladie.

## Vérification

- Cas normal : S01 — Mutuelle refusant des lunettes « hors période de renouvellement ».
- Cas limite : S02 — Décompte où la part de l'assurance maladie semble erronée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Prestations de sécurité sociale, envoi.

## Complément issu des frictions assurance

Points 12–13 et 53–57 de la [matrice](../dom-005-annexes/dom-005-frictions-utilisateurs.md).

- [ ] S03 — Décompte : séparer facture, base de remboursement, part obligatoire, complément, forfait, plafond et période ; un pourcentage de base n'est pas un pourcentage de facture.
- [ ] S04 — Prévoyance : distinguer effet, carence, franchise temporelle, définition d'incapacité et invalidité contractuelle ; la décision de caisse ne suffit pas à établir la garantie privée.
- [ ] S05 — Prestations arrêtées : demander clause, critère médical et rapport utile ; contre-avis médical à vérifier, sans diagnostic ni taux de séquelles établi par l'outil.

Scénarios S03–S05 **attendus, non exécutés** : reste à charge malgré un pourcentage annoncé, plafond annuel optique, invalidité sociale mais garantie refusée, arrêt des versements avant reprise professionnelle. Définir l'organisme et son code ; recueillir les seules données de santé nécessaires, sans stockage. Aucun remboursement recalculé. GAV relève de la lecture du contrat INS-004 ; préjudice corporel → DOM-035.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-annexes/dom-005-decoupage-assurance.md).

## Complément des frictions santé — 16 octobre 2026

Points 45, 123–134 de la [matrice santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md).

- [ ] FS01 — Rapprocher simulation/accord, facture/code et remboursement final, dates de soins, prise d'effet, carence, résiliation et avenants. Relever clause invoquée et justificatifs manquants sans retenir automatiquement la date de facture ni recodifier pour obtenir la garantie.
- [ ] FS02 — NOEMIE inactive ou organismes successifs : périodes d'affiliation et décomptes, demande écrite de régularisation ; aucune connexion au compte ni couverture déduite de la télétransmission.
- [ ] FS03 — Identifier auteur de la décision et régime ; réclamation privée puis médiateur compétent via INS-005, échéances via INS-021. Ne pas appliquer CRA/CMRA à la complémentaire ni transférer ses délais à la CPAM.

Scénarios **attendus, non exécutés** : soin avant résiliation mais facture
postérieure ; ancienne mutuelle encore raccordée ; simulation contredite par
plafond ou code. Sortie : clauses, dates, pièces et brouillon, sans prestation
recalculée. Collecte minimale sans stockage. [Portée](../dom-007-annexes/dom-007-frictions-verification.md).
