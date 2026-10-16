---
id: DOM-039
titre: "Cadrer un plugin micro-entreprise et travail indépendant"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-039 — Cadrer un plugin micro-entreprise et travail indépendant

## Objectif

Aider un auto-entrepreneur ou un travailleur indépendant à comprendre son
statut, ses déclarations, ses cotisations et ses impôts liés à l'activité, et
à préparer une démarche face à l'URSSAF ou à l'administration fiscale.
Ajouté le 16 octobre 2026 ([décisions](../decisions-2026-10-16.md)).

Nom de plugin proposé : `self-employed-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un courrier de l'URSSAF (cotisations, régularisation, majorations, mise en demeure) et repérer période, montant et stade.
- Vérifier une déclaration de chiffre d'affaires, un dépassement de seuil ou un changement de régime.
- Comprendre l'imposition de l'activité (versement libératoire, cotisation foncière des entreprises, TVA) sans calcul non sourcé.
- Préparer les questions sur le cumul de l'activité avec un emploi salarié, une indemnisation chômage ou des aides.
- Lire un avis de contrôle de l'URSSAF, une lettre d'observations ou une mise en demeure qui suit un contrôle, et préparer la réponse.

## Qualification et frontières

Statut (micro-entrepreneur, entreprise individuelle, autre), activité,
date de création, chiffre d'affaires déclaré, organismes, courriers reçus et
stade de chaque procédure.

L'activité indépendante est ici. Impôts du foyer hors activité → DOM-011 ;
prestations de la CAF et minima sociaux → DOM-012 ; retraite → DOM-036 ;
contrat avec un client professionnel → commercial ; client particulier →
consommation ou secteur ; relation de travail déguisée → travail privé ;
acte de saisie → DOM-003 ; difficultés de paiement globales d'une activité →
qualification séparée. Vérification de comptabilité par le fisc → DOM-011 ;
relation avec l'expert-comptable → DOM-041 (compléments du 16 octobre 2026).

## Sources à prévoir et vérifier

Code de la sécurité sociale, Code général des impôts et ses annexes, textes
relatifs au régime micro-social et micro-fiscal ; URSSAF, administration
fiscale et guichet des formalités comme sources d'information.

Les guides orientent le cadrage ; les textes et versions applicables seront
vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire un courrier de l'URSSAF adressé à un micro-entrepreneur et repérer
période, montants recopiés, stade et pièces à réunir.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son courrier sans connaître le nom du régime.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons avec DOM-011, DOM-012 et commercial.
- [ ] Aucun montant de cotisation ou d'impôt n'est calculé sans source lue et date établie.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une mise en demeure de l'URSSAF pour des cotisations d'un trimestre déclaré à zéro.
- Un dépassement de seuil de chiffre d'affaires découvert en fin d'année.
- Une micro-entrepreneuse également salariée à temps partiel et allocataire de la CAF.
- Une lettre d'observations de l'URSSAF après un contrôle, chiffrage non détaillé.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas
résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, tenir une comptabilité, faire des déclarations à la
place de la personne ou couvrir toute la fiscalité des entreprises.
