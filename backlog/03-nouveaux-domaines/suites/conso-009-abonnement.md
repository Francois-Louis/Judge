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
- [ ] A03 à A06 distinguent consentement, fin du contrat et paiement ; aucun bouton ni blocage ne vaut résiliation présumée.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : A01 — Salle de sport reconduite sans rappel reçu.
- Cas limite : A02 — Forfait mobile avec frais de résiliation.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Abonnements sectoriels, remboursement de prélèvements, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 21, 78–79, 81–92, 150 de la [matrice des besoins](../dom-001-annexes/dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Traiter souscription contestée et résiliation comme branches distinctes : essai devenu payant, réduction liée à une adhésion, reconduction, nouvel engagement allégué, hausse, préavis et frais. Demander preuves de consentement, information préalable, avis de reconduction, parcours de sortie, accusés et factures postérieures. Fiche : qui fournit, qui facture (y compris boutique d’applications), date de fin déclarée ou établie et sommes contestées.

Distinguer facilité de résiliation, effet immédiat, frais et durée ; documenter boutons absents et parcours défaillant sans supposer gratuité. Compte supprimé ne vaut pas fin du contrat ; blocage d’un paiement ne vaut pas disparition de la dette. Les opérations bancaires relèvent de BNK-006 et les remboursements après réclamation de CONSO-019. Service numérique inutilisable : CONSO-010 ; télécoms DOM-022 ou repli CONSO-014 annoncé.

- Cas limite : A03 — Essai gratuit, abonnement caché et consentement non fourni : brouillon de contestation, sans admettre la validité du contrat.
- Cas limite : A04 — Bouton absent puis demande ignorée et nouveau débit : preuves des tentatives, date d’effet réservée et banque séparée.
- Cas limite : A05 — Compte d’application supprimé mais facturation par une boutique : identifier fournisseur et canal, sans promettre la clôture.
- Cas limite : A06 — Hausse et frais de sortie au calcul opaque : demander clause, notification et détail.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-annexes/dom-001-decoupage-consommation.md).
