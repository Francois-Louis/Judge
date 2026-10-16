---
id: HUB-017
titre: "Désinstaller uniquement le skill communautaire suivi"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-019]
---

# HUB-017 — Désinstaller uniquement le skill communautaire suivi

## Objectif et résultat attendu

Une suppression bornée retire le seul répertoire suivi après présentation des chemins, en conservant configuration et sauvegardes.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/uninstall/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-manager/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/community-lifecycle.md` : adaptation ciblée.
- `legal-builder-hub/references/uninstall-review.md` : à créer, propriétaire HUB-017.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Identité/journal/empreinte actuels, chemins réellement résolus et décision explicite sur cette suppression.

## Travail attendu

- Le journal est seule autorité filesystem ; table starter pack informative et anciens snippets YAML non utilisés en écriture.
- Vérifier chemins/ancêtres/liens et tout fichier local modifié ; aucune suppression de paquet interne ou éditeur ni adoption d’une installation manuelle.
- Conserver configuration et backups par défaut, en afficher les limites de conservation ; suppression complémentaire nécessite tâche distincte.
- Appeler helper, enregistrer uninstall, puis projection ; aucune récupération par suppression récursive d’un chemin recalculé à partir du candidat.

## Sources à rechercher lors de l'implémentation

Journal et frontière BASE-008 ; règles de conservation réellement convenues et état disque, sans supposer suppression distante ou désinscription d’un service.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Un skill non suivi ou localement édité est préservé avec raison concrète.
- [ ] Retirer un skill n’efface pas le journal, les preuves ni les données d’un autre contexte.
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

- Cas normal : DS01 — Skill suivi intact disabled : chemins affichés, suppression via helper, configuration et backups conservés.
- Cas limite : DS02 — Candidat demande de supprimer commercial-legal ou un dossier arbitraire : aucune suppression ni message de succès.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

