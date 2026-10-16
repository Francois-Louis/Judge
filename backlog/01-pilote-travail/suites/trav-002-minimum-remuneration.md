---
id: TRAV-002
titre: "Vérifier le minimum de rémunération d'un salarié"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-002 — Vérifier le minimum de rémunération d'un salarié

## Objectif

Un salarié veut comprendre si son salaire de base respecte le minimum applicable pour une période donnée.

Résultat : Comparaison lisible salaire/période/minima vérifiés, composantes retenues et questions de régularisation.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : wage-hour-qa.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Contrat, bulletin anonymisé, fonctions réelles, classification, durée du travail, activité de l'employeur et documents collectifs.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Séparer classification conventionnelle et exemption US ; déterminer base comparable, période et éléments inclus selon chaque minimum, sans produire une paie complète.

Sources primaires à rechercher : Code du travail et textes de revalorisation ; CCN, grilles de branche et accords effectivement applicables, versions datées.
Ces pistes sont **non vérifiées pour cette story**. Lire les dispositions,
versions et transitions applicables lors de l'implémentation ; conserver
le relevé des accès et réserves BASE-005. Utiliser les voies officielles
alternatives de BASE-010 si une page web échoue, sans confondre lecture et validation.

Charger la méthode locale versionnée et embarquer les références utiles.
Conserver la frontière de stockage BASE-008 ; nommer les accès externes
nécessaires/optionnels et prévoir la sortie utile si la recherche reste empêchée.

## Critères d'acceptation

- [ ] Le résultat défini ci-dessus est observable sur le cas normal ci-dessous.
- [ ] La limite significative est traitée sans règle américaine de remplacement ni conclusion non établie.
- [ ] Règles collectives, statut réel, territoire et versions déterminants sont établis ou réservés explicitement.
- [ ] Sources et données sont traçables ; le paquet isolé ne requiert aucun fichier voisin du dépôt.
- [ ] Une personne sans formation juridique comprend ce qui est établi, les pièces à demander et la prochaine démarche.
- [ ] Le périmètre adapté et le reste non adapté sont explicitement distingués.

## Vérification

- Cas normal : Salaire fixe et classification documentés : comparaison reproductible.
- Limite : CCN ou temps de travail inconnu : calcul définitif réservé, pièces utiles nommées.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Rappels d'heures, paie complète, charges, net garanti et prescription de créance.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.

## Complément des frictions travail — 16 octobre 2026

**Minimum et fonctions réelles.** Pour les points 3.01–02 et 5.09, TRAV-027 documente la classification réelle avant comparaison. Confronter SMIC et minimum conventionnel sur des bases et périodes propres ; prime et remboursement de frais ne sont pas interchangeables. Ajouter un cas où le SMIC est respecté mais la grille ne l’est pas. TRAV-036 garde les autres anomalies de rémunération, TRAV-059 les comparateurs, TRAV-054 le calendrier de créance ; l’exclusion de la paie complète et de la prescription calculée reste maintenue.

Rattachement complet : [matrice des frictions](../pilote-001-annexes/pilote-001-frictions-utilisateurs.md).
Les critères restent non cochés. Pour ces ajouts, appliquer BASE-013 : phrase
finale nommant le professionnel compétent et renfort en tête si urgence ou
procédure ; sources, paquet détaché, client et compréhension à vérifier selon
BASE-005/006. Portée de l’intégration et lectures préliminaires :
[vérification](../pilote-001-annexes/pilote-001-frictions-verification.md).
