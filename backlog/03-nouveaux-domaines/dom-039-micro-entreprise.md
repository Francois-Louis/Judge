---
id: DOM-039
titre: "Cadrer un plugin micro-entreprise et travail indépendant"
statut: terminee
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

Cadrage réalisé le 17 octobre 2026 : [découpage en 42 suites proposées](dom-039-annexes/dom-039-decoupage-independants.md),
[couverture des demandes et compléments](dom-039-annexes/dom-039-couverture-demandes.md),
[vérification documentaire](dom-039-annexes/dom-039-verification.md).
Les mentions « à découper » des compléments datés ci-dessous décrivent le
besoin reçu le 16 octobre ; le tableau de couverture précise son traitement
actuel et les tâches laissées hors périmètre.

## Tâches métier à découper

- Lire un courrier de l'URSSAF (cotisations, régularisation, majorations, mise en demeure) et repérer période, montant et stade.
- Vérifier une déclaration de chiffre d'affaires, un dépassement de seuil ou un changement de régime.
- Comprendre l'imposition de l'activité (versement libératoire, cotisation foncière des entreprises, TVA) sans calcul non sourcé.
- Préparer les questions sur le cumul de l'activité avec un emploi salarié, une indemnisation chômage ou des aides ; la décision de France Travail ou d'une caisse sur ce cumul relève de DOM-012.
- Lire un avis de contrôle de l'URSSAF, une lettre d'observations ou une mise en demeure qui suit un contrôle, et préparer la réponse.

## Qualification et frontières

Statut (micro-entrepreneur, entreprise individuelle, autre), activité,
date de création, chiffre d'affaires déclaré, organismes, courriers reçus et
stade de chaque procédure.

