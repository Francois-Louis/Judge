---
id: COM-021
titre: "Lire un contrat de campagne d’influence"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006]
---

# COM-021 — Lire un contrat de campagne d’influence

## Objectif et résultat attendu

Une marque ou un créateur reçoit un tableau livrables/rémunérations/durée/droits/responsabilités et un brouillon de questions sur une campagne.

Issue de la [matrice des 140 frictions marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `commercial-legal` ; identifiant proposé ou existant `judge-fr-eu-commercial-legal`.

- `commercial-legal/skills/vendor-agreement-review/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `commercial-legal/references/contrat-influence.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Contrat, devis, échanges, parties/agence/sous-traitants, objectif, publications, année et cumul des rémunérations/avantages, statistiques et engagements, exclusivité, retrait et droits d’exploitation.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Identifier cocontractants et obligations ; distinguer publication, maintien en ligne, audience déclarée et performance garantie. Rechercher seuil et mentions de l’écrit en tenant compte du cumul et des avantages, sans transformer un montant inférieur en exemption générale. Examiner validation, exclusivité et partage des responsabilités sans croire qu’une clause efface les obligations envers tiers/autorités. PI garde les droits détaillés ; PDT-009 garde les mentions du contenu.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Textes français sur l’influence commerciale et décret de seuil effectivement applicable ; Code civil, règles commerciales et dispositions sectorielles selon public/produit. Vérifier dates, cumul, valorisation et mentions, sans reprendre le seuil de la source comme acquis.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Marque et créateur avec campagne, avantages et livrables écrits : tableau et questions ciblées.
- Cas limite : Plusieurs prestations annuelles et cadeaux dont valeur inconnue : cumul à reconstituer, aucune exemption ni responsabilité exclusive présumée.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Contrat prêt à signer, audit d’audience, publication, revue complète de droits PI ou autorisation sectorielle.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-annexes/exist-004-frictions-verification.md).
