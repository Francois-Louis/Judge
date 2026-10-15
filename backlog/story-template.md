# Modèle de story

Copier ce modèle dans le domaine concerné. Une story de cadrage produit un
inventaire ou des stories plus précises ; une story d'implémentation produit
une modification utilisable et vérifiable. Ne pas mélanger ces deux résultats.

```yaml
id: DOMAINE-XXX
titre: Une tâche et un résultat précis
statut: proposee
priorite: P2
nature: cadrage
dependances: []
```

## Objectif

Quel problème cette story résout et quel résultat concret doit exister à la fin ?

## Périmètre

- Plugin et tâche concernés.
- Entrées nécessaires, sortie attendue et cas pris en charge.
- Situation concrète et personne concernée ; ne pas présumer un utilisateur avocat ou service juridique.
- Fichiers à examiner ; arrêter les fichiers à modifier après examen.

## Travail attendu

- Étapes spécifiques à cette tâche.
- Sources primaires à consulter lors de l'implémentation, avec leur version
  applicable et leur statut réel de vérification.
- Profils, références, agents ou connecteurs directement touchés.

## Critères d'acceptation

- [ ] Le comportement attendu est observable sur une demande concrète.
- [ ] Le cas normal et au moins une limite significative sont couverts.
- [ ] La tâche ne dépend pas d'un fichier absent du plugin installé.
- [ ] Les limites du résultat sont documentées sans promettre l'adaptation du domaine entier.
- [ ] La sortie explique la somme, l'obligation, les pièces ou la démarche utile en langage clair, sans présumer un abus ni garantir une issue favorable.

## Vérification

Décrire des scénarios et résultats attendus, pas une simple recherche de mots-clés.
À l'exécution, ajouter les résultats observés et les limites de vérification.

## Hors périmètre

Ce qui doit rester dans une autre story.

## Bilan d'exécution

À remplir au cours du travail : changements, contrôles réellement effectués,
références juridiques effectivement consultées le cas échéant, points ouverts
et suites justifiées. Aucun élément ne doit être déclaré réalisé par anticipation.
