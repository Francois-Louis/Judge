# DOM-016 — Vérification du cadrage

Relecture documentaire du 17 octobre 2026 (Europe/Paris), par l’agent de
maintenance. Les [25 parcours](dom-016-parcours.md) renvoient aux deux
scénarios de chaque suite. Vérification des contrats écrits, pièces fictives,
sans sortie produite par un skill.

## Confrontation aux demandes initiales et compléments

| Entrée fictive et cas | Orientation observée dans le contrat | Pièces et résultat attendu contrôlés |
|---|---|---|
| Courrier incompris, signature pressante, C01/C02 | SUC-001 | Acte complet, réception et actes accomplis ; fiche et questions. Ni option ni signature validées sur un intitulé. |
| Relevés et dette sans détail, C03/C04 | SUC-002 | Inventaire sourcé et passif inconnu ; propriété du compte joint réservée, assurance-vie INS-011 et créance employeur sectorielle séparées. Aucun net distribuable. |
| Sommation et échéance fiscale, C05/C06 | SUC-003 ; fiscalité DOM-011 | Acte, réception, option et forme à vérifier ; urgence et calendriers séparés, pas de protection déduite du délai général. |
| Meuble vendu avant découverte du passif, C07/C08 | SUC-004 | Vente, motif, mandat et dates ; acceptation tacite seulement à rechercher, paiement conservatoire non qualifié automatiquement. |
| Déclaration protégée, inventaire non prouvé, C09/C10 | SUC-005 | Récépissé, publicité, inventaire/dépôt et décision de prorogation ; aucune protection ni prorogation acquises par simple demande. |
| Renonciation et descendants mineurs, C11/C12 | SUC-006, conflit parental DOM-013 | Filiation, représentation, autorisation et récépissé ; dossier par personne, aucune renonciation étendue aux enfants ou dispense de frais d’obsèques promise. |
| Créancier puis titre d’exécution, C13/C14 | SUC-007 ; acte DOM-003 prioritaire | Contrat, décompte, qualité, option, notification et engagement propre ; aucune dette personnelle reconnue. |
| Dette découverte après acceptation, C15/C16 | SUC-008 | Acceptation, connaissance et informations antérieures ; dossier pour avocat, voie et calendrier propres, pas de décharge promise. |
| Frais globaux, réforme constitutionnelle alléguée, C17/C18 | SUC-009 | Assiette, produits, tarif et date de service ; décision exacte à retrouver. Aucun plafond, gratuité ou remboursement établis. |
| Ancien livret, transfert inconnu, résultat négatif/coffre, C19/C20 | SUC-010 | Qualité, indices, notifications et détenteur ; banque/FICOBA/Ciclade distingués. Absence de résultat sans conclusion d’absence de fonds ; assurance-vie INS-011. |
| Facture obsèques et avance personnelle, C21/C22 | SUC-011 ; FUN-002/005 | Signataire, réponse bancaire, fonds et date ; règlement direct, remboursement d’avance et charge finale séparés ; aucun seuil d’un autre mécanisme réutilisé. |
| Compte joint, carte, procuration et retraits, C23/C24 | SUC-012 ; propriété SUC-002, paiement BNK-001 | Convention, mandat et opérations datées ; aucun usage des accès conseillé ni pouvoir prolongé par présomption. |
| Petit solde, testament/héritier contesté, C25/C26 | SUC-013 ; frais DOM-041 | Finalité de la pièce, biens et contestations ; simplification non déduite du seul montant. Qualité et option distinctes. |
| Effets non remis ou disparus, C27/C28 | SUC-014 ; facture établissement DOM-025 | Inventaire initial, dépositaire et reçus ; demande documentée sans répartition ni vol ou recel établis. |
| Donation omise ou testament photographié, C29/C30 | SUC-015 | Provenance, original, dates et bénéficiaires déclarés ; authenticité et portée réservées, aucune validité ou nullité conclues. |
| Estimations de dates et occupations différentes, C31/C32 | SUC-016 | Périmètre et méthodes ; écarts explicités sans moyenne choisie ou expertise produite. |
| Loyers et dépenses sans preuve, C33/C34 | SUC-017 | Postes, payeurs, accords et justificatifs ; aucun solde exigible ni compensation automatiques. |
| Occupant sans accord, survivant pressé de partir, C35/C36 | SUC-018 puis SUC-022 prioritaire | Titre, convention et droits propres ; aucune entrée forcée ni absence de droit déduite d’une pièce manquante. |
| Vente imposée, démembrement/protection, C37/C38 | SUC-019 ; pouvoirs DOM-026 | Projet, titulaires/droits, décision/mandat et texte invoqué ; aucune majorité universelle ou réforme de 2026 validée. |
| Projet de partage, annexes ou donation manquantes, C39/C40 | SUC-020 | Actif/passif, avances, évaluations et comptes ; rapprochement des postes, complétude réservée et aucun partage définitif. |
| Partage signé, omission, médiation, C41/C42 | SUC-021 | Acte, découverte et griefs ; fondements et calendriers propres, aucune suspension générale de prescription. |
| Conjoint menacé de départ, partenaire pacsé, C43/C44 | SUC-022 ; bail DOM-006, couple DOM-013 | Statut, titre, testament, occupation et volonté exprimée ; droits au logement et vocation successorale séparés, renfort en tête. |
| Généalogiste inconnu, facture sans mandat, C45/C46 | SUC-023 | Contrat, mission, identité à vérifier par voie distincte et information déjà connue ; aucune authenticité, dette ou abus présumés. |
| Donation avec charges, propriété/capacité discutées, C47/C48 | SUC-024 ; DOM-013/026/011 | Acte, intention et libéralités antérieures ; fiche de clauses et questions, aucun acte à signer ni stratégie fiscale. |
| Résidence étrangère, testament, décès ancien, C49/C50 | SUC-025 avant conclusions françaises dépendantes | Pays, résidence prouvée, nationalités, acte/choix allégué et procédures ; compétence, loi et circulation distinctes, champ et transitions réservés. |

