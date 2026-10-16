---
id: HUB-015
titre: "Restaurer une sauvegarde communautaire identifiée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-010, HUB-012, HUB-019]
---

# HUB-015 — Restaurer une sauvegarde communautaire identifiée

## Objectif et résultat attendu

Un rollback restaure uniquement une sauvegarde enregistrée et intacte, après revue de sa portée et des écarts ; ce n’est pas une garantie de validité actuelle.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/auto-updater/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/references/rollback-review.md` : à créer, propriétaire HUB-015.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Identité suivie, SHA exact de backup, état actuel, empreintes et métadonnées historiques ; risque et source de demande.

## Travail attendu

- Exiger --sha cohérent dans tous exemples, chemin/digest/identité du backup égaux au journal ; pas de tag ou fichier arbitraire.
- Montrer différence avec actuel et points historiques : fraîcheur/portée/capacités peuvent être devenues inadéquates ; refus de sécurité non contourné par rollback.
- Préserver l’état remplacé via helper et refuser chemin de backup occupé ou contenu local édité ; ne pas écraser une sauvegarde pour réparer.
- Échec/lock/staging incohérent donne état à examiner, pas réparation destructive ni accord hérité réutilisé.

## Sources à rechercher lors de l'implémentation

Journal/backups exacts et contrôles BASE-008 ; nouvelles vérifications de sources si un ancien contenu doit servir au droit actuel.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Backup modifié/étranger et installation localement éditée empêchent la restauration.
- [ ] Succès physique distinct de rechargement client et de validité juridique.
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

- Cas normal : RV01 — Backup journalisé intact et cible inchangée : revue, accord et restauration via helper avec trace.
- Cas limite : RV02 — Backup altéré ou destination de sauvegarde déjà occupée : refus en préservant tous octets, pas suppression de collision.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

