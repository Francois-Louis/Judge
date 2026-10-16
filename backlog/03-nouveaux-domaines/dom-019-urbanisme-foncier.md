---
id: DOM-019
titre: "Cadrer un plugin urbanisme et foncier"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-019 — Cadrer un plugin urbanisme et foncier

## Objectif

Aider à comprendre une règle locale, une autorisation ou une décision publique affectant un terrain.

Nom de plugin proposé : `planning-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer la lecture d'une décision de permis, déclaration préalable ou refus.
- Rassembler les pièces d'une contestation d'autorisation ou d'un contrôle de travaux.
- Qualifier une préemption, une expropriation ou une contrainte foncière pour orienter le dossier.

## Qualification et frontières

Commune et parcelle, projet, document d'urbanisme applicable, décision, affichage/notification, qualité du demandeur et actes déjà engagés.

Les actes d'urbanisme sont ici ; la responsabilité de l'entrepreneur reste en DOM-015, les droits privés de voisinage en DOM-020 et les litiges environnementaux en DOM-030.

## Sources à prévoir et vérifier

Code de l'urbanisme, textes fonciers spéciaux, Code de justice administrative et documents locaux opposables selon le dossier.

- [Géoportail de l'urbanisme](https://www.geoportail-urbanisme.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire un refus d'autorisation et préparer la liste des motifs, pièces et voies à vérifier.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage distingue autorisation administrative et droits privés ; il ne conclut pas sur une règle locale sans document applicable à la parcelle.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un propriétaire reçoit un refus pour son projet.
- Des travaux voisins débutent sans document accessible.
- Une collectivité adresse un courrier relatif à l'acquisition d'un terrain.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Complément des frictions logement — 16 octobre 2026

Points 71–72, 104–106, 115 de la [matrice logement](dom-006-annexes/dom-006-frictions-utilisateurs.md).

Découper le recours d'un tiers contre une autorisation et l'examen de travaux anciens ou irréguliers. Pièces : décision et dossier, commune/parcelle, règles locales, qualité/intérêt du requérant, photos du panneau et continuité d'affichage, achèvement, recours déjà déposés et preuves des notifications. Sortie : chronologie sourcée, recevabilité à vérifier, acte requis et destinataires de chaque notification ; distinguer recours gracieux/contentieux, délais et effets selon version aux faits. Aucun délai calculé depuis une photo isolée ou la seule date du permis. Distinguer prescriptions pénale, civile et administrative, extinction d'une action et régularité du bâti. Autorisation publique, autorisation collective DOM-018 et droits privés DOM-020 ne se remplacent pas ; la vente reste DOM-017. Aucun recours public orienté vers une fiche de procédure civile générique.

- [ ] Le futur découpage attribue à chaque tâche ses entrées, sortie, sources, limites et scénarios, y compris les voies urgentes distinctes.

Scénarios **attendus, non exécutés** : Panneau photographié tardivement et recours déjà déposé sans preuve de notification : demander dossier et traces immédiatement, ne pas présumer délai ouvert ou recours recevable. Ancienne véranda sans pièce : absence d'autorisation à établir, sans régularité déduite de l'ancienneté.
Les textes, versions, transitions, seuils et échéances seront vérifiés sur
sources officielles lors des implémentations. Ce complément ne termine pas
le cadrage, ne crée aucun plugin et n'exécute aucune démarche externe.
