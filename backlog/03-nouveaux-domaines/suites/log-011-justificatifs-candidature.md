---
id: LOG-011
titre: "Contrôler la liste de justificatifs d'une candidature locative"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-011 — Contrôler la liste de justificatifs d'une candidature locative

## Objectif et résultat attendu

Le candidat ou garant comprend les pièces demandées et prépare une question
au bailleur ou à l'agence. Location privée vide ou meublée ordinaire,
résidence principale en France métropolitaine ; liste applicable à confirmer.
La tâche compare des intitulés, sans recueillir tout le dossier personnel.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/rental-application-document-review/SKILL.md` — tâche (à créer)
- `housing-legal/references/justificatifs-candidature.md` — listes, versions et relais données (à créer)
- `housing-legal/skills/rental-application-document-review/references/question-justificatifs.md` — modèle (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification locale LOG-001 ; PRV-024/026 sont des relais facultatifs,
sans dépendance d'installation.

## Pièces et informations nécessaires

Liste des justificatifs réclamés et message de demande daté, régime du bail,
candidat ou garant (personne physique/morale à qualifier), rôle de l'agence,
finalités et notice de conservation reçues, statut accepté/refusé et
échanges. Intitulés, extraits masqués ou captures ciblées suffisent : ni
relevés bancaires complets, ni document d'identité intégral, ni données de santé
par défaut. Si une pièce est ambiguë, demander sa catégorie avant son contenu.

## Sortie attendue

Tableau pièce demandée/personne concernée/entrée de liste et version/écart
ou inconnue ; questions au bailleur ou à l'agence ; distinction contrôle
locatif, sécurité du canal, finalité et conservation ; relais PRV-026 pour
qualifier le traitement et PRV-024 pour préparer un effacement ciblé.

## Travail attendu

Répondre au point 44 de la [matrice données personnelles](../../02-plugins-existants/exist-003-annexes/exist-003-frictions-utilisateurs.md).
Vérifier liste autorisée, champ, date et différences candidat/garant. Ne pas
confondre pièce autorisée, nécessité de collecte et durée de conservation.
Après refus, documenter seulement données déjà envoyées, destinataire,
finalité et durée annoncée ; aucune suppression totale ou immédiate promise.
Transmettre une orientation résumée, jamais les pièces personnelles ; si
privacy absent, expliquer ce relais sans commande ni installation automatique.
Refus discriminatoire allégué → DOM-029, question distincte.

## Références métier et sources à rechercher

Textes locatifs, décret n° 2015-1437 et listes dans leur champ/version,
distinction candidat/garant ; ANIL/ADIL. RGPD et doctrine CNIL seulement pour
identifier les questions à confier à PRV-026/024, qui portent leur analyse.
Ouvrir les sources officielles applicables et les transitions au lot ;
aucune liste ni durée issue d'un guide n'est tenue pour actuelle ici.

## Critères d'acceptation

- [ ] P01 compare la demande à la liste applicable sans exiger les pièces sensibles elles-mêmes.
- [ ] P02 sépare justificatif locatif et sort du dossier refusé, avec relais PRV-026/024 sur les seuls faits nécessaires.
- [ ] P03 distingue candidat et garant ; sans source, la légalité de la pièce reste réservée.
- [ ] Paquet seul et références locales vérifiés selon BASE-006 ; absence de privacy n'empêche pas le contrôle locatif et n'invente pas une tâche disponible.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si délai, acte ou enjeu irréversible (BASE-013).

## Vérification

- Cas normal : P01 — Liste de pièces intrusives pour un candidat ; comparer les intitulés, demander la source et ne pas collecter les originaux.
- Cas limite : P02 — Candidature refusée et dossier conservé, privacy indisponible ; questions ciblées et orientation données distincte, aucune suppression garantie.
- Cas limite : P03 — Pièces exigées du garant et présentées comme celles du candidat ; qualifier les rôles et versions avant de conclure.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Social/conventionné, mobilité, autres usages/territoires, audit RGPD complet,
collecte ou coffre-fort de dossiers, effacement exécuté, plainte, discrimination
au fond, scoring de solvabilité et envoi.

## Complément des frictions logement — 16 octobre 2026

Points 7 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

Comparer séparément justificatifs du candidat et du garant à la liste du régime/date. Relevés bancaires, informations médicales ou crédit demandé : documenter la demande sans exiger leur téléchargement pour l'examiner. PRV-026 traite finalité et conservation, PRV-024 une demande d'effacement ciblée ; la liste locative ne décide pas seule de tout le traitement de données.

- [ ] Le scénario complémentaire produit les distinctions, pièces et réserves ci-dessous, dans la borne de la story.

Scénario **attendu, non exécuté** : Agence réclamant relevés complets et dossier médical au garant : analyser la liste de demandes, sans collecter ces pièces sensibles.
Les montants et délais du texte utilisateur ne sont pas validés ; appliquer
les sources locales et la recette de la story avant toute livraison.
