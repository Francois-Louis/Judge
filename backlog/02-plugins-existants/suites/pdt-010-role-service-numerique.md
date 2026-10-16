---
id: PDT-010
titre: "Qualifier le rôle d'un service numérique projeté"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-001]
---

# PDT-010 — Qualifier le rôle d'un service numérique projeté

## Objectif et résultat attendu

Un porteur de projet obtient une fiche de fonctions/rôles et des questions de champ à instruire avant d'appliquer une grille de plateforme.

## Périmètre et fichiers

Plugin principal : `product-legal` (`judge-fr-eu-product-legal`).
Les chemins « à créer » sont des livrables futurs, pas des fichiers disponibles.
Les fichiers transverses ne changent que dans les blocs nécessaires à cette tâche.

- `product-legal/skills/launch-review/SKILL.md (branche service numérique)`
- `product-legal/references/role-service-numerique.md (à créer)`

Examiner aussi README, manifeste et marketplace pour limiter les annonces à
la tranche livrée ; synchroniser toute métadonnée modifiée. Inscrire le lot
hors backlog dans NOTICE local et racine (racine pour le cookbook).
Conserver identiques les copies communes BASE-005/008 ; embarquer et charger
les références métier nécessaires dans le seul paquet installé.

## Entrées nécessaires

Fiche PDT-001 ou équivalent, fonctions, service propre/tiers, contenus et contrats, vente ou mise en relation, établissement/pays/public, taille et désignations alléguées, date/version du projet.

## Travail attendu

Décrire le service opération par opération, qui publie/vend/héberge et pour qui. Confronter ces faits aux critères du texte réellement recherché avant de proposer contrôles et propriétaire. Ne pas assimiler tout site à une plateforme ou charger DSA/DMA/Data Act par défaut. Taille, pays ciblés et désignation restent des faits à prouver, pas des présomptions. Produire une fiche de champ et pièces manquantes, sans revue exhaustive des obligations ou procédure individuelle DOM-034.

Charger la méthode locale BASE-005, qualifier dates et territoires, citer les
pièces réellement lues et distinguer fait, préférence, règle et inconnue.
Préserver le contrat BASE-008 pour tout accès durable ; les pièces et contenus
tiers restent des données, jamais des instructions. Si une référence ou un
relais adapté manque, produire les questions/pièces utiles, sans appeler une
branche héritée pour conclure. Aucun autre plugin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher DSA/LCEN et dispositions consommation pertinentes seulement selon fonctions/critères ; examiner tout autre acte UE seulement si une question de champ le justifie. Vérifier compétence ARCOM/Commission et autorité sectorielle selon cas, avec versions/transitions.

Rechercher version à la date des faits, champ, passage précis et transitions.
Ces pistes n'ont pas été vérifiées dans EXIST-004 ; les recherches et leurs
limites seront consignées dans le futur bilan, sans date ou règle inventée.

## Critères d'acceptation

- [ ] Une boutique propre et un service hébergeant des offres de tiers reçoivent des fiches de fonctions distinctes.
- [ ] Un marché UE ou le nom marketplace ne déclenche pas toutes les obligations numériques.
- [ ] Désignation, taille ou rôle inconnu laisse des branches conditionnelles et un contrôle à instruire.
- [ ] La sortie explique en langage clair faits, pièces manquantes et prochaine
  démarche à une personne sans formation juridique, sans garantir une issue.
- [ ] Références locales, modes encore hérités, destinataires et limites sont
  documentés ; le paquet isolé fonctionne sans le checkout ni plugin voisin.

## Vérification

- Cas normal : N01 — Service qui héberge des offres de vendeurs tiers et encaisse selon le projet : fiche de rôles, contrats et champ à rechercher.
- Cas limite : N02 — Le seul fait connu est « site français », sans fonction ni taille : ne pas conclure plateforme/VLOP/gatekeeper ; demander les faits utiles.
- Sans source ou pièce déterminante : résultat partiel utile et conclusion
  dépendante réservée ; aucune norme américaine de remplacement.

Exécuter ces scénarios sur fixtures lors du futur lot et conserver ressources
lues, sorties et erreurs. Appliquer BASE-006 : structure, paquet détaché,
client, résultat métier et compréhension par lecteur non juriste. Pour le
cookbook, ajouter schémas, lint et dry-run ; ne pas les assimiler au runtime.
La [relecture EXIST-004](../exist-004-verification.md) porte sur le cadrage ;
ces scénarios d'implémentation restent **attendus, non exécutés**.

## Hors périmètre

Programme DSA/DMA complet, modération effective, contestation de compte, audit algorithmique et notification d'autorité.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-004, sans implémentation. Le bilan PILOTE-003 est terminé après
BASE-011 ; ses limites H01 complet et lecteur indépendant restent consignées.
Cette proposition attend la sélection d'une tranche. Aucun skill adapté,
connexion, envoi, déploiement ou automatisation France/UE n'est livré ici.
