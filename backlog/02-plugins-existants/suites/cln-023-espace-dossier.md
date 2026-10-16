---
id: CLN-023
titre: "Isoler un espace minimal de dossier clinique"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006]
---

# CLN-023 — Isoler un espace minimal de dossier clinique

## Objectif et résultat attendu

Un espace minimal garde identifiant stable, métadonnées nécessaires et sorties isolées, en lien avec registres sans créer admission ou mandat.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/CLAUDE.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/client-comms/_README.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/handoffs/_README.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/espace-dossier-clinique.md` (à créer)
- `legal-clinic/skills/case-workspace/SKILL.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Identifiant pseudonyme choisi, action, accès/périmètre autorisé, cadre pour données réelles et références de pièces autorisées.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Créer tâche case-workspace bornée, pas système global ni Clio supposé. Identifiant commun intake/deadlines/comms/queue/handoff, pas nom/patronyme par défaut dans chemins. Garde racine/liens/collisions via helper, liste minimale et pas related=accès. Modèles en paquet lecture seule, état sous config. Archivage ne ferme droits ni détruit pièces et n’ouvre pas cohorte suivante ; données minimisées selon cadre.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

BASE-008 et règles réelles d’accès/données/conservation de structure ; aucune décision de fond depuis rangement.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Aucune collision, sortie de racine ou lecture croisée implicite ; identifiant ne crée ni dossier accepté ni mandat, modèles installés inchangés.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : ES01 — Dossier pseudonyme autorisé : pièces/sorties et registres reliés sans dupliquer identité civile.
- Cas limite : ES02 — Identifiant déjà présent, lien symbolique ou ancien dossier autre cohorte : refus propre, pas lecture/écrasement/accès élargi.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Système gestion complet, migration transverse, transfert de droits et effacement.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

