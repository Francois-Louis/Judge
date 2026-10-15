---
id: EXIST-003
titre: "Découper l'adaptation de la protection des données"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-003 — Découper l'adaptation de la protection des données

## Objectif

Faire du droit applicable en France, du RGPD et de la loi Informatique et Libertés le cadre des tâches de protection des données.

## Points de départ

- [privacy-legal/skills/dsar-response/SKILL.md](../../privacy-legal/skills/dsar-response/SKILL.md)
- [privacy-legal/skills/dpa-review/SKILL.md](../../privacy-legal/skills/dpa-review/SKILL.md)
- [privacy-legal/skills/pia-generation/SKILL.md](../../privacy-legal/skills/pia-generation/SKILL.md)
- [privacy-legal/skills/use-case-triage/SKILL.md](../../privacy-legal/skills/use-case-triage/SKILL.md)
- [privacy-legal/references/currency-watch.md](../../privacy-legal/references/currency-watch.md)

## Travail attendu

- Séparer exercice des droits, sous-traitance, AIPD, qualification d'un traitement et suivi de conformité.
- Rechercher les hypothèses américaines présentes dans les profils, exemples et grilles, même lorsque le workflow est déjà compatible avec le RGPD.
- Identifier les compléments français, les rôles, les données sensibles, transferts et secteurs particuliers à couvrir par des références ciblées.
- Sources à prévoir et à vérifier lors des futures implémentations : EUR-Lex, CNIL, loi Informatique et Libertés, CEPD et jurisprudence pertinente ; vérifier chaque délai selon son événement déclencheur.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `privacy-legal`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer des scénarios de demande d'accès, contrat de sous-traitance et traitement de données de santé ; un opt-out américain ne doit pas être appliqué par défaut.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

