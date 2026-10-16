---
id: VEI-005
titre: "Établir la chronologie d’un texte"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-001]
---

# VEI-005 — Établir la chronologie d’un texte

## Objectif et résultat attendu

Une fiche temporelle par disposition distingue dates constatées, événements juridiques à établir et échéances encore indéterminées.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/references/chronologie-texte.md` (à créer)
- `regulatory-legal/skills/text-status/SKILL.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Acte exact, dispositions finales/transitoires, publication, versions et rectificatifs, date de référence, territoire et événement déclencheur éventuel.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Créer tâche de statut temporel. Séparer adoption/publication/entrée en vigueur/application différée/transposition et échéance interne. Chaque événement lie passage/version/preuve et champ ; pas de date unique pour tout acte. Computation seulement avec déclencheur prouvé, règle actuelle, méthode reproductible, exceptions et contrôle attribué. Statut à vérifier sur chaque analyse, sans seuil 12 mois/30 jours. Manque : a-determiner, aucune date par défaut.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Acte/dispositions transitoires JORF ou JOUE, modifications/rectificatifs, textes de calcul spécifiques si nécessaires ; distinguer obligation et simple information.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Toute date porte type, passage et statut ; publication n’est pas application et donnée absente ne produit pas délai calculé.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : T01 — Texte fictif avec dispositions s’appliquant à deux dates : deux événements liés à leurs articles, pas date globale.
- Cas limite : T02 — Date dans résumé mais clause transitoire absente : a-determiner et pièce à obtenir, sans calendrier de mémoire.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Calendrier universel, décision de champ et agenda.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

