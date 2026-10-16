---
id: CTX-031
titre: "Structurer les demandes d'un petit litige civil"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-006, PILOTE-003, BASE-005, BASE-006, BASE-013, CTX-026]
---

# CTX-031 — Structurer les demandes d'un petit litige civil

## Objectif et résultat attendu

Un tableau de demandes principales, accessoires et reconventionnelles d’un petit litige civil oral identifié, avec montants justifiés et questions de fond à résoudre.

Issue des [125 frictions contentieuses](../exist-006-frictions-utilisateurs.md), intégrées le 16 octobre 2026. Aucun skill adapté dans cette proposition.

## Périmètre et fichiers à examiner

Propriétaire : `litigation-legal` (`judge-fr-eu-litigation-legal`). Tâche utilisable par un particulier ou une TPE sans profil de cabinet. Cibles futures à créer après examen du routage existant :

- `litigation-legal/skills/tableau-demandes-civiles/SKILL.md` ;
- `litigation-legal/references/tableau-demandes-civiles.md` ;
- README, description et routage strictement nécessaires à cette tâche.

Embarquer et charger méthode locale BASE-005 et références métier ; respecter le stockage BASE-008 pour toute écriture durable. Aucun accès runtime au backlog ou à un plugin voisin ; une fiche manuelle équivalente satisfait le contrat d’entrée, sans imposer l’exécution de CTX-026. Si métadonnées modifiées, synchroniser version/manifeste/marketplace et NOTICE racine/local selon CLAUDE.md.

## Entrées nécessaires

Procédure et représentation qualifiées, prétentions de chaque partie, contrats et faits, pièces de dommage, paiements, décomptes, intérêts et frais demandés.

## Travail attendu

Pour chaque demande, distinguer ce qui est allégué, prouvé, chiffrable et encore à justifier ; citer le fondement lu ou signaler son absence. Détailler principal, préjudices sans double compte, intérêts, dépens et frais demandés. Recenser la demande reconventionnelle et les réponses manquantes. Le fond spécialisé conserve son propriétaire ; ce tableau ne remplace pas un acte de saisine ni des conclusions complètes.

Distinguer document cité, fait déclaré, règle effectivement lue et inconnue. Pour tout délai calculé : texte/version et champ, déclencheur prouvé, calcul détaillé, exceptions/transitions, résultat et réserves. À défaut, terme `a-determiner`, faits manquants et interlocuteur compétent. CTX-016 garde sa seule échéance de procédure TJ écrite ; ne pas lui attribuer toutes les prescriptions ou voies de recours.

## Sources à rechercher lors de l’implémentation

CPC, objet du litige, demandes initiales/incidentes et procédure orale retenue ; Code civil et textes sectoriels des préjudices ; dépens et frais non compris dans les dépens.

Pistes non vérifiées dans ce cadrage : ouvrir les textes et jurisprudences officiels, versions aux dates utiles, champ et transitions selon BASE-005/BASE-010. Si une source est inaccessible, chercher une voie officielle alternative puis réserver la seule conclusion dépendante.

## Critères d’acceptation

- [ ] La sortie produit le résultat borné ci-dessus avec pièces, hypothèses, inconnues et prochaine démarche compréhensibles sans formation juridique.
- [ ] Chaque conclusion juridique est rattachée à une source lue applicable ; aucune nullité, suspension, recevabilité ni issue favorable n’est présumée.
- [ ] Le cas normal et la limite ci-dessous donnent des résultats distincts ; une source ou une pièce manquante reste visible.
- [ ] Le paquet installé seul contient ses références ; absence de profil, de connecteur ou de plugin voisin laisse une aide ponctuelle utile.
- [ ] BASE-013 est appliquée : phrase finale nommant l’avocat compétent, renfort en tête si délai, procédure urgente ou enjeu irréversible.

## Vérification

- Cas normal : Acompte et dommage documentés : chaque montant a sa pièce et sa justification, les accessoires restent distincts.
- Cas limite : Demande adverse non lue et indemnité sans justificatif : montants réservés, aucune indemnisation inventée.

Recettes attendues **non exécutées**. Lors de l’implémentation, conserver fixtures, textes lus, sorties et écarts ; appliquer BASE-006 (paquet détaché, client, résultat métier et compréhension).

## Hors périmètre

Rédaction d’acte complet, évaluation médicale, calcul autonome des droits sectoriels. Aucun envoi, dépôt, signature ou représentation dans cette tranche.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée. Contrat commun et frontières : [découpage EXIST-006](../exist-006-decoupage-contentieux.md). Le bilan PILOTE-003 est terminé avec ses limites documentées. Contrôles de cette intégration : [relevé documentaire](../exist-006-frictions-verification.md).
