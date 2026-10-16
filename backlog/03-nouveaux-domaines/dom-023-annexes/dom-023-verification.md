# DOM-023 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-023-decoupage-vehicules.md) et les
12 propositions VEH, pour vérifier l'orientation, les pièces à demander et le
résultat attendu. La story interdit de résoudre ces dossiers : aucun délai,
montant, durée de garantie ou droit n'est conclu. Le [relevé machine](dom-023-resultats.json)
consigne séparément les contrôles statiques.

## Dossier fictif G — opération facturée sans accord retrouvé

- `G-recit` : « J'ai laissé ma voiture pour la vidange, le garage a aussi
  changé les plaquettes et me les fait payer. Il dit m'avoir appelé, je ne
  m'en souviens pas. »
- `G-pieces` : bon de dépôt mentionnant « vidange » ; facture avec deux
  lignes ; aucun devis ; journal d'appels montrant un appel bref du garage le
  jour du dépôt ; véhicule rendu, facture payée « pour récupérer la voiture ».

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `vehicle-legal`, VEH-001. | — |
| Point d'entrée | Phrase courante « il a fait des travaux que je n'ai pas demandés » reconnue sans vocabulaire juridique. | — |
| Qualification | Garage professionnel, véhicule d'un particulier, usage privé déclaré ; prestation de réparation et d'entretien. | Usage professionnel éventuel, à confirmer. |
| Accord | Vidange : bon de dépôt. Plaquettes : appel établi par le journal, contenu inconnu ; ni accord retenu ni refus établi. | Message ou trace écrite côté garage ; mention d'un accord sur la facture ou l'ordre de réparation. |
| Tableau | Deux lignes ; la seconde sans devis ni accord écrit retrouvé ; montants recopiés. | — |
| Paiement | Paiement fait pour récupérer le véhicule, noté comme fait ; effet d'un paiement sous réserve non affirmé. | Mention de réserve écrite ou non. |
| Pièces remplacées | Restitution des anciennes plaquettes demandée dans le brouillon, sans conclusion sur leur état. | — |
| Sortie | Tableau, brouillon de demande d'explication, information préalable et forme de l'accord réservées. | Textes sur l'information préalable et le devis à lire. |
| Avertissement | Phrase BASE-013 nommant une association de consommateurs puis le médiateur du secteur. | — |

**Constat :** VEH-001 suffit ; le garage n'est pas présumé fautif, l'appel
n'est ni transformé en accord ni écarté, aucun remboursement n'est promis.

## Dossier fictif H — panne d'une voiture d'occasion peu après l'achat

Le même récit est suivi avec deux pièces de vente différentes pour éprouver
la séparation des régimes.

- `H-recit` : « Trois semaines après l'achat, la voiture fait un bruit
  énorme et le garage parle de la boîte de vitesses. »
- `H1-pieces` : facture d'un professionnel de l'automobile, garantie
  commerciale d'une société tierce, contrôle technique remis.
- `H2-pieces` : certificat de cession signé par un particulier, annonce sur
  une plateforme, contrôle technique remis, reçu de virement.

