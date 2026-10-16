---
id: DOM-035
titre: "Cadrer un plugin responsabilité civile et dommages"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-035 — Cadrer un plugin responsabilité civile et dommages

## Objectif

Aider une personne à organiser les faits et preuves d'un dommage et à comprendre les fondements à examiner.

Nom de plugin proposé : `civil-liability-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer la chronologie d'un accident ou d'un dommage matériel et identifier les personnes concernées.
- Organiser les justificatifs de préjudice et les demandes d'explication ou d'indemnisation.
- Distinguer responsabilité, preuve, couverture d'assurance et procédure de réparation.

## Qualification et frontières

Événement, date, lieu, victime, auteurs allégués, rôle d'un bien ou d'un mineur, preuves, dépenses, assureurs et éventuelles mesures déjà prises.

Les dommages civils sans domaine spécial identifié sont ici ; accident de circulation, dommage médical, défaut de construction et infraction exigent d'abord leur qualification sectorielle et leur routage.

Décision du 16 octobre 2026 ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : l'offre d'indemnisation faite par un assureur à une victime d'accident de la circulation relève de ce domaine ; la garantie due par l'assureur à son propre assuré reste en DOM-005.

## Sources à prévoir et vérifier

Code civil, régimes spéciaux pertinents et jurisprudence ; procédure, assurance et règles d'expertise selon le cas.

- [Service Public](https://www.service-public.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Structurer un dossier de dommage matériel du quotidien dans un cas borné, avec pièces et chiffrage documenté.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Fait, fondement, causalité et préjudice sont distingués ; aucune responsabilité ou indemnité ne sont déduites du seul fait qu'un dommage existe.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un objet est endommagé par un tiers.
- Un accident survient pendant une activité associative.
- Une victime reçoit une proposition d'indemnisation avec renonciation alléguée.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

