---
id: PI-006
titre: "Rapprocher une caractéristique et une revendication pour la France"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-006 — Rapprocher une caractéristique et une revendication pour la France

## Objectif et résultat attendu

Un tableau compare une caractéristique documentée à une revendication identifiée d’un titre pertinent pour la France, avec ambiguïtés et limites.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/fto-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/skills/infringement-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/rapprochement-brevet-france.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Produit/version et actes/pays, titre/numéro, texte de revendication/version, statut/effet territorial à vérifier, pièces techniques et objectifs.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner à un titre et une revendication, sans balayage FTO. Qualifier demande/titre, famille, effet en France, validations/effet unitaire éventuel et statut daté sans les présumer depuis numéro EP. Comparer passages techniques, laisser interprétation/équivalents/validité réservés. Retirer §271/treble damages et tableau US comme test français. Ne pas lancer litigation claim-chart hérité ; remettre fiche autonome spécialiste si nécessaire. Design/PP/RE ou pays différent exigent autre qualification.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI, titre et registre INPI/OEB selon voie/effet ; CBE, textes UE/accord JUB et jurisprudence seulement pour point/juridiction pertinent à établir.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Chaque cellule est sourcée ; aucun non-recoupement ou recherche partielle ne vaut liberté d’exploitation, absence de contrefaçon ou statut valide.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : F01 — Produit versionné et revendication EP fournie pour usage France : tableau passages/preuves/manques et statut territorial à vérifier.
- Cas limite : F02 — Titre délivré mais revendications amendées/validation inconnues : réserver comparaison finale, pas EP=protection partout ou expired=libre.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

FTO complète, validité/contrefaçon finale, toutes revendications et revendications nouvelles.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

