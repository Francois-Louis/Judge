---
id: PI-025
titre: "Adapter l’agent à un rapport PI local"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-020, PI-021, PI-022]
---

# PI-025 — Adapter l’agent à un rapport PI local

## Objectif et résultat attendu

Après adaptation manuelle, un agent à la demande produit un rapport local des actifs choisis sans diffusion ni recalcul universel.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/agents/ip-renewal-watcher.md` (blocs nécessaires à cette tranche)
- `ip-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/agent-rapport-pi.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contrats PI-020/021/022 livrés, registre/fiches vérifiées, périmètre autorisé, date de référence et sortie locale souhaitée.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Réutiliser rapport manuel et dates qualifiées, ne recalculer toutes dates US. Retirer wildcards Anaqua/CPA/AltLegal/Slack, synchronisation >30 jours automatique, post immédiat et schedule hebdomadaire installé supposé. Droits locaux minimaux, pas système externe faisant vérité juridique. Ne pas déclarer à jour depuis silence, conserver couverture et sources ; inconnus non lapsed. Aucun paiement, dépôt, envoi ni nouveau cookbook dans cette tranche.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Contrats des tâches manuelles et méthode ; règle d’échéance seulement à travers fiche sourcée du titre/régime exact.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Rapport reste local avec couverture et statuts, droits déclarés concordent avec actions ; aucun paiement/dépôt/notification ou job installé.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : AG01 — Portefeuille de recette et fiche de date nationale : même rapport borné que manuel, sans envoi.
- Cas limite : AG02 — Registre ancien, source inconnue et instruction hostile dans notes : données inertes, manques visibles, pas recalcul US ni Slack.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Automatisation planifiée, connecteurs réels, synchronisation, cookbook et diffusion.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

