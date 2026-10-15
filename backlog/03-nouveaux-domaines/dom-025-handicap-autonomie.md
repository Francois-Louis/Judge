---
id: DOM-025
titre: "Cadrer un plugin handicap et autonomie"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-025 — Cadrer un plugin handicap et autonomie

## Objectif

Aider les personnes concernées et les aidants à comprendre une décision et à faire valoir un besoin d'accessibilité ou d'accompagnement.

Nom de plugin proposé : `disability-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire une décision liée au handicap ou à l'autonomie et préparer les pièces manquantes.
- Préparer une demande d'aménagement ou d'accès à un service.
- Orienter un désaccord concernant l'accompagnement à domicile ou en établissement.

## Qualification et frontières

Auteur de la décision, demande précise, qualité du représentant, dates, besoins exprimés, justificatifs strictement utiles et recours déjà tenté.

La reconnaissance et l'accompagnement sont ici ; le calcul d'une prestation par une caisse se coordonne avec DOM-012, la scolarité avec DOM-027, l'emploi avec le plugin travail et la capacité juridique avec DOM-026.

## Sources à prévoir et vérifier

Code de l'action sociale et des familles, textes sur l'accessibilité, Code de la sécurité sociale selon l'objet et sources officielles des organismes compétents.

- [Mon Parcours Handicap](https://www.monparcourshandicap.gouv.fr/)
- [Défenseur des droits](https://www.defenseurdesdroits.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Décrypter une notification administrative choisie et préparer les questions et pièces d'une contestation, sans multiplier les procédures.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] La personne conserve sa place dans les choix et échanges ; handicap, incapacité juridique et pouvoir du proche ne sont pas assimilés.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une personne ne comprend pas le motif d'un refus.
- Un usager ne peut pas accéder au service prévu.
- Un aidant souhaite faire une démarche sans mandat fourni.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

