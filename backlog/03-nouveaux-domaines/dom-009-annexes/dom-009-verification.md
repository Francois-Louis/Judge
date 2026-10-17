# DOM-009 — Vérification documentaire du découpage

Parcours du **17 octobre 2026 (Europe/Paris)** par le rédacteur, sur les pièces
fictives décrites ci-dessous et les propositions du
[découpage](dom-009-decoupage-douanes.md). Il vérifie les propriétaires,
questions et limites documentaires ; aucun skill n'a été exécuté et aucune
consultation n'est résolue. Les scénarios métier des suites restent
**attendus, non exécutés**. Les [résultats statiques](dom-009-resultats.json)
ont une portée distincte de cette lecture.

## Dossier fictif A — achat expédié depuis un pays tiers

Pièces : confirmation d'achat d'un sac pour usage privé, vendeur domicilié
dans l'Union, suivi indiquant un départ de Chine puis « bloqué en douane »,
facture sans détail des frais. Destination métropolitaine ; aucun acte joint.

| Point relu | Routage | Informations à demander / réserve |
|---|---|---|
| Objet | DOU-001, dossier d'un envoi non accompagné pour un particulier. | Désignation, composition, quantité, trajet et dates ; détecter catégorie réglementée avant d'annoncer la tranche applicable. |
| Provenance et origine | Départ tiers observé dans le suivi, origine inconnue. | Fiche produit et preuve d'origine si pertinente ; domicile du vendeur et lieu d'expédition ne suffisent pas. |
| Blocage | Message du prestataire, pas d'acte douanier identifié. | Message complet, auteur, demande de pièces, déclaration et rôle du prestataire ; DOU-009 si acte officiel ensuite fourni. |
| Valeur et frais | Facture insuffisante pour arrêter valeur ou dette. | Paiement, devise, transport, assurance et frais privés détaillés ; aucun calcul. |
| Autres demandes | Vente DOM-001 ; prestation postale DOM-022 ou transport DOM-008 selon contrat. | Question précise sur livraison ou frais, sans transférer tout le dossier. |

**Constat :** DOU-001 produit un inventaire et des questions ; ni libération
promise ni taux déduit du prix ou de la mention « tout compris ».

## Dossier fictif B — envoi vers un territoire ultramarin

Pièces : bordereau portant seulement « outre-mer », récit d'un envoi familial
avec des biens achetés et usagés, demande de « la même formalité que pour la
métropole ». Commune destinataire et statut vente/cadeau inconnus.

| Point relu | Routage | Informations à demander / réserve |
|---|---|---|
| Sortie de première tranche | DOU-002. | Lieux exacts de départ, passage et destination, date et usage. |
| Territoires | Qualification douanière et fiscale séparée. | Aucune assimilation de tous les territoires ultramarins entre eux ni à un pays tiers. |
| Opération | Vente, cadeau ou transfert à qualifier. | Propriétaire, destinataire, facture ou inventaire et mode d'envoi ; pas de franchise depuis le seul lien familial. |
| Fiscalité autonome | DOM-011 selon question identifiée. | DOU-002 nomme la composante à vérifier sans établir tout le régime fiscal. |

**Constat :** le routage reste DOU-002 même avec un récit incomplet ; aucun
formulaire universel, seuil, taux ou délai n'est donné.

## Dossier fictif C — avis de contrôle ou perception notifié

Pièces : courrier numérisé dont la première page évoque un contrôle et une
somme réclamée, annexe manquante, date imprimée visible, réception inconnue ;
facture du prestataire contenant en plus des frais de dossier.

| Point relu | Routage | Informations à demander / réserve |
|---|---|---|
| Stade et urgence | DOU-009 avant dossier préparatoire. | Acte intégral, auteur, destinataire, réception, annexes et suite annoncée ; contact rapide adapté, sans calcul de délai. |
| Objets | Contrôle, dette, éventuelle sanction et frais privés séparés. | Ne pas lire tous les montants comme des droits dus ni la dette comme une infraction. |
| Fond de la dette | Questions de classement/origine/valeur identifiées puis réservées. | Déclaration, pièces et motifs ; DOU-006/007/008 comme propositions seulement. |
| Demande future | DOU-010 si remboursement demandé et paiement prouvé ; DOU-011 si remise demandée et état non payé établi. | Ni recevabilité ni suspension du recouvrement présumées ; pas d'appel automatique aux tâches absentes. |
| Pénal ou exécution | Avocat en droit douanier si sanction, retenue ou contentieux ; DOM-003 pour acte d'exécution distinct après qualification. | L'autorité émettrice n'est pas présentée comme conseil. Aucun recours universel ni défense improvisée. |

