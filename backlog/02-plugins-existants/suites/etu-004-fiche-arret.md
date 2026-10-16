---
id: ETU-004
titre: "Accompagner une fiche d’arrêt"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001]
---

# ETU-004 — Accompagner une fiche d’arrêt

## Objectif et résultat attendu

Une trame de fiche distingue faits pertinents, procédure, prétentions/moyens, question et solution selon les seuls passages disponibles.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/case-brief/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/references/fiche-arret.md` : à créer, propriétaire ETU-004.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Décision française identifiée, extrait ou texte intégral, consigne et première lecture de l’apprenant.

## Travail attendu

- Conserver la trame à compléter et l’apprenant d’abord ; distinguer texte de décision et sommaire éditorial.
- Retirer le repli vers un résumé complet de mémoire sur seul nom de décision ; citer seulement le passage effectivement lu.
- Signaler les parties absentes de l’extrait : pas de procédure, prétentions ou portée inventées.
- Rendre visible « fiche d’arrêt » sans l’assimiler au commentaire ; case-brief reste chemin technique initial, références croisées canoniques.

## Sources à rechercher lors de l'implémentation

Texte officiel de la décision et consigne ; référence, date, juridiction et périmètre de l’extrait à relever.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Chaque élément documenté est attribué au passage, et chaque manque reste explicite.
- [ ] La fiche ne devient ni un commentaire rédigé ni une consultation sur un litige réel.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : FA01 — Décision fournie : l’apprenant propose la solution, le retour indique le passage qui l’étaye puis la prochaine rubrique.
- Cas limite : FA02 — Seul nom ou extrait de motifs : demander le texte, garder inconnues procédure/portée, ne pas reconstituer de mémoire.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

