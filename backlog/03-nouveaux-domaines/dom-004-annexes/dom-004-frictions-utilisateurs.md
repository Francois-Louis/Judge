# Banque — Frictions utilisateur et réponses à prévoir

Demande du **16 octobre 2026** : « voici les frictions des utilisateurs auxquelles il faut pouvoir répondre ». Le [texte fourni](../sources/banques-frictions-2026-10-16.txt) est conservé comme expression du besoin. Ses 99 points numérotés sont repris ci-dessous, avec les tâches et résultats attendus.

**État : exigences de backlog.** Toutes les stories BNK et INS restent proposées. Une ligne attribuée ne signifie pas qu'un skill peut déjà répondre. DOM-016 et DOM-024 restent des cadrages à découper. Aucun nouveau domaine ni lancement de première tranche n'est décidé par cette intégration.

## Lecture du texte fourni

La mention « réglementation vérifiée au 16 octobre 2026 » appartient au document utilisateur ; elle ne vaut pas validation par le dépôt. Les pseudo-citations « Service Public +4 » et favicons n'identifient pas les passages sources. Aucun montant, délai, statistique ni événement juridique de ce texte n'est repris comme une règle vérifiée.

Pour les implémentations, contrôler particulièrement : plafonds et périmètres de frais, jours ouvrables ou ouvrés, pays et prestataires des paiements, calendrier des textes européens, solde insaisissable, frais de succession et allégation d'une décision constitutionnelle de juin 2026. Cette dernière reste une affirmation à rechercher dans une décision officielle, avec son effet dans le temps ; elle ne justifie ici aucune suppression de droit.

## Changements de découpage

