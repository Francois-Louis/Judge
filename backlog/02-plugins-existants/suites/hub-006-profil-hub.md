---
id: HUB-006
titre: "Configurer un profil minimal de gestion des skills"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-002, HUB-004]
---

# HUB-006 — Configurer un profil minimal de gestion des skills

## Objectif et résultat attendu

Un entretien minimal renseigne besoins, territoire et contexte d’usage sans imposer un métier, une entreprise ou un starter pack déjà adapté.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/cold-start-interview/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.
- `legal-builder-hub/references/hub-profile.md` : à créer, propriétaire HUB-006.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Besoins et préférences déclarés, politique active, profil du fork existant et capacités d’intégration réellement disponibles.

## Travail attendu

- Conserver entretien neuf du fork et reprise des réponses ; profil partagé facultatif selon public, aucun import de l’origine ni parcours obligatoire d’entreprise.
- Distinguer qualité professionnelle déclarée et autorité effective pour installer ; un avocat n’est pas automatiquement administrateur, un non-avocat n’est pas automatiquement privé de toute décision technique.
- Ne pas déduire le scope du produit depuis le répertoire courant ; lever uniquement les inconnues qui changent accès/installation.
- Départ rapide utilise le défaut restrictif cohérent ; une sélection de starter pack déclenche les revues par candidat, sans installation globale ni affirmation d’adaptation FR/UE.
- Un connecteur n’est fonctionnel que sur appel approprié réussi ; config déclarée/inconnue/inaccessible séparées. Conserver aide hors ligne, sans accès de recherche obligatoire par principe.

## Sources à rechercher lors de l'implémentation

Réponses/profil actifs, politique et capacités effectives ; règles officielles du produit pour scope et permissions à vérifier dans le futur lot.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Un particulier ou mainteneur démarre sans profil entreprise, coordonnées d’avocat ou autre plugin obligatoire.
- [ ] Les recommandations suivent la portée des tâches réellement livrées ; aucune hypothèse américaine ne remplit un champ inconnu.
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

- Cas normal : PH01 — Besoin France fourni, sans entreprise ni Slack : profil minimal et catalogue borné, aucune installation.
- Cas limite : PH02 — Profil partiel existant avec mode restrictif : compléter la section utile sans reset, import d’origine ou passage permissif.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

