---
id: BASE-002
titre: "Choisir le niveau d'indépendance du dépôt"
statut: terminee
priorite: P0
nature: decision
dependances: [BASE-001]
---

# BASE-002 — Choisir le niveau d'indépendance du dépôt

## Objectif

Distinguer l'absence de PR vers l'origine de la disparition du lien public entre les deux dépôts.

## Points de départ

- [.git/config](../../.git/config)
- [.github/workflows/cla.yaml](https://github.com/Francois-Louis/Judge/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/.github/workflows/cla.yaml) — supprimé par BASE-007 ; version auditée au commit `4a6c651`

## Travail attendu

- Documenter les options : conserver le fork, quitter le réseau de forks si l'option est disponible, ou créer un dépôt indépendant.
- Vérifier dans la documentation GitHub actuelle les effets sur l'historique, les issues, les PR, les autres métadonnées et la visibilité.
- Consigner le choix de l'utilisateur et, seulement ensuite, préparer une éventuelle opération distante dans une story dédiée.

## Critères d'acceptation

- [x] Le document explique qu'un commit ou push vers le fork ne crée pas, à lui seul, une PR vers l'origine.
- [x] Il ne promet pas l'invisibilité d'un fork public ni l'effacement de copies de commits déjà publiques.
- [x] Les pertes et effets irréversibles des options sont explicites.
- [x] Le choix reste « à décider » tant que l'utilisateur ne l'a pas fait ; aucune option destructive n'est exécutée.

## Vérification

Confronter chaque option à la documentation officielle GitHub et aux fonctions réellement disponibles sur ce dépôt.

## Hors périmètre

Effectuer le détachement, supprimer/recréer le dépôt ou publier du contenu.

## Bilan d'exécution — 15 octobre 2026

- Livrable : [dossier de décision](base-002-dossier-decision.md), comparant le
  maintien du fork, la sortie du réseau et la création d'un dépôt indépendant.
- Documentation officielle GitHub consultée : historique Git, visibilité,
  pertes de métadonnées, duplication, sauvegardes et suppression. Le dossier
  distingue la copie sous un autre nom de la suppression/recréation de Judge.
- Vérifications en lecture : configuration et URL Git locales, API publique
  du dépôt et de ses forks, métadonnées authentifiées via le connecteur GitHub.
  Judge est public, de taille annoncée 1 711 Ko, sans fork enfant ; l'accès
  administrateur est confirmé. Le bouton « Leave fork network » dans Settings
  n'a pas été inspecté : disponibilité effective encore à confirmer.
- Contrôles locaux : liens relatifs du livrable et de la story, cohérence du
  frontmatter et des critères d'acceptation, absence de changement des fichiers
  suivis et de la configuration Git.
- **Choix de l'utilisateur : à décider.** Le statut `terminee` concerne le
  dossier et les critères ci-dessus ; il ne signifie pas qu'une option a été
  choisie. Une éventuelle story d'opération distante sera préparée après ce choix.
- Aucun commit, push, PR, détachement, changement de visibilité, suppression,
  création de dépôt ou publication n'a été effectué.

