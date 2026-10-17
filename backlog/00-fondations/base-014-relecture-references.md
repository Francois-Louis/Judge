---
id: BASE-014
titre: "Relire les références embarquées avant chaque livraison"
statut: terminee
priorite: P1
nature: implementation
dependances: [BASE-005, BASE-006, LIV-001]
---

# BASE-014 — Relire les références embarquées avant chaque livraison

## Objectif

Aucun lot ne part avec une référence juridique embarquée dont la version, les
modifications ou la jurisprudence n'ont pas été revérifiées pour cette
livraison. Décision de l'utilisateur du 16 octobre 2026
([décisions](../decisions-2026-10-16.md)).

## Périmètre

- Références métier embarquées des plugins livrés (par exemple
  `employment-legal/references/hiring-review-fr.md`) et leurs tableaux de
  sources.
- Contrôleur [check-plugin-package.py](../../scripts/check-plugin-package.py)
  ou nouveau script, et [constructeur de lot](../../scripts/build-lot.py).
- [Recette BASE-006](../../references/package-validation.md) et procédure de
  livraison LIV.

## Travail attendu

- Ajouter à chaque source embarquée une date de dernière relecture réelle,
  distincte de la date de rédaction, et l'issue de la relecture (inchangée,
  modifiée, abrogée, jurisprudence nouvelle, inaccessible).
- Lors d'une relecture : texte et version consolidée, modifications publiées
  depuis la dernière relecture, dispositions transitoires, projets adoptés,
  décisions nouvelles utiles. Utiliser les voies officielles BASE-010.
- Faire refuser la construction d'un lot si une source n'a pas été relue
  pendant la préparation du lot, ou si une source est marquée modifiée sans
  mise à jour de la référence ; l'inventaire du lot liste les dates.
- Une source inaccessible reste signalée et sa conclusion réservée ; elle ne
  bloque pas le lot si la réserve est déjà dans la référence.

## Critères d'acceptation

- [x] Chaque source des références du lot porte date et issue de relecture. *Lot `employment-legal` ; `commercial-legal` à relire lors de son lot.*
- [x] Le constructeur refuse un lot dont une source n'est pas relue pour cette livraison, test à l'appui.
- [x] Une modification constatée produit une mise à jour de la référence et une entrée NOTICE. *Imposé par le constructeur, vérifié sur fixture : aucune modification réelle constatée.*
- [x] La relecture de `hiring-review-fr.md` est faite et consignée pour le prochain lot. *Lot préparé à partir du 17 octobre 2026.*

## Vérification

- Cas normal : toutes les sources relues, aucune modification → lot construit, dates dans l'inventaire.
- Cas limite : article modifié depuis la rédaction → construction refusée tant que la référence n'est pas mise à jour.
- Cas limite : Légifrance inaccessible, voie alternative BASE-010 réussie → relecture consignée avec la voie utilisée.

## Hors périmètre

Veille continue entre deux livraisons (VEI-021), recherche jurisprudentielle
exhaustive, mise à jour automatique sans relecture humaine.

## Bilan d'exécution — 17 octobre 2026

- [source_reviews.py](../../scripts/source_reviews.py) : contrôle des
  références métier d'un plugin (hors copie de la méthode commune). Toute
  source officielle liée doit figurer dans un tableau à colonne `Relecture`
  (`AAAA-MM-JJ · issue · voie[ · précision]`), datée entre le début de la
  préparation et le jour même ; un changement exige `intégrée X.Y.Z` égal à la
  version de la référence et une entrée NOTICE ; une source inaccessible exige
  `réserve`.
- [build-lot.py](../../scripts/build-lot.py) : option obligatoire
  `--relecture-depuis`, refus du lot en cas d'erreur, relevé des relectures
  dans `lot-inventory.json`. [Fixtures](../../scripts/test-source-reviews.py) :
  10 tests, dont une construction réelle et un refus réel.
- [Recette BASE-006 1.3.0](../../references/package-validation.md) : section
  « Relire les sources embarquées avant chaque lot » et ligne de la fiche de
  preuve ; `CLAUDE.md` du dépôt complété.
- `employment-legal` 0.3.2 : relecture réelle du 17 octobre 2026 de toutes les
  sources de `hiring-review-fr.md` et `worker-classification-fr.md`, consignée
  dans leurs colonnes `Relecture` ; aucune modification, une décision toujours
  inaccessible avec réserve. Journal : [relecture](base-014-annexes/base-014-relecture.json) ;
  contrôles : [vérification](base-014-annexes/base-014-verification.md).

## Portée

Voir la portée de la [vérification](base-014-annexes/base-014-verification.md).
Le contrôle lit le texte des références : la réalité et l'exactitude des
lectures restent de la responsabilité du préparateur. Versions futures
recherchées sur Légifrance pour un seul article ; pas de recherche
jurisprudentielle exhaustive. `commercial-legal` et les plugins hérités ne
sont pas relus : leur lot sera refusé tant qu'ils ne le seront pas. La méthode
commune et ses repères S1 à S4 ne sont pas soumis au contrôle.
