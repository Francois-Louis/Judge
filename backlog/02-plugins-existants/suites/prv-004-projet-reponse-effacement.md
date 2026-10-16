---
id: PRV-004
titre: "Préparer la réponse à une demande d'effacement"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006, PRV-002]
---

# PRV-004 — Préparer la réponse à une demande d'effacement

## Objectif et résultat attendu

L'organisme obtient un projet distinguant données à effacer, conservation motivée et preuves d'opérations déjà effectuées.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/dsar-response/SKILL.md (branche effacement)`
- `privacy-legal/references/reponse-effacement.md (à créer)`
- `privacy-legal/CLAUDE.md (DSAR effacement)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Fiche PRV-002, catégories/systèmes, durées et obligations invoquées, preuves des opérations, sauvegardes/prestataires, litige déclaré et pièces.

## Travail attendu

Examiner motifs et limites par catégorie/finalité ; ni litige annoncé ni obligation fiscale générique ne justifie tout conserver. Rechercher les notifications aux destinataires, durées et accès résiduels. Distinguer effacement proposé, décidé, demandé, attesté et traitement des sauvegardes/restaurations. Une case cochée ne permet pas d'écrire nous avons supprimé. Calendrier PRV-002, sans fermeture systématique du compte.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-annexes/exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-annexes/exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

RGPD/LIL, CNIL/CEPD et jurisprudence ; texte précis de conservation sectorielle invoqué et régime contentieux si réellement pertinent.

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

- Cas normal : A07 : compte inutilisé et aucun motif de maintien documenté ; actions proposées par système, affirmations limitées aux attestations reçues.
- Cas limite : A08 : factures, litige déclaré sans pièce, backups et prestataire sans attestation ; chaque motif et inconnu séparés, aucune exemption générale.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-annexes/exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Effacement technique, purge/restauration, clôture du compte et stratégie contentieuse.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
