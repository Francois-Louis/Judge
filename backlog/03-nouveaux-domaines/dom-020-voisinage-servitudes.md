---
id: DOM-020
titre: "Cadrer un plugin voisinage et servitudes"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-020 — Cadrer un plugin voisinage et servitudes

## Objectif

Aider à documenter les conflits de voisinage et à choisir une démarche proportionnée.

Nom de plugin proposé : `neighbourhood-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Préparer une chronologie et les pièces de nuisances sonores, fumées ou autres troubles allégués.
- Lire une demande concernant arbres, clôture, mitoyenneté, limite ou passage.
- Préparer un échange écrit, une conciliation ou un dossier contentieux selon l'objet.

## Qualification et frontières

Qualité des occupants/propriétaires, localisation, titre, plan et éventuelle servitude, dates, récurrence, preuves obtenues et échanges.

Le conflit entre voisins est ici ; permis et décisions publiques vont en DOM-019, pollution en DOM-030 et règles propres à la copropriété en DOM-018.

## Sources à prévoir et vérifier

Code civil, textes nationaux et locaux pertinents, règles de preuve et de procédure, décisions utiles selon la situation.

- [Service Public](https://www.service-public.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Préparer une réclamation factuelle pour une nuisance répétée, en distinguant faits documentés et interprétations.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Les mesures techniques, les règles locales et les droits inscrits dans un titre sont prévus comme vérifications distinctes ; aucune action matérielle unilatérale n'est suggérée par défaut.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un voisin revendique un droit de passage.
- Une haie ou une clôture fait l'objet d'un désaccord.
- Des nuisances récurrentes sont alléguées sans preuve datée.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

