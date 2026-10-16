---
id: PDT-022
titre: "Vérifier les justificatifs et la communication d’un IDU"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-020]
---

# PDT-022 — Vérifier les justificatifs et la communication d’un IDU

## Objectif et résultat attendu

Une petite entreprise reçoit un état par filière des justificatifs d’identification REP et des emplacements de communication à instruire.

Issue de la [matrice des 140 frictions marketing](../exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant proposé ou existant `judge-fr-eu-product-legal`.

- `product-legal/skills/verifier-idu/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `product-legal/references/identifiants-rep.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Rôle/filière qualifiés ou fiche manuelle, SIRET, attestations, identifiants fournis, titulaire, dates, contrat, CGV et pages du site, demande éventuelle d’une marketplace.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Distinguer SIRET, IDU et référence contractuelle. Rapprocher titulaire, filière, statut et source ; distinguer identifiant fourni et vérifié. Rechercher quelles communications incombent à cet acteur. Une attestation de fournisseur ne couvre pas toutes les opérations ; une résiliation n’établit pas seule l’effet sur l’identifiant. Donner pièces et questions de continuité, sans résilier ni enregistrer.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Code de l’environnement, textes de filière et ADEME pour enregistrement et communication ; source officielle consultable et preuve datée. Vérifier les conséquences d’une rupture d’adhésion sans déduire une perte automatique.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Attestation et CGV d’une même filière : tableau titulaire/validité observée/emplacements et preuves manquantes.
- Cas limite : IDU fournisseur réutilisé pour d’autres produits ou ventes étrangères : couverture réservée, pas d’identifiant européen universel.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Création ou récupération d’un IDU, modification d’un registre, affichage effectif et résiliation d’adhésion.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-frictions-verification.md).
