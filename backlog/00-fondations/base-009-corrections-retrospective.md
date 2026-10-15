---
id: BASE-009
titre: "Appliquer les corrections issues de la rétrospective des fondations"
statut: terminee
priorite: P0
nature: implementation
dependances: [BASE-001, BASE-008]
---

# BASE-009 — Appliquer les corrections issues de la rétrospective des fondations

## Objectif

Corriger les écarts relevés par la [rétrospective de l'epic](retrospective-fondations.md)
qui ne demandent aucune décision de l'utilisateur : formulations du hub
contraires à l'accord par mise à jour, scripts de cookbooks non portables,
backlog non actualisé et preuves non reproductibles.

## Périmètre

- `legal-builder-hub` : `agents/registry-sync.md`, `skills/auto-updater/SKILL.md`,
  `skills/customize/SKILL.md`, `README.md` et les deux `NOTICE` concernés.
- `scripts/test-cookbooks.sh` et `scripts/deploy-managed-agent.sh`.
- Backlog : README, statut de BASE-008, liens vers le workflow CLA supprimé.
- Documentation des dépendances de test : [CLAUDE.md](../../CLAUDE.md) et
  [relevé BASE-008](../../references/base008-validation.md).

## Travail attendu

- Supprimer toute formulation laissant croire à un mode d'application
  automatique des mises à jour communautaires. Le comportement voulu existe
  déjà dans `auto-updater` : diff, contrôle de confiance, accord explicite.
- Faire choisir aux scripts de cookbooks un interpréteur Python qui s'exécute
  réellement ; sous Windows, `python3` peut être un raccourci du Microsoft Store.
- Actualiser les statuts et constats du backlog devenus faux depuis BASE-008.
- Documenter l'environnement nécessaire pour rejouer les preuves.

## Critères d'acceptation

- [x] Aucun fichier du hub n'annonce une mise à jour appliquée sans accord.
- [x] Le dry-run des cinq cookbooks passe sur un poste Windows où `python3`
  est un raccourci non fonctionnel.
- [x] Le backlog n'affirme plus qu'aucun plugin n'est modifié ou synchronisé ;
  le statut de BASE-008 appartient au vocabulaire défini.
- [x] Les dépendances de test sont écrites ; l'absence d'un outil reste signalée
  comme test ignoré, jamais comme réussite.

## Hors périmètre

Choix du lien de fork (BASE-002), recette authentifiée et test réel des liens
symboliques (BASE-008), refonte complète du hub (EXIST-011), réglages GitHub,
push, PR ou publication.

## Bilan d'exécution — 15 octobre 2026

- Hub : `registry-sync` n'annonce plus « Applied N updates » ni d'installation
  sous réserve d'un auto-update ; `auto-updater` lit une préférence
  `notify / manual` ; `customize` refuse l'activation d'un mode automatique ;
  le README n'invite plus à l'activer. Les `NOTICE` racine et du hub listent
  ces fichiers. Recherche des formulations résiduelles : aucune occurrence.
- Scripts : variable `PYTHON` résolue au premier interpréteur fonctionnel
  (`python3`, puis `python`), surchargeable par l'environnement.
- Contrôles rejoués avec jsonschema et jq **1.8.1** installés dans un répertoire
  temporaire, sans installation globale :
  - `bash scripts/test-cookbooks.sh` : lint 5/5, dry-run 5/5 (5/4/4/4/4 corps) ;
  - `python scripts/test-base008-isolation.py` : 16 tests, 15 réussis,
    1 ignoré (lien symbolique, WinError 1314) ;
  - `python scripts/test-check-plugin-package.py` : 11/11 ;
  - contrôleur BASE-006 sur une copie détachée du hub : aucune erreur,
    47 points de relecture inchangés dans leur nature ;
  - `git diff --check` : propre.
- Backlog : README actualisé, BASE-008 passée au statut `en-cours`, liens
  vers `cla.yaml` remplacés par un permalien vers le commit `4a6c651`.
- Limites : aucune session de modèle, aucun skill exécuté, aucune modification
  distante. BASE-002 et la clôture de BASE-008 restent ouvertes.
