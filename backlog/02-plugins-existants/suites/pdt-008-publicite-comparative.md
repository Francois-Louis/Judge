---
id: PDT-008
titre: "Examiner une comparaison publicitaire déterminée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-005]
---

# PDT-008 — Examiner une comparaison publicitaire déterminée

## Objectif et résultat attendu

Une équipe marketing reçoit une fiche sur une comparaison précise, sa base de mesure et les pièces nécessaires avant de conserver ou reformuler le message.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/marketing-claims-review/SKILL.md (branche comparative)`
- `product-legal/references/publicite-comparative.md (à créer)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Allégation PDT-005 ou équivalent, concurrent explicite/implicite, biens et besoins comparés, marché/public/date, protocole et données comparatives, visuels/marques et conditions de test.

## Travail attendu

Examiner identité du concurrent, comparabilité, critères, actualité, vérifiabilité et présentation globale selon les sources retenues. Distinguer préférence interne interdisant toute comparaison et règle juridique. Retirer substitution automatique de « only » par « first » ou d'un nom par « legacy tools » : ces phrases portent encore une affirmation. Relever la question de marque/dénigrement sans faire une clearance PI. Proposer correction seulement dans la portée prouvée, sans approbation globale.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Code de la consommation, textes UE et jurisprudence officielle pertinents sur publicité comparative et pratiques commerciales ; Code de la propriété intellectuelle seulement pour question identifiée avec relais PI. Pas de Lanham Act/NAD par défaut.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] La fiche relie comparaison, biens/besoins, critère et protocole fourni.
- [ ] Une mesure ancienne ou des configurations différentes restent visibles comme limites.
- [ ] Retirer le nom du concurrent ne suffit pas à rendre une comparaison sûre ni une allégation exclusive prouvée.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : C01 — Deux carnets comparés sur une propriété définie, références et protocole disponibles : examen de cette seule comparaison.
- Cas limite : C02 — « Le seul carnet durable », étude portant sur deux concurrents il y a trois ans : exclusivité non prouvée, aucune conversion automatique en « le premier ».
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-annexes/exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Étude de marché, recherche de marque complète, contentieux concurrence et publication.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
