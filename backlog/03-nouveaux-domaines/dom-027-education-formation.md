---
id: DOM-027
titre: "Cadrer un plugin éducation et formation"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-027 — Cadrer un plugin éducation et formation

## Objectif

Aider parents, élèves, étudiants et personnes en formation à lire les décisions et contrats qui leur sont opposés.

Nom de plugin proposé : `education-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer la lecture d'une décision d'inscription, d'affectation ou de sanction.
- Organiser les pièces d'un litige de frais, d'annulation ou de prestation de formation.
- Préparer une demande d'aménagement, de protection ou de traitement d'un signalement.

## Qualification et frontières

Âge, représentant, niveau, public/privé, statut de l'établissement, contrat/règlement, décision, dates et financement.

Le litige avec l'établissement est ici ; les méthodes d'études restent dans law-student, le contrat de travail/apprentissage dans le plugin travail, les aides en DOM-012 et le volet handicap en DOM-025.

## Sources à prévoir et vérifier

Code de l'éducation, Code du travail pour le seul volet formation pertinent, Code de la consommation selon le contrat et textes/procédures de l'établissement.

- [Ministère de l'Éducation nationale](https://www.education.gouv.fr/)
- [Service Public](https://www.service-public.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une décision d'un établissement et préparer une demande motivée dans un régime précisément choisi.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Établissement public, privé sous contrat ou hors contrat, université et organisme de formation sont distingués ; aucun recours commun n'est présumé.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une école privée réclame des frais après un désistement.
- Une famille conteste une décision d'affectation.
- Une formation payée ne correspond pas au contrat fourni.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Complément des frictions IA — 16 octobre 2026

Points 20 et 28 de la [matrice IA](../02-plugins-existants/exist-005-annexes/exist-005-frictions-utilisateurs.md) : recueillir établissement public/privé, niveau, procédure/portail, représentant, classement, décision et dates de notification ; découper explication des critères d'affectation et contestation selon procédure. Information algorithmique publique → DOM-010, données → PRV-001/031, reconnaissance d'émotions → IA-003 pour qualification conditionnelle. Cas attendu : accès à des critères demandé alors qu'une échéance propre au portail approche ; restituer les deux démarches sans délai administratif générique ni place accordée promise.

Ces exigences restent à découper ou préciser ; [portée et contrôles de l'intégration](../02-plugins-existants/exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

