---
id: PRV-010
titre: "Motiver la nécessité ou non d'une AIPD"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006, PRV-009]
---

# PRV-010 — Motiver la nécessité ou non d'une AIPD

## Objectif et résultat attendu

Le porteur obtient une note motivée sur la nécessité d'AIPD ou les faits qui empêchent de conclure.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/use-case-triage/SKILL.md (test AIPD)`
- `privacy-legal/references/necessite-aipd.md (à créer)`
- `privacy-legal/CLAUDE.md (déclencheurs)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Fiche PRV-009, échelle/fréquence, vulnérabilité, technologies/croisements/surveillance, conséquences, mesures et antécédents.

## Travail attendu

Confronter risques aux textes, listes CNIL obligation/exemption et CEPD dans leur champ/version. Séparer obligation, analyse volontaire et préférence interne ; pas de score mécanique ou non-obligation depuis profil vide. Une donnée santé ne suffit pas à importer un régime US. Expliquer réexamen si finalité/échelle change ; absence d'AIPD ne signifie pas autorisation. Corriger provisoire US/lawyer et AIA automatique. Relais PRV-011 par fiche si indisponible.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-annexes/exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-annexes/exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

RGPD/LIL, listes/délibérations CNIL AIPD et exemption, CEPD et jurisprudence ; textes sectoriels selon qualification.

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

- Cas normal : T03 : suivi santé à grande échelle décrit ; critères reliés à faits et sources, sans autorisation de lancement.
- Cas limite : T04 : petit pilote réel, échelle inconnue, exemption invoquée sans champ ; résultat conditionnel, pas d'exemption automatique ni obligation inventée.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-annexes/exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Rédaction AIPD, lancement autorisé, analyse IA complète et revue de toute roadmap.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
