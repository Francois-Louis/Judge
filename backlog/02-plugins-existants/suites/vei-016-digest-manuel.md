---
id: VEI-016
titre: "Préparer une synthèse de veille à la demande"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-001]
---

# VEI-016 — Préparer une synthèse de veille à la demande

## Objectif et résultat attendu

Une synthèse locale d’un corpus d’événements fourni conserve nature, statut, pertinence interne et limites de couverture.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/reg-feed-watcher/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/digest-veille.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Événements qualifiés VEI-001 ou équivalents, collecte VEI-003 si disponible, corpus/fenêtre, critères de lecture explicites et destinataire.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Conserver classement de lecture comme préférence, distinct du droit applicable. Publication, directive/transposition, consultation et information séparées. Propager source/version/date et non-lus, erreurs, exclusions, changements tardifs. Pas d’obligation/gap depuis matérialité ; proposer question métier au lieu du diff automatique. Chat par défaut, fichier durable via helper si voulu ; retirer ~/digests hors racine et all-clear.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Méthode locale et fiches d’événements réellement lues, critères internes ; aucune nouvelle conclusion juridique depuis synthèse.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Chaque item garde type/statut et couverture, y compris échecs ; aucune couleur ou absence de résultat ne vaut conformité.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : DG01 — Corpus JORF/directive/consultation fictifs : trois rubriques et prochaines questions distinctes.
- Cas limite : DG02 — Aucun item mais un flux échoué : zéro résultat lu avec erreur visible, pas rien à signaler ou veille exhaustive.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Envoi, publication distante, calendrier et analyse complète.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

