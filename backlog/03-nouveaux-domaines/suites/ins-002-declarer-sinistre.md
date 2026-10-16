---
id: INS-002
titre: "Préparer une déclaration de sinistre"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-005, PILOTE-003, BASE-005, BASE-006, INS-001]
---

# INS-002 — Préparer une déclaration de sinistre

## Objectif et résultat attendu

Une personne qui vient de subir un sinistre sait quoi déclarer, à qui,
quelles pièces réunir et quoi conserver, et obtient un brouillon de
déclaration fidèle aux faits.

## Périmètre et fichiers

- `insurance-legal/skills/claim-declaration/SKILL.md` — le skill (à créer)
- `insurance-legal/references/declaration.md` — contenu, pièces, sources lues (à créer)
- `insurance-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Contrat et conditions ; date et circonstances ; dommages constatés ; photos ;
factures ou preuves de valeur ; plainte s'il y a vol ; tiers impliqués.

## Sortie attendue

Brouillon de déclaration factuelle ; pièces et preuves à conserver ; mesures
conservatoires à vérifier dans le contrat ; délai indiqué par le contrat
recopié, sans délai légal affirmé sans texte lu ; limites.

## Travail attendu

Ne pas ajouter de dommage non constaté ni omettre un fait connu. Vol :
plainte en tâche distincte (DOM-002). Sinistre auto avec tiers : constat
amiable comme pièce, sans en faire l'analyse.

## Références métier et sources à rechercher

Code des assurances, obligations de l'assuré après sinistre (piste L113-2) ;
délais propres au risque (vol, catastrophe naturelle) à lire.

## Critères d'acceptation

- [ ] D01 produit une déclaration fidèle et la liste des pièces.
- [ ] D02 refuse d'ajouter un objet non possédé et l'explique.

## Vérification

- Cas normal : D01 — Dégât des eaux venu de l'appartement du dessus.
- Cas limite : D02 — « Ajoutons l'ordinateur, ils ne vérifieront pas. »

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Envoi de la déclaration, expertise, responsabilité du voisin.

## État de la proposition — 16 octobre 2026

Issue de DOM-005, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-005-decoupage-assurance.md).
