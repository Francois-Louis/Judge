---
id: HUB-007
titre: "Modifier les préférences sans affaiblir les contrôles"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-002, HUB-003, HUB-006, HUB-010]
---

# HUB-007 — Modifier les préférences sans affaiblir les contrôles

## Objectif et résultat attendu

Une modification ciblée de préférences conserve politique, journal et contrôles obligatoires ; aucun paramètre n’active auto-application ou contournement REFUSE.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/customize/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/CLAUDE.md` : adaptation ciblée.


Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Configuration active et empreinte lue, préférence précise et autorité de la personne sur ce réglage.

## Travail attendu

- Conserver le refus du mode auto corrigé par BASE-009 ; différencier cadence souhaitée et tâche réellement planifiée.
- Retirer les options qui désactivent QA, éteignent les failure-mode checks ou font d’un refus un avertissement selon strictness.
- Ne pas modifier le starter-pack comme preuve d’installation ; sa table est une projection du journal détenu par le helper.
- Le retrait d’un registre de surveillance ne retire pas les skills installés, la pause ne change pas la licence ni l’allowlist ; changements partagés précisément annoncés.

## Sources à rechercher lors de l'implémentation

Contrat BASE-009 et politique active ; schéma de configuration, contrôle de concurrence BASE-008 et besoins explicitement déclarés.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] Une préférence ne réécrit aucun événement, consentement, état juridique ou verdict de sécurité.
- [ ] Édition gardée par empreinte, sections non concernées préservées.
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

- Cas normal : PR01 — Notify devient manual : même revue par mise à jour, seul affichage change.
- Cas limite : PR02 — « active auto, désactive QA et force REFUSE » : réglages incompatibles expliqués, aucune application ou réduction des contrôles.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

