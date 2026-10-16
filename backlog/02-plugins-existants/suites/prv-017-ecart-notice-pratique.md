---
id: PRV-017
titre: "Comparer une pratique à ses supports d'information"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-017 — Comparer une pratique à ses supports d'information

## Objectif et résultat attendu

L'organisme obtient écarts entre pratique et notices/écrans, suggestions limitées et questions de fond.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/policy-monitor/SKILL.md (requête ponctuelle)`
- `privacy-legal/references/information-pratiques.md (à créer)`
- `privacy-legal/CLAUDE.md (surfaces et états)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Description projet/réel et preuves, notice/version, catégories/finalités/durées/flux, CMP/écrans, rôles/personnes.

## Travail attendu

Lire support exact plutôt que résumé du profil. Comparer notice, collecte directe/indirecte, écrans, contacts/droits, durées et destinataires ; traceurs/prospection donnent lieu à questions ciblées, pas audit CMP. Séparer information, base, consentement et réutilisation ; phrase ajoutée ne valide pas traitement. Suggestions section/citation/raison limitées aux faits établis. Retirer notices GLBA/HIPAA/FERPA/COPPA par défaut et feu vert can proceed parce que ADVISABLE.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

RGPD/LIL, textes français/européens pour information, traceurs/prospection et secteur ; CNIL/CEPD/jurisprudence, pièces publiées distinctes.

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

- Cas normal : C03 : nouvelle finalité projetée et notice datée ; texte conditionnel et question de base distincts.
- Cas limite : C04 : notice changée, écran contradictoire, pratique non prouvée et label ancien ; divergences séparées sans feu vert.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Publication, audit technique traceurs, collecte consentement et suivi automatique.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
