---
id: HUB-005
titre: "Borner les suggestions aux données autorisées"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-003, HUB-004]
---

# HUB-005 — Borner les suggestions aux données autorisées

## Objectif et résultat attendu

Une suggestion facultative repose sur la tâche partagée et sa portée, sans lecture globale d’autres dossiers ou déclencheur supposé installé.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/related-skills-surfacer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/hooks/hooks.json` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.
- `legal-builder-hub/references/suggestions-context.md` : à créer, propriétaire HUB-005.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Description minimale de tâche autorisée, préférence de suggestions, contexte/juridiction, cache et liste des suggestions réellement montrées.

## Travail attendu

- Retirer « check what other plugins have been doing » comme droit de parcourir tous profils/dossiers ; pas d’envoi de contenu de dossier aux registres.
- Conserver absence de bruit et dédoublonnage, mais distinguer suggestion affichée, rejet explicite et simple silence ; le silence n’est pas un consentement ou un refus permanent.
- Charger la fiche de portée et ne pas promouvoir un candidat US pour une tâche FR par simple mot-clé.
- Constater hooks vides et Stop hook non câblé : invoquable directement ; aucune activité passive ou planification promise sans configuration réelle explicite.

## Sources à rechercher lors de l'implémentation

Configuration réelle des hooks et règles d’accès utilisateur ; catalogue daté et consignes de confidentialité réelles.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Préférence none n’émet aucune suggestion ni appel extérieur non nécessaire.
- [ ] La suggestion n’installe rien et ne révèle ni noms de clients ni extraits de pièces.
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

- Cas normal : SC01 — Demande explicite pour une tâche française et cache autorisé : une suggestion avec portée/provenance et limite.
- Cas limite : SC02 — Aucun hook, autre dossier non autorisé et silence précédent : pas exploration du dossier ni faux déclenchement ; pas rejet inféré.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

