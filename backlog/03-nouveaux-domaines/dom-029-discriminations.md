---
id: DOM-029
titre: "Cadrer un plugin discriminations et égalité d'accès"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-029 — Cadrer un plugin discriminations et égalité d'accès

## Objectif

Aider à qualifier un refus ou un traitement défavorable et à préparer un dossier factuel.

Nom de plugin proposé : `equality-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Distinguer désaccord, différence de traitement et discrimination alléguée à partir des faits.
- Organiser la chronologie, les comparateurs et les preuves licitement disponibles.
- Préparer une demande d'explication ou une orientation vers l'interlocuteur pertinent.

## Qualification et frontières

Situation, critère allégué, auteur, service ou droit concerné, dates, échanges, éléments de comparaison et résultat recherché.

Ce domaine porte la qualification et l'orientation ; le recours contre une rupture de contrat de travail, un bail ou une décision scolaire reste piloté dans son domaine.

## Sources à prévoir et vérifier

Code pénal, Code du travail, textes civils/administratifs et européens selon le champ ; décisions et ressources officielles du Défenseur des droits.

- [Défenseur des droits](https://www.defenseurdesdroits.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Préparer un dossier de refus d'accès à un service, sans décider que le refus est illégal sur le seul récit initial.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le récit est distingué des faits établis ; le régime de preuve et les voies choisies doivent être recherchés pour la situation réelle.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une personne reçoit un refus de location.
- Un service refuse un aménagement demandé.
- Deux clients semblent traités différemment sans motif connu.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Complément des frictions IA — 16 octobre 2026

Points 19–22 et 26 de la [matrice IA](../02-plugins-existants/exist-005-annexes/exist-005-frictions-utilisateurs.md) : prévoir la qualification d'une discrimination algorithmique alléguée et le dossier d'indices, notamment diffusion d'offres, tri de CV et critères de substitution. Recueillir situation, critère allégué, effets concrets, données connues, comparateurs licitement disponibles et décision, sans inférer de données sensibles tierces ni déduire la discrimination d'un simple refus. Sortie à découper : chronologie, indices/manques et orientation vers le Défenseur des droits ou autre interlocuteur selon compétence vérifiée. Le secteur garde son recours, PRV-031 la demande sur la décision automatisée et IA-003/004 la qualification IA. Cas attendu : code postal utilisé dans un score, effet défavorable connu et méthode inconnue ; préserver les hypothèses et les délais sectoriels sans verdict automatique. La décision n° 2025-182 citée dans la source reste à lire avant d'en tirer une règle. [Portée et contrôles](../02-plugins-existants/exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

