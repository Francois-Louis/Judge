---
id: INS-006
titre: "Résilier un contrat d'assurance ou lire une résiliation de l'assureur"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-006 — Résilier un contrat d'assurance ou lire une résiliation de l'assureur

## Objectif et résultat attendu

Un assuré qui veut résilier connaît les voies à vérifier et prépare sa
demande ; un assuré résilié par son assureur comprend le motif et la suite.

## Périmètre et fichiers

- `insurance-legal/skills/policy-termination/SKILL.md` — le skill (à créer)
- `insurance-legal/references/resiliation.md` — motifs, voies, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Contrat ; date de souscription et d'échéance ; avis d'échéance reçu ;
changement de situation ; courrier de résiliation de l'assureur ; primes
impayées.

## Sortie attendue

Voies de résiliation à vérifier selon le contrat et la situation ; brouillon
de demande ; lecture d'une résiliation reçue ; obligation d'assurance à
vérifier (auto, habitation du locataire) ; limites. Aucune date calculée sans
texte lu.

## Travail attendu

Assurance emprunteur → INS-008. Résiliation pour non-paiement : prime due et
suites, sans conseil d'arrêter de payer.

## Références métier et sources à rechercher

Code des assurances (pistes L113-3, L113-12, L113-15-1, L113-15-2).

## Critères d'acceptation

- [ ] T01 prépare la demande sans date non sourcée.
- [ ] T02 lit la résiliation pour non-paiement et signale l'obligation d'assurance éventuelle.

## Vérification

- Cas normal : T01 — Assurance habitation souscrite il y a deux ans, déménagement.
- Cas limite : T02 — Lettre de résiliation de l'assurance auto après impayés.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Souscription d'un nouveau contrat, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
