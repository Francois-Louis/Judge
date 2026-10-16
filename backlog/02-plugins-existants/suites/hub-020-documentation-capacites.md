---
id: HUB-020
titre: "Documenter les capacités réellement livrées du hub"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-002, HUB-004, HUB-010, HUB-011, HUB-018, HUB-019]
---

# HUB-020 — Documenter les capacités réellement livrées du hub

## Objectif et résultat attendu

La documentation distingue découverte, revue, gestion du communautaire et effets effectifs ; aucune promesse de validation juridique ou de fonctionnement passif non installé.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/README.md` : adaptation ciblée.
- `legal-builder-hub/.claude-plugin/plugin.json` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.


Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Lots effectivement livrés, commandes canoniques, hooks/agent/outils réels, résultats de validation et limites connues.

## Travail attendu

- Documenter dix skills dont neuf invocables, skill-manager référence et registry-sync agent séparé ; ajouter customize aux commandes publiques manquantes.
- Afficher origine/fork/communauté/éditeur, pertinence FR/UE et gates cohérentes sans badge « légalement fiable » issu d’une QA technique.
- Expliquer registres surveillés versus sources autorisées, défaut restrictif et table de profil versus journal, sans conseiller l’édition du modèle installé.
- Retirer promesses de routine passive, alertes ou arrêt immédiat par rename si elles ne sont pas démontrées ; montrer usage local utile sans intégration.
- Mettre version/NOTICE et champs communs marketplace en cohérence si métadonnées changent ; ne pas annoncer une autre suite proposée comme livrée.

## Sources à rechercher lors de l'implémentation

Fichiers et résultats du lot réellement livré, documentation officielle du produit pour effets observés ; aucun compte de registre ni service disponible affirmé sans lecture.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Le lecteur voit quelles tâches exigent une action et lesquelles ont réellement une capacité externe configurée.
- [ ] Un contrôle statique, une recette client et une revue du fond juridique sont présentés comme résultats distincts.
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

- Cas normal : DC01 — Lot de découverte livré seul : README annonce fiches de portée et limites, sans promettre nouvelle gestion d’update ou planification.
- Cas limite : DC02 — Liste de contrôles propre avec candidat Californie : aucune affirmation de compatibilité juridique France ou label global READY.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

