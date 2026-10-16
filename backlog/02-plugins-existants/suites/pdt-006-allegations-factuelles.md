---
id: PDT-006
titre: "Examiner la preuve d'une allégation factuelle"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-005]
---

# PDT-006 — Examiner la preuve d'une allégation factuelle

## Objectif et résultat attendu

Une TPE reçoit une fiche pour une allégation de performance ou quantité, les écarts de preuve et une reformulation circonscrite si les faits la permettent.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/marketing-claims-review/SKILL.md (branche factuelle)`
- `product-legal/references/allegation-factuelle.md (à créer)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Ligne PDT-005 ou instantané équivalent, phrase et contexte exacts, produit/public/pays/date, étude ou données avec méthode, échantillon, période et configuration.

## Travail attendu

Comparer chaque composant du message à ce que mesure effectivement la preuve ; vérifier version, représentativité et limites. Formuler manque et question au détenteur des données, séparer donnée brute, avis marketing et règle recherchée. Proposer une rédaction courte seulement dans la portée prouvée ; typically ou une mention en bas de page ne répare pas automatiquement une promesse. Une allégation réglementaire/santé/environnement ou comparative est orientée vers son examen spécialisé. Aucun feu vert global.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher dispositions consommation/publicité françaises, actes UE et jurisprudence pertinents pour le message et son public ; ne pas importer FTC/NAD ni considérer une attestation SOC 2 comme preuve de toute promesse de sécurité.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] Le lien message/mesure/version/public apparaît dans la fiche, avec statut de preuve.
- [ ] Un échantillon ancien ou un test de laboratoire étroit ne valide pas une promesse générale d'usage.
- [ ] Une retouche n'introduit pas une nouvelle affirmation non justifiée.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : M03 — « Résiste à 100 ouvertures », protocole daté pour ce modèle : fiche ciblée reliant chaque réserve aux essais réellement fournis.
- Cas limite : M04 — « Ne s'abîme jamais », trois prototypes testés une fois : manque signalé, aucune réparation automatique par « généralement » ni étude inventée.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Essai de laboratoire, certification, avis sectoriel et approbation/publication du support.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.

## Complément de besoins — 16 octobre 2026

Les points 11 à 18, 27, 45 et 47 à 49 de la [matrice marketing](../exist-004-frictions-utilisateurs.md) demandent de confronter origine, fabrication, qualité d’expert, certification, résultats et visuels à leurs preuves. Séparer simulation, illustration et essai réel ; une mention IA ou un label ne valide pas la promesse. Recette attendue supplémentaire : image produit synthétique avec accessoires absents de la livraison → écart localisé, preuve et demande utiles, aucune accusation depuis le procédé seul.

Ces exigences et scénarios restent proposés, sans règle ou résultat métier validé par cette intégration.
