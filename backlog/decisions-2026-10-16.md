# Décisions de l'utilisateur — 16 octobre 2026

Arbitrages rendus après les cadrages DOM-001 à DOM-005 et la livraison
LIV-001, en réponse aux questions de l'agent de maintenance. Chaque ligne
indique son effet dans le backlog. Ces décisions organisent le travail ; elles
ne valident aucune règle de droit.

## Livraison et dépôt

| Sujet | Décision | Effet |
|---|---|---|
| Clôture de LIV-001 | Accepter la recette BASE-011 : les fichiers de skill du lot 0.2.1 sont identiques à ceux recettés. | [LIV-001](04-livraison/liv-001-livrer-lot-borne.md) `terminee`, invocation sur l'artefact non exécutée et consignée. |
| Skills hérités dans le lot | Les garder, signalés comme non adaptés. | Lot inchangé. |
| Publication | Uniquement sur le dépôt de l'utilisateur `Francois-Louis/Judge`, jamais sur le dépôt d'origine. | Toute commande `gh` porte `--repo Francois-Louis/Judge` ; aucune PR vers l'origine. |
| Git | Tout commiter en une fois, fusionner les branches dans `main`, pousser vers `origin`. | Exécuté après application des décisions. |

## Frontières des domaines

| Sujet | Décision | Effet |
|---|---|---|
| Opposition d'un particulier à une injonction de payer | Domaine exécution. | [ENF-012](03-nouveaux-domaines/suites/enf-012-opposition-injonction.md) ; point ouvert de DOM-003 levé. |
| Offre d'indemnisation d'une victime d'accident de la circulation | Domaine responsabilité civile. | Rattachée à [DOM-035](03-nouveaux-domaines/dom-035-responsabilite-dommages.md) ; point ouvert de DOM-005 levé. |
| Placements et actifs numériques | Orientation seule. | BNK-011 inchangée ; aucun nouveau domaine. |
| Achats entre particuliers | Restent dans `consumer-legal`. | CONSO-011 inchangée. |
| Litige d'un secteur sans plugin disponible | `consumer-legal` traite avec les règles générales de la consommation et signale les règles sectorielles manquantes. | [CONSO-014](03-nouveaux-domaines/suites/conso-014-secteur-non-couvert.md) ; règle de frontière BASE-003 et découpage DOM-001 modifiés. Dès que le plugin du secteur est disponible, `consumer-legal` revient à l'orientation. |
| Premières tranches de nouveaux domaines | Aucune lancée pour l'instant. | CONSO-001, CRIM-001, ENF-001, BNK-001 et INS-001 restent `proposee`. |

## Ajouts au backlog

| Sujet | Décision | Story créée |
|---|---|---|
| Caution d'un prêt | Suite du domaine bancaire. | [BNK-012](03-nouveaux-domaines/suites/bnk-012-caution.md) |
| Saisie immobilière | Suite du domaine exécution. | [ENF-013](03-nouveaux-domaines/suites/enf-013-saisie-immobiliere.md) |
| Indemnisation des victimes d'infractions | Suite du domaine pénal. | [CRIM-013](03-nouveaux-domaines/suites/crim-013-indemnisation-victimes.md) |
| Exécution des peines | Suite du domaine pénal. | [CRIM-014](03-nouveaux-domaines/suites/crim-014-execution-peines.md) |
| Interpellations | Compléter DOM-002 ; la garde à vue reste CRIM-002. | [CRIM-015](03-nouveaux-domaines/suites/crim-015-interpellation.md) |
| Manifestations | Compléter DOM-002. | [CRIM-016](03-nouveaux-domaines/suites/crim-016-manifestation.md) |
| Armes | Compléter DOM-002. | [CRIM-017](03-nouveaux-domaines/suites/crim-017-armes.md) |
| Auto-entrepreneur, URSSAF, impôts de l'activité | Nouveau cadrage micro-entreprise ; CAF reste DOM-012, impôts des particuliers DOM-011. | [DOM-039](03-nouveaux-domaines/dom-039-micro-entreprise.md) et situation S-43 |
| Syndicats | Syndicats de salariés : droit syndical du salarié du privé. | [TRAV-018](01-pilote-travail/suites/trav-018-droits-syndicaux.md) |

