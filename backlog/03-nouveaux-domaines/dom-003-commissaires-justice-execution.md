---
id: DOM-003
titre: "Cadrer un plugin d'exécution et de recouvrement"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-003 — Cadrer un plugin d'exécution et de recouvrement

## Objectif

Isoler les actes des commissaires de justice, le recouvrement et l'exécution forcée du contentieux général.

Nom de plugin proposé : `enforcement-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Qualité de l'émetteur, titre de l'acte, mode et date de signification, créance et éventuel titre exécutoire.
- Tâches candidates : lecture d'acte, contrôle de décompte, recouvrement amiable, orientation face à une saisie ou une expulsion.
- Séparer saisies, mesures conservatoires et recouvrement ; articuler logement, dette bancaire et compétence du juge selon le régime vérifié.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des procédures civiles d'exécution, Code de procédure civile, Code civil, textes spéciaux et informations officielles de la profession.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture d'acte et de repérage des informations urgentes, sans promesse de suspension.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une relance d'une société de recouvrement.
- Un acte signifié dont la date est contestée.
- Une mesure de saisie avec ventilation des frais absente.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

