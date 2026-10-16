---
id: HUB-002
titre: "Unifier la politique de confiance du hub"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001]
---

# HUB-002 — Unifier la politique de confiance du hub

## Objectif et résultat attendu

Le défaut restrictif est cohérent partout ; une politique absente, illisible ou mal formée n’entraîne aucune installation permissive implicite.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/references/allowlist-default.yaml` : adaptation ciblée.
- `legal-builder-hub/skills/skill-installer/references/allowlist.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/cold-start-interview/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/customize/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/README.md` : adaptation ciblée.
- `legal-builder-hub/references/trust-policy.md` : à créer, propriétaire HUB-002.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Politique active du fork, mode et listes validées, identité de source, décisions explicites de l’administrateur et contexte d’usage.

## Travail attendu

- Corriger le commentaire HTML initial de allowlist-default.yaml, chargé comme clé parasite par PyYAML ; garder le modèle installé en lecture seule et créer l’état actif via helper.
- Aligner README, interview, référence et installer : absence/erreur ne choisit pas permissive. Un changement de politique est une action explicite indépendante de l’installation.
- Séparer registries, publishers, connectors et licences ; une liste vide restrictive refuse les capacités correspondantes, un registre surveillé n’est pas automatiquement autorisé.
- Contrôler l’origine depuis données de transport/commande avant le contenu candidat ; traiter délégations, URL imbriquées et redirections sans étendre la confiance depuis le texte non fiable.

## Sources à rechercher lors de l'implémentation

BASE-008, schéma local, politique réellement décidée ; règles de confiance du produit à vérifier, sans qualifier les registres par leur seule présence dans un modèle.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] La même entrée obtient la même décision depuis interview, navigateur et installer ; aucun fallback silencieux.
- [ ] Le candidat ne peut ni élargir l’allowlist ni changer son mode via métadonnées, licence ou consigne.
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

- Cas normal : CF01 — Source et licence explicitement autorisées, aucun connecteur : gate satisfait mais revue/consentement toujours requis.
- Cas limite : CF02 — Politique absente ou YAML HTML parasite : expliquer l’état, aucune installation permissive ni réécriture automatique de la politique.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

