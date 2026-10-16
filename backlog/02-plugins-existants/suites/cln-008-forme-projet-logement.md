---
id: CLN-008
titre: "Mettre en forme un projet logement déjà instruit"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-003]
---

# CLN-008 — Mettre en forme un projet logement déjà instruit

## Objectif et résultat attendu

Un projet de courrier au bailleur met en forme un contenu de fond fourni et relu par référent identifié, sans nouvelle analyse logement.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/draft/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/skills/form-generation/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/forme-projet-supervise.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Contenu sectoriel validé ou réserves explicites, dossier/pièces, auteur/qualité, bailleur/destinataire, cadre/guide, objectif et version à soumettre.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Borner un courrier logement, consommer contenu métier manuel ou de domaine sans exiger plugin installé. Préserver limites et points non validés, sources/pièces et voix de l’auteur, pas ajout de délai/menace/recours depuis généralités. Aucun formulaire d’éviction, I-589 ou FDCPA traduit. Alias form-generation reste redirect non invocable vers seule portée adaptée. Document versionné soumis à revue, pas court-ready, signé, envoyé ou déposé.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Contenu sectoriel et pièces effectivement fournis, règles de structure/auteur/diffusion ; droit de fond à rechercher par domaine/référent avant conclusion.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Chaque phrase substantielle renvoie au contenu fourni ou reste réservée ; aucun nouveau droit/délai introduit et aucun acte conforme prétendu.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : DR01 — Référent fournit analyse logement et demande bornée au bailleur : mise en forme avec pièces et points de revue.
- Cas limite : DR02 — Modèle français/contenu de fond absent ou étudiant demande assignation : plan/questions et relais, pas rédaction depuis modèle US ou généralités.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Analyse logement nouvelle, actes judiciaires, signature et envoi.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

