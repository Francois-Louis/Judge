---
id: PI-011
titre: "Examiner la licence d’une dépendance logicielle"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-011 — Examiner la licence d’une dépendance logicielle

## Objectif et résultat attendu

Une fiche d’un paquet/version identifie licence réelle, exceptions/options et questions liées au montage d’utilisation décrit.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/oss-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/licence-dependance.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Paquet/version/commit et provenance, LICENSE/NOTICE/en-têtes, licence/version exacte, dépendances connues, modifications et usage réel.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Lire texte et fichiers, distinguer metadata SPDX, octroi réel, source-available et choix dual. Ne pas traiter absence comme permissif, ni label GPL/AGPL/LGPL comme réponse. Rechercher clauses pertinentes au montage précis : copie/distribution, modification, liaison, réseau et destinataires, sans AGPL réseau=distribution ou static/dynamic couleur automatique. Contradiction reste visible ; aucune compatibilité universelle ou remplacement conseillé depuis mémoire.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Licence officielle/version/exception et octroi réel des fichiers, CPI/droit applicable seulement pour question précise ; métadonnée n’est pas texte.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Obligation et qualification reposent sur passage/version/faits ; inconnue de licence demeure inconnue, sans feu vert de livraison.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : OS01 — Paquet versionné et texte LGPL fournis avec liaison décrite : fiche conditions/preuves/questions sans couleur automatique.
- Cas limite : OS02 — README MIT, fichiers GPL et composant réseau AGPL : distinguer objets/versions/conflits, pas tout permissif ou réseau=distribution.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Audit sécurité, compatibilité tous paquets, publication et livraison.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

