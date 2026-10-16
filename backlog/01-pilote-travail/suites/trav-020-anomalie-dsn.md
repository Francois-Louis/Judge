---
id: TRAV-020
titre: "Lire une anomalie ou notification de substitution DSN"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-020 — Lire une anomalie ou notification de substitution DSN

## Objectif et résultat attendu

Tableau des données concernées, chronologie, auteur/destinataire, motifs, pièces manquantes et brouillon de question au déclarant ou à l'organisme ; délai réservé tant que non vérifié.

Issue des [frictions sur les formalités d'entreprise](../../02-plugins-existants/exist-002-annexes/exist-002-frictions-utilisateurs.md), points 74–75, 91–93, 98 pour orientation employeur. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : employment-legal. Nouveau skill proposé `employment-legal/skills/dsn-notice-review/SKILL.md` et référence locale `notifications-dsn.md` ; branche d'orientation employeur. La contestation Urssaf au fond reste à découper.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

Employeur et qualité du demandeur, période, DSN déposée et reçu, compte rendu métier, anomalie ou notification complète, dates de mise à disposition/réception, déclarant (interne ou prestataire), données avant/après et demandes antérieures.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Distinguer accusé technique, compte rendu, demande de correction, notification de substitution et décision de recouvrement. Vérifier le mécanisme invoqué, sa version, les effets annoncés et la voie propre de réponse. Ne pas recalculer de paie ni corriger automatiquement une DSN. Les données de salariés non nécessaires sont masquées dans la synthèse. Contrainte : urgence et régime spécial à qualifier avec DOM-003 ; CRA, remise et médiation d'un employeur société sont des tâches sociales supplémentaires à découper, pas couvertes par cette lecture. Travail indépendant → DOM-039.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code de la sécurité sociale, textes DSN et substitution selon date d'effet ; documentation officielle Urssaf et déclarative, sans assimiler une spécification technique à une règle de recours.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : TPE recevant un compte rendu d'anomalie après dépôt : relier période, champ et déclarant puis demander les éléments correctifs, sans assimiler dépôt et acceptation.
- Cas limite : Substitution alléguée avec date de réception incertaine puis mise en demeure : distinguer les actes, réserver le délai et signaler la nécessité d'une qualification sociale distincte.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Moteur de paie, dépôt ou correction de DSN, chiffrage des cotisations, rédaction de CRA/opposition à contrainte et analyse complète d'un contrôle Urssaf.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../../02-plugins-existants/exist-002-annexes/exist-002-frictions-verification.md).
