---
id: SOC-004
titre: "Créer le registre des formalités identifiées d'une société"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-004 — Créer le registre des formalités identifiées d'une société

## Objectif et résultat attendu

Le dirigeant obtient un registre initial daté des formalités identifiées pour sa société, avec fondement, déclencheur, pièces et informations à confirmer.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/entity-compliance/SKILL.md (Mode 1 et schéma inline)`
- `corporate-legal/CLAUDE.md (Entity Management)`
- `corporate-legal/references/formalites-societes.md (à créer)`
- `corporate-legal/references/compliance-tracker-schema.yaml (à créer)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Identité stable de chaque société, SAS/SARL, territoire, statuts, exercice social, événement précis, pièces de registre et formalités déjà connues, destinataire/mandataire éventuel.

## Travail attendu

Limiter le premier registre aux formalités liées à des décisions/événements identifiés ; pas de promesse d'inventaire exhaustif de toutes obligations. Séparer identifiant, forme, juridiction, établissement, exercice, formalité et période. Enregistrer source/version, déclencheur, unité/calcul, preuve, statut de vérification, destinataire et coût/devise seulement établi. Distinguer approbation des comptes, dépôt, changement de dirigeant et bénéficiaires effectifs selon champ à vérifier. Retirer calendrier Delaware/registered agent comme modèle français, custom_jurisdictions automatiquement recopié et rebuild destructif. Versionner le schéma et prévoir migration conservatrice des anciennes données. Filiale étrangère : ligne séparée avec régime non vérifié, pas de date française extrapolée.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Code civil/Code de commerce, textes d'application et formalités françaises à rechercher ; publications officielles INPI/Guichet unique, registre compétent/RNE/RCS, BODACC selon formalité, en distinguant guide et texte.

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

- Cas normal : S01/S02, même date de clôture déclarée : lignes séparées dont échéances restent conditionnées à forme, acte, dates et pièces.
- Cas limite : A01 filiale GmbH sans pièces locales : identité/pays et besoin de confirmation locale, aucune franchise tax ni date de dépôt française assignée.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Dépôt effectif, fiscalité, paie, calendrier universel et adaptation de toutes juridictions.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

