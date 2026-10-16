---
id: PI-019
titre: "Documenter un incident allégué de secret des affaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006]
---

# PI-019 — Documenter un incident allégué de secret des affaires

## Objectif et résultat attendu

Une fiche d’incident attribue information concernée, accès, mesures, actes allégués et preuves sans certifier secret ou détournement.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/infringement-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/incident-secret-affaires.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Information/périmètre, personnes/qualités, mesures d’accès/confidentialité, dates, accords, accès autorisés, divulgation/utilisation alléguées et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner premier relevé français de faits et critères à instruire. Distinguer secret invoqué, valeur, mesures existantes, connaissance publique, acquisition licite/illicite alléguée et exceptions. Contrat NDA seul ne prouve pas tous critères ni droit d’interdire ; pas DTSA/UTSA/preemption ou vol présumé depuis départ salarié. Pas collecte de comptes, accusation envoyée ou consigne de suppression ; relais travail/privacy/contentieux avec question précise.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI ou textes de droits pertinents selon objet, Code de commerce secret des affaires et droit UE/national applicables à vérifier, contrats et preuves, exceptions et jurisprudence primaire.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Allégation et qualification restent séparées ; aucune extraction massive ou accusation de vol depuis seul changement d’employeur.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : SA01 — Document technique identifié et logs d’accès autorisés : carte information/mesures/actes/preuves/contradictions.
- Cas limite : SA02 — Information publique, NDA non signé ou salarié rejoignant concurrent sans acte prouvé : manques visibles, pas secret ou détournement certain.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Enquête intrusive, licenciement, action judiciaire et qualification définitive.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

