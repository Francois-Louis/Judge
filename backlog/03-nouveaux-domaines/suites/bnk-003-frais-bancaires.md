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

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 1–15, 24, 54, 70, 75–77, 90 et 96 de la [matrice](../dom-004-frictions-utilisateurs.md).

Recueillir aussi notifications de frais et de modification tarifaire, ancien et nouveau tarifs, preuve du support et de réception, récapitulatif annuel ; pour la fragilité, critères retenus, période de reconnaissance, offre proposée ou souscrite et catégories facturées. Aucun justificatif de santé ou identifiant complet nécessaire.

La sortie ventile frais d'incident, commission, courrier, tenue de compte, package, service facultatif, agios, retrait/change et frais de saisie. Pour chaque plafond à vérifier : statut du client, catégories incluses, période, règle, base et montant recopié. Un forfait de rejet n'est pas additionné arbitrairement aux éléments qu'il inclut.

- [ ] T03 — Même prélèvement représenté : rapprocher références et montants, relever les doublons possibles et comparer frais et somme rejetée avec le texte applicable.
- [ ] T04 — Offre spécifique ou fragilité alléguée : demander l'examen d'éligibilité et distinguer protections légales, réglementaires, engagements professionnels et tarif contractuel ; ne pas étendre un plafond à tous les frais.
- [ ] T05 — Hausse peu visible ou frais sans préavis : comparer documents, support durable et dates ; demander récapitulatif annuel manquant et détail des services d'un package.
- [ ] T06 — Retrait en devises ou virement instantané : isoler taux, marge, frais du distributeur et tarification du virement classique comparable ; vérifier pays, prestataire et calendrier d'application.
- [ ] T07 — Agios contestés : demander taux, assiette, jours, minima et décompte ; aucune conclusion sur le taux d'usure sans catégorie, période et source lue, aucun calcul financier général.

Scénarios **attendus, non exécutés** : deux rejets d'une opération ; offre spécifique avec plusieurs catégories de frais ; tarif envoyé dans la messagerie sans preuve de réception ; frais de change ventilés ; facture d'un compte professionnel. Sources à rechercher : plafonds propres à chaque frais, information préalable, clientèle fragile, comptes réglementés et inactifs, change et virements instantanés. Assurance facultative → INS-006 ; clôture → BNK-008 ; frais successoraux → DOM-016. Le détail des services est expliqué sans négociation ni recommandation commerciale.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
