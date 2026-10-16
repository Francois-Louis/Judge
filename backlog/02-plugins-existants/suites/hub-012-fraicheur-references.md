---
id: HUB-012
titre: "Distinguer fraîcheur du code et des références"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-002]
---

# HUB-012 — Distinguer fraîcheur du code et des références

## Objectif et résultat attendu

Un état de fraîcheur documentaire distingue déclaration auteur, vérification effective et rappel, indépendamment d’un nouveau commit.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/skill-installer/references/freshness.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/auto-updater/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/skills-qa/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/cold-start-interview/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.
- `legal-builder-hub/references/reference-currency.md` : à créer, propriétaire HUB-012.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Tokens bruts puis validés, date de contrôle, seuils actifs et versions des pièces ; données journalisées sous metadata.

## Travail attendu

- Corriger l’explication « last_verified contre today + window » : échéance depuis last_verified plus fenêtre active ; définir jours/mois/années calendaires et comparaison des fenêtres à une même date.
- Dates futures, champs injectés, format invalide ou catégorie stable inadaptée restent inconnus/anomalies ; catégories ne prouvent aucune stabilité du droit.
- Valider avant préambule et approbation, n’injecter que tokens autorisés ; lire metadata du journal canonique, pas un chemin legacy de champs.
- URL affichée sans paramètres sensibles distincte de référence documentaire exacte nécessaire à la version ; ne pas perdre identifiant/version dans la preuve ni suivre une URL de candidat aveuglément.
- Rappel accepté ou refusé n’établit pas conformité actuelle ; commit nouveau ou last_verified avancé reste déclaration auteur, pas vérification de fond par le hub.

## Sources à rechercher lors de l'implémentation

Contrats BASE-005/008, pièces/source de vérification effective et règles de versions ; aucun seuil de quelques mois n’est une garantie juridique.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Même SHA mais fenêtre dépassée déclenche un état à revoir, pas mise à jour automatique.
- [ ] Un rappel suspendu ne marque pas la source vérifiée pour d’autres tâches ou dates.
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

- Cas normal : FR01 — SHA identique, sources datées au-delà du seuil : réserve et options de vérification, aucune réinstallation.
- Cas limite : FR02 — Nouveau commit de formatage et date auteur future/injectée : fraîcheur inconnue, pas « actualisé » ; données non interprétées.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

