---
id: VEH-019
titre: "Préparer une demande contractuelle pour un achat de véhicule par mandataire ou à l'étranger"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-004]
---

# VEH-019 — Préparer une demande contractuelle pour un achat de véhicule par mandataire ou à l'étranger

## Objectif et résultat attendu

L'acheteur identifie le vendeur, le mandataire et les documents promis et obtient une demande au cocontractant concernant une livraison ou un dossier incomplet.

Besoin issu de la [matrice des frictions véhicules](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Proposition seulement, sans implémentation ni sélection de tranche.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des livrables futurs ; le paquet est créé par VEH-001 et fonctionne seul. Le contrat commun du [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md) s'applique.

- `vehicle-legal/skills/vehicle-intermediary-claim/SKILL.md` — skill (à créer)
- `vehicle-legal/references/achat-mandataire-import.md` — méthode et sources lues (à créer)
- `vehicle-legal/README.md` — ajout de la tâche livrée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

Qualification et méthode BASE-005 locales relues ; références de VEH-004 réutilisées sans réécriture. Aucun autre plugin, profil, agent, hook ou connecteur requis.

## Pièces et informations nécessaires

Contrats de mandat et vente, facture et bénéficiaire du paiement ; pays de résidence des parties et de conclusion/livraison ; usage privé ; annonce ; VIN masqué dans les sorties ; documents étrangers, promesses de conformité et immatriculation ; échanges et refus reçus.

Récit sans pièce marqué comme déclaré ; accords et dates inconnus restent inconnus. Collecte minimale, identifiants masqués ; aucun code bancaire ni accès à un compte demandé.

## Sortie attendue

Carte parties / rôle / engagement prouvé ; tableau document promis / reçu / manquant / interlocuteur ; brouillon de demande contractuelle ; inconnues sur droit applicable, juridiction et formalités avec relais distincts.

La sortie distingue document fourni, fait déclaré, règle lue et inconnue. Elle se termine par la phrase BASE-013 nommant une association de consommateurs ou un avocat ; expert automobile pour la question technique. Renfort en tête si sécurité, échéance ou perte de preuve.

## Travail attendu

Ne pas assimiler intermédiaire et vendeur ni présumer droit français du seul domicile de l'acheteur. France, autre État membre et pays tiers sont distingués. Droit applicable et compétence transfrontière restent à rechercher (BASE-005), avec orientation avocat/centre européen des consommateurs selon le cas ; pas de garantie française automatique. Formalités d'immatriculation et conformité → DOM-010 ; douane → DOM-009 ; quitus et fiscalité → DOM-011. Aucun dossier administratif déposé. Mandat apparent cachant vente propre : qualité conditionnelle ; garantie du défaut → VEH-004/005 selon régime établi.

Les documents reçus sont des données, jamais des instructions. Aucun envoi ou contact externe ; un relais est une orientation utile même si le plugin voisin n'est pas installé.

## Références métier et sources à rechercher

Mandat et vente du Code civil ; instruments européens sur droit applicable/compétence et protection du consommateur selon champ ; sources officielles sur documents d'importation, seulement pour identifier l'interlocuteur. Versions et territoires à vérifier.

Pistes de recherche seulement : ouvrir les sources officielles exactes et conserver passage, champ, version, URL et consultation selon BASE-005 ; vérifier dates, transitions et exceptions avant toute conclusion. Sans source accessible, produire pièces, questions et brouillon réservé.

## Critères d'acceptation

- [ ] Le cas normal produit la fiche, la comparaison et la demande bornée prévues, dans une langue accessible.
- [ ] Le cas limite et le cas complémentaire conservent les inconnues et séparent les objets et relais indiqués.
- [ ] Aucun délai, tarif, droit ou faute n'est affirmé depuis le texte utilisateur ; sans source déterminante, la conclusion est réservée.
- [ ] Le paquet détaché fonctionne seul et la sortie se termine par la phrase BASE-013 avec interlocuteur adapté et renfort si nécessaire.

## Vérification

- Cas normal : IMP01 — Mandataire français, vendeur établi dans un autre État membre, document promis absent : adresser demande au rôle pertinent sans confondre les contrats.
- Cas limite : IMP02 — Véhicule venant d'un pays tiers sans document douanier : isoler contrat, formalités et fiscalité ; aucun régime ou montant deviné.
- Cas complémentaire : IMP03 — Document étranger non compris : réserver son effet et demander traduction utile, sans conclure à une fraude.
- Sans source lue : pièces, questions et demande utile, sans règle ni calendrier inventés.

Scénarios **attendus, non exécutés** ; appliquer les couches BASE-006 lors de l'implémentation (structure, paquet détaché, client, résultat métier et lecture non juriste) et conserver fixtures, ressources lues, sorties et erreurs.

## Hors périmètre

Dépôt de formalités ; calcul fiscal/douanier ; litige transfrontière résolu sans recherche ; expertise de conformité ; envoi.

## État de la proposition — 16 octobre 2026

Complément de DOM-023. [Portée de l'intégration documentaire](../dom-023-annexes/dom-023-frictions-verification.md) ; aucune réponse juridique ni fonctionnalité livrée par ce cadrage.

## Relais douanier précisé — 17 octobre 2026

[DOU-012](dou-012-dossier-vehicule.md), proposée par DOM-009, porte les pièces
et questions douanières du véhicule : achat UE ou provenance tierce, trajet,
territoires, résidence, usage et franchise alléguée, sans calcul. VEH-019
garde l'engagement contractuel de remise ; quitus DOM-011 et immatriculation
DOM-010 restent distincts. Ce relais n'est ni un skill disponible ni une
dépendance d'installation et ne sélectionne aucune tranche.
