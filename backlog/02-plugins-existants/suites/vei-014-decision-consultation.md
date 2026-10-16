---
id: VEI-014
titre: "Suivre une décision de participation à consultation"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-013]
---

# VEI-014 — Suivre une décision de participation à consultation

## Objectif et résultat attendu

Un registre sépare intention, décision attribuée, contribution préparée et dépôt prouvé pour une consultation.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/comments/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/gap-surfacer/references/comment-tracker.yaml` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/gap-surfacer/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/suivi-consultation.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche VEI-013 ou équivalente, décisionnaire/qualité, raison, date/source, pièces d’autorisation et preuve de dépôt si alléguée.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Corriger commentaire HTML modèle en commentaire YAML et remplacer CMT-001 actif par liste vide/exemple séparé. Mettre à jour vrais consommateurs watcher/comments, sans référence croisée mensongère gap-surfacer. Décision participer non déposée ; waived ambigu remplacé par décision motivée. Retirer gates avocat pour consigner intention, Slack/rappels automatiques et jalons 5 jours imposés. Date interne calculée seulement depuis préférence explicite, jamais règle légale.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Avis officiel/version et modalités, processus interne de représentation/mandat, preuve réelle de dépôt et méthode de dates.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Modèle chargé ne contient aucune clé parasite ni consultation active fictive ; décision et dépôt gardent preuve/état distincts.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : CD01 — Association décide participer sans brouillon : décision attribuée, dépôt non réalisé et date de clôture sourcée.
- Cas limite : CD02 — Statut filed demandé sans accusé ou avis prolongé allégué : preuve manquante, ancienne date conservée avec statut, aucun dépôt inventé.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Déposer, écrire contribution et automatiser rappels.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

