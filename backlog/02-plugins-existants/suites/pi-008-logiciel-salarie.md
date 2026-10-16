---
id: PI-008
titre: "Qualifier les droits sur un logiciel créé par un salarié"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-008 — Qualifier les droits sur un logiciel créé par un salarié

## Objectif et résultat attendu

Une fiche examine un logiciel et les circonstances de création salariée en France sans généraliser à toute création ou invention.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/ip-clause-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/skills/invention-intake/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/logiciel-salarie.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Code/version, contrats/statut/périodes/pays, fonctions et instructions, contributions/auteurs, éléments préexistants/tiers et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner au logiciel créé par salarié privé dans régime à qualifier. Distinguer code, documentation, autres œuvres, invention technique et contributions de tiers ; rechercher conditions du régime logiciel et droits moraux/patrimoniaux pertinents. Contrat ou salaire seul ne décide pas tout. Aucune clause hereby assigns ou waiver moral générique recommandée. Prestataire, stagiaire, agent public, logiciel hors fonctions ou apport antérieur : réserve/cadrage propre ; références OSS transmises à PI-011.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI dispositions propres au logiciel et création salariée, statut/fonctions/contrats et jurisprudence pertinente ; travail pour question de qualité distincte.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Conditions, contributions et périmètre sont visibles ; aucun transfert universel de toutes créations depuis statut salarié.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : LS01 — Développeur privé, code versionné et instructions documentées : carte objets/conditions/pièces, droits restant à vérifier.
- Cas limite : LS02 — Code antérieur et prestation indépendante confondue avec emploi : séparer contributions, pas attribution automatique employeur.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Invention de salarié, toutes œuvres salariées, rémunération et dépôt brevet.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

