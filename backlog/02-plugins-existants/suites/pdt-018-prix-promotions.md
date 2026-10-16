---
id: PDT-018
titre: "Examiner une annonce de prix ou de promotion"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-005]
---

# PDT-018 — Examiner une annonce de prix ou de promotion

## Objectif et résultat attendu

Une TPE reçoit une fiche annonce/prix de référence/conditions/preuves et les corrections ou questions utiles avant diffusion.

Issue de la [matrice des 140 frictions marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant proposé ou existant `judge-fr-eu-product-legal`.

- `product-legal/skills/marketing-claims-review/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `product-legal/references/prix-promotions.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Support complet, historique de prix daté, produit et variantes, stocks, frais, durée et réinitialisation des compteurs, public, pays et date de campagne.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Confronter prix barré, gratuité, urgence, rareté et comparaison à leurs justificatifs. Séparer réduction de prix, publicité comparative et présentation d’une garantie légale. Examiner la présentation globale et les omissions. Une capture ne prouve ni historique ni stock. Proposer une modification seulement lorsque les pièces la justifient.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Code de la consommation : pratiques commerciales, annonces de réduction, prix et options ; textes de liquidation si concernés, jurisprudence officielle et DGCCRF. Rechercher champ et exceptions de la référence de prix, sans copier une durée universelle.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Prix barré sur une variante avec historique daté : fiche rattachée au bon produit et à la bonne période.
- Cas limite : Compteur qui redémarre et stock inconnu : constater ce qui est visible, demander les preuves et réserver la qualification de fausse rareté.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Réclamation d’un acheteur, audit de stock ou certification de toute la campagne.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-annexes/exist-004-frictions-verification.md).
