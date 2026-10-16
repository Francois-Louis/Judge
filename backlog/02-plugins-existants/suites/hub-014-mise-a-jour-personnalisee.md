---
id: HUB-014
titre: "Préserver les adaptations lors d’une mise à jour"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-008, HUB-019]
---

# HUB-014 — Préserver les adaptations lors d’une mise à jour

## Objectif et résultat attendu

Une mise à jour compare version source de base, installation réelle et nouveau candidat ; les modifications locales sont préservées et aucune fusion n’est appliquée silencieusement.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/auto-updater/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/references/local-update-review.md` : à créer, propriétaire HUB-014.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Événement source, empreinte installée lue, base connue, nouveau commit et dossier revu ; la base peut manquer.

## Travail attendu

- Conserver notify/manual et accord par version issus de BASE-009 ; vérification de disponibilité distincte d’application.
- Présenter diff depuis l’état réellement installé, y compris renommage/préambule et références locales ; le seul diff upstream ancien→nouveau ne couvre pas l’adaptation.
- Si empreinte locale diffère du journal, garder le refus existant du helper, fournir comparaison/export des seules pièces autorisées et une tâche séparée de réconciliation ; ne pas réécrire le journal pour rendre les octets acceptables.
- Ne pas inventer la base absente ni écraser les deux versions en résolvant automatiquement un conflit ; restauration sauvegardée n’est pas fusion.
- Nouvelle revue de source/licence/QA/fraîcheur et accord exact si candidat réconcilié explicitement dans un lot futur ; backups vérifiés avant remplacement, aucune édition de contenu éditeur.

## Sources à rechercher lors de l'implémentation

Trois états effectifs si disponibles, journal/empreintes BASE-008, dossier de revue ; règles actuelles du produit pour chargement, distinctes de la préservation disque.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] La fixture de modification locale refuse l’update et laisse octets/journal inchangés.
- [ ] Un commit proposé ne certifie ni fraîcheur juridique ni maintien de la portée France/UE.
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

- Cas normal : MA01 — Installation suivie inchangée et nouveau candidat revu : diff, gates, accord puis helper et sauvegarde ; pas application pendant sync.
- Cas limite : MA02 — Référence personnalisée modifiée après installation : refus preserve-and-compare, aucun update event, ni perte ni modification automatique du journal.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

