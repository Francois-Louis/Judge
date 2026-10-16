---
id: COM-003
titre: "Trier un engagement de confidentialité commercial"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-001]
---

# COM-003 — Trier un engagement de confidentialité commercial

## Objectif et résultat attendu

Un indépendant ou une équipe reçoit un NDA commercial ; il obtient les engagements, exceptions, points à clarifier et un tri expliqué sans autorisation de signer.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/nda-review/SKILL.md`
- `commercial-legal/skills/review/SKILL.md (branche NDA)`
- `commercial-legal/CLAUDE.md (positions NDA et closing_action)`
- `commercial-legal/references/confidentialite-commerciale-fr.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

NDA complet, finalité des échanges, parties divulgatrice/réceptrice, informations, dates, durée, droit/juge, annexes et préférences déclarées.

## Travail attendu

Conserver tri court et questionnaire unilatéral ; distinguer divulgation et réception du côté achat/vente. Rechercher définition, exceptions, résiduels, restitution/archives, durée et secret des affaires. Détecter cession de droits, exclusivité ou non-concurrence cachées ; orienter ce complément sans le déclarer traité. Le tri interne ne constate ni validité générale ni signature approuvée. Le closing_action reste une suggestion et ne déclenche aucun envoi.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Code civil, Code de commerce et jurisprudence officielle ; texte UE et transposition française sur le secret des affaires selon le champ.

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

- Cas normal : Graphiste indépendant seul divulgateur : NDA unilatéral lu sans rejet automatique, engagements et inconnues expliqués.
- Cas limite : NDA avec licence et non-concurrence, sans positions prévalidées : portée élargie signalée, aucune classification rassurante par défaut.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Rédiger un NDA entier, contrats de travail, opération de fusion/acquisition, signature.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
