---
id: COM-010
titre: "Consigner le contexte d'écarts commerciaux acceptés"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-002]
---

# COM-010 — Consigner le contexte d'écarts commerciaux acceptés

## Objectif et résultat attendu

Pour un accord signé fourni, conserver les écarts au playbook applicable et leur contexte déclaré dans un journal traçable.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/agents/deal-debrief.md`
- `commercial-legal/CLAUDE.md (référentiel et dépôt)`
- `commercial-legal/references/journal-ecarts.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Accord et preuve de signature/date, version du playbook au moment retenu, côté, droit, identifiant du contrat, auteur des explications et exception ponctuelle éventuelle.

## Travail attendu

Une modification de fichier ou mention executed ne prouve pas une signature. Conserver clause exacte, position/version comparée, gravité et raison déclarée ; absent = non fourni. Dédupliquer sans confondre deux accords du même jour/partie. Garder exclude_from_patterns, ne pas transformer un accord signé en validation de sa légalité. Sans connecteur : accord fourni et journal local, aucune collecte générale ni notification.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Pièces et référentiel interne ; les questions de droit détectées suivent COM-002, la fréquence ne vérifie pas une règle.

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

- Cas normal : Accord signé fourni avec un plafond exceptionnel : écart et motif attribués, exception exclue des futurs motifs statistiques.
- Cas limite : Fichier final modifié hier sans preuve de signature ou playbook ancien absent : statut réservé, aucune signature déduite ni comparaison historique inventée.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Validation rétrospective de tous les contrats, changement du playbook, collecte non bornée, diffusion.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
