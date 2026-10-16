---
id: EXIST-005
titre: "Découper l'adaptation de la gouvernance IA"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-005 — Découper l'adaptation de la gouvernance IA

## Objectif

Recentrer les workflows IA sur les usages, rôles et obligations France/UE avec un calendrier vérifié à l'exécution.

## Points de départ

- [ai-governance-legal/skills/use-case-triage/SKILL.md](../../ai-governance-legal/skills/use-case-triage/SKILL.md)
- [ai-governance-legal/skills/aia-generation/SKILL.md](../../ai-governance-legal/skills/aia-generation/SKILL.md)
- [ai-governance-legal/skills/vendor-ai-review/SKILL.md](../../ai-governance-legal/skills/vendor-ai-review/SKILL.md)
- [ai-governance-legal/skills/ai-inventory/SKILL.md](../../ai-governance-legal/skills/ai-inventory/SKILL.md)
- [ai-governance-legal/references/currency-watch.md](../../ai-governance-legal/references/currency-watch.md)

## Travail attendu

- Séparer inventaire, qualification d'usage, évaluation, contrats fournisseur et politique interne.
- Définir les faits déterminant rôle, catégorie, territoire et calendrier ; ne pas confondre règlement adopté et obligation déjà applicable.
- Identifier les interactions avec RGPD, droit du travail, produits et règles sectorielles ; prévoir un renvoi ciblé et autonome plutôt qu'une duplication.
- Sources à prévoir et à vérifier lors des futures implémentations : Règlement IA et actes associés sur EUR-Lex, autorités françaises compétentes, CNIL et sources officielles de la Commission ; statut des guides à distinguer.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `ai-governance-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios (relecture documentaire sur cas fictifs par le rédacteur).
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer les questions de cadrage pour un outil RH, un assistant interne et un service destiné au public, sans attribuer de catégorie définitive sans les faits.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire complet](exist-005-inventaire-ia.md) : 23 fichiers dont 10 skills,
  modèles inline, références communes, sources d'actualité, profils, registres,
  sorties et relais ; décision individuelle motivée. Aucun agent ou cookbook
  propre livré dans ce plugin.
- [Découpage IA-001 à IA-020](exist-005-decoupage-ia.md) : propositions avec
  fichiers, entrées, résultat, recherches, exclusions et scénarios. Inventaire,
  qualification, obligations par rôle, évaluation interne/FRIA, contrats et
  politique ont des résultats distincts. Première tranche proposée : fiche
  factuelle d'un assistant interne, sans classement ni feu vert.
- [Relecture documentaire](exist-005-verification.md) : outil RH, assistant
  interne et service destiné au public ; faits déterminant rôle, catégories,
  territoires et calendrier, renvois ciblés et autonomes. Aucune catégorie
  définitive attribuée à ces dossiers fictifs.
- [Contrôles statiques et empreintes](exist-005-resultats.json) : couverture,
  dépendances, liens, cibles futures, copies communes, index et périmètre.
  Plugin et contenus éditeur inchangés, travaux EXIST-001/002/003/004 préservés.
- PILOTE-003 est terminé après BASE-011 : préalable satisfait, sans sélection
  d'une extension ; limites H01 complet et lecteur indépendant consignées.
  Les 20 suites restent `proposee`.

Fichiers du lot : présente story, inventaire, découpage, vérification,
résultats JSON, script de contrôles, 20 propositions `suites/ia-*.md` et index
`backlog/README.md`. Lot limité à `backlog/`, sans entrée NOTICE selon CLAUDE.md.

**Portée :** cadrage et relecture par le seul agent de maintenance sur pièces
fictives, contrôles statiques. Aucune source juridique externe consultée,
obligation/échéance vérifiée, adaptation ou exécution de skill, installation,
recette client, lecteur indépendant, connexion, envoi ou publication. Le
calendrier actuel et le statut des réformes/guides restent à rechercher lors
des futures implémentations, sans présenter ce cadrage comme adaptation livrée.

