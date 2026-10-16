---
id: PRV-022
titre: "Préparer une demande de rectification de données"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-022 — Préparer une demande de rectification de données

## Objectif et résultat attendu

Une personne ou son aidant obtient la fiche et le brouillon propres à cette tâche, en langage clair. Les points **40, 42** de la [matrice des frictions](../exist-003-frictions-utilisateurs.md) motivent ce résultat.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`). Parcours du demandeur, distinct de la réponse organisme PRV-002 à PRV-008.

- `privacy-legal/skills/rectification-request/SKILL.md` : nouveau parcours proposé, à créer.
- `privacy-legal/references/demande-rectification.md` : référence ciblée à créer par cette tranche.
- `privacy-legal/README.md` et seuls blocs de routage concernés de `privacy-legal/CLAUDE.md` ; examiner les liens avec `access-request` sans exécution préalable obligatoire.

Appliquer le [contrat commun](../exist-003-decoupage-donnees.md) : méthode BASE-005 locale, paquet autonome BASE-006, isolation BASE-008 et préférences facultatives. PRV-019/020 ne sont pas des préalables. Synchroniser les éventuelles métadonnées au marketplace et documenter seulement la tranche livrée dans README et NOTICE racine/local.

## Entrées nécessaires

Donnée actuelle, correction souhaitée, justificatifs minimaux et décision affectée.

## Travail attendu

Tableau erreur/preuve/correction puis brouillon au responsable ; distinguer fait erroné et appréciation contestée, notification aux destinataires et procédure spéciale de fichier bancaire.

Accepter des pièces manuelles et une lecture ponctuelle sans profil professionnel ni connecteur. Séparer fait, preuve, hypothèse, droit et action proposée. Aucun code, mot de passe ni justificatif d'identité systématique ; minimiser les données des tiers. Les relais transmettent les seules pièces nécessaires sans dépendance d'installation. Chaque calendrier précise source/version, champ, événement déclencheur, date prouvée et inconnues ; le tableau utilisateur ne fixe aucune échéance par défaut.

## Sources à rechercher

RGPD et loi Informatique et Libertés, CNIL/CEPD et jurisprudence CJUE/française sur le droit ou le traitement retenu. Vérifier les procédures Banque de France pour un fichier spécial et le régime de la décision professionnelle.

Lire les passages exacts, version et champ à la date des faits avec les voies officielles BASE-010 si nécessaire. Distinguer texte, décision et recommandation. Le texte utilisateur ne vaut pas vérification ; réserver les seules conclusions sans faits ou sources suffisants.

## Complément des frictions IA

Point 4 de la [matrice IA](../exist-005-frictions-utilisateurs.md) : une donnée erronée peut alimenter plusieurs scores. Relever responsables et destinataires documentés, demander la rectification et, selon les conditions vérifiées, l'information des destinataires et les renseignements communicables sur ceux-ci. La correction demandée à un organisme ne prouve pas la correction des copies tierces. Cas attendu : données corrigées auprès d'un acteur mais refus persistant ailleurs ; demandes et preuves de suite distinctes, sans propagation annoncée comme acquise.

## Critères d'acceptation

- [ ] La fiche et le brouillon répondent à la tâche sur le cas normal ; le cas limite garde les inconnues et une prochaine démarche utile.
- [ ] Rôles du demandeur/organisme et démarches données/recours sectoriel sont distincts ; aucun autre délai de recours n'est réputé suspendu par la seule demande RGPD.
- [ ] Sources, versions, faits, réception et éventuelles échéances sont traçables.
- [ ] Une personne sans formation juridique identifie destinataire, pièces et prochaine action.
- [ ] Le paquet détaché charge ses références locales et respecte BASE-008 sans profil ni connecteur obligatoire.
- [ ] Aucune transmission, suppression, préservation ou intervention externe n'est annoncée comme effectuée sans preuve.
- [ ] Documentation, métadonnées et NOTICE reflètent seulement le résultat livré et ses limites.
- [ ] La sortie se termine par le rappel court BASE-013 avec professionnel compétent ; urgence de délai/procédure signalée en tête.

## Vérification

- Cas normal : Horaires RH inexacts : correction documentée et relais distinct pour la sanction.
- Cas limite : Appréciation de recrutement contestée : questions et désaccord conservés sans rectification automatique.
- Pièce ou source déterminante manquante : sortie partielle utile, questions et interlocuteur sans règle étrangère de remplacement.

Recette attendue lors de l'implémentation selon BASE-006 : sorties conservées, paquet détaché, client, résultat métier et compréhension. Contrôles documentaires de cette intégration : [relevé des frictions](../exist-003-frictions-verification.md).

## Hors périmètre

Modification des fichiers, radiation bancaire et annulation de sanction. Aucun envoi ou démarche externe exécutés par cette proposition.

## État de la proposition — 16 octobre 2026

Ajout issu des 60 frictions ; statut `proposee`, sans sélection de tranche. Le préalable PILOTE-003 est satisfait ; ses limites restent consignées. Portée de l'intégration : voir le relevé lié ci-dessus.
