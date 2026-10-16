---
id: PDT-021
titre: "Rapprocher les pièces d’une déclaration REP"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-020]
---

# PDT-021 — Rapprocher les pièces d’une déclaration REP

## Objectif et résultat attendu

Une TPE reçoit un tableau traçable quantités/matériaux/catégories/barème/écarts pour une filière et une période, sans dépôt.

Issue de la [matrice des 140 frictions marketing](../exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant proposé ou existant `judge-fr-eu-product-legal`.

- `product-legal/skills/preparer-declaration-rep/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `product-legal/references/declaration-rep.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Qualification REP ou équivalent manuel, ventes et retours, dons, poids et composition, pays, période, barème/version et contrat de l’éco-organisme, déclarations et factures antérieures.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Rapprocher données et pièces ; isoler unités, quantités manquantes, emballages d’expédition, catégories discutées et doublons possibles. Calculer uniquement les lignes dont toutes les hypothèses sont documentées. Séparer écocontribution, prix, régularisation, minimum contractuel et accompagnement facultatif ; COM-002/016 gardent leur contestation. Adhésion, déclaration et paiement ont des preuves distinctes.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Textes de la filière et arrêtés applicables ; ADEME ; barèmes et conditions de l’éco-organisme comme pièces contractuelles, sans les présenter comme lois. Vérifier périodicité et règles de répercussion propres à la filière.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Période avec ventes, poids et barème fournis : rapprochement reproductible et écarts localisés.
- Cas limite : Facture fournisseur supposée couvrir la REP mais périmètre absent : doublon possible, aucune soustraction ni déclaration validée.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Télétransmission, certification de masse, paiement, choix automatique d’un éco-organisme ou réclamation contractuelle complète.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-frictions-verification.md).
