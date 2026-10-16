---
id: CLN-007
titre: "Préparer un support d’analyse pour l’étudiant"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-005]
---

# CLN-007 — Préparer un support d’analyse pour l’étudiant

## Objectif et résultat attendu

Un support pédagogique attribue question/faits/sources et laisse identifiés raisonnement et conclusion à produire ou relire.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/memo/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/support-analyse-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Question, corpus/plan CLN-005/006 ou équivalent, cadre/guide/posture explicites, notes de l’étudiant et objectif de revue.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Harmoniser règle assist/guide/teach avec champs canoniques du guide sans effacer responsabilité de l’étudiant. Ne pas inventer analyse/conclusion de l’étudiant, ni passer modèle généré pour son texte après deux essais. IRAC option pédagogique, pas méthode française imposée. Toute règle substantielle vient de source lue et domaine ; inconnu reste recherche nécessaire. Garder faits contraires et questions au référent, retirer repair-and-deduct et conclusion toute faite.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Méthode de sources, guide réel et textes/corpus du point borné ; pas obligation ABA ou droit de fond déduit de modèle.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Le support attribue ce que fait outil/étudiant et ne signe pas son raisonnement ; incertitudes et sources restent visibles au référent.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : ME01 — Étudiant apporte question et notes : trame avec faits/preuves et prompts d’analyse, conclusion attribuée seulement si fournie.
- Cas limite : ME02 — Demande de memo final au nom de l’étudiant sans recherches : support/réserves, pas analyse académique ou avis juridique inventés.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Avis final, notation automatique et substitution au référent de matière.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

