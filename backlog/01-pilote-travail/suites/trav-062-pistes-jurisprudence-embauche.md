---
id: TRAV-062
titre: "Requalifier les pistes jurisprudentielles de la revue d'embauche"
statut: terminee
priorite: P1
nature: implementation
dependances: [BASE-016, BASE-014]
---

# TRAV-062 — Requalifier les pistes jurisprudentielles de la revue d'embauche

## Objectif et résultat attendu

La référence `employment-legal/references/hiring-review-fr.md` cite ses deux
décisions avec une fiche conforme à la section 10 de la méthode `1.2.0`,
au lieu de pistes marquées illisibles. Constat du cadrage
[BASE-015](../../00-fondations/base-015-jurisprudence-runtime.md) le
17 octobre 2026 : l'arrêt Cass. soc., 21 septembre 2017, n° 16-20.103, noté
`inaccessible` dans la version 0.3.2, est diffusé sur Légifrance
(JURITEXT000035616989) ; l'arrêt du 10 juillet 2002 est lisible mais reste
présenté comme piste, sans recherche des évolutions.

## Périmètre et fichiers

Propriétaire : `employment-legal`. Fichiers :
`employment-legal/references/hiring-review-fr.md` (section « Lectures
manquantes »), `employment-legal/skills/hiring-review/SKILL.md` si un renvoi
change, NOTICE locale et racine, version du plugin.

## Travail attendu

- Lire les deux décisions sur Légifrance (motifs et dispositif) et remplir
  leur fiche ; corriger l'adresse de l'arrêt de 2017.
- Rechercher, de façon bornée, les décisions publiées postérieures sur la
  contrepartie et la validité de la clause de non-concurrence ; les intégrer
  seulement après lecture, en indiquant que la recherche n'est pas exhaustive.
- Colonne `Relecture` à jour (BASE-014) pour chaque décision.

## Critères d'acceptation

- [x] Chaque décision citée porte juridiction, formation, date, numéro, ECLI s'il est affiché, adresse Légifrance et passage lu.
- [x] Aucune décision n'est citée sans lecture ; une décision restée illisible garde sa réserve.
- [x] `python scripts/source_reviews.py employment-legal --depuis <date>` passe sans erreur.
- [x] La revue d'un contrat avec clause de non-concurrence se termine par la phrase de la section 8 (BASE-013).

## Vérification

- Cas normal : contrat fictif avec clause sans contrepartie ; la note cite la décision lue et la condition de contrepartie.
- Cas limite : décision illisible le jour du lot ; réserve maintenue, lot non bloqué si la réserve est consignée.

## Hors périmètre

Autres clauses (TRAV-057, TRAV-058), autres références du plugin, recette en client isolé (BASE-017).

## Bilan d'exécution — 17 octobre 2026

- **Lectures.** Les deux arrêts ont été ouverts sur Légifrance avec l'outil
  de lecture web de la session de maintenance : identité, visa, motifs et
  dispositif restitués littéralement par fragments (l'outil résume les pages
  et borne la longueur des citations). L'arrêt de 2017 est lu à
  JURITEXT000035616989 (ECLI:FR:CCASS:2017:SO02063) ; l'ancienne adresse du
  site de la Cour est retirée.
- **Recherche bornée.** Une recherche Légifrance (« clause de non-concurrence
  contrepartie financière dérisoire », 141 résultats, première page lue) ;
  deux arrêts publiés de la chambre sociale ouverts et intégrés :
  15 novembre 2006, n° 04-46.721, et 16 mai 2012, n° 11-10.760. Levée,
  renonciation, réduction par le juge, réparation et inédits non recherchés :
  listés dans les lectures manquantes.
- **Paquet.** `hiring-review-fr.md` 1.1.0, `employment-legal` 0.3.5 ; aucun
  renvoi du skill ne change. NOTICE locale et racine.
- **Contrôles.** `source_reviews.py employment-legal --depuis 2026-10-17` :
  0 erreur, 45 relectures ; `check-version-bump.py` réussi ;
  `test-base008-isolation.py` : 16 tests OK (2 ignorés) ;
  `test-source-reviews.py` OK sous `PYTHONUTF8=1` (sans, un test échoue au
  décodage de la sortie console Windows, avant comme après ce lot) ;
  `claude plugin validate` du marketplace et du paquet : réussi (avertissement
  attendu sur `CLAUDE.md`).
- **Critère 4 et cas normal.** Observés le 17 octobre 2026 dans le scénario
  S1 de [BASE-017](../../00-fondations/suites/base-017-recette-jurisprudence-runtime.md)
  (client isolé, paquet 0.3.5) : la note cite l'arrêt de 2002 lu sur
  Légifrance et la condition de contrepartie, et se termine par la phrase de
  la section 8. Le cas limite (décision illisible) ne s'est pas produit.

## Portée

Les passages cités viennent de la restitution d'un outil qui résume la page ;
aucune lecture du texte brut de Légifrance. La recherche n'est pas
exhaustive et aucune relecture juridique indépendante n'a été faite.
