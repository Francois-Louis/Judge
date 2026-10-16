---
id: PRV-031
titre: "Préparer une demande relative à une décision présentée comme automatisée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-031 — Préparer une demande relative à une décision présentée comme automatisée

## Objectif et résultat attendu

Une personne ou son aidant obtient la fiche et le brouillon propres à cette tâche, en langage clair. Les points **25, 41** de la [matrice des frictions](../exist-003-frictions-utilisateurs.md) motivent ce résultat.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`). Parcours du demandeur, distinct de la réponse organisme PRV-002 à PRV-008.

- `privacy-legal/skills/automated-decision-request/SKILL.md` : nouveau parcours proposé, à créer.
- `privacy-legal/references/decision-automatisee.md` : référence ciblée à créer par cette tranche.
- `privacy-legal/README.md` et seuls blocs de routage concernés de `privacy-legal/CLAUDE.md` ; examiner les liens avec `access-request` sans exécution préalable obligatoire.

Appliquer le [contrat commun](../exist-003-decoupage-donnees.md) : méthode BASE-005 locale, paquet autonome BASE-006, isolation BASE-008 et préférences facultatives. PRV-019/020 ne sont pas des préalables. Synchroniser les éventuelles métadonnées au marketplace et documenter seulement la tranche livrée dans README et NOTICE racine/local.

## Entrées nécessaires

Décision, score connu, effets, notification/date et rôle humain réel ou inconnu.

## Travail attendu

Fiche profilage/décision/intervention humaine et brouillon demandant données, informations pertinentes et intervention humaine si applicable ; rechercher champ, exceptions et garanties. Relais DOM-004 pour la contestation du refus de crédit, encore à découper, avec calendrier propre. BNK-005 lit une offre ; BNK-006 traite un prélèvement : ces stories ne couvrent pas ce refus.

Accepter des pièces manuelles et une lecture ponctuelle sans profil professionnel ni connecteur. Séparer fait, preuve, hypothèse, droit et action proposée. Aucun code, mot de passe ni justificatif d'identité systématique ; minimiser les données des tiers. Les relais transmettent les seules pièces nécessaires sans dépendance d'installation. Chaque calendrier précise source/version, champ, événement déclencheur, date prouvée et inconnues ; le tableau utilisateur ne fixe aucune échéance par défaut.

## Sources à rechercher

RGPD et loi Informatique et Libertés, CNIL/CEPD et jurisprudence CJUE/française sur le droit ou le traitement retenu. Cibler décision automatisée, information intelligible et textes sectoriels du crédit ou des décisions publiques.

Lire les passages exacts, version et champ à la date des faits avec les voies officielles BASE-010 si nécessaire. Distinguer texte, décision et recommandation. Le texte utilisateur ne vaut pas vérification ; réserver les seules conclusions sans faits ou sources suffisants.

## Complément des frictions IA

Points 1–6, 19, 23 et 48 de la [matrice IA](../exist-005-frictions-utilisateurs.md) : relever le rôle réel du score et de la personne, son pouvoir de modifier le résultat, les éléments effectivement examinés et la réponse motivée reçue. Un clic de validation ou l'étiquette « recommandation » ne décide pas de la qualification. Demander données/inférences, provenance et information intelligible ; rechercher les garanties et exceptions sans promettre code source ni intervention humaine universels. Secret des affaires invoqué : préparer une demande ciblée et contrôler la réponse plutôt que conclure à un refus toujours justifié ou toujours illégal. Ajouter un cas de support en boucle automatique : tickets conservés, relance et calendrier sectoriel séparés. IA-021 garde l'orientation globale ; DOM-010 garde la demande d'informations algorithmiques administratives à découper.

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

- Cas normal : Refus de crédit opaque : demande ciblée et qualification conditionnelle.
- Cas limite : Score examiné par agent au rôle imprécis : questions sur intervention réelle sans réexamen universel ni code source promis.
- Pièce ou source déterminante manquante : sortie partielle utile, questions et interlocuteur sans règle étrangère de remplacement.

Recette attendue lors de l'implémentation selon BASE-006 : sorties conservées, paquet détaché, client, résultat métier et compréhension. Contrôles documentaires de cette intégration : [relevé des frictions](../exist-003-frictions-verification.md).

## Hors périmètre

Révision de score, crédit obtenu, audit d'algorithme et conformité complète au règlement IA. Aucun envoi ou démarche externe exécutés par cette proposition.

## État de la proposition — 16 octobre 2026

Ajout issu des 60 frictions ; statut `proposee`, sans sélection de tranche. Le préalable PILOTE-003 est satisfait ; ses limites restent consignées. Portée de l'intégration : voir le relevé lié ci-dessus.
