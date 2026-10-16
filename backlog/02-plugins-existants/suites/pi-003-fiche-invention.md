---
id: PI-003
titre: "Constituer une fiche factuelle d’invention"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-003 — Constituer une fiche factuelle d’invention

## Objectif et résultat attendu

Une fiche technique attribue contributions, dates et divulgations d’une invention décrite sans verdict de brevetabilité.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/invention-intake/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/fiche-invention.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Description technique, versions, contributeurs/qualités, problème/solution, notes datées, démonstrations/publications et contrats disponibles.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Extraire faits du dossier, demander manques sans inventer mécanisme/contribution. Séparer inventeur, employeur, déposant et titulaire allégués. Distinguer date de document, conception alléguée et divulgation prouvée avec destinataires/contenu/conditions. NDA mentionné ne prouve pas tout confidentiel. Retirer score novelty/§101, délai de grâce un an et dépôt/renoncement depuis pitch. Préparer questions à PI-004/005 seulement si pertinentes ; protéger accès aux détails sans header garantissant secret.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et sources de preuve/qualité seulement pour les questions propres au dossier, pièces techniques/contrats ; brevetabilité en tâche séparée.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Chaque contribution et divulgation a une source ou statut déclaré ; aucun brevet, droit de l’employeur ou date butoir déduit.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : I01 — Salarié décrit prototype et trois contributeurs : fiche versions/contributions et documents nécessaires.
- Cas limite : I02 — Démonstration client alléguée sous NDA sans accord ni date : inconnues explicites, aucune grâce ou perte de droits certaine.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Brevetabilité, droit à rémunération chiffré, revendications et dépôt.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