| Point relu | H1 — vendeur professionnel | H2 — vendeur particulier |
|---|---|---|
| Tâche | VEH-004. | VEH-005 (arbitrage à confirmer : suite de CONSO-011 si la décision est étendue aux véhicules). |
| Qualité du vendeur | Établie par la facture. | Particulier déclaré ; indices à relever (nombre d'annonces, mentions) ; requalification conditionnelle vers VEH-004. |
| Voies à examiner | Garantie légale de conformité, garantie commerciale du tiers, vices cachés ; garant de la garantie commerciale lu sur le document. | Délivrance conforme et vices cachés ; aucune garantie de la consommation appliquée. |
| Durées et présomptions | Réservées : date de remise à prouver, textes à lire. | Réservées ; clause d'exclusion éventuelle ni validée ni écartée. |
| Question technique | Antériorité de la panne : question ouverte, expert automobile (VEH-010). | Même question ; connaissance du défaut par le vendeur non supposée. |
| Pièces à réunir | Facture, bon de commande, document de garantie, diagnostic, devis. | Annonce, cession, contrôle technique, échanges, diagnostic. |
| État à conserver | Ne pas faire réparer avant examen contradictoire, sans affirmer d'obligation. | Idem. |
| Relais | Crédit lié → DOM-004 ; garant tiers → VEH-011 si constructeur. | Escroquerie alléguée → DOM-002 ; protection de plateforme → CONSO-018. |
| Sortie | Tableau des voies, brouillon au vendeur. | Fondements civils, brouillon au vendeur. |

**Constat :** les deux régimes ne sont pas confondus ; la qualité du vendeur
est établie avant toute voie ; aucune annulation ni reprise n'est promise.

## Dossier fictif L — loueur réclamant des dommages au retour

- `L-recit` : « J'ai rendu la voiture de location à l'agence de l'aéroport
  tôt le matin, déposé les clés dans la boîte. Une semaine plus tard, on me
  prélève des frais pour une jante rayée. »
- `L-pieces` : contrat de location avec franchise et option de rachat non
  souscrite ; état de départ signé sans mention de la jante ; aucune photo au
  retour ; courriel du loueur avec deux photos et une estimation ; débit sur
  la carte.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | VEH-006 ; location courte durée, pas VEH-009. | — |
| États | Départ signé sans la jante ; retour sans état contradictoire, noté comme fait ; origine du dommage non présumée. | Photos de départ éventuelles du locataire ; heure et conditions du constat par le loueur. |
| Justificatifs | Estimation, pas facture ; demande de facture et de photos datées dans le brouillon. | Facture de réparation effective. |
| Contrat | Franchise et procédure de constat à lire ; aucune clause qualifiée d'abusive. | Clauses applicables, source à lire. |
| Prélèvement | Objet distinct : DOM-004 (BNK-001 ou BNK-016 selon l'opération). | Nature exacte de l'opération bancaire. |
| Assurance | Garantie de la carte de paiement → DOM-005, sans affirmer qu'elle joue. | Conditions de la carte. |
| Sortie | Tableau des états, brouillon de réponse au loueur demandant justificatifs. | — |

**Constat :** contrat, preuve des états et prélèvement restent trois
questions distinctes ; le loueur n'est pas présumé abusif ni le locataire
responsable.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| Garage refusant de rendre la voiture tant que la facture n'est pas payée | VEH-002 en premier, VEH-001 pour la facture ; renfort en tête. |
| Voiture enlevée sur la voie publique, frais de garde réclamés | Fourrière → DOM-010 ; VEH-002 seulement pour une rétention par un garage. |
| Facture de garage réglée en partie par l'assureur, franchise contestée | Facture et accords → VEH-001 ; franchise et garantie → DOM-005 (INS-004). |
| Accident pendant la location, conducteur blessé | Blessure → DOM-035 ; sinistre → DOM-005 ; dommages au véhicule loué → VEH-006 seulement pour la réclamation du loueur. |
| Amende reçue après la vente du véhicule | DOM-002 (CRIM-005) ; VEH-012 seulement si l'acheteur réclame aussi. |
| Compteur soupçonné d'avoir été modifié | VEH-004 ou VEH-005 pour la demande ; plainte → DOM-002 ; aucun fait tenu pour établi. |
| Véhicule utilitaire acheté pour une activité d'artisan | Qualification conditionnelle ; orientation commercial ; DOM-039 pour le statut. |
| Freins défaillants juste après une réparation | Sécurité en tête : ne pas circuler ; puis VEH-003 et VEH-010. |
| Voiture achetée en Allemagne par un mandataire | Point ouvert du découpage ; aucune story. |
| Trottinette électrique en panne sous garantie | Point ouvert du découpage ; en attendant, CONSO-002 pour un bien de consommation. |
| Saisie du véhicule par un commissaire de justice | DOM-003 (ENF-011) ; rien ici. |
| Offre de crédit pour l'achat d'une voiture | DOM-004 (BNK-005) ; VEH-007 pour la revue du bon de commande. |
| Fin de LOA avec frais de remise en état et contestation du coût du crédit | VEH-009 pour la restitution ; DOM-004 pour le financement. |
| Litige véhicule pendant que vehicle-legal n'est pas livré | CONSO-014 : règles générales, règles sectorielles annoncées comme non examinées. |

## Couverture des critères de la story

| Critère DOM-023 | Où il est traité |
|---|---|
| Stories avec entrées, sortie, pièces, limites et scénarios | Sections dédiées des 12 propositions, contrôlées par le relevé. |
| Partir du problème sans connaître le code | Table des points d'entrée du découpage ; dossier G. |
| Références métier, autonomie de paquetage, frontières | Contrat d'installation, références possédées par VEH-001, VEH-004 et VEH-006 ; table des frontières ; ligne de la matrice BASE-003. |
| Régimes non confondus | Garde-fou des quatre régimes ; VEH-004, VEH-005, VEH-006 et VEH-001 séparés ; dossier H. |
| Pas de présomption contre l'autre partie, pas de promesse | Garde-fous ; critères de VEH-001, VEH-004, VEH-006 et VEH-012 ; constats G, H et L. |
| Implémentations après PILOTE-003, aucune adaptation lancée | PILOTE-003 terminée ; aucun fichier sous `vehicle-legal/` ; marketplace inchangé. |

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles et textes cités sont des pistes de recherche
issues de la connaissance de l'agent, pas des règles vérifiées. Aucun délai,
durée de garantie ou montant établi, aucun skill créé ou exécuté, aucun
paquet installé, aucun lecteur réel ou indépendant, aucun envoi. Le
préalable PILOTE-003 est satisfait après BASE-011 ; aucune tranche n'est
sélectionnée par ce cadrage. L'arbitrage sur la vente entre particuliers
d'un véhicule reste à confirmer par l'utilisateur.
