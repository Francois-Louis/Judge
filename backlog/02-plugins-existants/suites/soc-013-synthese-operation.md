---
id: SOC-013
titre: "Expliquer les constats et décisions ouvertes d'une acquisition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-009]
---

# SOC-013 — Expliquer les constats et décisions ouvertes d'une acquisition

## Objectif et résultat attendu

Un dirigeant non juriste lit une synthèse courte adaptée au destinataire, avec faits établis, portée de la revue et questions à arbitrer.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/deal-team-summary/SKILL.md`
- `corporate-legal/CLAUDE.md (Deal team briefing et Outputs)`
- `corporate-legal/references/diligence-findings-schema.yaml (contrat SOC-009)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Constats datés, périmètre et versions lus, destinataire, éventuelle synthèse antérieure, états de checklist fournis et décisions réellement consignées.

## Travail attendu

Conserver toutes les réserves déterminantes, la gravité motivée et les conditions ; distinguer décision demandée, prise et action effectuée. Afficher couverture avec numérateur/dénominateur et non lus, pas pourcentage global sans base. Comparer évolutions sur identifiants/versions sans déclarer résolu un point disparu. Présenter en langage clair prix/obligation/pièces/prochaine question selon constat, sans conclusion juridique nouvelle non sourcée. Toute action de checklist reste proposée tant qu'inscription non prouvée. Confidentialité à qualifier par pièces/rôles, aucun héritage automatique de privilège ; brouillon local.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-annexes/exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-annexes/exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Sources et pièces des constats amont ; méthode BASE-005 pour ne pas renforcer une conclusion en la résumant. Recherche complémentaire primaire si conclusion nouvelle.

Pistes **non vérifiées dans ce cadrage** : lire les passages exacts, versions,
champs et dispositions transitoires à la date des faits lors de l'implémentation.
Tracer lectures et échecs, employer les voies officielles BASE-010 sans
abonnement obligatoire, et réserver seulement les conclusions dépendantes.

## Critères d'acceptation

- [ ] Le résultat annoncé est observable sur le cas normal avec pièces/localisations.
- [ ] Le cas limite garde les inconnues et propose une démarche utile.
- [ ] Faits déclarés, preuves, clauses, règles et préférences restent distincts.
- [ ] Sources exactes, versions, temporalité et applicabilité sont tracées selon BASE-005.
- [ ] Références locales du paquet détaché et isolation BASE-008 fonctionnent.
- [ ] Une personne sans formation juridique comprend les pièces et prochaines actions.
- [ ] Aucun brouillon ou état de registre n'est assimilé à une action externe exécutée.
- [ ] Documentation, métadonnées et NOTICE reflètent le seul périmètre adapté.

## Vérification

- Cas normal : A01 repreneur non juriste : comprendre différence entre accord tiers demandé, accord reçu sous condition et décision sociale encore à documenter.
- Cas limite : Nouvelle synthèse sans ancienne annexe ni dénominateur du corpus : dire comparaison/couverture indisponibles, pas « revue complète sans blocage ».
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-annexes/exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Arbitrage à la place des parties, certification ou envoi au conseil/équipe.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

