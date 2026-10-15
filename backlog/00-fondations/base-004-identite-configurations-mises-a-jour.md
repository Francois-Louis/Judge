---
id: BASE-004
titre: "Définir l'identité du fork et la séparation des configurations"
statut: terminee
priorite: P0
nature: cadrage
dependances: [BASE-001, BASE-003]
---

# BASE-004 — Définir l'identité du fork et la séparation des configurations

## Objectif

Permettre la coexistence de la version française et de la version d'origine sans collision ni écrasement.

## Points de départ

- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- [employment-legal/.claude-plugin/plugin.json](../../employment-legal/.claude-plugin/plugin.json)
- [employment-legal/CLAUDE.md](../../employment-legal/CLAUDE.md)
- [QUICKSTART.md](../../QUICKSTART.md)
- [legal-builder-hub/skills/auto-updater/SKILL.md](../../legal-builder-hub/skills/auto-updater/SKILL.md)
- [LICENSE](../../LICENSE)

## Travail attendu

- Choisir le nom du marketplace et l'espace de configuration du fork ; `judge-fr-eu` est une proposition, pas un nom déjà appliqué.
- Inventorier les chemins de profil, cache et dossiers, les commandes d'installation et les références au nom d'origine.
- Prévoir la migration éventuelle de profils sans écraser des données existantes ni importer automatiquement un profil juridique américain.
- Séparer attribution des contenus d'origine, maintenance des adaptations et affichage du fork ; conserver les obligations de licence.
- Définir une politique de mise à jour qui préserve les adaptations locales et rende les changements relisibles.

## Critères d'acceptation

- [x] La stratégie couvre installation côte à côte, stockage des données et mise à jour.
- [x] Les changements de manifeste, documentation et chemins ont une liste de fichiers et un ordre de migration.
- [x] Une simulation avec deux profils distincts montre qu'aucun n'est lu ou modifié par erreur.
- [x] La mise en œuvre est découpée en une story séparée ; aucune substitution globale n'est lancée à ce stade.

## Vérification

Utiliser des profils factices et un inventaire des références au nom d'origine. Examiner aussi les chemins écrits par les skills de configuration.

## Hors périmètre

Renommer les 150 skills, modifier tous les profils ou changer les auteurs originaux sans justification.

## Bilan d'exécution — 15 octobre 2026

- Livrable : [stratégie d'identité et de configurations](base-004-strategie-identite-configurations.md).
  Nom retenu : `judge-fr-eu` pour le marketplace et les configurations,
  identifiants de plugins préfixés `judge-fr-eu-` pour distinguer les commandes.
  Les manifestes opérationnels n'ont pas encore été renommés.
- [Inventaire reproductible](base-004-inventaire-references.tsv) : 218 fichiers
  à examiner, dont 187 / 1 150 lignes portant le nom d'origine ; profils,
  caches, dossiers, commandes, chemins du hub et déploiements distingués.
- Politique : entretien neuf par défaut, aucune reprise automatique du profil
  ou cache original, destination existante préservée. Attribution d'origine,
  maintenance du fork, licence et affichage séparés ; intégration amont,
  mise à jour de paquet et mise à jour communautaire traitées séparément.
- Vérification : `python scripts/check-base004-isolation.py` passe sur deux
  profils, deux profils partagés et deux dossiers factices de même slug.
  Absence de fallback, refus de collision/traversée/chemin absolu et conservation
  des profils lors d'un changement de paquet simulé vérifiés. Les 10 accès
  du modèle du fork restent dans sa racine ; les fixtures sont supprimées.
- Contrôles complémentaires : inventaire régénéré à l'identique, liens locaux,
  format Markdown, syntaxe Python et identifiants cibles vérifiés ; les 42 JSON
  du dépôt se chargent et le lint de portée des cinq cookbooks passe
  (`python -X utf8 scripts/lint-tool-scope.py`).
- Mise en œuvre découpée dans [BASE-008](base-008-isoler-identite-configurations.md),
  avec liste de fichiers, ordre de migration et recette des paquets réels.
- Limites : simulation du contrat cible, sans exécuter les skills existants,
  sans installation réelle ni migration de profils personnels. CLI `claude`
  indisponible sur le poste ; validation des manifestes par cette CLI et test
  côte à côte reportés à BASE-008. Aucun changement opérationnel des plugins.

