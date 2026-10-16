---
id: TPT-007
titre: "Préparer une relance après une réclamation de transport"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-008, PILOTE-003, BASE-005, BASE-006, BASE-008, TPT-001]
---

# TPT-007 — Préparer une relance après une réclamation de transport

## Objectif et résultat attendu

Un passager ayant réclamé obtient une chronologie, une relance ciblée et les voies ultérieures à vérifier pour son mode.

## Périmètre et fichiers

Plugin principal : `transport-legal` (`judge-fr-eu-transport-legal`).
Les chemins « à créer » désignent des livrables futurs.

- `transport-legal/references/qualification-transport.md` — relue, créée par TPT-001
- `transport-legal/README.md` — ajouter la tâche réellement livrée
- `transport-legal/NOTICE` — entrée datée
- `transport-legal/skills/transport-claim-follow-up/SKILL.md` — le skill (à créer)
- `transport-legal/references/relance-transporteur.md` — méthode métier, modèle de sortie et sources lues (à créer)
- `NOTICE` — entrée racine

Chaque lot met à jour la version du manifeste et les métadonnées synchronisées
selon CLAUDE.md ; la première version reste celle de TPT-001. Les références
communes ne sont pas dupliquées ni réécrites par chaque tâche.

## Pièces et informations nécessaires

Mode et contrat qualifiés ; réclamation et preuve de réception ; objet, pièces, réponse ou silence ; paiements, accord proposé, mandat d’une plateforme éventuelle ; dates et échéance invoquée.

Demander uniquement les pièces utiles, avec données non nécessaires masquées ;
distinguer pièce fournie, fait déclaré et information inconnue.

## Sortie attendue

Objet restant en litige ; chronologie ; brouillon de relance ou demande de motifs ; médiation, autorité de contrôle et juge distingués ; recevabilité et calendrier réservés faute de sources.

La sortie explique l’action à préparer, son destinataire et ce qui reste
conditionnel, dans des mots compréhensibles sans formation juridique.

## Travail attendu

Relance documentaire ; pour un mode dont la tâche n’est pas livrée, reprendre les faits et demandes sans réexaminer le fond. Vérifier médiateur compétent et conditions sur source lue ; distinguer signalement et indemnisation.

Charger la méthode BASE-005 locale et `qualification-transport.md` selon le
[découpage](../dom-008-annexes/dom-008-decoupage-transports.md).
Documenter sources réellement lues, version à la date des faits, rattachement
et inconnues. Distinguer demande, somme documentée et somme juridiquement due.
Aucun envoi, dépôt, accès à un compte de réservation ou paiement.

## Références métier et sources à rechercher

Sources du mode traité ; Code de la consommation si médiation applicable ; textes de compétence et procédures officielles du médiateur et de l’autorité identifiés ; conditions contractuelles.

Pistes non ouvertes par DOM-008 : existence, version, champ, modifications,
exceptions et jurisprudence doivent être vérifiés lors de ce lot. Aucun délai,
seuil, montant ou conversion n’est repris sans source effectivement lue.

## Critères d'acceptation

- [ ] La chronologie distingue envoi, réception prouvée, réponse et silence.
- [ ] Le fond d’un mode non livré reste réservé ; une relance factuelle reste possible.
- [ ] Médiateur, autorité et juge sont distingués, sans recevabilité ni effet indemnitaire d’un signalement présumés.
- [ ] Sans source accessible, la fiche factuelle reste utile et toute conclusion juridique dépendante est réservée.
- [ ] Le paquet détaché fonctionne seul, sans profil préalable ni connecteur obligatoire ; recette BASE-006 consignée par couche.
- [ ] La sortie se termine par la phrase BASE-013 avec un interlocuteur adapté ; renfort en tête si une échéance ou une difficulté immédiate est signalée.

## Vérification

- Cas normal : Réclamation aérienne et réponse contestant un motif : relance sur les points restants.
- Cas limite : Courrier simple sans preuve de réception : ne pas affirmer un délai expiré ou une médiation recevable.
- Cas limite : Mode maritime alors que seule la tâche aérienne est livrée : relance factuelle sans régime maritime improvisé.
- Sans source : qualification et pièces utiles, aucun droit, délai ou montant dû confirmé.
- Transfrontalier : tester pays tiers, acteur étranger et dates ; loi applicable, champ du régime et juge ne sont pas déduits de la langue du billet.
- Héritage étranger : joindre un modèle américain et vérifier qu’aucune règle ou somme n’est importée dans la réclamation.

Scénarios **attendus, non exécutés**. Lors de l’implémentation, exécuter sur
pièces fictives, conserver ressources lues, sorties et erreurs ; appliquer
BASE-006, puis faire relire par une personne sans formation juridique. La
[relecture DOM-008](../dom-008-annexes/dom-008-verification.md) porte seulement
sur le routage documentaire.

## Hors périmètre

Saisine ou dépôt, requête, exécution, transaction, cession de créance, fond d’un mode non livré et prescription non vérifiée ; réclamation forfait (TPT-006).

## État de la proposition — 16 octobre 2026

Issue de DOM-008, sans implémentation. Dépend de PILOTE-003 : préalable
satisfait après BASE-011 ; aucune tranche sélectionnée par ce cadrage.
Contrat commun : [découpage](../dom-008-annexes/dom-008-decoupage-transports.md).

## Complément des frictions transports — 16 octobre 2026

Points 64–65, 75, 95, 118–120, 122, 127–128 de la [matrice transports](../dom-008-annexes/dom-008-frictions-utilisateurs.md).

Conserver formulaire complet, annexes, accusé et motifs. Distinguer relance, signalement, médiation et action individuelle ; vérifier la réforme procédurale aérienne alléguée en 2026 (champ, entrée en vigueur, transitions, exceptions et acte requis). Ne pas proposer CTX-026 par défaut. Transaction vers CTX-039 ; PV vers TPT-012, avec calendrier propre sans suspension présumée.

- [ ] Le résultat conserve ces distinctions et les pièces correspondantes ; chiffres et délais du texte vérifiés sur sources à l’implémentation.

Scénario **attendu, non exécuté** : Dossier aérien fermé automatiquement puis médiateur non compétent : produire chronologie et vérifications de procédure, sans saisine simplifiée ou effet interruptif garanti.
