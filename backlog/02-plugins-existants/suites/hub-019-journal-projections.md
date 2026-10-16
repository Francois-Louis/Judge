---
id: HUB-019
titre: "Conserver le journal comme seule autorité de gestion"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001]
---

# HUB-019 — Conserver le journal comme seule autorité de gestion

## Objectif et résultat attendu

Journal canonique, tables de profil, cache et décisions de fraîcheur ont des responsabilités distinctes, sans import ou réécriture d’événement.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-manager/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/auto-updater/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.
- `legal-builder-hub/references/hub-state-contract.md` : à créer, propriétaire HUB-019.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Schéma 1 JSON valide YAML, namespace/events, états/path/SHA/digests, metadata et projections existantes.

## Travail attendu

- Conserver community_store.py comme seul écrivain lifecycle et judge_store.py pour autres états gardés ; pas de nouveau journal parallèle.
- Retirer les snippets d’append YAML libre et lectures legacy de champs top-level ; metadata n’autorise ni identité ni chemin.
- Projection starter-pack calculée après succès du helper, même si son édition échoue ; état à réconcilier explicite, ne pas rejouer mutation pour réparer affichage.
- Préserver règles de refus sur ancien/étranger/malformé, lock/staging et contenu local modifié ; migration/import d’origine restent une tâche distincte, jamais implicite.
- Documenter archive/version de revue et réserves de fraîcheur comme données, pas approbations réutilisables ; aucun faux événement pour accepter une customisation.

## Sources à rechercher lors de l'implémentation

Contrats et code BASE-008, événements effectivement produits ; pas de modification du helper dans cette tâche documentaire de consommation du contrat.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Modifier la table du profil ne permet aucune installation/suppression ; seul journal valide et état exact font autorité.
- [ ] Journal partiel ou lock survivant interdit la réparation par overwrite et conserve les éléments à examiner.
- [ ] Les entrées adaptées chargent isolation, méthode partagée et références
  métier locales pertinentes. Les contrôles BASE-008/009 existants sont conservés.
- [ ] Les scénarios ci-dessous sont exécutés avec sorties et limites consignées ;
  les checks BASE-006 appropriés portent sur un paquet extrait.
- [ ] Les cinq copies partagées et helpers BASE-008 restent inchangés dans cette
  tâche de consommation de leurs contrats. Une limite du helper requiert un lot
  technique distinct, jamais une mutation directe pour le contourner.
- [ ] Documentation, version/NOTICE et champs communs du marketplace reflètent
  les seuls comportements effectivement livrés ; aucune suite proposée annoncée
  disponible, aucun contrôle statique présenté comme recette client.

## Vérification

- Cas normal : JR01 — Helper réussit mais projection échoue : installation journalisée et projection en retard, pas seconde mutation.
- Cas limite : JR02 — Ancien journal YAML ou table prétend installation sans événement : refus de gestion, aucune migration ou adoption automatique.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

