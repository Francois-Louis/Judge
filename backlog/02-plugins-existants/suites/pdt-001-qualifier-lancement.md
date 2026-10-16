---
id: PDT-001
titre: "Qualifier un lancement B2C en France"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-001 — Qualifier un lancement B2C en France

## Objectif et résultat attendu

Une TPE sans service juridique obtient une fiche de lancement qui distingue ce qui est connu, les contrôles à instruire et les pièces à demander avant toute revue de conformité.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/launch-review/SKILL.md (mode qualification et dispatch)`
- `product-legal/references/qualification-lancement.md (à créer, contrat de fiche)`
- `product-legal/CLAUDE.md (accès ponctuel et qualification)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Description et version du produit, activité de celui qui le propose, destinataires et usages, pays ciblés, canal, calendrier, PRD/écrans disponibles ; rôle fabricant/importateur/vendeur/intermédiaire et éventuels mineurs, données ou IA.

## Travail attendu

Créer une fiche versionnée avec identifiant, provenance et couverture des pièces. Qualifier professionnel/consommateur/non-professionnel à partir des faits, bien/service/contenu numérique, produit propre ou plateforme et secteur potentiel. Ne pas déduire B2C du seul statut du vendeur ni appliquer la grille avant cette collecte. Conserver plusieurs branches si la catégorie manque ; pour une fiche complète, nommer les contrôles pertinents et ceux écartés avec raison. Distinguer lancement, évolution, publicité seule et question ponctuelle. Permettre le résultat conversationnel sans profil durable ni historique, en respectant l'entretien neuf requis si une configuration doit être créée.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher Code de la consommation/Code civil et textes UE nécessaires aux qualifications retenues, avec versions et champ. La fiche n'applique pas encore tout le droit du produit ; toute qualification juridique non établie reste conditionnelle.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] La vente directe de carnets à des particuliers en France produit une fiche acteur/public/marché/catégorie/rôle/date et les pièces manquantes, sans feu vert.
- [ ] Une association acheteuse ou une place de marché ne reçoit pas automatiquement la même grille qu'un consommateur achetant au fabricant.
- [ ] Une publicité seule et une évolution sont orientées vers leur résultat propre, sans lancer les branches héritées.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : L01 — Artisan vendant ses carnets sur son site français : fiche de qualification, écrans et notice à demander, relais ciblés sans conformité annoncée.
- Cas limite : L02 — Même dossier, fonctionnalité place de marché évoquée sans préciser les vendeurs, pays ou produits : branches et questions conservées, aucun DSA universel ni B2C présumé.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-annexes/exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Revue complète, CGV, allégations, AIPD/AIA, qualification détaillée DSA et sécurité, publication ou lancement.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
