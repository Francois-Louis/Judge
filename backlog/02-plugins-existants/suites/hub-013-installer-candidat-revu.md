---
id: HUB-013
titre: "Installer uniquement le candidat communautaire revu"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-008, HUB-019]
---

# HUB-013 — Installer uniquement le candidat communautaire revu

## Objectif et résultat attendu

Une installation active ne concerne que le candidat exact revu et autorisé, dans un nouveau chemin communautaire du fork.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/references/install-reviewed.md` : à créer, propriétaire HUB-013.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Fiche de candidat HUB-008, politique, décisions et autorité d’installation réelles, journal valide et destination absente.

## Travail attendu

- Conserver toutes gates : source/licence/capacités, brut/transformation, QA et limites FR/UE, puis accord sur les octets exacts ; --approved atteste le workflow et n’en est pas la preuve indépendante.
- Utiliser community_store.py existant après revue, sans copie directe, exécution du candidat ou dépendance à l’origine ; identité préfixée et destination exclusive.
- Refuser collision même répertoire vide, chemin interne/éditeur, lien/junction ou journal inconnu ; revalider les empreintes juste avant mutation.
- Le helper écrit le journal ; projection du profil après succès seulement. Installation disque ne prouve ni découverte par client ni exécution réussie.
- Corriger les mentions commit-or-tag : commit exact et transformations locales documentés, pas tag mutable.

## Sources à rechercher lors de l'implémentation

Dossier revu, journal actif et règles officielles d’installation du produit à vérifier ; mécanismes BASE-008 restent la frontière filesystem.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Le candidat changé après revue ne s’installe pas sous l’ancien accord.
- [ ] Paquet interne/éditeur et ancien journal ne sont jamais des destinations d’installation communautaire.
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

- Cas normal : IN01 — Candidat complet et chemin absent : helper, événement canonique et projection après succès, sans lancer le skill.
- Cas limite : IN02 — Répertoire occupé ou source différente depuis revue : refuser sans overwrite, préserver les deux arborescences.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

