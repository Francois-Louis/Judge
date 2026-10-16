---
id: PI-021
titre: "Documenter une échéance de renouvellement de marque française"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-020]
---

# PI-021 — Documenter une échéance de renouvellement de marque française

## Objectif et résultat attendu

Une fiche d’une échéance de marque nationale française expose source, déclencheur, calcul éventuel et état de vérification.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/portfolio/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/echeance-marque-france.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche PI-020 ou équivalente, marque/numéro/type/statut, dépôt/renouvellements documentés, notification/décision si pertinente, date de référence et acteur.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner marque nationale française, ne pas étendre à marque UE/Madrid/brevet/domaines. Vérifier règle actuelle/version, événement déclencheur/preuve, méthode reproductible, exceptions/prolongations et calendrier propre ; sinon a-determiner avec pièce utile. Échéance juridique, jalon interne et paiement/dépôt effectif séparés. Retirer §8/§9/§15, 3.5/7.5/11.5 et toute perte du titre déduite de date dépassée. Calcul ne certifie ni maintien ni possibilité de restauration.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et textes/modalités INPI applicables au titre aux dates utiles, pièces de renouvellement/notifications et décisions, calcul/recours selon seule question retenue.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Chaque date calculée est reproductible/sourcée ; date manquante ou statut incertain ne devient ni lapsed ni date par défaut.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : EC01 — Marque nationale identifiée, dates/pièces complètes : fiche de date et actions/preuves restant à obtenir, sans paiement.
- Cas limite : EC02 — Export ancien sans renouvellement ou titre UE présenté comme français : réserver calcul/champ et demander pièces, pas application règle nationale automatique.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Paiement, dépôt, restauration, autres titres et calendrier universel.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

