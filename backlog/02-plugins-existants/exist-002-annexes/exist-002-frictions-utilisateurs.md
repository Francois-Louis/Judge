# Formalités des entreprises — Frictions utilisateur et réponses à prévoir

Demande du **16 octobre 2026** : « voici les frictions des utilisateurs auxquelles il faut pouvoir répondre ». Le [texte fourni](../sources/formalites-entreprises-frictions-2026-10-16.txt) est conservé comme expression du besoin. La matrice reprend ses **100 points**, dans leur ordre, et les sections pratiques qui suivent.

**État : exigences de backlog.** Les rattachements ci-dessous décrivent des sorties futures. SOC-023 à SOC-027, COM-019/020 et TRAV-019 à TRAV-021 sont proposés par cette intégration ; aucun skill n'est adapté ou exécuté. Les cadrages DOM-011 et DOM-039 restent à découper : leur attribution ne constitue pas une couverture opérationnelle. Aucune première tranche ni nouveau plugin n'est lancé.

## Lecture du document fourni

La mention « règles vérifiées au 16 octobre 2026 » appartient au document utilisateur. Les favicons, noms de sites et mentions « +1 » ne permettent pas de vérifier les passages invoqués. Les liens identifiables sont des pistes ; aucun délai, seuil, montant ou changement de droit du texte n'est validé ici.

Les implémentations devront notamment vérifier les réformes alléguées de l'ACRE en 2026, l'occultation et les extraits d'actes, les plafonds micro et TVA, l'échéance Urssaf du 31 octobre 2026, la substitution DSN, la facturation électronique et la nouvelle référence de franchise de TVA annoncée au 1er septembre 2026. Pour chaque point : texte exact, version, entrée en vigueur, transitions, champ et faits du dossier. Les tableaux de délais fournis ne deviennent pas des calendriers par défaut.

## Répartition et changements proposés

- **Sociétés** : SOC-004/005/006/007 gardent le registre, les preuves, le rapport et l'audit documentaire ; SOC-023 lit le stade d'un dossier de formalité, SOC-024 qualifie une modification, SOC-025 contrôle les pièces d'un dépôt de comptes, SOC-026 prépare les questions d'une fermeture solvable. Les formes unipersonnelles doivent être qualifiées explicitement.
- **Difficultés de l'entreprise** : SOC-027 est un cadrage à mener pour répartir prévention, cessation des paiements, procédures et patrimoine de l'EI. Aucun des lots de fermeture amiable ou de recouvrement ne couvre actuellement ce besoin au fond.
- **Indépendants** : [DOM-039](../../03-nouveaux-domaines/dom-039-micro-entreprise.md) reçoit les exigences de création, déclarations, cotisations, aides, cessation et recours Urssaf ; il doit encore produire des stories bornées. Son cadrage conserve les impôts courants de l'activité de l'indépendant ; [DOM-011](../../03-nouveaux-domaines/dom-011-fiscalite.md) porte les impôts des sociétés, le contrôle fiscal et le contentieux fiscal, avec une fiche de relais explicite.
- **Contrats trompeurs** : COM-019 traite une demande de paiement présentée comme obligatoire ; COM-020 lit un abonnement ou mandat de formalités. Ni la qualité de professionnel ni une démarche à distance ne suffisent à trancher les protections applicables.
- **Employeurs** : TRAV-019 prépare les pièces d'une première embauche par une petite entreprise française, distincte de TRAV-014 (employeur étranger). TRAV-020 lit une anomalie DSN ; TRAV-021 rapproche les documents de fin de contrat sans contrôler la validité de la rupture.
- **Frontières** : publicité de registre → sociétés/DOM-039 ; droits sur un traitement privé → EXIST-003 ; marque → PI-002 ; activité réglementée → EXIST-007 et secteur ; paiement bancaire → DOM-004 ; acte d'exécution → DOM-003. Un litige fiscal ou social ne devient pas administratif général à cause du nom de l'organisme.

## Matrice des 100 points

Le premier propriétaire traite la question décrite ; les relais nommés portent une question distincte. « À découper » indique un manque de stories d'implémentation, même si le domaine est identifié.

