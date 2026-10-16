---
id: BNK-003
titre: "Contester des frais bancaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-003 — Contester des frais bancaires

## Objectif et résultat attendu

Un particulier ou un professionnel compare les frais prélevés aux conditions
tarifaires applicables, identifie les écarts et prépare une réclamation.

## Périmètre et fichiers

- `banking-legal/skills/bank-fees-claim/SKILL.md` — le skill (à créer)
- `banking-legal/references/frais.md` — types de frais, plafonds à vérifier selon le client, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Relevés ; conditions tarifaires datées ; convention de compte ; nature du
compte (personnel, professionnel) ; événements déclencheurs (rejet,
dépassement, saisie) ; échanges.

## Sortie attendue

Tableau : frais, date, montant recopié, ligne tarifaire, déclencheur, écart
ou question. Règles propres au particulier et au professionnel distinguées,
selon la source lue ; brouillon ; limites. Aucun plafond affirmé sans texte.

## Travail attendu

Compte professionnel : ne pas appliquer les repères du particulier.
Difficultés globales → DOM-024. Frais liés à une saisie : ici ; la saisie
elle-même → DOM-003.

## Références métier et sources à rechercher

Code monétaire et financier, convention de compte et plafonnement de certains
frais (pistes L312-1-1, L312-1-3) ; règles sur la clientèle fragile ; règles
propres aux comptes professionnels.

## Critères d'acceptation

- [ ] T01 rapproche frais et grille sans plafond non sourcé.
- [ ] T02 traite le compte professionnel avec ses propres repères.

## Vérification

- Cas normal : T01 — Frais de rejet répétés sur le compte d'un particulier.
- Cas limite : T02 — Commission d'intervention sur le compte professionnel d'un artisan.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Négociation tarifaire, changement de banque, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
