---
id: PRV-021
titre: "Créer une checklist d'actualité France/UE traçable"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-021 — Créer une checklist d'actualité France/UE traçable

## Objectif et résultat attendu

Le mainteneur dispose d'une checklist par sujet avec dernier accès réel, état de vérification et contrôles à reprendre.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/references/currency-watch.md`
- `privacy-legal/CLAUDE.md (currency watch)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Liste héritée, sources effectivement lues, date, sujets RGPD/LIL, corridors/secteurs explicitement demandés.

## Travail attendu

Retirer COPPA/États/FTC comme socle français sans valider/réfuter leurs assertions par traduction. Structurer RGPD/LIL/CNIL/CEPD/jurisprudence, AIPD/droits/délais/sous-traitance/transferts avec document/version/champ/source/date/état et motif de relecture. Date par entrée, aucune date globale qui paraît tout vérifier. DPF/adéquation et délais à relire si utilisés ; inaccessible/ancien reste non vérifié avec reprise. Index de recherche, pas table exécutable ni corpus automatiquement actuel ; étranger conditionné par lien factuel.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-annexes/exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-annexes/exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

EUR-Lex/JOUE, Légifrance/JO pour LIL/textes, CNIL, CEPD, CURIA et juridictions françaises ; BASE-010 pour accès.

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

- Cas normal : P05 : entrée AIPD relue sur texte officiel exact ; date/version/champ de cette seule entrée actualisés.
- Cas limite : P06 : ancien DPF et accès impossible ; statut inconnu, tentatives et reprise tracées sans date globale ou affirmation de remplacement.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-annexes/exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Veille planifiée, validation de tout le droit privacy, abonnement et format commun BASE-005 modifié.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
