---
id: COM-011
titre: "Proposer une évolution de position commerciale"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-010]
---

# COM-011 — Proposer une évolution de position commerciale

## Objectif et résultat attendu

À partir d'un journal borné, produire une proposition motivée de préférence commerciale, sans changer le profil.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/agents/playbook-monitor.md (étapes 1–4)`
- `commercial-legal/CLAUDE.md (paramètres et positions)`
- `commercial-legal/references/propositions-commerciales.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Journal versionné, dates, côtés, droit/objet, paramètres internes de fréquence/période, exclusions et décisions antérieures.

## Travail attendu

Séparer vente et achat et groupes comparables, exclure one-offs et données insuffisantes, signaler les tendances contradictoires. Seuil 5/12 mois = paramètre interne, jamais norme juridique ou marché certifié. Joindre clauses, données et version courante à la proposition ; préserver propositions non décidées et rejets/différés avec identifiants stables. Pas d'écrasement ni notification automatique. Une fréquence ne régularise pas une clause.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Journal et playbook interne, sources de droit des constats amont sans promotion de leur statut.

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

- Cas normal : Six concessions comparables côté achat dont une exception : proposition fondée sur les cinq retenues, traçable et sans écriture du profil.
- Cas limite : Trois écarts vente et trois achat opposés, dont proposition déjà différée : pas de fusion artificielle ni perte de la proposition existante.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Mise à jour du droit, approbation, édition du profil, envoi, veille réglementaire.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
