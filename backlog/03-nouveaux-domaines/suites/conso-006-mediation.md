---
id: CONSO-006
titre: "Préparer la saisine d'un médiateur de la consommation"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-006 — Préparer la saisine d'un médiateur de la consommation

## Objectif et résultat attendu

Après une réclamation écrite restée sans réponse satisfaisante, une personne
identifie le médiateur compétent, vérifie les conditions de saisine et
obtient un brouillon de demande avec la liste des pièces.

## Périmètre et fichiers

- `consumer-legal/skills/mediation-referral/SKILL.md` — le skill (à créer)
- `consumer-legal/references/mediation.md` — conditions, sources lues, modèle (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Réclamation écrite et sa date ; réponse du vendeur ; médiateur indiqué dans
les CGV, sur le site ou la facture ; pièces du litige ; démarches judiciaires
éventuelles.

## Sortie attendue

Médiateur identifié ou manque signalé ; conditions de recevabilité à
vérifier ; brouillon de saisine ; pièces ; limites (la médiation ne garantit
pas d'accord).

## Travail attendu

Accepter la sortie de CONSO-001 ou une réclamation fournie manuellement. Un
médiateur sectoriel (énergie, télécoms, banque, assurance) renvoie au
domaine du secteur. Conciliateur et juge : orientation vers le contentieux,
sans préparer l'acte.

## Références métier et sources à rechercher

Code de la consommation, médiation de la consommation ; liste officielle des
médiateurs et autorité qui la tient, consultées à la date du lot.

## Critères d'acceptation
- [ ] M01 identifie le médiateur et prépare la saisine sans affirmer de délai non lu.
- [ ] M02 signale l'absence de médiateur indiqué et la démarche pour l'obtenir.
- [ ] M03 oriente vers DOM-005 sans saisir un médiateur de consommation générique.
- [ ] M04 et M05 identifient compétence, antériorité des démarches et effet d’un accord sans recevabilité ou suspension présumées.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : M01 — Suite de N01 : réclamation sans réponse, médiateur nommé dans les CGV.
- Cas limite : M02 — Vendeur qui n'indique aucun médiateur.
- Cas limite : M03 — Refus d'un assureur.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Envoi de la saisine, conciliation, procédure judiciaire.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 135–140, 142 de la [matrice des besoins](../dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Recueillir réclamation initiale écrite, preuve de date, réponse, autres médiations et procédures déjà engagées. La sortie comprend un tableau de recevabilité : qualité des parties, compétence et rattachement vérifiés, démarche préalable, délai, saisine concurrente et inconnues. Aucun médiateur n’est choisi sur le seul secteur commercial affiché.

Distinguer rôle du médiateur, gratuité à vérifier, proposition et effets d’un accord accepté. La médiation ne garantit pas un remboursement. Conciliation, tentative amiable préalable et procédure judiciaire reçoivent une orientation EXIST-006 ; seuils, exceptions et effets sur la prescription restent à vérifier. Une offre de transaction relève aussi de CONSO-019.

- Cas limite : M04 — Deux médiateurs déjà saisis et réclamation initiale non datée : recevabilité réservée, sans date limite fabriquée.
- Cas limite : M05 — Proposition de remboursement acceptée avec engagements annexes : distinguer proposition et portée de l’accord avant toute suite.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
