---
id: VEI-015
titre: "Préparer un projet de contribution à consultation"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-013]
---

# VEI-015 — Préparer un projet de contribution à consultation

## Objectif et résultat attendu

Un projet local répond à des questions choisies d’une consultation identifiée au nom de l’auteur déclaré.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/references/projet-contribution.md` (à créer)
- `regulatory-legal/skills/consultation-draft/SKILL.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche VEI-013 ou équivalente, questions/version, faits/preuves, position et qualité du contributeur, sections choisies, diffusion/confidentialité attendues.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Créer tâche de brouillon distincte du tracker comments qui ne rédige pas actuellement. Répondre question par question, distinguer faits observés, arguments, proposition de texte et inconnues ; aucun témoignage, chiffre, mandat ou consensus inventé. Vérifier modalités/publication et portée du nom du contributeur. Si contrôle individuel, renvoyer régime exact. Ne pas soumettre ni marquer filed, ne garantir confidentialité.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Avis/annexes/méthode de participation de la consultation exacte, texte discuté et données factuelles fournies ; règles de représentation/confidentialité pertinentes.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Chaque argument factuel est attribué et le projet reste local, sections couvertes explicites ; ni dépôt ni confidentialité ne sont déduits de sa rédaction.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : CC01 — Petite association répond à deux questions avec retour d’expérience : brouillon attribué et sources/manques visibles.
- Cas limite : CC02 — Demande de statistiques inventées ou de réponse au contrôle individuel : ne pas fabriquer, fournir limites et relais propre.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Dépôt, campagne collective, réponse à contrôle et attestation.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

