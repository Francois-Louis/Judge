---
id: PI-002
titre: "Préparer une recherche préliminaire de marque pour la France"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-002 — Préparer une recherche préliminaire de marque pour la France

## Objectif et résultat attendu

Un relevé de recherche préliminaire pour un nom et ses produits/services décrit corpus, requêtes, résultats et limites.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/clearance/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/recherche-marque-france.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Signe exact/variantes, produits/services réels, public, territoires/usage envisagés, références disponibles et objectif, fiche PI-001 ou équivalente.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner au nom verbal destiné à la France. Choisir registres selon effets recherchés, INPI/UE/international si pertinent ; ne pas confondre classe, libellé et usage. Tracer source/date/requête/filtres/langue/accès et recherches non faites ; jamais résultat de mémoire. Examiner extraits exacts et statuts sans conclure dead=aucun risque ; noms/dénominations/domaines restent autres droits à instruire. Retirer provisional US, tests surnames/Tam/Brunetti et traductions réputées automatiquement équivalentes.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et sources INPI, titres et registres utiles ; EUIPO/OMPI si effets pertinents en France ; jurisprudence primaire du seul point examiné. Interfaces et couverture à vérifier.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Recherche faite/fournie/non faite sont distinctes ; zéro résultat ou domaine libre ne devient pas disponibilité ni droit d’exploiter.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : M01 — Nom fictif NÉRIVA pour cosmétiques France : périmètre, variantes et résultats sourcés ou absence d’accès explicite, questions de risque ciblées.
- Cas limite : M02 — Export ancien limité aux correspondances exactes et classe 3 : signaler variantes/autres droits non couverts, pas nom disponible ou couverture exhaustive.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Dépôt, opinion complète de disponibilité, tous territoires et opposition.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

