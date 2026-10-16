---
id: PI-031
titre: "Documenter les droits d’un visuel publicitaire synthétique"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-031 — Documenter les droits d’un visuel publicitaire synthétique

## Objectif et résultat attendu

Un créateur ou une petite marque reçoit une carte des droits et autorisations pour un visuel/une séquence générés ou retouchés, avec usages permis établis ou réservés.

Issue de la [matrice des 140 frictions marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `ip-legal` ; identifiant proposé ou existant `judge-fr-eu-ip-legal`.

- `ip-legal/skills/clearance/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `ip-legal/references/droits-campagne-synthetique.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Visuel/version et éléments source disponibles, générateur et conditions à la date d’usage, commande agence, personnes/voix/marques reconnaissables, licences et autorisations, supports, pays et durée de campagne.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Séparer droits sur les sources, licence du service, éventuelle protection de la sortie, droits des tiers et droit à l’image/voix. Le paiement de l’agence ou une licence commerciale du générateur ne purge pas les droits des tiers et ne démontre pas une originalité protégeable. Cartographier usages organiques/publicitaires, retouches, durée et territoire ; produire les questions et autorisations à demander. PI-007/009/010 gardent la photo identifiée ; DOM-035/043 le litige de personnalité/expression à qualifier. IA-005 et PDT-009 gardent transparence et mentions.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

CPI, Code civil et jurisprudence officielle pertinente pour image/voix/personnalité, textes UE applicables ; conditions/licences et contrats datés comme pièces privées. Ne pas assimiler INPI à une autorité générale ordonnant le retrait d’une image.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Agence livre un avatar avec sources et licence mais aucun visage réel identifié : carte des usages et réserves sur droits/protection.
- Cas limite : Voix de célébrité ou photo de tiers reprise sans autorisation : preuve et questions manquantes, aucune diffusion autorisée par la seule mention IA.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Autorisation générale, verdict de contrefaçon, détection IA, retrait ou publication exécutés.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-annexes/exist-004-frictions-verification.md).
