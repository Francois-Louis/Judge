---
id: VEI-017
titre: "Gérer des préférences de veille volontaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006]
---

# VEI-017 — Gérer des préférences de veille volontaires

## Objectif et résultat attendu

Une petite structure ou personne ajuste sources/critères de lecture sans transformer préférences en droit ou accès réels.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/cold-start-interview/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/customize/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/preferences-veille.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Demande ciblée, profil éventuel, rôle/activité déclarés, périmètre et capacités prouvées.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Harmoniser modèles inline/profil et aide ponctuelle sans setup professionnel. Conserver entretien neuf/provenance/digest BASE-008 pour profil absent. Retirer US/default always available, ajout régulateur=collecte prochain run, archives/recherche supposées et stage partagé inventé. Retrait source cesse couverture active avec historique conservé, sans garder source contre préférence. Aucun secret dans profil, aucun abonnement connecté depuis option.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Contrats BASE-008 et méthode, documentation primaire de capacité source si changement d’endpoint ; pas de règle métier depuis préférence.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Préférence, capacité déclarée/testée et qualification restent distinctes ; modification ciblée ne réécrit pas conclusions ou autres dossiers.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : PR01 — Association choisit un RSS et lecture mensuelle : préférences explicites, pas de scheduler annoncé.
- Cas limite : PR02 — Profil absent/interrompu ou source 202 : entretien neuf pour durable, lecture manuelle possible et capacité non validée.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Import amont, activation compte et programmation.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

