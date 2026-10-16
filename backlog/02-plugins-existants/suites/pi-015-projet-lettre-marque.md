---
id: PI-015
titre: "Préparer une lettre sur un usage de marque en France"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-014]
---

# PI-015 — Préparer une lettre sur un usage de marque en France

## Objectif et résultat attendu

Un projet local de lettre proportionnée pour un usage de marque identifié présente droit, faits et demande avec réserves.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/cease-desist/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/projet-lettre-marque.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche PI-014 ou équivalente, preuves/versions, qualité/mandat du signataire, destinataire, objectif et canal/notification envisagés.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner au droit/territoire français qualifiés ; vérifier demande et conséquences sans menacer dommages ou recours US. Distinguer assertion, demande de précisions et négociation. Retirer diligence universelle effectifs/PACER/financement et escalades de profil avant tout brouillon ; identité, titre et autorité utiles restent à instruire. Pas signalement plateforme simultané obligatoire, preservation demand US ou date fixe. Projet/envoi/réception séparés, pas envoi.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et sources du titre/usage qualifiés, représentation/notification et déontologie selon signataire ; procédure propre si menace précise.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Le projet cite preuves/limites et demande choisie ; aucun mandat, envoi, délai légal ou protection par mention n’est présumé.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : CM01 — Usage documenté et titre/mandat vérifiés : lettre factuelle avec demande bornée et checklist de revue.
- Cas limite : CM02 — Titularité ou licence contestée et demande d’annonce de poursuites certaines : réserves et questions, pas menace inventée ou double dépôt plateforme.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Autres droits, transaction complète, action judiciaire et envoi.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

