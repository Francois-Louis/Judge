---
id: PI-023
titre: "Gérer des préférences PI volontaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-023 — Gérer des préférences PI volontaires

## Objectif et résultat attendu

Un auteur, salarié, TPE ou professionnel modifie des préférences explicites sans en faire des règles ou capacités actives.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/cold-start-interview/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/skills/customize/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/CLAUDE.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/preferences-pi.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Demande ciblée, rôle/pays déclarés, profil éventuel et périmètre de changement.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Conserver entretien neuf, reprise, provenance et digest BASE-008 ; harmoniser modèles inline/profil, aide ponctuelle sans setup. Séparer appétence, critères internes et faits/règles ; ship-blocker n’est pas obligation de licence, classe ajoutée n’installe pas veille. Retirer patent agent USPTO comme qualité française, protection par header, dates calculées depuis seed portfolio et stage partagé inventé. Aucun secret ou compte actif déduit du champ.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Contrats BASE-008 et méthode ; règles de qualité/représentation selon tâche réelle, sans validation depuis préférence.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Une modification reste ciblée et ne requalifie aucun droit/date/dossier ; profil absent n’est pas créé ou importé hors entretien neuf.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : PR01 — Photographe demande langage simple et change interlocuteur : changement attribué sans entretien cabinet complet.
- Cas limite : PR02 — Profil absent/interrompu ou modification concurrente : aide ponctuelle possible, pas d’écrasement ou d’import amont.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Qualification automatique, activation connexion et migrations globales.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

