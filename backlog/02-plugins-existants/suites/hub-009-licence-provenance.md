---
id: HUB-009
titre: "Documenter la licence d’un candidat"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-002]
---

# HUB-009 — Documenter la licence d’un candidat

## Objectif et résultat attendu

Une fiche conserve licence déclarée, pièce effectivement lue, correspondance et limites selon l’usage prévu, sans autoriser une licence depuis du texte non fiable.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-installer/references/allowlist.md` : adaptation ciblée.
- `legal-builder-hub/skills/cold-start-interview/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/candidate-license.md` : à créer, propriétaire HUB-009.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Métadonnées du registre et LICENSE/NOTICE du candidat exact, contexte personnel/interne/distribution réellement indiqué, politique de licences active.

## Travail attendu

- Garder gate licence séparé de la confiance publisher ; autorisation d’un registre ne vaut pas acceptation de toutes ses licences.
- Traiter tokens SPDX et textes comme données, avec provenance/écarts ; une reconnaissance syntaxique ne conclut pas seule aux droits effectivement accordés ni obligations satisfaites.
- Retirer les affirmations générales « telle licence est fine en interne » ou droit acquis par install ; cas inconnu/personnalisé réserve bornée et revue compétente si nécessaire.
- Conserver refus restrictif si licence absente/hors politique/mismatch ; aucune inscription de licence dans l’allowlist depuis le candidat.
- Ne pas altérer contenus éditeur ou attributions, ni envoyer une demande au mainteneur sans instruction explicite.

## Sources à rechercher lors de l'implémentation

Licence/NOTICE exacts et politique effective ; sources officielles des licences et examen juridique du contexte seulement si une conclusion d’usage doit être rendue.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Mismatch entre métadonnées et fichier garde les deux preuves et le blocage applicable.
- [ ] Les textes bruts ne deviennent ni instruction ni politique, aucune conclusion de droit de distribution non vérifiée.
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

- Cas normal : LC01 — MIT déclarée et fichier concordant, autorisée : fiche sourcée, autres gates toujours nécessaires.
- Cas limite : LC02 — Métadonnées MIT mais fichier différent ou prose injectée : anomalie/politique appliquée, aucune licence ajoutée à la liste.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

