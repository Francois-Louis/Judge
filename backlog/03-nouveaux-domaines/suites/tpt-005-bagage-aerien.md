---
id: TPT-005
titre: "Préparer une réclamation pour un bagage aérien"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-005 — Préparer une réclamation pour un bagage aérien

## Objectif et résultat attendu

Un voyageur obtient un dossier pour un bagage retardé, perdu ou endommagé, distinct de l’incident du vol et de l’assurance.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/air-baggage-claim/SKILL.md` — le skill (à créer)
- `transport-legal/references/bagage-aerien.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Itinéraire, billet et transporteurs ; bagage cabine ou enregistré, étiquette ; constat et référence de signalement ; dates de remise et découverte ; échanges ; contenu utile, preuves d’achat et frais nécessaires ; forfait éventuel.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Chronologie et inventaire justifié ; statut déclaré du bagage et qualification réservée ; signalement/réclamation distingués ; brouillon ; postes documentés sans montant dû présumé ; volet forfait séparé.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Ne pas transformer automatiquement un retard en perte acquise, ni présenter un constat à l’aéroport comme une réclamation suffisante sans vérification. En forfait, coordonner TPT-006 sans fusionner acteurs, recours ou réparations.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Convention de Montréal ou de Varsovie selon champ ; règlement (CE) n° 2027/97 modifié ; Code des transports ; DGAC. Vérifier exigences, réclamations, limites et toute unité ou conversion dans les versions utiles.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Cabine/enregistré, statut du bagage et dates utiles sont qualifiés sans perte automatiquement acquise.
- [ ] Signalement et réclamation écrite sont distingués ; aucune suffisance du constat ni conversion présumée.
- [ ] En forfait, chaque acteur garde ses demandes et les sommes reçues sont recensées sans double réparation présumée.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Bagage enregistré non remis avec étiquette et frais documentés : dossier et postes séparés.
- Cas limite : Valise abîmée avec constat mais sans réclamation écrite : demander dates et vérifier exigences.
- Cas limite : Bagage absent pendant un forfait : TPT-005 pour le transporteur et TPT-006 pour le vendeur/organisateur, sans double réparation présumée.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Bagages des autres modes à découper ; marchandise professionnelle (TPT-010), assurance (DOM-005), dommage corporel, évaluation sans pièces et double paiement.

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
