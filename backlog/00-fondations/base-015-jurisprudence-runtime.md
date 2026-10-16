---
id: BASE-015
titre: "Cadrer l'accès à la jurisprudence pendant l'exécution d'un skill"
statut: proposee
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

- [ ] Les sources sont inventoriées avec un accès réellement testé et daté.
- [ ] La méthode de citation et la conduite en cas d'échec sont écrites pour évolution de BASE-005.
- [ ] Le découpage produit des stories bornées, sans dépendance à PISTE.
- [ ] Aucune « mémoire » du modèle n'est présentée comme décision lue.

## Vérification

- Cas normal : décision de la Cour de cassation sur une clause de non-concurrence, retrouvée et lue avec ses motifs.
- Cas limite : aucun résultat sur les sites officiels → réponse réservée, piste et voie de recherche indiquées.
- Cas limite : seule une analyse doctrinale accessible → citée comme telle, décision non lue.

## Hors périmètre

Abonnement à une base payante, indexation complète des fonds DILA, conseil
sur l'issue d'un litige.
