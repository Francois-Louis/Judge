---
id: SOC-014
titre: "Initialiser le plan des engagements après acquisition"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-014 — Initialiser le plan des engagements après acquisition

## Objectif et résultat attendu

Le dirigeant reçoit un plan initial des obligations postérieures identifiées, avec provenance et distinction entre délais contractuels, exigences à vérifier et objectifs internes.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/integration-management/SKILL.md (Mode 1)`
- `corporate-legal/references/integration-tracker-schema.yaml (à créer)`
- `corporate-legal/CLAUDE.md (contexte et sorties post-acquisition)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Opération/structure et entités, preuve/date de réalisation ou statut inconnu, accord et annexes/avenants, checklist éventuelle, responsables déclarés.

## Travail attendu

Créer un plan borné aux engagements postérieurs identifiés dans les pièces : id, source/version, déclencheur, échéance/calcul, responsable, preuve attendue et état. Séparer chaque garantie/période et date de séquestre ou earn-out ; conserver condition, bénéficiaire et incertitude, sans calculer performance financière ni délai contentieux. Ne pas appeler une liste générique complète. Retirer J1=+7 et jalons 30/90/180 comme prescriptions, COBRA/USPTO/Secretary of State comme parcours français ; objectifs internes explicitement choisis. Reprendre items de checklist sans perte de provenance et sans statut complet hérité sans preuve ; filiales étrangères séparées.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Accord et annexes comme obligations contractuelles ; Code civil/Code de commerce, textes d'application et formalités France/UE selon événement ; questions PI/travail/données/fiscalité dirigées vers leur domaine sans règle importée.

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

- Cas normal : A01 réalisation déclarée au 16 octobre et accord prévoyant une obligation 45 jours calendaires après : enregistrer le calcul conditionnel et sa source, distinct du jalon interne 30 jours.
- Cas limite : Seule une term sheet non signée et date de réalisation inconnue : plan préparatoire avec dates non calculées, pas d'engagement contractuel certifié.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Restructuration, fusion/dissolution, calcul d'indemnisation et performance d'earn-out.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

