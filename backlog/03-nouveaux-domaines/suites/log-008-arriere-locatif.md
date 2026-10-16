---
id: LOG-008
titre: "Rapprocher un arriéré locatif des paiements documentés"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-008 — Rapprocher un arriéré locatif des paiements documentés

## Objectif et résultat attendu

Le locataire ou petit bailleur comprend un décompte d'impayés et identifie
les écarts à faire expliquer. Bail privé vide de résidence principale,
France métropolitaine ; pas de décision sur le bien-fondé de toute la dette.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/rent-arrears-review/SKILL.md` — tâche (à créer)
- `housing-legal/references/decompte-locatif.md` — rapprochement et provenance (à créer)
- `housing-legal/skills/rent-arrears-review/references/demande-decompte.md` — modèle (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale de LOG-001 ; aucun autre plugin requis.

## Pièces et informations nécessaires

Bail et avenants utiles, décompte daté avec période, quittances et preuves
ciblées de paiement, aides connues et versements documentés, échanges ;
commandement ou jugement éventuel avec signification pour le seul routage.
Masquer opérations bancaires étrangères au litige ; aucun relevé entier requis.

## Sortie attendue

Tableau période/appel/versement/solde annoncé/écart/pièce ; sommes recopiées
et rapprochements reproductibles distingués des postes juridiquement dus ;
questions sur les affectations et justificatifs ; brouillon au bailleur.

## Travail attendu

Ne pas compter deux fois l'aide ou le versement ; affectation incertaine
signalée, jamais décidée pour équilibrer les chiffres. Charges au fond →
LOG-002 ; frais d'acte → ENF-003 ; acte et urgence → ENF-001/005 ; conditions
de délais et clause → LOG-009 ; dette globale → DOM-024. Le mot impayé ne
vaut pas validation de la somme ni orientation automatique vers la saisie.

## Références métier et sources à rechercher

Textes locatifs du régime choisi, Code civil pour preuve du paiement et
imputation, clause du bail, règles propres aux postes contestés ; ANIL/ADIL.
Ouvrir champ, versions et transitions ; frais, prescription et exigibilité
ne sont pas validés par l'arithmétique.

## Critères d'acceptation

- [ ] A01 identifie un paiement absent du relevé sans déclarer toute la dette éteinte.
- [ ] A02 sépare dette du bail et acte reçu ; aucune expulsion imminente déduite du solde.
- [ ] Sans source, rapprochement factuel et questions seulement ; paquet seul et références locales vérifiés selon BASE-006.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si acte, délai ou procédure (BASE-013).

## Vérification

- Cas normal : A01 — Virement documenté absent du décompte et aide non confirmée ; un écart et une inconnue distincts.
- Cas limite : A02 — Décompte joint à un commandement, frais mélangés au loyer ; priorité au routage de l'acte et séparation des postes.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006. Répond aux pièces des points 35–36 de
la [matrice exécution](../dom-003-annexes/dom-003-frictions-utilisateurs.md).

## Hors périmètre

Autres régimes locatifs, révision de loyer au fond, frais d'acte au fond,
échéancier imposé, prescription calculée, reconnaissance de dette et envoi.

## Complément des frictions logement — 16 octobre 2026

Points 18, 38, 50, 125 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

Distinguer dernier loyer, dépôt, charges et travaux contestés ; aucune compensation ou suspension unilatérale. Ventiler chaque période avant reconnaissance de dette et relever si une reconnaissance a déjà été signée, pour examiner séparément son effet. Ne pas fabriquer ni proposer une reconnaissance globale. Commandement : lecture d'acte ENF-001, conditions de délais LOG-009, demande judiciaire LOG-010 ; signaler l'urgence sans reprendre la durée du texte utilisateur.

- [ ] Le scénario complémentaire produit les distinctions, pièces et réserves ci-dessous, dans la borne de la story.

Scénario **attendu, non exécuté** : Reconnaissance globale proposée alors que charges et dépôt sont contestés : produire détail des postes et questions avant engagement, sans signer ni affirmer une interruption de prescription.
Les montants et délais du texte utilisateur ne sont pas validés ; appliquer
les sources locales et la recette de la story avant toute livraison.
