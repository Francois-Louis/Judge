---
id: CONSO-009
titre: "Résilier un abonnement de consommation hors secteur spécialisé"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-009 — Résilier un abonnement de consommation hors secteur spécialisé

## Objectif et résultat attendu

Une personne liée par un abonnement (salle de sport, box mensuelle, service
en ligne hors télécoms) comprend ses échéances et obtient un brouillon de
résiliation avec les preuves à conserver.

## Périmètre et fichiers

- `consumer-legal/skills/subscription-exit/SKILL.md` — le skill (à créer)
- `consumer-legal/references/abonnements.md` — reconduction, résiliation, sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Contrat ou conditions ; date de souscription ; durée et reconduction ;
informations reçues avant l'échéance ; moyen de résiliation proposé.

## Sortie attendue

Fiche : échéances déclarées et prouvées, moyen de résiliation, brouillon,
preuves ; limites. Aucune échéance calculée sans texte lu.

## Travail attendu

Orienter télécoms (DOM-022), énergie (DOM-021), assurance (DOM-005), banque
(DOM-004). Prélèvements à arrêter : tâche bancaire distincte.

## Références métier et sources à rechercher

Code de la consommation, reconduction tacite et résiliation par voie
électronique, version à la date des faits.

## Critères d'acceptation

- [ ] A01 produit fiche et brouillon sans échéance non sourcée.
- [ ] A02 oriente vers DOM-022 sans traiter le contrat.

## Vérification

- Cas normal : A01 — Salle de sport reconduite sans rappel reçu.
- Cas limite : A02 — Forfait mobile avec frais de résiliation.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Abonnements sectoriels, remboursement de prélèvements, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
