---
id: EXIST-004
titre: "Découper l'adaptation des produits et de la publicité"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-004 — Découper l'adaptation des produits et de la publicité

## Objectif

Remplacer les grilles américaines de lancement et d'allégations par des vérifications adaptées aux produits et marchés concernés.

## Points de départ

- [product-legal/skills/launch-review/SKILL.md](../../product-legal/skills/launch-review/SKILL.md)
- [product-legal/skills/feature-risk-assessment/SKILL.md](../../product-legal/skills/feature-risk-assessment/SKILL.md)
- [product-legal/skills/marketing-claims-review/SKILL.md](../../product-legal/skills/marketing-claims-review/SKILL.md)
- [product-legal/references/currency-watch.md](../../product-legal/references/currency-watch.md)

## Travail attendu

- Séparer lancement, évolution de fonctionnalité, publicité et question ponctuelle ; définir une première tâche bornée.
- Identifier qualité des clients, marché, catégorie de produit, rôle de plateforme et réglementation sectorielle avant d'appliquer une grille.
- Répartir les contrôles entre ce plugin, consommation, données et IA ; ne pas charger toutes les réglementations numériques dans chaque revue.
- Sources à prévoir et à vérifier lors des futures implémentations : Code de la consommation, textes français de publicité et de sécurité des produits, actes UE réellement dans le champ, autorités compétentes.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `product-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios (relecture documentaire par le rédacteur sur cas fictifs).
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer un lancement B2C en France et une campagne publicitaire avec allégation environnementale, sans conclure sur leur conformité pendant le cadrage.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire complet](exist-004-inventaire-produits.md) : 23 fichiers dont
  7 skills et 1 agent, 6 fichiers de cookbook lié, profils, grilles inline,
  exemples, références, sorties et relais. Décision motivée pour chaque fichier.
- [Découpage PDT-001 à PDT-017](exist-004-decoupage-produits.md) : 17 propositions
  avec fichiers, entrées, résultat borné, sources à rechercher, exclusions
  et scénarios. Première tranche proposée : fiche de qualification d'un
  lancement B2C France, sans avis de conformité. Lancement, évolution,
  publicité et question ponctuelle ont des parcours distincts.
- [Vérification documentaire](exist-004-verification.md) : lancement France et
  campagne environnementale fictifs, puis limites rôle de plateforme,
  sécurité produit, données/IA, profil et radar. Aucun de ces dossiers n'est
  résolu juridiquement pendant le cadrage.
- [Contrôles statiques et empreintes](exist-004-resultats.json) : couverture,
  frontmatter/dépendances, liens, fichiers futurs, copies communes et
  périmètre ; plugin, cookbook et contenu éditeur inchangés. Travaux
  EXIST-001/002/003 préexistants préservés.
- Le bilan PILOTE-003 est terminé après BASE-011 ; le préalable est satisfait,
  sans choix d'extension. Les 17 PDT restent `proposee` ; les limites H01 complet
  et lecteur indépendant du pilote restent consignées.

Fichiers du lot : présente story, inventaire, découpage, vérification,
résultats JSON, 17 propositions `suites/pdt-*.md` et index `backlog/README.md`.
Le lot reste sous `backlog/`, sans entrée NOTICE selon CLAUDE.md.

**Portée :** cadrage documentaire du checkout, relecture par l'agent de
maintenance sur pièces fictives et contrôles statiques, dans les limites de
la vérification liée. Aucune recherche juridique externe, conclusion de
conformité ou échéance validée, adaptation/exécution de skill, installation,
recette client ou lecteur indépendant, connexion ou action externe. Les
futures recherches et recettes sont décrites dans les propositions, sans
annoncer une adaptation France/UE déjà disponible.

## Intégration marketing — 16 octobre 2026

La [matrice des 140 frictions](exist-004-frictions-utilisateurs.md) relie les besoins aux tâches et relais. Huit propositions PDT-018 à PDT-025 complètent les 17 initiales ; les 25 PDT restent proposées. Les revues d’allégations et d’influence existantes sont précisées, sans implémentation. Les résultats et empreintes historiques ci-dessus sont conservés. Portée de l’intégration et contrôles dans le [relevé dédié](exist-004-frictions-verification.md).