La lecture confirme qu’un propriétaire et une sortie sont prévus pour chaque
demande et limite, et que les pièces manquantes restent visibles. Elle ne
vérifie pas le comportement futur d’un modèle.

## Couverture des critères

| Critère DOM-016 | Preuve documentaire |
|---|---|
| Entrées, sortie, pièces, limites et scénarios | 25 SUC, une tâche/un résultat par suite, cas nominal et limite C01–C50. |
| Départ accessible | Demandes courantes dans les suites et parcours ; récit accepté comme déclaré. Compréhension réelle non mesurée. |
| Autonomie et frontières | Contrat BASE-003/005/008, références locales et transmissions ; aucun plugin voisin ou connecteur obligatoire. |
| Option, partage, déclaration fiscale | SUC-003, SUC-020 et DOM-011 ; aucun partage définitif sur dossier incomplet dans le contrat commun. |
| Neutralité et absence d’issue promise | Fait/pièce/allégation/inconnu séparés ; aucun abus, recel, remboursement ou droit acquis par présomption. |
| Préalable et absence d’adaptation complète | PILOTE-003 relue et terminée après BASE-011 ; toutes les SUC proposées, aucun paquet créé. |
| Compléments banque et décès | Table de couverture des groupes de points DOM-004/031 ; calendriers et interlocuteurs propres. |

## Contrôles techniques

Le [relevé du lot](dom-016-resultats.json) rapporte les vérifications
effectuées : identifiants/frontmatters, dépendances existantes et sans cycle,
liens et ancres locaux, format UTF-8, inventaire des 25 suites et index généré.
Les commandes `python backlog/etat.py --check`,
`python scripts/check-version-bump.py` et `git diff --check` complètent le
contrôle du diff. Le contrôle de versions reste sans changement de plugin.

Le seul fichier de programme modifié est le générateur du backlog, pour
nommer la famille SUC. La régénération et `--check` valident cet usage.
Schémas et artefacts détachés BASE-006/008 sans objet ici : aucun plugin ou
manifeste créé ou modifié. Ces recettes restent dans les critères des futures
implémentations, sans être présentées comme passées.

## Portée

Cadrage documentaire, cas fictifs et relecture par l’agent rédacteur. Les
lectures d’information officielles et extraits UE sont tracés séparément ;
textes français, versions, transitions et décision constitutionnelle alléguée
non vérifiés, aucun dossier juridique résolu. Aucun skill exécuté, aucune
installation, aucun essai en client ou test de compréhension avec un
participant. Ces recettes concernent les suites non implémentées et ne sont
pas des critères techniques manquants du présent cadrage. L’utilisateur
prend en charge la relecture humaine des livrables ; elle n’est pas déclarée
effectuée ni assimilée à une validation juridique ou de compréhension.
