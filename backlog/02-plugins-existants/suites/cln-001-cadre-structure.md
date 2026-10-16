---
id: CLN-001
titre: "Documenter le cadre réel d’une clinique"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006]
---

# CLN-001 — Documenter le cadre réel d’une clinique

## Objectif et résultat attendu

Une fiche de structure distingue activité déclarée, rôles, limites, supervision et points à vérifier avant usage sur dossiers réels.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/cold-start-interview/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/CLAUDE.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/cadre-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Statut/activité de structure, règles/convention/charte, responsables et qualités déclarées, territoires, public, types d’actes, outils/données et destinataires.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Remplacer professeur avocat/étudiant habilité présumés par rôles réels : accueil, information, analyse, rédaction, validation pédagogique, validation professionnelle et représentation distincts. Rechercher cadre de l’activité et habilitations sans les déduire du nom clinique. Documenter traitement de données, information des personnes, accès, prestataires/rétention et points non résolus ; consentement IA n’est pas réponse universelle. Retirer ABA/Model Rules comme socle France et choix lighter-touch comme dispense juridique. Entretien neuf BASE-008, exercice fictif possible sans dossier réel.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Règles/conventions de structure et établissement, encadrement français de consultation/rédaction/qualités selon activité, règles professionnelles si applicables, RGPD/droit national et documentation contractuelle des outils.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Aucun titre de professeur ou choix pédagogique ne certifie habilitation, secret, mandat ou conformité données ; inconnues identifiées avant dossier réel.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : C01 — Association universitaire fait accueil avec référent identifié : fiche rôles/actes/validation/données et questions de preuve, sans consultation autorisée présumée.
- Cas limite : C02 — Responsable non avocat et règles/outils inconnus : fiche conditionnelle et exercice fictif, pas import ABA ou habilitation automatique.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Certification juridique de structure, installation de compte et traitement automatique des vrais dossiers.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

