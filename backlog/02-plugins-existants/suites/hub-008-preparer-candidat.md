---
id: HUB-008
titre: "Préparer un candidat exact pour la revue"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-002, HUB-009, HUB-010, HUB-011, HUB-012]
---

# HUB-008 — Préparer un candidat exact pour la revue

## Objectif et résultat attendu

Un dossier de revue montre l’intégralité du candidat épinglé, ses dépendances et les transformations prévues, avant activation.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/auto-updater/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/references/candidate-review.md` : à créer, propriétaire HUB-008.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Source autorisée, commit exact et sous-chemin ; SKILL, références, commandes, scripts, hooks, agents et MCP disponibles ; capacité de lecture isolée réelle.

## Travail attendu

- Séparer téléchargement/staging de revue, cache et installation active ; résoudre la contradiction « aucun fichier avant Step 7 » avec le téléchargement et les preuves, sans donner droit d’activer.
- Montrer source brute intégrale, fichiers annexes et changements de nom/préambule effectivement prévus ; si couverture tronquée, revue incomplète et aucune activation.
- Conserver lecture sans capacités de mutation pour le contenu non fiable ; restrictive requiert l’environnement isolé effectif, pas un simple nom de subagent ; ne pas proposer un downgrade automatique si indisponible.
- Préparer tous tokens de fraîcheur et licence avant la décision ; aucun préambule modifié après une approbation portant sur d’autres octets.
- Lier le dossier à commit, identité, arborescence, empreintes et versions des contrôles ; nouvelle version ou transformation invalide l’ancien accord.

## Sources à rechercher lors de l'implémentation

Contenu et métadonnées exacts du candidat, contrats locaux ; garanties réelles de permissions/lecture du produit à vérifier, sans confondre un prompt avec un sandbox.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Le candidat n’est jamais exécuté par fetch, QA ou staging.
- [ ] Tag/branche mutable, fichier manquant ou rapport partiel ne suffit pas à autoriser la copie.
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

- Cas normal : PC01 — Candidat épinglé complet : montrer brut, surfaces, transformation et rapports, sans installer.
- Cas limite : PC02 — Références manquantes ou scanner isolé indisponible en restrictive : limite visible et activation non réalisée, pas passage permissif automatique.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