| N° | Friction | Propriétaire et relais | Résultat attendu |
|---|---|---|---|
| 1 | Fausse facture d'inscription à un registre | [COM-019](../suites/com-019-demande-paiement-suspecte.md) ; SOC-023 pour le dossier réel | Comparer émetteur, obligation invoquée, commande et frais officiels à rechercher. |
| 2 | Annuaire professionnel présenté comme obligatoire | COM-019 | Repérer signature, prix, durée et preuve de commande ; préparer la contestation factuelle. |
| 3 | Faux avis INPI, SIRENE ou RNE | COM-019 | Identifier les éléments d'imitation et une voie de vérification indépendante. |
| 4 | Portail privé imitant une administration | COM-019 ; COM-020 si contrat | Distinguer frais de formalité et rémunération facultative du prestataire. |
| 5 | Faux courrier Urssaf ou DGFiP | COM-019 ; DOM-039/DOM-011 si acte authentique | Vérifier l'origine sans utiliser le lien ni le RIB reçu ; qualifier l'acte réel séparément. |
| 6 | Vente d'une prétendue conformité obligatoire | COM-019 ; secteur pour l'obligation réelle | Demander le texte, le champ et les éléments établissant l'achat de cette prestation. |
| 7 | Faux contrôle ou inspecteur | COM-019 ; domaine du contrôle, pénal si faits allégués | Préparer la vérification indépendante d'identité et d'habilitation sans conseiller l'obstruction. |
| 8 | Abonnement caché dans une formalité | [COM-020](../suites/com-020-abonnement-mandat-formalites.md) | Reconstituer consentement, prestations, prélèvements, durée et sortie contractuelle. |
| 9 | Menace de recouvrement d'un annuaire | COM-019 ; DOM-003 si acte d'exécution | Demander contrat et décompte, distinguer relance et titre, préparer le brouillon adapté. |
| 10 | Démarchage à partir de données de registre | COM-019 ; EXIST-003 pour traitement privé | Expliquer que des données exactes ne prouvent pas l'origine ; documenter l'usage des données. |
| 11 | Dépôt pris pour immatriculation achevée | [SOC-023](../suites/soc-023-lire-dossier-formalite.md) ; DOM-039 pour EI | Établir les états prouvés et le justificatif encore manquant. |
| 12 | Demande de régularisation manquée | SOC-023 ; DOM-039 pour EI | Lire la demande complète, la réception et les pièces ; rechercher le délai propre au cas. |
| 13 | Rejet nécessitant une nouvelle formalité | SOC-023 ; DOM-039 pour EI | Séparer rejet et correction, conserver motif, référence, paiement et voies à vérifier. |
| 14 | Activité ou code APE erroné | DOM-039 à découper ; SOC-024 pour société | Rapprocher activité réelle, déclaration et donnée contestée ; identifier le bon destinataire. |
| 15 | Activités principale et secondaire confondues | DOM-039 à découper ; SOC-024 pour société | Ventiler activités et recettes ; préparer les questions fiscales, sociales et de registre. |
| 16 | Statut juridique inadapté | DOM-039 à découper ; sociétés, fiscalité en relais | Préparer une comparaison qualitative datée, avec hypothèses et coûts restant à établir. |
| 17 | Activité réglementée sans prérequis vérifiés | Secteur à découper ; [EXIST-007](../exist-007-veille-reglementaire.md) pour changement de texte identifié | Identifier qualification, autorisation et assurance à rechercher ; ne pas déduire l'autorisation du registre. |
| 18 | Bénéficiaires effectifs oubliés à la création | SOC-023 ; SOC-004 pour suivi | Identifier contrôle, personnes, pièces et état de déclaration sans présumer dispense en société unipersonnelle. |
| 19 | Domiciliation mal comprise | COM-020 pour contrat ; SOC-024/DOM-039 pour registre | Séparer siège, établissement, exercice et droit d'utiliser l'adresse. |
| 20 | Justificatif facturé alors qu'une voie gratuite existe | SOC-023 ; DOM-039 pour EI | Identifier le document réellement nécessaire et vérifier son accès officiel et ses frais. |
| 21 | Adresse personnelle rendue publique | SOC-023/024 ; DOM-039 pour EI, EXIST-003 pour réutilisation privée | Distinguer non-diffusion, occultation d'acte et droits sur une copie privée ; préparer les pièces propres à chaque demande. |
| 22 | Immatriculation prise pour protection de marque | [PI-002](../suites/pi-002-recherche-nom-france.md) | Préparer la recherche sur nom, signes, activités et territoire sans annoncer disponibilité. |
| 23 | Demande ACRE manquée | DOM-039 à découper | Recueillir création, éligibilité, demande et accusé ; vérifier régime et échéance à la date des faits. |
| 24 | Déménagement non déclaré | [SOC-024](../suites/soc-024-qualifier-modification.md) ; DOM-039 pour EI | Identifier décision, siège/établissement et inscriptions à actualiser ; relais fiscal séparé. |
| 25 | Dirigeant non actualisé | SOC-024 ; SOC-001/003 pour décision et PV | Rapprocher nomination, pouvoirs et état du registre, puis lister les pièces manquantes. |
| 26 | Échéance de modification statutaire manquée | SOC-024 ; SOC-006 pour suivi | Établir événement, date prouvée et règle à vérifier avant tout calcul. |
| 27 | Bénéficiaire effectif non actualisé | SOC-024 | Comparer contrôle, identité, adresses et déclaration précédente ; rechercher l'actualisation nécessaire. |
| 28 | Statuts modifiés sans autres étapes | SOC-024 ; SOC-005 pour preuve | Séparer décision, acte, publication, dépôt et inscription obtenue. |
| 29 | Établissement oublié | SOC-024 ; DOM-039 pour EI | Identifier SIREN/SIRET, sites et dates ; séparer formalité et conséquences fiscales. |
| 30 | Changement d'activité non déclaré | SOC-024 ; DOM-039 pour EI, secteur réglementé | Décrire l'activité réelle, les registres et autorisations à examiner. |
| 31 | Capital modifié sans conséquences anticipées | SOC-024 ; SOC-009 et DOM-011 en relais | Repérer opération, contrôle, bénéficiaires et question d'enregistrement fiscal, sans rédiger la cession. |
| 32 | Mandat de prestataire excessif | COM-020 ; SOC-023 pour état du dossier | Lire pouvoirs, accès et révocation envisagée ; préparer restitution des pièces et vérification des dépôts. |
| 33 | Déclaration Urssaf à zéro oubliée | DOM-039 à découper | Rapprocher périodes, statut et reçus ; préparer la régularisation à vérifier. |
| 34 | Facturation confondue avec encaissement | DOM-039 à découper | Comparer factures, encaissements et déclaration sans modifier le compte de l'utilisateur. |
| 35 | Échéance mensuelle ou trimestrielle manquée | DOM-039 à découper | Établir périodicité, début d'activité et calendrier propre à la première déclaration. |
| 36 | Report d'un jour non ouvré présumé | DOM-039 à découper | Vérifier l'échéance officielle concernée, son heure et le régime de report ; aucun report automatique. |
| 37 | Déclaration annuelle fiscale oubliée | DOM-039 à découper | Distinguer déclarations sociales et fiscales, périodes et justificatifs. |
| 38 | Versement libératoire mal compris | DOM-039 à découper | Identifier option, revenu de référence, dates et informations nécessaires à une comparaison sourcée. |
| 39 | Plafonds micro et franchise TVA confondus | DOM-039 à découper | Présenter deux qualifications séparées avec périodes et seuils à rechercher. |
| 40 | Seuil majoré de TVA dépassé | DOM-039 à découper | Reconstituer le cumul daté et les opérations autour du dépassement ; réserver la date d'effet non vérifiée. |
| 41 | Prorata de création oublié | DOM-039 à découper | Qualifier chaque seuil séparément, dates et base de prorata ; aucun calcul commun présumé. |
| 42 | Sortie du régime micro non anticipée | DOM-039 à découper | Lire les recettes de plusieurs exercices et préparer les questions sur le régime et ses dates d'effet. |
| 43 | Compte professionnel payant présumé obligatoire | DOM-039 à découper ; [DOM-004](../../03-nouveaux-domaines/dom-004-banque.md) pour contrat bancaire | Séparer obligation légale de compte, compte dédié et conditions commerciales de la banque. |
| 44 | Taux de cotisation inadapté aux recettes | DOM-039 à découper | Ventiler recettes, période, catégorie et régime ; rechercher les taux applicables avant calcul. |
| 45 | Absence d'activité prise pour disparition des obligations | DOM-039 à découper | Distinguer chiffre d'affaires nul, inactivité, cessation et radiation ; dresser les vérifications restantes. |
| 46 | Déclaration initiale CFE oubliée | DOM-039 pour indépendant ; DOM-011 pour société, à découper | Identifier création, établissement, déclaration et accusé ; vérifier exonération et échéance propres au cas. |
| 47 | Avis CFE non reçu par courrier | DOM-039/DOM-011 selon contribuable | Rechercher avis et mise à disposition, accès professionnel et date de paiement à vérifier. |
| 48 | Exonération de cotisation minimum non examinée | DOM-039/DOM-011 selon contribuable | Recueillir recettes, période de référence et prorata ; distinguer cotisation minimum et CFE totale. |
| 49 | Exonération artisan méconnue | DOM-039 à découper | Décrire travail manuel, achats, salariés et activité ; vérifier les conditions au-delà de l'étiquette artisan. |
| 50 | CFE sans local professionnel | DOM-039/DOM-011 selon contribuable | Lire commune, établissement, base et exonérations sans conclure à partir de la seule adresse personnelle. |
| 51 | Réduction CFE après cessation oubliée | DOM-039/DOM-011 selon contribuable | Rapprocher cessation effective, avis et demande ; vérifier conditions et période de réduction. |
| 52 | Exonération géographique manquée | DOM-039/DOM-011 selon contribuable | Qualifier commune, dates, implantation et régime ; rechercher demande et transitions. |
| 53 | TVA non déclarée après changement de régime | DOM-039 pour indépendant ; DOM-011 pour société | Rapprocher seuil, option, opérations, facturation et date d'effet vérifiée. |
| 54 | Franchise TVA prise pour dispense internationale | DOM-039/DOM-011 ; DOM-009 si douane | Qualifier pays, biens/services et partenaires avant déclaration ou autoliquidation. |
| 55 | Acomptes et solde IS mal suivis | DOM-011 à découper | Identifier société, régime, clôture et déclarations ; préparer le calendrier sourcé. |
| 56 | Espace fiscal inadapté ou non activé | DOM-039/DOM-011 selon contribuable | Identifier service, contribuable et preuve de dépôt ; préparer les démarches d'accès utiles. |
| 57 | Contestation supposée suspendre le paiement | DOM-011 à découper | Séparer réclamation, exigibilité et demande de sursis, avec conditions à vérifier. |
| 58 | Délai de réclamation fiscale expiré | DOM-011 à découper | Qualifier impôt, acte, mise en recouvrement, événement et demande antérieure avant tout calcul. |
| 59 | Réception électronique non anticipée | DOM-011 à découper ; DOM-039 pour faits de l'indépendant | Qualifier assujettissement, flux et taille puis rechercher calendrier, obligations et preuve de préparation. |
| 60 | Fausse plateforme présentée comme agréée | COM-019 ; DOM-011 pour réforme, COM-020 pour abonnement | Vérifier identité et statut sur une liste officielle datée, puis distinguer service et obligation. |
| 61 | E-reporting des opérations oublié | DOM-011 à découper | Distinguer facturation et transmission de données selon flux B2B, B2C et internationaux. |
| 62 | Mention de franchise déclarée obsolète par un vendeur | DOM-011 à découper ; COM-019 pour pression commerciale | Vérifier référence, entrée en vigueur et transition avant de demander une modification. |
| 63 | Mentions de facture incomplètes | [COM-015](../suites/com-015-facture-b2b-impayee.md) pour pièces B2B ; DOM-011 pour TVA | Comparer facture, parties et opération ; la vérification exhaustive d'un modèle reste à découper. |
| 64 | Livres micro et justificatifs manquants | DOM-039 à découper | Identifier livres requis selon activité et pièces ; produire une liste documentaire, sans tenir la comptabilité. |
| 65 | Dépôt des comptes manqué | [SOC-025](../suites/soc-025-pieces-depot-comptes.md) ; SOC-006 pour suivi | Séparer clôture, approbation et dépôt ; qualifier voie, date, justificatif et délai à rechercher. |
| 66 | Confidentialité des comptes non demandée | SOC-025 | Vérifier taille, groupe, exclusions, pièces et portée de la demande sans promettre une confidentialité totale. |
| 67 | SASU sans rémunération réputée sans obligations | SOC-004/025 ; DOM-011 pour fiscalité | Identifier obligations par événement et exercice, indépendamment du seul salaire du dirigeant. |
| 68 | Décisions de l'associé unique non documentées | [SOC-001](../suites/soc-001-qualifier-decision-sociale.md), SOC-003 | Qualifier SASU/EURL, auteur, acte et preuve ; ne pas inventer d'assemblée ou de vote collectif. |
| 69 | Dépenses personnelles mélangées aux dépenses d'activité | DOM-039 pour indépendant ; DOM-011 pour fiscalité | Reconstituer l'objet et les justificatifs des dépenses ciblées sans présumer leur déductibilité. |
| 70 | Durée d'archivage unique appliquée partout | SOC-007 pour pièces sociales ; DOM-039/011 et travail pour leurs pièces | Établir une liste par catégorie, finalité et durée à rechercher ; pas de purge automatique. |
| 71 | DPAE oubliée | [TRAV-019](../../01-pilote-travail/suites/trav-019-premiere-embauche-tpe.md) | Vérifier embauche prévue/réalisée, dépôt et accusé ; signaler la recherche de régularisation si nécessaire. |
| 72 | Registre du personnel absent | TRAV-019 | Identifier salarié, effectif et support ; préparer les éléments manquants sans créer d'inscription fictive. |
| 73 | DUERP absent | TRAV-019 | Repérer existence, activité et risques ; préparer les pièces et l'interlocuteur, sans produire une évaluation universelle. |
| 74 | DSN tardive ou incorrecte | [TRAV-020](../../01-pilote-travail/suites/trav-020-anomalie-dsn.md) | Rapprocher période, dépôt, comptes rendus et anomalie ; préparer une question au déclarant. |
| 75 | Substitution DSN non comprise | TRAV-020 | Lire notification, modifications et réponse annoncée ; vérifier dispositif et délai sans calculer la paie. |
| 76 | Suivi de santé au travail oublié | TRAV-019 | Séparer DPAE, affiliation et suivi médical applicable ; rechercher les démarches selon le poste. |
| 77 | Achat de panneaux présenté comme imposé | TRAV-019 ; COM-019 pour vendeur | Distinguer information à fournir, mode autorisé et produit commercial proposé. |
| 78 | Documents et signalements de départ oubliés | [TRAV-021](../../01-pilote-travail/suites/trav-021-pieces-fin-contrat.md) | Comparer rupture documentée, pièces remises, signalements et sommes à expliquer ; paie hors périmètre. |
| 79 | Arrêt d'activité pris pour fermeture | DOM-039 pour EI ; [SOC-026](../suites/soc-026-qualifier-fermeture-solvable.md) pour société | Reconstituer arrêt, formalités et preuves ; lister les obligations restant à examiner. |
| 80 | Mise en sommeil confondue avec radiation | DOM-039 pour EI ; SOC-026 pour société | Qualifier temporaire/définitif et conséquences à rechercher, sans déclarer l'entreprise fermée. |
| 81 | Déclarations finales oubliées | DOM-039 pour indépendant ; DOM-011 pour société | Séparer cessation, dernière période sociale et fiscale, TVA et CFE ; vérifier chaque calendrier. |
| 82 | Coût et étapes de fermeture sous-estimés | SOC-026 | Présenter étapes documentées, pièces et catégories de frais sans forfait inventé. |
| 83 | Liquidation amiable confondue avec judiciaire | SOC-026 ; [SOC-027](../suites/soc-027-cadrage-entreprises-difficulte.md) à cadrer | Identifier indices et inconnues de solvabilité ; réserver le parcours amiable si doute déterminant. |
| 84 | Déclaration de cessation des paiements tardive | SOC-027 à cadrer | Prévoir qualification actif disponible/passif exigible, dates, juridiction et urgence à vérifier ; aucun diagnostic de bilan seul. |
| 85 | Prévention des difficultés trop tardive | SOC-027 à cadrer | Découper orientation, conditions des procédures et préparation documentaire distinctes. |
| 86 | Radiation supposée effacer les dettes | SOC-027 à cadrer ; DOM-039/011 selon dette | Identifier débiteur, dettes, garanties et procédures ; ne pas inférer l'extinction de l'inscription radiée. |
| 87 | Patrimoine de l'EI mal anticipé à la cessation | SOC-027 à cadrer ; DOM-039 pour cessation | Recueillir dates, patrimoines, créanciers et sûretés ; prévoir une analyse distincte et sourcée. |
| 88 | Décision administrative crue incontestable | DOM-039 pour Urssaf indépendant ; DOM-011 pour fiscalité ; DOM-010 subsidiaire | Identifier acte, motifs, calcul et régime avant de préparer une demande écrite. |
| 89 | Contestation seulement téléphonique | Même propriétaire que la dette ou la décision | Préparer un écrit retraçant objet, références, faits et pièces, avec preuve d'envoi à conserver. |
| 90 | Message informel pris pour recours | Même propriétaire que l'acte ; DOM-010 subsidiaire | Séparer réclamation, recours préalable, médiation et saisine, avec effets à vérifier. |
| 91 | Recours CRA Urssaf manqué | DOM-039 à découper ; travail pour employeur société | Lire décision et notification ; qualifier la voie et son déclencheur avant de calculer le délai. |
| 92 | Contrainte Urssaf ignorée | [ENF-001](../../03-nouveaux-domaines/suites/enf-001-lire-acte.md) pour acte ; DOM-039/travail pour contestation sociale à découper | Identifier contrainte, notification, urgence et régime spécial d'opposition ; pas de CRA appliquée par défaut. |
| 93 | Remise de majorations non demandée | DOM-039 à découper ; travail pour employeur société | Distinguer contestation du principal et demande gracieuse ; recueillir régularisation et conditions à rechercher. |
| 94 | Droit à l'erreur pris pour protection générale | Domaine de l'obligation | Qualifier erreur, omission, retard, bonne foi et régularisation sans promettre remise ni suspension. |
| 95 | Difficultés de paiement non signalées | DOM-039/DOM-011 selon dette ; SOC-027 pour difficulté globale | Préparer budget et échéancier demandé ; séparer acceptation, exigibilité et prévention des difficultés. |
| 96 | Anomalie du Guichet unique sans preuve | SOC-023 ; DOM-039 pour EI | Constituer chronologie, identifiant, captures datées, ticket et accusés de dépôt. |
| 97 | INPI confondu avec autorité de validation | SOC-023 ; DOM-039 pour EI | Distinguer opérateur technique, destinataire, auteur de demande et auteur de décision ; rechercher la voie propre. |
| 98 | Médiation Urssaf et délais confondus | DOM-039 à découper ; travail pour employeur société | Qualifier réclamation préalable, admissibilité et effets sur chaque délai selon textes lus ; aucun effet présumé. |
| 99 | Faux créancier payé sous pression | COM-019 ; DOM-004 si paiement, DOM-003 si acte | Demander contrat, décompte et pouvoir de recouvrement ; séparer contestation de dette et réponse bancaire. |
| 100 | Rétractation B2B exclue par principe | COM-020 ; COM-019 pour commande trompeuse | Vérifier mode de conclusion, effectif, activité principale, objet, dates et exceptions avant toute conclusion. |

