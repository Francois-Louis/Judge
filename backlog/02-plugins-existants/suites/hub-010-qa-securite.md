---
id: HUB-010
titre: "Rendre cohérents les verdicts de sécurité"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-011, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-009, HUB-001, HUB-002]
---

# HUB-010 — Rendre cohérents les verdicts de sécurité

## Objectif et résultat attendu

Un vocabulaire de verdict distingue observation heuristique, besoin de revue et refus non contournable ; tous consommateurs appliquent la même priorité.

Plugin principal : `legal-builder-hub`. Suite proposée, non réalisée par
EXIST-011. Le bilan PILOTE-003 est clos après BASE-011 ; ce préalable satisfait
ne sélectionne pas la suite. Un lot doit rester limité à la tâche ci-dessus.

## Périmètre et fichiers

- `legal-builder-hub/skills/skills-qa/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/skill-installer/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/auto-updater/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/skills/customize/SKILL.md` : adaptation ciblée.
- `legal-builder-hub/references/qa-security-verdicts.md` : à créer, propriétaire HUB-010.

Les autres références futures sont consommées après leurs suites propriétaires,
sans copie concurrente. Garder les références nécessaires dans le paquet,
sans dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Arborescence/périmètre lus, lignes et données observées, surface de capacités, versions des règles et contrôles disponibles.

## Travail attendu

- Conserver repérage d’injection, sources brutes et preuves fichier/ligne ; scan propre n’est ni audit de sécurité ni autorisation.
- Corriger skills-qa Step 1.5 qui émet REFUSE puis permet override, et sa fin « verdict advisory » ; distinguer simple finding à examiner de motif de refus concret.
- Une exfiltration/vol d’identifiants ou modification hostile établie n’a pas de bouton install anyway ; un rôle professionnel ou strictness ne baisse pas ce refus.
- Clarifier régression à la mise à jour sans transformer toute variation de texte en malware certain ; aucun renommage de verdict pour contourner le blocage.
- Pas d’exécution de code candidat ni de permission supplémentaire pour vérifier une affirmation de sécurité.

## Sources à rechercher lors de l'implémentation

Fichiers exacts et contrats de capacités du produit ; sources primaires de sécurité si besoin de caractériser un mécanisme, pas réputation du publisher.

Lire les documents utiles et garder version, date, périmètre et provenance.
Présence d’une URL, d’une licence ou d’une date auteur ne prouve pas les
conclusions que le contenu en tire. Les règles du produit ne sont pas
vérifiées en ligne par ce cadrage.

## Critères d'acceptation

- [ ] REFUSE reste identique dans QA, installation, mise à jour et personnalisation.
- [ ] Les constats conservent preuve et limite de scan ; une analyse partielle n’émet pas « sûr ».
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

- Cas normal : QS01 — Hooks ajoutés et URL nouvelle : différence et capacités affichées, revue obligatoire même sans payload avéré.
- Cas limite : QS02 — Texte demande exfiltration d’identifiants : refus sans override, aucune action réseau exécutée.

Ces scénarios restent à exécuter dans l’implémentation ; la relecture EXIST-011
et sa fixture filesystem existante ne constituent pas leur recette complète.

## Hors périmètre

Réécrire tout le hub, modifier des plugins internes/éditeur depuis le lifecycle,
installer ou mettre à jour un contenu réel dans le cadre du cadrage, modifier
l’origine ou importer son journal, certifier la sécurité ou l’exactitude du
droit, contacter un tiers, envoyer une notification, publier ou déployer
sans tâche explicite. Aucun nouveau registre n’est rendu fiable par traduction.

