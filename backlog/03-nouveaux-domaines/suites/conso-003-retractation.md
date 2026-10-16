---
id: CONSO-003
titre: "Exercer la rétractation d'un achat à distance ou hors établissement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-003 — Exercer la rétractation d'un achat à distance ou hors établissement

## Objectif et résultat attendu

Une personne qui veut revenir sur un achat sait si un droit de rétractation
peut exister, quelles dates doivent être prouvées, et obtient un brouillon de
déclaration avec les preuves à conserver.

## Périmètre et fichiers

- `consumer-legal/skills/withdrawal-notice/SKILL.md` — le skill (à créer)
- `consumer-legal/references/retractation.md` — canaux, exceptions, informations dues, sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Canal (site, téléphone, domicile, foire ou salon, magasin) ; date de
conclusion et de réception ; nature du bien ou du service (personnalisé,
périssable, descellé, service commencé à la demande) ; informations reçues
sur la rétractation ; état du bien ; crédit lié à l'achat.

## Sortie attendue

Existence conditionnelle du droit avec les faits qui la décident ; dates
connues et à prouver ; brouillon de déclaration ; preuves d'envoi et de
retour à conserver ; limites. Aucun délai calculé sans texte lu et date de
départ établie (informations minimales d'un délai, BASE-005).

## Travail attendu

Appliquer `qualification-achat.md`. Distinguer droit légal et politique
commerciale du magasin. Orienter le crédit lié (DOM-004), les travaux à
domicile (DOM-015), le voyage (DOM-008) et l'assurance (DOM-005). Pour un
petit professionnel contractant hors établissement, qualification
conditionnelle, sans accorder ni écarter la protection.

## Références métier et sources à rechercher

Code de la consommation, contrats à distance et hors établissement,
exceptions, foires et salons ; directive 2011/83/UE. Version à la date de
conclusion.

## Critères d'acceptation

- [ ] R01 produit le brouillon et la liste des preuves, avec délai seulement s'il est sourcé et daté.
- [ ] R02 isole l'achat sur salon et le crédit en questions distinctes.
- [ ] R03 laisse la protection du petit professionnel conditionnelle.
- [ ] La sortie se comprend sans formation juridique, sans garantir l'issue.

## Vérification

- Cas normal : R01 — Robe commandée en ligne, reçue, qui ne convient pas.
- Cas limite : R02 — Canapé commandé sur un salon, financé par un crédit proposé sur place.
- Cas limite : R03 — Fleuriste démarché dans sa boutique pour un site web.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Remboursement bancaire, annulation d'un crédit, frais de retour chiffrés
sans source, envoi de la déclaration.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
