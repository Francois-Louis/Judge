---
id: TRAV-019
titre: "Préparer les pièces d'une première embauche par une TPE française"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006]
---

# TRAV-019 — Préparer les pièces d'une première embauche par une TPE française

## Objectif et résultat attendu

Liste courte de pièces et démarches liées à une seule embauche, responsable/destinataire, état prouvé et échéance établie ou à vérifier ; absence d'action externe clairement indiquée.

Issue des [frictions sur les formalités d'entreprise](../../02-plugins-existants/exist-002-frictions-utilisateurs.md), points 71–73, 76–77. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : employment-legal. Nouveau skill proposé `employment-legal/skills/first-hire-checklist/SKILL.md` et référence locale `premiere-embauche-tpe.md` ; orientation et README concernés. TRAV-014/015 gardent le parcours d'employeur étranger.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

Employeur français identifié, activité, lieux, effectif, salarié et qualité du demandeur, poste/risques, contrat, début prévu ou passé, convention collective à vérifier, reçus DPAE, registre, DUERP et pièces de santé au travail disponibles.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Distinguer déclaration préalable, registre du personnel, évaluation des risques, adhésion et suivi de santé au travail, information/affichages. Ne pas assimiler DPAE aux autres obligations accomplies. La liste vérifie existence et pièces ; elle ne tient pas la paie ni ne réalise toute l'évaluation des risques. Affichage et information par autre moyen restent à rechercher selon effectif/poste ; aucun achat de kit imposé. Si prise de poste passée sans preuve, préparer les questions de régularisation sans antidater. Faux vendeur → COM-019.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code du travail, sécurité sociale et textes d'application ; Urssaf, ministère du Travail et sources officielles de prévention ; convention collective et régime du poste dans leur champ/version.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : Artisan recrutant un premier salarié : reçu DPAE fourni, registre et DUERP absents. Produire les lacunes par obligation, sans marquer l'embauche globalement conforme.
- Cas limite : Prise de poste déjà intervenue ou poste à risque mal décrit : dates et risque visibles, recherche ciblée/régularisation à préparer ; employeur étranger orienté vers TRAV-014.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Embauche ou dépôt effectif, paie/DSN, rédaction complète du contrat, diagnostic de risques universel et adaptation de tous employeurs.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../../02-plugins-existants/exist-002-frictions-verification.md).
