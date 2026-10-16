---
id: DOM-044
titre: "Cadrer un plugin militaires, réservistes et anciens combattants"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-044 — Cadrer un plugin militaires, réservistes et anciens combattants

## Objectif

Aider un militaire, un gendarme, un réserviste, un ancien militaire, un
ancien combattant, une victime de guerre ou leurs proches à comprendre une
décision liée à l'état militaire, une pension d'invalidité ou une
reconnaissance, et à préparer la démarche qui convient.
Ajouté le 16 octobre 2026 ([décisions](../decisions-2026-10-16.md)).

Nom de plugin proposé : `military-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire une décision individuelle : engagement, renouvellement ou non-renouvellement de contrat, résiliation, mutation, avancement, notation, solde ou radiation des cadres.
- Organiser les pièces d'une procédure disciplinaire militaire ou d'une sanction, avec la procédure et le conseil propres au statut.
- Préparer le recours administratif préalable propre aux militaires avant tout recours contentieux, après avoir vérifié son existence, son champ et ses exclusions à la date des faits.
- Lire une décision sur une pension militaire d'invalidité (blessure, maladie, imputabilité au service, taux), puis préparer la contestation prévue par le régime.
- Lire un refus de carte du combattant, de titre ou de statut de reconnaissance, ou de droit d'ancien combattant ou de victime de guerre.
- Préparer les questions d'un réserviste sur sa convocation, sa relation avec l'employeur civil et sa protection.
- Documenter un harcèlement, une discrimination ou une violence subis dans le service, avec les signalements internes propres aux armées et à la gendarmerie.

## Qualification et frontières

Statut exact (militaire de carrière, sous contrat, volontaire, gendarme,
réserviste, ancien militaire, ancien combattant, victime ou ayant droit),
armée ou formation de rattachement, décision, autorité signataire, dates,
notification et objet exact.

L'état militaire et les droits propres aux militaires, anciens combattants et
victimes de guerre sont ici. Un civil de la défense (fonctionnaire ou
contractuel) relève de DOM-037. Un salarié d'une entreprise de défense relève
du travail privé. La pension de retraite militaire, sa liquidation et la
carrière à valider relèvent de DOM-036, avec les faits de service établis
ici. Les prestations sociales de droit commun relèvent de DOM-012, la
reconnaissance d'un handicap de DOM-025. La plainte, la poursuite ou
l'infraction militaire alléguée relèvent de DOM-002, et le rapport entre un
réserviste et son employeur civil, pour la relation de travail elle-même,
du travail privé.

Le statut est vérifié avant le régime : les règles de la fonction publique
civile ou du salarié privé ne sont pas appliquées par défaut. Le juge et la
voie de recours dépendent de l'objet (carrière, discipline, pension
d'invalidité, reconnaissance) et sont recherchés pour chaque tâche, sans
recours commun présumé.

## Sources à prévoir et vérifier

Code de la défense (statut général des militaires, réserve, recours
administratif préalable), Code des pensions militaires d'invalidité et des
victimes de guerre, Code des pensions civiles et militaires de retraite pour
la seule articulation avec DOM-036, textes propres à la gendarmerie,
jurisprudence administrative ; informations officielles du ministère des
Armées et de l'Office national des combattants et des victimes de guerre.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà
embarqué. L'existence, le champ, les délais et les effets de chaque recours
préalable seront ouverts et vérifiés lors de l'implémentation.

## Première tranche proposée

Lire une décision individuelle de carrière pour un militaire sous contrat :
statut, objet, autorité, notification, voies de recours mentionnées et
questions à vérifier avant le recours préalable.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son courrier ou de son problème sans connaître le nom du code ou du recours.
- [ ] Le statut réel est vérifié avant le régime ; aucune règle de la fonction publique civile, du salarié privé ou du conseil de prud'hommes n'est appliquée par défaut.
- [ ] Chaque recours préalable propre aux militaires est rattaché à un texte lu et daté ; aucun délai n'est donné sans source.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons avec DOM-002, DOM-012, DOM-025, DOM-036 et DOM-037.
- [ ] La collecte se limite aux pièces utiles ; aucune information classifiée ou opérationnelle n'est demandée.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas une pension, un taux ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un militaire sous contrat reçoit un non-renouvellement et veut saisir directement le tribunal administratif.
- Un gendarme invoque une règle du Code général de la fonction publique contre une mutation.
- Une ancienne militaire conteste le taux d'une pension militaire d'invalidité pour une blessure en service.
- Un ancien militaire se voit refuser la carte du combattant.
- Un réserviste convoqué craint une sanction de son employeur civil.
- Un civil de la défense se présente comme militaire.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas
résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story, traiter
d'informations classifiées ou d'opérations, ou exécuter une démarche externe.
