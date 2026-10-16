# DOM-008 — Vérification documentaire du découpage

Relecture du **16 octobre 2026** par l’agent de maintenance, sur des pièces
fictives. Elle suit le [découpage](dom-008-decoupage-transports.md) et les dix
propositions TPT. Aucun skill exécuté, droit conclu, délai, seuil ou montant
fourni ; ce parcours ne résout pas les consultations. Le
[relevé machine](dom-008-resultats.json) distingue les contrôles statiques.

## Dossier fictif A — vol annulé avec correspondance

- `A-confirmation` : Paris–Madrid–Lima, achat sur une même plateforme ;
  document commercial avec deux transporteurs, mais conditions de contrat
  absentes et transporteurs effectifs non établis.
- `A-avis` : premier segment annulé ; le voyageur demande « le remboursement
  et une indemnité pour tout le voyage » ; date de réception non fournie.
- `A-frais` : facture d’un hébergement et proposition d’un autre vol,
  sans preuve d’acceptation ni paiement déjà reçu.

| Point relu | Routage retenu | Informations à demander / conclusion réservée |
|---|---|---|
| Première tranche | TPT-001 détecte plusieurs segments et sort vers TPT-002. | Ne pas produire une réclamation de vol direct. |
| Contrat | Réservation unique ou contrats distincts inconnus. | Billets, confirmations complètes, conditions, vendeur et transporteur effectif de chaque segment ; même site insuffisant. |
| Champ | Départ, destination finale, segment touché et acteurs à cartographier. | Rattachement territorial et temporel à rechercher sans étendre automatiquement le régime à tous les segments. |
| Dates | Annulation déclarée, réception inconnue. | Avis daté, réception, horaires prévus/réels et fuseaux ; aucun calendrier confirmé. |
| Demandes | Remboursement, réacheminement, prise en charge et indemnisation séparés. | Choix déjà accepté, sommes reçues, justificatifs ; cumul et conditions réservés. |
| Sortie du cadrage | Fiche, carte des contrats à compléter, questions ciblées. | Brouillon futur seulement si qualification établie ; aucune créance annoncée. |

**Constat :** le scénario appartient à TPT-002 ; la première tranche garde
un incident simple. Assurance éventuelle → DOM-005 pour une question distincte.

## Dossier fictif B — retard ferroviaire

- `B-billet` : trajet régional puis train international, deux titres émis
  dans un même panier ; aucune preuve de billet direct.
- `B-horaires` : premier train retardé ; correspondance manquée ; seule
  l’heure de départ réelle est fournie.
- `B-garantie` : capture d’une garantie commerciale invoquée par le voyageur.

| Point relu | Routage retenu | Informations à demander / conclusion réservée |
|---|---|---|
| Domaine et mode | TPT-004, régime ferroviaire. | Aucun barème aérien appliqué. |
| Service | Segment régional et segment international distingués. | Entreprises, catégorie exacte, dates et règles de champ/exemptions à vérifier. |
| Contrat | Achat groupé sans billet direct établi. | Billets complets et conditions, qualification de chaque contrat avant de traiter la correspondance. |
| Retard | Départ seul documenté. | Heures prévues/réelles à destination et preuves ; ne pas calculer depuis le seul départ. |
| Garantie | Engagement commercial distinct des droits légaux. | Version des conditions et champ de la garantie, sans présumer qu’elle remplace les droits légaux. |
| Sortie du cadrage | Fiche, chronologie incomplète et pièces utiles. | Demandes distinctes à vérifier, aucune indemnité ni échéance calculée. |

**Constat :** mode, service et contrat sont tous nécessaires ; le même
panier n’efface pas les questions sur les billets et les correspondances.

## Dossier fictif C — bagage perdu lors d’un voyage à forfait

- `C-contrat` : contrat intitulé forfait comprenant vol et hôtel, avec
  organisateur, détaillant et compagnie distincts ; qualification à confirmer.
- `C-bagage` : étiquette d’enregistrement, constat à l’arrivée et message
  « bagage introuvable » ; aucune réclamation écrite ni date de remise.
