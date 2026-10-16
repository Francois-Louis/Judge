---
id: USAGE-002
titre: "Prioriser les premières tâches selon leur utilité quotidienne"
statut: terminee
priorite: P1
nature: cadrage
dependances: [USAGE-001, BASE-006]
---

# USAGE-002 — Prioriser les premières tâches selon leur utilité quotidienne

## Objectif

Choisir de petites tâches qui rendent un service concret et vérifiable aux
personnes, en gardant une progression maîtrisée.

## Points de départ

- [Situations du quotidien](../usages-quotidiens.md).
- [Revue d'embauche proposée comme pilote](../01-pilote-travail/pilote-002-revue-embauche.md).
- [Contrôles d'une adaptation](../00-fondations/base-006-controles-paquetage.md).

## Travail attendu

- Comparer quelques tranches limitées : lire un contrat reçu par un candidat,
  demander les justificatifs d'une facture, contester une retenue sur dépôt,
  relire un devis ou décrypter une demande de pièces.
- Pour chaque tranche, préciser personne aidée, sortie utile, pièces, sources,
  difficulté de vérification, urgence éventuelle et dépendances techniques.
- Distinguer potentiel d'utilité et capacité à livrer correctement : une
  urgence grave ne justifie pas de commencer par un workflow mal maîtrisé.
- Proposer un ordre court et justifié. Les fréquences, économies ou taux de
  succès ne sont pas inventés ; une hypothèse de priorisation est étiquetée
  comme telle, une statistique utilisée est sourcée.
- Si le pilote proposé change, mettre à jour ses stories et dépendances
  explicitement. Ne pas lancer un second pilote en parallèle par défaut.

## Critères d'acceptation

- [x] La comparaison porte sur des tâches réalisables, pas seulement sur des noms de codes ou de plugins.
- [x] Le résultat attendu peut être évalué : document compris, pièce identifiée ou demande correctement préparée.
- [x] Le premier lot est limité et ses exclusions sont écrites.
- [x] Les domaines spécialisés restent dans le backlog même lorsqu'ils ne sont pas le premier lot choisi.
- [x] Le choix du pilote reste proposé tant qu'il n'est pas arrêté ; aucun développement n'est déclenché par le classement.

## Vérification

Relire le classement avec trois profils : un salarié, un retraité et un petit
exploitant. Identifier le bénéfice concret attendu et les obstacles de chaque
tâche sans présumer leurs connaissances juridiques ou leurs moyens.

## Hors périmètre

Prioriser tout le catalogue dans le détail, promettre une couverture exhaustive
ou remplacer le contrôle juridique par une mesure de satisfaction.

## Bilan d'exécution — 15 octobre 2026

- Livrable : [comparaison et ordre proposé](usage-002-annexes/usage-002-comparaison-priorites.md)
  de cinq tâches bornées : contrat reçu par un candidat, facture de matériel
  après retour d'une box, demande de pièces du notaire, retenue sur dépôt et
  devis de rénovation. Chaque ligne précise public, sortie évaluable, pièces,
  pistes de sources, difficulté, urgence éventuelle et dépendances.
- L'utilité potentielle est séparée de la capacité à livrer correctement.
  L'ordre est une hypothèse sans statistiques inventées : contrat, facture,
  pièces du notaire, dépôt, devis. Les rangs suivants restent à réexaminer
  après bilan et ne remplacent pas les premières tranches des cadrages DOM.
- Premier lot proposé : PILOTE-002 seulement, avec CDI privé en France
  métropolitaine comme cas nominal, CDD en vérification spécifique et
  orientations hors champ. Sortie, modifications nécessaires, exclusions et
  conditions de recette BASE-006 sont écrites. Aucun skill n'est modifié.
- [Relecture avec trois profils fictifs](usage-002-annexes/usage-002-verification.md) : quinze
  croisements salarié/retraité/petit exploitant × cinq tâches, avec bénéfice
  attendu, obstacle et prochaine étape. Aucun niveau juridique, équipement
  ou moyen financier n'est déduit du profil. Le bénéfice du pilote pour les
  personnes sans projet d'emploi est explicitement limité.
- PILOTE-002 et PILOTE-003 restent proposées, avec leurs dépendances
  inchangées ; le choix du pilote n'est pas arrêté. Les domaines spécialisés
  et leurs priorités restent au backlog. Aucun second pilote n'est lancé.
- Contrôles documentaires : liens locaux, tableaux, UTF-8, cohérence des
  statuts et dépendances, conservation des stories et du périmètre technique ;
  résultats consignés dans le relevé de vérification.
- Limites : relecture de cadrage sur récits fictifs, sans participant réel,
  consultation de sources métier externes, validation juridique, exécution
  de skill ni installation isolée. Ces contrôles restent aux futurs lots ;
  terminer USAGE-002 ne déclenche pas leur développement.
