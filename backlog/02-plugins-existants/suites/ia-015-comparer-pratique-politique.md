---
id: IA-015
titre: "Comparer une pratique IA à une politique déterminée"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-015 — Comparer une pratique IA à une politique déterminée

## Objectif et résultat attendu

Une pratique proposée obtient une comparaison précise avec une politique/version, avec écarts, choix et pièces manquantes.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/policy-monitor/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/comparaison-pratique-politique.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Texte réel de politique et version, description de la pratique/stade, personnes, automatisation, flux fournisseur et décisions internes disponibles.

## Travail attendu

Lire la politique réelle, pas uniquement son résumé dans le profil. Citer engagements concernés et distinguer compatible/inconnu/silence/contradiction sans verdict juridique. Un écart peut conduire à adapter la pratique, demander preuve ou proposer nouvelle politique ; ne pas toujours réécrire le texte pour suivre la pratique. Séparer proposition, approbation, déploiement et réalisation. L'obligation légale éventuelle appelle recherche dédiée, pas catégorie REQUIRED depuis le seul silence. Ne pas conclure can proceed depuis ADVISABLE. Proposer une modification limitée si demandée, sans publication.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Politique fournie et pièces de pratique ; rechercher une disposition contraignante seulement si nécessaire au point traité, avec qualification préalable. Guide et engagement interne gardent leur statut distinct.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Chaque écart conserve source/version/localisation, état proposé ou réel, preuve et décision restante ; aucune conformité légale déduite de l'accord à la politique.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : M01 — Politique interdisant traitement de dossiers clients dans l'outil, pratique proposée d'import de ces dossiers : contradiction localisée et options, aucune réécriture automatique.
- Cas limite : M02 — Politique non fournie ou résumé ancien : matrice de questions utile, pas d'affirmation couvert ni absence d'écart.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Balayage de tout l'historique, surveillance Slack, autorisation d'usage et adoption d'une nouvelle politique.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
