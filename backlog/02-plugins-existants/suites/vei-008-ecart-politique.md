---
id: VEI-008
titre: "Comparer un changement qualifié à une politique"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-004, VEI-007]
---

# VEI-008 — Comparer un changement qualifié à une politique

## Objectif et résultat attendu

Un rapport sur une politique/version choisie relie exigences applicables, passages internes et écarts documentaires ou éléments non vérifiables.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/policy-diff/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/ecart-politique.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Qualification VEI-007, preuve de modification VEI-004 ou équivalents, texte intégral, politique/version lue, périmètre/exclusions et propriétaire.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Conserver table exigences/citations/écart, sans inférer politique inexistante depuis index vide ou match absent. Exclusion = non examiné, pas absence ; politique illisible = inconnu. Distinguer exigence applicable, future et scénario de projet, ce dernier sans compliance gap. Aucun no-gap textuel ne certifie pratiques réelles. Une politique à jour sans changement prouvé ne justifie pas delta inventé.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Disposition applicable effectivement lue et politique interne versionnée ; source de modification et calendrier, méthode locale.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Chaque écart est documentaire et motivé ; bibliothèque vide ou zone exclue ne produit pas écart juridique automatique.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : E01 — Texte changé et politique fournie : tableau exigences/passages avec modification ciblée à instruire.
- Cas limite : E02 — Politique absente ou projet de texte seulement : incomparabilité/scénario distinct, ni new-policy gap automatique ni violation.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Audit de pratique, rédaction, toutes politiques et certification.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

