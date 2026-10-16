---
id: TRAV-006
titre: "Découper le parcours de rupture économique collective"
statut: proposee
priorite: P2
nature: cadrage
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-006 — Découper le parcours de rupture économique collective

## Objectif

Un salarié ou une petite structure évoque plusieurs suppressions d'emploi ; le parcours actuel ne peut pas les assimiler à une rupture personnelle.

Résultat : Arbre de qualification proposé et nouvelles stories bornées par procédure et acte observable.

## Périmètre

Plugin principal : `employment-legal`. Entrées à examiner : termination-review.
Fichiers source sous `employment-legal/skills/`, profil et références associées,
avec les dépendances décrites dans l'[inventaire PILOTE-001](../pilote-001-annexes/pilote-001-releve-inventaire.md).
Les fichiers à modifier seront arrêtés après lecture ; aucun fichier métier
n'est adapté par la présente proposition.

Entrées nécessaires : Effectifs et entités, nombre/période des mesures envisagées, lieux, documents et représentation collective déclarée.
Qualifier pour ce périmètre statut privé/public, qualité des personnes,
convention collective et accords pertinents, lieux exacts (outre-mer et
transfrontalier compris), dates et versions. Orienter ce qui sort de la tranche.

## Travail attendu

Cartographier les branches, seuils à rechercher, acteurs et dépendances ; séparer information du salarié, consultation et procédures collectives ; ne pas adapter tout le parcours dans ce cadrage.

Sources primaires à rechercher : Code du travail, accords collectifs et publications/jurisprudence officielles sur procédures économiques ; seuils et périodes non vérifiés à ce stade.
Ces pistes sont **non vérifiées pour cette story**. Lire les dispositions,
versions et transitions applicables lors de l'implémentation ; conserver
le relevé des accès et réserves BASE-005. Utiliser les voies officielles
alternatives de BASE-010 si une page web échoue, sans confondre lecture et validation.

Décrire pour les futures implémentations le chargement de la méthode locale,
les références à embarquer, la frontière de stockage BASE-008 et les accès
nécessaires/optionnels. Cette story de cadrage ne modifie pas le plugin.

## Critères d'acceptation

- [ ] Le résultat défini ci-dessus est observable sur le cas normal ci-dessous.
- [ ] La limite significative est traitée sans règle américaine de remplacement ni conclusion non établie.
- [ ] Règles collectives, statut réel, territoire et versions déterminants sont établis ou réservés explicitement.
- [ ] Chaque branche retenue produit une story bornée, avec entrées, sortie, dépendances et scénario propre.
- [ ] Une personne sans formation juridique comprend ce qui est établi, les pièces à demander et la prochaine démarche.
- [ ] Le découpage distingue les futurs lots du parcours collectif encore non adapté.

## Vérification

- Cas normal : Plusieurs mesures sur des périodes proches : questions de périmètre explicitement listées.
- Limite : Effectifs ou statut des mesures inconnus : aucun régime ni calendrier affirmé.

Relire l'arbre de qualification sur pièces fictives ; garder les questions,
orientations et nouvelles stories produites. Décrire la recette BASE-006 dans
les futures stories d'implémentation, sans déclarer un skill exécuté ici.
Pour cette proposition, **aucun scénario métier n'a été exécuté**.
Le livrable est un découpage documenté ; les scénarios vérifient l'orientation et les nouvelles stories, sans mise en œuvre du licenciement collectif.

## Hors périmètre

Mise en œuvre de licenciements collectifs, PSE complet, choix des salariés et calendrier exécutable.
Aucun envoi, dépôt, signature ni décision irréversible implicite.

## Bilan d'exécution

Proposition issue de PILOTE-001, le 15 octobre 2026. Implémentation et recette
restent à réaliser après PILOTE-003 ; les dépendances n'annoncent aucune
fonctionnalité adaptée déjà disponible.
