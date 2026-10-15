---
id: DOM-026
titre: "Cadrer un plugin de protection juridique des majeurs"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-026 — Cadrer un plugin de protection juridique des majeurs

## Objectif

Aider les personnes et leurs proches à comprendre une mesure, les pouvoirs et les démarches de protection.

Nom de plugin proposé : `adult-protection-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire une décision de protection et distinguer les pouvoirs réellement accordés.
- Préparer les questions relatives à un acte patrimonial, une dépense ou un compte de gestion.
- Organiser un dossier de demande, réexamen ou contestation d'une mesure selon l'objectif.

## Qualification et frontières

Qualité de la personne et du demandeur, décision ou mandat, date, étendue des pouvoirs, acte envisagé, urgence et souhait de la personne.

La protection et les pouvoirs sont ici ; la succession reste en DOM-016, les soins en DOM-007, l'accompagnement de l'autonomie en DOM-025 et une infraction alléguée en DOM-002.

## Sources à prévoir et vérifier

Code civil, Code de procédure civile et textes d'application, Justice et Service Public ; nature exacte de la mesure à vérifier.

- [Protection juridique des majeurs — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/N155?lang=fr)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une décision de protection pour identifier qui peut accomplir l'acte concerné et quelles vérifications restent nécessaires.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Sauvegarde, curatelle, tutelle, habilitation et mandat ne sont pas regroupés sous des pouvoirs identiques ; aucun diagnostic de capacité n'est établi par le skill.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un proche veut vendre un bien d'une personne protégée.
- La personne conteste une décision prise en son nom.
- Un parent est présumé incapable du seul fait de son âge.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

