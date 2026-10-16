---
id: IA-005
titre: "Préparer la transparence d'une fonction IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-002]
---

# IA-005 — Préparer la transparence d'une fonction IA

## Objectif et résultat attendu

Une fonction et son public ont une fiche de transparence : déclencheurs, acteurs, support, moment, preuves et texte de mention proposé si le fondement est établi.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/use-case-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/transparence-usage.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

IA-002, interaction réelle ou contenu généré/manipulé, public/mineurs éventuels, canal, captures et accessibilité, chaîne fournisseur/utilisateur, dates d'usage.

## Travail attendu

Séparer interaction avec personne, marquage technique du contenu, information par le déployeur et cas particuliers ; déterminer qui doit quoi au lieu d'un statut limited exclusif. Rechercher conditions/exceptions, calendrier et contenu requis avant de rédiger une mention. Comparer maquette et affichage prouvé. Conserver question privacy/consommation/secteur distincte ; une bannière IA ne remplace pas leur information. L'absence de haut risque n'exclut pas la recherche de transparence.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher dispositions de transparence du règlement IA, actes et guides officiels pertinents, avec statut et application dans le temps ; information RGPD ou sectorielle seulement par relais ciblé.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Complément des frictions IA

Points 30–31 de la [matrice](../exist-005-frictions-utilisateurs.md) : distinguer interaction avec chatbot, génération/marquage et présentation d'un contenu manipulé, avec acteur et public propres. Rechercher obligations, exceptions et date d'application par fonction. Le soupçon de deepfake n'est pas une authentification ; transparence ne règle pas à elle seule consentement, image, retrait ou infraction. Cas attendu : contenu possiblement synthétique et intime ; relais urgent vers plateforme/expression/pénal selon demande, sans attendre une échéance alléguée du règlement IA.

## Critères d'acceptation

- [ ] La fiche distingue obligation du fournisseur et du déployeur, vérification de support et date ; aucune mention universelle ni calendrier depuis la watch list.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : T01 — Chatbot public de réponse documentaire : rôle, destinataire, point d'affichage et inconnues listés avant proposition de mention.
- Cas limite : T02 — Vidéo synthétique reprise par un intermédiaire, étiquette dans des métadonnées non visibles : ne pas confondre marquage, information du public et preuve de diffusion.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Politique complète, notice RGPD complète, certification de marquage et publication de mention.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.

## Complément de besoins — 16 octobre 2026

Les points 44 à 58 et l’encadré IA de la [matrice marketing](../exist-004-frictions-utilisateurs.md) exigent un examen ciblé de l’article 50 et de sa temporalité : fournisseur/déployeur, interaction, marquage technique, deepfake, contenu d’intérêt public et exceptions ne sont pas un seul cas. Toute image synthétique ne reçoit pas automatiquement une mention publique. Les mentions françaises d’influence restent à examiner dans PDT-009 et ne sont pas confondues avec les obligations IA. Recette attendue supplémentaire : chatbot et avatar publicitaire dans la même campagne → fiches par fonction/acteur avec sources, aucune validation du témoignage par la bannière IA.

Ces exigences et scénarios restent proposés, sans règle ou résultat métier validé par cette intégration.
