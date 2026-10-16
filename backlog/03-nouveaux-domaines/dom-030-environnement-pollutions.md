---
id: DOM-030
titre: "Cadrer un plugin environnement et pollutions"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-030 — Cadrer un plugin environnement et pollutions

## Objectif

Aider les riverains et usagers à documenter une nuisance environnementale et à identifier les démarches pertinentes.

Nom de plugin proposé : `environmental-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer un signalement documenté de pollution, déchets, rejets ou activité gênante.
- Lire un document ou une décision concernant une installation ou un milieu.
- Organiser les pièces d'un préjudice allégué et distinguer contrôle, prévention et indemnisation.

## Qualification et frontières

Lieu, milieu affecté, activité/source supposée, dates et répétition, observations, documents disponibles, autorité contactée et dommage allégué.

La police et les règles environnementales sont ici ; les droits privés entre voisins restent en DOM-020, l'autorisation d'urbanisme en DOM-019 et les obligations d'une exploitation agricole se coordonnent avec DOM-014.

## Sources à prévoir et vérifier

Code de l'environnement, textes européens et locaux applicables, décisions administratives pertinentes, sources officielles du ministère et des services compétents.

- [Ministère de la Transition écologique](https://www.ecologie.gouv.fr/)
- [Géorisques](https://www.georisques.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Structurer un signalement d'un fait observé sans attribuer une responsabilité ou une causalité non établies.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Une observation, une mesure technique et un lien causal sont distingués ; signalement et demande de réparation ne sont pas présentés comme interchangeables.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Des rejets sont observés près d'un terrain.
- Un dépôt de déchets revient régulièrement.
- Un riverain souhaite consulter les documents d'une installation.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Frontière avec les emballages — 16 octobre 2026

La [matrice marketing](../02-plugins-existants/exist-004-annexes/exist-004-frictions-utilisateurs.md) attribue les obligations REP et PPWR d’une mise sur le marché à product-legal (PDT-020 à PDT-025), avec ses références métier embarquées. DOM-030 garde pollution, déchets observés, contrôle d’installation et dommage environnemental à cadrer ; contrat d’éco-organisme chez commercial, recours contre une décision administrative chez DOM-010. Ce complément ne lance pas le cadrage DOM-030.
