---
id: ETU-006
titre: "Relire un brouillon de commentaire d’arrêt"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-010, PILOTE-003, BASE-005, BASE-006, ETU-001, ETU-005]
---

# ETU-006 — Relire un brouillon de commentaire d’arrêt

## Objectif et résultat attendu

Le retour repère paraphrase, détachement des motifs ou portée non étayée et demande une reprise ciblée.

Plugin principal : `law-student`. Une tâche bornée de formation juridique,
sans traitement d’un litige réel. Suite proposée, non implémentée par EXIST-010.
PILOTE-003 est terminé après BASE-011 ; sa clôture ne sélectionne pas cette suite.

## Périmètre et fichiers

- `law-student/skills/legal-writing/SKILL.md` : adaptation ciblée à cette tâche.


Les références futures d’une autre suite sont consommées après cette suite,
sans second fichier concurrent. Les méthodes et l’isolation restent embarquées ;
aucune dépendance runtime au checkout ou à un autre plugin.

## Entrées nécessaires

Décision, consigne, brouillon et éventuellement grille officielle fournie.

## Travail attendu

- Ajouter un mode commentaire avec critères propres, sans utiliser automatiquement ceux de cas pratique ou de memo américain.
- Relier chaque observation à un passage du brouillon et de la décision ; ne pas écrire une introduction ou un plan de remplacement.
- Conserver la séparation retour/texte à remettre ; les motifs de décision ne sont pas les faits d’un nouveau cas pratique.

## Sources à rechercher lors de l'implémentation

Consigne, grille éventuelle et passages exacts de décision ; commentaires doctrinaux seulement s’ils sont identifiés et effectivement lus.

Lire les documents utiles et consigner provenance, version et périmètre ;
un document retrouvé ou fourni n’est pas une règle automatiquement applicable.
Méthode et exercice ne certifient pas l’actualité du droit.

## Critères d'acceptation

- [ ] Le retour explique la différence entre restitution, analyse et affirmation non sourcée.
- [ ] Aucun plan en deux parties ou barème uniforme n’est imposé faute de consigne.
- [ ] Les entrées adaptées chargent les références locales pertinentes et respectent
  les règles d’aide réelles ; aucun devoir substitutif ou corrigé intégral livré.
- [ ] Les scénarios ci-dessous sont exécutés et leurs sorties conservées, avec les
  contrôles BASE-006 appropriés au paquet extrait. Installation, recette client
  et revue juridique restent des résultats distincts.
- [ ] Documentation et commandes citées reflètent les seules tâches réellement
  livrées ; version et NOTICE actualisés si le plugin change, sans modifier
  les copies partagées BASE-005/BASE-008 dans ce lot.

## Vérification

- Cas normal : RA01 — Brouillon paraphrase le dispositif : demander ce que les motifs apportent et où cela apparaît dans la décision.
- Cas limite : RA02 — Copie sans décision ni consigne : retour de structure seulement, pas validation du sens de l’arrêt.

Ces scénarios sont spécifiés ici ; ils ne sont pas déclarés exécutés par EXIST-010.

## Hors périmètre

Adapter tout le plugin, garantir une note ou une réussite, produire une copie
à remettre, prédire un sujet, attribuer un statut professionnel à l’utilisateur,
valider des droits sur un support par sa simple présence, envoyer des données,
synchroniser un calendrier ou installer/déployer sans tâche explicite.
Les litiges scolaires relèvent de DOM-027 et les dossiers réels de leur domaine ;
ceci ne rend pas ces futurs plugins déjà disponibles.

