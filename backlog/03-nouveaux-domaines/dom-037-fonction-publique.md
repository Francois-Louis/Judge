---
id: DOM-037
titre: "Cadrer un plugin fonction publique et agents publics"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-037 — Cadrer un plugin fonction publique et agents publics

## Objectif

Aider fonctionnaires et contractuels publics à comprendre une décision de carrière, de rémunération ou de discipline.

Nom de plugin proposé : `public-employment-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un contrat, une décision de recrutement, de renouvellement ou de fin de fonctions.
- Préparer un dossier de rémunération, temps de service, congé ou évolution de carrière.
- Organiser les pièces d'une décision disciplinaire ou d'un signalement, avec sa procédure propre.

## Qualification et frontières

Employeur, versant, statut titulaire/stagiaire/contractuel, contrat/corps, décision, dates, notifications et objet exact.

La relation d'emploi public est ici ; l'emploi salarié privé reste dans employment-legal, la pension en DOM-036 et les prestations des caisses dans DOM-012.

## Sources à prévoir et vérifier

Code général de la fonction publique, statuts et textes d'application, textes spéciaux selon le personnel, jurisprudence administrative et sources officielles.

- [Portail de la fonction publique](https://www.fonction-publique.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une décision individuelle de carrière ou de rémunération pour un statut choisi.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le statut réel est vérifié avant le régime ; le conseil de prud'hommes et les règles de rupture du privé ne sont pas appliqués comme défaut.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un contractuel reçoit une décision de non-renouvellement.
- Un agent conteste un élément de rémunération.
- Une règle du salarié privé est invoquée pour un fonctionnaire.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Complément des frictions IA — 16 octobre 2026

Points 19–24 de la [matrice IA](../02-plugins-existants/exist-005-annexes/exist-005-frictions-utilisateurs.md) : qualifier statut, recrutement, évaluation ou surveillance avant le régime de recours. Découper les indices de discrimination et les effets d'un score sur une candidature/carrière ; accès données → PRV-001/030/031, informations algorithmiques publiques → DOM-010, qualification d'émotions/pratique interdite → IA-003. Recueillir offre, décision/évaluation, critères déclarés, notification et réception ; aucune transposition des règles du salarié privé. Cas attendu : évaluation contestée et rôle humain seulement déclaré, avec demandes d'explication et recours statutaires séparés.

Ces exigences restent à découper ou préciser ; [portée et contrôles de l'intégration](../02-plugins-existants/exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.


## Complément des frictions données personnelles — 16 octobre 2026

Points 32–40 de la [matrice données personnelles](../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md) : qualifier statut et décision, sans déduire le régime de la seule qualité publique de l'employeur. PRV-001/022/025/030 portent les droits et la fiche de surveillance ; décision de carrière, évaluation ou sanction et son recours restent à découper ici. Scénario attendu : donnée erronée dans une sanction, demande de correction et calendrier statutaire distincts. Portée et contrôles : voir la matrice.
