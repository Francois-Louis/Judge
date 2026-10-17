---
id: TRAV-062
titre: "Requalifier les pistes jurisprudentielles de la revue d'embauche"
statut: proposee
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

- [ ] Chaque décision citée porte juridiction, formation, date, numéro, ECLI s'il est affiché, adresse Légifrance et passage lu.
- [ ] Aucune décision n'est citée sans lecture ; une décision restée illisible garde sa réserve.
- [ ] `python scripts/source_reviews.py employment-legal --depuis <date>` passe sans erreur.
- [ ] La revue d'un contrat avec clause de non-concurrence se termine par la phrase de la section 8 (BASE-013).

## Vérification

- Cas normal : contrat fictif avec clause sans contrepartie ; la note cite la décision lue et la condition de contrepartie.
- Cas limite : décision illisible le jour du lot ; réserve maintenue, lot non bloqué si la réserve est consignée.

## Hors périmètre

Autres clauses (TRAV-057, TRAV-058), autres références du plugin, recette en client isolé (BASE-017).
