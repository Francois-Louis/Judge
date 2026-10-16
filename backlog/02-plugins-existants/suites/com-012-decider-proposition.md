---
id: COM-012
titre: "Décider d'une proposition de position commerciale"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-011]
---

# COM-012 — Décider d'une proposition de position commerciale

## Objectif et résultat attendu

Examiner une proposition identifiée, accepter/éditer/rejeter/différer et conserver exactement la décision autorisée.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/review-proposals/SKILL.md`
- `commercial-legal/agents/playbook-monitor.md (étape 5)`
- `commercial-legal/references/propositions-commerciales.md (à créer par COM-011)`
- `commercial-legal/CLAUDE.md (édition ciblée)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Proposition et identifiant, version du profil ayant servi au diff, décision et qualité du décideur, propositions en attente.

## Travail attendu

Afficher le diff exact et appliquer seulement l'édition autorisée avec digest du helper ; conflit de version = relecture. Conserver auteur/date et états distincts. Rejet ne modifie pas le profil ; différé reste actif après archivage et passage suivant. Fichier absent signifie absence de proposition accessible, pas droit ou playbook à jour. Une préférence approuvée ne change pas une règle juridique.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Pièces COM-011, pouvoir de décision déclaré et frontière de stockage BASE-008 ; aucune validation juridique par le vote.

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

- Cas normal : Accepter un fallback précis et rejeter un second : seul le diff approuvé est appliqué, décisions conservées.
- Cas limite : Différer puis relancer le monitor ; profil modifié entre lecture et écriture : différé préservé, écriture périmée refusée sans écrasement.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Réécriture automatique du playbook, changement de règle de droit, notification externe.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
