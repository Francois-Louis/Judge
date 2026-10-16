---
id: VEI-001
titre: "Qualifier une publication fournie"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006]
---

# VEI-001 — Qualifier une publication fournie

## Objectif et résultat attendu

Une fiche qualifie un document fourni, sa provenance et le type d’événement pour une petite structure sans profil professionnel.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/reg-feed-watcher/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/qualification-publication.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Document/URL ou extrait identifié, auteur, identifiant éventuel, langue, dates visibles, activité et question de lecture.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Créer mode manuel français explicite. Distinguer texte publié, projet, communiqué, guide, décision, consultation et document indéterminé ; allégation et qualification vérifiée séparées. Conserver URL/version et statut de lecture, demander pièces manquantes sans inventer publication. Ne pas collecter tous flux, appliquer filtre US, calculer délai ou créer gap. Résumé fourni reste piste tant que texte primaire manque.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

JORF/Légifrance, EUR-Lex/JOUE, site officiel de l’émetteur selon document ; rechercher acte exact, version et statut dans le futur lot.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Type, provenance et manques sont visibles ; aucune publication ne devient automatiquement obligation applicable ou consultation ouverte.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : Q01 — Arrêté JORF fictif fourni intégralement : fiche d’identification et événements temporels à rechercher, sans date d’application déduite du titre.
- Cas limite : Q02 — Alerte de cabinet annonçant une réforme sans texte : piste secondaire et référence à obtenir, aucun constat de conformité.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Collecte complète, applicabilité de fond, calcul de délai et diffusion.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

