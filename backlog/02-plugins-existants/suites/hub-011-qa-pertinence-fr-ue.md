---
id: HUB-011
titre: "Évaluer séparément la pertinence France et UE"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-004, HUB-010]
---

# HUB-011 — Évaluer séparément la pertinence France et UE

## Objectif et résultat attendu

Le rapport sépare sécurité, conception et pertinence documentaire pour la tâche/juridiction ; un skill US bien sourcé n’est pas qualifié prêt pour la France.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/skills-qa/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.
- `legal-builder-hub/references/qa-fr-eu.md` : à créer, propriétaire HUB-011.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Tâche demandée, territoire/date, corpus du candidat réellement lu, sources déclarées et couverture du contrôle.

## Travail attendu

- Ajouter portée déclarée/observée, sources primaires pertinentes, versions, limites et règles de routage à la revue de conception ; aucune moyenne ne compense une juridiction incompatible.
- Des références US exactes peuvent être bien attribuées tout en étant hors portée FR/UE ; afficher ce statut sans traduire ni appliquer leur doctrine.
- Retirer l’assurance universelle attachée à PRIVILEGED & CONFIDENTIAL et les généralisations de protection juridique ; marquage ≠ effet juridique, statut de professionnel ≠ validation.
- Supprimer « continuer sous framework US avec caveat » comme voie d’une tâche française ; conserver une aide méthodologique bornée ou recherche pertinente.
- Ne pas certifier le fond du droit : vérification ponctuelle exige textes lus/version/contexte et revue compétente distincte de la QA technique.

## Sources à rechercher lors de l'implémentation

Méthode BASE-005 et sources officielles FR/UE réellement pertinentes lors de l’implémentation ; la QA ne constitue pas une consultation ou une validation exhaustive du droit.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] La fixture Californie reste techniquement structurée mais hors portée France, jamais READY global pour ce besoin.
- [ ] Inconnu n’est pas conforme, cache récent et langue française ne certifient rien.
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

- Cas normal : QF01 — Skill procédure Californie sans risque technique détecté : trois dimensions séparées, juridiction US explicite et hors portée France.
- Cas limite : QF02 — Skill traduit en français mais articles/autorités US inchangés : aucune adaptation FR/UE reconnue, sources à rechercher et conclusion réservée.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

