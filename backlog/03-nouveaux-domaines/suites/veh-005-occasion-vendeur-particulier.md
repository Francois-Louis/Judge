---
id: VEH-005
titre: "Documenter une panne après l'achat d'un véhicule à un particulier"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-004]
---

# VEH-005 — Documenter une panne après l'achat d'un véhicule à un particulier

## Objectif et résultat attendu

Un acheteur dont le véhicule acheté à un particulier présente un défaut
comprend que les garanties de la consommation ne s'appliquent pas en
principe, quels fondements civils examiner, quelles pièces de la vente
comptent, et obtient un brouillon de demande au vendeur.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs. Story soumise à l'arbitrage du [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md) ;
si la vente entre particuliers d'un véhicule revient à `consumer-legal`, elle
devient une suite de CONSO-011.

- `vehicle-legal/skills/used-vehicle-private-defect/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/vente-entre-particuliers-vehicule.md` — fondements civils, pièces de cession, sources lues (à créer)
- `vehicle-legal/references/vente-vehicule.md` — relue, créée par VEH-004
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Annonce, échanges, certificat de cession, reçu de paiement ; plateforme utilisée.
- Procès-verbal de contrôle technique remis et sa date ; certificat de situation administrative remis.
- Kilométrage annoncé et constaté ; historique d'entretien déclaré.
- Clause d'exclusion de garantie écrite ou déclarée ; description et diagnostic du défaut.

## Sortie attendue

1. Résumé : vente entre particuliers, défaut, demande envisagée.
2. Indices de la qualité du vendeur ; qualification conditionnelle si un usage professionnel est suspecté.
3. Fondements civils à examiner : délivrance conforme, vices cachés ; pièce utile et question ouverte pour chacun.
4. Écart entre annonce, contrôle technique et état constaté, présenté comme comparaison de pièces.
5. Brouillon de demande au vendeur.
6. Suites : vendeur professionnel établi → VEH-004 ; escroquerie alléguée → DOM-002 ; protection de plateforme → CONSO-018 ; expertise → VEH-010.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `vente-entre-particuliers-vehicule.md` et l'appliquer : aucune
garantie de la consommation appliquée à un vendeur particulier ; la
connaissance du défaut par le vendeur reste une question ; une clause
d'exclusion n'est ni validée ni écartée sans source lue. Les règles propres
à la plateforme sont distinguées du droit.

## Références métier et sources à rechercher

Code civil, délivrance conforme (pistes 1604 et suivants) et vices cachés
(pistes 1641 à 1649) ; Code de la route, contrôle technique avant cession et
déclaration de cession (pistes R322-4, R323-22), à vérifier ; pistes VEH-004
pour la qualification du vendeur.

## Critères d'acceptation

- [ ] Q01 n'applique pas la garantie légale de conformité à un vendeur particulier et prépare une demande civile.
- [ ] Q02 compare annonce, contrôle technique et diagnostic sans conclure à la connaissance du défaut.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs ou un avocat, et un expert automobile pour la question technique.

## Vérification

- Cas normal : Q01 — Embrayage défaillant quelques semaines après un achat entre particuliers.
- Cas limite : Q02 — Contrôle technique favorable remis, défaut grave constaté par un garage peu après.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Garanties de la consommation, plainte, règles internes de plateforme
appliquées comme droit, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).
