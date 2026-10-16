---
id: PI-013
titre: "Lire une lettre d’assertion de droits PI reçue"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-013 — Lire une lettre d’assertion de droits PI reçue

## Objectif et résultat attendu

Une fiche extrait droit, usage reproché, demandes, pièces et dates alléguées d’un courrier reçu sans reconnaissance d’atteinte.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/cease-desist/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/courrier-pi-recu.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Lettre/annexes, auteur/destinataire/qualités, droit/territoire, usage/version, contrats/licences et réception connue.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Lire allégations exactement, demander titre/preuve/mandat et différencier délai demandé/légal/interne. Pas ignore+preserve, DJ préventif, cancel/invalidity ou dommages statutaires US par défaut. Ne pas traiter diligence taille/financement/PACER comme condition de lecture. Préparer questions au titulaire/conseil et relais du droit propre ; aucun accusé/envoyé, date butoir ou dette/droit reconnu depuis lettre.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI du droit identifié, contrat/titre/registre pertinents, règles de procédure seulement si acte qualifié et dates prouvées.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Allégation, preuve et conclusion restent séparées ; aucune notification, réponse ou consentement juridictionnel américain automatique.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : CR01 — Courrier pour nom de marque France avec pièce registre : fiche demandes/usage/titre et points manquants.
- Cas limite : CR02 — Menace brevet US, réception inconnue et rétablissement plateforme demandé : qualifier rattachements/actes, réserver délais et ne pas appliquer régime français universel.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Réponse envoyée, invalidité complète, stratégie contentieuse et exécution.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

