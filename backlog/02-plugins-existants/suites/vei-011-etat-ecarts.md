---
id: VEI-011
titre: "Présenter l’état des écarts suivis"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-010]
---

# VEI-011 — Présenter l’état des écarts suivis

## Objectif et résultat attendu

Un état borné des écarts autorisés sépare actions ouvertes, décisions internes, dates légales documentées et revues nécessaires.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/gaps/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/gap-surfacer/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/etat-ecarts.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Registre/provenance, périmètre autorisé, date de référence, filtres, versions/statuts et responsables.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Façade gaps charge référence commune locale. Retirer overdue depuis due non typé, silence=conformité et disparition silencieuse des risk-accepted ; décisions restent visibles avec effets limités. Exposer lecture partielle, manques et âge de l’information. Compter consultations seulement dans rubrique séparée si contrat explicite, sans dupliquer obligations. Tableau/dashboard local échappé, aucun rappel distant.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Méthode locale et fiches de dates/applicabilité déjà établies ; toute nouvelle conclusion exige recherche dédiée.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Retard interne et obligation dépassée ne sont pas confondus ; décisions d’acceptation et inconnues restent visibles.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : R01 — Trois entrées avec dates de natures différentes : rubriques et preuves distinctes, pas urgence juridique uniforme.
- Cas limite : R02 — Registre vide/partiel, source statut inconnue : couverture explicite, aucune conformité ou absence de risque affirmée.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Nouvelles qualifications, notifications et audit de conformité.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

