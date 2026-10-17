---
id: BASE-016
titre: "Intégrer la conduite sur les décisions de justice à la méthode BASE-005"
statut: terminee
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

- [x] La section 10 distingue décision lue, résumé officiel, communiqué, conclusions, doctrine, résultat de moteur et mémoire.
- [x] La fiche exige juridiction, formation, date, numéro, ECLI s'il est affiché, accès et passages des motifs lus.
- [x] Les conduites « recherche vide », « décision inaccessible », « jurisprudence divergente », « décision ancienne et texte récent » et « aucun outil web » sont écrites avec une formulation utilisable.
- [x] Les onze copies sont identiques à la source, contrôle à l'appui.
- [x] Aucune voie ne dépend de PISTE ni d'un script du dépôt à l'exécution.

## Vérification

- `python scripts/test-base008-isolation.py`, `python scripts/check-version-bump.py`,
  comparaison des empreintes des onze copies, `backlog/etat.py --check`.
- Relecture : un lecteur suit la section 10 sur l'arrêt Cass. soc.,
  24 janvier 2024, n° 22-20.926, et produit une fiche complète.

## Hors périmètre

Recette dans un client isolé (BASE-017), mise à jour des références métier
(TRAV-062 et lots de chaque domaine), outils de maintenance (BASE-018).

## Bilan d'exécution — 17 octobre 2026

- **Méthode `1.2.0`.** [Source](../../../references/research-citation-method.md) :
  section 10 « Rechercher, lire et citer une décision de justice » reprise de
  la [proposition BASE-015](../base-015-annexes/base-015-methode-jurisprudence.md)
  (nature de ce qui est lu, fiche, lecture des motifs, ordre de recherche
  borné à trois recherches et trois décisions, voies observées, huit
  conduites d'échec et deux formulations) ; renvois d'une phrase dans les
  sections 3, 4 et 5. Les sections 1 à 9 gardent leur numéro. Voies rejouées
  le jour même, aucune correction nécessaire.
- **Synchronisation.** Copie identique dans les onze paquets ; versions
  0.1.2, `commercial-legal` 0.2.2, `employment-legal` 0.3.4 ; marketplace,
  versions attendues du test BASE-008, NOTICE racine et locales.
- **Renvois.** `hiring-review` et `worker-classification` suivent la
  section 10 pour les décisions au lieu de désigner le site de la Cour de
  cassation ou les archives DILA, illisibles ou réservées à la maintenance ;
  `review`, l'orientation commerciale, les deux références et le profil
  modèle d'`employment-legal` citent `1.2.0`. README racine et du plugin.
- **Modèle de story.** Critère « décision lue ou présentée comme piste,
  aucune décision restituée de mémoire ».
- **Vérification.** [Voies rejouées, fiche de l'arrêt n° 22-20.926 et
  contrôles du dépôt](base-016-annexes/base-016-verification.md).

## Portée

Voir la portée de la [vérification](base-016-annexes/base-016-verification.md) :
aucun skill installé n'a été exécuté (BASE-017) ; relecture par l'agent
rédacteur ; aucune règle de droit ajoutée. `employment-legal` part de
0.3.3, publiée pendant cette story par le suivi BASE-014 (voie LEGI des
versions futures, `b0d3ba2`) ; les contrôles ont été rejoués sur cette base.
