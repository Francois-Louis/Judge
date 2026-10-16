---
id: PI-005
titre: "Préparer l’examen de brevetabilité d’une invention"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-003]
---

# PI-005 — Préparer l’examen de brevetabilité d’une invention

## Objectif et résultat attendu

Un dossier borné d’une invention précise questions d’examen et antériorités effectivement disponibles, sans avis de brevetabilité.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/invention-intake/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/dossier-brevetabilite.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche technique PI-003, contributions/dates/divulgations, pays/voie envisagée, documents techniques et références antérieures fournies ou récupérées.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Remplacer verdict des screens US par questions sourcées sur objet technique, nouveauté, activité inventive et conditions du régime choisi. Distinguer recherche réalisée, références connues et non recherchées ; ne pas déduire nouveauté d’absence de résultat ou inventivité du seul gain. Brevet français et voie européenne ne sont pas même procédure ; pas OEB plus permissif donc admissible, pas §101/Alice ou grâce US généraux. Droit de déposer/emploi et liberté d’exploitation sont sujets séparés.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et documentation/exigences INPI pour voie française ; CBE/OEB pour voie européenne effectivement envisagée, publications techniques exactes et versions.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Le dossier porte ses recherches/non-recherches et ne conclut ni brevetabilité ni permission de commercialiser ; aucune antériorité inventée.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : B01 — Mécanisme précis et deux publications connues : questions par condition et passages à comparer, sans verdict global.
- Cas limite : B02 — Logiciel/IA avec description fonctionnelle seulement ou divulgation incertaine : demander détails/chronologie, sans rejet Alice ni promesse OEB.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Rédaction de revendications, dépôt, FTO complète et avis spécialiste final.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

