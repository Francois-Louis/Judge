---
id: BASE-001
titre: "Auditer les push et les automatisations du fork"
statut: terminee
priorite: P0
nature: audit
dependances: []
---

# BASE-001 — Auditer les push et les automatisations du fork

## Objectif

Établir précisément ce qui reste local au fork et ce qui pourrait contacter ou modifier le dépôt d'origine.

## Points de départ

- [.git/config](../../.git/config)
- [.github/workflows/cla.yaml](https://github.com/Francois-Louis/Judge/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/.github/workflows/cla.yaml) — supprimé par BASE-007 ; version auditée au commit `4a6c651`
- [CLA.md](../../CLA.md)
- [CONTRIBUTING.md](../../CONTRIBUTING.md)
- [legal-builder-hub/skills/auto-updater/SKILL.md](../../legal-builder-hub/skills/auto-updater/SKILL.md)
- [legal-builder-hub/agents/registry-sync.md](../../legal-builder-hub/agents/registry-sync.md)

## Travail attendu

- Relever les remotes, les URL de push, le suivi de branche et les éventuels hooks locaux, sans exposer de secrets.
- Lire tous les workflows et scripts susceptibles de créer une PR, publier, synchroniser ou mettre à jour du contenu. Distinguer automatisations GitHub et skills exécutés à la demande.
- Proposer les modifications minimales utiles au fork, dont le devenir du workflow CLA et des instructions de contribution héritées. Ne pas confondre ce workflow avec un mécanisme de création de PR.

## Critères d'acceptation

- [x] Un relevé daté décrit chaque mécanisme examiné et sa destination.
- [x] Les destinations d'un push ordinaire sont explicites ; les limites de cet audit local sont indiquées.
- [x] Les mises à jour pouvant écraser une adaptation locale sont identifiées.
- [x] Aucun push, aucune PR et aucune modification distante n'ont été effectués.

## Vérification

Comparer le relevé à `git remote -v`, aux configurations Git effectives et aux fichiers réellement présents. Vérifier les scripts appelés par les workflows, pas seulement leurs noms.

## Hors périmètre

Modifier des réglages GitHub, détacher le fork ou supprimer des ressources distantes. L'application des corrections fera une story bornée après l'audit.

## Bilan d'exécution — 15 octobre 2026

- Livrable : [relevé daté de l'audit](base-001-annexes/base-001-releve-audit.md), avec configuration
  Git effective, hooks, workflow CLA et code tiers épinglé, scripts, skills,
  agents, cookbooks, destinations et risques d'écrasement.
- `main` suit `origin/main` ; les URL effectives de lecture et de push visent
  `git@github.com:Francois-Louis/Judge.git`. Aucun remote `upstream`, réécriture
  d'URL ou hook Git actif observé. Aucune création automatique de PR identifiée.
- Contradiction relevée entre l'accord humain obligatoire de l'auto-updater
  et les formulations d'auto-update de `registry-sync` et d'autres consignes.
- Vérifications : configuration comparée à `git remote -v` et aux URL résolues,
  inventaire et lecture des mécanismes présents, lint des cinq orchestrateurs
  réussi, contrôle des liens et de la cohérence du backlog.
- Suite proposée : [BASE-007](base-007-cla-contributions-fork.md) borne le retrait
  du contrôle CLA hérité et l'adaptation des consignes de contribution.
  L'isolation des profils reste dans BASE-004, les corrections du hub dans
  le découpage EXIST-011. Aucune de ces corrections n'a été appliquée.
- Limites : réglages et applications GitHub, configuration privée des hôtes,
  planifications et déploiements existants non vérifiés. Aucun push, aucune PR
  et aucune modification distante effectués.

