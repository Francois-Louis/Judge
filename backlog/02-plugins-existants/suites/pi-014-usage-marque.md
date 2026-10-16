---
id: PI-014
titre: "Examiner un usage contesté d’une marque pour la France"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-014 — Examiner un usage contesté d’une marque pour la France

## Objectif et résultat attendu

Une fiche met en regard un titre/signe déterminé et un usage documenté en France, avec faits favorables/contraires et questions réservées.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/infringement-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/usage-marque-france.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Titre/numéro/statut/effets à vérifier, titulaire/mandat, signes reproduits, produits/services, usages/territoire/dates et preuves/licences.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner marque, sans choisir droit depuis classe seule. Rechercher fondement exact selon titre français/UE/effets internationaux et usage ; distinguer descriptif, comparaison, licence ou autre justification à instruire sans fair use quatre facteurs importé. Présenter ressemblances/différences et manques, pas confusion/contrefaçon certaine. Atteinte alléguée n’est ni validité ni absence de droits de tiers. Dessins, brevet, concurrence/pub et domaine sont questions distinctes.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI, titre et INPI ; règlement marque UE/EUR-Lex et EUIPO si titre UE, jurisprudence primaire compétente pour point précis.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Chaque analyse lie critère, fait et source ; aucune contrefaçon ni autorisation d’agir depuis seule similarité ou classe.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : UM01 — Marque enregistrée alléguée et signe proche pour produits décrits : tableau titre/usage/preuves/justifications à vérifier.
- Cas limite : UM02 — Licence antérieure, signe descriptif ou titre incomplet : préserver défense et statut incertain, pas injonction ou Lanham par défaut.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Constat final de contrefaçon, opposition, nullité et toutes formes d’atteinte.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