**Constat :** une notification fait sortir de DOU-001. Le dossier reçu ne
permet pas de conclure à une dette exigible ni de dater une échéance.

## Cas véhicules — points 45 et 191

| Pièces fictives et cas | Routage et questions | Limite retenue |
|---|---|---|
| V1 : facture d'un vendeur allemand, trajet réel incomplet, demande de « dédouanement tiers » | DOU-012 ; vérifier lieu de départ, statut et trajet, origine distincte, date et usage. | L'achat UE n'est pas renommé importation tierce depuis le seul récit ; aucun document douanier exigé automatiquement. Quitus DOM-011, immatriculation DOM-010. |
| V2 : véhicule expédié du Japon, facture et documents étrangers présents, aucune pièce de dédouanement | DOU-012 ; demander parcours, point d'entrée, déclaration/document effectivement reçu et rôle du représentant. | Ni dédouanement accompli ni infraction présumés ; VEH-019 garde la promesse contractuelle de remise, VEH-007 l'historique. |
| V3 : véhicule personnel tiers, « franchise déménagement » invoquée, résidence et usage incomplets | DOU-012 ; chronologie des résidences, propriété et usage, trajet, dates et justificatifs strictement utiles. | Conditions et texte exacts à vérifier ; aucune franchise acquise, aucun taux ni droit calculé. |

**Constat :** les trois cas ont un propriétaire documentaire unique sans
confondre douane, quitus, immatriculation et engagement contractuel.

## Autres limites relues

| Cas fictif | Résultat du parcours documentaire |
|---|---|
| Biens ramenés dans une valise | DOU-003 ; voyageur distinct de colis, aucun seuil de franchise mémorisé. |
| Stock importé pour revente | DOU-004 ; rôles et usage professionnel, pas DOU-001. |
| Vente exportée définitivement avec trajet incomplet | DOU-005 ; destination, biens et acteurs, aucune conformité export certifiée. |
| Produit vendu sous un nom vague | DOU-006 ; fiche technique requise, code réservé. |
| Expédition d'un entrepôt européen et préférence invoquée | DOU-007 ; production et preuve distinctes du pays d'expédition. |
| Facture en devise avec frais et facture rectifiée | DOU-008 ; pièces et postes séparés, pas de total juridiquement arrêté. |
| Avis et paiement couvrant plusieurs postes | DOU-010 ; rapprocher dette, paiements et objet demandé, remboursement non promis. |
| Droits non payés et simple difficulté de trésorerie | DOU-011 ; motif à établir, remise et facilité de paiement non assimilées. |
| Marchandise sanitaire, double usage, retenue pour contrefaçon ou personne retenue | Hors tranche ordinaire ; question spécialisée et aide humaine immédiate selon l'acte, aucune liste générique de formalités. |
| Source absente ou modèle américain joint | Fiche factuelle poursuivie, conclusion dépendante réservée ; aucun barème, formulaire ou délai étranger importé. |

## Acceptation et portée

| Critère DOM-009 | Élément relu |
|---|---|
| Domaine et frontières | Ligne douanes BASE-003 et tableau du découpage ; un plugin principal par tâche. |
| Hiérarchie et première tranche | Douze propositions DOU, tranche DOU-001 bornée au dossier d'achat privé tiers vers la métropole, exclusions explicites. |
| Stories relisibles | Entrées, sortie, source métier à rechercher, fichiers futurs et scénarios distincts dans chaque suite. |
| Autonomie | Paquet et références locaux prévus, aucun profil ni plugin voisin obligatoire ; aucun agent, connecteur ou hook justifié. |
| Bilan pilote et absence de lancement | PILOTE-003 terminé après BASE-011 ; dépendance dans chaque suite, choix d'extension toujours explicite. Aucun paquet créé. |

Les critères de cadrage sont satisfaits par ces livrables documentaires et
les contrôles statiques consignés. Aucune source juridique externe ouverte,
aucune version applicable validée, aucun montant ou délai calculé, aucune
installation, invocation, démarche externe ou validation juridique.
La relecture humaine est prise en charge par l'utilisateur selon AGENTS.md
du 17 octobre 2026 ; elle n'est pas déclarée effectuée. La compréhension par
un lecteur réel n'a pas été observée. Ces limites ne sont pas des contrôles
techniques en échec et ne maintiennent pas la story de cadrage ouverte.
