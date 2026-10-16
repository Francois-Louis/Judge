---
id: ETU-005
titre: "Guider la méthode d’un commentaire d’arrêt"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-004]
---

# ETU-005 — Guider la méthode d’un commentaire d’arrêt

## Objectif et résultat attendu

Un skill distinct aide à construire une lecture du sens, de la valeur et de la portée de la décision selon la consigne.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/case-brief/SKILL.md` : adaptation ciblée à cette tâche.
- `law-student/.claude-plugin/plugin.json` : adaptation ciblée à cette tâche.
- `law-student/README.md` : adaptation ciblée à cette tâche.
- `law-student/skills/commentaire-arret/SKILL.md` : à créer, propriétaire ETU-005.
- `law-student/references/commentaire-arret.md` : à créer, propriétaire ETU-005.

Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Décision et passages, consigne de commentaire, fiche déjà produite ou manques identifiés, pistes de l’apprenant.

## Travail attendu

- Créer une entrée bornée pour la méthode, charger le contexte, isolation et méthode empaquetés ; case-brief oriente sans prétendre déjà faire un commentaire.
- Faire formuler une question de commentaire et discuter des liens entre motifs, solution et plan proposé ; pas de plan rempli livré comme copie.
- Distinguer analyse de la décision et application à une situation hypothétique : pas de retour automatique à IRAC.
- N’exiger ni dissent américain ni plan immuable ; extrait trop court : lecture partielle et pièces manquantes, pas portée établie.

## Sources à rechercher lors de l'implémentation

Décision complète officielle, consigne institutionnelle et textes/arrêts de comparaison réellement lus si une portée est discutée.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] La sortie n’est pas la trame de cas pratique ni une fiche seule ; elle demande un travail critique appuyé sur la décision.
- [ ] Chaque affirmation de portée exige corpus et source lus ; aucun commentaire complet rédigé pour l’apprenant.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : CA01 — Texte et pistes de plan fournis : discuter leur ancrage dans les motifs et demander une justification de la portée.
- Cas limite : CA02 — Extrait du support EXIST-010 seul : commenter ce qu’il permet d’observer, demander le reste, sans extrapoler procédure ou portée.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

