---
id: PILOTE-001
titre: "Inventorier le plugin travail et découper son adaptation"
statut: terminee
priorite: P1
nature: audit
dependances: [BASE-003, BASE-005]
---

# PILOTE-001 — Inventorier le plugin travail et découper son adaptation

## Objectif

Préparer l'adaptation du plugin existant `employment-legal`, skill par skill.

## Points de départ

- [employment-legal/skills/](../../employment-legal/skills/)
- [employment-legal/agents/leave-tracker.md](../../employment-legal/agents/leave-tracker.md)
- [employment-legal/CLAUDE.md](../../employment-legal/CLAUDE.md)
- [employment-legal/.mcp.json](../../employment-legal/.mcp.json)
- [employment-legal/README.md](../../employment-legal/README.md)

## Travail attendu

- Examiner les 20 skills, le profil, l'agent et les références ; ne pas se limiter aux descriptions.
- Pour chaque workflow, distinguer logique réutilisable, règles américaines à remplacer et prérequis français à rechercher.
- Relever notamment at-will, classification exempt/non-exempt, FLSA, FMLA et modèles de rupture ; les remplacer exige une analyse métier, pas une traduction.
- Proposer les stories suivantes : qualification de la relation, rémunération/temps, rupture, congés, enquête interne, politiques et implantation. Fractionner une tâche encore trop large.

## Critères d'acceptation

- [x] Chaque skill existant a une ligne dans l'inventaire avec ses dépendances de contenu.
- [x] Les règles collectives, le secteur public/privé et les rattachements territoriaux sont prévus lorsque pertinents.
- [x] Le skill `hiring-review` a une liste de sections à modifier et des scénarios de contrôle.
- [x] Le reste du plugin reste explicitement non adapté à ce stade.

## Vérification

Suivre les appels de `leave-tracker` et des commandes d'enquête jusqu'aux agents et fichiers réellement utilisés pour éviter de manquer du droit américain indirect.

## Hors périmètre

Réécrire le plugin entier ou traiter les 20 skills dans la même livraison.

## Bilan d'exécution — 15 octobre 2026

- [Inventaire des 20 skills](pilote-001-annexes/pilote-001-releve-inventaire.md) : corps des
  fichiers lus, dépendances communes et particulières, quatre références,
  profil, agent, métadonnées et accès externes distingués.
- Chaînes suivies dans le contenu : `leave-tracker` jusqu'à l'agent et son
  registre ; les cinq commandes d'enquête jusqu'aux modes, modèles et fichiers
  de `internal-investigation`. Délais américains codés dans `log-leave`,
  marquage work product dans le wrapper de mémo et calcul FLSA indirect relevés.
- [Plan hiring-review](pilote-001-annexes/pilote-001-plan-hiring-review.md) : sections à reprendre,
  ajustements minimaux de configuration et 14 scénarios attendus.
- [Découpage](pilote-001-annexes/pilote-001-decoupage-travail.md) : 16 stories TRAV proposées,
  avec pièces, résultats et limites. Salaire/temps, modes de rupture,
  saisie/suivi d'arrêt, étapes d'enquête, charte/diff et lancement/suivi
  d'implantation sont séparés. Les suites attendent PILOTE-003 ; la dépendance
  USAGE-002 de PILOTE-002 est conservée.
- [Contrôles statiques et empreintes](pilote-001-annexes/pilote-001-resultats.json) : couverture
  exacte 20/20, liens locaux, frontmatter/dépendances sans cycle, copie BASE-005
  identique et absence de modification du plugin métier. Aucun paquet modifié
  par l'audit ; validation client et exécution métier non réalisées.
  Lint des cinq cookbooks réussi avec `python -X utf8`, 45 JSON valides et
  `git diff --check` propre ; le mode UTF-8 évite l'erreur d'affichage cp1252
  du lint sur cette console Windows.
- À la demande de l'utilisateur, [BASE-010](../00-fondations/base-010-acces-sources-officielles.md)
  ajoute des voies de lecture officielles sans souscription API : tests réseau
  CDTN/CELLAR et XML DILA LEGI/KALI/CASS, preuves et limites séparées.
  Ces accès ne valident pas les règles des futures tâches.
- Aucun skill adapté, aucun agent d'enquête lancé, aucun profil personnel
  consulté, aucun scénario H01–H14 exécuté. Le prochain lot proposé reste
  PILOTE-002, pas la réécriture du plugin entier.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 115, 117, 119 de la [matrice](../03-nouveaux-domaines/dom-031-annexes/dom-031-frictions-utilisateurs.md). Tâches candidates à découper ; aucune nouvelle capacité livrée.

- [ ] Recueillir les besoins à découper hors des skills d’embauche : demande de congé pour décès/deuil d’un salarié privé, lien, événement, dates, convention et justificatif minimal ; sortie candidate : demande à l’employeur et droits sourcés, sans présumer une faveur discrétionnaire.
- [ ] Prévoir une tâche distincte sur salaires/congés et sommes dus après décès du salarié : demandeur et qualité, contrat, bulletins, solde, décompte et pièces ; sortie candidate : tableau et demande au service employeur, sans distribuer les sommes entre héritiers.
- [ ] Séparer congés emploi, aides DOM-012, prévoyance INS-009 et créance successorale DOM-016 ; statut public vers DOM-037. Ce complément ne rouvre pas la tranche pilote livrée et ne change pas son statut.

Scénarios supplémentaires **attendus, non exécutés** : salarié demandant un congé après décès d’un enfant ; proche réclamant le solde de salaire sans qualité établie ; agent public orienté vers son régime.

Sources à ouvrir lors de l’implémentation : Code du travail et convention applicable pour événements familiaux, droits dus et justificatifs ; statut du demandeur avant toute règle.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../03-nouveaux-domaines/dom-031-annexes/dom-031-frictions-verification.md).

## Complément de cadrage — frictions travail du 16 octobre 2026

Le [découpage actualisé](pilote-001-annexes/pilote-001-decoupage-travail.md)
et la [matrice des 182 points](pilote-001-annexes/pilote-001-frictions-utilisateurs.md)
précisent sept suites et ajoutent quarante propositions TRAV-022 à TRAV-061.
Le [texte reçu](sources/travail-frictions-2026-10-16.txt) est conservé à l’octet
près ; recours sociaux, CSE/élections et ruptures aux torts de l’employeur
gardent leurs besoins de découpage explicites. Le bilan initial ci-dessus
reste historique ; aucune nouvelle fonctionnalité ni priorité d’implémentation
n’est sélectionnée. Voir la [vérification](pilote-001-annexes/pilote-001-frictions-verification.md)
pour les contrôles et la portée de ce complément.
