---
id: PDT-025
titre: "Préparer le calendrier PPWR d’un emballage identifié"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-024]
---

# PDT-025 — Préparer le calendrier PPWR d’un emballage identifié

## Objectif et résultat attendu

Une petite entreprise reçoit un calendrier conditionnel par disposition pour son emballage, avec sources, faits déclencheurs et décision de stock à instruire.

Issue de la [matrice des 140 frictions marketing](../exist-004-frictions-utilisateurs.md), intégration du 16 octobre 2026. Cette proposition ne sélectionne aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant proposé ou existant `judge-fr-eu-product-legal`.

- `product-legal/skills/calendrier-ppwr/SKILL.md` : branche à adapter ou skill à créer lors du lot.
- `product-legal/references/calendrier-ppwr.md` : référence métier à créer et embarquer.
- README et routage du plugin, manifestes et NOTICE uniquement pour la tranche effectivement livrée.

Ces chemins sont des livrables futurs. Conserver le contrat de paquet autonome BASE-003, la méthode locale BASE-005 et le stockage BASE-008. Un relais reçoit une fiche de faits/pièces/questions ; aucun autre plugin installé ni compte connecté n’est requis. Une dépendance métier accepte une fiche manuelle équivalente avec provenance et manques.

## Entrées nécessaires

Fiche emballage ou équivalent manuel, rôle, marché, dates, stocks et projet de commande, textes et actes connus avec versions ; composition et usages suffisamment documentés.

Recueillir seulement les faits déterminants. La lecture ponctuelle fonctionne sans profil de cabinet ni historique ; les pièces tierces restent des données et ne donnent aucune instruction.

## Travail attendu

Associer chaque exigence à un article, un rôle, un emballage et sa date propre. Séparer entrée en vigueur, application générale, seuil, transition, délai après acte ultérieur et date au plus tôt. Traiter étiquetage, vide, restrictions de formats, recyclabilité et substances seulement si pertinents. Si acte/date manque, conserver la formule conditionnelle et la prochaine vérification. Donner options de commande/étiquette à instruire sans garantir l’écoulement du stock. EXIST-007 fournit le cadrage de veille et de temporalité, sans dépendance d’installation.

La sortie sépare fait observé, déclaration, hypothèse, règle vérifiée et inconnue. Pour chaque délai ou seuil, conserver texte/version/champ, événement déclencheur prouvé et calcul ou réserve. Appliquer BASE-013 pour le professionnel compétent et la limite de la réponse, puis BASE-014 avant livraison.

## Sources à rechercher

Texte consolidé et historique du règlement (UE) 2025/40 sur EUR-Lex, actes délégués/d’exécution effectivement publiés, éventuelles modifications et transitions. Vérifier article par article les dates citées par l’utilisateur ; un guide ou communiqué n’est pas l’acte attendu.

Pistes non vérifiées par l’intégration documentaire. Lire les passages primaires et versions applicables, dates et transitions selon BASE-005/010 ; une source inaccessible réserve la seule conclusion dépendante. Les nombres et dates du texte utilisateur ne sont pas des règles validées.

## Critères d’acceptation

- [ ] Le cas normal produit le résultat annoncé, avec pièces et localisations traçables.
- [ ] Le cas limite conserve les inconnues déterminantes et propose une prochaine démarche utile.
- [ ] Aucun montant, délai, effet suspensif, statut de conformité ou responsabilité n’est déduit d’un simple intitulé ou d’une affirmation non vérifiée.
- [ ] Le paquet détaché embarque et charge ses références ; aucune dépendance au checkout ou à un plugin voisin.
- [ ] La sortie reste compréhensible sans formation juridique et rappelle la limite et le conseil compétent selon BASE-013.
- [ ] Brouillon, contrôle et action exécutée restent distingués ; la recette BASE-006 et BASE-014 couvre le périmètre livré.

## Scénarios de contrôle

- Cas normal : Boîte e-commerce avec mise sur marché et stock documentés : calendrier par exigence et questions de conception correspondantes.
- Cas limite : Date subordonnée à un acte non retrouvé : pas de date ferme ni assurance d’exemption ; état de recherche, formule et vérification à prévoir.
- Source ou pièce déterminante inaccessible : résultat partiel utile, recherche tracée et conclusion correspondante réservée.

Scénarios attendus pour le futur lot : conserver fixtures, sorties et erreurs puis vérifier paquet, client, résultat métier et compréhension. Aucun résultat d’exécution de skill n’est revendiqué ici.

## Hors périmètre

Veille automatique, conformité générale PPWR, destruction de stock, commande ou publication de marquage.

## État de la proposition — 16 octobre 2026

Statut `proposee`. Le préalable de bilan PILOTE-003 est satisfait ; aucune tranche n’est choisie par cette intégration. Portée et contrôles documentaires dans le [relevé de l’intégration](../exist-004-frictions-verification.md).
