---
id: PDT-024
titre: "Constituer la fiche factuelle d’un emballage PPWR"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-024 — Constituer la fiche factuelle d’un emballage PPWR

## Objectif et résultat attendu

Une TPE reçoit un dossier d’un emballage/version : composants, rôles, usages et justificatifs disponibles ou manquants pour les contrôles PPWR.

Issue de la [matrice des 140 frictions marketing](../exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant proposé ou existant `judge-fr-eu-product-legal`.

- `product-legal/skills/dossier-emballage-ppwr/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `product-legal/references/dossier-emballage-ppwr.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Description et nomenclature, dimensions/poids, colles/films/fenêtres/revêtements, usages vente/groupage/transport/e-commerce, contact alimentaire, fournisseurs, pays et dates, essais et attestations.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Cartographier composants et chaîne d’opérateurs ; documenter usage, réemploi revendiqué, contenu recyclé, recyclabilité et substances comme questions distinctes. Une matière dite recyclable ne prouve ni filière effective ni contenu recyclé. Recueillir la méthode de mesure du vide et traiter le calage selon la disposition recherchée. Identifier justificatifs PFAS si contact alimentaire pertinent ; ne pas produire de résultat d’essai depuis une fiche commerciale.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Règlement (UE) 2025/40 et actes associés, articulation avec textes contact alimentaire et substances si dans le champ ; textes/version/date et rôles exacts. Les attestations du fournisseur restent des preuves à apprécier, pas une exemption générale.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Boîte, film et calage d’un envoi e-commerce : fiche séparant composants, fonctions et preuves.
- Cas limite : Boîte robuste dite réutilisable ou emballage alimentaire sans composition du revêtement : qualification et contrôle substances réservés, questions au fournisseur.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Essais de laboratoire, calcul d’ACV, certification de recyclabilité, déclaration de conformité complète ou qualification REP automatique.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-frictions-verification.md).
