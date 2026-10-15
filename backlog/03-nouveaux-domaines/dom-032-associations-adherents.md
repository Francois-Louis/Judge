---
id: DOM-032
titre: "Cadrer un plugin associations et droits des adhérents"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-032 — Cadrer un plugin associations et droits des adhérents

## Objectif

Aider membres, bénévoles et petites associations à comprendre leurs statuts, décisions et engagements.

Nom de plugin proposé : `association-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire statuts, règlement, convocation, vote ou décision d'exclusion.
- Préparer une demande d'accès à une information ou une contestation interne.
- Distinguer cotisation, prestation payante, rôle bénévole et responsabilité de dirigeant.

## Qualification et frontières

Statut et siège de l'association, qualité du demandeur, documents internes, type de paiement, décision et dates.

La relation associative est ici ; le service vendu peut relever de DOM-001, le salarié du plugin travail et l'accident de DOM-035. Le sport, la culture et les loisirs sont des cas à qualifier, pas un régime unique.

## Sources à prévoir et vérifier

Loi du 1er juillet 1901, régime local le cas échéant, Code civil et textes sectoriels selon l'activité ; sources officielles de la vie associative.

- [Associations.gouv.fr](https://www.associations.gouv.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une décision d'exclusion et les règles internes invoquées, pour préparer une demande d'explication.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Association, société commerciale, fédération et régime local sont distingués ; la qualification d'une somme ne dépend pas uniquement de son intitulé.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un adhérent est exclu sans explication fournie.
- Une assemblée prend une décision contestée.
- Un club conserve une somme que l'usager assimile à une cotisation.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

