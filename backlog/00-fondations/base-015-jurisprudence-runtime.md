---
id: BASE-015
titre: "Cadrer l'accès à la jurisprudence pendant l'exécution d'un skill"
statut: terminee
priorite: P1
nature: cadrage
dependances: [BASE-005, BASE-010]
---

# BASE-015 — Cadrer l'accès à la jurisprudence pendant l'exécution d'un skill

## Objectif

Définir comment un skill installé cherche et cite une décision de justice
pendant une réponse, sans abonnement PISTE, et ce qu'il dit quand aucune
décision n'est trouvée ou lisible. Décision de l'utilisateur du 16 octobre
2026 ([décisions](../decisions-2026-10-16.md)). Constat de départ : la
recette BASE-011 a montré un accès Légifrance refusé, un repli sur la Cour de
cassation sans résultat et une règle citée « de mémoire » hors réseau.

## Travail attendu

- Inventorier les sources officielles consultables par les outils d'une
  session : Légifrance, sites de la Cour de cassation, du Conseil d'État, du
  Conseil constitutionnel, de la CJUE et de la CEDH, données ouvertes ; tester
  leur accès réel et consigner les échecs, comme BASE-010.
- Distinguer décision lue, résumé officiel, communiqué et doctrine ; exiger
  juridiction, date, numéro et ECLI s'il existe, et la lecture des motifs.
- Prévoir la conduite à tenir : recherche vide, décision inaccessible,
  jurisprudence divergente, décision ancienne contredite par un texte récent.
- Décider ce qui reste au runtime (recherche ciblée par le skill) et ce qui
  relève de la maintenance (scripts BASE-010, références embarquées relues par
  BASE-014).
- Découper en stories d'implémentation bornées, sans promettre une recherche
  exhaustive.

## Critères d'acceptation

- [x] Les sources sont inventoriées avec un accès réellement testé et daté.
- [x] La méthode de citation et la conduite en cas d'échec sont écrites pour évolution de BASE-005.
- [x] Le découpage produit des stories bornées, sans dépendance à PISTE.
- [x] Aucune « mémoire » du modèle n'est présentée comme décision lue. *Règle écrite et scénarios joués par l'agent de maintenance ; comportement d'un skill installé à observer par BASE-017.*

## Vérification

- Cas normal : décision de la Cour de cassation sur une clause de non-concurrence, retrouvée et lue avec ses motifs.
- Cas limite : aucun résultat sur les sites officiels → réponse réservée, piste et voie de recherche indiquées.
- Cas limite : seule une analyse doctrinale accessible → citée comme telle, décision non lue.

## Hors périmètre

Abonnement à une base payante, indexation complète des fonds DILA, conseil
sur l'issue d'un litige.

## Bilan d'exécution — 17 octobre 2026

- **Inventaire.** [Accès testés](base-015-annexes/base-015-inventaire-acces.md)
  le 17 octobre 2026 par deux voies : outils web de la session
  ([journal S01 à S27](base-015-annexes/base-015-acces-session.json)) et HTTP
  direct ([sonde](base-015-annexes/base-015-sonde.py),
  [relevé](base-015-annexes/base-015-acces-http.json)). Légifrance (JURI,
  CETAT), le Conseil d'État, le Conseil constitutionnel et HUDOC (adresse de
  conversion) sont lisibles par l'outil web ; le site de la Cour de cassation,
  CURIA et EUR-Lex ne le sont pas ; CELLAR ne l'est que par une adresse de
  manifestation connue. Légifrance et HUDOC refusent le client HTTP direct
  (403) ; les fonds DILA de jurisprudence sont listés sans compte.
- **Méthode.** [Proposition de section 10](base-015-annexes/base-015-methode-jurisprudence.md)
  pour la méthode `1.2.0` : nature de ce qui est lu (de la décision lue à la
  mémoire du modèle), fiche d'une décision, lecture des motifs, ordre de
  recherche borné et voies observées, conduite pour huit situations d'échec,
  partage entre exécution (outil web seul, sans script ni PISTE) et
  maintenance (BASE-010, BASE-014, BASE-018, VEI-021). Non livrée : BASE-016.
- **Découpage.** [BASE-016, TRAV-062, BASE-017, BASE-018](base-015-annexes/base-015-decoupage.md),
  toutes `proposee`.
- **Constat hors périmètre.** L'arrêt Cass. soc., 21 septembre 2017,
  n° 16-20.103, noté inaccessible dans `employment-legal` 0.3.2, est diffusé
  sur Légifrance ; correction confiée à TRAV-062, plugin non modifié ici.
- **Vérification.** Les trois scénarios de la story, joués avec les outils
  d'une session : [résultats](base-015-annexes/base-015-verification.md).

## Portée

Voir la portée de la [vérification](base-015-annexes/base-015-verification.md) :
scénarios joués par l'agent de maintenance, pas par un skill installé ;
lectures WebFetch résumées par un modèle ; accès valables à la date et pour
les outils testés ; aucune recherche exhaustive ni analyse d'applicabilité.
Aucun plugin, aucune référence partagée et aucun script de `scripts/` ne sont
modifiés par cette story.
