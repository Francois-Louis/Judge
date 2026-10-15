---
id: DOM-024
titre: "Cadrer un plugin dettes et surendettement des particuliers"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-024 — Cadrer un plugin dettes et surendettement des particuliers

## Objectif

Aider une personne en difficulté à mettre ses dettes à plat et à comprendre les documents et démarches qui la concernent.

Nom de plugin proposé : `debt-relief-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Établir un inventaire documenté des dettes, revenus, charges et procédures déjà engagées.
- Préparer les pièces d'un dossier ou lire une décision de surendettement.
- Comparer contestation d'une dette, demande de délai, négociation et orientation vers une procédure adaptée.

## Qualification et frontières

Statut personnel/professionnel, territoire, nature des dettes, créanciers, échéances, décisions, saisies, ressources et stade du dossier.

Le traitement global des difficultés est ici ; le bien-fondé du crédit reste en DOM-004, l'acte de saisie en DOM-003 et les procédures d'une activité professionnelle demandent une qualification séparée.

## Sources à prévoir et vérifier

Code de la consommation, règles de procédure et régimes spéciaux pertinents ; Banque de France et sources officielles selon le territoire.

- [Surendettement — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/N99?lang=fr)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une notification de surendettement et repérer stade, demandes de pièces et points à vérifier.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Dépôt, recevabilité et mesures de traitement sont distingués ; le cadrage ne promet ni effacement de dette ni arrêt automatique des poursuites.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une personne cumule loyers, crédit et factures impayés.
- Un dossier a été déposé mais aucune décision de recevabilité n'est fournie.
- Une dette mêle dépenses privées et activité indépendante.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

