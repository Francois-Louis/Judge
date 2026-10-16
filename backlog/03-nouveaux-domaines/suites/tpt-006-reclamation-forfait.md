---
id: TPT-006
titre: "Préparer une réclamation relative à un forfait touristique"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-006 — Préparer une réclamation relative à un forfait touristique

## Objectif et résultat attendu

Un voyageur obtient une qualification de la vente et un brouillon pour une prestation du forfait non exécutée ou modifiée.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/package-travel-claim/SKILL.md` — le skill (à créer)
- `transport-legal/references/reclamation-forfait.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Contrat, confirmation, facture et information précontractuelle ; organisateur et détaillant ; lieux et dates ; services achetés ensemble ou séparément ; incident, signalement et réponse ; solutions, dépenses et paiements reçus.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Qualification forfait/prestations liées/contrats distincts établie ou réservée ; engagements et incidents comparés ; acteurs et demandes distincts ; brouillon ; articulation avec transport et assurance ; pièces et inconnues.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Une réclamation sur une prestation d’un forfait, après qualification obligatoire. Ne pas appeler tout achat vol+hôtel un forfait. Distinguer organisateur, détaillant et transporteur, puis remède, remboursement, réduction de prix et réparation ; tenir compte des sommes déjà reçues.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Code du tourisme, vente de voyages et forfaits, parties législative et réglementaire à identifier ; directive (UE) 2015/2302 et transposition ; DGCCRF, Atout France, Your Europe. Aucune directive appliquée automatiquement entre particuliers.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Forfait, prestation liée et contrats isolés sont qualifiés à partir des pièces.
- [ ] Organisateur, détaillant et transporteur ont des rôles distincts ; chaque demande correspond à un engagement identifié.
- [ ] Le volet bagage et les sommes déjà reçues restent visibles sans lettre universelle ni double réparation présumée.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Forfait identifié, prestation hôtelière non fournie : comparer contrat, signalement et réponse.
- Cas limite : Vol et hôtel achetés sur deux sites sans contrat commun : ne pas conclure à un forfait.
- Cas limite : Bagage perdu pendant le séjour : TPT-005 pour le transporteur, TPT-006 pour les engagements propres au forfait.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Prestations liées ou isolées : orientation ; annulation personnelle avant départ, insolvabilité et rapatriement à découper ; assurance (DOM-005), hébergement isolé (DOM-001) hors location résidentielle.

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
