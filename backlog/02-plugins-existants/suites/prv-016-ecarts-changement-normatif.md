---
id: PRV-016
titre: "Comparer un changement normatif à des pratiques documentées"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-016 — Comparer un changement normatif à des pratiques documentées

## Objectif et résultat attendu

Un responsable associatif ou DPO obtient écarts établis/inconnus pour un changement déterminé et actions/preuves proposées.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/reg-gap-analysis/SKILL.md`
- `privacy-legal/references/ecarts-normatifs.md (à créer)`
- `privacy-legal/CLAUDE.md (sources et suivi)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Changement/version/dates, traitement/périmètre, notice et preuves de pratique, mesures et états des actions.

## Travail attendu

Lire le texte exact et qualifier portée/temps, sans transformer guide/résumé en norme. Comparer exigence/preuve et distinguer absence d'écart, absence de preuve, hors champ et écart. Séparer projet/application/sanction, sans attendre enforcement. Plan avec acteur, source et délai déclenché confirmé/hypothétique, cible interne distincte. Risk accepted n'efface pas l'obligation ; aucun organisme certifié depuis rapport, ni collecte globale inter-clients.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

Textes France/UE Légifrance/EUR-Lex et transitions, CNIL/CEPD et jurisprudence avec leur portée ; pratiques prouvées séparément.

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

- Cas normal : C01 : changement identifié à application différée et pratiques datées ; exigences/écarts/actions reliés et calendrier expliqué.
- Cas limite : C02 : consultation publique résumée ou pratique sans preuve ; pas d'obligation nouvelle ni already compliant, résultat conditionnel.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Veille, politique entièrement réécrite, corrections exécutées, notification et audit général.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
