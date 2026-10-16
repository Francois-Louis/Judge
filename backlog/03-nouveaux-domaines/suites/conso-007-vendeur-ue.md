---
id: CONSO-007
titre: "Orienter un litige avec un vendeur établi dans un autre État de l'UE"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-007 — Orienter un litige avec un vendeur établi dans un autre État de l'UE

## Objectif et résultat attendu

Une personne résidant en France en litige avec un vendeur établi dans un
autre État de l'UE sait quelles questions de loi et de juge se posent, quel
organisme d'aide consulter et quelles pièces préparer.

## Périmètre et fichiers

- `consumer-legal/skills/cross-border-purchase/SKILL.md` — le skill (à créer)
- `consumer-legal/references/transfrontalier.md` — pistes de loi, juridiction, aide transfrontalière, sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Pays d'établissement du vendeur ; site, langue, livraison proposée vers la
France ; conditions acceptées et choix de loi éventuel ; pièces du litige.

## Sortie attendue

Fiche de qualification transfrontalière avec ce qui reste conditionnel ;
orientation vers le CEC France ; pièces ; limites. Vendeur hors UE : limites
explicites et douane (DOM-009) si pertinent.

## Travail attendu

La demande de fond (non-livraison, défaut) reste dans le skill qui la
traite ; ce skill ajoute la dimension transfrontalière. Ne mentionner un
mécanisme européen de règlement en ligne qu'après vérification de son statut
à la date du lot.

## Références métier et sources à rechercher

Règlement Rome I, art. 6 ; règlement Bruxelles I bis, art. 17 à 19 ;
procédure européenne de règlement des petits litiges ; CEC France comme
organisme d'orientation. Copies propres au paquet : les lectures faites pour
commercial ne sont pas une dépendance.

## Critères d'acceptation
- [ ] X01 laisse loi et juge conditionnels et oriente vers le CEC France.
- [ ] X02 explique les limites hors UE sans promettre de recours.
- [ ] Aucun mécanisme européen cité sans statut vérifié.
- [ ] X03 ne propose aucun service obsolète ou hors périmètre comme recours certain.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : X01 — Vendeur établi en Allemagne, commande non livrée.
- Cas limite : X02 — Vendeur hors UE sur une place de marché européenne.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Saisine d'une juridiction, traduction, recouvrement à l'étranger.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 1, 4, 51, 143 de la [matrice des besoins](../dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Identifier pays réel, preuve d’établissement et activité dirigée, sans déduire la loi du nom de domaine. Vérifier périmètre géographique et personnel du CEC et statut des services européens à la date de la démarche. L’annonce de fermeture de la plateforme ODR/RLL dans le guide reste une piste à ouvrir ; aucun ancien lien de CGV n’est proposé comme service actuel sans contrôle. Les limites hors UE et celles du recouvrement sont annoncées.

- Cas limite : X03 — CGV renvoyant à un ancien service européen, vendeur d’un pays encore inconnu : vérifier disponibilité et périmètre avant orientation.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
