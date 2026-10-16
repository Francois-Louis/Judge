---
id: TPT-002
titre: "Qualifier une annulation aérienne avec correspondance"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-002 — Qualifier une annulation aérienne avec correspondance

## Objectif et résultat attendu

Un passager obtient une carte des segments et contrats, puis une réclamation bornée si le rattachement est établi.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/connecting-flight-cancellation/SKILL.md` — le skill (à créer)
- `transport-legal/references/annulation-correspondance.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Tous les billets et confirmations ; références de réservation ; vendeur et transporteur effectif par segment ; lieux, dates, horaires prévus et réels à destination finale ; segment annulé ; solutions acceptées et frais.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Carte des contrats et segments ; réservation unique établie ou inconnue ; chronologie ; demandes par acteur ; brouillon si qualifié, sinon questions au vendeur et conclusions réservées.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Ne pas déduire une réservation unique du même panier ou site. Distinguer contrats séparés et correspondance autonome ; examiner départ, destination, lieu de perturbation et transporteurs sans extension automatique à tous les segments.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Règlement (CE) n° 261/2004 ; jurisprudence CJUE sur correspondances, réservation unique et destination via CURIA/EUR-Lex ; Code des transports ; contrats et conditions à la date d’achat.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Chaque segment, contrat et transporteur effectif apparaît dans la carte du trajet.
- [ ] La réservation unique est établie par les pièces ou reste inconnue ; même panier ne suffit pas.
- [ ] Les demandes sont adressées par acteur sans couverture globale présumée des contrats séparés.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Deux segments documentés sous une réservation unique, premier annulé : cartographie avant demande.
- Cas limite : Deux billets achetés séparément : ne pas promettre la couverture de l’ensemble.
- Cas limite : Même plateforme sans pièce établissant les contrats : question ciblée et conclusion réservée.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Retard sans annulation (TPT-003), forfait (TPT-006), garantie commerciale de correspondance, faute du vendeur et billet multimodal non qualifiés.

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
