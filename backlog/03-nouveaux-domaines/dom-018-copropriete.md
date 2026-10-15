---
id: DOM-018
titre: "Cadrer un plugin copropriété et syndic"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-018 — Cadrer un plugin copropriété et syndic

## Objectif

Aider les copropriétaires à contrôler les documents, charges et décisions qui leur sont opposés.

Nom de plugin proposé : `co-ownership-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un appel de charges et demander les justificatifs pertinents.
- Préparer l'examen d'une convocation, d'un vote et d'un procès-verbal d'assemblée générale.
- Organiser une réclamation sur des travaux, la gestion du syndic ou l'accès aux documents.

## Qualification et frontières

Qualité de copropriétaire ou locataire, lots, règlement, répartition, convocation/PV, votes, notifications et objet précis de la demande.

Les relations avec le syndic et le syndicat sont ici ; les charges récupérables réclamées au locataire restent en DOM-006, les malfaçons en DOM-015 et la transaction en DOM-017.

## Sources à prévoir et vérifier

Loi du 10 juillet 1965 et textes d'application, Code civil et règles de procédure pertinentes ; ANIL et sources officielles du logement.

- [ANIL](https://www.anil.org/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Décrypter un appel de charges contesté et préparer une demande de justificatifs adaptée à la qualité du demandeur.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] L'accès à une pièce, la contestation d'une charge et l'action contre une décision d'assemblée ne sont pas assimilés à une même démarche.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un copropriétaire reçoit une régularisation importante.
- Une résolution votée ne correspond pas à ce qu'il a compris en séance.
- Un locataire demande au syndic des documents relevant de sa relation avec le bailleur.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

