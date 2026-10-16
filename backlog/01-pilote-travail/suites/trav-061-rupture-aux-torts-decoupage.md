---
id: TRAV-061
titre: "Découper les demandes de rupture aux torts de l'employeur"
statut: proposee
priorite: P2
nature: cadrage
dependances: [PILOTE-001, PILOTE-003, BASE-005, BASE-006, BASE-013]
---

# TRAV-061 — Découper les demandes de rupture aux torts de l'employeur

## Objectif et résultat attendu

Deux propositions séparées pour lecture d'une prise d'acte et dossier de résiliation judiciaire.

Issue des [frictions travail](../pilote-001-annexes/pilote-001-frictions-utilisateurs.md)
du 16 octobre 2026 ; les points correspondants sont identifiés dans la matrice.

## Périmètre et entrées

Propriétaire : `employment-legal`. Salarié ou candidat du secteur privé ;
qualifier statut, demandeur, employeur, territoire, dates, CCN et accords.
Entrées nécessaires : Manquements allégués, preuves, chronologie, contrat et situation actuelle.
Une lecture ponctuelle accepte les pièces manuelles, sans profil professionnel,
registre ni connecteur obligatoire ; ne demander que les données utiles.

## Travail attendu

Distinguer effet immédiat allégué et contrat poursuivi, gravité et preuve sans recommander l'acte ; chaque suite fixe pièces, résultat, risque, voie et scénarios ; conseil avant cessation du travail.

Livrables : stories distinctes, chacune avec pièces, acte, résultat,
calendrier à rechercher, propriétaire et scénarios. Décrire les fichiers
et références à embarquer par les futurs lots ; ce cadrage ne crée pas de skill.

## Sources et calendrier à vérifier

Code du travail et jurisprudence officielle sur prise d'acte et résiliation judiciaire.
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
- [ ] Les suites produites ont chacune un acte, des entrées, des exclusions et un scénario vérifiables.

## Vérification attendue

- Cas normal : Salaires impayés et souhait de départ : deux parcours séparés, aucun courrier de rupture produit.
- Cas limite : Prise d'acte déjà envoyée : chronologie et orientation urgente, effets non garantis.
- Pièce ou source déterminante manquante : réserve ciblée, prochaine demande
  utile et professionnel pouvant conseiller, sans règle étrangère de remplacement.

## Hors périmètre

Rupture envoyée, stratégie chômage et saisine exécutée. Aucun envoi, dépôt, signature ou représentation effectué par cette proposition.

## État de la proposition

Statut `proposee` ; aucune extension sélectionnée ni scénario métier exécuté.
PILOTE-003 est terminé avec ses limites documentées. Portée des contrôles de
cette intégration : voir le relevé lié ci-dessus. La priorité P2 exprime la
famille du backlog, pas une fréquence statistique ni un ordre de livraison.
