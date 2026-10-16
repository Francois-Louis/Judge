---
id: TPT-003
titre: "Préparer une réclamation pour un retard aérien"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-003 — Préparer une réclamation pour un retard aérien

## Objectif et résultat attendu

Un passager retardé obtient une chronologie et une demande au transporteur avec les conditions de chaque droit à vérifier.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/flight-delay-claim/SKILL.md` — le skill (à créer)
- `transport-legal/references/retard-aerien.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Réservation, contrats et itinéraire complet ; transporteur effectif ; horaires prévus/réels et preuve d’arrivée, fuseaux ; motif annoncé ; prestations proposées, frais et paiements.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Fiche du trajet ; chronologie départ/arrivée avec preuves ; demandes distinctes ; brouillon ; conditions et pièces manquantes.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Vol direct ou correspondance dont le contrat est établi avec le questionnaire commun. Aucun retard à l’arrivée déduit du seul départ. Motif annoncé et effet juridique restent distincts ; contrat non qualifié : conclusion dépendante réservée.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Règlement (CE) n° 261/2004 et jurisprudence CJUE sur retard, arrivée et circonstances invoquées ; Code des transports ; DGAC, Your Europe ; aucun seuil repris de mémoire.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Le retard à l’arrivée est documenté ou réservé, jamais déduit du seul départ.
- [ ] La chronologie traite fuseaux et destination pertinente ; motif allégué et effet juridique restent distincts.
- [ ] Une correspondance non qualifiée réserve les demandes qui en dépendent.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Vol direct arrivé tardivement avec heures documentées : chronologie et demandes séparées.
- Cas limite : Capture du départ seulement : demander la preuve d’arrivée sans calculer une indemnité.
- Cas limite : Correspondance manquée sur contrats distincts : ne pas traiter le voyage comme une réservation unique.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Annulation (TPT-001/TPT-002), forfait (TPT-006), refus d’embarquement, bagages, dommage corporel et fret.

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
