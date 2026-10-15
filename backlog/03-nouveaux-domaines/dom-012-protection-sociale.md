---
id: DOM-012
titre: "Cadrer un plugin de sécurité sociale et prestations"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-012 — Cadrer un plugin de sécurité sociale et prestations

## Objectif

Isoler les droits et recours contre les organismes sociaux des décisions de l'employeur.

Nom de plugin proposé : `social-security-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Organisme, prestation/cotisation, période, décision, motif, ressources déclarées et notification.
- Tâches candidates : lecture d'une décision, contestation d'indu, préparation d'un recours préalable et dossier de prestation.
- Séparer CAF, assurance maladie, France Travail et cotisations ; identifier compétences et procédures propres, sans inventer un recours commun.
- Les [retraites](dom-036-retraites.md) ont un cadrage dédié. Articuler les prestations et décisions liées au [handicap/autonomie](dom-025-handicap-autonomie.md) avec ce plugin, en désignant pour chaque demande un domaine principal.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code de la sécurité sociale, Code de l'action sociale et des familles et autres textes selon l'organisme ; sources officielles des caisses et jurisprudence.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture d'une notification d'indu pour un organisme et une prestation choisis.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une notification d'indu.
- Un refus de prise en charge.
- Une décision portant sur un droit à prestation ou un calcul.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

