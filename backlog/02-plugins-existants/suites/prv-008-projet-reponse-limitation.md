---
id: PRV-008
titre: "Préparer la réponse à une demande de limitation"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006, PRV-002]
---

# PRV-008 — Préparer la réponse à une demande de limitation

## Objectif et résultat attendu

L'organisme obtient un projet sur la limitation, les usages concernés et les conditions d'une éventuelle levée.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/dsar-response/SKILL.md (branche limitation)`
- `privacy-legal/references/reponse-limitation.md (à créer)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Fiche PRV-002, motif, données/finalités, contestation et chronologie, capacités/preuves de restriction et destinataires.

## Travail attendu

Rechercher conditions, usages permis et information en cas de levée. Distinguer limitation, suspension de compte, effacement et gel contentieux ; un statut de journal n'est pas preuve technique. Proposer actions par système et messages conditionnels, sans blocage/sécurité garantis. Calendrier PRV-002 et droits liés distincts.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

RGPD/LIL, CNIL/CEPD et jurisprudence sur limitation, usages et notifications ; règles propres au traitement contesté.

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

- Cas normal : A15 : exactitude contestée et capacités documentées ; projet par finalité, conditions de levée à vérifier.
- Cas limite : A16 : compte suspendu mais marketing actif, legal hold seulement déclaré ; pas d'assimilation à limitation RGPD, preuves manquantes visibles.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Blocage SI, mesure contentieuse, fermeture de compte et décision automatique de levée.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
