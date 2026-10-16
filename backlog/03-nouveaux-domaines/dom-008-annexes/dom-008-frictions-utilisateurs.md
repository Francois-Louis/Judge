# DOM-008 — Frictions des voyageurs et propriétaires des réponses

Intégration du **16 octobre 2026 (Europe/Paris)** des 128 points du
[texte utilisateur](../sources/transports-frictions-2026-10-16.txt), conservé
à l’octet près. Le texte se présente comme un état du droit vérifié ; cette
mention appartient à la contribution reçue et n’est pas une validation du dépôt.
Ses liens de favicon et mentions « +N » ne permettent pas de vérifier ses règles.

Les dix suites initiales sont précisées et douze suites TPT-011 à TPT-022
ajoutées, toutes `proposee`. La première tranche TPT-001 reste inchangée.
Un propriétaire désigne un travail futur ; un renvoi vers un cadrage signale
une tâche au fond à découper, jamais une fonctionnalité déjà livrée.
Voir la [vérification](dom-008-frictions-verification.md) pour la portée.

## Matrice des 128 points

| Point | Friction fournie | Propriétaire principal, puis relais éventuels | Réponse observable à prévoir |
|---|---|---|---|
| 1 | Billet acheté mais train supprimé | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Choix remboursement/réacheminement, avoir et décision déjà acceptée distingués. |
| 2 | Correspondance vendue sans véritable protection | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Qualification billet direct/contrats indépendants avant toute garantie. |
| 3 | Correspondance ratée à cause du premier train | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Segments, retard initial et protection de la correspondance établis ou réservés. |
| 4 | Billet marqué « non remboursable » | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Annulation du service séparée de la renonciation personnelle et du tarif. |
| 5 | Billet devenu beaucoup plus cher après un échange | [TPT-011](../suites/tpt-011-billet-ferroviaire.md) | Frais d’échange et différence tarifaire rapprochés de l’écran accepté. |
| 6 | Achat à un intermédiaire | [TPT-011](../suites/tpt-011-billet-ferroviaire.md), [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Vendeur et transporteur identifiés selon erreur de vente ou incident du service. |
| 7 | Mauvaise date, mauvaise gare ou mauvais nom | [TPT-011](../suites/tpt-011-billet-ferroviaire.md) | Erreur de date, gare ou identité qualifiée ; demande de correction ciblée. |
| 8 | Réduction achetée sans justificatif valable | [TPT-011](../suites/tpt-011-billet-ferroviaire.md), [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Justificatif de réduction vérifié ; PV traité par son circuit distinct. |
| 9 | Billet électronique inaccessible | [TPT-011](../suites/tpt-011-billet-ferroviaire.md), [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Incident de présentation documenté sans assimiler preuve d’achat et titre valable. |
| 10 | Bagage jugé non conforme à bord | [TPT-011](../suites/tpt-011-billet-ferroviaire.md), [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Conditions bagage datées et frais rapprochés ; contestation du PV séparée. |
| 11 | Retard insuffisamment indemnisé | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Retard à destination, champ et garantie légale/commerciale vérifiés. |
| 12 | Absence de proposition de réacheminement | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Solutions communiquées et choix du passager documentés avant demande. |
| 13 | Train annulé et voyageur abandonné en gare | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Assistance et dépenses nécessaires distinguées de l’indemnisation. |
| 14 | Aucun réacheminement communiqué | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Chronologie des propositions et trajet de substitution ; régime et coûts à vérifier. |
| 15 | Refus d'indemnisation pour « circonstances exceptionnelles » | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Motif d’exonération prouvé et effets par demande recherchés. |
| 16 | Retards répétés sur une ligne utilisée quotidiennement | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Abonnement, retards récurrents et mécanisme de compensation daté identifiés. |
| 17 | Retard d'un TER traité comme celui d'un TGV | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Service régional, exemptions et billet direct qualifiés sans régime TGV automatique. |
| 18 | Remboursement automatiquement proposé en bon d'achat | [TPT-004](../suites/tpt-004-incident-ferroviaire.md) | Argent, bon d’achat et garantie commerciale séparés. |
| 19 | Titre payé, mais non validé | [TPT-012](../suites/tpt-012-contester-pv-transport.md), [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Validation du titre et contestation du PV distinguées. |
| 20 | Validation sans confirmation | [TPT-012](../suites/tpt-012-contester-pv-transport.md), [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Confirmation de validation et preuve du dysfonctionnement reconstituées. |
| 21 | Ticket chargé sur téléphone mais indisponible | [TPT-013](../suites/tpt-013-service-titre-urbain.md), [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Chargement, activation et présentation numérique vérifiés ; PV séparé. |
| 22 | Correspondance hors du périmètre du ticket | [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Réseau, zones, durée et correspondance du titre identifiés. |
| 23 | Abonnement expiré le premier jour du mois | [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Période d’activation rapprochée de l’achat et du paiement. |
| 24 | Ticket au tarif réduit sans justificatif | [TPT-012](../suites/tpt-012-contester-pv-transport.md), [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Réduction et justificatif au contrôle examinés avant argument. |
| 25 | Titre nominatif utilisé par un proche | [TPT-013](../suites/tpt-013-service-titre-urbain.md), [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Caractère nominatif/transférable vérifié sans tenir paiement pour autorisation. |
| 26 | Amende dressée malgré un automate ou un valideur défectueux | [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Matériel, heure, photos et signalement au réseau joints au dossier PV. |
| 27 | Contrôle à la sortie du réseau | [TPT-012](../suites/tpt-012-contester-pv-transport.md), [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Périmètre de contrôle et durée de validité du titre recherchés. |
| 28 | Erreur d'identité ou de lieu sur un procès-verbal | [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Erreur matérielle et identité contestée distinguées sans nullité automatique. |
| 29 | Amende payée dans la précipitation pour éviter des complications | [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Quittance et effets procéduraux du paiement vérifiés avant recours. |
| 30 | Amende laissée sans réponse | [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Stade du PV, événement, acte requis et autorité déterminés ; majoration orientée. |
| 31 | Réclamation effectuée uniquement par téléphone | [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Texte de contestation et preuve de dépôt conservés ; appel seul signalé comme preuve insuffisante. |
| 32 | Médiateur saisi trop tard | [TPT-012](../suites/tpt-012-contester-pv-transport.md) | Médiation PV distincte du commercial ; recevabilité et calendrier vérifiés sans suspension présumée. |
| 33 | Bus passé en avance | [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Horaire prévu et passage constaté comparés avec preuves datées. |
| 34 | Bus qui ne s'arrête pas malgré la présence de voyageurs | [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Ligne, véhicule et présence à l’arrêt documentés pour réclamation. |
| 35 | Dernier métro ou bus supprimé sans solution | [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Suppression du dernier service et frais justifiés sans taxi automatiquement remboursé. |
| 36 | Abonnement mensuel maintenu malgré de fortes perturbations | [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Abonnement et campagne de dédommagement rapprochés des critères datés. |
| 37 | Escalator, ascenseur ou accès PMR durablement indisponible | [TPT-019](../suites/tpt-019-assistance-pmr-transport.md) | Accès indisponible et besoin fonctionnel documentés ; solution accessible demandée. |
| 38 | Accident, chute ou blessure dans un véhicule ou une station | [DOM-035](../dom-035-responsabilite-dommages.md) | Constat, témoins et exploitant ; sécurité et orientation corporelle, tâche au fond à découper. |
| 39 | Prix d'appel trompeur | [TPT-014](../suites/tpt-014-billet-aerien-frais.md) | Prix d’appel, frais obligatoires et options consenties comparés. |
| 40 | Bagage cabine facturé au dernier moment | [TPT-014](../suites/tpt-014-billet-aerien-frais.md) | Conditions cabine datées, dimensions et supplément documentés. |
| 41 | Supplément pour enregistrement à l'aéroport | [TPT-014](../suites/tpt-014-billet-aerien-frais.md) | Échéance d’enregistrement, information et frais vérifiés. |
| 42 | Correction d'une faute de frappe facturée au prix fort | [TPT-014](../suites/tpt-014-billet-aerien-frais.md) | Rectification d’identité et transfert de billet séparés. |
| 43 | Bagage à main refusé à la porte d'embarquement | [TPT-014](../suites/tpt-014-billet-aerien-frais.md) | Refus du bagage en porte et règle tarifaire rapprochés des preuves. |
| 44 | Vol aller manqué entraînant l'annulation du retour | [TPT-014](../suites/tpt-014-billet-aerien-frais.md) | Clause no-show et notification sur le retour examinées sans nullité automatique. |
| 45 | Deux vols vendus avec une correspondance non garantie | [TPT-002](../suites/tpt-002-annulation-correspondance.md), [TPT-003](../suites/tpt-003-retard-aerien.md) | Carte des contrats/segments ; correspondance indépendante non garantie par défaut. |
| 46 | Billet non remboursable présenté comme totalement perdu | [TPT-022](../suites/tpt-022-taxes-vol-non-effectue.md) | Ventilation tarif/taxes/redevances ; seule restitution justifiée demandée. |
| 47 | Assurance annulation présentée comme couvrant tous les motifs | [DOM-005](../dom-005-assurance.md) | Garantie et exclusions vers INS-004/001 selon demande ; aucune couverture tous motifs présumée. |
| 48 | Vol annulé avec remboursement imposé | [TPT-001](../suites/tpt-001-annulation-vol-direct.md) | Remboursement imposé et droit au réacheminement examinés séparément. |
| 49 | Réacheminement limité aux vols de la même compagnie | [TPT-001](../suites/tpt-001-annulation-vol-direct.md) | Options comparables, autres transporteurs et frais documentés. |
| 50 | Indemnisation forfaitaire jamais proposée spontanément | [TPT-001](../suites/tpt-001-annulation-vol-direct.md) | Champ et conditions d’indemnisation vérifiés avant barème ou chiffrage. |
| 51 | Retard de trois heures sous-estimé | [TPT-003](../suites/tpt-003-retard-aerien.md) | Arrivée finale, trajet et seuils propres au retard vérifiés. |
| 52 | Excuse générique de mauvais temps | [TPT-001](../suites/tpt-001-annulation-vol-direct.md), [TPT-003](../suites/tpt-003-retard-aerien.md) | Motif météo et lien causal demandés ; aucune exonération sur réponse générique. |
| 53 | Grève utilisée comme justification universelle | [TPT-001](../suites/tpt-001-annulation-vol-direct.md), [TPT-003](../suites/tpt-003-retard-aerien.md) | Auteur de la grève et circonstances distingués ; effets à vérifier. |
| 54 | Hôtel et repas non proposés | [TPT-001](../suites/tpt-001-annulation-vol-direct.md), [TPT-003](../suites/tpt-003-retard-aerien.md) | Assistance examinée séparément du motif d’exonération indemnitaire. |
| 55 | Surréservation ou surbooking | [TPT-015](../suites/tpt-015-refus-embarquement-aerien.md) | Refus volontaire/involontaire, présentation et motif qualifiés avant demandes. |
| 56 | Proposition d'un bon d'achat à la place de l'argent | [TPT-001](../suites/tpt-001-annulation-vol-direct.md) | Avoir, accord et paiement en argent distingués. |
| 57 | Vol décalé à une heure très différente | [TPT-001](../suites/tpt-001-annulation-vol-direct.md), [TPT-003](../suites/tpt-003-retard-aerien.md) | Modification d’horaire qualifiée à partir des avis ; avance non traitée comme simple retard. |
| 58 | Valise absente à l'arrivée | [TPT-005](../suites/tpt-005-bagage-aerien.md) | PIR, référence, étiquette et signalement joints ; PIR distinct de la réclamation écrite. |
| 59 | Bagage endommagé | [TPT-005](../suites/tpt-005-bagage-aerien.md) | Réception, dommage et notification écrite documentés ; délai vérifié. |
| 60 | Bagage livré en retard | [TPT-005](../suites/tpt-005-bagage-aerien.md) | Remise tardive, écrit et dépenses nécessaires rapprochés. |
| 61 | Valise définitivement perdue | [TPT-005](../suites/tpt-005-bagage-aerien.md) | Perte qualifiée, inventaire et valeurs justifiées sans indemnité égale au prix neuf présumée. |
| 62 | Remboursement forfaitaire arbitraire des bagages | [TPT-005](../suites/tpt-005-bagage-aerien.md) | Calcul demandé, dommage prouvé et plafond de responsabilité séparés. |
| 63 | Réclamation adressée uniquement à l'agence de réservation | [TPT-001](../suites/tpt-001-annulation-vol-direct.md), [TPT-003](../suites/tpt-003-retard-aerien.md), [TPT-005](../suites/tpt-005-bagage-aerien.md) | Transporteur effectif et rôle de l’agence identifiés pour l’obligation concernée. |
| 64 | Action en justice engagée sans respecter la procédure | [TPT-007](../suites/tpt-007-relance-transporteur.md) | Procédure aérienne récente signalée comme recherche prioritaire ; juge et acte vers contentieux. |
| 65 | Plainte auprès de la DGAC confondue avec une action en indemnisation | [TPT-007](../suites/tpt-007-relance-transporteur.md) | Signalement DGAC et demande individuelle d’indemnisation séparés. |
| 66 | Autocar annulé sans proposition de solution | [TPT-008](../suites/tpt-008-incident-autocar.md) | Service et champ qualifiés avant choix remboursement/réacheminement. |
| 67 | Départ retardé de plus de deux heures | [TPT-008](../suites/tpt-008-incident-autocar.md) | Retard au départ et défaut de choix documentés ; indemnisation additionnelle conditionnelle. |
| 68 | Car parti avant l'heure affichée | [TPT-008](../suites/tpt-008-incident-autocar.md) | Départ anticipé et qualification d’annulation recherchés sur source applicable. |
| 69 | Arrêt déplacé sans information suffisante | [TPT-008](../suites/tpt-008-incident-autocar.md) | Arrêt initial, modification et information reçue comparés. |
| 70 | Autocar qui ne s'arrête pas | [TPT-008](../suites/tpt-008-incident-autocar.md) | Présence au bon arrêt, horaire et service documentés. |
| 71 | Correspondance ratée entre deux autocars | [TPT-008](../suites/tpt-008-incident-autocar.md) | Même contrat ou billets indépendants établis ; régime ferroviaire écarté. |
| 72 | Voyageur laissé de nuit dans une gare routière | [TPT-008](../suites/tpt-008-incident-autocar.md) | Durée prévue, attente et assistance recherchées dans le champ qualifié. |
| 73 | Bagage disparu dans la soute | [TPT-020](../suites/tpt-020-bagage-autocar.md) | Preuve de dépôt en soute, disparition et inventaire pour réclamation distincte. |
| 74 | Bagage refusé ou supplément imprévu | [TPT-020](../suites/tpt-020-bagage-autocar.md) | Franchise, dimensions, refus et supplément vérifiés selon contrat. |
| 75 | Réclamation envoyée trop tard | [TPT-008](../suites/tpt-008-incident-autocar.md), [TPT-007](../suites/tpt-007-relance-transporteur.md) | Réclamation et réception datées ; délai propre au service à vérifier. |
| 76 | Taxi refusant la carte bancaire | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Règle de paiement taxi vérifiée et refus documenté. |
| 77 | Compteur non enclenché | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Compteur, type de course et réglementation locale identifiés. |
| 78 | Suppléments injustifiés | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Suppléments comparés aux montants autorisés à la date et au lieu. |
| 79 | Course dans un aéroport à tarif forfaitaire réglementé | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Itinéraire et forfait local aéroport vérifiés avant chiffrage. |
| 80 | Refus de délivrer une facture | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Demande de note et obligation applicable identifiées sans seuil recopié de mémoire. |
| 81 | Taxi empruntant volontairement un itinéraire anormal | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Trajet réel, justification et prix comparés sans exiger toujours le plus court. |
| 82 | Faux taxi à la sortie d'une gare ou d'un aéroport | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md), [DOM-002](../dom-002-police-penal.md) | Identité du service et preuves ; sécurité et relais pénal sans confrontation. |
| 83 | Faux VTC usurpant une réservation | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md), [DOM-002](../dom-002-police-penal.md) | Réservation, plaque et identité comparées ; sécurité avant contestation. |
| 84 | Majoration dynamique VTC mal comprise | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Prix VTC libre et transparence/consentement séparés ; majoration non abusive par principe. |
| 85 | Course VTC facturée malgré une annulation par le conducteur | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Auteur de l’annulation, notifications et frais rapprochés. |
| 86 | Frais d'attente ou de non-présentation injustifiés | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Point contractuel, présence, appels et attente reconstitués. |
| 87 | Course terminée dans l'application alors que le trajet continue, ou inversement | [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Fin informatique et fin réelle de la course comparées pour correction. |
| 88 | Taxi conventionné confondu avec VTC | [DOM-012](../dom-012-protection-sociale.md), [TPT-016](../suites/tpt-016-reclamation-taxi-vtc.md) | Conventionnement, prescription et mode distingués ; remboursement médical à découper. |
| 89 | Traversée annulée et bon d'achat imposé | [TPT-009](../suites/tpt-009-incident-maritime.md) | Choix remboursement/réacheminement et avoir examinés selon traversée. |
| 90 | Départ retardé de plus de 90 minutes | [TPT-009](../suites/tpt-009-incident-maritime.md) | Retard au départ et assistance séparés de l’indemnité d’arrivée. |
| 91 | Indemnisation du retard à l'arrivée ignorée | [TPT-009](../suites/tpt-009-incident-maritime.md) | Durée prévue et arrivée réelle ; seuils et proportion vérifiés. |
| 92 | Frais d'hôtel après une annulation | [TPT-009](../suites/tpt-009-incident-maritime.md) | Frais terrestres, plafonds et effet propre de la météo sur l’hébergement vérifiés. |
| 93 | Véhicule endommagé pendant la traversée | [TPT-021](../suites/tpt-021-dommage-bien-maritime.md) | État du véhicule, constat et notification ; régime du dommage qualifié. |
| 94 | Dégradation d'un bagage non signalée | [TPT-021](../suites/tpt-021-dommage-bien-maritime.md) | Type de bagage, découverte et notification ; délai propre au dommage recherché. |
| 95 | Réclamation maritime tardive | [TPT-009](../suites/tpt-009-incident-maritime.md), [TPT-007](../suites/tpt-007-relance-transporteur.md) | Plainte perturbation et réception séparées de la notification dommage et de la prescription. |
| 96 | Conducteur annulant à la dernière minute | [TPT-017](../suites/tpt-017-reclamation-covoiturage.md) | Annulation du conducteur, sommes et conditions de plateforme rapprochées. |
| 97 | Conducteur demandant un supplément en espèces | [TPT-017](../suites/tpt-017-reclamation-covoiturage.md) | Supplément hors réservation et messages joints à la demande. |
| 98 | Trajet annoncé puis fortement modifié | [TPT-017](../suites/tpt-017-reclamation-covoiturage.md) | Trajet convenu et modification comparés avant qualification du manquement. |
| 99 | Passager abandonné en cours de route | [TPT-017](../suites/tpt-017-reclamation-covoiturage.md) | Sécurité, lieu de dépose et engagements documentés ; aide humaine si besoin. |
| 100 | Faux covoiturage masquant du transport professionnel clandestin | [TPT-017](../suites/tpt-017-reclamation-covoiturage.md) | Partage de frais et activité professionnelle alléguée qualifiés sans automatisme. |
| 101 | Covoiturage confondu avec transport professionnel | [TPT-017](../suites/tpt-017-reclamation-covoiturage.md) | Qualité des parties vérifiée ; aucun régime autocar transposé entre particuliers. |
| 102 | Assurance mal comprise lors d'un accident | [DOM-005](../dom-005-assurance.md), [DOM-035](../dom-035-responsabilite-dommages.md) | Accident et couverture obligatoire/complémentaire distingués ; garantie et dommage vers tâches à qualifier. |
| 103 | Location qui continue après restitution | [TPT-018](../suites/tpt-018-facturation-libre-service.md) | Restitution, clôture et facturation comparées grâce aux preuves. |
| 104 | Véhicule déclaré mal stationné | [TPT-018](../suites/tpt-018-facturation-libre-service.md) | Photo et règle locale de stationnement rapprochées du grief. |
| 105 | Véhicule prétendument dégradé après utilisation | [TPT-018](../suites/tpt-018-facturation-libre-service.md) | État avant/après, imputabilité et chiffrage du dommage demandés. |
| 106 | Préautorisation bancaire confondue avec un débit | [TPT-018](../suites/tpt-018-facturation-libre-service.md), [DOM-004](../dom-004-banque.md) | Préautorisation et débit séparés ; litige bancaire orienté distinctement. |
| 107 | Application qui impose un stationnement à un endroit inaccessible ou non autorisé | [TPT-018](../suites/tpt-018-facturation-libre-service.md) | Erreur de localisation et échange support documentés sans stationnement illicite conseillé. |
| 108 | Facturation à la minute poursuivie pendant une panne | [TPT-018](../suites/tpt-018-facturation-libre-service.md) | Panne, signalement et durée facturée rapprochés. |
| 109 | Abonnement renouvelé automatiquement | [TPT-018](../suites/tpt-018-facturation-libre-service.md) | Offre, échéance et résiliation d’abonnement isolées de la course contestée. |
| 110 | Assurance présentée comme incluse | [DOM-005](../dom-005-assurance.md), [TPT-018](../suites/tpt-018-facturation-libre-service.md) | Garantie annoncée, exclusions et franchise vérifiées sans assurance universelle. |
| 111 | Assistance PMR refusée faute de réservation suffisamment anticipée | [TPT-019](../suites/tpt-019-assistance-pmr-transport.md) | Préavis et demande tardive examinés mode par mode, sans délai universel. |
| 112 | Refus d'embarquement fondé uniquement sur le handicap | [TPT-019](../suites/tpt-019-assistance-pmr-transport.md), [DOM-029](../dom-029-discriminations.md) | Motif de refus et exceptions documentés ; discrimination au fond à découper. |
| 113 | Fauteuil roulant endommagé ou perdu | [TPT-019](../suites/tpt-019-assistance-pmr-transport.md) | Fauteuil, constat et régime sectoriel ; remplacement temporaire et réparation à rechercher. |
| 114 | Accompagnant facturé alors que sa présence est imposée pour la sécurité | [TPT-019](../suites/tpt-019-assistance-pmr-transport.md) | Accompagnant imposé et régime de gratuité vérifiés selon mode. |
| 115 | Taxi ou VSL médical facturant des prestations contestables | [DOM-012](../dom-012-protection-sociale.md) | Prescription, facture et conventionnement ; facturation médicale à découper. |
| 116 | Remboursement de transport médical refusé | [DOM-012](../dom-012-protection-sociale.md) | Refus CPAM, notification et accord préalable ; recours social à découper. |
| 117 | Absence de preuve d'un retard | [TPT-001](../suites/tpt-001-annulation-vol-direct.md), [TPT-004](../suites/tpt-004-incident-ferroviaire.md), [TPT-008](../suites/tpt-008-incident-autocar.md), [TPT-009](../suites/tpt-009-incident-maritime.md), [TPT-013](../suites/tpt-013-service-titre-urbain.md) | Numéro de service, horaires et notifications conservés par la tâche du mode concerné. |
| 118 | Réclamation perdue dans un formulaire en ligne | [TPT-007](../suites/tpt-007-relance-transporteur.md) | Copie du formulaire, pièces et accusé d’enregistrement joints à la chronologie. |
| 119 | Plateforme qui ferme le dossier sans réponse motivée | [TPT-007](../suites/tpt-007-relance-transporteur.md) | Clôture, motif demandé et médiateur compétent vérifiés. |
| 120 | Réponse automatique affirmant que le dossier est clôturé | [TPT-007](../suites/tpt-007-relance-transporteur.md) | État informatique séparé du sort des demandes et des voies de recours. |
| 121 | Signature d'un accord pour solde de tout compte | [CTX-039](../../02-plugins-existants/suites/ctx-039-lire-transaction-litige.md) | Portée des engagements et renonciations vers transaction civile qualifiée ; aucune signature. |
| 122 | Acceptation d'une compensation commerciale de faible valeur | [TPT-007](../suites/tpt-007-relance-transporteur.md) | Offre commerciale et indemnisation légale comparées avant accord ; transaction CTX-039 si nécessaire. |
| 123 | Demande de remboursement sans factures | [TPT-001](../suites/tpt-001-annulation-vol-direct.md), [TPT-004](../suites/tpt-004-incident-ferroviaire.md), [TPT-008](../suites/tpt-008-incident-autocar.md), [TPT-009](../suites/tpt-009-incident-maritime.md) | Factures et nécessité des dépenses rapprochées des obligations du mode. |
| 124 | Accident sans identification de témoins | [DOM-035](../dom-035-responsabilite-dommages.md) | Constat, témoins et identification ; préjudice corporel au fond à découper. |
| 125 | Images de vidéosurveillance effacées avant une demande | [EXIST-003](../../02-plugins-existants/exist-003-donnees-personnelles.md) | Images et responsable identifiés ; accès/conservation hors travail à découper, sans gel automatique. |
| 126 | Erreur d'interlocuteur | [TPT-001](../suites/tpt-001-annulation-vol-direct.md) | Qualification commune des acteurs réutilisée par la tâche de l’incident, sans responsabilité collective présumée. |
| 127 | Saisie d'un médiateur non compétent | [TPT-007](../suites/tpt-007-relance-transporteur.md) | Compétence, recevabilité et effets temporels vérifiés ; mauvaise saisine non supposée interruptive. |
| 128 | Confusion entre signalement et indemnisation | [TPT-007](../suites/tpt-007-relance-transporteur.md) | Signalement de contrôle et réparation individuelle séparés. |

## Sections non numérotées et calendrier

- Section 11, tableau des délais : exigences de recherche, jamais barème
  embarqué. TPT-004 vérifie retard, réacheminement, service régional et billet
  direct ; TPT-012 le PV et sa médiation ; TPT-001/003 l’aérien ; TPT-005 le
  bagage ; TPT-008/009 la plainte autocar/bateau ; TPT-007 les voies ultérieures.
  Chaque date distingue seuil d’ouverture du droit, notification de dommage,
  réclamation, médiation et prescription judiciaire, avec événement, preuve,
  version, acte requis, destinataire et inconnues. Une relance, négociation
  ou mauvaise saisine ne reçoit aucun effet interruptif/suspensif automatique.
- Point 64 et dernière ligne du tableau : vérifier en priorité la réforme
  procédurale aérienne alléguée au 7 février 2026, texte d’entrée en vigueur,
  champ, transitions, exceptions, médiation et mode de saisine. Cette date
  n’est pas certifiée ici. TPT-007 oriente vers contentieux pour l’acte exact ;
  CTX-026 ne doit pas être proposé automatiquement comme saisine simplifiée.
- Section 12, méthode pratique : TPT-001 possède la liste commune des preuves
  (billet, conditions datées, segments, acteurs, choix, dépenses et réponses).
  Chaque tâche spécialisée conserve sa propre urgence et son acte requis.
  TPT-007 possède copie intégrale de réclamation, pièces, réception et relance ;
  TPT-012 garde la contestation de PV et son circuit spécifique.
- Les organismes cités sont des pistes : vérifier le canal et sa compétence.
  SignalConso, DGAC et autorités de contrôle ne remplacent pas la demande
  individuelle ; médiation et juge restent distincts. Brouillons seulement.

## Frontières et lacunes explicites

Taxi/VTC (TPT-016), covoiturage (TPT-017) et libre-service (TPT-018) ont leur
propriétaire dans les transports pour l’exécution et la facturation du trajet.
Consommation garde les autres locations et ventes ; banque garde l’opération
bancaire et assurance la garantie. Aucun de ces domaines n’est une dépendance
d’installation. Les bagages autocar (TPT-020) et biens maritimes (TPT-021)
restent distincts des perturbations du service TPT-008/009.

Transport médical et refus CPAM (DOM-012), dommage corporel (DOM-035),
discrimination au fond (DOM-029), faux chauffeur/recours pénal (DOM-002) et
images hors travail (EXIST-003) nécessitent encore leur découpage spécialisé.
PRV-030 est bornée à la surveillance au travail : elle ne couvre pas les
caméras d’une gare. Une demande d’accès ne garantit pas la conservation.
TPT-019 garde assistance sectorielle et fauteuil, sans absorber ces matières.

Restent hors de ce complément : déclassement aérien, bagage ferroviaire au fond,
annulation personnelle hors taxes/garantie, recours judiciaires rédigés,
contrat multimodal complexe, rapatriement, insolvabilité et fret au fond.
TPT-010 reste une qualification de fret. Aucun régime universel de voyageurs
ni moteur général de délais ou d’indemnités n’est créé.
