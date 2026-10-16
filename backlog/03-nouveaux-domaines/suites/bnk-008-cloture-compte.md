---
id: BNK-008
titre: "Réagir à une clôture ou à un refus d'ouverture de compte"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-004, PILOTE-003, BASE-005, BASE-006, BNK-001]
---

# BNK-008 — Réagir à une clôture ou à un refus d'ouverture de compte

## Objectif et résultat attendu

Une personne dont le compte est clôturé, ou qui ne parvient pas à ouvrir de
compte, comprend la décision, les démarches possibles et le dispositif de
droit au compte à vérifier.

## Périmètre et fichiers

- `banking-legal/skills/account-closure-access/SKILL.md` — le skill (à créer)
- `banking-legal/references/compte.md` — clôture, droit au compte, sources lues (à créer)
- `banking-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Lettre de clôture ou de refus ; convention ; date ; statut (particulier,
professionnel) ; autres comptes détenus.

## Sortie attendue

Décision lue ; démarches à vérifier (droit au compte, nouvelle banque) ;
brouillon de demande d'explication ; limites.

## Travail attendu

Refus allégué discriminatoire → question à DOM-029. Compte professionnel :
dispositif à vérifier pour ce statut.

## Références métier et sources à rechercher

Code monétaire et financier, droit au compte et clôture (piste L312-1) ;
procédure de la Banque de France.

## Critères d'acceptation

- [ ] A01 explique la décision et la démarche à vérifier.
- [ ] A02 isole la question de discrimination.

## Vérification

- Cas normal : A01 — Lettre de clôture sans motif, préavis indiqué.
- Cas limite : A02 — Trois refus d'ouverture que la personne relie à sa nationalité.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisine de la Banque de France faite à la place de la personne, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 12, 42–44, 49–51, 55 et 98 de la [matrice](../dom-004-frictions-utilisateurs.md).

Inclure la clôture demandée par le client et refusée ou retardée ; recueillir sa demande et sa réception, opérations en attente, cotisations prépayées, date effective et solde de clôture. Pour l'ouverture, conserver dépôt, pièces remises, refus exprès ou silence.

- [ ] A03 — Demande de clôture bloquée : expliquer les obstacles documentés et préparer la relance ; frais après fermeture et part de cotisation → demande de restitution à vérifier, détail BNK-003.
- [ ] A04 — Silence sur une ouverture : établir réception et conditions du dossier avant la procédure de droit au compte ; ne pas supposer que tout silence est un refus.
- [ ] A05 — Micro-entrepreneur : distinguer compte dédié, offre commerciale professionnelle et usage permis par la convention ; qualification de l'obligation → DOM-039.
- [ ] A06 — Clôture avec chèques non débités ou nouvelles conditions : identifier opérations et versions ; mobilité → BNK-013, compte bloqué sans clôture → BNK-014.

Scénarios A03–A06 **attendus, non exécutés**. Sources : clôture à l'initiative de chaque partie, restitution de frais périodiques, droit au compte, conventions et obligations de compte selon l'activité. Aucune clôture exécutée.

## État de la proposition — 16 octobre 2026

Issue de DOM-004, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-004-decoupage-banque.md).