| Chasse et pêche de loisir | Nouveau cadrage (question posée le même jour). | [DOM-040](03-nouveaux-domaines/dom-040-chasse-peche.md) et situation S-45 |
| Relation avec un notaire ou un avocat (frais, réclamation) | Nouveau cadrage « professionnels du droit ». | [DOM-041](03-nouveaux-domaines/dom-041-professionnels-du-droit.md) et situation S-44 |
| Contrôles du fisc, de la CAF, de l'URSSAF et des autres organismes | Traités dans chaque domaine, pas de cadrage transversal. | Compléments dans [DOM-011](03-nouveaux-domaines/dom-011-fiscalite.md), [DOM-012](03-nouveaux-domaines/dom-012-protection-sociale.md) et [DOM-039](03-nouveaux-domaines/dom-039-micro-entreprise.md) |
| Comptables | Expert-comptable dans DOM-041 (professionnels du droit et du chiffre) ; comptable public et vérification de comptabilité dans DOM-011. | Compléments dans [DOM-041](03-nouveaux-domaines/dom-041-professionnels-du-droit.md) et DOM-011 |
| Artistes-auteurs et intermittents du spectacle | Nouveau cadrage dédié. | [DOM-042](03-nouveaux-domaines/dom-042-artistes-spectacle.md) et situation S-46 |
| Droit d'auteur au-delà de la photo et du logiciel ; dessins et modèles | Suites du plugin propriété intellectuelle. | PI-026 à PI-030 ([découpage EXIST-008](02-plugins-existants/exist-008-annexes/exist-008-decoupage-pi.md)) |
| Faire ou subir un procès civil | Suites du plugin contentieux pour le particulier. | CTX-025 à CTX-028 ([découpage EXIST-006](02-plugins-existants/exist-006-annexes/exist-006-decoupage-contentieux.md)) et situation S-47 |
| Urbanisme | Déjà cadré par DOM-019 ; rien à ajouter. | — |
| Avertissement « ne remplace pas » | Phrase courte en fin de chaque réponse, renfort en tête si délai, procédure, pénal ou enjeu irréversible ; l'interlocuteur nommé dépend du domaine (avocat, juriste, notaire, commissaire de justice, expert-comptable…). L'autorité qui mène une procédure n'est pas un conseil. | [BASE-013](00-fondations/base-013-avertissement-interlocuteur.md) ; critère ajouté au [modèle de story](story-template.md) |
| Actualité des textes avant livraison | Relecture datée de chaque référence embarquée, bloquante pour un lot. | [BASE-014](00-fondations/base-014-relecture-references.md) |
| Jurisprudence pendant une réponse | Cadrer l'accès aux décisions sans PISTE et la conduite en cas d'échec. | [BASE-015](00-fondations/base-015-jurisprudence-runtime.md) |
| Veille des références livrées | Suite du plugin de veille réglementaire. | [VEI-021](02-plugins-existants/suites/vei-021-veille-references-plugins.md) |
| Médias | Nouveau cadrage couvrant personne atteinte, personne mise en cause, journalistes et créateurs, petits médias et sites. | [DOM-043](03-nouveaux-domaines/dom-043-medias-expression.md) et situation S-48 |
| Vices de procédure et nullités | Repérage prudent dans chaque procédure : points à soumettre à l'avocat, alerte sur le moment (avant toute défense au fond), jamais « l'acte est nul ». | [CTX-029](02-plugins-existants/suites/ctx-029-reperer-irregularites-civiles.md), [ENF-020](03-nouveaux-domaines/suites/enf-020-reperer-irregularites-execution.md), [CRIM-024](03-nouveaux-domaines/suites/crim-024-reperer-irregularites-penales.md), complément de [DOM-010](03-nouveaux-domaines/dom-010-administratif.md) |
| France Travail, allocation chômage, RSA, prime d'activité | Compléter DOM-012 avec une tâche par régime (organisme, recours et juge propres) ; le cadrage dira si un plugin distinct se justifie. | Complément de [DOM-012](03-nouveaux-domaines/dom-012-protection-sociale.md) et situation S-64 |
| Aides à la création d'entreprise | ACRE dans DOM-039 ; aide en capital et maintien de l'allocation de France Travail dans DOM-012, qui décide aussi du cumul avec l'activité. | Frontières de [DOM-039](03-nouveaux-domaines/dom-039-micro-entreprise.md) et de DOM-012 |
| Militaires, gendarmes, réservistes et anciens combattants | Nouveau cadrage dédié, distinct de la fonction publique civile. | [DOM-044](03-nouveaux-domaines/dom-044-militaires-anciens-combattants.md), situation S-65 ; frontières de DOM-036 et [DOM-037](03-nouveaux-domaines/dom-037-fonction-publique.md) |

## Retrait d'un plugin hérité

| Sujet | Décision | Effet |
|---|---|---|
| Plugin `legal-clinic` (cliniques juridiques universitaires américaines) | Retirer le plugin, garder la trace du cadrage. | Répertoire et entrée du marketplace supprimés ; références actives retirées (README, connecteurs, `law-student`, hub). Le nom `judge-fr-eu-legal-clinic` reste réservé par le hub. [EXIST-009](02-plugins-existants/exist-009-clinique-juridique.md) reste `terminee` ; CLN-001 à CLN-023 passent `abandonnee`. Le marketplace compte onze plugins et 134 skills. |

Les nouvelles stories sont `proposee`. Elles suivent le contrat commun de leur
découpage et n'ont été ni sélectionnées ni implémentées.
