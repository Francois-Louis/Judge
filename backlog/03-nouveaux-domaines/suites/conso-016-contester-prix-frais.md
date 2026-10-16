---
id: CONSO-016
titre: "Contester un prix, un supplément ou une promotion appliquée"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-016 — Contester un prix, un supplément ou une promotion appliquée

## Objectif et résultat attendu

Une personne qui conteste un prix ou un supplément obtient un rapprochement lisible entre l’offre, le panier accepté et la facture, puis un brouillon de demande au vendeur.

## Périmètre et fichiers

Plugin principal : `consumer-legal` (`judge-fr-eu-consumer-legal`), installé seul.
Les chemins « à créer » désignent des livrables futurs.

- `consumer-legal/skills/price-fee-claim/SKILL.md` — le skill (à créer)
- `consumer-legal/references/prix-frais.md` — grille, sources lues et modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche effectivement livrée
- `consumer-legal/.claude-plugin/plugin.json` — version du lot

`qualification-achat.md` (CONSO-001) est relu, pas réécrit. Aucun profil,
agent, hook, connecteur ni stockage durable ajouté.

## Pièces et informations nécessaires

Affichage en rayon ou en ligne, capture de promotion et conditions ; panier, confirmation et facture ; option ou assurance ajoutée ; preuve du consentement ; tarif antérieur allégué ; CGV acceptées et version ultérieure invoquée.

Sans pièce, commencer sur le récit marqué comme déclaré ; ne jamais inventer
une donnée absente ni demander de code bancaire ou de mot de passe.

## Sortie attendue

Tableau prix annoncé / prix accepté / prix facturé, sommes documentées et écarts ; caractère légal ou contractuel de chaque demande à vérifier ; brouillon de correction ou restitution ; limites sur le prix de référence et l’erreur manifeste.

## Travail attendu

Examiner faux rabais, urgence artificielle, frais tardifs, options précochées, assurance colis, frais de paiement, panier modifié et CGV postérieures. Distinguer affichage ambigu et erreur de prix manifeste, sans promettre une vente forcée. Les calculs reposent sur les montants fournis ; aucun barème ni majoration non sourcés. Offre réservée aux membres ou aux porteurs d’une carte : vérifier la condition et le consentement à l’abonnement (CONSO-009). Crédit et paiement fractionné relèvent de DOM-004 ; assurance souscrite distinctement de DOM-005. Le signalement de la pratique relève de CONSO-013.

Appliquer le contrat commun du [découpage](../dom-001-annexes/dom-001-decoupage-consommation.md),
la méthode locale BASE-005 et le protocole d’orientation USAGE-001.

## Références métier et sources à rechercher

Code de la consommation : information sur le prix, annonces de réduction, suppléments, consentement, pratiques trompeuses et clauses abusives ; Code monétaire et financier pour les frais de paiement, sans traiter le litige bancaire ; Code civil pour erreur et accord contractuel.

Pistes non vérifiées ici : ouvrir et dater les sources à la date des faits.
Une page inaccessible ou un conflit entre guide et texte reste explicite.

## Critères d'acceptation
- [ ] F01 rapproche offre, panier et facture, distingue consentement prouvé et contesté, puis produit le brouillon.
- [ ] F02 réserve erreur manifeste et prix de référence absent, sans imposer la vente ni inventer un historique.
- [ ] Droit légal, promesse contractuelle et affirmation d’un interlocuteur sont distingués.
- [ ] Aucun délai, montant légal ou effet de démarche n’est affirmé sans source applicable lue.
- [ ] Le paquet détaché reste autonome ; seule la tâche livrée est annoncée, sans envoi.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : F01 — Option colis précochée et frais de traitement ajoutés à la dernière page : rapprocher les pièces et préparer la contestation.
- Cas limite : F02 — Prix manifestement dérisoire et historique des promotions absent : réserver la demande de livraison et ne pas inventer le prix de référence.
- Sans source accessible : produire les pièces et questions utiles, avec le point juridique réservé.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Revue de campagne marketing, décision de fraude, crédit, remboursement bancaire, envoi.

## Origine et état — 16 octobre 2026

Issue des [155 frictions utilisateur](../dom-001-annexes/dom-001-frictions-utilisateurs.md),
sans implémentation ni sélection. Préalable PILOTE-003 satisfait après BASE-011.
