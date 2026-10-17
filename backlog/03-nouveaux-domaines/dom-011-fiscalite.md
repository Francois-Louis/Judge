---
id: DOM-011
titre: "Cadrer un plugin de fiscalité"
statut: proposee
priorite: P3
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-011 — Cadrer un plugin de fiscalité

## Objectif

Distinguer l'assistance déclarative, le contrôle et la réclamation fiscale.

Nom de plugin proposé : `tax-legal`. Le cadrage peut le modifier ; aucun répertoire de plugin n'est créé par cette story.

## Travail attendu

- Impôt, période, contribuable, résidence, déclaration, acte reçu et stade de la procédure.
- Tâches candidates : lecture d'avis, préparation de réclamation, lecture de proposition de rectification, constitution de pièces.
- Séparer assiette, contrôle, recouvrement, pénalités et demande gracieuse ; prévoir les conventions et régimes particuliers sans tout traiter d'emblée.
- Définir un skill par tâche, ses entrées, sa sortie et ses dépendances. Écrire des stories d'implémentation assez petites pour être relues séparément.

## Sources à prévoir

Code général des impôts, Livre des procédures fiscales, textes UE ou conventions pertinents, impots.gouv.fr et BOFiP avec portée à vérifier.

Ces pistes ne constituent ni une vérification du droit actuel ni un corpus déjà embarqué. Les sources exactes seront ouvertes et vérifiées lors de l'implémentation.

## Première tranche proposée

Un premier skill de lecture et de qualification d'un document fiscal précisément identifié.

## Critères d'acceptation

- [ ] Le domaine a son propre plugin dans la matrice d'architecture, avec des frontières explicites.
- [ ] Les tâches candidates sont hiérarchisées ; le premier skill a un périmètre et des exclusions précis.
- [ ] Chaque story d'implémentation précise les références métier, les pièces nécessaires, la sortie et les scénarios de contrôle.
- [ ] Le plugin est prévu pour être installé seul ; agents, connecteurs et hooks ne sont ajoutés que pour un besoin identifié.
- [ ] Les implémentations sont conditionnées au bilan PILOTE-003 et ne sont pas lancées dans cette story.

## Scénarios pour éprouver le découpage

- Une erreur alléguée sur un avis d'impôt.
- Une proposition de rectification.
- Une demande de délai de paiement.
- Une demande de justifications reçue d'un service des impôts, sans proposition de rectification.
- Un avis de vérification de comptabilité adressé à un artisan.
- Un avis de paiement majoré du comptable public, suivi d'une saisie administrative.

Vérifier le routage et les informations à demander. La story ne doit pas résoudre ces consultations ni fournir de délais ou montants non vérifiés.

## Compléments du 16 octobre 2026

Ajoutés par décision de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)). Ces tâches candidates
s'ajoutent à celles ci-dessus ; elles restent à hiérarchiser par le cadrage.

- **Contrôle fiscal**, phase par phase : demande de renseignements ou de
  justifications, contrôle sur pièces, avis d'examen de la situation fiscale
  personnelle, avis de vérification de comptabilité ; puis proposition de
  rectification, réponse et recours internes. Garanties du contribuable
  contrôlé à lire dans les textes et documents officiels applicables.
- **Vérification de comptabilité d'une entreprise ou d'un indépendant** :
  la procédure fiscale est ici ; les cotisations sociales de l'indépendant
  restent à DOM-039, la relation avec l'expert-comptable à DOM-041.
- **Comptable public** : avis de paiement, majorations, délais de paiement
  et remise gracieuse. L'acte de saisie administrative est lu par ENF-001
  et ENF-004 ; son bien-fondé fiscal reste ici.
- **Fraude alléguée** : volet pénal → DOM-002, sans qualification présumée.

Sources à prévoir en plus : Livre des procédures fiscales (procédures de
contrôle, garanties, recouvrement), documents officiels remis au contribuable
contrôlé, à identifier dans leur version.

## Hors périmètre

Implémenter le domaine entier, créer un plugin vide pour donner l'impression d'avancer, ou regrouper les autres matières dans un module France/UE.

## Complément — fiscalité des entreprises, 16 octobre 2026

La [matrice des 100 frictions](../02-plugins-existants/exist-002-annexes/exist-002-frictions-utilisateurs.md), points 37–42, 46–63, 69–70, 81 et 88–95, impose de préciser les tâches ci-dessous. DOM-011 reste un cadrage proposé, **à découper**, sans calcul ni règle vérifiée par cet ajout.

- Avis CFE : lire contribuable, commune/établissement, base, période de référence et mise en recouvrement ; préparer séparément explication, examen d'exonération et réclamation. Distinguer cotisation minimum, absence de local, critères de l'activité artisanale, implantation géographique et cessation.
- TVA : séparer franchise, option, seuils et dates d'effet, puis opérations internationales (biens/services, pays et qualité des partenaires). Ne pas confondre plafonds micro, seuils TVA et prorata ; les douanes gardent les opérations de leur champ.
- IS : lire un échéancier/avis ou une obligation déclarative d'un exercice identifié ; demander régime, clôture, paiements et accusés, sans moteur général de calcul.
- Facturation électronique : découper qualification d'un flux et calendrier de réception/émission, vérification documentaire d'une plateforme et e-reporting. La vente d'une offre imposée relève de COM-019/020 ; ne pas certifier un fournisseur. Vérifier séparément les mentions fiscales de facture et les transitions de référence légale alléguées dans le texte.
- Dépenses et archivage : demander les justificatifs d'une dépense ciblée, distinguer nature, finalité et période ; prévoir une liste des durées par catégorie, sans comptabilité complète ni purge.
- Recours : séparer lecture de décision, réclamation d'assiette, recouvrement, sursis, remise gracieuse et demande d'échéancier. Lire acte, notification, période, auteur et recours antérieur ; l'exigibilité et le délai de contestation gardent des analyses distinctes.
- Cessation : préparer les dernières obligations par impôt et régime, dont réduction CFE éventuelle ; la radiation de registre n'est pas une preuve de traitement fiscal final.

