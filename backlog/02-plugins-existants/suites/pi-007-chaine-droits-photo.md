---
id: PI-007
titre: "Documenter la chaîne de droits d’une photographie"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-007 — Documenter la chaîne de droits d’une photographie

## Objectif et résultat attendu

Une fiche distingue auteur allégué, titulaires/mandats, droits revendiqués et usages autorisés sur une photographie déterminée.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/infringement-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/skills/ip-clause-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/chaine-droits-photo.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Photo/version/origine, auteur/contributeurs, date/pays, contrat/commande, cessions/licences, usage et documents disponibles.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Qualifier œuvre et preuves sans originalité ou titularité déduite du fichier, paiement ou watermark. Identifier auteur, droits patrimoniaux et questions de droit moral séparés ; licence n’est pas cession. Création salariée demande régime/qualité propres, pas work-for-hire universel ni logiciel appliqué à photo. Retirer enregistrement Copyright Office comme préalable français. Apport IA ou autres personnes/droits à l’image : question distincte et limites, pas droit certifié depuis outil.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI droit d’auteur, contrats/cessions/licences exacts, sources UE/jurisprudence du point retenu ; droits à l’image/données en relais si concernés.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Chaque maillon est prouvé/déclaré/inconnu ; aucune propriété complète depuis commande, paiement, travail salarié ou métadonnée.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : DA01 — Photographe indépendant et association avec licence email : carte auteur/autorisation/usage/limites.
- Cas limite : DA02 — Photo créée par salarié ou générée avec IA sans contribution documentée : réserver régime/droits, demander pièces sans appliquer US copyright.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Certification d’originalité, cession nouvelle, droit à l’image complet et contentieux.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

