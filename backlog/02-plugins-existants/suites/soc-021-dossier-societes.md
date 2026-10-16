---
id: SOC-021
titre: "Isoler et archiver un dossier sociétés ou opération"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006, SOC-020]
---

# SOC-021 — Isoler et archiver un dossier sociétés ou opération

## Objectif et résultat attendu

Une personne ouvre, choisit et archive un dossier dont les pièces et sorties restent séparées des autres sociétés ou opérations.

## Périmètre et fichiers

Plugin principal : `corporate-legal` (`judge-fr-eu-corporate-legal`).
Les noms techniques restent conservés ; fichiers « à créer » et contrats des
autres SOC sont des livrables futurs, pas des ressources déjà disponibles.

- `corporate-legal/skills/matter-workspace/SKILL.md`
- `corporate-legal/CLAUDE.md (Matter workspaces et lien deals)`
- `corporate-legal/references/deal-context-template.md (contrat SOC-020)`

Reprendre les seuls blocs de documentation et métadonnées concernés, synchroniser
le marketplace si le manifeste change et consigner les modifications dans les
NOTICE du paquet et de la racine. Copies communes conservées identiques.

## Entrées nécessaires

Client/entités et rôle, objet société/opération, slug, contexte SOC-020 si opération, droits de lecture croisée explicités et état actif.

## Travail attendu

Réécrire modèles commerciaux copiés en modèles sociétés/opérations, conserver new/list/switch/close/none et archivage via helper. Autoriser isolation pour dirigeant multi-entités aussi, sans auto-activer accès croisé. Choisir stockage canonique et liaison explicite vers deals ; pas de copies concurrentes contradictoires ni autre dossier lu par simple lien « related ». Vérifier collision avant move et conserver historique ; fermeture n'est ni dissolution de société ni opération terminée. Garder absence de contrôle conflits/retention exécuté explicite ; sources runtime locales.

Charger `corporate-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; SOC-022 résout sa copie dans le plugin embarqué.
Appliquer le [contrat commun](../exist-002-decoupage-societes.md) et les
[dépendances inventoriées](../exist-002-inventaire-societes.md). Corriger les
blocs setup/routage qui empêchent cette tâche sans imposer SOC-019/020/021
comme préalables à toute lecture ponctuelle. Sans profil ou connecteur,
restituer les pièces/questions et la sortie locale utile.

## Sources à rechercher

Contrat BASE-008 pour chemins/helper et BASE-005 pour provenance ; pièces d'identification, sans analyse juridique nouvelle du dossier.

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

- Cas normal : Deux sociétés sous même dirigeant : changement de dossier affiche bonne identité, archive conserve historique et coupe actif si nécessaire.
- Cas limite : Slug actif/archivé déjà présent et contexte deal appartenant à autre matière : refus de collision/mélange, anciennes pièces préservées.
- Sans source/pièce déterminante : produire le résultat partiel utile sans
  modèle américain de remplacement ni conclusion juridique non établie.

Exécuter les scénarios sur pièces fictives dans le futur lot, conserver
sorties et ressources lues ; appliquer les couches BASE-006 (structure,
paquet détaché, client, résultat métier, compréhension par lecteur non juriste).
La relecture de cadrage est dans la [vérification EXIST-002](../exist-002-verification.md) ;
ces scénarios de skills restent **attendus, non exécutés**.

## Hors périmètre

Suppression, politique de conservation, audit des conflits et changement de règles juridiques par profil.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-002, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection explicite d'une tranche ; aucune
commande, connexion ou automatisation France/UE n'est annoncée comme livrée.

