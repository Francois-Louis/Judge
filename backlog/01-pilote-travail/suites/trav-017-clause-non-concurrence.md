---
id: TRAV-017
titre: "Expliquer une clause de non-concurrence reçue à l'embauche"
statut: proposee
priorite: P2
nature: implementation
dependances: [PILOTE-003, BASE-005, BASE-006]
---

# TRAV-017 — Expliquer une clause de non-concurrence reçue à l'embauche

## Objectif

Un candidat du privé en France métropolitaine comprend les emplois que la
clause pourrait lui interdire après le contrat, les conditions financières
annoncées et les questions à poser avant de répondre. Approfondissement
borné du reliquat H02 de l'[inventaire pilote](../pilote-001-annexes/pilote-001-plan-hiring-review.md)
et du défaut D05 du [bilan PILOTE-003](../pilote-003-annexes/pilote-003-verification.md).

## Périmètre

Plugin principal `employment-legal`, `skills/hiring-review/SKILL.md`, ses
repères métier et tests de recette. Pas de nouveau skill imposé. Entrées :
clause complète et annexes, fonctions réelles, territoire, dates, textes
collectifs applicables et éventuelle levée annoncée.
Sortie : activités visées, durée/espace, contrepartie et modalités de levée
expliquées dans un tableau sourcé, avec question/destinataire et réserves.

## Travail attendu

- Distinguer non-concurrence, exclusivité et non-sollicitation ; ne pas
  transformer le titre d'une clause en qualification acquise.
- Lire L1121-1, les décisions pertinentes de la Cour de cassation et les
  textes collectifs applicables, avec versions, portée et transitions.
  La décision du 10 juillet 2002, pourvoi `00-45.135`, est une **piste non
  vérifiée** dans le pilote, pas une décision déjà lue ; rechercher aussi
  les décisions ultérieures utiles au cas avant de formuler une conclusion.
- Authentifier les références par les voies officielles BASE-010 si besoin.
  Aucun accès PISTE obligatoire ; un extrait de moteur ne vaut pas lecture.
- Charger la méthode locale BASE-005, embarquer les repères nécessaires et
  tracer les lectures ; aucune dépendance runtime au backlog.
- Expliquer les conséquences sur un projet d'emploi concret sans décider de
  signer, contourner la clause ou contacter l'employeur à la place du candidat.

## Critères d'acceptation

- [ ] Le candidat distingue ses engagements pendant et après le contrat.
- [ ] Activités/durée/espace, contrepartie, paiement et levée sont confrontés aux fonctions et aux sources réellement lues.
- [ ] Une annexe absente du dossier n'est pas déclarée absente du contrat complet.
- [ ] Conclusion déterminante sourcée et datée ; source inaccessible ou champ collectif inconnu entraîne une réserve ciblée.
- [ ] Tableau et questions identifient une démarche utile auprès du recruteur/RH ou d'un professionnel, sans verdict global sur le contrat.
- [ ] Paquet installé autonome et scénarios réels BASE-006 conservés ; un lecteur non juriste reformule restriction, question et réserve.

## Vérification

Cas normal : CDI fictif complet, clause et annexe financière, fonctions et
champ collectif établis ; expliquer ce qui affecterait un poste envisagé.
Limites : H02 avec annexe manquante, puis décision primaire inaccessible ;
réserver sans affirmer validité/nullité ni inventer de consultation.
Rejouer H15 avec modèle américain : aucun régime étranger importé.
Le cas transfrontalier reste orienté hors tranche, sans avis sur le droit étranger.

## Hors périmètre

Contentieux, calcul d'indemnisation pour violation, stratégie de départ,
transaction, licenciement, rédaction générale de clauses ou envoi.
Cette proposition ne lance pas un second skill ni un nouveau domaine.

## Bilan d'exécution

Proposition du 15 octobre 2026 ; aucune adaptation réalisée ici. Les sources
jurisprudentielles et conventionnelles restent à lire et à appliquer à la
tranche explicitement choisie après la recette du pilote.
