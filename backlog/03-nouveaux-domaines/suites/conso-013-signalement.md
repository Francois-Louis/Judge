---
id: CONSO-013
titre: "Préparer le signalement d'une pratique commerciale"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-013 — Préparer le signalement d'une pratique commerciale

## Objectif et résultat attendu

Une personne qui constate une pratique commerciale qui lui paraît trompeuse
prépare un signalement factuel et comprend qu'il ne règle pas son propre
litige.

## Périmètre et fichiers

- `consumer-legal/skills/practice-report/SKILL.md` — le skill (à créer)
- `consumer-legal/references/signalement.md` — canaux en vigueur et sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Captures datées ; adresse du site ou du magasin ; identité du professionnel ;
faits constatés ; démarche individuelle déjà faite.

## Sortie attendue

Fiche de signalement ; canal à vérifier ; pièces ; distinction signalement et
réclamation ; limites. Aucun envoi.

## Travail attendu

Ne pas qualifier la pratique d'infraction. Escroquerie alléguée → DOM-002 ;
données → privacy. Une demande de remboursement renvoie à la tâche métier concernée, puis CONSO-019 selon le stade.
La médiation relève de CONSO-006.

## Références métier et sources à rechercher

DGCCRF et service public de signalement en vigueur à la date du lot.

## Critères d'acceptation
- [ ] S01 produit une fiche factuelle sans qualification d'infraction.
- [ ] S02 explique la limite et oriente vers la réclamation individuelle.
- [ ] S03 et S04 distinguent signalement, preuve et recours individuel ; aucune attente de réponse administrative ne remplace le calendrier.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : S01 — Site affichant des prix barrés jamais pratiqués selon la personne.
- Cas limite : S02 — Personne qui attend un remboursement du signalement.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Dépôt du signalement, plainte, publication.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 8–12, 14–15, 83–84, 120, 123, 133–135, 152 de la [matrice des besoins](../dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Ajouter au dossier captures datées, prix successifs, parcours de résiliation et coordonnées du faux SAV allégué. Un signalement décrit les faits, distingue la déclaration de la preuve et ne conclut pas à l’infraction. Expliquer rôles distincts de DGCCRF, SignalConso, INC, association, médiateur, conciliateur et juge à partir des services effectivement vérifiés ; ne pas promettre de traitement individuel par un organisme d’information.

La demande au vendeur reste dans sa tâche métier ; après refus ou remboursement bloqué, CONSO-019. Une médiation relève de CONSO-006. La personne garde un calendrier séparé : aucun effet sur prescription ou remboursement n’est déduit du seul signalement.

- Cas limite : S03 — Signalement déjà fait, personne attendant que l’autorité ordonne le remboursement : réorienter vers la demande individuelle et son calendrier.
- Cas limite : S04 — Avis supprimés et compteur réinitialisé, sans accès aux données internes : conserver constats et inconnues sans affirmer manipulation prouvée.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
