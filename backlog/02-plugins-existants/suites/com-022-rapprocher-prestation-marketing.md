---
id: COM-022
titre: "Rapprocher une prestation marketing et sa facturation"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006]
---

# COM-022 — Rapprocher une prestation marketing et sa facturation

## Objectif et résultat attendu

Un indépendant reçoit un tableau promesses/livrables/mesures/dépenses/honoraires/justificatifs et une demande d’explication à son agence.

Issue de la [matrice des 140 frictions marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `commercial-legal` ; identifiant proposé ou existant `judge-fr-eu-commercial-legal`.

- `commercial-legal/skills/vendor-agreement-review/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `commercial-legal/references/prestation-marketing.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Devis et CGV, factures, preuves de paiement, rapports, définitions de lead/vente/clic, paramètres d’attribution, preuves des achats publicitaires et éventuels mandats/commissions.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Distinguer SEO, annonces payantes, trafic, clics, prospects et ventes. Rapprocher période/périmètre des indicateurs et doublons d’attribution possibles sans calcul de ROI non justifié. Séparer budget média, honoraires, commissions et résultat contractuellement promis. Décrire les éléments de faux trafic allégué sans diagnostiquer des robots depuis les chiffres seuls. Vérifier si le régime de transparence de l’achat d’espace est pertinent selon montage ; pas d’application universelle.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Code civil et Code de commerce, contrat et règles françaises de transparence de l’achat d’espace si dans le champ, consommation seulement après qualification de protections interprofessionnelles ; jurisprudence officielle ciblée. Règle privée de référencement séparée du droit.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Rapport de clics présenté comme ventes et facture média globale : tableau des unités et justificatifs à demander.
- Cas limite : Deux plateformes revendiquent les mêmes conversions, données brutes absentes : chevauchement possible, aucun montant remboursable établi.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Audit technique SEO/fraude, expertise comptable, accès aux comptes, calcul automatique de dommages ou demande bancaire.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-annexes/exist-004-frictions-verification.md).
