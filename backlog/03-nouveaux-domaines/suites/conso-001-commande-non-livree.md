---
id: CONSO-001
titre: "Préparer une réclamation pour une commande non livrée"
statut: a-verifier
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# CONSO-001 — Préparer une réclamation pour une commande non livrée

## Objectif et résultat attendu

Une personne qui a commandé un bien à distance à un professionnel et ne l'a
pas reçu obtient, en langage clair, la fiche de sa commande, les pièces qui
manquent et un brouillon de réclamation au vendeur. Cette tranche crée le
paquet `consumer-legal` avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `consumer-legal` (`judge-fr-eu-consumer-legal`). Les fichiers
ci-dessous sont créés par la tranche du 17 octobre 2026 ; le bilan en fin de
story distingue les couches de validation.

- `consumer-legal/.claude-plugin/plugin.json` — manifeste, version `0.1.0`
- `consumer-legal/README.md` — tâche livrée, public, limites
- `consumer-legal/CLAUDE.md` — modèle minimal, aucun profil requis
- `consumer-legal/NOTICE` — entrée datée du lot
- `consumer-legal/LICENSE` — copie de la licence du dépôt
- `consumer-legal/references/shared/research-citation-method.md` — copie BASE-005 courante `1.2.0` identique
- `consumer-legal/references/isolation.md` — copie BASE-008 identique
- `consumer-legal/scripts/judge_store.py` — copie BASE-008 identique
- `consumer-legal/references/company-profile-template.md` — copie BASE-008 identique
- `consumer-legal/references/dashboard-template.md` — copie BASE-008 identique
- `consumer-legal/references/qualification-achat.md` — contrat commun de qualification
- `consumer-legal/skills/non-delivery-claim/SKILL.md` — le skill
- `consumer-legal/skills/non-delivery-claim/references/non-livraison.md` — repères, sources lues, modèle de brouillon
- `.claude-plugin/marketplace.json` — inscription, sélection explicite par la présente demande
- `scripts/test-base008-isolation.py` — décompte réel et exception bornée de paquet sans entretien
- `NOTICE` — entrée racine du lot

Les mentions « douze paquets » de `CLAUDE.md` et des scripts sont mises à
jour dans le même lot si le plugin est inscrit. Le skill n'utilise aucun
stockage durable ; les copies BASE-008 sont présentes pour le contrat de
paquet, pas pour un accès aux données.

## Pièces et informations nécessaires

- Confirmation ou récapitulatif de commande ; capture de l'annonce si disponible.
- Identité du vendeur : nom, pays, vendeur direct ou vendeur tiers d'une place de marché.
- But de l'achat (privé, professionnel, mixte) et nom sur la facture.
- Date de commande ; date ou délai de livraison annoncé, ou absence d'indication.
- Mode de livraison : domicile, point relais, transporteur proposé par le vendeur ou choisi par l'acheteur.
- Suivi du transporteur, y compris un statut « livré » contesté.
- Paiement : montant, moyen, date, débit effectif.
- Échanges avec le vendeur ou la plateforme, avec leurs dates.

Sans pièce, le skill commence sur la déclaration de la personne, marquée
comme telle, et pose une question à la fois.

## Sortie attendue

1. Résumé en quelques phrases : ce qui est établi, ce qui manque, la démarche proposée.
2. Fiche de commande : chaque fait avec sa pièce source et son statut (prouvé, déclaré, inconnu).
3. Pièces à réunir et questions au vendeur.
4. Brouillon de réclamation écrite : faits, pièces, demande de livraison ou de remboursement. Aucun délai légal ni article cité sans source lue à la date des faits.
5. Prochaines étapes et interlocuteurs : vendeur d'abord ; médiation (CONSO-006, proposée) ; banque pour le paiement, tâche distincte (DOM-004).
6. Limites : ce que le skill n'a pas vérifié et ce qui changerait la réponse.

## Travail attendu

Créer `qualification-achat.md` selon le [découpage](../dom-001-annexes/dom-001-decoupage-consommation.md)
et l'appliquer avant toute réclamation :

- achat pour l'activité professionnelle → pas de brouillon « consommateur » ;
  orientation vers commercial avec les questions sur l'objet, l'effectif et
  le canal (protection particulière possible, à vérifier) ;
- vendeur particulier → orientation (CONSO-011, proposée) ;
- objet sectoriel (voyage, véhicule, travaux, contenu numérique) → orientation au secteur ;
- vendeur hors de France → fiche et orientation réservée (CONSO-007, proposée) ;
- colis retenu en douane → la question douanière va à DOM-009, la demande au vendeur reste ici ;
- faux site ou escroquerie suspectés → banque et pénal en tâches distinctes,
  sans conclure à l'infraction.

Charger la méthode locale BASE-005. Lire et citer les sources réellement
ouvertes dans `non-livraison.md`, avec version et date de lecture. Rédiger
pour une personne sans formation juridique (protocole USAGE-001).

## Références métier et sources à rechercher

Pistes à ouvrir et vérifier : Code de la consommation, article liminaire et
dispositions sur la livraison et le transfert des risques (piste L216-1 et
suivants) ; directive 2011/83/UE, articles sur la livraison et le transfert
du risque ; Code civil sur l'inexécution et la mise en demeure. DGCCRF comme
guide d'orientation, distinct du texte. Toute règle non lue reste réservée ;
aucune norme étrangère de remplacement.

