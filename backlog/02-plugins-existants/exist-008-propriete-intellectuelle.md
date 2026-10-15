---
id: EXIST-008
titre: "Découper l'adaptation de la propriété intellectuelle"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-008 — Découper l'adaptation de la propriété intellectuelle

## Objectif

Revoir les tâches PI selon les titres, territoires, auteurs et procédures réellement concernés.

## Points de départ

- [ip-legal/skills/clearance/SKILL.md](../../ip-legal/skills/clearance/SKILL.md)
- [ip-legal/skills/fto-triage/SKILL.md](../../ip-legal/skills/fto-triage/SKILL.md)
- [ip-legal/skills/invention-intake/SKILL.md](../../ip-legal/skills/invention-intake/SKILL.md)
- [ip-legal/skills/cease-desist/SKILL.md](../../ip-legal/skills/cease-desist/SKILL.md)
- [ip-legal/skills/takedown/SKILL.md](../../ip-legal/skills/takedown/SKILL.md)
- [ip-legal/skills/oss-review/SKILL.md](../../ip-legal/skills/oss-review/SKILL.md)

## Travail attendu

- Séparer marques, brevets, droit d'auteur, licences, retrait de contenu et portefeuille ; ne pas présenter une recherche partielle comme une liberté d'exploitation complète.
- Rechercher les hypothèses USPTO, DMCA et fair use ; définir leur traitement seulement lorsqu'un rattachement étranger le justifie.
- Identifier les références INPI, EUIPO, OEB et juridictions pertinentes selon le titre et le territoire, sans tout rendre obligatoire dans chaque tâche.
- Distinguer les contrats de cession, créations de salariés et invention de salarié, avec leurs sources propres.
- Sources à prévoir et à vérifier lors des futures implémentations : Code de la propriété intellectuelle, titres et registres pertinents, EUR-Lex et jurisprudence applicable ; contrats et licences à lire.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `ip-legal`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer un nom de marque en France, une invention de salarié et un retrait de contenu ; chaque cas doit avoir un périmètre de recherche et un résultat attendus différents.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

