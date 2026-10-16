---
id: VEI-006
titre: "Documenter la transposition française d’une directive"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-001, VEI-005]
---

# VEI-006 — Documenter la transposition française d’une directive

## Objectif et résultat attendu

Une fiche relie une disposition de directive à ses mesures françaises identifiées ou constate les recherches et manques.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/references/suivi-transposition.md` (à créer)
- `regulatory-legal/skills/directive-transposition/SKILL.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Directive/version et disposition précise, date de référence, pays France, mesures nationales alléguées et activité seulement décrite.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Borner à une directive et une disposition/périmètre français. Distinguer échéance de transposition, notification d’une mesure, texte national effectivement lu et couverture matérielle à vérifier. Rechercher textes nationaux et leur temporalité sans déduire transposition complète d’une fiche ou d’un booléen. Absence de résultat ne prouve absence de mesure. Ne pas conclure applicabilité à un acteur privé ou effet direct depuis directive/délai seuls.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

EUR-Lex/JOUE, métadonnées nationales puis textes français JORF/Légifrance effectivement lus, versions et tables de correspondance si disponibles avec statut.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Mesure déclarée, publiée, lue et couverture établie restent distinctes ; aucune transposition complète ou absence de transposition depuis un seul résultat.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : D01 — Directive fictive et deux mesures françaises partielles : carte disposition/mesure avec manques, dates qualifiées.
- Cas limite : D02 — Mesure notifiée sans texte lisible ou échéance dépassée alléguée : état de recherche réservé, pas obligation privée déduite.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Effet direct/conflit normatif, transposition tous pays et analyse sectorielle complète.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

