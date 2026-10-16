---
id: EXIST-006
titre: "Découper l'adaptation des workflows de contentieux"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-006 — Découper l'adaptation des workflows de contentieux

## Objectif

Reconstruire les tâches de contentieux selon les procédures concernées, au lieu de traduire les noms des actes américains.

## Points de départ

- [litigation-legal/skills/subpoena-triage/SKILL.md](../../litigation-legal/skills/subpoena-triage/SKILL.md)
- [litigation-legal/skills/deposition-prep/SKILL.md](../../litigation-legal/skills/deposition-prep/SKILL.md)
- [litigation-legal/skills/privilege-log-review/SKILL.md](../../litigation-legal/skills/privilege-log-review/SKILL.md)
- [litigation-legal/skills/legal-hold/SKILL.md](../../litigation-legal/skills/legal-hold/SKILL.md)
- [litigation-legal/skills/demand-draft/SKILL.md](../../litigation-legal/skills/demand-draft/SKILL.md)
- [litigation-legal/skills/claim-chart/references/element-templates.md](../../litigation-legal/skills/claim-chart/references/element-templates.md)

## Travail attendu

- Classer les tâches réutilisables (chronologie, dossier, suivi) et celles nécessitant une refonte juridique.
- Décider du devenir et du nom des tâches subpoena, deposition et privilege log : absence d'équivalent automatique à documenter, tâche française à définir avant renommage.
- Séparer mise en demeure, conservation/production des preuves, rédaction d'écritures et suivi de procédure ; préciser les frontières avec pénal, administratif et exécution.
- Identifier les mentions de work product, discovery et without prejudice qui supposent une analyse de droit applicable.
- Sources à prévoir et à vérifier lors des futures implémentations : Codes de procédure selon la matière, Code civil, règles professionnelles et textes de compétence ; vérifier acte, notification et représentation.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `litigation-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios (relecture documentaire sur cas fictifs par le rédacteur).
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Utiliser une mise en demeure reçue, une demande de production de pièce et une convocation française ; aucun de ces documents ne doit déclencher mécaniquement une procédure américaine.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire exhaustif](exist-006-inventaire-contentieux.md) : 38 fichiers,
  dont 19 skills, références, modèles inline, registre, agent et dépendances
  de sortie ; six fichiers du cookbook associés et décisions individuelles.
- [Découpage CTX-001 à CTX-024](exist-006-decoupage-contentieux.md) : fichiers,
  entrées, résultats, sources à rechercher, exclusions et scénarios. Mise en
  demeure, conservation/communication des preuves, écritures et suivi sont
  séparés ; pénal, administratif, exécution et secteurs ont des relais précis.
- Subpoena, deposition et privilege log : aucune équivalence automatique ;
  CTX-005/010/009 définissent d'abord la tâche française et son intitulé futur,
  sans renommer les commandes dans ce lot. Work product, discovery et without
  prejudice sont localisés et traités comme points de recherche, sans effets
  juridiques déduits d'une traduction ou d'un en-tête.
- [Relecture du cadrage](exist-006-verification.md) sur mise en demeure reçue,
  demande de production de pièces et convocation française fictives : aucune
  procédure US n'est prescrite par les suites ; pas de délai calculé.
- [Contrôles statiques et empreintes](exist-006-resultats.json), exécutables
  avec le [contrôleur documentaire](exist-006-controles.py). Le commentaire
  HTML du modèle `_log.yaml` est interprété comme une clé YAML parasite ;
  sa correction bornée est assignée à CTX-014 et non réalisée ici.
- PILOTE-003 est terminé après BASE-011 : préalable satisfait, sans sélection
  d'extension. Limites H01 complet et lecteur indépendant consignées. Les 24
  suites restent `proposee` ; première tranche suggérée CTX-001, non lancée.

Fichiers du lot : présente story, inventaire, découpage, vérification,
contrôleur, résultats JSON, 24 propositions `suites/ctx-*.md` et index
`backlog/README.md`. Modifications limitées à `backlog/`, sans entrée NOTICE
selon CLAUDE.md ; empreintes des plugins et des travaux EXIST précédents
préservées. Des différences simultanées sur DOM-001 et l'architecture sont
consignées séparément, sans les attribuer à EXIST-006 ou les modifier.

**Portée :** cadrage et relecture par le seul agent de maintenance sur fixtures
fictives reproduites dans la vérification, contrôles statiques. Aucune source
juridique externe consultée, règle ou échéance réelle validée, adaptation ou
exécution de skill, installation, recette client, lecteur indépendant,
connexion, envoi, renommage, publication ou déploiement. Les textes, versions,
compétences, actes, notifications, représentation et régimes de confidentialité
restent à rechercher lors des futures implémentations. Plugin, cookbook et
contenus éditeur inchangés ; aucune capacité France/UE nouvelle livrée ici.

