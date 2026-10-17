---
id: DOM-014
titre: "Cadrer un plugin agricole et rural"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-014 — Cadrer un plugin agricole et rural

## Objectif

Aider exploitants, fermiers, petits propriétaires et familles rurales à comprendre leurs contrats et à préparer une contestation étayée.

Nom de plugin proposé : `agricultural-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un bail rural et une demande de fermage, de reprise ou de résiliation.
- Préparer les pièces d'un litige avec une coopérative, un acheteur ou un fournisseur agricole.
- Orienter une décision relative à l'exploitation, au foncier ou à une aide, en identifiant le régime concerné.

## Qualification et frontières

Qualité des parties, activité réelle, parcelles et usage, bail écrit ou oral allégué, dates, décompte, acte reçu, arrêté local ou décision d'aide invoqués.

Le bail rural relève de ce domaine ; le contrat de travail va au plugin travail, le recours MSA au domaine social et l'indemnisation d'un assureur au domaine assurance. Les successions d'exploitation croisent DOM-016 sans être absorbées dans ce plugin.

## Sources à prévoir et vérifier

Code rural et de la pêche maritime, textes d'application et locaux, sources du ministère de l'Agriculture, de la MSA et textes UE dans leur champ.

- [Bail rural — Service Public Entreprendre](https://entreprendre.service-public.gouv.fr/vosdroits/N32025)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une demande de fermage et dresser la liste des montants, pièces et règles à vérifier, pour un bail et un territoire bornés.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage distingue bail rural, occupation d'un terrain et location d'habitation ; il n'applique pas une règle locative urbaine par défaut.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un fermier reçoit une hausse qu'il ne comprend pas.
- Un propriétaire demande la restitution d'une parcelle occupée depuis plusieurs années.
- Une coopérative applique des retenues que l'exploitant conteste.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.


## Complément des frictions douanes — 17 octobre 2026

Points 55 et 57, dossier K02 : C22/C23 demandent de qualifier matière/espèce et emballage avant d'attribuer un volet agricole, sanitaire ou phytosanitaire. DOM-009 garde documents et opération douanière ; confirmer ici la tâche sectorielle selon faits plutôt qu'attribuer tout matériau naturel au rural. Entrées : espèce scientifique si disponible, origine/licéité, transformation, pays/date, traitement/marquage et documents. Sortie future à découper : exigences pertinentes, pièces manquantes et question à l'autorité spécialisée. Cas : palette bloquée malgré produit accepté ; manche en bois ou matière animale mal identifié. CITES, réglementation de destination et NIMP 15 se recherchent séparément ; aucune autorisation ou exemption certifiée.

Exigences de la [matrice des 75 points](dom-009-annexes/dom-009-frictions-utilisateurs.md), sans sélection de tranche ni capacité annoncée comme livrée. [Portée et contrôles](dom-009-annexes/dom-009-frictions-verification.md).
