---
id: VEI-007
titre: "Qualifier le champ d’un changement pour une activité"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-001, VEI-005]
---

# VEI-007 — Qualifier le champ d’un changement pour une activité

## Objectif et résultat attendu

Une fiche motive application, exclusion conditionnelle ou impossibilité de conclure pour un changement et une activité/acteur déterminés.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/policy-diff/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/applicabilite-activite.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Texte/version/statut, fiche temporelle VEI-005 ou équivalente, activité réelle, rôle, territoire, dates, taille/seuils pertinents et pièces.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Borner analyse de champ distincte du filtre de veille et de l’écart. Rechercher critères/exceptions et preuve de chacun ; si directive, consommer éléments VEI-006 ou équivalents avant conclusion sur règle nationale. Aucune priorité interne ne rend texte applicable et aucun faible intérêt n’écarte obligation. Relais privacy/IA/produit/travail/secteur avec question précise si expertise adaptée manque ; conclusions de fond complexes restent dans leur domaine.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Texte primaire et dispositions de champ/transitions, règles nationales pertinentes et sources sectorielles propres à la seule question retenue.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Qualification dépend de faits sourcés et critères exacts ; organisation française ou mot-clé ne suffisent pas à attribuer une obligation.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : A01 — TPE décrit activité/rôle visés par changement fictif : fiche critère/fait/pièce et réserves.
- Cas limite : A02 — Rôle ou seuil inconnu, branche sectorielle non adaptée : résultat conditionnel et fiche autonome, pas de conformité ou transfert automatique.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Analyse globale de conformité, obligations de tous secteurs et autorisation d’activité.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

