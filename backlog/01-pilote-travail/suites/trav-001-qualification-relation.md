---
id: TRAV-001
titre: "Qualifier une relation de travail proposée"
statut: terminee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-001 — Qualifier une relation de travail proposée

## Objectif

Une personne envisage une prestation ou un recrutement en France, avant tout début d'exécution.

Résultat : Tableau faits/critères/sources/risques et pièces à demander, sans choix automatique du statut.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : worker-classification.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Description des tâches, contrôle exercé, moyens, rémunération, autonomie, durée, acteurs et lieux/dates.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Retirer ABC, IRS, W-2/1099 et la promesse vendor/SOW plus propre ; rechercher la qualification réelle, distinguer qualification sociale et objet du contrat.

Sources primaires à rechercher : Code du travail, textes sociaux et jurisprudence officielle sur subordination ; cadres prestation, intérim et portage selon les faits.
Ces pistes sont **non vérifiées pour cette story**. Lire les dispositions,
versions et transitions applicables lors de l'implémentation ; conserver
le relevé des accès et réserves BASE-005. Utiliser les voies officielles
alternatives de BASE-010 si une page web échoue, sans confondre lecture et validation.

Charger la méthode locale versionnée et embarquer les références utiles.
Conserver la frontière de stockage BASE-008 ; nommer les accès externes
nécessaires/optionnels et prévoir la sortie utile si la recherche reste empêchée.

## Critères d'acceptation

- [x] Le résultat défini ci-dessus est observable sur le cas normal ci-dessous. Observé en client sur pièce fictive (T01), relu par le rédacteur.
- [x] La limite significative est traitée sans règle américaine de remplacement ni conclusion non établie. Observé en client sur pièce fictive (T02), relu par le rédacteur.
- [x] Règles collectives, statut réel, territoire et versions déterminants sont établis ou réservés explicitement. Observé sur pièces fictives (T01, T03), relu par le rédacteur.
- [x] Sources et données sont traçables ; le paquet isolé ne requiert aucun fichier voisin du dépôt. Copie détachée chargée seule par `--plugin-dir`, client non isolé.
- [ ] Une personne sans formation juridique comprend ce qui est établi, les pièces à demander et la prochaine démarche. Compréhension non observée ; relecture prise en charge par l'utilisateur, non bloquante pour la clôture (décision du 17 octobre 2026).
- [x] Le périmètre adapté et le reste non adapté sont explicitement distingués.

## Vérification

- Cas normal : Projet de prestataire intégré à une équipe : chaque facteur est relié aux faits et sources.
- Limite : Relation déjà exécutée : orientation distincte, pas de remédiation improvisée ni simple bannière autorisant des conclusions rétrospectives.

Exécuter sur pièces fictives, garder sorties, ressources lues et résultats
par couche BASE-006 ; faire reformuler par un lecteur non juriste.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.

## Hors périmètre

Audit du passé, contrat de prestation complet, cotisations et fiscalité chiffrées.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.

## Implémentation du 17 octobre 2026

Plugin `employment-legal` `0.3.0`. `worker-classification` est réécrit pour un
projet en France avant exécution : barrière de début d'exécution sans bannière
« proceed anyway », qualification des acteurs et du cadre, critères lus
(qualification par les faits, subordination, service organisé, présomption
L8221-6, objet du contrat, prêt de main-d'œuvre et portage), tableau
facteur/faits/critère et source/indication/pièce, risques sans chiffrage,
pièces et interlocuteur, phrase finale BASE-013. Retirés : tests ABC et
économiques, IRS § 530, W-2/1099, PAGA, « joint employer », préférence pour le
vendor/SOW et porte d'avocat obligatoire.

Fichiers : [skill](../../../employment-legal/skills/worker-classification/SKILL.md),
[repères embarqués 1.0.0](../../../employment-legal/references/worker-classification-fr.md),
modèle de profil (exception sans profil), README et NOTICE du plugin,
manifeste et marketplace, README et NOTICE racine, version attendue du test
BASE-008. Méthode BASE-005 locale `1.0.0` inchangée et identique à la source.

Sources : 25 articles du Code du travail lus sur le Code du travail numérique,
cinq décisions de la Cour de cassation lues dans le fonds CASS de la DILA après
un refus HTTP 403 de Légifrance, règlement Rome I (art. 8) et directive
2024/2831 (art. 5 et 29) sur EUR-Lex ; [relevé](trav-001-annexes/trav-001-sources-lues.json).
Accès externes : lecture de publications officielles, optionnelle ; sans
elle, la note relève faits et pièces et réserve les conclusions dépendantes.

Recette : [vérification par couche](trav-001-annexes/trav-001-verification.md),
[pièces fictives](trav-001-annexes/trav-001-pieces-fictives.md),
[sorties](trav-001-annexes/trav-001-sorties.md),
[journaux](trav-001-annexes/trav-001-resultats.json). Trois scénarios
exécutés en client, deux défauts corrigés puis confirmés (calcul de seuil,
reformulation remplie par le client).

État avant la décision ci-dessous : `a-verifier`, uniquement pour la
reformulation par un lecteur non juriste non faite.

### Clôture sur décision de l'utilisateur — 17 octobre 2026

Story `terminee` : l'utilisateur prend en charge toute la relecture et
autorise la clôture des stories ouvertes pour ce seul motif
([décision](../../decisions-2026-10-17.md)). La reformulation par un lecteur
non juriste reste non exécutée et son critère reste non coché ; aucune
relecture indépendante ni compréhension observée n'est déclarée acquise.
Les résultats et limites de la recette ci-dessus sont conservés.

## Portée

Comportement observé sur pièces fictives dans un client réel non isolé ; voir
la [vérification](trav-001-annexes/trav-001-verification.md). Pas de
relecture juridique indépendante. Les sources citées par le client au-delà des
repères embarqués n'ont pas été relues. Restent non adaptés : audit d'une
relation exécutée (TRAV-025), intérim (TRAV-024), contrat de prestation
complet, cotisations et fiscalité, emploi public, territoires hors L1511-1.
