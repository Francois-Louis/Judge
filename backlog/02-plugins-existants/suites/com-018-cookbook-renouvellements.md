---
id: COM-018
titre: "Adapter le cookbook de suivi des renouvellements"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-007, COM-008, COM-009]
---

# COM-018 — Adapter le cookbook de suivi des renouvellements

## Objectif et résultat attendu

Préparer un cookbook distant cohérent avec le registre adapté, produisant un rapport local et un handoff explicite, sans déploiement.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Adaptation du cookbook associé, distinct du paquet installé.

- `managed-agent-cookbooks/renewal-watcher/agent.yaml`
- `managed-agent-cookbooks/renewal-watcher/subagents/repo-reader.yaml`
- `managed-agent-cookbooks/renewal-watcher/subagents/deadline-calculator.yaml`
- `managed-agent-cookbooks/renewal-watcher/subagents/alert-writer.yaml`
- `managed-agent-cookbooks/renewal-watcher/README.md`
- `managed-agent-cookbooks/renewal-watcher/steering-examples.json`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Registre/contrat de données COM-006, sorties COM-007/008/009, sources et versions, périmètre d'accès, date/fuseau et destination déclarée.

## Travail attendu

Conserver séparation lecteur/calcul/rédacteur et défense injection ; vérifier permissions MCP réelles plutôt qu'une étiquette read-only. Remplacer USD/ASCII imposés, schémas URL mono-CLM et bandes 30/60 divergentes ; couvrir jour 0 et dates non déterminées. Ne pas calculer au plus tôt de deux dates de nature différente sans qualification. Distinguer handoff, transmission prouvée et décision ; sources indisponibles = rapport partiel, pas all-clear. Adapter le marquage sans secret présumé. Garder le plugin local autonome.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Contrats de données des COM préalables ; aucune nouvelle règle juridique créée par l'orchestrateur.

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

- Cas normal : Dry-run sur fixtures françaises avec accents, EUR et échéance aujourd'hui : schémas acceptés, bande identique au rapport local, handoff produit sans envoi.
- Cas limite : Connecteur absent, champ requis inconnu ou texte injecté : échec/limite tracé, aucune instruction suivie ni notification externe.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Déploiement API, ordonnanceur actif, envoi Slack/email, changement transverse du moteur sans story bornée.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
