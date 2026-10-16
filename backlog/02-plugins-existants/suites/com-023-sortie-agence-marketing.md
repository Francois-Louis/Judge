---
id: COM-023
titre: "Préparer la sortie d’une agence marketing"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006]
---

# COM-023 — Préparer la sortie d’une agence marketing

## Objectif et résultat attendu

Une TPE reçoit une liste de comptes, données et créations à restituer, un calendrier contractuel réservé si nécessaire et un projet de demande.

Issue de la [matrice des 140 frictions marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `commercial-legal` ; identifiant proposé ou existant `judge-fr-eu-commercial-legal`.

- `commercial-legal/skills/vendor-agreement-review/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `commercial-legal/references/sortie-agence-marketing.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Contrat/avenants, préavis, durée et reconduction, frais de sortie, comptes et administrateurs déclarés, noms de domaine, fiche locale, exports et licences, factures et échanges.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Distinguer propriété juridique, compte technique, rôle administrateur, accès délégué et droit d’export. Comparer promesse mensuelle et engagement réel, prestations en cours et conséquences de sortie. Préparer une demande séquencée de restitution et preuves ; ne pas modifier d’accès ou révoquer un mandat. COM-016/017 restent les revues générales des frais/rupture ; PI examine les licences, DOM-034 une décision de plateforme. Ne pas garantir la restitution de toute audience ou donnée contenant des droits de tiers.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Code civil, droit commercial de la relation et du mandat, contrat/version, règles PI ou données par relais borné ; conditions des plateformes comme pièces privées à dater. Qualification des protections B2B requise avant tout droit de rétractation.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Agence administratrice de comptes et rapport exportable prévus au contrat : demande ciblée et dépendances pratiques.
- Cas limite : Compte créé au nom de l’agence et licence non cessible : conserver l’incertitude, prévoir options et conseil sans promettre transfert.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Résiliation envoyée, révocation d’accès, migration technique, récupération de compte ou transfert forcé de données.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-annexes/exist-004-frictions-verification.md).
