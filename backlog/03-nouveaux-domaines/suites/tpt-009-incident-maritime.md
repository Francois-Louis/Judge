---
id: TPT-009
titre: "Préparer une réclamation pour un trajet maritime ou fluvial perturbé"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-009 — Préparer une réclamation pour un trajet maritime ou fluvial perturbé

## Objectif et résultat attendu

Un passager de bateau obtient une réclamation pour annulation ou retard après qualification du service.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/waterborne-disruption-claim/SKILL.md` — le skill (à créer)
- `transport-legal/references/incident-maritime.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Billet, transporteur effectif et vendeur ; ports, dates, service et navire ; transport ou croisière, forfait éventuel ; incident et motif, météo alléguée ; solutions, dépenses et réponses.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Qualification transport/croisière/forfait ; chronologie ; demandes séparées ; brouillon ; preuve du motif et questions de champ réservées.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Vérifier champ et exclusions, puis transport/croisière sans étendre toutes les dispositions à celle-ci. La météo alléguée ne suffit pas à conclure sur toutes les demandes.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Règlement (UE) n° 1177/2010 ; Code des transports et mesures nationales selon service ; conditions du transporteur ; Your Europe et autorités compétentes. Règles de croisière et exclusions à lire séparément.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Transport, croisière, forfait et exclusions de champ sont distingués.
- [ ] La météo annoncée reste un motif allégué dont les effets sont vérifiés par demande.
- [ ] Les dispositions du ferry ne sont pas appliquées automatiquement à une croisière.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Traversée ferry annulée avec billet et réponse : demandes selon le champ établi.
- Cas limite : Croisière avec escale supprimée : qualifier le contrat sans automatisme du régime ferry.
- Cas limite : Tempête invoquée : conserver le motif comme déclaration et vérifier ses effets par demande.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Bagages, dommage corporel, fret, avarie du véhicule embarqué, simple excursion et forfait non qualifié ; forfait établi (TPT-006), assurance (DOM-005).

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
