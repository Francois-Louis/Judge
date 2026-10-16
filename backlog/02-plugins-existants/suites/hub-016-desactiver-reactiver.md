---
id: HUB-016
titre: "Désactiver et réactiver un skill suivi"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-019]
---

# HUB-016 — Désactiver et réactiver un skill suivi

## Objectif et résultat attendu

Une seule identité communautaire suivie change d’état via helper, avec fichiers/prérequis et limites de prise d’effet visibles.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/disable/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-manager/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/references/activation-review.md` : à créer, propriétaire HUB-016.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Journal valide, chemin/digest exacts, état enabled/disabled et liste des entrées/hooks/agents à renommer.

## Travail attendu

- Conserver skill-manager non invocable et disable comme entrée publique ; pas de seconde commande ou moteur de rename.
- Retirer les renames directs et append YAML hérités de la référence : helper seul propriétaire, pas table de profil comme preuve d’autorité.
- Montrer changements avant action et collision possible ; refuser fichier édité, interne, éditeur ou identité inconnue.
- Désactivation sur disque ne prouve pas arrêt d’un processus, suppression de tâche planifiée externe ou rechargement client ; préciser les limites réelles et contrôles effectifs.
- Réactivation n’efface pas réserves de sécurité/fraîcheur ni données de configuration.

## Sources à rechercher lors de l'implémentation

Contrat BASE-008 et capacités réelles de découverte/rechargement du produit, à vérifier sans déduire un scheduler d’un fichier agent.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Une collision de fichier disabled ne produit aucun écrasement ni état de réussite fictif.
- [ ] Aucun agent ou hook d’un autre plugin n’est désactivé par le contenu du candidat.
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

- Cas normal : AC01 — Identité communautaire intacte : lister puis renommer via helper, événements et projection cohérents.
- Cas limite : AC02 — Skill édité ou hook externe encore actif : garder refus/limite visible, ne pas annoncer que toute exécution a cessé.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

