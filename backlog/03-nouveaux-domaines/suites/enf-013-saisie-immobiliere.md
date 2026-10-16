---
id: ENF-013
titre: "S'orienter face à une saisie immobilière"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-013 — S'orienter face à une saisie immobilière

## Objectif et résultat attendu

Un propriétaire qui reçoit un commandement valant saisie immobilière ou un
acte de la procédure comprend l'étape, l'urgence et la nécessité de consulter
rapidement un avocat. Aucune analyse au-delà de cette orientation.
Ajout du 16 octobre 2026 ([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `enforcement-legal/skills/real-estate-seizure-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/saisie-immobiliere.md` — étapes, représentation, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

`qualification-acte.md` (ENF-001) est relu, pas réécrit.

## Pièces et informations nécessaires

Commandement ou acte reçu ; titre visé ; bien concerné ; occupants ; autres
dettes ; procédure de surendettement éventuelle.

## Sortie attendue

Étape identifiée ; bloc d'urgence ; représentation par avocat à vérifier ;
interlocuteurs (avocat, point d'accès au droit, aide juridictionnelle) ;
questions ; limites. Aucune date d'audience ou de vente calculée.

## Travail attendu

Situation globale → DOM-024. Prêt immobilier au fond → DOM-004. Ne pas
conseiller de vendre ou de transférer le bien pour échapper à la saisie.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, saisie immobilière (pistes L311-1
et suivants, R311-1 et suivants) ; aide juridictionnelle.

## Critères d'acceptation

- [ ] I01 identifie l'étape et la nécessité de l'avocat sans date calculée.
- [ ] I02 oriente la situation globale vers DOM-024.

## Vérification

- Cas normal : I01 — Commandement valant saisie immobilière pour un prêt impayé.
- Cas limite : I02 — Même acte, dossier de surendettement déjà déposé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Procédure d'adjudication, défense au fond, vente amiable, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-003-decoupage-execution.md).
