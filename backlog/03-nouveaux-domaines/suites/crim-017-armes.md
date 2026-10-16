---
id: CRIM-017
titre: "Qualifier la détention ou le transport d'une arme ou d'un objet"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-017 — Qualifier la détention ou le transport d'une arme ou d'un objet

## Objectif et résultat attendu

Une personne qui détient ou transporte une arme, un couteau ou un objet
(héritage, chasse, tir sportif, collection, outil), ou à qui un tel objet a
été saisi, comprend la catégorie à vérifier, les autorisations ou motifs à
établir et la démarche régulière. Ajout du 16 octobre 2026
([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `criminal-legal/skills/weapons-status/SKILL.md` — le skill (à créer)
- `criminal-legal/references/armes.md` — catégories, autorisations, transport, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Description de l'objet et documents (facture, permis de chasser, licence,
déclaration) ; origine (achat, héritage) ; usage ; circonstances d'un
contrôle ou d'une saisie ; procès-verbal remis.

## Sortie attendue

Catégorie à vérifier et ce qui la décide ; démarche régulière à vérifier
(déclaration, autorisation, remise) ; lecture d'une saisie ; questions ;
limites. Aucune catégorie affirmée sans texte lu.

## Travail attendu

Démarches d'autorisation auprès de l'administration → orientation DOM-010.
Ne fournir aucune aide pour acquérir, modifier, dissimuler ou transporter une
arme en dehors du cadre légal ; un héritage d'arme reçoit la démarche
régulière, pas un moyen de conserver sans déclaration.

## Références métier et sources à rechercher

Code de la sécurité intérieure, armes et munitions (pistes L311-1 et
suivants, R311-2) ; Code pénal pour le port et le transport sans motif
légitime ; services officiels en ligne en vigueur.

## Critères d'acceptation

- [ ] W01 donne la démarche régulière sans catégorie non sourcée.
- [ ] W02 lit la saisie et oriente sans aide au contournement.

## Vérification

- Cas normal : W01 — Fusil de chasse hérité d'un grand-père, sans papiers.
- Cas limite : W02 — Couteau saisi lors d'un contrôle, la personne invoque un usage professionnel.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Achat, modification ou réparation d'armes, demande d'autorisation rédigée,
défense au fond, envoi.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-002-annexes/dom-002-decoupage-penal.md).
