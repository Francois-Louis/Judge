---
id: PDT-012
titre: "Orienter une question produit ou publicité ponctuelle"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-012 — Orienter une question produit ou publicité ponctuelle

## Objectif et résultat attendu

Un artisan, une fondatrice ou un PM reçoit une réponse courte : faits connus, question déterminante et prochaine démarche, avec la conclusion réservée lorsqu'une source manque.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/is-this-a-problem/SKILL.md`
- `product-legal/references/question-produit.md (à créer)`
- `product-legal/CLAUDE.md (réponse ponctuelle et destinataire)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Question en langage courant, action envisagée, acteur/public/marché/catégorie/rôle/date et pièce disponible ; demander d'abord le fait qui change l'orientation au lieu d'un questionnaire complet.

## Travail attendu

Séparer produit, publicité, contrat, données, IA et simple choix commercial ; répondre à la bonne taille. Retirer Fine/Ship it depuis calibration, promesse d'une minute et délais PIA/AIA internes présentés comme nécessaires. Une notice existante ou une pratique habituelle n'est pas une autorisation. Si analyse complexe, produire une fiche minimale pour la tranche adaptée sans exécuter les workflows hérités. Adapter confidentialité et destinataire depuis les faits, sans en-tête US imposé ni avocat obligatoire pour obtenir une explication.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher uniquement la question juridique déterminante dans les sources officielles françaises/UE pertinentes, avec statut de lecture ; si elles manquent, donner pièces/interlocuteur et réserver la conclusion, sans retour au droit américain.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] La réponse contient une prochaine action utile et distingue fait, préférence et règle recherchée.
- [ ] Le profil absent n'empêche pas une orientation conversationnelle ; aucun profil n'est importé ou créé implicitement.
- [ ] Un exemple de calibration ou l'absence de changement visible ne produit pas de feu vert.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : Q01 — « Puis-je afficher le logo de mon client ? », clause publicité fournie : question de portée/usage et relais contrat/PI/publicité selon faits.
- Cas limite : Q02 — « Ajouter un événement analytics, c'est juste une UI ? », aucun flux fourni : question données pertinente, pas de fine depuis la notice ni PIA automatique en un jour.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Revue complète, avis sur toute la loi, publication, consultation automatique d'un autre plugin et message Slack.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
