---
id: VEI-002
titre: "Vérifier la capacité d’une source de veille"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006]
---

# VEI-002 — Vérifier la capacité d’une source de veille

## Objectif et résultat attendu

Une fiche décrit une seule source choisie, méthode/endpoint exact, format observé, accès nécessaire et limites de couverture.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/reg-feed-watcher/references/source-catalog.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/reg-feed-watcher/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/cold-start-interview/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/capacite-source.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Autorité/secteur/pays, URL fournie, méthode voulue, format attendu, fenêtre et besoins ; aucun secret dans la sortie.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Réécrire seulement le contrat d’une source France/UE choisie, avec provenance du catalogue et test réel borné. Distinguer HTML/RSS/Atom/JSON/XML/archive/email, URL de découverte et endpoint. Consigner HTTP, redirection, taille, parseur, pagination, auth déclarée versus testée. Aucun compte, clé ou souscription supposés actifs. Conserver historique des changements d’endpoint ; retirer Federal Register par défaut et dates de vérification héritées. Une page HTML ne prouve ni absence de tout flux sur le site ni RSS fonctionnel.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Documentation technique primaire de l’émetteur, Légifrance/DILA ou EUR-Lex/Office des publications selon source ; droits/conditions et limites à rechercher.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Source déclarée, accessible et exploitable sont distinguées ; test échoué laisse état et alternative manuelle, aucune couverture globale garantie.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : S01 — Source CNIL retenue : vérifier endpoint réel et parser RSS, décrire fenêtre et couverture, sans certifier toutes décisions.
- Cas limite : S02 — Accueil EUR-Lex en 202 vide ou page EDPB HTML : ne pas enregistrer comme flux valide, proposer document fourni ou endpoint à rechercher.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Catalogue mondial adapté, activation de compte et collecteur autonome.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

