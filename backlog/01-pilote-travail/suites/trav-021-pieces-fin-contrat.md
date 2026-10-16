---
id: TRAV-021
titre: "Rapprocher les pièces administratives d'une fin de contrat de travail"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-021 — Rapprocher les pièces administratives d'une fin de contrat de travail

## Objectif et résultat attendu

Tableau des documents présents, incohérents et manquants, dates et sommes recopiées avec leur provenance, puis brouillon de demande ciblé.

Issue des [frictions sur les formalités d'entreprise](../../02-plugins-existants/exist-002-annexes/exist-002-frictions-utilisateurs.md), points 78. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : employment-legal. Nouveau skill proposé `employment-legal/skills/end-of-contract-documents/SKILL.md` et référence locale `pieces-fin-contrat.md` ; orientation depuis `termination-review` sans appel à ses branches non adaptées.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

Employeur/salarié et demandeur, contrat et avenants utiles, acte de rupture fourni, date de fin alléguée, préavis, bulletins/solde, certificat, attestation et signalements fournis, dates de remise et accusés.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Lire les suites documentaires d'une seule fin de contrat sans en valider la cause ni l'indemnisation. Distinguer production, remise au salarié et signalement déclaratif ; une attestation ne prouve pas l'ensemble accompli. Repérer contradictions de dates ou de montants sans moteur de paie. Le motif de rupture relève de TRAV-004/005 ou d'une tranche encore à découper, la DSN de TRAV-020. Ne pas demander au salarié de signer un document pour obtenir la lecture.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code du travail et textes de remise des documents, attestation et signalements ; sources officielles France Travail/DSN selon champ, version et type de rupture.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : Salarié ayant reçu un solde et un certificat, sans attestation : liste des pièces et demande de remise, sans conclusion sur le montant dû.
- Cas limite : Date de fin divergente entre lettre, bulletin et attestation : contradiction préservée, calcul et délai réservés ; rupture contestée orientée séparément.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Calcul de paie/indemnités, validation du licenciement, signature ou transmission des documents, dépôt déclaratif et contentieux.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../../02-plugins-existants/exist-002-annexes/exist-002-frictions-verification.md).

## Complément des frictions travail — 16 octobre 2026

**Pièces et reçu de fin de contrat.** Point 10.16 et catégorie finale de la checklist : ajouter, selon situation, informations d’épargne salariale et preuve de remise aux documents déjà prévus. Distinguer document établi, transmis et effectivement reçu ; aucune signature exigée pour l’analyse. Cas ajouté : attestation France Travail reçue mais incohérente avec la date de fin, informations d’épargne absentes : demande ciblée sans droit à prestation conclu. TRAV-051 garde montant d’une indemnité et portée du reçu, TRAV-053 créance/AGS ; TRAV-021 ne devient ni moteur de solde ni validation du motif.

Rattachement complet : [matrice des frictions](../pilote-001-annexes/pilote-001-frictions-utilisateurs.md).
Les critères restent non cochés. Pour ces ajouts, appliquer BASE-013 : phrase
finale nommant le professionnel compétent et renfort en tête si urgence ou
procédure ; sources, paquet détaché, client et compréhension à vérifier selon
BASE-005/006. Portée de l’intégration et lectures préliminaires :
[vérification](../pilote-001-annexes/pilote-001-frictions-verification.md).

## Complément des frictions allocations et aides sociales — 16 octobre 2026

Points 2–4 de la [matrice](../../03-nouveaux-domaines/dom-012-annexes/dom-012-frictions-utilisateurs.md).
Prévoir rapprochement attestation France Travail, contrat/rupture et bulletins,
avec dates de remise/transmission, salaires et motif ; brouillon de correction
ou relance employeur. Ouvrir les textes propres à l'attestation et à sa
transmission lors de l'implémentation. FT01/02 chez DOM-012 gardent admission
et calcul ARE, sans les déduire de la seule attestation.
Cas attendu : motif de démission sur attestation contredit par lettre de
rupture ; qualifier contradiction sans corriger soi-même le motif ni garantir
les droits. Scénario non exécuté ;
[portée](../../03-nouveaux-domaines/dom-012-annexes/dom-012-frictions-verification.md).
