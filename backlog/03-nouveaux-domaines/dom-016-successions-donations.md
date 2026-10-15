---
id: DOM-016
titre: "Cadrer un plugin successions et donations"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-016 — Cadrer un plugin successions et donations

## Objectif

Aider les héritiers et les donateurs à comprendre les pièces, les options et les étapes d'une transmission patrimoniale.

Nom de plugin proposé : `inheritance-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un courrier de notaire ou une demande de pièce et préparer des questions précises.
- Organiser l'actif, le passif et les informations nécessaires avant une décision successorale.
- Préparer un dossier de désaccord entre héritiers, de partage ou de donation à analyser.

## Qualification et frontières

Date du décès, liens familiaux, régime matrimonial, résidence habituelle, testament ou donations connus, biens/dettes, actes déjà signés et élément étranger.

Ce domaine traite la transmission et l'indivision successorale ; les obsèques relèvent de DOM-031, la fiscalité de DOM-011, le patrimoine du couple de DOM-013 et la protection d'un majeur de DOM-026.

## Sources à prévoir et vérifier

Code civil, Code de procédure civile, textes fiscaux pour leur seule articulation, instruments transfrontaliers pertinents et sources officielles Justice et Service Public.

- [Règlement d'une succession — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/N171?lang=fr)
- [Indivision entre héritiers — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/F1296)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Décrypter un courrier de règlement de succession et produire une liste de pièces, de points à éclaircir et de décisions à ne pas confondre.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] L'option successorale, le partage et la déclaration fiscale sont traités comme des tâches distinctes ; aucun partage définitif n'est calculé sur un dossier incomplet.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un héritier est invité à signer un document qu'il ne comprend pas.
- Une succession comporte des dettes mal identifiées.
- Des héritiers sont en désaccord sur l'occupation ou la vente d'un bien.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

