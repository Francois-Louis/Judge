---
id: PRV-018
titre: "Produire un rapport de dérive sur un corpus délimité"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006, PRV-017]
---

# PRV-018 — Produire un rapport de dérive sur un corpus délimité

## Objectif et résultat attendu

Le gestionnaire obtient changements lus, surfaces affectées et accès incomplets avec reprise fiable.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/policy-monitor/SKILL.md (sweep et reprise)`
- `privacy-legal/references/suivi-derive.md (à créer)`
- `privacy-legal/CLAUDE.md (dernier passage)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Périmètre autorisé dossier/pratique, inventaires, outputs/version/date, supports exacts, preuves d'état et dernier passage complet.

## Travail attendu

Comparer identifiants/versions et pas seuls noms/dates ; projet/revu/signé/déployé/retiré distincts, APPROVED ne prouve pas pratique. Réutiliser PRV-017, préserver gravité/raison d'évolution. Journaliser lus/non lus/illisibles, pas de policy current depuis dossier vide. Pointeur limité au périmètre traité avec succès ; dernier état complet préservé sur échec, reprise sans perte/doublon. Aucun autre dossier par défaut. Rapport local et données minimales dans dashboard ; cadence seulement si réellement activée dans un futur lot.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

Sources PRV-017 et des constats repris avec statut/date vérifiés ; changement de fichier ne prouve pas nouveauté normative.

Pistes non vérifiées par EXIST-003 : lire passages exacts, version, champ et
transitions à la date pertinente. Tracer lectures/échecs, employer les voies
officielles BASE-010 sans abonnement obligatoire ; distinguer texte,
recommandation, pièce, fait déclaré et préférence.

## Critères d'acceptation

- [ ] Le résultat annoncé est observable sur le cas normal avec pièces/localisations.
- [ ] Le cas limite garde les inconnues et une prochaine démarche compréhensible.
- [ ] Rôles, règles, préférences, preuves et actions proposées/exécutées restent distincts.
- [ ] Sources, versions et applicabilité sont tracées ; chaque délai a son déclencheur.
- [ ] Une personne sans formation juridique peut utiliser la sortie sans service juridique imposé.
- [ ] Le paquet détaché charge ses références locales et respecte BASE-008.
- [ ] Aucune action externe, requête SI ou transmission n'est annoncée sans preuve.
- [ ] Documentation, métadonnées et NOTICE reflètent seulement la tranche adaptée.

## Vérification

- Cas normal : C05 : DPA modifié et AIPD projet sans preuve d'exécution ; changements/états séparés sans pratique déclarée réelle.
- Cas limite : C06 : Drive partiel, PDF illisible, fichier remplacé sous même nom ; rapport incomplet et pointeur complet préservé.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Scheduler, crawl global, Slack, publication, registre général et corrections exécutées.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
