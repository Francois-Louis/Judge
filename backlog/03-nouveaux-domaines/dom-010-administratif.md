---
id: DOM-010
titre: "Cadrer un plugin de droit administratif"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-010 — Cadrer un plugin de droit administratif

## Objectif

Prévoir les demandes à l'administration et les recours dans un domaine distinct des contentieux civils.

Nom de plugin proposé : `administrative-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Administration, objet, demande ou décision, notification, délai et éventuel recours préalable.
- Tâches candidates : lecture de décision, demande d'accès aux documents, recours administratif et préparation d'un dossier.
- Identifier les régimes spéciaux et les frontières avec fiscalité et protection sociale ; leur présence n'autorise pas un délai générique.
- Les [actes d'urbanisme](dom-019-urbanisme-foncier.md), le [séjour/nationalité/asile](dom-028-sejour-nationalite-asile.md), les [décisions d'emploi public](dom-037-fonction-publique.md) et la [scolarité](dom-027-education-formation.md) sont orientés vers leurs cadrages métier. L'existence d'une administration ne suffit pas à choisir ce plugin général.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

CRPA, Code de justice administrative et textes sectoriels ; Service Public, Conseil d'État et CADA selon l'objet.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture d'une décision et de ses voies de recours, avec régime borné.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une décision notifiée avec voies de recours.
- Une demande restée sans réponse.
- Un refus d'accès à un document administratif.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