## Exigences communes aux sorties

La personne doit pouvoir partir de son courrier, facture, notification ou capture du portail. Recueillir seulement les faits nécessaires : qualité du demandeur, EI/micro ou société et forme exacte, activité, établissement, organisme, événement, période, dates et pièces. Une micro-entreprise n'est pas une forme de société ; un associé unique ne rend pas la formalité inexistante.

Chaque résultat explique le document et son stade, les montants recopiés ou calculés avec leur provenance, ce qui est établi, ce qui manque, puis une démarche concrète et son destinataire. Distinguer coût officiel et prestation privée, dépôt et validation, compte rendu et décision, réclamation et recours, dette et acte exécutoire. Aucun paiement, envoi, dépôt ou changement d'accès n'est déduit d'un brouillon.

### Calendrier fourni — section 10

Transformer chaque échéance pertinente en fiche : obligation, personne/régime, événement déclencheur, date et preuve de notification, règle/version, unité, mode de calcul, exceptions/transitions, date/heure et état de vérification. Si une donnée déterminante manque, indiquer l'urgence à vérifier et la pièce nécessaire ; ne pas inventer une date rassurante. L'échéance de recours et l'exigibilité du paiement gardent des champs séparés.

### Checklist et interlocuteurs — sections 11 et 12

Prévoir : vérification indépendante de l'émetteur ; lecture de l'obligation et des voies de recours ; conservation de la décision, de l'enveloppe ou notification électronique, des captures et accusés ; demande du fondement et du décompte ; brouillon au destinataire identifié ; vérification distincte d'un sursis ou de l'effet d'une médiation ; preuve de dépôt et suivi. Ne pas appliquer un interlocuteur unique à tous les registres ou toutes les voies de recours.

