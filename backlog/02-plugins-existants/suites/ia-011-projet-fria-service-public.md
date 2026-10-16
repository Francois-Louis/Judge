---
id: IA-011
titre: "Préparer un projet FRIA pour un déployeur de service public"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-010]
---

# IA-011 — Préparer un projet FRIA pour un déployeur de service public

## Objectif et résultat attendu

Un déployeur dont le besoin FRIA est établi dispose d'un projet limité à un système et un service public, avec contenu requis, preuves et décisions restantes.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/aia-generation/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/projet-fria-service-public.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Fiche IA-010 concluant au besoin avec fondement vérifié, processus du service, groupes affectés, fréquence/durée, contrôles, recours, pièces techniques et analyses déjà réalisées.

## Travail attendu

Décrire processus, contexte, groupes, risques pour les droits fondamentaux et mesures selon le texte réellement vérifié. Réutiliser seulement les parties pertinentes d'une analyse existante en indiquant source/version et lacunes. Documenter participation ou consultation seulement si réalisée ou à rechercher ; ne pas inventer témoignages. Produire projet, tableau de pièces manquantes et validations nécessaires. Distinguer rédaction de l'analyse, revue humaine, éventuelle communication/notification et mise à jour ; ces actions ne sont pas exécutées par le skill. Un formulaire officiel est vérifié avant usage, jamais reconstitué de mémoire.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher exigences FRIA, modalités/formulaire officiels applicables et obligations connexes pour le service délimité ; textes et compétence des autorités à vérifier à l'exécution. Le droit sectoriel du service reste un relais ciblé.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Le projet affiche pièces lues, manques, validations et nature de brouillon ; AIA, AIPD et décision d'accès au service restent des livrables distincts.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : R03 — Outil d'aide à l'accès à un service public, champ FRIA préalablement établi : projet traçable avec groupes, processus, risques et mesures.
- Cas limite : R04 — AIPD antérieure sur un autre flux et formulaire absent : réutilisation limitée, annexes manquantes et formalités réservées ; aucun dépôt simulé.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

FRIA de tout secteur, décision individuelle d'accès, AIPD complète, notification et certification.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
