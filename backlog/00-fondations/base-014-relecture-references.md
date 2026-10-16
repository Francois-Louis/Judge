---
id: BASE-014
titre: "Relire les références embarquées avant chaque livraison"
statut: proposee
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

- [ ] Chaque source des références du lot porte date et issue de relecture.
- [ ] Le constructeur refuse un lot dont une source n'est pas relue pour cette livraison, test à l'appui.
- [ ] Une modification constatée produit une mise à jour de la référence et une entrée NOTICE.
- [ ] La relecture de `hiring-review-fr.md` est faite et consignée pour le prochain lot.

## Vérification

- Cas normal : toutes les sources relues, aucune modification → lot construit, dates dans l'inventaire.
- Cas limite : article modifié depuis la rédaction → construction refusée tant que la référence n'est pas mise à jour.
- Cas limite : Légifrance inaccessible, voie alternative BASE-010 réussie → relecture consignée avec la voie utilisée.

## Hors périmètre

Veille continue entre deux livraisons (VEI-021), recherche jurisprudentielle
exhaustive, mise à jour automatique sans relecture humaine.