- `C-demandes` : voyageur demandant « au voyagiste de tout rembourser » ;
  achats nécessaires documentés et assurance voyage possible.

| Point relu | Routage retenu | Informations à demander / conclusion réservée |
|---|---|---|
| Bagage | TPT-005, bagage aérien non remis ; perte déclarée, qualification juridique non acquise. | Itinéraire complet, transporteur effectif, dates de constat, remise éventuelle et réclamation. |
| Signalement | Constat reçu comme pièce, sans équivalence automatique avec réclamation. | Contenu du constat, échanges, preuve de réception ; exigences et délais propres à lire ultérieurement. |
| Forfait | TPT-006 pour les engagements de l’organisateur/détaillant. | Contrat complet et prestations ; le titre commercial ne suffit pas. |
| Deux objets | Transporteur pour le bagage, acteur du forfait pour ses obligations propres. | Pas de responsabilité collective ni de lettre universelle ; réparations et sommes reçues à rapprocher. |
| Assurance | DOM-005 pour une garantie distincte. | Conditions, déclaration et réponse de l’assureur seulement si ce volet est demandé. |
| Sortie du cadrage | Deux dossiers articulés, faits communs et pièces utiles. | Aucun remboursement intégral, plafond ou conversion promis ; pas de double réparation présumée. |

**Constat :** TPT-005 et TPT-006 gardent leurs objets. Si un seul skill est
livré à terme, l’autre objet est orienté sans appel à une commande absente.

## Cas limites et frontières relus

| Pièce ou demande fictive | Routage / question déterminante | Limite retenue |
|---|---|---|
| Voyageur annulant lui-même pour maladie | Point ouvert annulation personnelle ; garantie → DOM-005. | TPT-001 ne transforme pas ce récit en annulation par le transporteur. |
| Vol direct retardé, seule preuve du départ | TPT-003 ; preuve de l’arrivée et fuseaux demandés. | Aucun calcul d’indemnité. |
| Autobus local annulé, trajet partiel indiqué | TPT-008 ; service et distance pertinente à établir. | Aucun seuil inventé ni barème aérien. |
| Ferry annulé et tempête invoquée | TPT-009 ; champ, contrat et motif à documenter. | Aucune exonération globale déduite du seul mot « tempête ». |
| Croisière et escale supprimée | TPT-009 pour qualifier, TPT-006 si forfait établi. | Régime du ferry non étendu automatiquement. |
| Palette professionnelle abîmée sur route internationale | TPT-010 ; vente, transport, commission et assurance distingués. | Pas de régime passager ni de demande indemnitaire au fond. |
| Colis importé retenu avec un acte douanier | DOM-009 pour l’acte ; DOM-001 pour la vente au consommateur ; DOM-022 si prestation postale. | Le mot colis n’impose pas TPT-010. |
| Achat d’un véhicule ou facture de réparation | DOM-023. | Aucun régime de transport tiré de la présence d’un véhicule. |
| Assurance refusant une annulation | DOM-005 ; obligations du vendeur/transporteur isolées si pertinentes. | Le refus de garantie ne décide pas les droits envers le transporteur. |
| Relance sans preuve de réception | TPT-007 ; demander date, destinataire et preuve. | Aucune médiation déclarée recevable ni prescription calculée. |
| Modèle américain joint à une demande française | Source étrangère isolée ; trajet, contrat et sources propres à vérifier. | Aucune règle ni somme importée. |
| Voyageur à mobilité réduite bloqué | Besoin d’assistance qualifié en tête, interlocuteur humain du transporteur ; droits sectoriels à découper. | Aucun dossier médical complet ni couverture spécialisée annoncée. |

## Portée de la relecture

Les trois scénarios demandés ont un propriétaire et des questions ciblées ;
les cas limites séparent les modes, le fret et les voisins. Ce constat
porte sur des propositions documentaires et leur cohérence, par leur
rédacteur. Aucune source juridique externe ouverte, aucune consultation
résolue, aucun lecteur réel ou indépendant, aucune installation ou invocation
de skill. Les scénarios TPT restent **attendus, non exécutés** ; les futurs
lots doivent appliquer BASE-006 sur leurs sorties observées.
