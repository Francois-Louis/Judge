---
id: TRAV-002
titre: "Vérifier le minimum de rémunération d'un salarié"
statut: terminee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-002 — Vérifier le minimum de rémunération d'un salarié

## Objectif

Un salarié veut comprendre si son salaire de base respecte le minimum applicable pour une période donnée.

Résultat : Comparaison lisible salaire/période/minima vérifiés, composantes retenues et questions de régularisation.

## Périmètre

Plugin principal : `employment-legal` **0.4.0**, entrée adaptée :
`/judge-fr-eu-employment-legal:wage-hour-qa`. Skill réécrit, références
embarquées, exception de profil, README/manifeste/marketplace et NOTICE
actualisés ; méthode BASE-005 locale `1.3.0` inchangée.

Entrées nécessaires : Contrat, bulletin anonymisé, fonctions réelles, classification, durée du travail, activité de l'employeur et documents collectifs.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Séparer classification conventionnelle et exemption US ; déterminer base comparable, période et éléments inclus selon chaque minimum, sans produire une paie complète.

Sources primaires à rechercher : Code du travail et textes de revalorisation ; CCN, grilles de branche et accords effectivement applicables, versions datées.
Les lectures et réserves sont consignées dans le
[relevé des sources](trav-002-annexes/sources-lues.json) et les
[repères embarqués](../../../employment-legal/references/minimum-remuneration-fr.md).
Exemple de branche documenté : IDCC 1486, grille ETAM 2.3/355, article 7.1
(garantie annuelle et planchers mensuels distincts). Cette grille ne préjuge
pas la convention applicable au dossier. Les autres conventions et régimes
appellent une recherche propre ; aucun barème universel.

Charger la méthode locale versionnée et embarquer les références utiles.
Conserver la frontière de stockage BASE-008 ; nommer les accès externes
nécessaires/optionnels et prévoir la sortie utile si la recherche reste empêchée.

## Critères d'acceptation

- [x] Le résultat défini ci-dessus est observable sur le cas normal ci-dessous.
- [x] La limite significative est traitée sans règle américaine de remplacement ni conclusion non établie.
- [x] Règles collectives, statut réel, territoire et versions déterminants sont établis ou réservés explicitement.
- [x] Sources et données sont traçables ; le paquet isolé ne requiert aucun fichier voisin du dépôt.
- [ ] Une personne sans formation juridique comprend ce qui est établi, les pièces à demander et la prochaine démarche.
- [x] Le périmètre adapté et le reste non adapté sont explicitement distingués.

## Vérification

- Cas normal : Salaire fixe et classification documentés : comparaison reproductible.
- Limite : CCN ou temps de travail inconnu : calcul définitif réservé, pièces utiles nommées.

Huit scénarios fictifs exécutés dans le client Claude Code 2.1.301 sur un
paquet détaché et rejoués après corrections ; essai M02 avec WebFetch puis
M09 ciblé sur l'extension, également rejoué après correction.
[Pièces et attendus](trav-002-annexes/fixtures.json),
[recette par couche](trav-002-annexes/verification.md),
[sorties et appels finaux](trav-002-annexes/executions-finales-2026-10-17/results.json),
[essai web final](trav-002-annexes/executions-web-finales-2026-10-17/results.json).
Le compte/HOME du client restent réels : copie détachée et outils bornés,
pas de bac à sable du système d'exploitation. Aucun lecteur non juriste n'a
reformulé les sorties ; le critère de compréhension reste non coché.

## Hors périmètre

Rappels d'heures, paie complète, charges, net garanti et prescription de créance.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Implémentation du 17 octobre 2026 : comparaisons distinctes SMIC/branche,
éléments inclus/exclus et périodes propres, fonctions réelles et classification
documentée, dates/territoires/statuts établis ou réservés, formules et arrondis,
pièces et questions de régularisation au service paie. Profil facultatif,
frontière BASE-008 conservée, aucun envoi ni écriture automatique. Retirés :
FLSA, regular rate, exemption US, dommages doublés et prescription américaine.

M01 : 2 200 € de base, SMIC janvier 2026 de 1 823,03 €, plancher mensuel
conventionnel de 1 942,75 €, frais réels de 150 € exclus. M02 : base de
1 900 €, soit +76,97 € face au SMIC mais −42,75 € face au plancher de branche ;
pas de rappel mensuel automatique de 145 €. Garantie annuelle réservée sur un
seul mois ; avec treizième mois (M07), plancher distinct de 1 881,40 €.
Ces comparaisons sont bornées aux pièces et aux réserves d'applicabilité.

Références et contrôles : voir la [vérification](trav-002-annexes/verification.md).
Les huit articles du Code du travail ont aussi été contrôlés dans le stock
LEGI et ses 464 lots postérieurs jusqu'au 16 octobre 2026 : aucune version
future ni fin de vigueur trouvée dans ce fonds ; dates de début comparées aux
reproductions CDTN. Ce résultat documentaire ne certifie pas l'applicabilité.
La relecture juridique et de compréhension est prise en charge par
l'utilisateur selon les consignes du 17 octobre 2026 ; elle n'est pas déclarée
effectuée et aucun résultat de compréhension n'est inventé.

## Complément des frictions travail — 16 octobre 2026

**Minimum et fonctions réelles.** Pour les points 3.01–02 et 5.09, TRAV-027 documente la classification réelle avant comparaison. Confronter SMIC et minimum conventionnel sur des bases et périodes propres ; prime et remboursement de frais ne sont pas interchangeables. Ajouter un cas où le SMIC est respecté mais la grille ne l’est pas. TRAV-036 garde les autres anomalies de rémunération, TRAV-059 les comparateurs, TRAV-054 le calendrier de créance ; l’exclusion de la paie complète et de la prescription calculée reste maintenue.

Rattachement complet : [matrice des frictions](../pilote-001-annexes/pilote-001-frictions-utilisateurs.md).
Ajouts intégrés : fonctions réelles, frais distincts des primes, cas M02
au-dessus du SMIC mais sous le plancher conventionnel ; phrase finale BASE-013
et renfort si urgence. La compréhension par un participant n'est pas observée.
Portée de l’intégration et lectures préliminaires :
[vérification](../pilote-001-annexes/pilote-001-frictions-verification.md).
