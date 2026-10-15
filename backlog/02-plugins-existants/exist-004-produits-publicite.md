---
id: EXIST-004
titre: "Découper l'adaptation des produits et de la publicité"
statut: proposee
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

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `product-legal`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer un lancement B2C en France et une campagne publicitaire avec allégation environnementale, sans conclure sur leur conformité pendant le cadrage.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

