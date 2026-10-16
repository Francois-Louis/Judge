---
id: PI-017
titre: "Préparer un signalement de reprise de photographie"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-007, PI-016]
---

# PI-017 — Préparer un signalement de reprise de photographie

## Objectif et résultat attendu

Un projet local sur une photographie et des emplacements précis rassemble justification de droits, faits et éléments requis par le canal qualifié.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/takedown/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/signalement-photo.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Chaîne PI-007, qualification PI-016 ou équivalentes, photographie/version, URL localisées, copies/licences, service/canal et qualité du déclarant.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner régime français/UE préalablement qualifié et reproduction de photo documentée. Vérifier autorité, œuvre/usages, droits/exceptions/autorisations alléguées et éléments du mécanisme exact à partir de sources, sans déclarer illicéité certaine. Proposer uniquement données nécessaires, points réservés et preuve de réception à obtenir après soumission. Aucun modèle DMCA, serment/perjury, consentement fédéral, fair use ou garanties de confidentialité/délai. Texte distinct de dépôt.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI droit d’auteur et mécanisme de notification France/UE retenu, texte DSA/national pertinent et modalités officielles du service réellement lues.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Le projet relie chaque URL et droit à sa pièce ou réserve ; brouillon non déposé, aucun retrait garanti.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : SP01 — Photographe et droits documentés, copie exacte localisée : projet avec emplacement/justification et manques propres au canal.
- Cas limite : SP02 — Licence possible, auteur non confirmé ou page non lue : réserver faits/droit et demander pièce, pas affidavit ou demande mensongère.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Dépôt, atteintes tous droits, retrait effectif et rétablissement.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

