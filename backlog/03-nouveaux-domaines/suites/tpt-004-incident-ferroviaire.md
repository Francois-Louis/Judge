---
id: TPT-004
titre: "Préparer une réclamation pour un incident ferroviaire"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-004 — Préparer une réclamation pour un incident ferroviaire

## Objectif et résultat attendu

Un voyageur en train obtient une réclamation après retard ou annulation adaptée au service et au contrat ferroviaires.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/rail-disruption-claim/SKILL.md` — le skill (à créer)
- `transport-legal/references/incident-ferroviaire.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Billets et éventuel billet direct ; entreprise ferroviaire et vendeur ; service national, régional ou international ; gares, dates, horaires ; information reçue, solutions, frais et garantie commerciale invoquée.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Qualification du service et des billets ; chronologie ; remboursement, poursuite/réacheminement, assistance et indemnisation séparés ; garantie commerciale identifiée ; pièces et brouillon.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Vérifier champ, service, exemptions et régime temporel. Billets séparés, billet direct et achat groupé ne sont pas équivalents. Distinguer droits légaux et engagements commerciaux ; ne pas appliquer un barème aérien.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Règlement (UE) 2021/782 et régime antérieur selon dates ; Code des transports et exemptions nationales ; conditions du transporteur ; Your Europe et autorités françaises compétentes à identifier.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Service, champ, exemptions et régime temporel ferroviaires sont vérifiés ou réservés.
- [ ] Billet direct, achat groupé et contrats distincts sont différenciés avant de traiter la correspondance.
- [ ] Garantie commerciale et droits légaux restent distincts, sans barème aérien.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Train international annulé, billet complet : qualification du service puis demandes distinctes.
- Cas limite : Service régional avec garantie commerciale : vérifier champ et exemptions sans emprunt aérien.
- Cas limite : Deux billets achetés ensemble sans contrat établi : réserver le traitement de la correspondance.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Fret, bagage ferroviaire, dommage corporel, forfait et contrat multimodal non qualifié ; erreur de réservation du vendeur à qualifier séparément.

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
