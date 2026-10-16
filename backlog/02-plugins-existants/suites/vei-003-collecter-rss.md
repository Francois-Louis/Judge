---
id: VEI-003
titre: "Collecter manuellement un flux RSS français"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-002]
---

# VEI-003 — Collecter manuellement un flux RSS français

## Objectif et résultat attendu

Une exécution à la demande d’un seul RSS CNIL choisi donne les éléments lus, erreurs et couverture avec curseur documenté.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/reg-feed-watcher/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/collecte-rss.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Capacité VEI-002 ou équivalente, endpoint autorisé, fenêtre, état antérieur, limites/format et objectif.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Borner à un RSS retenu après contrôle, pas veille France entière. Garder source originale, identifiant, URL, titre, langue et récupération ; corps de flux non fiable. Dédupliquer sans remplacer version précédente, gérer même date et entrée tardive. Décrire limite/pagination/erreur ; n’avancer curseur que sur couverture effectivement lue avec fenêtre de recouvrement explicite. Aucun texte complet ou modification juridique présumés depuis extrait ; pas d’email/Slack.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Documentation de la source CNIL et modalités de collecte, méthode locale de provenance ; textes normatifs seulement dans tâche de qualification séparée.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Chaque élément reste traçable et échec partiel ne disparaît pas derrière all-clear ; aucun gap ou obligation déduit du flux.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : C01 — RSS de recette avec dix items dont doublon : liste dédupliquée avec versions et fenêtre réellement couverte.
- Cas limite : C02 — RSS inaccessible, item tardif et page incomplète : erreurs et périmètre visibles, pas de curseur global avancé ni silence interprété.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Scheduler, collecte multi-sources, JORF archives et applicabilité.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