Le contact chargé de traiter le dossier et le professionnel pouvant conseiller la personne sont nommés séparément. Appliquer BASE-013 et la relecture avant livraison BASE-014 dans chaque future tranche ; une proposition de délai ne remplace pas la lecture des textes et de la notification.

## Scénarios de recette à prévoir

Ces scénarios sont **attendus, non exécutés** ; ils vérifient une réponse utile, pas seulement la présence d'un mot-clé.

| Cas | Sortie attendue |
|---|---|
| Micro-entrepreneur recevant un annuaire après sa création | Commande à vérifier, facture suspecte distinguée du dossier réel, brouillon de demande de preuve. |
| Société dont le dossier affiche un paiement puis un rejet | Chronologie et pièces ; aucune immatriculation déduite du paiement ; bon auteur du rejet à identifier. |
| EI avec activité mixte et données APE incohérentes | Activités et recettes séparées, organisme compétent à rechercher, pas de taux unique inventé. |
| SASU sans rémunération dont les comptes doivent être déposés | Forme unipersonnelle, approbation et dépôt distingués, confidentialité à vérifier. |
| Micro-entrepreneuse dépassant un seuil en cours d'année | Micro, TVA et prorata séparés ; calendrier réservé si source/version manquante. |
| Artisan recevant une CFE sans local et invoquant une exonération | Critères factuels et périodes demandés ; absence de local sans conclusion automatique. |
| Prestataire imposant une plateforme et une nouvelle mention TVA | Vérification officielle et transition à rechercher ; abonnement commercial isolé. |
| TPE française recrutant son premier salarié | Parcours employeur adapté sans profil d'expansion internationale, liste de pièces et lacunes. |
| Notification de substitution DSN sans preuve de réception | Anomalie et dates incertaines visibles, pas de paie corrigée ni de délai calculé sans base. |
| Contrainte Urssaf reçue après une simple réclamation | Acte et urgence identifiés ; pas de substitution par une CRA ou une médiation supposée suspensive. |
| Fermeture envisagée avec dettes et trésorerie inconnues | Parcours amiable réservé, pièces de solvabilité et orientation vers le cadrage difficultés. |
| EI radiée dont un créancier réclame une dette ancienne | Débiteur, date, garanties et patrimoine à rechercher ; aucune dette effacée par déduction. |

## Bilan de l'intégration

Source archivée, 100 points rattachés, dix propositions ajoutées et exigences reportées dans les cadrages propriétaires et les index. Les contrôles portent sur la fidélité de l'archive, la numérotation complète, les liens, les identifiants, dépendances et décomptes. Les résultats observés figurent dans la [vérification de cette intégration](exist-002-frictions-verification.md).

**Portée :** intégration documentaire des besoins sous `backlog/`, sans recherche juridique externe, scénario métier exécuté, essai utilisateur, adaptation de plugin ni démarche administrative réalisée. Les absences de traitement au fond restent explicites, notamment DOM-011, DOM-039 et SOC-027. Les anciens bilans et leurs empreintes restent les preuves de leurs lots historiques, pas une validation de ces ajouts.