Frontière : impôts courants de l'activité indépendante → DOM-039 ; impôts de société, contrôle et contentieux fiscal → ici. Une demande formelle issue du premier parcours reçoit une fiche de relais avec pièces et dates, sans nouvelle qualification contradictoire. Espaces particulier/professionnel et services activés doivent être identifiés ; aucune déclaration déduite du seul accès au compte.

Scénarios attendus : CFE d'un artisan invoquant une exonération ; avis disponible uniquement en ligne ; société sans local ; franchissement de seuil en cours d'année ; prestation internationale sous franchise ; facture électronique et mention TVA présentées comme une urgence commerciale ; réclamation pendante sans sursis établi ; société fermée avec dernières déclarations manquantes. Résultat : distinction des questions, pièces et calculs réservés ; pas d'exécution métier ici. Voir la matrice pour la portée.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 78–80, 82, 104 et D11 de la [matrice](dom-031-annexes/dom-031-frictions-utilisateurs.md). Tâches candidates à découper ; aucune nouvelle capacité livrée.

- [ ] Découper déclaration fiscale de succession : date et lieu du décès, domiciles fiscaux, actif, donations, qualité, mission du notaire, dépôt et paiement ; sortie : pièces et échéances séparées de l’option civile, sans exonération assimilée à dispense de déclaration.
- [ ] Prévoir la fiscalité du capital d’assurance-vie après décès : contrats, dates/primes, âge pertinent, bénéficiaire et attestations ; expliquer les questions au professionnel sans exonération générale ni liquidation sur données incomplètes.

Scénarios supplémentaires **attendus, non exécutés** : héritier pensant attendre le partage avant dépôt ; bénéficiaire d’assurance-vie convaincu de l’exonération totale ; déclaration confiée au notaire sans preuve de dépôt.

Sources à ouvrir lors de l’implémentation : CGI, BOFiP et textes de dépôt/paiement/dispenses et assurance-vie ; territorialité et version à la date des faits.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](dom-031-annexes/dom-031-frictions-verification.md).

## Complément des frictions véhicules — 16 octobre 2026

Point 191 : découper la préparation d'une demande de quitus ou la lecture d'un blocage fiscal d'acquisition de véhicule à l'étranger. Recueillir pays et qualité vendeur/acheteur, factures, dates, première mise en circulation, kilométrage utile, TVA annoncée, documents et réponse du service. Sortie : régime à rechercher, pièces manquantes et brouillon ciblé, sans TVA ou quitus automatiquement dû. Distinguer fiscalité DOM-011, douane DOM-009, immatriculation DOM-010 et documents promis VEH-019. Cas attendus : véhicule présenté comme occasion mais qualification fiscale inconnue ; facture étrangère et demande de pièce complémentaire. Versions, territorialité et définition fiscale à vérifier dans les sources officielles ; aucune règle ni montant repris du texte fourni.

Exigences de la [matrice des 195 points](dom-023-annexes/dom-023-frictions-utilisateurs.md), à découper sans sélection de tranche. Sources et scénarios métier non vérifiés ; [portée de l’intégration](dom-023-annexes/dom-023-frictions-verification.md).

## Complément des frictions allocations et aides sociales — 16 octobre 2026

Point 86 de la [matrice](dom-012-annexes/dom-012-frictions-utilisateurs.md).
À découper : traitement fiscal personnel d'un versement ARCE. Recueillir année,
résidence fiscale, notification, décompte/retenues et attestation fiscale ;
sortie : qualification des sommes et questions/rubriques à vérifier, sans
assimiler capital chômage à prêt ou CA d'activité. Attribution/versement ARCE
chez DOM-012 ; fiscalité courante de l'activité indépendante chez DOM-039.
Sources futures : CGI et doctrine fiscale officielle selon année et situation.
Cas attendu : capital reçu et déclaration préremplie discordante. Scénario
non exécuté ; [portée](dom-012-annexes/dom-012-frictions-verification.md).

## Complément des frictions douanes — 17 octobre 2026

Points 2–4, 12, 39 et 41–44, 48 et 52 : V04 demande de découper TVA import/IOSS, assiette et correction, autoliquidation/déduction, preuve fiscale de sortie, ventes à distance/OSS, état récapitulatif TVA et DES selon opération et statut. IND-027 porte le parcours de l'indépendant, sans seconde qualification contradictoire ; contrôle/contentieux et sociétés restent ici. Douanes : C01 ventile, DOU-008 prépare la valeur, C02/C03 concernent déclaration, C20 EMEBI statistique. Recueillir factures/paiements, déclaration, identification/régime TVA, territoires, flux et période. Sorties : rapprochement des postes, pièces et brouillon fiscal ciblé après recherche. Cas : TVA au panier puis livraison ; micro en franchise important ; vente export sans preuve de sortie. Aucun seuil, forfait 2026, CA3, droit à déduction ou remboursement général repris sans vérification.

Exigences de la [matrice des 75 points](dom-009-annexes/dom-009-frictions-utilisateurs.md), sans sélection de tranche ni capacité annoncée comme livrée. [Portée et contrôles](dom-009-annexes/dom-009-frictions-verification.md).
