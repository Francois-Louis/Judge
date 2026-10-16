---
id: COM-005
titre: "Tracer une chaîne d'avenants et une clause"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006, COM-001]
---

# COM-005 — Tracer une chaîne d'avenants et une clause

## Objectif et résultat attendu

La personne fournit contrat et avenants ; elle obtient un historique sourcé ou la trace d'une clause, avec la version candidate et ses réserves.

## Périmètre et fichiers

Plugin principal : `commercial-legal` (`judge-fr-eu-commercial-legal`).
Noms techniques existants conservés ; tout nouveau skill indiqué reste une proposition.

- `commercial-legal/skills/amendment-history/SKILL.md`
- `commercial-legal/CLAUDE.md (confidentialité et dossiers)`
- `commercial-legal/references/chaine-avenants-fr.md (à créer)`

Les chemins « à créer » sont des livrables futurs, pas des ressources disponibles.
Reprendre aussi les blocs de documentation et métadonnées concernés par la tranche,
avec synchronisation du marketplace si son manifeste change. Conserver les
références communes embarquées et ne pas modifier leurs copies isolément.

## Entrées nécessaires

Base, avenants, signatures, dates de prise d'effet, parties, renvois, ordre de priorité et pièces manquantes.

## Travail attendu

Conserver les deux vues du même index. Distinguer signature, effet et date de fichier ; comparer numérotation, changement de partie et cession. Ne pas affirmer quelle clause gouverne un conflit non résolu ; afficher les passages et la question. Retirer la prétention de collecte CLM/dépôt encore coming soon. Réserver une revue complète à sa tâche adaptée.

Charger `commercial-legal/references/shared/research-citation-method.md` depuis
le paquet installé ; pour le cookbook, résoudre la copie du plugin embarqué.
Suivre le [contrat commun du découpage](../exist-001-annexes/exist-001-decoupage-commercial.md)
et les [dépendances de contenu](../exist-001-annexes/exist-001-inventaire-commercial.md).
Corriger les seuls blocs setup/profil qui empêchent ce résultat, sans imposer
COM-013 à une lecture ponctuelle. Aucun abonnement ni connecteur obligatoire ;
nommer les accès optionnels et fournir la sortie partielle utile s'ils manquent.

## Sources à rechercher

Code civil/commerce, preuve, modification et cession ; eIDAS si pertinent ; jurisprudence et droit dans le temps à vérifier.

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

- Cas normal : Base et deux avenants signés fournis dans le désordre, effet rétroactif déclaré : chronologie et clause prix tracées sans confondre les dates.
- Cas limite : Avenant non signé et renvoi à une pièce absente : version candidate conditionnelle, aucune consolidation certifiée.
- Sans profil / sans source : garder une sortie préparatoire utile, aucune
  hypothèse américaine de remplacement ni conclusion non établie.

Exécuter sur pièces fictives ; conserver sorties, ressources lues et contrôles
par couche BASE-006, puis faire reformuler par un lecteur non juriste.
Ces scénarios sont **attendus, non exécutés** dans EXIST-001.

## Hors périmètre

Rédiger de nouveaux avenants, trancher une interprétation litigieuse ou certifier une signature.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-001, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; une sélection explicite de cette tranche reste nécessaire avant
son lancement. Les dépendances satisfaites ne valent pas validation du métier.
