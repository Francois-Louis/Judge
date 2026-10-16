---
id: PRV-005
titre: "Préparer la réponse à une demande de rectification"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006, PRV-002]
---

# PRV-005 — Préparer la réponse à une demande de rectification

## Objectif et résultat attendu

L'organisme obtient un projet expliquant corrections prouvées/proposées et désaccords restant à vérifier.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/dsar-response/SKILL.md (branche rectification)`
- `privacy-legal/references/reponse-rectification.md (à créer)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Fiche PRV-002, champs contestés, valeurs minimisées, justificatifs nécessaires, sources/destinataires et preuves de correction.

## Travail attendu

Confronter champ, source et demande ; distinguer donnée factuelle, information incomplète et opinion contestée. Ne pas réviser automatiquement une décision. Lister systèmes, destinataires et notifications à rechercher, avec preuve de correction. Garder une trace minimale des différences sans archiver un justificatif excessif. Calendrier et rôle PRV-002.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-annexes/exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-annexes/exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

RGPD/LIL, CNIL/CEPD et jurisprudence sur rectification/exactitude/notifications ; règles sectorielles du document si nécessaires.

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

- Cas normal : A09 : adresse erronée, justificatif proportionné et attestation CRM ; réponse limitée à la correction prouvée, autres systèmes ouverts.
- Cas limite : A10 : note professionnelle ou score contesté ; distinguer faits et appréciation, pièces et relais sans correction de toute évaluation.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-annexes/exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Écriture en base, contestation de décision scolaire/professionnelle et modification de document officiel.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
