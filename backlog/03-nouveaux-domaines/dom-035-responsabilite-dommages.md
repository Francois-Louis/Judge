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

## Besoins issus des frictions assurance

Points 28, 44, 47–48, 52 et 58 de la [matrice assurance](dom-005-frictions-utilisateurs.md). Au futur découpage, prévoir inventaire des préjudices corporels et justificatifs (revenus, assistance, dépenses, séquelles alléguées, douleurs, besoins futurs), état de consolidation à établir avec les professionnels médicaux et lecture d'une offre avec renonciation. L'offre de l'assureur à la victime de la circulation garde ce propriétaire, conformément à la décision du 16 octobre 2026 ; garantie propre et seuil GAV restent en DOM-005.

Scénarios **attendus, non exécutés** : offre corporelle avant consolidation ou sans poste de perte de revenus ; constat auto contesté et coefficient modifié. Distinguer faits et responsabilité alléguée, postes documentés et expertise médicale, transaction et provision ; ne pas déduire la responsabilité d'une case de constat. Prévoir régime spécial circulation, procédure d'offre et prescription à partir des faits et textes lus, sans calcul ni délai validé ici. Le coefficient et la cotisation restent INS-014 ; complément factuel au constat INS-002. Ces tâches au fond restent à découper ; aucun skill n'est livré par ce complément.

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

## Besoin issu des frictions des commissaires de justice

La [matrice utilisateur](dom-003-frictions-utilisateurs.md) et sa liste d'organismes demandent de distinguer réclamation professionnelle, recours contre une mesure et réparation d'un dommage. Au futur découpage, prévoir la préparation factuelle d'un dossier de responsabilité professionnelle alléguée : mission et actes, dates, faute alléguée, dommage documenté, causalité discutée, recours exercés et assureur éventuellement identifié. Aucune responsabilité n'est déduite de la seule irrégularité alléguée.

Scénarios **attendus, non exécutés** : préjudice financier attribué à un acte contesté ; réclamation professionnelle déjà déposée mais indemnisation demandée séparément. ENF-015 possède la réclamation, ENF-014 les frais et la story de la mesure son recours. Vérifier régime de responsabilité, prescription, compétence et assurance à partir des faits ; cette tâche au fond reste à découper, sans demande indemnitaire livrée.
