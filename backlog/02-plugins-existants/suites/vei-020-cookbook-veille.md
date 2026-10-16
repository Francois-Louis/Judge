---
id: VEI-020
titre: "Vérifier le cookbook après adaptation manuelle"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-019]
---

# VEI-020 — Vérifier le cookbook après adaptation manuelle

## Objectif et résultat attendu

Une chaîne de cookbook bornée reproduit la synthèse locale sur fixtures, avec dry-run jetable et droits vérifiés.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `managed-agent-cookbooks/reg-monitor/agent.yaml` (seule chaîne de synthèse retenue)
- `managed-agent-cookbooks/reg-monitor/subagents/feed-reader.yaml` (seule chaîne de synthèse retenue)
- `managed-agent-cookbooks/reg-monitor/subagents/materiality-filter.yaml` (seule chaîne de synthèse retenue)
- `managed-agent-cookbooks/reg-monitor/subagents/digest-writer.yaml` (seule chaîne de synthèse retenue)
- `managed-agent-cookbooks/reg-monitor/steering-examples.json` (seule chaîne de synthèse retenue)
- `managed-agent-cookbooks/reg-monitor/README.md` (seule chaîne de synthèse retenue)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Tranches manuelles VEI-003/016 et agent VEI-019 livrés, fixtures RSS/événements, identifiant neuf et schémas/outils disponibles.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Story séparée après adaptation manuelle, pas préalable à lecture ponctuelle. Adapter lecteur au seul RSS choisi et allowlist réelle, JSON d’erreurs et champs français/version/temps ; aucun champ required omis silencieusement. Filtre conserve nature/statut indépendants de pertinence. Writer local unique, échappement/URLs inertes, pas header protecteur/all-clear/Slack worker imaginaire. Corriger docs selon droits effectifs, dry-run y compris injection/échec ; aucun déploiement ou compte réel.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Contrats techniques BASE-008 et cookbook, documentation de capacité source réellement retenue, méthode ; aucune qualification juridique par orchestrateur.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Dry-run exécuté et documenté, schémas/permissions/README concordants ; corpus incomplet reste incomplet et aucun accès distant de diffusion n’existe.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : CB01 — Déploiement jetable avec fixtures JORF/directive/consultation : trois types conservés, sortie dans seule racine.
- Cas limite : CB02 — XML invalide, titre accentué, URL hostile et champ requis absent : erreur structurée/échappement et aucun fetch hors allowlist ni envoi.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Production, abonnement, scheduler, Slack/email et audit de conformité.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

