---
id: PI-022
titre: "Présenter un portefeuille PI délimité"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-020]
---

# PI-022 — Présenter un portefeuille PI délimité

## Objectif et résultat attendu

Un rapport des seuls actifs autorisés présente couverture, statuts datés, échéances qualifiées et questions ouvertes.

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/portfolio/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/etat-portefeuille-pi.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Registre/corpus, périmètre d’accès, date de référence, fiches de dates PI-021 ou équivalentes, filtres et objectif.

Une fiche manuelle équivalente à une dépendance métier est admise avec contrôle
de provenance et des manques, sans historique d’exécution ou plugin voisin.
PI-025 attend livraison et recette des tâches manuelles PI-020/021/022, pas
seulement leurs contrats de planification.

## Travail attendu

Conserver report/audit sans recalcul depuis tables intégrées. Source système externe ne gagne pas automatiquement sur titre/registre, conflit à signaler. Distinguer fait expiré allégué/date dépassée/état de vérification, dépôt demandé/prouvé/paiement accepté. agent_managed est responsable déclaré, pas validation de date ; autre règle/pays reste inconnue. Aucun all-clear depuis registre vide/ancien et pas divulgation interclient. Dashboard si utile avec échappement.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d’action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit/titre,
objet/version, acteur/qualité, territoire/actes/dates, sources/pages, manques
et conclusion réservée ; aucun lancement automatique d’un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Méthode locale, preuves de titres/dates réellement lues ; nouvelles conclusions exigent recherche de régime propre.

Pistes non vérifiées dans EXIST-008 : rechercher passage exact, version aux
dates utiles, champ, statut, transitions, lien et date réelle de consultation.
Choisir sources/registre/juridiction d’après titre et territoire ; INPI, EUIPO
et OEB ne sont pas obligatoires ensemble. Une source inaccessible donne voie
officielle alternative BASE-010 puis réserve de la seule conclusion dépendante,
sans droit, titre, date ou consultation inventés. Contrats et licences réellement
accordés sont lus ; connexion déclarée ne prouve ni recherche ni authentification.

## Critères d'acceptation

- [ ] Rapport garde inconnues et couverture ; compteur ou statut ne prouve ni droits vivants ni perte, paiement ou enregistrement réalisé.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.
- [ ] Branches héritées signalées ; brouillon, choix interne ou résultat
  partiel ne devient autorisation d’exploiter, droit acquis ou action externe.

## Vérification

- Cas normal : EP01 — Trois actifs avec dates de natures différentes : rubriques avec statut/provenance, sans assimilation de titres.
- Cas limite : EP02 — Échéance sans source, entrée ancienne ou accès partiel : revue nécessaire, pas tout à jour ou aucun risque.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. La
[relecture du cadrage](../exist-008-annexes/exist-008-verification.md) n’est pas cette recette.

## Hors périmètre

Nouveaux calculs universels, paiement, dépôt et certification de propriété.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-008, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
la prochaine tranche attend une sélection explicite, aucun skill adapté ou
agent déployé n’est livré par ce cadrage.

