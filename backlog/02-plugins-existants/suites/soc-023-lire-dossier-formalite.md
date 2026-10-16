---
id: SOC-023
titre: "Lire le stade et les blocages d'un dossier de formalité de société"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-023 — Lire le stade et les blocages d'un dossier de formalité de société

## Objectif et résultat attendu

Chronologie des états prouvés, distinction dépôt/signature/paiement/régularisation/validation/rejet, pièces manquantes, auteur de chaque message et brouillon de demande au bon interlocuteur.

Issue des [frictions sur les formalités d'entreprise](../exist-002-annexes/exist-002-frictions-utilisateurs.md), points 11–13, 18, 20–21, 32, 96–97. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : corporate-legal. `corporate-legal/skills/entity-compliance/SKILL.md` : branche de lecture ponctuelle à borner ; `corporate-legal/references/lecture-dossier-formalite.md` à créer. Examiner README et routage concernés.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

Société et forme exacte (SAS/SASU ou SARL/EURL pour la première tranche), SIREN s'il existe, événement déclaré, numéro du dossier, portail, mandataire, captures datées, demande de pièces ou rejet intégral, reçus et preuves de réception.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Lire un dossier fourni sans initialiser de registre. Distinguer opérateur du portail, autorité de validation et mandataire. Vérifier le document d'immatriculation demandé, son accès officiel et ses frais. Pour les bénéficiaires effectifs ou l'adresse publiée, repérer l'état documentaire et préparer la question spécifique ; ne pas certifier contrôle ou occultation. Un rejet ne prouve ni qu'une simple correction suffit ni qu'un nouveau dépôt est toujours requis. Une panne conserve captures, ticket et historique ; son effet sur une échéance doit être recherché séparément.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code de commerce et textes d'application propres à la forme et à la formalité ; documents officiels INPI, registres et autorité de validation ; règles de notification et de recours propres à l'acte.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : SASU : reçu de paiement, demande de pièce puis rejet. Restituer les trois états, la pièce demandée et l'auteur du rejet, sans annoncer l'immatriculation.
- Cas limite : Mandataire indiquant « terminé » alors que la seule preuve est une capture sans date ; état réservé et pièces concrètes à obtenir. EI orientée vers DOM-039.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Dépôt effectif, rédaction des statuts, recours contentieux au fond, formalités de toutes formes, création d'EI et validation juridique de bénéficiaires effectifs.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../exist-002-annexes/exist-002-frictions-verification.md).
