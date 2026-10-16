---
id: COM-009
titre: "Expliquer une revue commerciale en langage courant"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-002, COM-008]
---

# COM-009 — Expliquer une revue commerciale en langage courant

## Objectif et résultat attendu

Transformer une revue fournie en synthèse courte : engagement, conséquence, inconnues et deux ou trois actions utiles pour la personne.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/stakeholder-summary/SKILL.md`
- `commercial-legal/CLAUDE.md (sorties et audience)`
- `commercial-legal/references/etats-actions-commerciales.md (à créer par COM-008)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Revue et pièces citées, audience et rôle réel, côté achat/vente, états de demandes d'arbitrage et registre si une inscription est évoquée.

## Travail attendu

Conserver limite de 200 mots pour le corps, conditions et réserves amont, avec références accessibles en note. Adapter à indépendant/artisan sans jargon. Vérifier une entrée réelle du registre plutôt qu'un fichier de sortie pour dire inscrit ; fichier d'escalade = brouillon jusqu'à preuve de transmission. Séparer transmis et approuvé ; aucune suggestion de signature sûre à partir du résumé. Pas de secret automatique par suppression/ajout d'un en-tête.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Sources de la revue amont à conserver avec leur statut, sans nouvelle conclusion juridique implicite.

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

- Cas normal : Artisan lisant une revue de maintenance avec hausse conditionnelle au tarif promotionnel : condition et action préservées.
- Cas limite : Deux approbateurs nommés, un brouillon et aucune preuve d'envoi, registre absent : zéro transmis/prouvé, inscription non faite et actions visibles.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Nouvelle revue complète, diffusion, certification de protection juridique, approbation.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
