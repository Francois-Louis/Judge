---
id: BASE-012
titre: "Désigner le binaire claude utilisé par le contrôleur de paquet"
statut: terminee
priorite: P1
nature: implementation
dependances: [BASE-006]
---

# BASE-012 — Désigner le binaire claude utilisé par le contrôleur de paquet

## Objectif

Le contrôle `--schema` de BASE-006 ne cherchait `claude` que dans le PATH,
alors qu'un binaire embarqué par l'application desktop était disponible
(écart 4 de la [rétrospective du pilote](../01-pilote-travail/retrospective-pilote-travail.md)).
Décision de l'utilisateur du 16 octobre 2026 : option et variable dédiées.

## Critères d'acceptation

- [x] `--claude <chemin>`, puis `JUDGE_CLAUDE_CLI`, puis le PATH désignent le binaire.
- [x] La sortie indique le binaire retenu et son origine (`SCHEMA CLI`).
- [x] Un chemin désigné introuvable donne `NON_EXECUTE`, jamais `SCHEMA OK`.
- [x] Recette BASE-006 et `CLAUDE.md` documentent l'option et la recherche hors du PATH.

## Bilan d'exécution — 16 octobre 2026

- [check-plugin-package.py](../../scripts/check-plugin-package.py) : fonction
  `resolve_cli`, option `--claude`, ligne `SCHEMA CLI`.
- [Fixtures](../../scripts/test-check-plugin-package.py) : deux tests ajoutés
  (chemin explicite et variable ; variable introuvable) ; le test isole la
  variable d'environnement. 13 tests réussis.
- Essai réel : paquet `employment-legal` copié hors du dépôt, binaire embarqué
  2.1.299 désigné par `JUDGE_CLAUDE_CLI` : `SCHEMA OK: code 0`, structure
  `INCOMPLET` (code 2) inchangée.
- [Recette BASE-006](../../references/package-validation.md) en version `1.2.0`.

## Portée

Changement du contrôleur de maintenance seulement : aucun paquet ni skill
modifié. Le schéma officiel ne vaut toujours pas exécution d'un skill.
