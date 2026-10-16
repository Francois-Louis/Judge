---
id: PI-016
titre: "Qualifier une demande ou décision de retrait de contenu"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-016 — Qualifier une demande ou décision de retrait de contenu

## Objectif et résultat attendu

Une fiche identifie contenu, droit invoqué, service/canal et régime à rechercher avant signalement ou contestation.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/takedown/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/skills/cease-desist/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/qualification-retrait.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contenu/URL exacts, original/droit allégué, auteur/titulaire/mandat, service/activité, décision ou formulaire/version, pays/actes/dates et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Définir mode français explicite sans renommer technique avant tâche. Séparer réclamation au titulaire, notification à hébergeur, modération/compte et acte judiciaire. Qualifier rôle du service/rattachements et instrument pertinent, pas DSA=DMCA ni siège US=DMCA automatique. Identifier pièces/coordonnées exigées et diffusion potentielle à instruire. Retirer serment, consentement fédéral, fair use et 10–14 jours dans parcours français ; régime étranger justifié hors recette avec fiche spécialiste.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

CPI, textes UE/France de services et retrait pertinents, notamment DSA et textes nationaux selon qualification, conditions réelles du service ; US seulement après rattachement vérifié.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Canal/régime inconnu reste à établir ; aucune contre-notification US ou promesse de retrait/rétablissement depuis une URL.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : RT01 — Photo copiée sur service accessible en France : qualifier droit/titulaire/hébergeur et pièces avant notification.
- Cas limite : RT02 — Compte suspendu pour spam ou demande DMCA sans acte complet : relais modération/DOM-034 ou examen étranger ciblé, pas formulaire PI automatique.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Soumission, décision de contrefaçon, suppression et contentieux.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

