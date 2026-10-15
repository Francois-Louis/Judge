---
id: DOM-002
titre: "Cadrer un plugin police et procédure pénale"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-002 — Cadrer un plugin police et procédure pénale

## Objectif

Créer des tâches distinctes pour l'identification d'une mesure policière, les droits, les plaintes et les contestations pénales.

Nom de plugin proposé : `criminal-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Statut de la personne, mesure exacte, autorité, dates/heures, âge et urgence ; ne pas confondre contrôle d'identité, audition libre et garde à vue.
- Tâches candidates : lecture d'une convocation, orientation pendant une mesure, préparation factuelle de plainte, lecture d'un avis d'amende.
- Séparer droits immédiats, qualification d'infraction et voies de recours ; éviter tout équivalent automatique de Miranda ou subpoena.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Codes pénal, de procédure pénale, de la sécurité intérieure et de la route selon les faits ; Justice, textes officiels et jurisprudence pertinente.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture et qualification d'une convocation, avant les régimes urgents plus complexes.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une convocation sans qualification claire de l'audition.
- Une mesure en cours avec heure de début connue.
- Un avis d'amende déjà payé ou reçu tardivement.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

