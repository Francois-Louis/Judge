---
id: SOC-010
titre: "Préparer une annexe de contrats selon l'accord d'acquisition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-008, SOC-009]
---

# SOC-010 — Préparer une annexe de contrats selon l'accord d'acquisition

## Objectif et résultat attendu

Une personne prépare un projet d'annexe contractuelle, avec chaque inclusion/exclusion expliquée par la définition réellement fournie.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/material-contract-schedule/SKILL.md`
- `corporate-legal/references/diligence-findings-schema.yaml (contrat SOC-009)`
- `corporate-legal/CLAUDE.md (annexes contractuelles)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Version du contrat d'acquisition, définition exacte et format de l'annexe, date/périmètre, constats ou grille vérifiés, contrats/avenants et valeurs/devises.

## Travail attendu

Appliquer chaque branche de la définition négociée, pas le seuil du profil. Garder inclus/exclus/indéterminés et justification par pièce ; valeur ou contrat manquant ne devient pas exclusion. Distinguer projet interne et annexe destinée à remise, sans notes internes ou secret américain automatique. Conserver id/entité/version/VDR et overlay interne séparé des accords requis ; signaler limite de complétude. Produire handoff SOC-011/012 manuel si aval indisponible.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Accord d'acquisition comme pièce contractuelle ; Code civil/Code de commerce et jurisprudence à rechercher si portée de déclaration, garanties ou informations nécessite analyse. Aucune liste légale de Material Contracts présumée.

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

- Cas normal : A01 définition par montant OU clause de contrôle : contrat sous seuil mais avec clause de contrôle inclus avec justification.
- Cas limite : Montant inconnu et annexe de contrat absente : inclusion indéterminée, pas d'attestation « tous contrats importants listés ».
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Négociation de la définition, validation des déclarations/garanties et remise à l'acquéreur.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

