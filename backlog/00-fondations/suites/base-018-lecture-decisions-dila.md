---
id: BASE-018
titre: "Lire une décision par son identifiant dans les fonds de jurisprudence DILA"
statut: terminee
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

- [x] Une décision de la Cour de cassation citée par `employment-legal` est lue par son identifiant sans Légifrance.
- [x] Un identifiant absent, une archive en échec et un dépassement de borne ne sont pas des succès.
- [x] La procédure dit que cette voie relève de la maintenance, pas de l'exécution.

## Vérification

Tests hors ligne de `scripts/test-legal-sources.py` ; une lecture réseau réelle consignée en annexe.

## Hors périmètre

Recherche plein texte, index local complet, API Judilibre ou Légifrance.

## Bilan d'exécution — 19 octobre 2026

- `scripts/legal_sources.py` : fonds CAPP ajouté ; commande `juri-read
  <CASS|INCA|CAPP|JADE|CONSTIT> <identifiant>`. Le préfixe est contrôlé par fonds
  (`JURITEXT`, `CETATEXT`, `CONSTEXT`). L'outil lit en flux le dernier stock
  `Freemium_<fonds>_global_*` puis chaque lot postérieur, sans rien écrire sur
  le disque ; la dernière publication l'emporte, une liste de suppression la
  retire. Sortie : identité, juridiction, formation, date, numéros, ECLI,
  solution, publication, décision attaquée, texte, XML, SHA-256 de l'archive
  et du XML, occurrences. Sommaire, analyses et rapprochements sont séparés
  du texte, comme éditoriaux. La sélection du stock LEGI réutilise la même
  fonction, sans changer son comportement.
- Échecs distincts d'un succès (`state: unavailable`, code de sortie 1) :
  `absent-des-archives-lues`, `lecture-incomplete` (archive en échec, borne de
  membres, de taille ou de durée), `copies-divergentes`, `xml-invalide`. Bornes :
  celles des archives LEGI et 180 minutes par défaut (`--max-minutes` 1–600).
- [`scripts/test-legal-sources.py`](../../../scripts/test-legal-sources.py) :
  38 tests hors ligne réussis, dont 8 nouveaux sur archives fictives. Les
  fixtures reprennent la structure observée dans les vrais XML (`SCT`/`ANA`,
  `CITATION_JP`). Une première version lisait le sommaire au mauvais endroit :
  l'écart a été vu sur le XML réel, puis corrigé et couvert par un test.
- [Lecture réseau réelle](base-018-annexes/base-018-lecture-reseau.json) :
  `JURITEXT000007046365` (Cass. soc., 10 juillet 2002, n° 00-45.135, cité par
  [hiring-review-fr.md](../../../employment-legal/references/hiring-review-fr.md))
  est lu sans Légifrance dans le stock CASS (248 Mio) et ses 55 lots postérieurs,
  en 61 s. Les cinq passages cités par la fiche (motifs, visa de l'article
  L. 120-2, dispositif) figurent dans le texte ; solution et décision attaquée
  concordent ; l'ECLI est vide dans le XML comme dans la fiche. Une lecture
  CONSTIT (`CONSTEXT000054148611`, 23 archives, 7 s) éprouve une autre famille
  d'identifiants. INCA, CAPP et JADE : tests hors ligne seulement.
- [Procédure d'accès](../../../references/legal-source-access.md) : section
  dédiée, qui pose la voie comme outil de maintenance, sans usage pendant la
  réponse d'un skill. Le CLAUDE.md du dépôt cite la commande.
- Non fait, conformément au hors-périmètre : recherche plein texte, index
  local, API. La fiche de `hiring-review-fr.md` n'a pas été modifiée : la
  lecture confirme les passages cités, sans nouvelle relecture BASE-014.
