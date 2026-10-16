---
id: COM-006
titre: "Enregistrer une échéance contractuelle traçable"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-001]
---

# COM-006 — Enregistrer une échéance contractuelle traçable

## Objectif et résultat attendu

À partir d'une clause et de ses preuves, créer ou corriger une fiche de renouvellement avec calcul reproductible et statut explicite.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/renewal-tracker/SKILL.md (modes 1/3 et calcul)`
- `commercial-legal/skills/renewal-tracker/references/renewal-register.yaml`
- `commercial-legal/skills/saas-msa-review/SKILL.md (handoff)`
- `commercial-legal/skills/vendor-agreement-review/SKILL.md (handoff)`
- `commercial-legal/references/echeances-contractuelles-fr.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Clause complète, terme courant et initial, durée/unité de renouvellement, preuve de dates, mode de notification, réception/envoi, heure/fuseau, calendrier prévu, identité contrat et devise.

## Travail attendu

Versionner un schéma unique et migrer les anciens champs sans écrasement ; conserver source/section, hypothèses et validation humaine. Réconcilier handoff SaaS, exemple YAML et tracker. Calculer depuis le terme courant justifié. Séparer échéance contractuelle et marge opérationnelle ; aucun vendredi, calendrier US ou transport 5/10 jours par défaut. Enregistrer une date déclarée comme telle ; fondement manquant = a-determiner. Import facultatif CLM limité aux accès autorisés, métadonnées non certifiées, reprise manuelle possible.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Clauses exactes et méthode BASE-005 section délais ; droit français/UE de notification et computation seulement après qualification du régime.

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

- Cas normal : Clause fictive avec terme au 31 décembre 2026, réception au moins 60 jours calendaires avant : calcul conditionnel au 1er novembre, sans recul au vendredi inventé.
- Cas limite : Ancien registre cancel_by seul, renouvellement déjà intervenu et délai en mois : migration sans perte, calcul réservé jusqu'aux pièces utiles, doublon distingué d'un second contrat.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Rapport périodique, notification, décision de reconduction, prescription/recours, calendrier juridique universel.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
