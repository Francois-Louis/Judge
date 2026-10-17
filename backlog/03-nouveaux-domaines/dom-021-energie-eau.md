---
id: DOM-021
titre: "Cadrer un plugin énergie, eau et services essentiels"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-021 — Cadrer un plugin énergie, eau et services essentiels

## Objectif

Aider les ménages à comprendre une facture, une modification de contrat ou une interruption de service.

Nom de plugin proposé : `utilities-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Vérifier les données d'une facture contestée : période, index, estimation, prix et régularisation.
- Préparer une réclamation sur une souscription, une modification, un déménagement ou une résiliation.
- Identifier les informations urgentes face à un impayé ou à une interruption annoncée.

## Qualification et frontières

Service, fournisseur/gestionnaire, contrat, compteur, relève, factures, dates, qualité d'abonné et courriers reçus.

Les règles de facturation et d'accès au service sont ici ; les charges du bailleur restent en DOM-006, la rénovation énergétique en DOM-015 et les aides sociales dans leur domaine.

## Sources à prévoir et vérifier

Code de l'énergie, règles de l'eau et des services publics selon l'opérateur, Code de la consommation, textes locaux et autorités sectorielles.

- [Médiateur national de l'énergie — litiges](https://www.energie-mediateur.fr/les-litiges/)
- [Impayés de factures — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/F20055)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire une régularisation d'électricité et préparer une demande de justification, sans extrapoler un régime à l'eau.

## Critères d'acceptation

- [x] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [x] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique — entrées par récit et parcours fictifs relus par le rédacteur ; compréhension d'un lecteur réel non observée.
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [x] Eau, électricité, gaz, fourniture et réseau sont distingués ; le cadrage ne généralise pas une protection ou un médiateur à tous les services.
- [x] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [x] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une facture augmente après une longue estimation.
- Un abonnement a changé sans accord allégué du client.
- Un courrier annonce une restriction ou une coupure.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Complément des frictions logement — 16 octobre 2026

Points 27 ; relais 37, 44, 54 de la [matrice logement](dom-006-annexes/dom-006-frictions-utilisateurs.md).

Découper une tâche propre à la surconsommation d'eau et au plafonnement allégué, distincte de la première tranche électricité. Pièces : qualité d'abonné, contrat/opérateur, compteur et relevés, factures historiques, alerte reçue et date prouvée, localisation de fuite, réparation et attestation disponible. Sortie : comparaison des périodes/volumes, conditions et exclusions à vérifier, demande au service compétent et échéances de réponse ; ni plafonnement automatique ni responsabilité déduite de la consommation. Identifier fuite sur canalisation, équipement et situation avant tout régime ; si facture du bailleur, LOG-002 garde répartition et récupération, le droit de l'abonné doit être qualifié séparément. Coupure par bailleur et éviction → ENF-005 ; panne d'équipement → LOG-004/005 ; recherche de fuite → INS-017 et DOM-018 selon question.

- [x] Le futur découpage attribue à chaque tâche ses entrées, sortie, sources, limites et scénarios, y compris les voies urgentes distinctes.

Scénarios **attendus, non exécutés** : Facture anormale après fuite réparée sans alerte retrouvée : demander relevés, preuve d'information et attestation ; si charges collectives, identifier abonné et destinataire avant d'invoquer le mécanisme.
Les textes, versions, transitions, seuils et échéances seront vérifiés sur
sources officielles lors des implémentations. Ce complément ne termine pas
le cadrage, ne crée aucun plugin et n'exécute aucune démarche externe.

## Bilan d'exécution — 17 octobre 2026

- [Découpage des services](dom-021-annexes/dom-021-decoupage-services.md) :
  nom `utilities-legal` conservé, identifiant futur
  `judge-fr-eu-utilities-legal`, qualification du service, des fonctions
  fourniture/réseau, du contrat, compteur, abonné, logement, dates et urgence.
- Quatorze stories UTI-001 à UTI-014 sous `suites/` : trois lectures de
  facture, surconsommation d'eau, souscription/modification/clôture séparées
  pour énergie et eau, trois voies urgentes d'impayés et une qualification
  d'interruption hors impayé. Chaque tâche a ses entrées, sortie, pièces,
  référence métier locale future, limites et scénarios.
- Première tranche UTI-001 : une régularisation d'électricité d'un ménage
  directement abonné en métropole, tableau des périodes/index/prix/acomptes
  et demande de justification. Pas d'extension au gaz, à l'eau, au contrat
  professionnel ou à l'urgence ; leur détection oriente vers la tâche propre.
- UTI-004 reprend le point logement 27 : statut d'abonné, volumes et
  périodes comparables, information et réception, canalisation/équipement,
  réparation/attestation et vérification du compteur. Ni plafonnement
  automatique ni responsabilité déduite. LOG-002, ENF-005, LOG-004/005,
  INS-017 et DOM-018 gardent leurs questions distinctes.
- [Registre des sources](dom-021-annexes/dom-021-sources.md) : pages du
  Médiateur national de l'énergie et deux guides Service Public ouverts ;
  tentatives CGCT consignées avec refus 403, sans texte lu ni version
  applicable certifiée. Programme de recherche attribué à chaque suite.
- [Vérification documentaire](dom-021-annexes/dom-021-verification.md) :
  treize dossiers/variantes fictifs A à M et limites transverses relus par
  le rédacteur. Le [relevé des contrôles](dom-021-annexes/dom-021-resultats.json)
  distingue les résultats statiques de l'exécution future des scénarios.
- Ligne énergie/eau BASE-003, situation S-11 et point 27 de la matrice
  logement reliés au découpage ; famille UTI ajoutée au générateur et index
  ETAT régénéré. Lot limité à `backlog/`, sans NOTICE ni version de plugin.

**Portée :** cadrage documentaire clos, aucun plugin créé ou inscrit au
marketplace, aucun skill implémenté, installé ou exécuté, aucune démarche
externe. Les guides ont été lus pour orienter le découpage ; les textes,
versions, exceptions, seuils et échéances restent à vérifier dans les lots
d'implémentation. Les scénarios métier des suites sont attendus, non
exécutés ; les parcours A à M n'observent pas une sortie de skill.
PILOTE-003 est terminé après BASE-011 : son bilan reste à relire avant
extension ; aucune tranche n'est sélectionnée automatiquement et toutes les
suites restent `proposee`.

La relecture humaine est prise en charge par l'utilisateur conformément à
AGENTS.md du 17 octobre 2026. Elle n'est pas déclarée effectuée, ni la
compréhension d'un lecteur réel vérifiée. La story est close sur ses
livrables et contrôles de cadrage, sans attendre cette relecture.
