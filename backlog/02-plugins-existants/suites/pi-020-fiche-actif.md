---
id: PI-020
titre: "Enregistrer les faits d’un actif PI"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-020 — Enregistrer les faits d’un actif PI

## Objectif et résultat attendu

Une fiche/entrée de registre identifie un actif, territoire/effets, personnes, dates et sources sans recalcul universel.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/portfolio/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/fiche-actif-pi.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Titre/document/export ou déclaration, type/identifiants, pays/effets, titulaire déclaré/inscrit, dates/statuts, pièces de chaîne et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Posséder schéma registre/actif et données sourcées sans importer compte automatiquement. Distinguer dépôt/délivrance/statut daté et propriétaire déclaré/inscrit/transfert à vérifier. Famille et titre ne fusionnent pas pays, effets EP/unitaire à établir ; domaine inscrit comme autre actif hors titre PI. Corriger exemples US du modèle inline et seeds setup associés. Retirer next_deadlines calculées à l’init : PI-021 ou fiche manuelle vérifiée. Toute donnée conflictuelle garde sa source.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Titre/registre pertinent INPI, EUIPO, OEB ou OMPI selon actif et effets, actes de cession/licences ; statut juridique non certifié depuis seul système.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Chaque état porte source/date/qualité ; aucune délivrance, propriété complète ou échéance supposée depuis export.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : PO01 — Marque nationale française et export : entrée identifiée avec statut daté, manques de chaîne visibles.
- Cas limite : PO02 — Même famille brevet sur deux territoires, titulaire divergent : conserver objets/sources séparés, pas synchronisation autoritaire.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Audit de propriété exhaustif, annuités tous titres et migration inter-systèmes.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