## Critères d'acceptation
- [ ] N01 produit fiche, pièces manquantes et brouillon sans délai ni article non vérifié.
- [ ] N02 conserve les branches (vendeur tiers, pays, statut « livré ») et pose les questions utiles, sans conclusion sur la responsabilité.
- [ ] N03 n'emploie pas de brouillon « consommateur » et oriente vers commercial avec les questions sur la protection éventuelle.
- [ ] La sortie se comprend sans formation juridique, sans présumer d'abus ni garantir l'issue.
- [ ] Le paquet détaché fonctionne sans le checkout ni autre plugin ; copies communes identiques ; README limité à ce skill.
- [ ] N04 à N07 séparent remise, transfert du risque et résolution ; un remboursement non reçu est orienté vers CONSO-019.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : N01 — Casque audio commandé sur le site d'un vendeur français, date annoncée dépassée de trois semaines, carte débitée, deux relances sans réponse.
- Cas limite : N02 — Achat sur une place de marché à un vendeur tiers dont le pays est inconnu ; suivi « livré en point relais », colis jamais retiré.
- Cas limite : N03 — Plombier commandant un nettoyeur haute pression facturé à son entreprise, qui demande « la protection du consommateur ».
- Sans source lue : résultat partiel utile, règle réservée.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-001](../dom-001-annexes/dom-001-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Bien reçu défectueux ou incomplet, rétractation, service, voyage, contenu
numérique, véhicule, travaux, vente entre particuliers, contestation
bancaire, procédure judiciaire, indemnité chiffrée, envoi du courrier.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 25–30, 34, 37–40, 144 de la [matrice des besoins](../dom-001-annexes/dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Documenter instructions de remise, dépôt devant la porte, voisin autorisé ou non, signature contestée et relais déplacé. Distinguer transporteur proposé par le vendeur et transporteur extérieur mandaté par l’acheteur. Le statut informatique « livré » n’est pas traité comme une preuve suffisante par principe.

Ajouter à la sortie une chronologie de l’engagement de livraison et des demandes prouvées. Séparer réclamation, délai supplémentaire raisonnable à vérifier, résolution et demande de remboursement. Une date essentielle ou un refus de livrer allégué appelle la recherche des conditions permettant une autre séquence ; aucun délai standard ni droit de résolution automatique. Le remboursement après résolution documentée peut être suivi dans CONSO-019 ; aucune majoration calculée ici. Un colis reçu incomplet ou cassé va à CONSO-002.

- Cas limite : N04 — Colis devant la porte ou chez un voisin sans instruction fournie : conserver les branches et demander preuve de remise.
- Cas limite : N05 — Signature contestée et relais déplacé : comparer contrat, suivi et justificatif, sans désigner d’auteur de faux.
- Cas limite : N06 — Date d’un mariage annoncée avant commande, livraison manquée : vérifier caractère essentiel et conditions d’une résolution immédiate.
- Cas limite : N07 — Transporteur extérieur mandaté par l’acheteur : ne pas confondre avec un choix proposé dans le panier.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026 (historique)

Issue de DOM-001, sans implémentation. Préalable PILOTE-003 satisfait après
BASE-011 ; aucune tranche sélectionnée. Contrat commun : [découpage](../dom-001-annexes/dom-001-decoupage-consommation.md).

## Implémentation — 17 octobre 2026

Sélection par la demande de l'utilisateur « implémente la story conso-001 » :
création et inscription de `consumer-legal` `0.1.0`, avec le seul skill
`non-delivery-claim`. La demande autorise l'inscription prévue par le cadrage.
Le compte réel est désormais de 13 paquets et 136 skills, en tenant compte
de BNK-001 ajouté en parallèle ; le passage anticipé 12 → 13 n'était pas
l'état initial constaté de ce chantier (11 paquets, 134 skills).

Tous les fichiers du périmètre du paquet sont créés. La copie commune est
la version courante BASE-005 `1.2.0`, identique à la racine, plutôt que la
`1.0.0` mentionnée dans la proposition ancienne. Aucun profil, stockage durable,
agent, hook ou connecteur ajouté. Qualification commune et branches N01–N07
sont intégrées ; les autres CONSO restent proposées, sans commande annoncée.

Les sources lues, leurs bornes temporelles et les accès impossibles sont
consignés dans les références métier. L'article liminaire et L221-15 n'ont
pas pu être ouverts : conclusions dépendantes réservées. Le chapitre de
livraison, les repères civils, la directive via CELLAR et la fiche DGCCRF
ont été lus ; aucune veille exhaustive ou règle étrangère de remplacement.

Voir le [bilan par couche](conso-001-annexes/verification.md), les
[fixtures N01–N13](conso-001-annexes/pieces-fictives.md), le
[contrôle reproductible](conso-001-annexes/controles.py), les
[résultats du paquet](conso-001-annexes/resultats-paquet.json) et la
[trace CELLAR](conso-001-annexes/source-directive.json).

Les critères comportementaux ci-dessus restent ouverts : installation locale
jetable et schéma ne valent pas invocation du skill. Aucun compte authentifié
dans cette configuration, aucune authentification personnelle importée.
Scénarios N01–N13 et reformulation par un lecteur réel **non exécutés** ;
statut `a-verifier`, sans prétendre valider les sorties attendues.

## Reprise des tests client — 17 octobre 2026

N01–N13 : quinze sorties avec N04 porte/voisin et N07 extérieur/panier séparés. Défauts de sources et de provenance corrigés dans consumer-legal 0.1.2 ; le développement de certaines variantes par le nouvel exécuteur a aussi été corrigé. Ces sorties ne valident pas les fixtures propres ni la version finale, à rejouer.

La relecture est prise en charge par l'utilisateur et ne bloque pas la
clôture. Le statut reste `a-verifier` pour les défauts/rejeux et tests
non exécutés, après épuisement du quota annoncé jusqu'à 16 h 40
(Europe/Paris). Aucun critère métier non observé n'est déclaré réussi.

[Bilan transversal et commande de reprise](../../recette-2026-10-17.md).
