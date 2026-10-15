---
id: DOM-005
titre: "Cadrer un plugin d'assurance"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-005 — Cadrer un plugin d'assurance

## Objectif

Structurer la revue de couverture, les sinistres et les refus de garantie dans un plugin dédié.

Nom de plugin proposé : `insurance-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Qualités des parties, organisme, contrat, conditions générales/particulières, dates et type de risque.
- Tâches candidates : revue de garantie, préparation de déclaration, analyse de refus, contestation de chiffrage, résiliation et protection juridique.
- Ne pas confondre absence de garantie, exclusion, déchéance et nullité ; isoler les régimes auto, construction, santé et emprunteur.
- Séparer le litige de garantie de la responsabilité de l'intervenant : travaux en DOM-015, garage en DOM-023, soins en DOM-007 et dommage civil en DOM-035. Un dossier peut avoir plusieurs volets sans dupliquer la même analyse.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des assurances ou régimes de mutualité/prévoyance selon le contrat, textes spéciaux, ABE Infoservice et ACPR.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill d'analyse d'un refus de garantie à partir du contrat et du courrier de refus.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un refus fondé sur une exclusion citée dans un courrier.
- Un sinistre avec conditions particulières manquantes.
- Un désaccord sur le montant d'une expertise.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

