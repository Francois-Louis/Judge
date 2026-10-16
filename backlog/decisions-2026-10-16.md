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

Les nouvelles stories sont `proposee`. Elles suivent le contrat commun de leur
découpage et n'ont été ni sélectionnées ni implémentées.
