---
id: COM-019
titre: "Lire une demande de paiement présentée comme une obligation administrative"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-001, PILOTE-003, BASE-005, BASE-006]
---

# COM-019 — Lire une demande de paiement présentée comme une obligation administrative

## Objectif et résultat attendu

Fiche des éléments observés, obligation et commande à vérifier, méthode de contrôle indépendante, pièces à préserver et brouillon ciblé de demande de preuve ou de contestation.

Issue des [frictions sur les formalités d'entreprise](../exist-002-annexes/exist-002-frictions-utilisateurs.md), points 1–7, 9–10, 60, 77, 99–100. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : commercial-legal. Nouveau skill proposé `commercial-legal/skills/suspicious-payment-request/SKILL.md`, référence locale `demandes-administratives-trompeuses.md` ; examiner routage de `review` et README. Aucune promesse de cette tâche livrée par COM-001.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

Courrier complet et enveloppe ou message original, émetteur, SIREN allégué, facture/décompte, contrat ou formulaire signé, CGV, dates, paiements éventuels, effectif et activité du destinataire, façon dont le contact a été établi.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Séparer facture privée, frais publics, offre commerciale, relance, mise en demeure, décision et acte exécutoire. Ne pas qualifier définitivement une fraude sur un logo, un prix ou un SIREN connu. Vérifier émetteur et prestation alléguée sans suivre lien/RIB reçu ; comparer à l'obligation réelle dans son domaine. Faux annuaire, plateforme ou contrôle : documenter l'imitation et orienter vérification ou signalement éventuel, sans obstruction ni envoi. Examiner les conditions particulières de protection du petit professionnel sans généraliser la rétractation. Un paiement déjà effectué appelle une question bancaire distincte ; acte d'exécution → DOM-003, infraction alléguée → DOM-002.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code civil, Code de commerce et Code de la consommation selon champ B2B/hors établissement ; DGCCRF et décisions officielles ; textes et portails de l'obligation prétendue chez son propriétaire.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : Micro-entrepreneur recevant un formulaire d'annuaire avec prix en petits caractères puis relance : extraire commande alléguée, durée et somme, préparer une demande de preuve circonstanciée.
- Cas limite : Courrier mélangeant des frais officiels possibles et des honoraires privés, ou vrai contrôle insuffisamment identifié : statut réservé et voie de vérification indépendante ; aucune consigne d'ignorer l'acte.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Constat définitif d'escroquerie, injonction de ne pas payer un acte authentique, envoi de signalement, recours judiciaire, remboursement bancaire ou audit de toute conformité.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../exist-002-annexes/exist-002-frictions-verification.md).

## Complément de besoins — 16 octobre 2026

Le point 140 et les encadrés REP de la [matrice marketing](../exist-004-annexes/exist-004-frictions-utilisateurs.md) couvrent aussi les demandes de renouvellement de nom de domaine/référencement ou d’accompagnement REP présentées comme obligatoires. Vérifier émetteur, service réellement souscrit et canal officiel connu ; ne pas confondre offre privée et échéance du registre ou de la filière. Recette attendue : courrier menaçant la visibilité d’un artisan → éléments à vérifier et écrit ciblé, sans déclarer fraude ou absence d’obligation depuis l’apparence seule.

Ces exigences et scénarios restent proposés, sans règle ou résultat métier validé par cette intégration.
