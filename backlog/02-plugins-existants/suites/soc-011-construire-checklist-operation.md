---
id: SOC-011
titre: "Construire la liste sourcée des conditions et livrables d'une acquisition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-011 — Construire la liste sourcée des conditions et livrables d'une acquisition

## Objectif et résultat attendu

Le repreneur obtient une liste des conditions, actes et livrables identifiés, reliés au contrat d'acquisition et aux questions réglementaires encore à vérifier.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/closing-checklist/SKILL.md (Mode 1 et schéma)`
- `corporate-legal/references/closing-checklist-schema.yaml (à créer)`
- `corporate-legal/CLAUDE.md (Closing checklist)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Structure d'acquisition, contrat et annexes avec version/date/signature établie ou non, calendrier envisagé, entités et pays, conditions et livrables nommés.

## Travail attendu

Distinguer signature, réalisation, conditions suspensives, obligations antérieures/postérieures, autorisation sociale et accord tiers. Extraire chaque exigence avec id stable, source/version, responsable déclaré, échéance/fondement, preuve attendue, état et inconnues. Bloquant contractuel n'est pas autorisation légale ; une formalité non listée au contrat peut devoir être recherchée. Contrôle concurrence, investissements étrangers et secteurs : identifier critères/faits et rechercher sources officielles avant tout délai, sans HSR/CFIUS remplacés mot à mot. Versionner données et préparer rapprochements non destructifs. Ne pas certifier opération prête ou fonds libérables.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Code civil/Code de commerce et droit France/UE selon acquisition ; textes et sources officielles Autorité de la concurrence/Commission, DG Trésor et régulateur sectoriel si champ établi ; statuts/pouvoirs et accord sont des pièces distinctes.

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

- Cas normal : A01 accord fictif identifiant décisions sociales, tiers et documents : lignes séparées par entité/condition avec preuve attendue.
- Cas limite : Projet non signé et approbation réglementaire mentionnée sans faits de seuil : ligne à vérifier, aucun délai d'attente ou caractère obligatoire présumé.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Conseil de structure, calcul universel d'autorisations, rédaction des actes et certification de réalisation.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

