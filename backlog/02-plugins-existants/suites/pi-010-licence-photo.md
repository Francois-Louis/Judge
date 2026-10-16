---
id: PI-010
titre: "Examiner une licence d’utilisation de photographie"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-010 — Examiner une licence d’utilisation de photographie

## Objectif et résultat attendu

Une fiche relie licence exacte, photo/version, acteur et usage prévu, avec autorisations, conditions et inconnues.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/ip-clause-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/licence-photo.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Licence/version/conditions à date, photo/origine, concédant/qualité, usages/supports/pays/durée, modifications et sous-licence envisagées.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Distinguer licence/cession, exclusivité, périmètre, crédit, modifications et droits de tiers ; pas licence implicite depuis accès au site ou paiement. Lire contrat/annexes et version réellement accordée, conditions de sortie/fin et preuve d’autorité du concédant. Ne pas appliquer CC par label ni supposer toutes clauses valides. Si interprétation réservée, proposer question précise plutôt que feu vert.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et contrat/licence effectivement accordée, texte officiel/version de licence standard si utilisée ; droits de tiers à rechercher selon faits.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Chaque usage envisagé renvoie à une clause ou reste réservé ; licence ne devient pas propriété ni autorisation tous usages.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : L01 — Photo autorisée sur site associatif, campagne payante envisagée : comparer supports/finalité/crédit et demander extension si nécessaire à instruire.
- Cas limite : L02 — Métadonnée CC sans version/texte ou licence non commerciale ambiguë : pas permission certaine, demander preuve exacte.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Licence logicielle/OSS, rédaction complète, signature et publication.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

