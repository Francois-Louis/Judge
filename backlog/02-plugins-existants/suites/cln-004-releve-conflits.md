---
id: CLN-004
titre: "Préparer un relevé pour contrôle de conflits"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-001]
---

# CLN-004 — Préparer un relevé pour contrôle de conflits

## Objectif et résultat attendu

Un relevé minimal donne parties/qualités, périmètre autorisé, vérifications réalisées et décision humaine de conflits encore attendue ou documentée.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/client-intake/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/CLAUDE.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/releve-conflits.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Cadre/processus CLN-001, identités strictement utiles, parties liées pertinentes, périmètre de registre autorisé et source de décision éventuelle.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Distinguer indicateur, recherche tentée, absence de résultat, contrôle non fait et décision attribuée. Pas accès à tout dossier ou rapprochement interclient depuis simple nom ; minimisation et visibilité aux personnes autorisées. Présence dans registre ou rien trouvé ne signifie pas cleared. Conserver homonymie et conflit potentiel, ne pas décider représenter/refuser sans décideur compétent ; aucun envoi à partie adverse.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Processus réel de structure, règles professionnelles selon activités/qualités, données et accès ; aucune règle ABA importée.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Une décision clear exige auteur/qualité/périmètre/date et preuve déclarée ; sinon statut non vérifié, jamais contrôle certifié par outil.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : CF01 — Deux parties nommées et procédure de contrôle locale : relevé séparant demande de vérification et décision reçue.
- Cas limite : CF02 — Homonymie ou base inaccessible : incertitude visible, pas exploration de dossiers non autorisés ou clearance par défaut.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Moteur de conflits global, décision professionnelle et admission.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

