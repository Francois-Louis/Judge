---
id: PILOTE-005
titre: "Appliquer les corrections issues de la rétrospective du pilote travail"
statut: terminee
priorite: P1
nature: implementation
dependances: [PILOTE-002, PILOTE-003, PILOTE-004]
---

# PILOTE-005 — Appliquer les corrections issues de la rétrospective du pilote travail

## Objectif

Corriger les écarts relevés par la [rétrospective de l'epic](retrospective-pilote-travail.md)
qui ne demandent aucune décision : fins de ligne, mentions périmées de la CLI,
décomptes et NOTICE désynchronisés, règles manquantes du modèle de story.

## Périmètre

- Epic 01 : `pilote-004-verification.md`, `pilote-003-bilan-pilote.md`.
- Paquet : `employment-legal/.claude-plugin/plugin.json`, `employment-legal/NOTICE`
  (fins de ligne seulement).
- Racine : `NOTICE`, `.claude-plugin/marketplace.json` (fins de ligne), README du
  backlog, [modèle de story](../story-template.md).

## Critères d'acceptation

- [x] Les quatre fichiers passés en CRLF sont en LF ; aucun autre octet modifié.
- [x] Plus aucune mention de CLI absente n'est présentée comme l'état actuel.
- [x] Le README du backlog compte toutes les stories et renvoie à la rétrospective.
- [x] Le NOTICE racine recense PILOTE-004 comme le NOTICE du plugin.
- [x] Le modèle de story impose de consigner la recherche d'un outil déclaré
  absent, et de lier les critères d'une story de validation au résultat observé.

## Hors périmètre

Commits, environnement de recette, lecteur réel, allègement de `hiring-review`,
option `--claude` du contrôleur, politique de recensement dans NOTICE.

## Bilan d'exécution — 15 octobre 2026

- Fins de ligne normalisées en LF ; `git diff --ignore-cr-at-eol` sur ces fichiers
  inchangé avant/après. Conséquence : `plugin.json` et `marketplace.json` ne
  correspondent plus aux empreintes CRLF de [PILOTE-003](pilote-003-controles.json)
  et [PILOTE-004](pilote-004-controles.json). L'artefact exact de PILOTE-003 reste
  dans `%TEMP%` avec son ZIP. La prochaine recette produit un nouvel inventaire.
- `pilote-004-verification.md` : la structure et la recette renvoient à la
  [reprise des schémas](pilote-003-schema-cli.json).
- README du backlog : décompte, lien vers la rétrospective, PILOTE-005 dans le tableau.
- NOTICE racine : entrée PILOTE-004 (fichiers du plugin et script de test).
- Modèle de story : deux règles ajoutées dans « Vérification ».
- `pilote-003-bilan-pilote.md` : ligne vide finale retirée.

## Portée

Corrections documentaires et de fins de ligne seulement : aucun comportement de
skill ni contenu de plugin modifié. Les contrôles rejoués après correction sont
indiqués dans la [rétrospective](retrospective-pilote-travail.md). Ils ne
remplacent pas la recette en client ni l'essai avec un lecteur réel.
