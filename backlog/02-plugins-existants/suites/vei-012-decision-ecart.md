---
id: VEI-012
titre: "Consigner une décision de suivi d’écart"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-010]
---

# VEI-012 — Consigner une décision de suivi d’écart

## Objectif et résultat attendu

Une décision attribuée de clôture de tâche ou d’acceptation interne conserve preuves, risques restants et conditions de réexamen.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/gaps/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/gap-surfacer/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/decision-ecart.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Entrée/source/versions, décisionnaire et autorité déclarée, raison, politique approuvée, preuve de pratique si invoquée et date.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Séparer décision proposée/décidée, texte modifié/approuvé et pratique exécutée ; ne pas certifier conformité par close. Acceptation du risque ne supprime pas obligation ni entrée, exclusion de champ exige qualification motivée. Correction par nouvel historique ; réexamen si texte/périmètre change. Corriger gate qui confond simplement enregistrer décision et attester conformité. Ni attestation ni envoi.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Texte qualifié, politique/mesures et preuves réelles, processus interne d’autorité ; méthode locale.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Clôture ou risque accepté reste décision de suivi visible avec résiduel ; aucune régularisation ou conformité depuis seul statut.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : DC01 — Politique approuvée mais mesure technique non prouvée : état partiel et action restante explicites.
- Cas limite : DC02 — Responsable demande risk-accepted pour obligation applicable : consigner portée interne sans effacer l’obligation ni garantir licéité.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Attestation, décision d’autorité et suppression des écarts.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

