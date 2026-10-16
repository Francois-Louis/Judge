---
id: TPT-001
titre: "Préparer une réclamation pour un vol direct annulé"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# TPT-001 — Préparer une réclamation pour un vol direct annulé

## Objectif et résultat attendu

Un passager obtient un dossier pour un vol direct confirmé annulé par le transporteur, hors forfait. Cette tranche crée le paquet avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/.claude-plugin/plugin.json` — manifeste, version initiale `0.1.0` (à créer)
- `transport-legal/README.md` — tâche livrée et limites (à créer)
- `transport-legal/CLAUDE.md` — modèle minimal, aucun profil requis (à créer)
- `transport-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `transport-legal/NOTICE` — entrée datée (à créer)
- `transport-legal/references/shared/research-citation-method.md` — copie BASE-005 identique (à créer)
- `transport-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `transport-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `transport-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `transport-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `transport-legal/references/qualification-transport.md` — questionnaire commun et frontières (à créer)
- `.claude-plugin/marketplace.json` — entrée après sélection explicite de TPT-001
- `scripts/test-base008-isolation.py` — décompte et version après la même sélection
- `transport-legal/skills/flight-cancellation-claim/SKILL.md` — le skill (à créer)
- `transport-legal/references/annulation-vol-direct.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Réservation, billet, vendeur, transporteurs commercial et effectif ; départ, arrivée et dates ; avis et motif de l’annulation, réception ; solutions et choix déjà acceptés ; dépenses et paiements ; qualité et pouvoir du demandeur.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Résumé ; fiche du trajet et des acteurs ; chronologie ; tableau remboursement, réacheminement, prise en charge et indemnisation ; choix exercés et cumuls à vérifier ; pièces ; brouillon au transporteur identifié ; inconnues et suite.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Établir le champ territorial et temporel avant tout régime. Examiner chaque demande séparément ; ne pas promettre de cumul remboursement/réacheminement. Champ inconnu : fiche factuelle et questions seulement.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Règlement (CE) n° 261/2004 : champ, annulation et demandes ; Code des transports ; jurisprudence CJUE ; DGAC et Your Europe comme information. Modifications et versions à la date des faits à rechercher, sans barème mémorisé.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] Le trajet est un vol direct hors forfait, le transporteur effectif et le champ territorial/temporel sont établis ou explicitement réservés.
- [ ] Remboursement, réacheminement, prise en charge et indemnisation sont séparés, avec choix acceptés et cumuls à vérifier.
- [ ] Une correspondance ou une annulation personnelle sort de cette tranche avant toute conclusion.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Vol direct au départ de France annulé, réservation et frais documentés : demandes distinctes, sans somme due présumée.
- Cas limite : Vol au départ d’un pays tiers avec transporteur effectif inconnu : régime et droits réservés.
- Cas limite : Billet annoncé direct mais comprenant un changement de vol : sortie de tranche vers TPT-002.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Correspondance (TPT-002), retard (TPT-003), bagage (TPT-005), forfait (TPT-006), annulation personnelle, refus d’embarquement, déclassement, dommage corporel, fret et envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
