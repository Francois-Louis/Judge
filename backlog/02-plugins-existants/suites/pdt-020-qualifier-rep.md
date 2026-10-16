---
id: PDT-020
titre: "Qualifier une mise sur le marché au regard de la REP"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-020 — Qualifier une mise sur le marché au regard de la REP

## Objectif et résultat attendu

Un artisan, importateur ou vendeur reçoit une fiche de rôle et de filière REP pour un flux de produits ou d’emballages identifié.

Issue de la [matrice des 140 frictions marketing](../exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant proposé ou existant `judge-fr-eu-product-legal`.

- `product-legal/skills/qualifier-rep/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `product-legal/references/qualification-rep.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Chaîne fournisseur/conditionneur/importateur/distributeur, pays et dates, destinataires, produits gratuits ou vendus, emballages ménagers/professionnels/expédition, effectif et activité si pertinents.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Décomposer une opération par pays et filière ; identifier les faits de première mise à disposition et les éventuelles exceptions à rechercher. Ne pas confondre fabricant matériel, producteur réglementaire, plateforme ou titulaire de l’IDU. Demander au fournisseur la preuve de prise en charge invoquée et signaler les risques de doublon sans conclure depuis une facture seule. Le rôle PPWR reste une qualification distincte.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Code de l’environnement et textes propres à la filière ; ADEME, ministère, arrêtés d’agrément et textes nationaux des pays concernés. Vérifier le statut normatif d’un report, ses transitions et son champ ; une annonce administrative ne remplace pas le texte.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Artisan expédiant en France un produit dans un carton acheté à un fournisseur : chaîne et filière à vérifier avant attribution de l’obligation.
- Cas limite : Produits offerts, clients professionnels et ventes dans deux pays : lignes distinctes ; IDU français et statut de microentreprise ne suffisent pas à conclure.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Adhésion, déclaration, calcul de taxe, conformité générale de l’entreprise ou avis sur toutes les filières.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-frictions-verification.md).
