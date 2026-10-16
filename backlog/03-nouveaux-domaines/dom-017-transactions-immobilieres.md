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

## Complément des frictions logement — 16 octobre 2026

Points 55, 69, 75, 92, 107–116 de la [matrice logement](dom-006-annexes/dom-006-frictions-utilisateurs.md).

Découper avant-contrat et condition de prêt ; rétractation et complétude documentaire ; surface Carrez ; annexes, droits réels et servitudes ; comptes et travaux de copropriété lors de vente ; défauts dissimulés et clause d'exonération. Pour chaque tâche : annonce, promesse/acte, notifications, titres, règlement/état descriptif, PV/appels, diagnostics, mesurage et rapports strictement utiles ; sortie sous forme de comparaison sourcée, chronologie et questions au notaire ou avocat. Distinguer exigibilité opposable au syndicat et accord vendeur/acquéreur. La condition de prêt se confronte aux demandes/refus réels, sans la confondre avec l'analyse bancaire. Carrez n'est pas la surface locative LOG-015 ; la jouissance exclusive n'est pas une propriété. Absence de notification ou de document : réserver point de départ ; défaut ou peinture récente ne suffit pas à prouver connaissance et dissimulation. Urbanisme DOM-019, droits privés DOM-020, comptes DOM-018 restent distincts.

- [ ] Le futur découpage attribue à chaque tâche ses entrées, sortie, sources, limites et scénarios, y compris les voies urgentes distinctes.

Scénarios **attendus, non exécutés** : Promesse avec condition de prêt, pièces de copropriété incomplètes et jardin seulement en jouissance : trois vérifications séparées avant engagement, sans délai de rétractation inventé. Après vente : infiltration et clause d'exonération, préserver preuves et conditions de l'action sans garantie d'annulation.
Les textes, versions, transitions, seuils et échéances seront vérifiés sur
sources officielles lors des implémentations. Ce complément ne termine pas
le cadrage, ne crée aucun plugin et n'exécute aucune démarche externe.
