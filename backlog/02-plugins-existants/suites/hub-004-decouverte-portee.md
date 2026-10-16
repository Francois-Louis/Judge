---
id: HUB-004
titre: "Afficher la portée des skills découverts"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-003]
---

# HUB-004 — Afficher la portée des skills découverts

## Objectif et résultat attendu

Une fiche de découverte affiche juridiction, tâche, limites et statut de lecture ; un skill américain reste visiblement américain dans une recherche française.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/registry-browser/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/discovery-scope.md` : à créer, propriétaire HUB-004.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Requête, territoire/matière demandés, index/candidat accessibles et provenance ; la juridiction peut être inconnue.

## Travail attendu

- Séparer correspondance lexicale et pertinence juridique ; langue française, nom Judge ou sources bien citées ne prouvent pas une adaptation.
- Afficher FR/UE, État US nommé, multi-juridiction ou inconnu selon preuve, sans convertir une référence américaine en règle française.
- Distinguer portée déclarée par auteur et constatée dans les passages lus ; couverture partielle visible et pas recommandation principale comme solution FR si hors périmètre.
- Le navigateur montre un contenu non fiable et propose une revue ; il n’installe ni n’exécute le skill et ne suit pas ses instructions.

## Sources à rechercher lors de l'implémentation

Textes du candidat et sources déclarées effectivement lus ; vérification de matière/territoire ultérieure par sources officielles pertinentes, sans recherche juridique complète par défaut.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Le cas Californie de la vérification reste « US — Californie, hors portée France demandée », même si techniquement structuré.
- [ ] Sans texte, la portée reste non établie ; pas de badge FR depuis les seuls mots du titre.
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

- Cas normal : DP01 — Recherche France, candidat cite uniquement une procédure californienne : fiche signale explicitement l’écart et propose chercher une autre portée.
- Cas limite : DP02 — Description « international » sans références accessibles : inconnu/partiel, pas adapté FR/UE supposé.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

