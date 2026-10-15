---
id: DOM-017
titre: "Cadrer un plugin d'achat et de vente immobilière"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-017 — Cadrer un plugin d'achat et de vente immobilière

## Objectif

Aider acheteurs et vendeurs à lire les documents et à repérer les risques d'une transaction immobilière.

Nom de plugin proposé : `real-estate-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Examiner annonce, mandat, offre, promesse ou compromis selon le stade.
- Préparer les vérifications sur conditions suspensives, diagnostics, frais et pièces communiquées.
- Organiser un dossier de non-conformité alléguée ou de désaccord après la vente.

## Qualification et frontières

Qualité des parties, type de bien, localisation, neuf/ancien/vente en l'état futur d'achèvement, dates de notification, financement et actes déjà signés.

L'achat et la vente sont ici ; le bail reste en DOM-006, les travaux en DOM-015, la copropriété en DOM-018, le prêt en DOM-004 et l'urbanisme en DOM-019.

## Sources à prévoir et vérifier

Code civil, Code de la construction et de l'habitation, Code de la consommation selon le contrat, règles de l'intermédiation et sources officielles du logement.

- [Service Public — logement](https://www.service-public.gouv.fr/particuliers/vosdroits/N19808)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire un avant-contrat pour l'achat d'un logement ancien par un particulier, avec pièces et hypothèses explicites.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] Le cadrage distingue offre, avant-contrat et acte de vente ; il n'applique pas la même faculté de retrait à tous les actes et acquéreurs.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une agence facture des frais dont l'acheteur conteste la base.
- Le financement n'est pas obtenu après signature.
- Un défaut est découvert après la remise des clés.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

