---
id: PI-018
titre: "Lire une notification de retrait de contenu"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-016]
---

# PI-018 — Lire une notification de retrait de contenu

## Objectif et résultat attendu

Une fiche distingue décision du service, réclamation du tiers, motifs et voies à vérifier avec pièces/dates manquantes.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/takedown/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/notification-retrait-recue.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Notification intégrale/annexes, contenu/URL/version, service/rôle, motif/droit, licence/contrat et réception connue.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner lecture à acte/canal qualifiés ; relever qui affirme quoi et si décision exécutée ou seulement annoncée. Distinguer défense sur droits et mécanisme de contestation du service ; lister voies/délais seulement si fondement/version/point de départ vérifiés, sinon a-determiner. Ne pas traduire counter DMCA en recours UE, ne signer consentement fédéral ni promettre rétablissement. Suspension de compte sans PI → DOM-034.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et textes/mécanismes France/UE ou étrangers selon acte exact, conditions et décision du service, sources de voies/notification propres.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Aucune option ne produit de dépôt, aveu, compétence ou date butoir inventée ; faits/licences contradictoires conservés.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : NR01 — Retrait de photo malgré licence fournie : fiche des motifs/licence/versions et pièces utiles à contestation.
- Cas limite : NR02 — Notice DMCA réelle alléguée, destinataire non-US et annexes absentes : réserver régime/conséquences et relais qualifié, pas counter automatique.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Contre-notification soumise, conseil tous pays et garantie de rétablissement.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

