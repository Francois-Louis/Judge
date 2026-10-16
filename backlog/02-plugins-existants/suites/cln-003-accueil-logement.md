---
id: CLN-003
titre: "Préparer un accueil logement sans analyse de fond"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006, CLN-002]
---

# CLN-003 — Préparer un accueil logement sans analyse de fond

## Objectif et résultat attendu

Une fiche logement organise récit, qualité d’occupant, acte reçu, pièces et questions au référent avec urgences non résolues.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/client-intake/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/accueil-logement.md` (à créer)
- `legal-clinic/skills/client-intake/references/intake-templates/housing-fr.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Récit, type/lieu logement et qualité déclarés, bail/échanges/acte disponibles, dates littérales et réception connue, objectif et canal de contact sûr.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Borner collecte factuelle logement France. Demander acte complet et différencier bailleur/locataire/occupant/structure, dépôt/charges/travaux et procédure/acte d’exécution allégué. Pas UD/CCP/repair-and-deduct, délai d’expulsion de mémoire ou conseil de suspendre paiement. Préparer relais logement DOM-006 ; acte d’exécution → DOM-003 distinct ; sécurité/violence seulement faits utiles/canal adapté sans dossier partagé automatiquement. Date inconnue reste urgence de vérification, pas pas d’urgence.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Règles d’accueil et données de structure ; textes/logement/procédure selon acte à rechercher par domaine compétent, pas par modèle américain.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] Résumé et urgence sont motivés par faits/manques ; aucune référence CA/IL/fédérale ou procédure française déduite du seul mot expulsion.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : L01 — Locataire parle réparations et courrier bailleur sans réception prouvée : fiche faits/pièces/acte à lire, référent et date à déterminer.
- Cas limite : L02 — Photo incomplète d’acte commissaire ou récit de violence : pas délai calculé ni banalisation, canal et référent à identifier avec minimum de données.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Conseil de fond logement, acte judiciaire, expulsion exécutée et décision de protection.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

