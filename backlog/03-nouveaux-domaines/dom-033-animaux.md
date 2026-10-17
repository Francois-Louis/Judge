---
id: DOM-033
titre: "Cadrer un plugin animaux et responsabilités"
statut: terminee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-033 — Cadrer un plugin animaux et responsabilités

## Objectif

Aider détenteurs, acquéreurs et personnes concernées par un animal à comprendre contrats et responsabilités.

Nom de plugin proposé : `animal-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un contrat de vente, cession, adoption, garde ou pension.
- Organiser une contestation sur les documents, la prestation ou l'état allégué de l'animal.
- Qualifier un incident ou signalement et orienter vers le domaine compétent.

## Qualification et frontières

Espèce, usage, détenteur/propriétaire, qualité du cédant, contrat, identification, dates et pièces vétérinaires strictement utiles.

Les règles propres à l'animal et à sa détention sont ici ; l'élevage professionnel se coordonne avec DOM-014, le voisinage avec DOM-020, l'assurance avec DOM-005 et la qualification pénale avec DOM-002.

## Sources à prévoir et vérifier

Code rural et de la pêche maritime, Code civil, Code pénal et règles locales ou spécifiques selon l'espèce et l'activité ; ministère de l'Agriculture.

- [Ministère de l'Agriculture](https://agriculture.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

[ANM-001](suites/anm-001-acquisition-chien-documents.md) : lire les documents
de vente d'un chien de compagnie à un particulier, auprès d'un professionnel
ou d'un particulier, contrat et remise en France. Lecture des engagements, pièces à vérifier
et questions au cédant ; ni diagnostic ni action en garantie. Proposition,
sans lancement d'implémentation.

## Critères d'acceptation

- [x] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [x] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique. *Parcours documentaires fictifs relus par le rédacteur ; compréhension réelle non observée.*
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons. *Contrat cible documenté, aucun paquet créé.*
- [x] Le cadrage prévoit les régimes spécifiques de cession et d'espèce ; il ne transpose pas mécaniquement la garantie d'un bien courant et ne produit pas de diagnostic vétérinaire.
- [x] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [x] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici. *Préalable satisfait après BASE-011 ; aucune tranche sélectionnée.*

## Scénarios de contrôle

- Un vendeur n'a pas remis les documents attendus.
- Une pension facture des prestations contestées.
- Un animal cause un dommage pendant une garde.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Bilan d'exécution — 17 octobre 2026

- [Découpage du domaine](dom-033-annexes/dom-033-decoupage-animaux.md) :
  nom cible `animal-legal` conservé (`judge-fr-eu-animal-legal`), qualification
  progressive, contrat d'installation autonome, références et sources à vérifier.
- Sept suites `proposee`, ANM-001 à ANM-007 : acquisition de chien,
  adoption associative de chat, facture de pension de chien, dommage matériel
  pendant garde privée, état allégué après vente, incident/signalement de
  chien et qualification d'une cession d'autre espèce. ANM-001 est la première
  tranche proposée ; elle créera seule le socle et le paquet si sélectionnée.
- [Vérification documentaire](dom-033-annexes/dom-033-verification.md) des
  trois scénarios de la story et des cas limites ; liste des preuves par critère.
- Matrice BASE-003 et entrée S-35 actualisées ; famille ANM ajoutée au
  générateur d'état et index régénéré.
- [Résultats des contrôles](dom-033-annexes/dom-033-resultats.json) :
  structure des propositions, dépendances, liens, format, index et absence
  de création de paquet, séparés de la relecture du routage.

Fichiers du lot : présente story, trois annexes (découpage, vérification,
relevé JSON), sept suites ANM, ligne animaux de BASE-003, ligne S-35,
`backlog/etat.py` et `backlog/ETAT.md`. Lot limité à `backlog/`, sans entrée NOTICE.

**Portée :** cadrage documentaire et contrôles statiques ; aucune source
juridique externe ouverte ni règle actuelle validée. Aucun plugin créé,
skill exécuté ou paquet installé. Les scénarios métier des futures suites
restent à exécuter lors de leur sélection. La relecture est prise en charge
par l'utilisateur conformément à AGENTS.md et CLAUDE.md, sans déclarer sa
relecture faite ni une compréhension vérifiée. Détail et limites dans la
vérification liée ci-dessus.

