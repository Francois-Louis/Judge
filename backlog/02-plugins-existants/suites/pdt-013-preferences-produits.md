---
id: PDT-013
titre: "Créer ou modifier des préférences produit volontaires"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-013 — Créer ou modifier des préférences produit volontaires

## Objectif et résultat attendu

Une personne ou TPE choisit ses préférences de format, priorités et interlocuteurs sans devoir disposer d'un GC, de dix revues ou d'un outil connecté.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/cold-start-interview/SKILL.md`
- `product-legal/skills/customize/SKILL.md`
- `product-legal/CLAUDE.md (profil et configuration)`
- `product-legal/README.md (publics et sept skills)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Réponses explicites, éventuel profil existant, section à modifier, précédents facultatifs et intégrations que l'utilisateur souhaite tester ; aucune recherche dans historique personnel ou cache.

## Travail attendu

Distinguer préférences, faits société, qualification par produit et règles à vérifier. Conserver pause/reprise et champs non répondus ; remplacer defaults US/GC/VC par inconnues explicites et exemples adaptés. Un précédent renseigne une pratique, pas le droit. Diff ciblé avant édition, helper avec digest et conservation des sections voisines ; profil partagé seulement pour faits effectivement communs, sans modifier isolément son modèle commun. Statut intégration testé/configuré/non testé honnête ; aucune cadence créée. Retirer promesses de claims log/archive non contractualisés. Corriger contradictions STOP/ad hoc et en-têtes automatiques selon les futures tranches.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Charger méthode locale BASE-005 ; vérifier toute règle/date/seuil que l'utilisateur souhaite enregistrer selon sa source/portée, sinon la conserver comme assertion non établie. Confidentialité/secret français selon contexte, pas de protection automatique par label.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] Une boutique sans historique termine un profil minimal volontaire sans doctrine américaine ajoutée.
- [ ] Une modification de format conserve le reste du profil et refuse une édition sur digest périmé.
- [ ] Une préférence supprimant une revue ne supprime pas une obligation applicable et une déclaration MCP ne devient pas connexion testée.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : P01 — Artisan choisissant format court et contact qualité, sans avocat ni tracker : préférences limitées sauvegardées explicitement.
- Cas limite : P02 — Ancien profil US en pause, changement d'un seul destinataire, fichier modifié concurremment : réponses préservées et conflit signalé avant toute réécriture.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Migration de profil d'une autre distribution, corpus juridique dans le profil, modification transverse des modèles communs et création de scheduler.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
