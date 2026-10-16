---
id: PI-009
titre: "Examiner une cession de droits sur une photographie"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-009 — Examiner une cession de droits sur une photographie

## Objectif et résultat attendu

Une revue ciblée explique portée et manques d’une clause de cession pour une photographie d’un indépendant.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/ip-clause-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/cession-photo.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contrat complet/annexes, photo identifiée, auteur/chaîne, qualité/côté, droits/usages/territoires/durée/prix et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner à une cession envisagée sous régime français qualifié, séparer propriétaire du support et droits. Lire droits cédés, destination, étendue, rémunération et exclusions selon sources ; ne pas substituer simply hereby assigns ou renonciation générale morale. Garantie/indemnité et transfert ont analyses distinctes. Conserver redline minimale si base vérifiée, sinon questions ciblées. Création salariée, logiciel, brevet ou cession globale future hors branche.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI règles de cession/droit moral/rémunération selon œuvre et faits, contrat réel et jurisprudence pertinente aux dates.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] La portée de cession est expliquée sans inventer droit détenu ; pas de waiver moral ou formule US réputée suffisante.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : C01 — Contrat photo pour catalogue avec clause mondiale illimitée : comparer usage voulu/texte, droits et points à négocier.
- Cas limite : C02 — Facture payée sans clause ou auteur absent : signaler chaîne/consentement manquants, aucune cession présumée.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Signature, transaction, toutes cessions PI et revue B2B générale.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

