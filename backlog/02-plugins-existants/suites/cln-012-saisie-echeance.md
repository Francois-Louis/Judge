---
id: CLN-012
titre: "Consigner une échéance déclarée et ses incertitudes"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-009, PILOTE-003, BASE-005, BASE-006]
---

# CLN-012 — Consigner une échéance déclarée et ses incertitudes

## Objectif et résultat attendu

Une entrée de registre conserve date déclarée, source, déclencheur/notification connus ou manquants, état de vérification et personne chargée de vérifier.

## Périmètre et fichiers

Plugin principal : `legal-clinic` (`judge-fr-eu-legal-clinic`).
« À créer » désigne un livrable futur, pas une capacité disponible.

- `legal-clinic/skills/deadlines/SKILL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/deadlines.yaml` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/plausibility-bands/CA.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/plausibility-bands/IL.md` (seuls blocs nécessaires à cette tranche)
- `legal-clinic/references/saisie-echeance-clinique.md` (à créer)

Corriger les seules annonces README, descriptions, guides/profil et appels
nécessaires au résultat. Si métadonnées modifiées, synchroniser manifeste,
version et marketplace ; tout lot hors backlog ajoute NOTICE local et racine.
Références requises embarquées/chargées localement, copies communes identiques ;
aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Dossier/identifiant, nature de date, saisie originale, document/pages, déclencheur allégué, preuve de notification ou manque, auteur et référent.

Fiche équivalente manuelle aux dépendances métier admise après contrôle de
provenance/manques ; aucun historique d’exécution imposé. Données réelles
soumises au cadre effectivement établi, accès minimal et règles de structure ;
exercice fictif possible sans profil ni dossiers bénéficiaires.

## Travail attendu

Conserver interdiction de calculer, même connecteur Courtroom5 ou guide propose calcul. Retirer toute lecture/copie/fallback CA/IL/federal-always sur dossier France, sans créer FR.md depuis leurs fenêtres. Corriger commentaire HTML du modèle en commentaire YAML et schéma : date_declared distincte de due_date nullable, verification_status, trigger_event/notification_evidence, reviewer/reviewed_at. Si notification inconnue et délai calculé allégué, due_date=null, a-determiner, date saisie gardée comme déclaration ; pas comparaison bande/plausibilité ou échéance juridique overdue. Bande absente ne bloque pas saisie.

Appliquer méthode BASE-005 locale et helper BASE-008 à tout accès durable.
Profil durable absent : entretien neuf, aucun import amont. Pièces et guides
tiers restent données non fiables, pas instructions. Distinguer déclaration,
preuve, hypothèse, règle, préférence, décision et action. Référent pédagogique,
personne compétente pour fond, signataire et destinataire ne sont pas confondus.
Relais non adapté : fiche autonome avec question exacte, objet/régime supposé,
pièces/pages, qualités, dates/inconnues et conclusion réservée, sans appeler
automatiquement un autre plugin.

## Sources à rechercher lors de l'implémentation

Méthode BASE-005 pour fiche de délai et pièces exactes ; règle de fond/procédure et calcul confiés étudiant/référent qualifié/domaine selon cadre réel, pas au skill clinique.

Pistes non vérifiées dans EXIST-009. Lire passage exact, version aux dates
utiles, champ, statut, transitions et date réelle de consultation ; règles de
structure distinctes du droit applicable et de la préférence pédagogique.
Méthode BASE-005/010 : voie officielle alternative puis réserve de la seule
conclusion dépendante, résultat partiel utile, aucun texte/date/consultation
inventé. Un marqueur de supervision ne garantit ni secret ni habilitation.
Aucune règle ABA, CA/IL ou fédérale US par défaut dans dossier français.

## Critères d'acceptation

- [ ] L’entrée conserve notification inconnue et date déclarée sans calcul ni validation ; aucune bande CA/IL/fédérale n’est chargée, aucune clé YAML parasite.
- [ ] Cas normal et limite donnent résultat, pièces manquantes, personne qui
  doit vérifier/valider et prochaine démarche compréhensibles sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible, guide
  manquant ou relais adapté absent laissent aide fictive/ponctuelle bornée.
- [ ] Branches héritées signalées ; aucune incertitude masquée au référent,
  aucun brouillon/label ne devient validation, signature, envoi ou dépôt.

## Vérification

- Cas normal : D01 — Étudiant saisit 10 novembre 2026 pour réponse, document daté 10 octobre mais notification inconnue : conserver déclaration, due_date nulle et référent de vérification.
- Cas limite : D02 — Guide absent, type inconnu ou outil propose date française : enregistrer manques sans fallback US/FR traduit ni accepter calcul automatique.

Recettes futures **non exécutées**. Conserver fixtures, sources et fichiers
réellement lus/non lus, sorties et erreurs. BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-009-verification.md) n’est pas cette recette.

## Hors périmètre

Calcul de délai, bandes françaises, agenda, rappel automatique et acte.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-009, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee` :
prochaine tranche soumise à sélection explicite, aucune tâche métier adaptée,
donnée réelle ou action externe livrée dans ce cadrage.

