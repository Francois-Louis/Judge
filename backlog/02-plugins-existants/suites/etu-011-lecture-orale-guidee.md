---
id: ETU-011
titre: "Préparer une discussion orale sur une décision"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-004]
---

# ETU-011 — Préparer une discussion orale sur une décision

## Objectif et résultat attendu

Des questions progressives entraînent à expliquer les passages d’une décision sans prévoir celles d’un professeur.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/cold-call-prep/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/skills/socratic-drill/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/oral-guided-reading.md` : à créer, propriétaire ETU-011.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Texte, objectif d’oral, consigne, niveau et mode de dialogue souhaité ; ne pas collecter le nom du professeur sans besoin.

## Travail attendu

- Renommer l’intitulé visible cold call en lecture/discussion orale ; supprimer hobby horses, classements prédictifs et dissent obligatoire.
- Conserver question puis réponse de l’apprenant, indices ciblés et possibilité de changer de rythme ; pas de pression fondée sur l’échec supposé au barreau.
- Un nom/date réel dans un arrêt n’est pas une demande de conseil. Si la demande devient un litige personnel, qualifier et orienter vers le domaine compétent sans déduire le statut professionnel de l’utilisateur.
- Aucun récit de décision depuis mémoire si le texte manque ; le journal relève les questions travaillées, pas la probabilité de réussir l’oral.

## Sources à rechercher lors de l'implémentation

Consigne orale et décision fournie ; aucune biographie de professeur ou prédiction d’épreuve.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Les questions sont attribuées à l’exercice créé et non au professeur ou à un futur jury.
- [ ] Sans texte, méthode limitée et demande du support plutôt que détail inventé.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : OR01 — Décision française fournie : une question sur les motifs, attendre puis proposer un indice ancré dans le passage.
- Cas limite : OR02 — « Quelles seront les questions du prof ? » sans texte : pas de classement prédictif ; proposer une grille générale de lecture.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

