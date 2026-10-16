---
id: PRV-003
titre: "Préparer la réponse à une demande d'accès"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006, PRV-002]
---

# PRV-003 — Préparer la réponse à une demande d'accès

## Objectif et résultat attendu

Un responsable de petite structure obtient un projet d'accès et la note des données/informations à communiquer et à contrôler.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/dsar-response/SKILL.md (branche accès)`
- `privacy-legal/references/reponse-acces.md (à créer)`
- `privacy-legal/CLAUDE.md (systèmes et sortie accès)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Fiche PRV-002, systèmes, extractions et preuves de recherche, destinataires, durées/finalités, identité et canal sûr à confirmer.

## Travail attendu

Distinguer non recherché/non trouvé/trouvé/illisible par système, sans requête SI. Préparer copie et informations de traitement avec preuves ; une liste de catégories n'est pas automatiquement la copie. Examiner tiers, secrets et limites motivées, occultation partielle plutôt que refus global ou sur-invocation d'exemptions. Séparer lettre externe et note interne, pièces et canal proposé. Calendrier PRV-002 ; aucune exhaustivité sur corpus incomplet.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

RGPD/LIL, CNIL/CEPD et jurisprudence CJUE/française sur copie, informations, destinataires, tiers et limites ; textes sectoriels pertinents.

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

- Cas normal : A05 : CRM/tickets et informations de traitement fournis ; copie/informations à joindre expliquées, aucune transmission déclarée.
- Cas limite : A06 : email avec données de tiers, pièce illisible et sauvegarde non recherchée ; occultation ciblée et inconnues, pas d'exemption générale backups/journaliste.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Extraction SI, accès automatisé, envoi, autres droits et procédure de plainte.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
