---
id: CONSO-005
titre: "Lire une garantie commerciale ou une extension proposée"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-002]
---

# CONSO-005 — Lire une garantie commerciale ou une extension proposée

## Objectif et résultat attendu

Une personne à qui l'on propose une garantie ou une extension, ou qui en
détient une au moment d'une panne, comprend qui la donne, ce qu'elle couvre,
ce qu'elle coûte et ce qu'elle ne remplace pas.

## Périmètre et fichiers

- `consumer-legal/skills/commercial-warranty-reading/SKILL.md` — le skill (à créer)
- `consumer-legal/references/garantie-commerciale.md` — grille de lecture et sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

`garanties-legales.md` (CONSO-002) est relu, pas réécrit.

## Pièces et informations nécessaires

Document de garantie ou offre d'extension ; garant indiqué ; prix ; facture
du bien ; date de la panne s'il y en a une.

## Sortie attendue

Fiche lisible : garant, durée, couverture, exclusions, prix, démarche ;
rapport aux garanties légales selon la référence relue ; questions à poser
avant d'acheter ou au moment de la panne.

## Travail attendu

Le garant décide de la branche : un document émis par un assureur relève de
DOM-005. Ne pas qualifier l'offre de trompeuse ; relever les écarts entre ce
qui est dit et ce qui est écrit.

## Références métier et sources à rechercher

Code de la consommation, garantie commerciale et information due, version à
la date de souscription.

## Critères d'acceptation
- [ ] W01 explique la couverture et ce qu'elle ne remplace pas, selon la source lue.
- [ ] W02 oriente vers DOM-005 sans analyser le contrat d'assurance.
- [ ] La sortie se comprend sans formation juridique.
- [ ] W03 et W04 expliquent coût et apport éventuel de l’extension sans la déclarer inutile ni confondre assurance et garantie commerciale.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : W01 — Extension de trois ans proposée en caisse pour un téléviseur.
- Cas limite : W02 — « Garantie casse » dont le document nomme un assureur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Contrat d'assurance, conseil d'achat, comparaison de prix.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 58, 73, 75, 80 de la [matrice des besoins](../dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Ajouter à la fiche un comparatif des prestations réellement supplémentaires : périodes, risques, exclusions, frais, interlocuteur et prix. Une durée commerciale annoncée n’épuise pas la garantie légale. Contrat d’assurance ou assistance distincte : identité du garant et orientation DOM-005, sans qualification d’après le seul nom marketing. La vente prétendument indispensable de l’extension peut faire l’objet d’un signalement séparé (CONSO-013).

- Cas limite : W03 — Extension payante présentée comme seule protection, mais mêmes pannes et période que les droits légaux allégués : comparatif conditionnel.
- Cas limite : W04 — Protection au nom d’un assureur sans conditions remises : pièces manquantes et relais assurance, aucune couverture présumée.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
