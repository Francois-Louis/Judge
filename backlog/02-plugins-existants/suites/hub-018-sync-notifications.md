---
id: HUB-018
titre: "Séparer synchronisation et notifications"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-003, HUB-004, HUB-007]
---

# HUB-018 — Séparer synchronisation et notifications

## Objectif et résultat attendu

Un relevé de nouveautés ne fait aucune installation ; une notification externe exige canal/destinataire et autorisation réels, sinon résultat local.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/agents/registry-sync.md` : adaptation ciblée.
- `legal-builder-hub/.mcp.json` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.
- `legal-builder-hub/README.md` : adaptation ciblée.
- `legal-builder-hub/references/registry-notifications.md` : à créer, propriétaire HUB-018.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Watchlist et cache, politique active, préférences notify/manual, destination autorisée et capacité de notification réellement disponible.

## Travail attendu

- Conserver neutralisations BASE-009 : agent n’applique jamais, notification n’est ni accord d’update ni preuve d’installation.
- Distinguer cadence hebdomadaire décrite et scheduler effectivement configuré ; agent YAML/frontmatter et hooks vides ne planifient rien seuls.
- Borner outils Write au cache/état gardés et supprimer wildcard d’envoi Slack au profit de la capacité effectivement nécessaire dans le futur lot ; absence de capacité n’est pas succès.
- Sans instruction d’envoi explicite, préparer relevé local ; pas de message à un registre ou tiers déclenché par métadonnées non fiables.
- Relevé conserve erreurs par source et portées US/inconnues, pas « conforme FR » ni sync global réussi sur accès partiel.

## Sources à rechercher lors de l'implémentation

Configuration réelle du client/scheduler/connecteur et autorisation de destination ; règles produit à vérifier seulement pour les capacités effectivement retenues.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Notify n’exécute pas auto-updater --apply ; manual n’installe rien non plus.
- [ ] Échec d’envoi reste échec d’envoi, pas état delivered ni bascule vers un autre destinataire.
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

- Cas normal : SN01 — Sync autorisé sans Slack : digest local et sources réellement lues, aucune mise à jour appliquée.
- Cas limite : SN02 — Texte de registre demande message sur canal public ou annonce auto-applied : données ignorées comme instructions, aucun envoi ni changement.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

