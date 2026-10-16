---
id: IA-022
titre: "Examiner les pouvoirs délégués à un agent IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-022 — Examiner les pouvoirs délégués à un agent IA

## Objectif et résultat attendu

Une TPE, une association ou un indépendant obtient une matrice comparant tâche autorisée, permissions documentées et actions possibles d'un agent sur un outil déterminé. Point 38 de la [matrice des frictions](../exist-005-annexes/exist-005-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).

- `ai-governance-legal/skills/agent-authority-review/SKILL.md` : nouveau parcours proposé.
- `ai-governance-legal/references/pouvoirs-agent.md` : référence locale à créer.
- README et seuls blocs de routage concernés de CLAUDE.md ; examiner ai-policy et vendor-ai-review pour leurs contrats d'entrée.

Appliquer le [contrat commun IA](../exist-005-annexes/exist-005-decoupage-ia.md), BASE-005 locale, BASE-006 et BASE-008. Accepter pièces manuelles, sans profil, connexion ou inventaire préalable. Embarquer les références nécessaires, synchroniser les métadonnées modifiées et documenter la tranche dans les NOTICE racine/local lors de l'implémentation.

## Entrées nécessaires

Tâche voulue, outil/version, compte et rôle déclarés, instructions/mandat, écrans ou export de permissions, actions et destinataires, seuils, confirmations, journaux disponibles, possibilité documentée d'arrêt ou de retour. Aucun secret ni jeton d'accès demandé.

## Travail attendu

Comparer pour une intégration : lire, écrire, envoyer, supprimer, payer ou engager la structure ; ressource, destinataire, limite, décideur et preuve. Distinguer permission technique, instruction interne et pouvoir juridique. Repérer les écarts et proposer une restriction minimale, un seuil ou une validation humaine attribuée. Décrire journalisation, arrêt et retour possibles uniquement selon pièces ; absence de documentation reste une inconnue. Une validation humaine est une mesure à organiser, pas une obligation universelle déduite de l'usage d'un agent. Après action inattendue, transmettre une fiche IA-023 avec effets et traces ; banque, emploi ou administratif gardent les conséquences de l'acte.

## Sources à rechercher

Documentation exacte et datée de l'outil, mandat/délégation et contrats ; textes officiels de représentation, responsabilité, règlement IA et données selon fonction. Distinguer mesure interne souhaitée, faculté technique vérifiée et obligation légale applicable ; aucun comportement actuel de fournisseur supposé de mémoire.

## Critères d'acceptation

- [ ] La matrice relie chaque pouvoir à une pièce et montre les écarts de périmètre avec une mesure proposée et son responsable.
- [ ] Lecture, envoi, paiement et suppression sont distingués ; une permission technique ne prouve pas un mandat.
- [ ] Une option d'arrêt ou de retour non documentée reste à vérifier ; aucun réglage n'est annoncé modifié.
- [ ] Le paquet isolé donne un résultat utile sans accès au compte, profil ou plugin voisin.
- [ ] Sources/version et limites sont lisibles ; conclusion BASE-013 nommant le professionnel compétent.

## Vérification

- Cas normal : agent autorisé à préparer un courriel avec permission d'envoi ; identifier l'écart et proposer brouillon/validation selon capacités documentées.
- Cas limite : F11, envoi déjà observé mais export de permissions absent ; ne pas inventer une cause, une révocation ou une annulation, préparer le relais incident.

Recette future BASE-006 : sorties, paquet détaché, client et compréhension ; [portée de cette intégration](../exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Audit de cybersécurité, test intrusif, modification d'autorisations, exécution d'actions, révocation de jetons ou annulation juridique d'un acte.

## État de la proposition — 16 octobre 2026

`proposee`, préalable PILOTE-003 satisfait, aucune implémentation sélectionnée.
