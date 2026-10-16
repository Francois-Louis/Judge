---
id: TRAV-031
titre: "Préparer des observations sur une évaluation professionnelle"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006, BASE-013]
---

# TRAV-031 — Préparer des observations sur une évaluation professionnelle

## Objectif et résultat attendu

Tableau objectif/moyens/résultat et brouillon d'observations datées.

Issue des [frictions travail](../pilote-001-annexes/pilote-001-frictions-utilisateurs.md)
du 16 octobre 2026 ; les points correspondants sont identifiés dans la matrice.

## Périmètre et entrées

Propriétaire : `employment-legal`. Salarié ou candidat du secteur privé ;
qualifier statut, demandeur, employeur, territoire, dates, CCN et accords.
Entrées nécessaires : Objectifs successifs/dates, moyens, dépendances, évaluations et incidents.
Une lecture ponctuelle accepte les pièces manuelles, sans profil professionnel,
registre ni connecteur obligatoire ; ne demander que les données utiles.

## Travail attendu

Séparer insuffisance, faute, objectifs irréalisables, retrait de moyens et notation après alerte/mandat ; identifier automatisation sans déduire une IA d'un score.

Fichiers à examiner puis créer si ce choix est confirmé :
`employment-legal/skills/objectifs-evaluation/SKILL.md` et
`employment-legal/references/objectifs-evaluation.md`, ainsi que le routage minimal
et la documentation concernés. Ces chemins sont des propositions futures.
Charger la copie locale de BASE-005 et les références métier embarquées ;
respecter BASE-008 pour les écritures durables, sans dépendre d'un autre plugin
ou du backlog à l'exécution. Les relais indisponibles produisent une fiche
manuelle ; ne jamais invoquer une branche héritée non adaptée.

## Sources et calendrier à vérifier

Code du travail, accords et jurisprudence officielle sur objectifs, évaluation et formation.
Pistes à lire lors de l'implémentation : textes exacts, versions aux dates du
dossier, champ et transitions, avec voies alternatives BASE-010 si nécessaire.
Le [relevé d'intégration](../pilote-001-annexes/pilote-001-frictions-verification.md)
distingue les quelques lectures officielles préliminaires des sources futures.
Les assertions du guide utilisateur ne constituent pas un corpus validé.

Pour toute échéance : nature (signalement, rétractation, procédure ou
prescription), règle/version, événement et date prouvés, unité de décompte,
exceptions, acte requis, destinataire et inconnues. Une réclamation, une demande
RGPD, une négociation ou une mauvaise saisine ne reçoit aucun effet suspensif
ou interruptif automatique. Si les éléments manquent, terme `a-determiner`,
pièces à obtenir et interlocuteur compétent, sans fausse date rassurante.

## Critères d'acceptation

- [ ] Le résultat annoncé est observable et relie chaque constat aux pièces, faits déclarés et inconnues.
- [ ] Cas normal et limite conduisent aux réponses distinctes décrites ci-dessous, compréhensibles sans formation juridique.
- [ ] Les conclusions et calculs déterminants reposent sur des sources effectivement lues et applicables ; aucun abus, indemnisation forfaitaire ou succès n'est présumé.
- [ ] Le périmètre et les relais restent explicites ; paquet autonome, méthode locale et stockage BASE-008 prévus selon la nature du lot.
- [ ] BASE-013 : phrase finale nommant l'avocat en droit du travail ou le professionnel compétent ; renfort en tête si urgence, procédure ou acte irréversible.
- [ ] La recette BASE-006 conserve sorties, paquet détaché, invocation client, résultat métier et compréhension ; un contrôle statique seul ne suffit pas.

## Vérification attendue

- Cas normal : Objectifs modifiés après période évaluée : versions et obstacles rapprochés.
- Cas limite : Note dégradée après signalement : indices conservés sans discrimination présumée ; TRAV-043 et données séparées.
- Pièce ou source déterminante manquante : réserve ciblée, prochaine demande
  utile et professionnel pouvant conseiller, sans règle étrangère de remplacement.

## Hors périmètre

Enquête employeur, licenciement et audit d'algorithme. Aucun envoi, dépôt, signature ou représentation effectué par cette proposition.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée ni scénario métier exécuté.
PILOTE-003 est terminé avec ses limites documentées. Portée des contrôles de
cette intégration : voir le relevé lié ci-dessus. La priorité P2 exprime la
famille du backlog, pas une fréquence statistique ni un ordre de livraison.
