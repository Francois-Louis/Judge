---
id: CRIM-016
titre: "Comprendre le cadre d'une manifestation et ses suites pour un participant"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-001]
---

# CRIM-016 — Comprendre le cadre d'une manifestation et ses suites pour un participant

## Objectif et résultat attendu

Un participant à une manifestation comprend le cadre annoncé (déclaration,
interdiction, périmètre), et, après coup, ce que signifie une verbalisation
ou une convocation liée à sa participation. Ajout du 16 octobre 2026
([décisions](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

- `criminal-legal/skills/demonstration-guide/SKILL.md` — le skill (à créer)
- `criminal-legal/references/manifestations.md` — police administrative et pénale, sanctions possibles, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Arrêté ou annonce de la préfecture ; lieu, date ; avis de contravention ou
convocation reçus ; objets transportés ; faits déclarés.

## Sortie attendue

Distinction entre mesure administrative (déclaration, interdiction,
périmètre) et suite pénale (contravention, délit allégué) ; lecture de l'acte
reçu ; questions ; interlocuteurs ; limites. Aucune sanction affirmée sans
texte lu.

## Travail attendu

Contestation d'un arrêté d'interdiction ou démarches de l'organisateur →
DOM-010. Avis d'amende → CRIM-003 ; interpellation → CRIM-015 ou CRIM-002.
Ne donner aucun conseil pour contourner un dispositif de maintien de l'ordre
ou commettre une infraction.

## Références métier et sources à rechercher

Code de la sécurité intérieure, manifestations sur la voie publique (pistes
L211-1 et suivants) ; Code pénal, participation à une manifestation interdite
ou attroupement (pistes 431-3 et suivants, R644-4).

## Critères d'acceptation

- [ ] D01 distingue mesure administrative et suite pénale sans sanction non sourcée.
- [ ] D02 oriente la contestation d'un arrêté vers DOM-010.

## Vérification

- Cas normal : D01 — Contravention reçue pour participation à une manifestation interdite.
- Cas limite : D02 — Organisateur qui veut contester l'interdiction de sa manifestation.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Organisation d'une manifestation, recours administratif rédigé, défense au
fond, envoi.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 49–58 et 82–87 de la [matrice](../dom-002-frictions-utilisateurs.md). Ajouter chronologie avant/pendant/après, lieu et déplacements, sommations entendues ou non, conditions de sortie d'un encerclement, durée déclarée, unités, identifiants, armes alléguées et blessures. CRS et gendarmes mobiles sont distingués dans le choix du canal.

- [ ] D03 — Usage de force, dispersion ou nasse : relever contexte, danger annoncé, sommations, exceptions à rechercher, nécessité et proportionnalité à examiner ; ni absence de sommation ni présence d'une arme ne suffisent à conclure au droit applicable.
- [ ] D04 — Interpellation dans une foule : séparer présence et faits individuels allégués ; CRIM-002/015 selon mesure en cours ou achevée ; avocat si mise en cause.
- [ ] D05 — Images et agents non identifiés : séquences complètes, témoins et identification visible → CRIM-020 ; signalement → CRIM-021 ; plainte → CRIM-004. Aucun conseil pour franchir ou contourner un dispositif.

Scénarios **attendus, non exécutés** : encerclement avec sortie alléguée impossible ; force sans sommations perçues ; vidéo tronquée d'une interpellation. Sources supplémentaires à rechercher : règles d'usage de la force et armes, sommations et exceptions, textes opérationnels et jurisprudence officielle sur l'encerclement avec date et portée exactes ; aucune décision présumée depuis le texte utilisateur.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation ni sélection.
Contrat commun : [découpage](../dom-002-decoupage-penal.md).
