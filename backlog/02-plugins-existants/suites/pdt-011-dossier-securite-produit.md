---
id: PDT-011
titre: "Préparer les justificatifs de sécurité d'un bien courant"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-001]
---

# PDT-011 — Préparer les justificatifs de sécurité d'un bien courant

## Objectif et résultat attendu

Un petit vendeur ou importateur obtient l'état des pièces de sécurité/traçabilité d'un bien de consommation non alimentaire courant, avec les manques et les points nécessitant expertise.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/launch-review/SKILL.md (branche dossier sécurité)`
- `product-legal/references/dossier-securite-produit.md (à créer)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Fiche PDT-001 ou équivalent, nature/usages/utilisateurs du bien, fabrication/importation/distribution, date de mise sur marché envisagée, lot/fournisseur, notices/étiquettes/évaluations et incidents connus.

## Travail attendu

Qualifier catégorie et rôle avant collecte : si jouet, électrique, médical, aliment ou autre secteur spécial, borner l'orientation et ne pas appliquer la grille de bien courant. Pour le cas retenu, faire tableau exigence recherchée/pièce/version/manque/contact, traçabilité et cohérence de notice. Distinguer document déclaré, effectivement lu et preuve d'essai ; ne jamais déduire sécurité ou CE universel. Un signal de danger interrompt la routine et donne faits minimaux, pièces et interlocuteur à rechercher, sans procédure de rappel inventée.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher règlement UE de sécurité générale des produits, articulation sectorielle, Code de la consommation et textes français pertinents selon date/catégorie/rôle ; identifier l'autorité compétente et les démarches de sécurité si signal, sans calculer une échéance non sourcée.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] Le dossier d'un bien courant distingue rôle, pièce existante, pièce manquante et preuve d'essai.
- [ ] Un produit sectoriel sort de la branche courante avec motif et orientation précise.
- [ ] Une déclaration du fournisseur ou un logo CE ne produit aucun certificat de sécurité ; un incident ne reçoit pas une simple liste administrative.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : S01 — Carnet non alimentaire sans fonction spéciale : tableau des justificatifs pertinents et inconnues, pas de sécurité certifiée.
- Cas limite : S02 — Objet présenté comme carnet mais doté de batterie, ou incident de brûlure déclaré : catégorie à reprendre et orientation ciblée/urgente, aucun feu vert ni rappel envoyé.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Tests de laboratoire, analyse technique, homologation, certification CE, procédure complète de rappel et notification à l'autorité.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
