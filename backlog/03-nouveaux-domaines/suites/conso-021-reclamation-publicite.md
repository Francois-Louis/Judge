---
id: CONSO-021
titre: "Préparer une réclamation après une publicité contestée"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-004]
---

# CONSO-021 — Préparer une réclamation après une publicité contestée

## Objectif et résultat attendu

Un acheteur reçoit une chronologie annonce/achat/résultat et un brouillon de réclamation ciblé, avec demande et preuves à préciser.

Issue de la [matrice des 140 frictions marketing](../../02-plugins-existants/exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `consumer-legal` ; identifiant proposé ou existant `judge-fr-eu-consumer-legal`.

- `consumer-legal/skills/reclamation-publicite/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `consumer-legal/references/reclamation-publicite.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Annonce complète, URL/date, auteur et vendeur, bon de commande, facture, bien ou service reçu, promesse exacte, conditions, messages et demande recherchée.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Consommer la qualification d’achat CONSO-004 ou son équivalent manuel, puis comparer promesse et faits sans déduire l’illégalité d’une publicité désagréable. Distinguer tromperie alléguée, défaut de conformité, rétractation et inexécution ; ne pas inventer d’annulation automatique. Identifier vendeur, annonceur, agence, influenceur ou plateforme avec rôle établi/inconnu. Les garanties, prix et abonnements gardent leurs parcours existants ; signalement CONSO-013, médiation CONSO-006 et action judiciaire restent distincts. Sans achat, proposer le signalement adapté plutôt qu’une demande de remboursement fictive. Préserver en priorité les contenus éphémères.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Code de la consommation et Code civil selon fondement, pratiques commerciales et textes sectoriels pertinents ; sources officielles des voies de signalement et de médiation. Vérifier canal, compétence, recevabilité et chaque délai sans suspension déduite d’un signalement.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Produit acheté sur la foi d’une démonstration contredite par la livraison : tableau promesse/pièce/écart et projet au vendeur.
- Cas limite : Vidéo possiblement IA sans achat ni preuve de fabrication : soupçon distingué du fait, aucun remboursement ou verdict depuis un détecteur.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Signalement envoyé, plainte pénale, demande judiciaire, diagnostic technique d’IA ou réparation garantie.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../../02-plugins-existants/exist-004-frictions-verification.md).
