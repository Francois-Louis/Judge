---
id: BASE-016
titre: "Intégrer la conduite sur les décisions de justice à la méthode BASE-005"
statut: proposee
priorite: P1
nature: implementation
dependances: [BASE-015, BASE-005, BASE-013]
---

# BASE-016 — Intégrer la conduite sur les décisions de justice à la méthode BASE-005

## Objectif

Tout skill adapté qui charge la méthode commune sait chercher, lire, citer
une décision de justice et réserver sa conclusion quand la recherche échoue,
sans abonnement PISTE. Issue du cadrage [BASE-015](../base-015-jurisprudence-runtime.md).

## Périmètre

- `references/research-citation-method.md` : version `1.2.0`, nouvelle section 10
  reprise de la [proposition BASE-015](../base-015-annexes/base-015-methode-jurisprudence.md)
  et renvois d'une phrase depuis les sections 3 à 5. Les sections existantes
  gardent leur numéro.
- Copie identique dans `<plugin>/references/shared/research-citation-method.md`
  des onze paquets ; renvois de version dans les skills adaptés qui citent
  `1.1.0`.
- [Modèle de story](../../story-template.md) : critère « toute décision citée
  est lue ou marquée comme piste, selon la section 10 ».

## Travail attendu

- Relire la proposition contre les voies observées le jour de l'intégration ;
  rejouer les adresses de la table 10.4 et corriger celles qui ont changé.
- Garder la méthode transverse : aucune décision sectorielle, aucun corpus.
- Version de patch de chaque plugin, NOTICE racine et locaux, marketplace,
  versions attendues de `scripts/test-base008-isolation.py`.

## Critères d'acceptation

- [ ] La section 10 distingue décision lue, résumé officiel, communiqué, conclusions, doctrine, résultat de moteur et mémoire.
- [ ] La fiche exige juridiction, formation, date, numéro, ECLI s'il est affiché, accès et passages des motifs lus.
- [ ] Les conduites « recherche vide », « décision inaccessible », « jurisprudence divergente », « décision ancienne et texte récent » et « aucun outil web » sont écrites avec une formulation utilisable.
- [ ] Les onze copies sont identiques à la source, contrôle à l'appui.
- [ ] Aucune voie ne dépend de PISTE ni d'un script du dépôt à l'exécution.

## Vérification

- `python scripts/test-base008-isolation.py`, `python scripts/check-version-bump.py`,
  comparaison des empreintes des onze copies, `backlog/etat.py --check`.
- Relecture : un lecteur suit la section 10 sur l'arrêt Cass. soc.,
  24 janvier 2024, n° 22-20.926, et produit une fiche complète.

## Hors périmètre

Recette dans un client isolé (BASE-017), mise à jour des références métier
(TRAV-062 et lots de chaque domaine), outils de maintenance (BASE-018).
