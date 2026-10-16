---
id: PDT-023
titre: "Examiner le marquage d’un emballage pour un marché"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-023 — Examiner le marquage d’un emballage pour un marché

## Objectif et résultat attendu

Un fabricant reçoit une fiche des mentions et consignes de tri à rechercher pour une boîte/version et un pays, avec zones de maquette à adapter.

Issue de la [matrice des 140 frictions marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant proposé ou existant `judge-fr-eu-product-legal`.

- `product-legal/skills/examiner-marquage-emballage/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `product-legal/references/marquage-emballage.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Maquette à l’échelle, dimensions et surfaces, composants, produit, filière, pays de vente, dates de production et mise sur marché, étiquettes et QR code prévus.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Distinguer Triman, information de tri, allégation écologique et futur étiquetage harmonisé. Examiner les adaptations de petit format seulement après vérification du champ. Conserver séparés règle française en vigueur, contentieux UE et changement futur. Une procédure contre un État ne démontre pas une abrogation. Comparer options d’étiquette/maquette sans certifier leur conformité ni ordonner l’impression.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Code de l’environnement et dispositions françaises de marquage, actes UE dont PPWR et actes d’exécution pertinents, état officiel du contentieux si invoqué ; ADEME/ministère pour guides de statut distinct.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Fabricant de couteaux avec boîte export et étiquette France : distinguer graphisme, mentions par marché et pièces à confirmer.
- Cas limite : Très petite boîte avec QR code et futur pictogramme proposé : rechercher dérogations et calendrier, sans présumer que tout peut être dématérialisé.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Bon à tirer réglementaire, impression, conseil universel sur l’autocollant ou label environnemental certifié.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-annexes/exist-004-frictions-verification.md).
