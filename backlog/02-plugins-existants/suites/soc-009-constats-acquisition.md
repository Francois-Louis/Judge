---
id: SOC-009
titre: "Extraire les constats documentaires d'une acquisition de titres"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-009 — Extraire les constats documentaires d'une acquisition de titres

## Objectif et résultat attendu

Le repreneur ou dirigeant reçoit des constats bornés sociétés/contrats, les pièces manquantes et les questions de décision ou de relais.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/diligence-issue-extraction/SKILL.md`
- `corporate-legal/CLAUDE.md (M&A, sources, gravité)`
- `corporate-legal/references/diligence-findings-schema.yaml (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Structure/phase/parties de l'opération, corpus et request list, statuts/pactes/pouvoirs de cible, contrat d'acquisition et versions disponibles, contrats et avenants ; seuils internes explicités.

## Travail attendu

Borner à acquisition de titres d'une cible SAS/SARL ; documenter inventaire lu/non lu/exclu/illisible, seuils et catégories. Un seuil financier ne masque pas statuts, pouvoirs, restrictions ni documents de valeur inconnue. Séparer fait, clause, hypothèse, règle vérifiée et conséquence possible ; rattacher chaque constat à entité/opération/contrat/version. Retirer §280G/HSR/CFIUS et doctrines successor liability US comme mécanismes France. Préparer handoffs complets (condition, garant, préavis, preuve, gravité et réserve) sans exécuter aval non adapté. Grille ou export IA facultatif ; pas de boucle ni transfert automatique vers outil. PI, travail, fiscalité, concurrence/investissements : signaler question et source à rechercher sans audit complet.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Code civil/Code de commerce, textes d'application, règles France/UE et jurisprudence officielle selon question de titres, restrictions, pouvoirs, contrats ; instruments de conflit ou autorisations spécifiques seulement après qualification.

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

- Cas normal : A01 pacte de cible et contrat commercial contenant contrôle indirect : constats séparés avec source, mécanisme et question à vérifier.
- Cas limite : A01 filiale allemande sans statuts ni annexe de garantie : manque et analyse locale nécessaire, aucune conclusion de pouvoir du groupe ou exonération fondée sur acquisition d'actifs.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Revue de tous domaines de due diligence, négociation des garanties, fiscalité et opinion de réalisation.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