- BNK-001 à BNK-012 : préciser les pièces, demandes, distinctions et scénarios ; conserver leurs bornes (pas de calcul général de frais, d'indemnité ou de prescription).
- BNK-013 à BNK-019 : sept tâches nouvelles, mobilité, blocage, erreur de virement, disponibilité de la carte, compte inactif, financement professionnel et encaissement commerçant.
- INS-012 : rachat d'assurance-vie retardé, distinct du paiement au bénéficiaire après décès (INS-011).
- INS-008 et INS-011, ENF-004, DOM-016 et DOM-024 : compléter les exigences chez leur propriétaire.
- Placements, PEA et actifs numériques : maintenir l'orientation seule décidée le 16 octobre 2026. Les points 80–83 et 89 n'ont donc pas de traitement au fond prévu. BNK-011 doit l'annoncer et fournir les pièces et l'interlocuteur utiles. Un contrôle juridique des frais de PEA ou du conseil en investissement demanderait un arbitrage de périmètre ultérieur.

## Matrice des 99 points

Chaque résultat ci-dessous est une exigence future. Les numéros correspondent exactement à ceux du texte fourni ; les propriétaires secondaires traitent une question distincte.

| N° | Friction | Propriétaire et relais | Résultat attendu |
|---|---|---|---|
| 1 | Second rejet du même prélèvement | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Rapprocher les références et les frais des représentations. |
| 2 | Frais supérieurs au montant rejeté | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Comparer le montant du rejet et le plafond applicable. |
| 3 | Commissions d'intervention répétées | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Ventiler les interventions et vérifier le cumul pertinent. |
| 4 | Cumul forfait de rejet et commission | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Rechercher une double facturation dans le forfait. |
| 5 | Courriers facturés | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Demander le fondement tarifaire et vérifier l'inclusion dans un plafond. |
| 6 | Frais d'incident sans information préalable | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Comparer notification et débit avec leurs dates prouvées. |
| 7 | Tenue de compte et cotisations cumulées | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Rendre visible le coût total des lignes facturées. |
| 8 | Package surdimensionné | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Demander détail, services séparés et coût, sans recommander une offre. |
| 9 | Services facultatifs renouvelés | [BNK-003](../suites/bnk-003-frais-bancaires.md), [INS-006](../suites/ins-006-resilier-contrat.md) | Identifier souscription, renouvellement et résiliation ; assurance à part. |
| 10 | Hausse de tarif peu visible | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Comparer ancien tarif, support durable, réception et entrée en vigueur. |
| 11 | Agios opaques | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Obtenir taux, jours, base et minima ; demander le décompte, sans recalcul dans ce lot. |
| 12 | Frais après clôture | [BNK-008](../suites/bnk-008-cloture-compte.md), [BNK-003](../suites/bnk-003-frais-bancaires.md) | Établir la clôture effective puis demander restitution des lignes contestées. |
| 13 | Retraits à l'étranger et hors réseau | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Ventiler banque, réseau, distributeur et conversion. |
| 14 | Marge de change invisible | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Demander taux de conversion, marge et information présentée. |
| 15 | Récapitulatif annuel absent | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Demander le document puis rapprocher les frais des relevés. |
| 16 | Ancien abonnement encore prélevé | [BNK-006](../suites/bnk-006-prelevement.md), [DOM-001](../dom-001-consommation.md) | Séparer remboursement bancaire et résiliation ou dette envers le créancier. |
| 17 | Mandat SEPA inconnu | [BNK-006](../suites/bnk-006-prelevement.md) | Demander référence, preuve du mandat et autorisation contestée. |
| 18 | Mandat révoqué mais débits persistants | [BNK-006](../suites/bnk-006-prelevement.md) | Documenter révocation et information de la banque ; demande de blocage adaptée. |
| 19 | Prélèvement autorisé mais montant erroné | [BNK-006](../suites/bnk-006-prelevement.md) | Qualifier Core ou autre régime ; distinguer remboursement et dette. |
| 20 | Prélèvement rejeté sans alerte | [BNK-006](../suites/bnk-006-prelevement.md), [BNK-003](../suites/bnk-003-frais-bancaires.md) | Identifier refus et information disponible, régularisation utile et frais à vérifier. |
| 21 | Double débit après changement de compte | [BNK-013](../suites/bnk-013-mobilite-bancaire.md), [BNK-006](../suites/bnk-006-prelevement.md) | Comparer les deux comptes et attribuer l'anomalie de transfert. |
| 22 | Virement au mauvais IBAN | [BNK-015](../suites/bnk-015-erreur-virement.md) | Demander rappel et recherche sans garantie de récupération. |
| 23 | Virement suspendu par un contrôle | [BNK-014](../suites/bnk-014-blocage-compte.md) | Tracer justificatifs et échanges en respectant les limites d'information. |
| 24 | Surcoût de virement instantané | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Comparer l'opération classique comparable et le régime du prestataire. |
| 25 | Vérification nom et IBAN absente ou erronée | [BNK-015](../suites/bnk-015-erreur-virement.md), [BNK-002](../suites/bnk-002-virement-tromperie.md) | Rechercher écran, avertissement, date et champ d'application. |
| 26 | Double débit par carte | [BNK-016](../suites/bnk-016-carte-preautorisation.md) | Distinguer attente et comptabilisation, demander les références des deux opérations. |
| 27 | Préautorisation persistante | [BNK-016](../suites/bnk-016-carte-preautorisation.md) | Documenter statut et demande de levée à l'acteur compétent. |
| 28 | Achat non livré et chargeback | [BNK-001](../suites/bnk-001-contester-paiement.md), [DOM-001](../dom-001-consommation.md) | Préparer la demande de conditions de réseau ; traiter la vente séparément. |
| 29 | Refus bancaire sans examen du paiement | [BNK-001](../suites/bnk-001-contester-paiement.md), [BNK-004](../suites/bnk-004-mediation-bancaire.md) | Demander motif, données et réexamen puis escalade. |
| 30 | Plafond de carte incompris | [BNK-016](../suites/bnk-016-carte-preautorisation.md) | Lire période glissante, différé et empreintes dans le contrat. |
| 31 | Code ou application présenté comme preuve suffisante | [BNK-001](../suites/bnk-001-contester-paiement.md) | Séparer authentification et consentement ; demander les preuves invoquées. |
| 32 | Négligence grave affirmée | [BNK-001](../suites/bnk-001-contester-paiement.md) | Demander faits et éléments de preuve sans trancher la négligence. |
| 33 | Faux conseiller et refus immédiat | [BNK-002](../suites/bnk-002-virement-tromperie.md) | Décrire appel, affichage et validations sans présumer l'autorisation. |
| 34 | Plainte exigée avant examen | [BNK-001](../suites/bnk-001-contester-paiement.md) | Documenter l'exigence et demander son fondement ; plainte distincte. |
| 35 | Enquête retardant le remboursement | [BNK-001](../suites/bnk-001-contester-paiement.md) | Comparer signalement, réponse et éventuelle exception avec les textes lus. |
| 36 | Frais consécutifs non restitués | [BNK-001](../suites/bnk-001-contester-paiement.md), [BNK-003](../suites/bnk-003-frais-bancaires.md) | Relier les frais à l'opération et demander la remise en état documentée. |
| 37 | Virement volontaire après manipulation | [BNK-002](../suites/bnk-002-virement-tromperie.md) | Traiter la qualification et les griefs sans remboursement automatique promis. |
| 38 | Opération avec prestataire hors EEE | [BNK-001](../suites/bnk-001-contester-paiement.md) | Qualifier les prestataires, pays, devise et clause avant tout délai. |
| 39 | Décision de refus inexpliquée | [BNK-001](../suites/bnk-001-contester-paiement.md), [BNK-004](../suites/bnk-004-mediation-bancaire.md) | Demander une réponse écrite séparant consentement, authentification et faute alléguée. |
| 40 | Irréversibilité opposée à toute demande | [BNK-015](../suites/bnk-015-erreur-virement.md), [BNK-001](../suites/bnk-001-contester-paiement.md) | Séparer rappel technique, qualification et recours éventuel. |
| 41 | Débits après opposition | [BNK-001](../suites/bnk-001-contester-paiement.md) | Comparer heures d'opposition, autorisation et comptabilisation. |
| 42 | Clôture par la banque sans préavis | [BNK-008](../suites/bnk-008-cloture-compte.md) | Lire notification, réception, statut du compte et exceptions. |
| 43 | Refus de clôture à l'initiative du client | [BNK-008](../suites/bnk-008-cloture-compte.md) | Préparer la demande écrite et documenter les opérations restant à traiter. |
| 44 | Cotisation de carte non restituée | [BNK-008](../suites/bnk-008-cloture-compte.md), [BNK-003](../suites/bnk-003-frais-bancaires.md) | Identifier période prépayée et date de résiliation ; restitution à vérifier. |
| 45 | Compte dormant facturé | [BNK-017](../suites/bnk-017-compte-inactif.md), [BNK-003](../suites/bnk-003-frais-bancaires.md) | Vérifier qualification du compte, produit et frais applicables. |
| 46 | Fonds transférés à la Caisse des dépôts | [BNK-017](../suites/bnk-017-compte-inactif.md) | Identifier banque ou Ciclade et les pièces de recherche. |
| 47 | Mobilité bancaire inachevée | [BNK-013](../suites/bnk-013-mobilite-bancaire.md) | Suivre les étapes et les créanciers à partir du mandat reçu. |
| 48 | Incident causé par la mobilité | [BNK-013](../suites/bnk-013-mobilite-bancaire.md) | Documenter le manquement, la causalité et la demande d'indemnisation. |
| 49 | Clôture avec chèques en circulation | [BNK-013](../suites/bnk-013-mobilite-bancaire.md), [BNK-008](../suites/bnk-008-cloture-compte.md) | Lister les chèques et la provision à vérifier avant clôture. |
| 50 | Refus d'ouverture de compte | [BNK-008](../suites/bnk-008-cloture-compte.md) | Préparer les pièces pour vérifier le droit au compte. |
| 51 | Aucune notification de refus d'ouverture | [BNK-008](../suites/bnk-008-cloture-compte.md) | Documenter dépôt, complétude et silence pour la démarche Banque de France. |
| 52 | Compte bloqué pour conformité | [BNK-014](../suites/bnk-014-blocage-compte.md) | Rapprocher pièces demandées, remises et réponses. |
| 53 | Panne durable et opérations empêchées | [BNK-014](../suites/bnk-014-blocage-compte.md) | Préparer chronologie, demande de solution et pertes documentées. |
| 54 | Frais sur produit réglementé | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Identifier le produit et ses règles propres avant de contester. |
| 55 | Conditions modifiées sans information claire | [BNK-003](../suites/bnk-003-frais-bancaires.md), [BNK-008](../suites/bnk-008-cloture-compte.md) | Comparer versions, support, notification et objet de la modification. |
| 56 | Assurance emprunteur imposée par la banque | [INS-008](../suites/ins-008-assurance-emprunteur.md), [BNK-005](../suites/bnk-005-offre-credit.md) | Lire garanties exigées et préparer une demande de délégation. |
| 57 | Refus de substitution inexpliqué | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Comparer garanties et motifs, avec pièces et dates. |
| 58 | Pénalisation de l'assurance externe | [INS-008](../suites/ins-008-assurance-emprunteur.md), [BNK-005](../suites/bnk-005-offre-credit.md) | Documenter frais et modifications des conditions du prêt. |
| 59 | Renégociation sans coût complet | [BNK-009](../suites/bnk-009-remboursement-anticipe.md) | Tableau des coûts annoncés : restant dû, avenant, garanties, assurance ; pas de simulation. |
| 60 | Indemnité de remboursement anticipé excessive | [BNK-009](../suites/bnk-009-remboursement-anticipe.md) | Demander le décompte et le fondement des plafonds, sans calcul dans cette tranche. |
| 61 | Exonération d'indemnité ignorée | [BNK-009](../suites/bnk-009-remboursement-anticipe.md) | Recueillir cause de la vente et justificatifs pour vérifier l'exonération. |
| 62 | Frais de dossier sans clause | [BNK-005](../suites/bnk-005-offre-credit.md), [BNK-003](../suites/bnk-003-frais-bancaires.md) | Rapprocher prélèvement, contrat et consentement. |
| 63 | Coût du crédit renouvelable minimisé | [BNK-005](../suites/bnk-005-offre-credit.md) | Distinguer capital, mensualité, coût annoncé, assurance et amortissement. |
| 64 | Assurance emprunteur inadaptée au risque | [INS-008](../suites/ins-008-assurance-emprunteur.md) | Lire exclusions, carence, franchise, quotité et critères de garantie. |
| 65 | Échéances en retard et pénalités | [BNK-007](../suites/bnk-007-difficulte-credit.md) | Préparer demande d'aménagement et orientation vers délais judiciaires à vérifier. |
| 66 | Déchéance du terme incomprise | [BNK-007](../suites/bnk-007-difficulte-credit.md) | Rapprocher clause, mises en demeure, dates et décompte exigé. |
| 67 | Inscription FICP sans procédure préalable | [BNK-010](../suites/bnk-010-fichiers-banque-france.md) | Rechercher notification, réception et possibilité de régularisation. |
| 68 | FICP maintenu après paiement | [BNK-010](../suites/bnk-010-fichiers-banque-france.md) | Préparer demande de mise à jour au déclarant avec preuves de régularisation. |
| 69 | Forclusion du crédit non repérée | [BNK-007](../suites/bnk-007-difficulte-credit.md) | Isoler la chronologie et orienter le calcul contentieux ; ne pas faire signer un nouvel accord. |
| 70 | Frais de SATD excessifs | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Vérifier base et frais ; acte de saisie traité par ENF-004. |
| 71 | Aucune somme disponible après saisie | [ENF-004](../suites/enf-004-saisie-compte.md) | Lire l'acte et documenter fonds disponibles et protection à vérifier. |
| 72 | Prestations insaisissables prélevées | [ENF-004](../suites/enf-004-saisie-compte.md), [DOM-012](../dom-012-protection-sociale.md) | Identifier origine et justificatifs des fonds, sans insaisissabilité générale présumée. |
| 73 | Délais SATD et saisie-attribution confondus | [ENF-004](../suites/enf-004-saisie-compte.md) | Identifier acte, notification, autorité et procédure avant tout délai. |
| 74 | Mainlevée ou échéancier inexpliqués | [ENF-004](../suites/enf-004-saisie-compte.md) | Identifier auteur de la saisie et préparer les questions de régularisation. |
| 75 | Fragilité financière non prise en compte | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Recueillir critères, période reconnue et catégories de frais concernées. |
| 76 | Offre spécifique jamais proposée | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Demander examen d'éligibilité, proposition et tarif. |
| 77 | Plafonds de l'offre spécifique dépassés | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Ventiler catégories, mois et année sans cumuler arbitrairement les plafonds. |
| 78 | Nouveau crédit proposé pour payer les frais | [DOM-024](../dom-024-dettes-surendettement.md), [BNK-005](../suites/bnk-005-offre-credit.md) | Mettre à plat la situation et lire l'offre sans recommander l'endettement supplémentaire. |
| 79 | Surendettement durable sans dossier | [DOM-024](../dom-024-dettes-surendettement.md) | Préparer inventaire et pièces, distinguer dépôt et recevabilité. |
| 80 | Placement vendu comme sans risque | [BNK-011](../suites/bnk-011-placement.md) | Orientation : produit, documents, publicité et interlocuteur ; pas d'analyse au fond. |
| 81 | Frais de placement mal compris | [BNK-011](../suites/bnk-011-placement.md) | Orientation : demander le relevé des coûts et les clauses ; pas de calcul de rendement. |
| 82 | Transfert de PEA retardé | [BNK-011](../suites/bnk-011-placement.md) | Orientation : chronologie et médiateur compétent à identifier ; pas de réclamation au fond. |
| 83 | Frais de transfert de PEA élevés | [BNK-011](../suites/bnk-011-placement.md) | Orientation : lignes, facture et documents à demander ; pas de contrôle juridique au fond. |
| 84 | Rachat d'assurance-vie retardé | [INS-012](../suites/ins-012-rachat-assurance-vie.md) | Établir réception et pièces, puis préparer la relance à l'assureur. |
| 85 | Capital décès non versé | [INS-011](../suites/ins-011-assurance-vie-beneficiaire.md) | Établir qualité, pièces nécessaires, réception et demande d'intérêts à vérifier. |
| 86 | Frais bancaires de succession élevés | [DOM-016](../dom-016-successions-donations.md) | Prévoir une tâche de lecture du décompte : périmètre, date, avoirs et tarifs. |
| 87 | Gratuité successorale mal appliquée | [DOM-016](../dom-016-successions-donations.md) | Vérifier droit dans le temps et éventuelle décision officielle avant toute conclusion. |
| 88 | Comptes oubliés d'un défunt | [DOM-016](../dom-016-successions-donations.md) | Documenter qualité successorale et recherches banque/Ciclade ; assurance-vie séparée. |
| 89 | Garantie de l'épargne confondue avec absence de risque | [BNK-011](../suites/bnk-011-placement.md) | Orientation sur nature du produit et documents ; pas d'évaluation du risque. |
| 90 | Plafonds des particuliers appliqués au professionnel | [BNK-003](../suites/bnk-003-frais-bancaires.md) | Qualifier client et usage avant de lire les conditions professionnelles. |
| 91 | Découvert professionnel dénoncé | [BNK-018](../suites/bnk-018-financement-professionnel.md) | Lire concours, notification et exceptions ; identifier la médiation du crédit. |
| 92 | Trésorerie réduite avant une échéance | [BNK-018](../suites/bnk-018-financement-professionnel.md) | Documenter décision, trésorerie et échéances pour une demande urgente. |
| 93 | Refus de financement professionnel | [BNK-018](../suites/bnk-018-financement-professionnel.md) | Préparer le dossier d'orientation, sans droit au financement présumé. |
| 94 | Tarif du terminal de paiement opaque | [BNK-019](../suites/bnk-019-encaissement-professionnel.md) | Ventiler commissions, abonnement, location et résiliation. |
| 95 | Encaissements commerçants retenus | [BNK-019](../suites/bnk-019-encaissement-professionnel.md) | Demander fondement de la réserve et conditions de libération. |
| 96 | Coût du financement professionnel incompris | [BNK-018](../suites/bnk-018-financement-professionnel.md), [BNK-003](../suites/bnk-003-frais-bancaires.md) | Demander ventilation taux, commissions et garanties ; frais facturés à rapprocher. |
| 97 | Caution personnelle mal comprise | [BNK-012](../suites/bnk-012-caution.md) | Lire montant, durée, portée et date du cautionnement. |
| 98 | Compte personnel utilisé pour l'activité | [BNK-008](../suites/bnk-008-cloture-compte.md), [DOM-039](../dom-039-micro-entreprise.md) | Distinguer obligation de compte dédié, offre professionnelle et usage contractuel permis. |
| 99 | Mauvais médiateur professionnel saisi | [BNK-018](../suites/bnk-018-financement-professionnel.md), [BNK-004](../suites/bnk-004-mediation-bancaire.md) | Distinguer financement professionnel, litige de service et recevabilité de la médiation. |

## Exigences communes issues des autres sections du texte

Les tableaux de délais, les démarches et les dix réflexes ne créent pas des délais supplémentaires et ne sont pas perdus dans les 99 lignes :

| Besoin | Exigence attendue | Propriétaire |
|---|---|---|
| Comprendre la pratique | Distinguer irrégularité établie par une règle lue, point contestable et clause défavorable ; présenter faits et preuves, sans présumer un abus. | Toutes les tâches BNK/INS concernées |
| Constituer le dossier | Convention et versions, relevés, brochure, opérations, notifications, preuves de réception et demandes précédentes ; masquer les identifiants. Distinguer fait déclaré, pièce lue et inconnue. | Tâche métier concernée |
| Contester utilement | Brouillon avec dates, montants recopiés, références masquées, demande précise, pièces et réponse attendue ; conserver preuve de l'envoi effectué par la personne. | Tâche métier concernée |
| Suivre les échéances | Tableau séparant événement déclencheur, date prouvée ou inconnue, nature du délai, unité de jours, texte/version, échéance vérifiée ou à établir. Une réclamation ne fait pas disparaître les autres échéances ; aucun calcul sans qualification et source lue. | BNK-004 pour le suivi de réclamation ; tâche métier pour son régime ; ENF-004 pour la saisie |
| Réagir à une urgence | Opposition et signalement par les canaux officiels, conservation des preuves ; demande de rappel pour un virement pertinent ; aucune opération exécutée par l'outil. | BNK-001, BNK-002, BNK-015 |
| Choisir l'interlocuteur | Banque et service réclamations, médiation de consommation, AMF, Médiation du crédit ou assureur selon statut et produit ; signalement au contrôle distinct d'un recours individuel. | BNK-004, BNK-011, BNK-018, INS-005 |
| Prévenir la répétition | Liste adaptée au dossier : relevés, récapitulatif annuel, versions tarifaires, preuve de demande et échéances à suivre ; pas d'abonnement automatique ni de connexion au compte. | Tâche métier concernée |

## Vérification de cette intégration

Contrôle documentaire : 99 identifiants uniques et continus, propriétaire existant pour chaque ligne, liens locaux, dépendances sans cycle, stories et tableau de découpage cohérents. Les contrôles DOM-004 vérifient cette structure ; ils ne prouvent pas le droit ni l'efficacité d'un futur skill.

Relecture des frontières sur les situations du texte :

- Points 25 et 37 : erreur de bénéficiaire → BNK-015 ; validation sous manipulation → BNK-002 ; aucun consentement déduit d'une seule authentification.
- Points 26 et 95 : fonds indisponibles du titulaire de carte → BNK-016 ; versements retenus du commerçant → BNK-019.
- Points 70 et 73 : frais de saisie → BNK-003 ; procédure, sommes protégées et contestation → ENF-004.
- Points 84 et 85 : rachat par le souscripteur → INS-012 ; capital après décès → INS-011.
- Points 86–88 : succession → DOM-016 ; recherche des fonds personnels d'un titulaire vivant → BNK-017.
- Points 91 et 99 : rupture du concours et Médiation du crédit → BNK-018 ; médiation de consommation non présumée pour un professionnel.
- Points 80–83 et 89 : orientation seule, limite affichée plutôt que couverture au fond annoncée.

**Portée :** intégration documentaire des besoins et relecture par l'agent de maintenance. Les scénarios métier restent attendus, non exécutés ; aucune recherche juridique externe, création de plugin, exécution de skill, recette client ou publication.
