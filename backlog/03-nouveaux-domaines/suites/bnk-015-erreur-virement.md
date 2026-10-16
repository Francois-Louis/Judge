---
id: BNK-015
titre: "Réagir à une erreur d'exécution ou de bénéficiaire d'un virement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-015 — Réagir à une erreur d'exécution ou de bénéficiaire d'un virement

## Objectif et résultat attendu

L'émetteur d'un virement qui s'est trompé de bénéficiaire ou constate une anomalie d'exécution prépare immédiatement une demande de recherche, de rappel ou de correction adaptée.

Besoin issu des frictions 22, 25, 40 de la [matrice utilisateur](../dom-004-annexes/dom-004-frictions-utilisateurs.md).

## Périmètre et fichiers

- `banking-legal/skills/transfer-error-claim/SKILL.md` — le skill (à créer)
- `banking-legal/references/erreur-virement.md` — qualification, pièces, demandes et sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

Les références de qualification et de paiement de BNK-001 sont relues, pas réécrites.

## Pièces et informations nécessaires

Ordre et confirmation masqués, nom et IBAN partiellement masqué du bénéficiaire prévu, dates, devise, pays et prestataires, avertissement de concordance affiché, relevé et échanges.

## Sortie attendue

Fiche ordre/exécution ; qualification provisoire erreur du donneur d'ordre ou anomalie d'exécution ; demande urgente de recherche ou rappel ; pièces et brouillon au prestataire. Les règles, montants et délais nécessitent une source lue et la date des faits.

## Travail attendu

Séparer IBAN saisi par erreur, virement non autorisé (BNK-001) et manipulation (BNK-002). Examiner les éléments affichés lors de la vérification du bénéficiaire et le champ d'application temporel et territorial. Irrévocabilité, rappel technique et droit éventuel à réparation sont trois questions séparées.

Appliquer le contrat commun DOM-004 : urgence, minimisation des données, brouillons seulement, autonomie du paquet et méthode BASE-005 embarquée.

## Références métier et sources à rechercher

Code monétaire et financier, identifiant unique, exécution et responsabilité des prestataires ; règlement (UE) 2024/886, vérification du bénéficiaire et calendrier selon le prestataire. Pistes non vérifiées par cette proposition ; rechercher le texte et sa version applicable lors de l'implémentation.

## Critères d'acceptation

- [ ] Le brouillon demande rapidement le rappel sans garantir la récupération ni un remboursement automatique.
- [ ] La sortie recherche les preuves de vérification et laisse son applicabilité ouverte si pays, date ou prestataire manquent.
- [ ] La sortie reste compréhensible sans formation juridique et le skill fonctionne dans le paquet détaché.

## Vérification

- Cas normal : VIR01 — IBAN erroné saisi et ordre confirmé, sans fraude alléguée.
- Cas limite : VIR02 — Le nom et l'IBAN ne concordent pas, aucune alerte conservée ; prestataire étranger.
- Source absente ou contrat incomplet : questions et pièces manquantes, règle réservée.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Action contre le bénéficiaire, exécution du rappel, calcul de réparation, envoi.

## État de la proposition — 16 octobre 2026

Ajout issue des frictions fournies par l'utilisateur ; sans implémentation ni sélection. Contrat commun : [découpage](../dom-004-annexes/dom-004-decoupage-banque.md).
