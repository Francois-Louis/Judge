---
id: DOM-008
titre: "Cadrer un plugin transports et voyages"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-008 — Cadrer un plugin transports et voyages

## Objectif

Séparer les réclamations selon le mode, le trajet et le contrat de transport.

Nom de plugin proposé : `transport-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Mode, trajet, dates, transporteur effectif, vendeur, réservation unique ou contrats distincts, passager ou marchandise.
- Tâches candidates : retard/annulation aérienne, trajet ferroviaire, bagage, forfait touristique et réclamation transporteur.
- Distinguer remboursement, réacheminement, prise en charge et indemnisation ; ne pas appliquer un barème aérien au train ni le régime passager au fret.
- L'achat et la réparation d'un véhicule sont cadrés dans [DOM-023](dom-023-vehicules-garages.md), les prestations postales dans [DOM-022](dom-022-telecoms-poste.md). Réserver ici les obligations propres au trajet, au voyage ou au transport.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code des transports, Code du tourisme, règlements UE et conventions dans leur champ, Your Europe et autorités françaises compétentes.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de réclamation pour un mode et un type d'incident, à choisir au cadrage.

## Critères d'acceptation

- [x] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [x] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [x] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [x] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [x] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Un vol annulé avec correspondance.
- Un retard ferroviaire.
- Un bagage perdu lors d'un voyage à forfait.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Bilan d’exécution — 16 octobre 2026

- [Découpage](dom-008-annexes/dom-008-decoupage-transports.md) : nom
  `transport-legal` conservé (`judge-fr-eu-transport-legal`), qualification
  commune des modes, trajets, dates, acteurs, contrats et qualités ; quatre
  demandes distinctes, sans barème commun aux modes ni régime passager au fret.
- Dix propositions TPT-001 à TPT-010 sous `suites/`, hiérarchisées : vol direct
  annulé en première tranche ; correspondances, retard aérien, ferroviaire,
  bagage aérien et forfait ensuite ; relance, autocar et bateau au rang 3 ;
  qualification du fret professionnel sans réclamation au fond au rang 4.
- Chaque story précise skill, références à ouvrir, pièces, sortie, fichiers,
  dépendances et scénarios futurs, non exécutés. TPT-001 crée le paquet avec
  son seul skill ; aucun profil ni autre plugin requis, aucun besoin identifié
  d’agent, connecteur ou hook. Aucune implémentation lancée dans DOM-008.
- Frontières explicites avec véhicules/garages (DOM-023), poste (DOM-022),
  consommation, assurance, douanes, banque, commercial, responsabilité,
  contentieux, données personnelles et travail.
- [Vérification documentaire](dom-008-annexes/dom-008-verification.md) :
  parcours sur vol annulé avec correspondance, retard ferroviaire et bagage
  perdu en forfait ; douze cas limites, sans résoudre les consultations.
- Ligne transports de la [matrice BASE-003](../00-fondations/base-003-annexes/base-003-dossier-architecture.md)
  précisée ; famille TPT ajoutée au générateur et index régénéré.
- [Contrôles statiques](dom-008-annexes/dom-008-resultats.json) produits par
  [le contrôleur du lot](dom-008-annexes/dom-008-controles.py).

Fichiers du lot : présente story, découpage, vérification, contrôleur, relevé
JSON, dix propositions `suites/tpt-*.md`, ligne BASE-003, `backlog/etat.py` et
`backlog/ETAT.md`. Lot limité à `backlog/`, sans entrée NOTICE.

**Portée :** cadrage documentaire relu par l’agent de maintenance sur pièces
fictives et contrôles statiques. Aucune source juridique externe ouverte :
les textes nommés sont des pistes à vérifier, pas du droit actuel validé.
Aucun plugin créé, skill exécuté, paquet installé ou lecteur indépendant.
Le préalable PILOTE-003 est satisfait après BASE-011 ; aucune tranche n’est
sélectionnée par ce cadrage.

## Complément des frictions utilisateurs — 16 octobre 2026

- [Source reçue](sources/transports-frictions-2026-10-16.txt) conservée à
  l’octet près ; [matrice des 128 points](dom-008-annexes/dom-008-frictions-utilisateurs.md),
  sections calendrier/méthode et lacunes explicites.
- Dix suites initiales précisées et douze propositions TPT-011 à TPT-022 :
  billet ferroviaire, PV, titre/service urbain, frais aériens, refus
  d’embarquement, taxi/VTC, covoiturage, libre-service, assistance PMR,
  bagage autocar, bien maritime et taxes de vol non effectué.
- Frontières et relais actualisés : consommation, protection sociale,
  responsabilité corporelle, pénal, discrimination et données personnelles.
- [Vérification du complément](dom-008-annexes/dom-008-frictions-verification.md)
  et [contrôles reproductibles](dom-008-annexes/dom-008-frictions-controles.py),
  avec [relevé daté](dom-008-annexes/dom-008-frictions-resultats.json).

Fichiers du complément : présente story, source, matrice, découpage, rapport,
contrôleur et relevé, 22 suites TPT, cadrages DOM-002/012/029/035 et EXIST-003,
frontière DOM-001, index ETAT. Lot limité à `backlog/`, sans entrée NOTICE.

**Portée du complément :** intégration et relecture documentaires du rédacteur,
contrôles structurels ; aucune recherche juridique, validation des chiffres
et délais reçus, implémentation/exécution de skill, installation client,
relecture indépendante ni démarche externe. Toutes les suites restent
`proposee` ; aucune tranche n’est sélectionnée. Les contrôles et relevés du
cadrage initial à dix suites sont historiques et ne sont pas réécrits.

## Complément des frictions douanes — 17 octobre 2026

Points 5–6 et 13–22, 35–38, 57–58 : V01 demande de découper frais privés de dédouanement/stockage/retour et réclamation fret selon mode, trajet et contrat. TPT-010 reste une qualification de l'incident, sans recours au fond élargi implicitement. Recueillir contrat, rôles, demandes/pièces datées, déclaration éventuelle, tarif, chronologie du dommage et frais. Sortie future : tableau frais/causalité et brouillon ciblé. Cas : documents transmis mais magasinage continué ; transport retour après refus ; casse attribuée à la douane sans preuve. DOU-009 garde acte officiel, DOM-022 prestation postale, DOM-001 livraison de vente ; V02/DOM-005 police d'assurance distincte des plafonds de responsabilité du transporteur. Aucun barème passager appliqué au fret.

Exigences de la [matrice des 75 points](dom-009-annexes/dom-009-frictions-utilisateurs.md), sans sélection de tranche ni capacité annoncée comme livrée. [Portée et contrôles](dom-009-annexes/dom-009-frictions-verification.md).
