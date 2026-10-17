---
id: CHP-007
titre: "Documenter des dégâts de gibier et préparer les questions d'indemnisation"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-040, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, CHP-001]
---

# CHP-007 — Documenter des dégâts de gibier et préparer les questions d'indemnisation

## Objectif et périmètre

Une personne dont le jardin ou terrain est endommagé obtient un dossier
factuel réutilisable et les voies à vérifier. Plugin proposé
`hunting-fishing-legal`,
[contrat commun](../dom-040-annexes/dom-040-decoupage-chasse-peche.md).
Le résultat ne décide ni responsabilité ni indemnité.

## Entrées et pièces

Usage du terrain (jardin privé, culture d'exploitation ou mixte), qualité de
propriétaire/occupant/exploitant, lieu, dates de découverte et répétition,
espèce supposée et éléments qui l'étayent, photos existantes datées, constats,
devis/factures et courriers déjà reçus. Distinguer observation personnelle,
témoignage et supposition ; aucune collecte au contact des animaux demandée.

## Sortie attendue

Chronologie, inventaire des dégâts sans expertise ni valorisation nouvelle,
tableau preuve existante/manque, interlocuteur potentiel et fondement à
vérifier ; brouillon de demande d'information sur la voie adaptée. Montants
des devis recopiés comme évaluations proposées, sans quantum indemnisable.
Jardin privé et dégâts de cultures d'un exploitant sont séparés avant toute
orientation. Phrase BASE-013 nommant un avocat ou juriste compétent ; renfort
si acte ou échéance annoncée, sans délai de déclaration supposé.

## Travail et références métier

Créer `skills/game-damage-file/SKILL.md` et `references/degats-gibier.md` ;
réutiliser méthode/qualification locales et actualiser README, version,
inventaire attendu et NOTICE. Rechercher Code de l'environnement pour
mécanismes d'indemnisation, bénéficiaires et exclusions ; Code civil et
jurisprudence utile si voie de responsabilité à explorer. Identifier les
conditions avant de retenir fédération, assureur ou responsable allégué.
Aucune responsabilité automatique du voisin ou de l'association et aucune
indemnisation fédérale présumée pour un jardin.

## Critères d'acceptation

- [ ] C04 distingue jardin privé, espèce alléguée et dégâts établis ; aucun remboursement ni voie acquise annoncé.
- [ ] C15 transmet les cultures d'exploitation à DOM-014, en conservant le dossier factuel et sans second chiffrage.
- [ ] Origine domestique possible → DOM-033 ; garantie → DOM-005 ; responsabilité/réparation et dommage corporel → DOM-035 ; espèces/milieu → DOM-030.
- [ ] Sources/version, phrase BASE-013, lecture des décisions selon BASE-005 et recette client/autonomie du contrat commun vérifiées ; aucun envoi ni collecte risquée.

## Vérification prévue

- C04 : jardin retourné, sangliers supposés d'après traces et devis de
  remise en état → dossier d'indices et demande sur le régime, sans assimiler
  jardin et récoltes agricoles ni désigner un payeur.
- C15 : même terrain avec jardin privé et parcelle de maïs d'un exploitant
  → séparer usages et dégâts ; DOM-014 pour cultures, DOM-005 si garantie
  invoquée, aucune prise en charge déduite du devis.

## Hors périmètre et état

Expertise, calcul d'indemnité, dépôt de déclaration, recours, piégeage,
destruction ou éloignement d'animaux. Proposition non implémentée ;
[portée](../dom-040-annexes/dom-040-verification.md#portée).
