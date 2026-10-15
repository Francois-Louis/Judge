---
id: EXIST-010
titre: "Découper l'adaptation des méthodes et examens juridiques"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-010 — Découper l'adaptation des méthodes et examens juridiques

## Objectif

Adapter les tâches pédagogiques aux cursus et exercices français demandés.

## Points de départ

- [law-student/skills/irac-practice/SKILL.md](../../law-student/skills/irac-practice/SKILL.md)
- [law-student/skills/case-brief/SKILL.md](../../law-student/skills/case-brief/SKILL.md)
- [law-student/skills/bar-prep-questions/SKILL.md](../../law-student/skills/bar-prep-questions/SKILL.md)
- [law-student/skills/outline-builder/SKILL.md](../../law-student/skills/outline-builder/SKILL.md)
- [law-student/skills/exam-forecast/SKILL.md](../../law-student/skills/exam-forecast/SKILL.md)
- [law-student/CLAUDE.md](../../law-student/CLAUDE.md)

## Travail attendu

- Distinguer cas pratique, fiche/commentaire d'arrêt, dissertation, note de synthèse et préparation au CRFPA selon l'exercice réel.
- Définir l'évolution des noms IRAC et bar prep sans supposer une équivalence avec un examen américain ; prévoir la compatibilité des commandes seulement si utile.
- Conserver l'accompagnement pédagogique et les règles d'intégrité ; adapter critères et exercices à la consigne de l'établissement.
- Séparer méthode, plan de révision et actualisation du droit ; ne pas promettre une prédiction fiable des sujets d'examen.
- Sources à prévoir et à vérifier lors des futures implémentations : Consignes de cours et d'examen, décisions et textes français/UE ; sources officielles actuelles pour les épreuves et calendriers.

## Critères d'acceptation

- [ ] Un inventaire couvre tous les skills et dépendances de contenu de `law-student`, pas seulement les points d'entrée ci-dessus.
- [ ] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [ ] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [ ] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Comparer les consignes d'un cas pratique et d'un commentaire d'arrêt avec un extrait de décision française ; les attendus doivent différer.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