L'activité indépendante est ici. Impôts du foyer hors activité → DOM-011 ;
prestations de la CAF, minima sociaux, allocation chômage et aides de France
Travail à la création (aide en capital, maintien de l'allocation) → DOM-012,
l'ACRE restant ici ; retraite → DOM-036 ;
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

- [x] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios — 42 propositions IND-001 à IND-042.
- [x] Un utilisateur peut partir de son courrier sans connaître le nom du régime — parcours documentaire fictif A ; compréhension par un utilisateur non observée.
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons avec DOM-011, DOM-012 et commercial — contrat prévu, installation non exécutée dans ce cadrage.
- [x] Aucun montant de cotisation ou d'impôt n'est calculé sans source lue et date établie — aucun calcul livré ; calculs futurs séparés et conditionnés aux sources/version/paramètres.
- [x] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici — préalable satisfait, aucune tranche sélectionnée.

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

## Complément — formalités des entreprises, 16 octobre 2026

La [matrice des 100 frictions](../02-plugins-existants/exist-002-annexes/exist-002-frictions-utilisateurs.md) ajoute les tâches candidates ci-dessous. Elles restent **à découper**, avec une story par résultat borné ; ce complément ne termine pas DOM-039 et ne lance pas de plugin.

| Groupe de points | Tâches à séparer et résultats attendus |
|---|---|
| 11–15, 19–21, 24, 29–30, 96–97 | Lire le stade d'une formalité d'EI ; préparer les pièces d'une régularisation ; qualifier une donnée APE/activité/établissement à corriger. Identifier opérateur technique et autorité compétente selon la donnée ; reçu de paiement et validation restent séparés. |
| 16–17, 22–23 | Préparer les questions sur le choix de régime/statut ; vérifier les prérequis d'une activité avec son secteur ; lire la situation d'une demande ACRE. La recherche de marque relève de PI-002. |
| 33–36, 44 | Rapprocher une déclaration sociale avec les encaissements, activités et accusés ; préparer une régularisation ciblée. Séparer déclaration à zéro, première échéance, périodicité et report des jours non ouvrés. Aucun taux ou calendrier repris du texte sans lecture officielle. |
| 37–42 | Lire une option micro-fiscale ou versement libératoire ; qualifier séparément plafond micro, franchise TVA, dépassement, prorata et changement de régime. Découper chaque contrôle et calcul ; aucune comparaison chiffrée générale de statuts dans la première tranche. |
| 43, 45, 64, 69–70 | Vérifier l'obligation de compte dédié selon les faits ; dresser les pièces de livres/recettes et d'archivage ; distinguer inactivité et cessation. Contrat bancaire → DOM-004 ; comptabilité tenue par un professionnel → DOM-041 pour la relation. |
| 46–54, 56 | Lire un avis CFE de l'indépendant ; préparer une demande d'explication ou d'exonération ; qualifier sa TVA et ses opérations internationales. Demander recettes, périodes de référence, commune, local, métier réel, salariés, options et dates avant calcul. |
| 79–81, 86–87 | Qualifier cessation temporaire/définitive d'EI ; rapprocher déclaration de cessation et radiation ; préparer les dernières périodes sociales/fiscales. Sort des dettes et patrimoine → SOC-027 à cadrer ; aucune extinction déduite de la radiation. |
| 88–95, 98 | Séparer lecture de décision, contrôle, CRA, opposition à contrainte, remise de majorations, échéancier et médiation Urssaf. Chaque recours exige sa story et son régime propre ; ni messagerie ni médiation ne remplacent un recours par déduction. |

Qualifier EI et régime micro séparément, date de création, activité réelle et mixte, pays des opérations, qualité de l'organisme, nature de l'acte et preuve de réception. Le dépôt d'une formalité, la non-diffusion SIRENE, l'occultation d'actes et la réutilisation privée d'une adresse sont des questions distinctes ; les droits sur un traitement privé relèvent d'EXIST-003.

Frontière fiscale : conserver ici les impôts courants de l'activité de l'indépendant prévus au cadrage ; transmettre à DOM-011 la procédure de contrôle et le contentieux fiscal (réclamation formelle, sursis et recours), avec faits, périodes, pièces et questions déjà établis. Facturation électronique et e-reporting → exigences de cadrage DOM-011 ; aucun double calcul chez deux propriétaires.

Les recours sociaux d'un employeur société ne sont pas couverts par DOM-039 ; TRAV-020 ne fait que lire les notifications DSN et orienter. Leur lecture de décision, CRA, opposition à contrainte et médiation restent à découper dans le domaine travail. Une contrainte reçue par un indépendant appelle aussi l'identification de l'acte ENF-001, avec régime spécial à vérifier, pas un délai générique d'exécution.

Scénarios de cadrage à prévoir : première déclaration sans accusé ; déclaration à zéro pénalisée ; activités mixtes avec encaissements décalés ; franchise TVA confondue avec micro ; CFE d'un artisan sans local ; ACRE dont l'échéance annoncée n'est pas sourcée ; cessation d'EI sans déclarations finales ; contrainte reçue alors qu'une médiation est en cours. Résultats attendus : pièces, périodes, branche propre et prochaine démarche, sans traiter ces consultations dans le cadrage. Portée et contrôles : voir la matrice.

## Complément des frictions données personnelles — 16 octobre 2026

Le point 29 de la [matrice données personnelles](../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md) exige une tâche de non-diffusion/occultation des données de l'EI encore à découper : qualifier registre, acte, donnée, statut du demandeur, date et canal officiel. Distinguer Sirene/RNE, information de registre et copie privée ; procédures et effets à vérifier. PRV-028 prépare la demande à un annuaire privé, PRV-029 au moteur, sans disparition des copies garantie. Scénario attendu : domicile servant d'adresse professionnelle repris dans deux annuaires après changement de statut de diffusion. Portée et contrôles : voir la matrice.

## Complément des frictions allocations et aides sociales — 16 octobre 2026

Points 66–67, 73–80, 92–95 et 108 de la [matrice](dom-012-annexes/dom-012-frictions-utilisateurs.md).
Tâches candidates à découper, sans sélection de tranche :

- ACRE (CR01) : qualifier statut, date de création/reprise, antécédents, demande et accusé ; lire décision et période/taux de cotisations, puis préparer demande d'explication ou contestation propre. Séparer éligibilité/dépôt, suivi et calcul ; aucune réforme 2026 ni délai du guide adopté sans texte/version/transitions.
- Rapprocher CA par activité, bénéfice et rémunération avec déclarations et pièces ; règles de prestation CAF ou ARE chez DOM-012, sans assiette ou abattement commun aux trois administrations.
- Après cessation : dernières périodes, déclarations, régularisation et notification ; aucune extinction des cotisations déduite de la radiation. ATI et attestation de non-viabilité à coordonner avec CR07 chez DOM-012.

Entrées : régime réel/micro, activité mixte éventuelle, création/début réel,
CA encaissé, demandes, courriers, cotisations et réception. Résultat :
chronologie, écarts de pièces et brouillon ciblé, sans tenue comptable.
Sources à ouvrir : CSS, textes ACRE et transitions, Urssaf et formalités.
Cas attendus : création autour d'une réforme et accusé absent ; cessation
avec régularisation reçue après radiation. Scénarios non exécutés ;
[portée et contrôles](dom-012-annexes/dom-012-frictions-verification.md).

## Bilan d'exécution — 17 octobre 2026

- [Découpage](dom-039-annexes/dom-039-decoupage-independants.md) : 42 propositions
  IND-001 à IND-042, quatre rangs, toutes `proposee` ; première tranche proposée
  IND-001, lecture factuelle d'un courrier Urssaf sans calcul ni recours.
- Formalités EI, prérequis, ACRE (demande, décision, calcul), déclarations,
  seuils micro et TVA, options fiscales, CFE, opérations TVA, cessation,
  contrôle et recours, diffusion Sirene/occultation RNE et cumul séparés.
  Chaque suite décrit entrées, sortie, pièces, sources futures, fichiers,
  limites et scénarios nominal/limite/manquant/sans source/transfrontalier.
- [Couverture](dom-039-annexes/dom-039-couverture-demandes.md) des exigences
  initiales et des trois compléments, avec relais explicites : ACRE/CR01
  ici, ARCE/ARE/ATI chez DOM-012, régularisation CR08 ici ; fiscalité courante
  d'activité ici, contrôle/contentieux fiscal et facturation électronique
  chez DOM-011. Les lacunes et tâches laissées hors tranche sont nommées.
- [Vérification](dom-039-annexes/dom-039-verification.md) : quatre cas initiaux,
  huit cas du complément et onze cas complémentaires, parcours documentaires
  A à W ; aucune consultation résolue et aucun délai ou montant juridique fixé.
- Contrat de paquet autonome et recette BASE-006/008 prévus ; références
  métier locales, copie BASE-005 versionnée, aucun connecteur ni profil requis.
  Ligne BASE-003 et famille IND du générateur mises à jour, index régénéré.
- [Contrôles reproductibles](dom-039-annexes/dom-039-controles.py) et
  [relevé](dom-039-annexes/dom-039-resultats.json) : structure, dépendances,
  cohérence du découpage, couverture, liens, format, index et absence de plugin.

Fichiers du lot : présente story, cinq annexes (découpage, couverture,
vérification, contrôleur et relevé), 42 suites IND, ligne BASE-003,
`backlog/etat.py` et `backlog/ETAT.md`. Lot limité à `backlog/`, sans entrée
NOTICE ni changement de version de plugin.

**Portée :** cadrage documentaire relu sur cas fictifs par l'agent de
maintenance et contrôles statiques exécutés ; aucune source juridique
externe ouverte, règle reçue validée, implémentation de skill, installation,
recette client ou démarche externe. La compréhension par un lecteur n'a
pas été observée. La relecture est prise en charge par l'utilisateur selon
la décision du 17 octobre 2026, sans être déclarée effectuée. Le préalable
PILOTE-003 est satisfait après BASE-011 ; les tests des futures suites
restent à exécuter lors de leur implémentation, aucune tranche sélectionnée.

## Complément des frictions douanes — 17 octobre 2026

Points 40–44 et 46 : préciser IND-027 pour import de biens, franchise, identification et déclaration TVA, ventes UE/OSS et obligations distinctes ; aucun seuil micro assimilé au seuil TVA ou douanier. DOU-004 qualifie EORI/rôle/régime et C20 EMEBI ; contrôle et contentieux fiscal restent DOM-011. Pièces : statut, flux/territoires, factures, identification, période et données déclarées. Cas : micro en franchise estimant l'import sans obligation fiscale ; paiement étranger bloqué après livraison, question bancaire vers BNK-014/019 selon contrat. Ces relais ne sont pas des fonctionnalités livrées ; autoliquidation, CA3 et migration EORI du guide restent à rechercher.

Exigences de la [matrice des 75 points](dom-009-annexes/dom-009-frictions-utilisateurs.md), sans sélection de tranche ni capacité annoncée comme livrée. [Portée et contrôles](dom-009-annexes/dom-009-frictions-verification.md).
