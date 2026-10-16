---
id: LOG-006
titre: "Lire un congé reçu du bailleur pour une location meublée"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-006 — Lire un congé reçu du bailleur pour une location meublée

## Objectif et résultat attendu

Un locataire comprend le motif, les dates figurant au congé et les points
à vérifier avant une réponse. Bail meublé privé ordinaire, résidence
principale en France métropolitaine ; mobilité et étudiant exclus au fond.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/furnished-landlord-notice-review/SKILL.md` — tâche (à créer)
- `housing-legal/references/conge-bailleur-meuble.md` — motif, notification, protection et sources (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale de LOG-001 ; aucun autre plugin requis.

## Pièces et informations nécessaires

Bail et avenants, inventaire si le régime est discuté, congé complet et
enveloppe/preuve de réception ou signification, motif, dates du bail et
échanges. Informations personnelles de protection seulement si nécessaires,
par catégories utiles et sans avis fiscal complet par défaut.

## Sortie attendue

Fiche régime/motif/dates documentées ou déclarées ; points de forme, fond
et protection à vérifier ; pièces manquantes ; questions ou brouillon de
demande d'explication au bailleur ; conseil et limites. Aucune date de départ
validée depuis la seule date portée au courrier.

## Travail attendu

Distinguer congé, relance, commandement et jugement. Acte signifié : question
sur l'acte vers ENF-001 ; fond du congé ici. Ne pas appliquer le congé d'un
bail vide ni le droit de l'achat immobilier parce que le motif est la vente.
Régime étudiant/mobilité ou localisation hors borne : orientation. Aucun
congé déclaré valable ou nul sans textes et faits suffisants.

## Références métier et sources à rechercher

Loi du 6 juillet 1989, régime meublé choisi, congé, motifs, notification et
protections ; Code civil et règles de notification pertinentes ; ANIL/ADIL.
Ouvrir versions, champ, exceptions et transitions avant tout calendrier.

## Critères d'acceptation

- [ ] M01 demande la preuve de réception et distingue date du courrier et fait de notification.
- [ ] M02 qualifie le bail étudiant/mobilité hors borne ; M03 distingue congé et expulsion.
- [ ] Sans source : dates recopiées et questions, aucun délai déduit ; paquet seul et références locales vérifiés selon BASE-006.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête pour le congé reçu, son urgence à vérifier et le conseil (BASE-013).

## Vérification

- Cas normal : M01 — Congé pour reprise d'un meublé, preuve de réception absente ; lecture et demande de pièce sans date d'effet calculée.
- Cas limite : M02 — Contrat étudiant joint au même courrier ; réserver le régime ordinaire et orienter.
- Cas limite : M03 — Locataire croyant devoir partir immédiatement ; distinguer fin du bail alléguée et acte d'expulsion, sans promettre maintien.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Vide, étudiant, mobilité, social/conventionné, saisonnier, résidence secondaire,
contestation judiciaire, expulsion, calcul d'une date sans source et envoi.
