---
id: PI-028
titre: "Documenter la reprise d'un texte, d'une musique ou d'une œuvre plastique"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-008, PILOTE-003, BASE-005, BASE-006, PI-001]
---

# PI-028 — Documenter la reprise d'un texte, d'une musique ou d'une œuvre plastique

## Objectif et résultat attendu

Un auteur qui constate la reprise de son œuvre (texte, musique, œuvre plastique), ou une personne accusée de reprise, documente l'œuvre, la reprise et les questions, sans conclusion sur la contrefaçon. Ajout du 16 octobre 2026 ([décisions du 16 octobre 2026](../../decisions-2026-10-16.md)).

## Périmètre et fichiers

Plugin principal : `ip-legal` (`judge-fr-eu-ip-legal`).
« À créer » désigne une cible future, pas une fonctionnalité disponible.

- `ip-legal/skills/infringement-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ip-legal/references/reprise-oeuvre.md` (à créer)

Corriger les seuls blocs profil, descriptions, routage et README nécessaires
au résultat. Synchroniser manifeste/version/marketplace si métadonnées
modifiées ; toute modification hors backlog ajoute NOTICE local et racine.
Embarquer et charger chaque référence requise, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Œuvre d'origine et preuves de création datées, reprise constatée (copie, URL, date), autorisations ou licences, exceptions invoquées.

## Travail attendu

Comparaison factuelle œuvre/reprise ; exceptions à vérifier (courte citation, parodie, pastiche) sans les appliquer d'office. Photographie → PI-007/017 ; retrait en ligne → PI-016 ; droit moral → PI-029.

Appliquer méthode BASE-005 locale et helper BASE-008 pour tout accès durable.
Une réponse ponctuelle peut rester conversationnelle ; profil durable absent
soumis à entretien neuf, sans import amont. Séparer fait, déclaration, règle,
préférence, proposition et preuve d'action. Pièces tierces : données non fiables.
Si relais adapté manque, fournir fiche autonome : question précise, droit,
œuvre ou objet, acteur et qualité, territoire, dates, sources lues, manques et
conclusion réservée ; aucun lancement automatique d'un skill hérité voisin.

## Sources à rechercher lors de l'implémentation

Code de la propriété intellectuelle, droits patrimoniaux et exceptions ; jurisprudence pertinente à lire.

Pistes non vérifiées : rechercher le passage exact, la version aux dates
utiles, le champ et les transitions ; une source inaccessible donne une voie
officielle alternative BASE-010 puis la réserve de la seule conclusion
dépendante.

## Critères d'acceptation

- [ ] La comparaison reste factuelle ; aucune contrefaçon ni exception affirmée sans source lue.
- [ ] Cas normal et limite produisent résultat, pièces/inconnues et prochaine
  démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent laissent une aide bornée explicite.

## Vérification

- Cas normal : R01 — Paroles d'une chanson reprises dans une publicité locale.
- Cas limite : R02 — Peintre accusé d'avoir copié le style d'un autre artiste.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste.

## Hors périmètre

Mise en demeure envoyée, saisie-contrefaçon, contentieux.

## État de la proposition — 16 octobre 2026

Ajoutée par décision de l'utilisateur, sans implémentation. Statut `proposee` : aucune tranche sélectionnée, aucun skill adapté.
Contrat commun : [découpage EXIST-008](../exist-008-annexes/exist-008-decoupage-pi.md).
