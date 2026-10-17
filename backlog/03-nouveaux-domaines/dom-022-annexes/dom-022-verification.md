# DOM-022 — Vérification documentaire du découpage

Parcours du **17 octobre 2026 (Europe/Paris)** par le rédacteur à partir des
cas fictifs ci-dessous et des neuf propositions du
[découpage](dom-022-decoupage-telecoms-poste.md). Il porte sur orientation,
pièces et sortie attendue ; il ne résout pas les dossiers et n'exécute aucun
skill. Les scénarios des suites restent **attendus, non exécutés**.
Les [contrôles statiques](dom-022-resultats.json) ont une portée distincte.

## Scénarios demandés par DOM-022

| Cas et pièces fictives | Orientation relue | Pièces à demander / inconnues | Résultat attendu et limite |
|---|---|---|---|
| A — « J'ai rendu ma box, elle est facturée » ; facture et suivi livré, pas d'inventaire ni accusé du contenu. | TEL-002, pas TEL-001 pour le seul matériel. | Consignes, inventaire, référence du dépôt et suivi, contenu déclaré, accusé opérateur et motif exact. | Rapprochement des preuves et brouillon ciblé ; livraison d'un colis distincte de reconnaissance de tout le matériel, aucun remboursement promis. |
| B — « Je paie la fibre jamais installée » ; commande, facture, rendez-vous manqué, message « ligne activée ». | TEL-004 ; vérifier absence de service initial plutôt que présumer une panne TEL-005. | Contrat, date/périmètre promis, comptes rendus, activation, tests et factures/paiements. | Chronologie des versions et demande à l'opérateur cocontractant ; installateur et gestionnaire d'infrastructure non déclarés débiteurs par défaut, aucune faute technique arrêtée. |
| C — « Le colis de ma commande est perdu » ; destinataire acheteur, confirmation de vente et suivi, vendeur renvoyant vers la poste. | Livraison DOM-001/CONSO-001 ; TEL-006 pour une question postale distincte seulement. | Contrat de vente, demande au vendeur, bordereau et achat du service postal, identité du cocontractant, pouvoir éventuel. | Dossier vendeur conservé, rôle postal à établir ; ni renvoi exclusif au transporteur ni exclusion générale du destinataire. |

**Constat documentaire :** les trois problèmes ont un propriétaire principal
et des questions ciblées sans exiger une qualification juridique préalable.
Le cas C ne transforme pas la présence d'un suivi postal en substitution du
prestataire au vendeur. Rien ici ne constate le résultat futur d'un skill.

## Première tranche et autres branches

| Cas fictif | Parcours documentaire retenu |
|---|---|
| D — Frais après rupture ; facture mêlant fermeture, engagement et matériel, motif de déménagement non justifié. | TEL-001 pour frais de rupture, TEL-002 pour matériel ; demander contrat daté, demande/accusé et justificatif utile au motif. Tableau des postes et demande conditionnelle, aucune exonération ni somme due calculée. |
| E — Option inconnue, nom d'un tiers sur la facture. | TEL-003 ; demander accord et identité du vendeur/service, sans présumer absence de consentement ni annuler le prélèvement. |
| F — Service auparavant actif, coupures intermittentes et tests Wi-Fi. | TEL-005 ; journal des périodes, tickets, offre et réponses, cause inconnue ; aucun diagnostic réseau ni indemnité forfaitaire. |
| G — Envoi acheté par un particulier, colis endommagé, bordereau d'intermédiaire. | TEL-006 ; contrats, produit, rôles, état/réserves et valeur, sans faire du transporteur effectif le seul débiteur ni de toute option une assurance. |
| H — Retour de box perdu, étiquette fournie par l'opérateur. | TEL-002 garde la facture ; TEL-006 examine contrat de retour, achat du bordereau et qualité ; usager non présumé responsable du transport. |
| I — Refus opérateur après une réclamation ; personne veut une médiation. | TEL-007 ; vérifier champ opérateur/service, étapes, dates, réception et procédure en cours. Index conditionnel ; refus ne suffit pas à établir recevabilité. |
| J — Colis d'un prestataire privé, charte d'un autre prestataire jointe. | TEL-008 ; rechercher médiateur et champ exacts, pas de compétence déduite de la seule présence d'un colis ni de circuit télécoms transposé. |
| K — « Je veux que l'ARCEP rembourse ma facture ». | TEL-009 pour alerte factuelle si champ confirmé ; réclamation individuelle TEL-001/003 et médiation TEL-007 séparées. Aucun remboursement ou délai préservé par l'alerte présumé. |
| L — Relance accompagnée d'un acte de recouvrement ou d'une décision. | Demander acte complet, auteur et réception ; urgence et avocat compétent, question d'exécution DOM-003 ou de procédure litigation distincte du fond télécoms. Aucun recours générique. |
| M — Suivi « bloqué en douane », sans acte officiel. | TEL-006 pour prestation identifiée ; DOM-009 si question douanière réelle, demander auteur/message/acte. Le suivi ne prouve pas une mesure douanière. |
| N — Fret spécialisé, service professionnel, international ou outre-mer. | Détecter l'exclusion et préciser rôle, produit et territoire ; DOM-008 ou commercial selon question. Pas de régime métropolitain de particulier transposé. |
| O — Pièce déterminante manquante, source absente ou modèle américain joint. | Faits et questions poursuivis ; seule conclusion dépendante réservée, pas de délai/barème/droit étranger importé et pas de source déclarée lue. |

## Correspondance avec les critères

| Critère DOM-022 | Livrable et constat documentaire |
|---|---|
| Stories avec entrées, sortie, pièces, limites et scénarios | TEL-001 à TEL-009, un skill et une référence métier par tâche ; cas normaux et limites propres. |
| Départ depuis le problème | Tableau « Partir du problème », situation S-12 et cas A à K ; aucun nom de code requis. |
| Autonomie et frontières | Contrat de paquetage local, ligne BASE-003, tableau des domaines voisins ; voisins comme orientations sans installation requise. |
| Médiation, signalement, réparation, contrat postal | Tableau des voies ; TEL-006/007/008/009 ; cas C, G à K. |
| Pas de tort ni succès présumés | Faits/pièces/hypothèses séparés ; pas de montant dû, indemnité acquise ou compensation automatique ; cas A à O. |
| Bilan pilote, aucun lancement complet | PILOTE-003 terminé après BASE-011 ; dépendance conservée dans chaque suite, sélection explicite requise, aucun paquet créé. |

## Portée

Les critères de **cadrage** sont satisfaits par ces livrables, le parcours du
rédacteur et les contrôles structurels consignés. Aucune source juridique
externe n'a été consultée ; aucun texte/version, délai, montant, champ de
médiateur ou effet d'un canal n'est certifié. Les sources restent des pistes
à ouvrir lors des implémentations. Aucun paquet installé, skill invoqué,
scénario métier exécuté, envoi, résiliation ou dépôt.

Relecture humaine prise en charge par l'utilisateur conformément à AGENTS.md
du 17 octobre 2026. Elle n'est pas déclarée effectuée ; compréhension par
une personne réelle non observée. Ces limites du cadrage ne constituent pas
une recette technique ou juridique d'un plugin et n'imposent pas d'attendre
la relecture pour clore DOM-022.
