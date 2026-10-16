---
id: COM-008
titre: "Préparer une demande d'arbitrage contractuel"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-002]
---

# COM-008 — Préparer une demande d'arbitrage contractuel

## Objectif et résultat attendu

Depuis un constat de revue, nommer le destinataire confirmé et préparer un brouillon autonome pour une décision humaine.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/escalation-flagger/SKILL.md`
- `commercial-legal/CLAUDE.md (matrice et états)`
- `commercial-legal/references/etats-actions-commerciales.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Constat sourcé, côté vente/achat, valeur/devise et seuils confirmés si pertinents, autorité du demandeur, destinataire éventuel et date justifiée.

## Travail attendu

Retirer la matrice USD d'exemple comme autorité. Une TPE peut décider elle-même ou demander un conseil sans inventer un GC. Séparer préférence hors fallback et question de droit réservée. Définir états proposé, brouillon, transmis avec preuve, décidé avec auteur/date ; ne jamais consigner envoyé depuis la simple création du fichier. Préserver les réserves et degrés de gravité amont.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Pièces et analyse amont, délégation/matrice fournie ; règles de représentation ou de pouvoir seulement si nécessaires et vérifiées.

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

- Cas normal : TPE sans matrice, clause de responsabilité à discuter : brouillon pour interlocuteur choisi, aucun destinataire fictif.
- Cas limite : Valeur/devise absentes et approbateurs contradictoires : questions ciblées, aucun seuil converti ou envoi enregistré.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Approbation automatique, envoi, ticket CLM réel, enveloppe de signature.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
