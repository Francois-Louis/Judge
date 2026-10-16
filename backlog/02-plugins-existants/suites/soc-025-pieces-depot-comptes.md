---
id: SOC-025
titre: "Rapprocher les pièces d'un dépôt de comptes et d'une demande de confidentialité"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-025 — Rapprocher les pièces d'un dépôt de comptes et d'une demande de confidentialité

## Objectif et résultat attendu

Tableau des pièces présentes/manquantes, dates établies, question d'approbation séparée du dépôt, éligibilité à la confidentialité à vérifier et prochaine démarche.

Issue des [frictions sur les formalités d'entreprise](../exist-002-frictions-utilisateurs.md), points 65–67. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : corporate-legal. `corporate-legal/skills/entity-compliance/SKILL.md` : branche de revue documentaire ; `corporate-legal/references/depot-comptes.md` à créer ; revoir les liens vers SOC-001/003/004 sans appel à un mode non adapté.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

SAS/SASU ou SARL/EURL, exercice et clôture, comptes fournis, décision d'approbation ou état de sa préparation, date/voie de dépôt, accusés, données de taille, appartenance à un groupe et catégorie invoquée pour la confidentialité.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Lire les pièces d'un seul exercice. Vérifier champ, pièces à déposer, délai et voie de dépôt, ainsi que critères/exclusions et portée de la confidentialité. Aucun délai déduit de la seule clôture. Une demande ou un accusé de dépôt ne prouve pas son acceptation. L'absence de rémunération du dirigeant n'établit pas l'absence d'obligation. SOC-001/003 restent propriétaires des décisions/PV, SOC-004/005/006 du suivi.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code de commerce et textes d'application sur comptes, approbation, publicité et confidentialité ; documentation officielle du registre et du Guichet unique, avec champ et date.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : SASU sans salaire du président : comptes et approbation fournis, dépôt non prouvé. Lister les justificatifs et vérifier la voie et le calendrier.
- Cas limite : SARL invoquant sa petite taille sans informations sur le groupe ni les exclusions : confidentialité réservée ; ne pas promettre l'occultation de tous les comptes.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Tenue ou certification comptable, approbation fictive, dépôt, calcul fiscal, adaptation de toutes formes sociales.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../exist-002-frictions-verification.md).
