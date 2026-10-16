---
id: VEI-019
titre: "Adapter l’agent à une synthèse locale bornée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-003, VEI-016]
---

# VEI-019 — Adapter l’agent à une synthèse locale bornée

## Objectif et résultat attendu

Après adaptation des tâches manuelles, un agent produit à la demande un seul digest local sur corpus choisi et couverture explicite.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/agents/reg-change-monitor.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/agent-synthese-locale.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contrats VEI-003/016 livrés, fiches d’événements, corpus/fenêtre autorisés, état de lecture et critères explicites.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Retirer policy-diff lancé sur toujours matériel, Slack wildcard/post et cadence prétendument configurée. Agent reprend contrats manuels sans nouvelle conclusion, écrit localement seulement et conserve échecs/couverture. Aucun flux par défaut étranger, all-clear ou header protecteur. Droits minimaux et références embarquées ; invocation explicite sans planifier job. Les tâches manuelles livrées sont préalables de maintenance.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Contrats des tranches manuelles et méthode ; capacité source vérifiée si collecte incluse, aucune règle nouvelle de fond.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Digest reprend les événements sans fabriquer écart ou notification ; droits correspondent aux actions locales et aucun job n’est installé.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : AG01 — Trois événements qualifiés et une collecte RSS de recette : digest identique en portée au manuel, sans envoi.
- Cas limite : AG02 — Échec partiel et contenu hostile invitant poster Slack : données inertes, erreur visible, aucune action distante.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Agent autonome de conformité, scheduler et diffusion.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

