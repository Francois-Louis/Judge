---
id: PI-004
titre: "Qualifier une invention de salarié en France"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-003]
---

# PI-004 — Qualifier une invention de salarié en France

## Objectif et résultat attendu

Une fiche conditionnelle examine une invention et la relation salariée, avec pièces nécessaires à classification, droits et obligations à instruire.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/invention-intake/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/skills/ip-clause-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/invention-salarie.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Fiche PI-003 ou équivalente, contrat/statut, mission effective, employeur, pays/période, contributions, moyens, déclarations/échanges et accords collectifs pertinents.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner salarié privé relevant du régime français à qualifier. Examiner mission inventive, fonctions réelles, circonstances/moyens et chaîne d’employeurs ; ne pas déduire propriété du salaire ou contrat seul. Séparer classification, déclarations, droit d’attribution/cession éventuel et questions de rémunération ; chaque délai exige texte/version/déclencheur prouvé. Logiciel, indépendant, agent public ou collaboration étrangère : autre régime à qualifier, pas work-for-hire ou présent assignment automatique.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI et textes d’application inventions de salariés, contrat/accord collectif et sources emploi pour qualité/mission, jurisprudence primaire pertinente aux dates.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Classification est motivée ou réservée par faits/critères ; aucune titularité ou rémunération automatique et pas de régime logiciel confondu avec invention.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : IS01 — Ingénieur privé avec mission inventive décrite et prototype : carte critères/pièces, manques et obligations à vérifier.
- Cas limite : IS02 — Développeur prestataire ou agent public présenté comme salarié : réserver champ et préparer relais, pas cession ni déclaration salariale fictive.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Contentieux, calcul de rémunération, toutes créations salariées et dépôt.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

