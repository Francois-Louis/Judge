---
id: DOM-028
titre: "Cadrer un plugin séjour, nationalité et asile"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-028 — Cadrer un plugin séjour, nationalité et asile

## Objectif

Aider les personnes étrangères et leurs proches à comprendre une demande, un refus ou une mesure qui affecte leurs droits en France.

Nom de plugin proposé : `immigration-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire une demande de pièce, une convocation, un refus ou une mesure reçue.
- Organiser les preuves de dépôt, de notification et de situation pour une démarche déterminée.
- Découper séparément séjour, nationalité, asile et mesures d'éloignement selon les acteurs et procédures.

## Qualification et frontières

Nationalité, âge, résidence et localisation actuelle, statut allégué, type d'acte, date et mode de notification, procédure et éventuelle restriction de liberté.

Le statut et ses décisions sont ici ; le contrat de travail, l'accès aux prestations et les relations familiales restent dans leurs domaines avec un rattachement explicite.

## Sources à prévoir et vérifier

CESEDA, Code civil pour la nationalité, textes UE et conventions applicables, sources officielles de l'administration, de l'OFPRA, de la CNDA et des juridictions.

- [Service Public](https://www.service-public.gouv.fr/)
- [OFPRA](https://www.ofpra.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une demande de pièces dans une procédure de titre de séjour choisie ; les mesures urgentes seront des stories distinctes.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage sépare les régimes et urgences ; il ne propose pas un délai de recours de droit commun pour tous les actes.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une preuve de dépôt est disponible mais pas la décision.
- Une personne reçoit un acte dont elle ne comprend pas la portée.
- Une décision est lue plusieurs jours après sa notification alléguée.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

