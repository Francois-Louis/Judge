---
id: PDT-014
titre: "Isoler un dossier de produit, version ou campagne"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006]
---

# PDT-014 — Isoler un dossier de produit, version ou campagne

## Objectif et résultat attendu

Une petite équipe peut créer, sélectionner et archiver un dossier sans mêler preuves de deux versions ou campagnes, même chez le même organisme.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/matter-workspace/SKILL.md`
- `product-legal/references/dossier-produit.md (à créer)`
- `product-legal/CLAUDE.md (dossier actif et confidentialité)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Identifiant de dossier minimisé, type lancement/évolution/campagne, versions/dates, pièces et destinataires ; profil effectif si persistance, sans obligation de représenter plusieurs clients.

## Travail attendu

Adapter new/list/switch/close/none au produit/version/campagne ; remplacer exemples MSA/NDA/Delaware, autoriser plusieurs dossiers in-house. Liste minimale, sortie et journal limités au dossier, gravité/provenance conservées. Related matters ne suffit pas pour lecture croisée ; respecter flag et demande explicite. Utiliser helper et digest, refuser collisions et archive existante, distinguer archivage/conservation/effacement. Aucun effet de protection juridique depuis un niveau de confidentialité ou un en-tête.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Contrat technique BASE-008 et méthode BASE-005 ; recherche ciblée pour confidentialité/secret/conservation si une durée ou obligation est invoquée. Ne pas inventer politique de rétention depuis le simple archivage.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] Deux campagnes du même vendeur gardent leurs preuves, sorties et versions séparées.
- [ ] La fermeture du dossier actif retire son pointeur et n'écrase pas d'archive homonyme.
- [ ] Lister ou déclarer un dossier lié ne permet pas de lire son contenu ni de lui attribuer un sign-off.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : D01 — Deux campagnes pour deux versions du même carnet : création et bascule explicites, preuve rattachée à la bonne version.
- Cas limite : D02 — Slug archivé déjà présent, lien de dossier et demande cross-matter ambiguë : refus sans écrasement ni accès voisin, questions ciblées.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-annexes/exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Gestion de conservation complète, contrôle de conflits professionnel, garantie de secret et partage externe.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
