---
id: BASE-018
titre: "Lire une décision par son identifiant dans les fonds de jurisprudence DILA"
statut: proposee
priorite: P2
nature: implementation
dependances: [BASE-010, BASE-015]
---

# BASE-018 — Lire une décision par son identifiant dans les fonds de jurisprudence DILA

## Objectif

Le mainteneur relit une décision citée par une référence embarquée même quand
Légifrance refuse l'outil, à partir des données ouvertes de la DILA, sans
compte. Issue du cadrage [BASE-015](../base-015-jurisprudence-runtime.md) :
Légifrance répond 403 au client HTTP direct et `dila-read` exige de connaître
l'archive qui contient la décision.

## Périmètre

Outil de maintenance `scripts/legal_sources.py` et ses tests ; procédure
[accès aux sources](../../../references/legal-source-access.md). Fonds CASS,
INCA, CAPP (absent de l'outil au 17 octobre 2026), JADE et CONSTIT. Pas
d'usage pendant la réponse d'un skill.

## Travail attendu

- Ajouter le fonds CAPP à la liste des fonds lisibles.
- Retrouver un identifiant (`JURITEXT…`, `CETATEXT…`, `CONSTEXT…`) en lisant
  en flux le dernier stock complet puis les lots postérieurs, comme pour les
  versions d'articles LEGI ; rien n'est écrit sur le disque.
- Restituer identité, juridiction, date, numéro, ECLI, texte et empreintes ;
  un identifiant absent des archives lues est signalé comme tel.
- Bornes de taille et de durée documentées ; tests hors ligne sur archives fictives.

## Critères d'acceptation

- [ ] Une décision de la Cour de cassation citée par `employment-legal` est lue par son identifiant sans Légifrance.
- [ ] Un identifiant absent, une archive en échec et un dépassement de borne ne sont pas des succès.
- [ ] La procédure dit que cette voie relève de la maintenance, pas de l'exécution.

## Vérification

Tests hors ligne de `scripts/test-legal-sources.py` ; une lecture réseau réelle consignée en annexe.

## Hors périmètre

Recherche plein texte, index local complet, API Judilibre ou Légifrance.
