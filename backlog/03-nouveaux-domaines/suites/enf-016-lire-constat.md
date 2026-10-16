---
id: ENF-016
titre: "Examiner la portée d'un constat de commissaire de justice"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-016 — Examiner la portée d'un constat de commissaire de justice

## Objectif et résultat attendu

Une personne qui reçoit un constat comprend ce qui a été observé, ce qui a été rapporté par autrui et ce qui demeure à établir pour le litige.

## Périmètre et fichiers

- `enforcement-legal/skills/bailiff-report-reading/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/lecture-constat.md` — qualification, pièces, modèle de sortie et sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

Le paquet et `qualification-acte.md` sont créés par ENF-001. Chaque référence consommée est embarquée dans le paquet ; aucun plugin voisin n'est requis. Appliquer le contrat commun du [découpage](../dom-003-decoupage-execution.md).

## Pièces et informations nécessaires

Constat intégral et annexes, photographies et supports ; date, lieu, commanditaire et mission ; conditions d'accès ; pièces contraires ; observations de la personne ; objet du litige.

## Sortie attendue

Tableau passage cité, observation personnelle, déclaration rapportée ou déduction ; limites de la mission et du support ; contradictions étayées ; preuves manquantes et questions au conseil ou expert ; domaine du litige identifié.

## Travail attendu

Distinguer existence matérielle, cause, auteur et qualification juridique. Une photographie ou un propos consigné ne prouve pas à lui seul la responsabilité. Vérifier la portée probatoire et les conditions du constat au lieu d'affirmer qu'il est irréfutable ou nul. Conserver contexte, dates et annexes ; orienter le fond vers son domaine, une question technique vers l'expert et une contestation procédurale vers le contentieux.

## Références métier et sources à rechercher

Statut des commissaires de justice et portée de leurs constatations ; Code civil et Code de procédure civile, preuve et contradiction ; règles sectorielles et conditions d'accès selon le cas. Lire les textes et versions avant d'attribuer une force probante précise.

## Critères d'acceptation

- [ ] Le cas normal produit la sortie utile avec chaque fait attribué à sa pièce ou marqué comme déclaré.
- [ ] Le cas limite explicite les manques et distingue les procédures sans promettre d'issue favorable.
- [ ] Aucune règle, somme, compétence ou échéance n'est affirmée sans source lue et faits nécessaires ; un point réservé garde une action utile.
- [ ] Le résultat est compréhensible sans formation juridique ; le paquet installé seul contient les références et la méthode BASE-005 nécessaires.

## Vérification

- Cas normal : C01 — Constat d'humidité avec déclarations d'un voisin sur la cause : distinguer traces observées, déclaration et causalité encore à établir.
- Cas limite : C02 — Constat numérique incomplet et photographies contradictoires : demander annexes, contexte, date et méthode sans conclure à la nullité.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Expertise technique, conclusions ou demande de nullité rédigées, nouvelle constatation, devis de prestation ENF-018, envoi.

## État de la proposition — 16 octobre 2026

Issue des points 44 de la [matrice des frictions](../dom-003-frictions-utilisateurs.md). Exigence de backlog, sans sélection ni implémentation.
