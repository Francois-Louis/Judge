---
id: EXIST-002
titre: "Découper l'adaptation du droit des sociétés et des opérations"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-002 — Découper l'adaptation du droit des sociétés et des opérations

## Objectif

Adapter les tâches de sociétés et d'opérations à la forme sociale et aux actes français, sans reproduire les procédures de Delaware.

## Points de départ

- [corporate-legal/skills/written-consent/SKILL.md](../../corporate-legal/skills/written-consent/SKILL.md)
- [corporate-legal/skills/board-minutes/SKILL.md](../../corporate-legal/skills/board-minutes/SKILL.md)
- [corporate-legal/skills/entity-compliance/SKILL.md](../../corporate-legal/skills/entity-compliance/SKILL.md)
- [corporate-legal/skills/tabular-review/SKILL.md](../../corporate-legal/skills/tabular-review/SKILL.md)
- [corporate-legal/skills/integration-management/SKILL.md](../../corporate-legal/skills/integration-management/SKILL.md)

## Travail attendu

- Inventorier les décisions sociales, procès-verbaux, formalités, diligences et suivi d'opération ; les découper en stories distinctes.
- Qualifier forme sociale, statuts, pactes, pouvoirs, organe compétent et modalités de décision avant tout modèle de consentement écrit.
- Revoir les références et colonnes de due diligence ; conserver la traçabilité documentaire utile et isoler les formalités propres à chaque juridiction.
- Sources à prévoir et à vérifier lors des futures implémentations : Code civil, Code de commerce, textes d'application et formalités françaises à vérifier ; les statuts font partie des pièces nécessaires.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `corporate-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Comparer les tâches attendues pour une SAS et une SARL à partir de statuts fictifs, puis un dossier d'acquisition comportant une filiale étrangère.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire complet](exist-002-annexes/exist-002-inventaire-societes.md) : 30 fichiers dont
  13 skills et un agent, profils, schémas inline, références de grille et
  dépendances suivies vers les sept fichiers du cookbook diligence-grid.
  Décisions et justifications individuelles, noms techniques conservés.
- [Découpage SOC-001 à SOC-022](exist-002-annexes/exist-002-decoupage-societes.md) : 22 stories
  d'implémentation proposées, chacune avec fichiers, entrées, résultat borné,
  sources à rechercher, exclusions et scénarios. Qualification SAS/SARL avant
  projet, puis décisions, PV, formalités, diligence et suivi séparés.
- [Vérification documentaire](exist-002-annexes/exist-002-verification.md) : comparaison SAS/SARL
  sur extraits de statuts fictifs, puis acquisition de titres avec filiale
  allemande. Les clauses, préférences et règles à rechercher sont distinguées ;
  aucun acte juridique n'est déclaré validé par cette relecture.
- [Contrôles et empreintes](exist-002-annexes/exist-002-resultats.json) : couverture, liens,
  identifiants/frontmatter/dépendances, copies communes et périmètre.
  Plugin, cookbook et contenu éditeur inchangés.
- PILOTE-003 est terminé après BASE-011 ; le préalable de bilan est satisfait,
  sans sélectionner de suite. Les 22 SOC restent `proposee` ; H01 complet et
  lecture indépendante du pilote restent des limites, pas une extension autorisée.

Fichiers du lot : présente story, inventaire, découpage, vérification,
résultats JSON, 22 propositions `suites/soc-*.md` et index `backlog/README.md`.
Tout reste sous `backlog/` ; pas d'entrée NOTICE nécessaire selon CLAUDE.md.

**Portée :** cadrage et relecture sur pièces fictives par l'agent de maintenance,
contrôles statiques et arithmétique illustrative ; aucune source juridique
externe consultée, aucun skill adapté ou exécuté, aucune recette de client,
participant réel, connexion, diffusion ou déploiement. Les sources et scénarios
métier seront vérifiés lors des implémentations choisies.

## Complément de besoins — formalités, 16 octobre 2026

La [matrice des 100 frictions](exist-002-annexes/exist-002-frictions-utilisateurs.md) ajoute SOC-023 à SOC-026, quatre propositions d'implémentation bornées (dossier bloqué, modification, dépôt de comptes et questions de fermeture), ainsi que SOC-027, **cadrage** des entreprises en difficulté. Le découpage compte désormais 27 SOC, toutes proposées. Les formes unipersonnelles et les frontières EI/fiscalité/contrats sont explicitement prises en compte.

Le bilan initial et ses empreintes ci-dessus portent sur les 22 propositions historiques. Cette intégration ne les revalide pas, ne clôture aucun nouveau cadrage et ne sélectionne aucune tranche. Portée et contrôles : matrice et [vérification de l'intégration](exist-002-annexes/exist-002-frictions-verification.md).
