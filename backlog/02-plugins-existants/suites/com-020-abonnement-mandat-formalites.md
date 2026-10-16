---
id: COM-020
titre: "Expliquer un abonnement ou mandat lié aux formalités d'entreprise"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006]
---

# COM-020 — Expliquer un abonnement ou mandat lié aux formalités d'entreprise

## Objectif et résultat attendu

Tableau prestations/coûts/durée/reconduction, portée des pouvoirs, conditions de sortie établies ou réservées, pièces et brouillon de questions ou demande ciblée.

Issue des [frictions sur les formalités d'entreprise](../exist-002-annexes/exist-002-frictions-utilisateurs.md), points 4, 8, 19, 32, 60, 100. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : commercial-legal. `commercial-legal/skills/vendor-agreement-review/SKILL.md` : branche de lecture bornée ; référence locale `prestataire-formalites.md` à créer ; raccord au routage sans imposer une revue SaaS.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

Devis, commande, CGV/version acceptée, facture et prélèvements, mandat, conditions de domiciliation ou d'assistance, dates et mode de conclusion, effectif, activité principale, identités et accès détenus par le prestataire.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Séparer formalité ponctuelle, domiciliation, assistance et abonnement. Tracer consentement et dépendances pratiques (adresse, documents, accès) avant la fin du contrat. Vérifier la possibilité de résiliation, non-renouvellement, révocation du mandat et éventuelle rétractation comme questions distinctes. Un contrat à distance B2B ne donne aucune conclusion automatique ; demander lieu/mode de conclusion, effectif, objet, activité principale et exceptions. Demander restitution des pièces et état des dépôts sans révoquer ni modifier des accès. SOC-023/DOM-039 vérifient le dossier réel.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code civil, Code de commerce ; Code de la consommation pour protections interprofessionnelles selon champ ; textes de domiciliation et mandat ; jurisprudence officielle et contrat/version signée.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : Création facturée une fois puis assistance prélevée mensuellement : identifier preuve d'adhésion, durée et prochain événement contractuel avec ses inconnues.
- Cas limite : Mandataire seul détenteur du dossier et adresse de domiciliation utilisée par l'entreprise : exposer pièces et conséquences à vérifier avant toute sortie ; aucune révocation effectuée.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Résiliation ou envoi effectif, changement d'adresse ou d'accès, audit de formalités, comparaison commerciale de prestataires et promesse de remboursement.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../exist-002-annexes/exist-002-frictions-verification.md).
