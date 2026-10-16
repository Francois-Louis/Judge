---
id: CONSO-011
titre: "Préparer une demande dans un achat entre particuliers"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-004]
---

# CONSO-011 — Préparer une demande dans un achat entre particuliers

## Objectif et résultat attendu

Une personne qui a acheté à un autre particulier un bien non livré ou non
conforme à l'annonce comprend que le droit de la consommation ne s'applique
pas en principe, quels fondements examiner, et obtient un brouillon de
demande au vendeur.

## Périmètre et fichiers

- `consumer-legal/skills/private-sale-dispute/SKILL.md` — le skill (à créer)
- `consumer-legal/references/vente-entre-particuliers.md` — régime civil, rôle des plateformes, sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Annonce ; échanges ; paiement et intermédiaire ; remise ou envoi ; état du
bien ; profil du vendeur (volume d'annonces, mentions).

## Sortie attendue

Fiche ; fondements civils à vérifier ; règles privées de la plateforme
distinguées du droit ; brouillon ; limites.

## Travail attendu

Un « particulier » vendant en volume reçoit une qualification
conditionnelle de vendeur professionnel, avec retour vers CONSO-001 ou
CONSO-002 si elle est établie. Escroquerie alléguée → DOM-002 ; paiement →
DOM-004.

## Références métier et sources à rechercher

Code civil, vente, délivrance, vices cachés ; obligations d'information des
places de marché sur la qualité du vendeur.

## Critères d'acceptation

- [ ] P01 n'applique pas le Code de la consommation au vendeur particulier.
- [ ] P02 laisse la qualité du vendeur conditionnelle et nomme les indices.

## Vérification

- Cas normal : P01 — Console d'occasion différente de l'annonce.
- Cas limite : P02 — Vendeur « particulier » qui publie quarante annonces identiques.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Plainte pénale, procédure judiciaire, médiation de la plateforme exécutée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
