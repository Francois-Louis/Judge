---
id: ENF-011
titre: "S'orienter face à une saisie de biens ou de véhicule"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-011 — S'orienter face à une saisie de biens ou de véhicule

## Objectif et résultat attendu

Une personne dont des biens meubles ou le véhicule sont saisis comprend la
mesure, l'inventaire, les biens dont l'insaisissabilité est à vérifier et les
suites possibles.

## Périmètre et fichiers

- `enforcement-legal/skills/goods-seizure-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/saisie-biens.md` — mesures, biens protégés, suites, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Procès-verbal et inventaire ; titre visé ; biens appartenant à un tiers et
preuves ; usage professionnel d'un bien ; véhicule et papiers.

## Sortie attendue

Fiche de la mesure ; biens à discuter et preuves ; suites à vérifier ;
questions ; limites.

## Travail attendu

Bien d'un tiers : preuves de propriété à réunir, revendication à vérifier.
Ne jamais conseiller de déplacer ou cacher un bien saisi. Achat ou réparation
du véhicule → DOM-023.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, saisie-vente, biens insaisissables,
immobilisation du véhicule.

## Critères d'acceptation

- [ ] G01 produit la fiche et les biens à discuter sans conclusion.
- [ ] G02 traite le bien d'un tiers comme question de preuve.

## Vérification

- Cas normal : G01 — Saisie-vente au domicile, inventaire incluant un outil de travail.
- Cas limite : G02 — Véhicule immobilisé appartenant à un parent.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisie immobilière, contestation rédigée, envoi.

## Complément issu des frictions des commissaires de justice

Points 29–34 de la [matrice utilisateur](../dom-003-frictions-utilisateurs.md).

- [ ] G03 — Commandement avant saisie-vente : réunir titre, commandement, signification et inventaire ; identifier le délai et les formalités à vérifier avant de dater une suite.
- [ ] G04 — Bien nécessaire, outil professionnel ou bien d'un tiers : documenter usage, propriété, valeur et exceptions de protection ; identifier les démarches de revendication ou distraction à faire examiner sans les rédiger.
- [ ] G05 — Entrée au domicile : décrire heure, lieu, titre, présence du débiteur, accompagnement et formalités ; vérifier le régime sans annoncer une interdiction absolue d'entrée ni conseiller une obstruction.
- [ ] G06 — Mesures jugées excessives : tableau dette, actes, biens, coûts et effets ; demander examen de nécessité et proportionnalité au JEX via un professionnel, sans présumer l'abus. Même exigence pour la story d'une autre mesure.
- [ ] G07 — Vente amiable envisagée : faire vérifier fenêtre temporelle, proposition d'acquéreur, accord et contrôle requis ; aucun déplacement ou vente libre d'un bien saisi conseillé.

Scénarios G03–G07 **attendus, non exécutés** : commandement sans saisie encore réalisée ; outil appartenant à un client ; entrée en l'absence du débiteur ; plusieurs actes pour une dette modeste ; acquéreur proposé après inventaire. Sources supplémentaires à rechercher : commandement préalable, biens protégés et exceptions, tiers propriétaires, accès aux locaux, proportionnalité (piste L111-7) et vente amiable. Aucune durée du document utilisateur n'est validée ici.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
