---
id: DOM-007
titre: "Cadrer un plugin santé et droits des patients"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-007 — Cadrer un plugin santé et droits des patients

## Objectif

Créer des workflows juridiques de santé distincts des soins médicaux et de la protection sociale.

Nom de plugin proposé : `health-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Qualité du demandeur, établissement public/privé, professionnel, dates et objectif : accès, réclamation, indemnisation ou mesure de soins.
- Tâches candidates : accès au dossier médical, information/consentement, réclamation sur une prise en charge, orientation d'un dommage.
- Distinguer établissement/CDU, ARS, ordre, assurance, CCI/ONIAM et juge ; traiter séparément soins sans consentement et remboursement par une caisse.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code de la santé publique, textes de responsabilité et de procédure selon le recours, ministère de la Santé, ONIAM et CNIL pour les données.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de préparation d'une demande d'accès au dossier médical, limité à un demandeur et un régime précis.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une demande de dossier médical par le patient.
- Une demande d'un proche dont le pouvoir reste à vérifier.
- Une réclamation cherchant à la fois sanction et indemnisation.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.


## Complément des frictions données personnelles — 16 octobre 2026

Points 45–47 de la [matrice données personnelles](../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md) : découper demande d'accès au dossier médical et contestation d'un accès tardif selon le régime sectoriel. Qualifier demandeur/pouvoir, nature et ancienneté des informations, réception et exceptions avant de rechercher les délais ; aucun calendrier RGPD automatique. PRV-001/025/034 gardent les demandes relatives au traitement et aux accès injustifiés allégués ; PRV-026 qualifie une transmission de données de santé. Demander au DPO les vérifications utiles sans promettre toutes les identités des agents. Scénario attendu : copie du dossier et soupçon de consultation, avec deux objets et calendriers distincts. Ces tâches sectorielles restent à découper ; portée et contrôles dans la matrice.
