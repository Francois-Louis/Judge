---
id: PDT-003
titre: "Décrire les effets d'une évolution de fonctionnalité"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-003 — Décrire les effets d'une évolution de fonctionnalité

## Objectif et résultat attendu

Un responsable produit reçoit une fiche avant/après qui relie le changement aux personnes, engagements et contrôles affectés, sans relancer toute la grille.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/feature-risk-assessment/SKILL.md (mode évolution et dispatch)`
- `product-legal/references/evolution-fonctionnalite.md (à créer)`
- `product-legal/CLAUDE.md (périmètre des deux modes)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Version ancienne et projetée, description et écrans, utilisateurs et pays, date, engagements existants, changements de données/prix/accès/fournisseur/IA et ancien avis si fourni.

## Travail attendu

Créer le contrat de fiche delta : id/version/date, fait ancien, fait projeté, source, personnes affectées, promesse et question associée. Renommer l'intitulé visible du mode en fiche d'évolution, conserver l'identifiant. Identifier les inconnues et réutilisations exactes possibles d'une revue antérieure ; ne pas considérer l'absence de nouveau marché ou le mot UI comme exemption. Trier ce qui relève du produit, données, consommation, IA et secteur ; fiche de relais sans exécution automatique. Corriger ses propres blocs de profil et de diffusion.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher seulement les dispositions françaises/UE nécessaires aux questions du changement, dont consommation, données ou accessibilité si faits déclencheurs ; les analyses spécialisées restent chez leur propriétaire, avec statut de preuve distinct.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] Chaque changement et chaque reprise de constat ancien mentionnent versions et preuve.
- [ ] Un déplacement de bouton modifiant choix ou accès n'est pas classé sans effet depuis son seul étiquetage UI.
- [ ] Une absence de version initiale produit une comparaison partielle et les questions nécessaires, sans ancien avis supposé.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : F01 — Option payante ajoutée à une fonctionnalité jusque-là incluse : fiche des promesses et utilisateurs affectés, question consommation/contrat ciblée.
- Cas limite : F02 — PRD dit UI-only mais déplace un choix de consentement et ajoute un événement analytics, ancienne maquette absente : delta partiel et relais données, aucune validation par notice seule.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Revue complète du lancement, AIPD/AIA automatique, audit technique et décision de déployer.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
