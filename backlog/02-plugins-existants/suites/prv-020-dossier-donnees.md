---
id: PRV-020
titre: "Isoler et archiver un dossier de protection des données"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-020 — Isoler et archiver un dossier de protection des données

## Objectif et résultat attendu

Un organisme multi-dossiers ou praticien ouvre/sélectionne/liste/archive un contexte sans exposer les données d'un autre dossier.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.

- `privacy-legal/skills/matter-workspace/SKILL.md`
- `privacy-legal/CLAUDE.md (dossier actif et journal)`
- `privacy-legal/references/dossier-donnees.md (à créer)`

Documentation et métadonnées limitées à la tranche livrée ; si le manifeste
change, synchroniser le marketplace. Consigner le lot dans NOTICE local et
racine ; conserver identiques les copies communes BASE-005/008.

## Entrées nécessaires

Id pseudonyme, type demande/traitement/contrat, acteurs utiles, accès, conservation à confirmer, pointeur/historique.

## Travail attendu

Adapter new/list/switch/close/none au helper et privacy ; modèle sans MSA/Delaware ni nom dans slug. Liste minimale, archives distinctes, collision refusée. Pas de désactivation in-house ; cross-matter on ne vaut pas lecture globale sans demande. Journaux/notes/outputs isolés et digest d'édition, pas de journal nominatif partagé par défaut. Archivage n'atteste ni effacement ni conservation justifiée ; détacher actif et vérifier état archivé.

Charger `privacy-legal/references/shared/research-citation-method.md` depuis
le paquet installé. Appliquer le [contrat commun](../exist-003-decoupage-donnees.md)
et les [dépendances inventoriées](../exist-003-inventaire-donnees.md).
Corriger les seuls blocs setup/routage de cette tâche ; PRV-019/020/021 ne
sont pas des préalables universels. Sans profil ni connecteur, une pièce
fournie permet une sortie ponctuelle utile ; réserver les seules conclusions
sans faits ou sources suffisants. Les accès durables utilisent le helper.

## Sources à rechercher

BASE-008/005, RGPD/LIL minimisation/sécurité/conservation et règles de secret/secteur réellement pertinentes.

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

- Cas normal : P03 : deux demandes pseudonymes du même organisme ; changement sans lecture croisée, archivage garde preuve et détache actif.
- Cas limite : P04 : slug archivé, chemin traversant/lien et journal global nominatif ; refus helper sans normalisation silencieuse ni fuite.
- Sans pièce/source déterminante : sortie partielle utile, réserve explicite,
  aucun modèle ou délai américain de remplacement.

Scénarios attendus, non exécutés par EXIST-003. Dans le futur lot, conserver
sorties et ressources lues et suivre BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension. La
[relecture de cadrage](../exist-003-verification.md) ne remplace pas cette recette.

## Hors périmètre

Purge, politique générale de conservation, conflits d'intérêts et lecture voisine sans demande.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-003, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecture indépendante restent consignées.
Cette suite attend la sélection explicite d'une tranche ; aucune commande
France/UE supplémentaire n'est annoncée comme déjà disponible.
