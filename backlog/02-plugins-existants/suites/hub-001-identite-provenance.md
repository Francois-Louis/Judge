---
id: HUB-001
titre: "Identifier l’origine et la version d’un skill"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009]
---

# HUB-001 — Identifier l’origine et la version d’un skill

## Objectif et résultat attendu

Une fiche distingue paquet interne du fork, skill communautaire suivi, copie personnalisée et contenu éditeur ; provenance et chemin ne sont jamais déduits du seul nom.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/auto-updater/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-manager/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/references/candidate-identity.md` : à créer, propriétaire HUB-001.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

URL/dépôt et sous-chemin, commit exact, identité déclarée, chemin installé canonique et journal du fork s’ils existent ; état local réellement lu.

## Travail attendu

- Documenter origine, type de distribution, upstream slug, identité préfixée, commit source, empreinte des fichiers installés et lien éventuel vers une base revue.
- Distinguer customisation d’un paquet interne, copie communautaire personnalisée et contenu éditeur ; un préfixe Judge ou une déclaration de publisher ne prouve pas leur origine.
- Conserver la liste canonique de douze internes et les chemins protégés ; le hub ne met à jour ni ces paquets ni les plugins éditeur, même si une source ressemble à une entrée communautaire.
- Un chemin inconnu ou journal absent reste non gérable ; ne pas reconstruire l’autorité depuis un profil, un cache, l’origine ou le candidat.

## Sources à rechercher lors de l'implémentation

Contrats BASE-008 et manifeste local ; preuves de provenance et règles officielles du produit à vérifier lors de l’implémentation.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Chaque opération future cible une identité et des octets réellement identifiés, sans collision par homonymie.
- [ ] Un contenu éditeur/interne n’est jamais transformé en communautaire afin de permettre une mutation.
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

- Cas normal : ID01 — Skill communautaire suivi et copie locale : montrer provenance, commit et empreinte séparés.
- Cas limite : ID02 — Un candidat prend le nom commercial-legal ou un nom préfixé protégé : aucune installation/mise à jour sur un paquet interne ; origine inconnue reste inconnue.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

