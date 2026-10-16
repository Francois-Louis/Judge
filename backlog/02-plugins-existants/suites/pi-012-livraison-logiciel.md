---
id: PI-012
titre: "Préparer les obligations d’une livraison logicielle bornée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-011]
---

# PI-012 — Préparer les obligations d’une livraison logicielle bornée

## Objectif et résultat attendu

Une checklist de livraison d’un binaire/version compare corpus de dépendances déclaré, licences lues et pièces de réalisation disponibles.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/oss-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/livraison-logiciel.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

SBOM/lockfile/version du livrable, licences PI-011 ou équivalentes, transitifs disponibles, architecture/liaisons/modifications, destinataires et notices/sources prévues.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Borner à une livraison déterminée et corpus explicitement couvert, sans exécuter installation/scanner ni tout historique. Conserver dépendances manquantes, choix de licence/exception et versions. Relier chaque obligation retenue à texte et fait, distinguer NOTICE proposé/fourni/distribué et source disponible/effectivement remise. Incompatibilité alléguée demande textes exacts, pas tableau de mémoire. Aucun open-sourcing automatique ou attestation de conformité depuis case.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Licences/version/exceptions réellement accordées et documents de livraison, droit applicable et sources primaires pour seuls points litigieux.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Checklist conserve corpus non couvert et preuve d’exécution ; aucun livrable prétendu conforme depuis SBOM seul.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : OB01 — Binaire, trois dépendances et textes complets : tableau pièces/obligations/source d’obligation et actions restantes.
- Cas limite : OB02 — Transitifs absents, licence double non choisie ou lien inconnu : couverture limitée, pas affirmation de compatibilité globale.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Audit intégral dépôt, sécurité, exécution build et publication.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

