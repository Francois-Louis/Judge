# DOM-039 — Couverture des demandes de cadrage

Relevé du 17 octobre 2026. Le tableau rattache les exigences reçues à des
stories **proposées**, pas à des fonctions disponibles. Les matrices sources
restent des relevés historiques ; aucun taux, réforme, délai ou chiffre du
texte utilisateur n'est adopté. Le [découpage](dom-039-decoupage-independants.md)
fixe les frontières et les sources futures, les suites détaillent les pièces.

Sources de besoin : [DOM-039](../dom-039-micro-entreprise.md),
[formalités — 100 points](../../02-plugins-existants/exist-002-annexes/exist-002-frictions-utilisateurs.md),
[données personnelles — point 29](../../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md),
[allocations et aides](../dom-012-annexes/dom-012-frictions-utilisateurs.md).
Les numéros d'une source ne sont pas ceux d'une autre.

## Besoins initiaux et compléments

| Demande DOM-039 | Suite(s) | Séparation de résultat |
|---|---|---|
| Courrier Urssaf, montants, stade | IND-001 | Recopie et lecture ; aucun calcul ou recours dans la première tranche |
| Déclaration, dépassement, changement | IND-010 à IND-019, IND-042 | Rapprochement/correction, calendrier, zéro, plafonds micro, TVA, options, déclaration annuelle et calculs séparés |
| Cotisations, impôts courants, CFE/TVA | IND-009, IND-019, IND-023 à IND-027, IND-042 | Calcul de cotisations/ACRE/libératoire borné ; CFE/TVA sur pièces sans liquidation |
| Cumul salarié/allocataire | IND-041 | Questions sur activité ici, contrat chez travail, décision de caisse DOM-012 |
| Contrôle et suites | IND-032, IND-033, IND-001, IND-034 | Avis, observations, mise en demeure puis recours propre ; pas de régime commun |
| Création, registres et publicité | IND-002 à IND-008, IND-039, IND-040 | État, pièces, donnée, statut, prérequis, ACRE et deux procédures de diffusion |
| Cessation et recours | IND-022, IND-028 à IND-038 | Pas d'extinction déduite de radiation ni recours remplacé par médiation |

## Points formalités attribués à DOM-039

La table inclut les relais vers DOM-039, sans réattribuer les points des
sociétés ou du fisc. « À cadrer ailleurs » reste une lacune explicite.

| Points de la matrice formalités | Stories IND | Résultat et limite |
|---|---|---|
| 5, 7 | IND-001, IND-032 | Acte authentique et contrôle distincts d'imitation commerciale COM-019 |
| 11, 13, 20, 96, 97 | IND-002 | État et autorité ; paiement, coût officiel et preuve distincts ; recours contre rejet encore hors tranche |
| 12 | IND-003 | Pièces de régularisation et notification |
| 14, 15, 19, 24, 29, 30 | IND-004 | Une donnée à qualifier/corriger ; domiciliation contractuelle COM-020 |
| 16 | IND-005 | Questions qualitatives sur statut, société/IS chez leurs propriétaires |
| 17 | IND-006 | Qualification des prérequis, vérification métier chez le secteur |
| 21 | IND-039, IND-040 | Sirene, RNE/acte et copies privées séparés |
| 22 | IND-006 pour relais seulement ; PI-002 garde la recherche | L'immatriculation ne vaut pas protection de marque ; aucune recherche concurrente ici |
| 23 | IND-007, IND-008, IND-009 | Dépôt/éligibilité, lecture décision, application chiffrée ACRE distincts |
| 33 | IND-013 | Zéro CA et déclaration à zéro non assimilés |
| 34 | IND-010, IND-011 | Rapprocher puis préparer correction ciblée |
| 35, 36 | IND-012 | Première échéance, périodicité, heure et report vérifiés séparément |
| 37 | IND-017 | Déclaration fiscale annuelle distincte des déclarations sociales |
| 38 | IND-018, IND-019 | Option et calcul libératoire séparés ; pas de simulation globale |
| 39, 40, 41, 42 | IND-014, IND-015, IND-016 | Plafonds, proratas, franchise et changements séparés |
| 43 | IND-020 | Obligation légale distincte du contrat DOM-004 |
| 44 | IND-010, IND-042, IND-009 | Ventilation, calcul ordinaire, application ACRE propre |
| 45 | IND-022, IND-013 | Inactivité et obligations, sans cessation présumée |
| 46, 56 | IND-023 | Déclaration initiale et pièces d'accès/dépôt, sans connexion au compte |
| 47, 50 | IND-024 | Avis, commune/local et date de mise à disposition, aucune exonération déduite |
| 48, 49, 51, 52 | IND-025 | Un fondement d'exonération/réduction par dossier ; réclamation formelle DOM-011 |
| 53, 54 | IND-015, IND-026, IND-027 | Franchise/date, opération intérieure, opération internationale et douane distinctes |
| 59 | IND-026 pour fiche de faits seulement | Facturation électronique et e-reporting gardés par DOM-011 ; aucune implémentation concurrente |
| 64, 69, 70 | IND-021 | Inventaire ciblé de livres/pièces/conservation, sans tenue comptable ni déductibilité générale |
| 79, 80 | IND-022, IND-028 | Pause et cessation définitive distinguées |
| 81 | IND-029, IND-030 | Dernière période sociale et dossier d'un impôt séparés |
| 86, 87 | IND-028, IND-031 | Dette et radiation distinctes ; patrimoine/difficultés vers SOC-027 à cadrer |
| 88, 89, 90 | IND-001, IND-034, IND-038 | Lecture, recours et médiation séparés ; brouillon/messagerie ne valent pas recours |
| 91, 92 | IND-034, IND-035 | CRA et opposition à contrainte, ENF-001 pour identification de l'acte |
| 93, 94 | IND-011, IND-036 | Correction et remise gracieuse propres ; droit à l'erreur sans immunité promise |
| 95, 98 | IND-037, IND-038 | Échéancier et médiation sans effet sur les délais présumé |

## Données personnelles et allocations

| Source et points | Suite(s) ou relais | Contrôle prévu |
|---|---|---|
| Données personnelles, 29 | IND-039, IND-040 ; PRV-028/029 | Domicile repris dans deux annuaires après changement de diffusion : registre et copies privées, aucune disparition garantie |
| Allocations, 66, 67 | IND-010, IND-041 ; prestations chez DOM-012 | Revenus par activité, assiette et abattement propres à chaque administration ; jamais d'abattement doublé |
| Allocations, 73 à 80 et D07/CR01 | IND-007, IND-008, IND-009 | Critères, dépôt/réception, décision puis calcul ACRE ; réforme alléguée et transitions à vérifier, aucun délai reçu adopté |
| Allocations, 92 à 95/CR04 | IND-010, IND-041 ; DOM-012, sociétés si SASU | CA/bénéfice/rémunération distingués ; régularisation ARE/CAF gardée par caisse, zéro salaire n'est pas zéro obligation |
| Allocations, 108/CR08 | IND-031, IND-029 ; CR07 DOM-012 pour ATI | Dernières périodes et régularisation après radiation sans dette effacée ni ATI acquise |

La liste de couverture est documentaire. La [vérification](dom-039-verification.md)
consigne les parcours relus et les contrôles exécutés ; les scénarios des
suites seront exécutés lors de leurs implémentations.
