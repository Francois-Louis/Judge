---
id: IA-003
titre: "Examiner une pratique IA potentiellement interdite"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-002]
---

# IA-003 — Examiner une pratique IA potentiellement interdite

## Objectif et résultat attendu

Une note examine une pratique précise et ses critères, avec faits correspondants, exceptions éventuelles et conclusion motivée ou réservée.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/use-case-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/pratiques-interdites.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Qualification IA-002, fonction réelle, personnes et contexte, moyens utilisés, objectifs/effets allégués, documentation et chronologie.

## Travail attendu

Prendre une pratique ciblée, par exemple inférence d'émotions alléguée en recrutement, et lire la disposition complète avec conditions et exceptions. Séparer émotion, sentiment déclaré, biométrie et simple traitement de texte ; demander le fonctionnement manquant. Une red line interne n'est pas une interdiction légale. Relever sans retard un signal sérieux, sans inventer de verdict ni proposer contournement par simple présence humaine. Conserver questions et mesures conservatoires proposées avec leur auteur ; aucune coupure technique exécutée.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher pratiques interdites, définitions, exceptions, calendrier et éventuels actes modificatifs dans le règlement IA ; guides officiels de Commission et autorités compétentes seulement avec statut distinct. Relais travail/privacy pour leurs questions propres.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] La note distingue opposition de politique interne, soupçon documenté et interdiction légalement établie ; une source inaccessible laisse la conclusion dépendante ouverte.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : B01 — Outil prétendant inférer les émotions de candidats depuis des vidéos : rapprochement critère/pièce et questions techniques avant conclusion.
- Cas limite : B02 — L'étiquette emotion AI ne correspond qu'à des réponses déclaratives ; source ou fonctionnement absent : pas d'interdiction déduite du nom ni d'exemption commerciale acceptée.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Examen de toutes les pratiques en une fois, décision RH, sanction, conseil de contournement et arrêt d'un service.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
