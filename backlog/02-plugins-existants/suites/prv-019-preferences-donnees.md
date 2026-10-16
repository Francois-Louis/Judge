---
id: PRV-019
titre: "Créer ou ajuster des préférences privacy volontaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-019 — Créer ou ajuster des préférences privacy volontaires

## Objectif et résultat attendu

Particulier, association ou DPO peut enregistrer des préférences ou ajuster une section sans règles inventées ni lecture ponctuelle bloquée.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/cold-start-interview/SKILL.md`
- `privacy-legal/skills/customize/SKILL.md`
- `privacy-legal/CLAUDE.md (profil et garde-fous)`
- `privacy-legal/README.md (publics et neuf skills)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Réponses explicites, profil absent/partiel/existant, section visée, rendu/contacts optionnels ; seeds/connecteurs facultatifs.

## Travail attendu

Harmoniser quick/full/redo/pause/check-integrations et personnalisation, digest et réponses conservés via helper. Utilisateur distinct du rôle RGPD par traitement ; aucun GC/avocat/seed imposé. SLA souhaité, délai sourcé et risque séparés ; délai interne plus court pas interdit par principe. Résoudre stop/réponse ad hoc et web/provenance ; charger méthode locale. Revoir en-têtes/secret sur sources françaises, sans traduction attorney work product. Retirer registre ou notifications annoncés sans workflow. Ne changer aucune copie commune isolément, profil partagé compatible et faits confirmés seulement.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

BASE-005, RGPD/LIL pour rôles/obligations, textes/jurisprudence France/UE secret/confidentialité selon auteur/destinataire ; organisation sur réponses/pièces.

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

- Cas normal : P01 : association sans DPO déclaré, seed ou connecteur ; préférences partielles sauvegardées, lecture ponctuelle accessible.
- Cas limite : P02 : profil interrompu, SLA plus court et exemption générale demandée ; préserver réponses, préférence licite sans exception fabriquée.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Réécriture des workflows métier, import, refonte de templates communs et connexion non autorisée.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
