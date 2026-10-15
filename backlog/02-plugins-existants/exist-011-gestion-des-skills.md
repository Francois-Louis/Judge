---
id: EXIST-011
titre: "Découper l'adaptation du hub et de ses mises à jour"
statut: proposee
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

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `legal-builder-hub`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Simuler une mise à jour d'un skill personnalisé et la découverte d'un skill propre à une juridiction américaine ; l'un doit préserver les modifications, l'autre afficher sa portée.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

