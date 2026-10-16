---
id: PRV-013
titre: "Qualifier les rôles sur les opérations d'un contrat"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-013 — Qualifier les rôles sur les opérations d'un contrat

## Objectif et résultat attendu

Client ou prestataire obtient une matrice finalité/opération/acteur/rôle pour choisir le cadre contractuel à rechercher.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/dpa-review/SKILL.md (qualification des rôles)`
- `privacy-legal/references/roles-traitement.md (à créer)`
- `privacy-legal/CLAUDE.md (rôles par opération)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Contrat/DPA/annexes, finalités/moyens réellement décidés, instructions/usages propres, sous-prestataires, personnes/pays et utilisateur.

## Travail attendu

Confronter étiquettes et faits sans inférer rôle du sens de l'envoi/paiement ou politique unique. Couvrir chaîne, responsables autonomes/conjoints et activités mixtes. Relier chaque qualification aux opérations/preuves ; pièces et désaccords visibles. Art. 26/28 à rechercher ; responsable/responsable reçoit une fiche hors revue sous-traitance, pas playbook inversé. Ne pas écrire un rôle universel dans le profil.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-annexes/exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-annexes/exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

RGPD/LIL, CEPD/CNIL et jurisprudence CJUE/française sur responsable, sous-traitant, conjoints et usages propres.

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

- Cas normal : D01 : hébergement sur instructions d'une association ; matrice indépendante de l'auteur du DPA.
- Cas limite : D02 : usages d'entraînement propres étiquetés processor ; finalités distinguées, mauvais modèle réservé.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-annexes/exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Accord art. 26 rédigé, revue DPA/MSA, transferts et licéité globale des usages.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
