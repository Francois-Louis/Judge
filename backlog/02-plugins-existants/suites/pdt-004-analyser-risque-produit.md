---
id: PDT-004
titre: "Comparer les mesures pour un risque produit déterminé"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-003]
---

# PDT-004 — Comparer les mesures pour un risque produit déterminé

## Objectif et résultat attendu

Une équipe ou TPE obtient des options de conception pour un risque concret, leurs effets attendus et les preuves nécessaires pour constater la réduction du risque.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/feature-risk-assessment/SKILL.md (mode risque ciblé)`
- `product-legal/references/risque-produit.md (à créer)`
- `product-legal/CLAUDE.md (calibration et décision)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Fiche delta PDT-003 ou instantané équivalent, risque déclencheur précis, personnes concernées, constat amont et gravité, mesures existantes/projetées, contraintes et pièces de mise en œuvre.

## Travail attendu

Décrire un risque et ses variantes, préjudices pour les personnes, probabilité/gravité motivées et incertitudes. Comparer deux ou trois mesures réalistes avec coût, couverture et risque restant, en distinguant prévu/réalisé/prouvé. Ne pas limiter les variantes déterminantes à un nombre arbitraire. Rechercher l'obligation même sans attention récente du régulateur. Ne pas traiter acceptation interne du risque comme dispense ; garder la gravité amont ou justifier toute évolution. Séparer choix du décideur et recommandation de recherche, sans AIA/PIA doublonnée par défaut.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Sources françaises/UE propres au risque établi, droit des contrats/consommation ou texte sectoriel selon champ ; jurisprudence seulement si pertinente, avec faits et portée confrontés. Secret et diffusion à examiner selon auteur/destinataire, aucun privilège garanti par marquage.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] La réduction du risque annoncé repose sur une mesure et une preuve identifiées ; une mesure future reste future.
- [ ] Une option contraire à une obligation vérifiée n'est pas rendue acceptable par l'appétence au risque.
- [ ] Une baisse de gravité amont est justifiée et les limites des analyses spécialisées restent visibles.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : F03 — Risque d'achat involontaire lié à une commande en un clic : options de confirmation, impacts et preuves d'écrans/test à obtenir.
- Cas limite : F04 — Mesure de confirmation annoncée mais non déployée et ancienne revue marquée rouge : risque conservé, aucune baisse depuis une promesse ou un concurrent qui l'utilise.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-annexes/exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Modèle quantitatif, étude générale de responsabilité, audit UX, avis IA/données spécialisé et validation technique.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
