---
id: EXIST-011
titre: "Découper l'adaptation du hub et de ses mises à jour"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-011 — Découper l'adaptation du hub et de ses mises à jour

## Objectif

Garder la découverte et la gestion des skills compatibles avec un fork personnalisé et des sources juridiques françaises.

## Points de départ

- [legal-builder-hub/skills/skill-installer/SKILL.md](../../legal-builder-hub/skills/skill-installer/SKILL.md)
- [legal-builder-hub/skills/auto-updater/SKILL.md](../../legal-builder-hub/skills/auto-updater/SKILL.md)
- [legal-builder-hub/skills/skills-qa/SKILL.md](../../legal-builder-hub/skills/skills-qa/SKILL.md)
- [legal-builder-hub/agents/registry-sync.md](../../legal-builder-hub/agents/registry-sync.md)
- [legal-builder-hub/references/allowlist-default.yaml](../../legal-builder-hub/references/allowlist-default.yaml)
- [legal-builder-hub/skills/registry-browser/references/registries.yaml](../../legal-builder-hub/skills/registry-browser/references/registries.yaml)

## Travail attendu

- Inventorier registres, listes de confiance, profils, mises à jour et autorisations ; ne pas supprimer les protections existantes par simple changement de langue.
- Définir comment distinguer skills du fork, contenus communautaires et contenus éditeur ; aucune mise à jour ne doit écraser silencieusement une adaptation locale.
- Adapter les critères de qualité à la pertinence France/UE en plus de la sécurité technique ; ne pas noter positivement un skill américain parce qu'il cite bien ses sources.
- Rechercher les contradictions entre notifications, installation et auto-application dans l'agent et les skills. Les formulations d'application automatique de `registry-sync`, `auto-updater`, `customize` et du README ont déjà été neutralisées par [BASE-009](../00-fondations/base-009-corrections-retrospective.md) ; vérifier les autres fichiers.
- Sources à prévoir et à vérifier lors des futures implémentations : Règles d'installation du produit, provenance des registres, licences et sources déclarées ; les plugins d'éditeur restent hors modification automatique.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `legal-builder-hub`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Simuler une mise à jour d'un skill personnalisé et la découverte d'un skill propre à une juridiction américaine ; l'un doit préserver les modifications, l'autre afficher sa portée.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire exhaustif](exist-011-annexes/exist-011-inventaire-hub.md) : 30 fichiers, dix skills
  (neuf invocables et skill-manager référence), un agent, aucun cookbook propre.
  Registres, allowlists, profils, journaux, transformations et droits audités ;
  décisions de conservation/réécriture/retrait justifiées individuellement.
- [Découpage HUB-001 à HUB-020](exist-011-annexes/exist-011-decoupage-hub.md) : vingt suites bornées
  avec fichiers, entrées, résultats, sources futures, scénarios et dépendances.
  Origines fork/communauté/éditeur séparées ; aucune mise à jour communautaire
  de paquet interne ni contenu éditeur, aucune adoption implicite de copie locale.
- Protections BASE-008/009 conservées. Contradictions restantes assignées :
  modes de confiance, clés HTML parasites dans YAML, REFUSE/override/advisory,
  QA désactivable, table/journal, commit/tag, fraîcheur après accord et routine
  passive/scheduled. Rien n’est supprimé par traduction.
- [Vérification](exist-011-annexes/exist-011-verification.md) : simulation filesystem réellement
  exécutée en faux home ; update sur deux fichiers personnalisés refusée,
  octets et journal inchangés. [Résultats](exist-011-annexes/exist-011-simulation-resultats.json)
  et [script](exist-011-annexes/exist-011-simulation.py) conservés. Pas test de prompt ou client.
- [Fixture documentaire de découverte](exist-011-annexes/exist-011-scenarios.json) : skill
  Californie bien structuré supposé, mais hors portée France demandée ;
  sécurité, conception et pertinence documentaire ont des états distincts.
  Relecture des attendus futurs, sans discovery ou QA de modèle exécutées.
- [Contrôles documentaires et empreintes](exist-011-annexes/exist-011-resultats.json) rejouables
  avec le [contrôleur](exist-011-annexes/exist-011-controles.py) ; couverture, dépendances,
  liens/index/format, copies partagées, invariants et travaux antérieurs préservés.
- PILOTE-003 terminé après BASE-011 : préalable satisfait, aucune extension
  sélectionnée ; limites H01 complet et lecteur indépendant consignées.
  Vingt suites `proposee`, première tranche suggérée HUB-001.

Fichiers du lot : présente story, inventaire, découpage, vérification,
contrôleur, rapport général, scénarios JSON, simulation et ses résultats,
vingt propositions `suites/hub-*.md` et index `backlog/README.md`. Modifications
limitées à `backlog/`, sans entrée NOTICE selon CLAUDE.md. Ce lot préserve
le hub, les contenus éditeur et les travaux antérieurs. Des modifications
concurrentes hors lot, notamment métadonnées racine et employment-legal,
sont consignées sans attribution ; pas d’affirmation de workspace entier figé.

**Portée :** cadrage et relecture par le seul agent de maintenance, plus fixture
technique temporaire sur le helper existant. Aucune réécriture de plugin,
source externe ou règle actuelle du produit consultée, licence de candidat réel,
provenance distante, sécurité exhaustive ou fond juridique validés. Pas de
skill/modèle exécuté, installation dans le home réel, recette client/reload,
lecteur indépendant, connexion, message, publication ou déploiement. --approved
utilisé dans la fixture est une attestation de workflow, pas preuve d’accord
humain réel. Les résultats distincts restent aux futures suites sélectionnées.
