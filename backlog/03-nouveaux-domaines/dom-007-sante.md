---
id: DOM-007
titre: "Cadrer un plugin santé et droits des patients"
statut: terminee
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

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle (scénarios rédigés, non exécutés).
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une demande de dossier médical par le patient.
- Une demande d'un proche dont le pouvoir reste à vérifier.
- Une réclamation cherchant à la fois sanction et indemnisation.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.


## Complément des frictions données personnelles — 16 octobre 2026

Points 45–47 de la [matrice données personnelles](../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md) : découper demande d'accès au dossier médical et contestation d'un accès tardif selon le régime sectoriel. Qualifier demandeur/pouvoir, nature et ancienneté des informations, réception et exceptions avant de rechercher les délais ; aucun calendrier RGPD automatique. PRV-001/025/034 gardent les demandes relatives au traitement et aux accès injustifiés allégués ; PRV-026 qualifie une transmission de données de santé. Demander au DPO les vérifications utiles sans promettre toutes les identités des agents. Scénario attendu : copie du dossier et soupçon de consultation, avec deux objets et calendriers distincts. Ces tâches sectorielles restent à découper ; portée et contrôles dans la matrice.

## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-007-annexes/dom-007-decoupage-sante.md) : nom `health-legal`
  conservé (`judge-fr-eu-health-legal`) ; installation seule, sans profil,
  agent, hook, connecteur ni accès à un espace numérique de santé ;
  garde-fous (ni diagnostic ni avis médical, urgence médicale d'abord,
  qualité du demandeur d'abord, quatre objets non fusionnés, statut public
  ou privé établi, aucun délai ni seuil inventé, collecte minimale) ;
  qualification commune (demandeur, structure, objectif, informations
  visées, dates, pièces, urgence) ; frontières avec protection sociale,
  assurance, responsabilité, protection des majeurs, handicap, données
  personnelles, pénal, violences, contentieux, travail, fonction publique,
  séjour, successions, consommation, publicité et éducation.
- 12 propositions SAN-001 à SAN-012 sous `suites/`, en quatre rangs.
  Première tranche : SAN-001, demande d'accès au dossier médical par le
  patient majeur pour lui-même, qui crée le paquet avec ce seul skill.
  Représentant ou proche, ayant droit, relance, réclamation et orientation
  d'un dommage au rang 2 ; ordre, ARS, information, soins sans consentement
  et frais au rang 3 ; directives anticipées au rang 4.
- Établissement et commission des usagers, ARS, ordre, assurance,
  commissions et ONIAM et juge répartis entre SAN-005 à SAN-008 et DOM-005 ;
  soins sans consentement (SAN-010) et remboursement par une caisse
  (DOM-012) séparés.
- Complément des frictions données personnelles : points 45–47 rattachés
  dans le découpage, sans modifier la matrice EXIST-003 ; scénario « copie
  du dossier et soupçon de consultation » relu.
- Quatre points ouverts sans story : médecine du travail et dossiers d'un
  assureur ou d'un médecin-conseil, structures médico-sociales (partage
  avec DOM-025), refus de soins discriminatoire, espace numérique de santé.
- [Vérification documentaire](dom-007-annexes/dom-007-verification.md) :
  les trois scénarios de la story, le scénario des frictions et onze cas
  limites, sans délai, montant ni droit conclu.
- Ligne `health-legal` de la [matrice BASE-003](../00-fondations/base-003-annexes/base-003-dossier-architecture.md)
  précisée ; famille SAN ajoutée au générateur de l'index et index régénéré.
- [Contrôles statiques](dom-007-annexes/dom-007-resultats.json), produits par
  [le contrôleur du lot](dom-007-annexes/dom-007-controles.py), sur le modèle de DOM-005.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 12 propositions `suites/san-*.md`, ligne de BASE-003,
`backlog/etat.py` et `backlog/ETAT.md`. Le lot reste sous `backlog/`, sans
entrée NOTICE.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles cités sont des pistes. Aucun plugin créé, skill exécuté, paquet
installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est satisfait
après BASE-011 ; aucune tranche n'est sélectionnée.

## Complément des frictions santé — 16 octobre 2026

Le [texte utilisateur](sources/sante-frictions-2026-10-16.txt) est conservé à
l'octet près. La [matrice](dom-007-annexes/dom-007-frictions-utilisateurs.md)
relie les 155 points et les sections 12–15 à leurs tâches, résultats et
limites. Elle complète le cadrage terminé, sans rouvrir ni réécrire son
bilan initial et ses relevés historiques.

- SAN-001 à SAN-012 reçoivent des scénarios et exigences ciblés.
- Sept nouvelles propositions : SAN-013 accès/continuité, SAN-014 anomalies
  de facturation, SAN-015 devis dentaire/optique/auditif, SAN-016 pharmacie,
  SAN-017 soins en médico-social, SAN-018 préparation du dossier CCI,
  SAN-019 observations d'expertise amiable/CCI.
- DOM-012 reçoit les tâches candidates caisse/IJ/CRA/CMRA/transport ;
  INS-004/009 le contrat et les refus de complémentaire ; DOM-025
  l'accompagnement, DOM-029 les discriminations, DOM-035 le préjudice,
  EXIST-003 les accès/données et le besoin Mon espace santé. Le découpage
  travail reçoit les besoins attestation de salaire et subrogation.
- Les points ouverts initiaux médico-social et refus de soins sont précisés
  par ces frontières ; médecine du travail/assureur/médecin-conseil et
  contrôles numériques propres à Mon espace santé restent à découper.

Les **19 propositions SAN restent `proposee`**, sans plugin créé ni tranche
sélectionnée. Première tranche SAN-001 conservée ; les sources, montants et
délais du texte ne sont pas validés. [Vérification et portée](dom-007-annexes/dom-007-frictions-verification.md)
et [contrôles du complément](dom-007-annexes/dom-007-frictions-controles.py).
Les fichiers produits restent sous `backlog/`, sans entrée NOTICE.
