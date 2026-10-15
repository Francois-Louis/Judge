---
id: DOM-013
titre: "Cadrer un plugin famille et patrimoine du couple"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-013 — Cadrer un plugin famille et patrimoine du couple

## Objectif

Aider les personnes à comprendre les conséquences d'une union, d'une séparation et des décisions relatives aux enfants, avec les pièces et démarches correspondantes.

Nom de plugin proposé : `family-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Statut familial, régime, enfants, qualité des demandeurs, résidence, actes existants et éventuelle urgence.
- Tâches candidates : lecture d'une décision, préparation de pièces de séparation, contribution, résidence et organisation familiale, liquidation du patrimoine du couple à découper séparément.
- Distinguer décisions concernant les adultes et intérêt de l'enfant ; identifier représentation, signature et pouvoirs selon les actes.
- Les [successions et donations](dom-016-successions-donations.md), la [protection juridique des majeurs](dom-026-protection-majeurs.md), les [obsèques](dom-031-deces-obseques.md) et la [protection face aux violences intrafamiliales](dom-038-violences-intrafamiliales.md) ont des cadrages distincts. Définir leurs échanges sans les absorber ici.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code civil, Code de procédure civile, textes spéciaux et instruments transfrontaliers selon la matière ; sources officielles Justice et Service Public.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Lire une décision d'organisation familiale pour en extraire les obligations, dates et points à éclaircir, dans un cas borné.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une séparation avec décision existante.
- Un désaccord sur la répartition des frais concernant un enfant.
- Un désaccord patrimonial à la fin d'un PACS ou d'un mariage.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

