---
id: COM-007
titre: "Produire un rapport d'échéances contractuelles"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-006]
---

# COM-007 — Produire un rapport d'échéances contractuelles

## Objectif et résultat attendu

À une date de référence explicite, restituer les échéances connues, fenêtres dépassées et données incomplètes, avec les actions à préparer.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/renewal-tracker/SKILL.md (modes 2/4 et options)`
- `commercial-legal/agents/renewal-watcher.md`
- `commercial-legal/references/dashboard-template.md (réutilisation)`
- `commercial-legal/CLAUDE.md (alertes et capacités)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Registre versionné, état de validation de chaque date, as_of/heure/fuseau, fenêtre demandée, périmètre couvert et dernière synchronisation connue.

## Travail attendu

Unifier --days, date servant aux alertes et bandes 0–13/14–44/45–89 ; tester jour 0 et limites. Afficher séparément envoi prudent et réception contractuelle. Une fenêtre passée sans trace ne prouve pas reconduction ni absence de notification. Conserver les entrées a-determiner et signaler leur couverture ; pas de all-clear global si registre vide/incomplet. Watcher produit le rapport local ; pas de scan modifiant le registre sous couvert de lecture seule, ni promesse d'ordonnanceur installé.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Clauses et fiches COM-006 ; aucune nouvelle durée légale déduite des bandes internes d'urgence.

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

- Cas normal : Registre fictif aux distances -1/0/13/14/44/45/89/90 : une seule bande par entrée, jour 90 exclu de la fenêtre 90.
- Cas limite : Registre vide ou notification extérieure non enregistrée : couverture limitée, statut inconnu, aucune certitude de renouvellement ou d'absence de risque.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Envoi Slack/email, ordonnanceur, annulation, acceptation tacite décidée par l'outil, cookbook distant COM-018.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
