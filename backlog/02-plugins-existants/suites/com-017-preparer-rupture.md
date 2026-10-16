---
id: COM-017
titre: "Préparer les questions avant rupture d'une relation B2B"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-002, COM-005]
---

# COM-017 — Préparer les questions avant rupture d'une relation B2B

## Objectif et résultat attendu

Un artisan/TPE envisage ou subit l'arrêt d'une relation professionnelle ; il obtient chronologie, obligations à vérifier et questions avant notification.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/preparer-rupture-b2b/SKILL.md (création proposée)`
- `commercial-legal/skills/review/SKILL.md (orientation)`
- `commercial-legal/references/rupture-relation-b2b.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Contrat/avenants, relation réelle et ancienneté, commandes récurrentes, dépendance déclarée, motifs, notifications et preuves, durée, droit/juge et dates.

## Travail attendu

Distinguer fin de terme/non-renouvellement, résiliation pour inexécution, résiliation d'un contrat indéterminé et rupture de relation commerciale établie à rechercher. Tracer les clauses sans calculer un préavis raisonnable depuis le seul tracker ou une préférence. Vérifier changements de partie et avenants ; séparer voies contractuelles et points impératifs possibles. Fournir questions et pièces pour interlocuteur compétent, sans notifier ni décider la rupture.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Code civil/commerce et jurisprudence officielle sur résiliation et rupture des relations commerciales établies ; conflits de lois si transfrontalier.

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

- Cas normal : Sous-traitant avec commandes régulières et contrat annuel : chronologie et questions de préavis contractuel/relation réelle distinctes.
- Cas limite : Notification déjà reçue, relation ancienne, date de réception incertaine : urgence potentielle, pièces précises, aucun délai de recours ou indemnité garanti.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Préavis universel, calcul d'indemnisation contentieuse, notification, procédure collective, exécution d'un titre.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
