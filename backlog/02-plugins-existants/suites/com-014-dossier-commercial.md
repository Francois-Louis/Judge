---
id: COM-014
titre: "Gérer un dossier commercial isolé"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-013]
---

# COM-014 — Gérer un dossier commercial isolé

## Objectif et résultat attendu

Créer, sélectionner, lister ou archiver un dossier avec ses pièces et son historique sans fuite de contexte vers un autre client.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/matter-workspace/SKILL.md`
- `commercial-legal/CLAUDE.md (dossier actif)`
- `commercial-legal/references/dossier-commercial.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Identité du dossier, client représenté, contrepartie, tâche, faits/territoires/dates, confidentialité déclarée, accès autorisés et dossier actif.

## Travail attendu

Conserver new/list/switch/close/none et archivage sans suppression ; remplacer modèles US et en-têtes promettant une protection. Utiliser exclusivement le helper pour le durable, refuser collisions/slug invalide, ne pas ouvrir le contenu d'un autre dossier sous prétexte de lien. Liste limitée aux métadonnées utiles. Pas de contrôle de conflits ou de conservation annoncé comme effectué.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Contrat BASE-008, méthode de minimisation/confidentialité ; règles professionnelles seulement si le résultat les invoque et après vérification.

Pistes **non vérifiées pour cette proposition** : lire textes, passages,
versions et transitions lors de l'implémentation. Tracer les accès réels,
y compris les voies officielles alternatives BASE-010 si nécessaire ; réserver
la conclusion dépendante lorsqu'une source ou une pièce manque.

## Critères d'acceptation

- [ ] Le résultat annoncé est observable sur le cas normal, avec renvois aux pièces.
- [ ] Le cas limite réserve les conclusions dépendantes et propose une suite utile.
- [ ] Faits, clauses, hypothèses de droit et préférences de négociation restent distincts.
- [ ] Sources exactes, versions, temporalité et applicabilité sont tracées selon BASE-005.
- [ ] Le paquet détaché charge ses références locales ; isolation BASE-008 conservée.
- [ ] La sortie est comprise par une personne sans formation juridique ; aucune action externe implicite.
- [ ] Documentation, métadonnées et NOTICE reflètent seulement le périmètre réellement adapté.

## Vérification

- Cas normal : Deux clients, ouverture puis sélection de A : sortie dans A et aucune pièce de B chargée.
- Cas limite : Archive homonyme ou slug ../B : refus explicite sans déplacement ni suppression ; reprise du dossier actif vérifiable.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Gestion de conflits d'intérêts, politique de rétention, archivage probatoire certifié, synchronisation externe.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
