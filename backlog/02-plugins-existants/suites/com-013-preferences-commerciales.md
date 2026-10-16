---
id: COM-013
titre: "Créer et modifier des préférences commerciales volontaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006]
---

# COM-013 — Créer et modifier des préférences commerciales volontaires

## Objectif et résultat attendu

Un indépendant ou une équipe crée ses préférences, ou en modifie une, sans les transformer en droit ni exiger une organisation juridique.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/cold-start-interview/SKILL.md`
- `commercial-legal/skills/customize/SKILL.md`
- `commercial-legal/CLAUDE.md`
- `commercial-legal/references/company-profile-template.md (réutilisation, synchronisation transverse si évolution)`
- `commercial-legal/README.md (parcours de configuration)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Réponses et documents explicitement partagés, rôles, territoires/dates, côté achat/vente, préférences et contacts réellement connus ; profil existant et progression éventuelle.

## Travail attendu

Conserver pause/reprise, édition ciblée, --side et contrôle réel des intégrations. Retirer defaults US, chiffres juridiques présumés et exigence de 5–10 contrats ; pas de profil obligatoire pour comprendre un document isolé. Distinguer faits partagés, préférences commerciales et sources de droit, sans importer cache/mémoire. Harmoniser quick/full/provisoire avec BASE-008 et retirer déduction du scope depuis cwd. Pas de secret professionnel automatiquement garanti par le rôle. Préserver les autres réponses et copies communes synchronisées.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Méthode BASE-005, isolation et protocole USAGE-001 ; sources exactes à vérifier si une réponse affirme une règle de droit.

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

- Cas normal : Artisan sans équipe, sans avocat attitré ni contrats antérieurs : préférences minimales volontaires et champs juridiques non résolus.
- Cas limite : Profil en pause puis modification d'une seule préférence achat : autres réponses préservées, aucun import ni écrasement de la partie vente.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Refonte simultanée des 12 plugins, analyse juridique d'un contrat, migration de profils tiers.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
