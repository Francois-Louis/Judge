---
id: DOM-041
titre: "Cadrer un plugin relation avec un professionnel du droit ou du chiffre"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-041 — Cadrer un plugin relation avec un professionnel du droit ou du chiffre

## Objectif

Aider une personne à comprendre les frais d'un notaire, les honoraires d'un
avocat ou d'un expert-comptable, à préparer une réclamation ou une
contestation et à savoir à qui s'adresser lorsque la relation avec ce
professionnel pose problème.
Ajouté le 16 octobre 2026 ([décisions](../decisions-2026-10-16.md)).

Nom de plugin proposé : `professional-services-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un décompte de frais de notaire et distinguer émoluments, débours, taxes et honoraires libres.
- Lire une convention ou une facture d'honoraires d'avocat et préparer une contestation.
- Préparer une réclamation contre un notaire, un avocat ou un commissaire de justice : retard, absence de réponse, restitution du dossier.
- Préparer une demande d'aide juridictionnelle pour une procédure identifiée.
- Lire une lettre de mission ou des honoraires d'expert-comptable ; préparer une réclamation pour documents non rendus, retard ou erreur alléguée dans une déclaration.

## Qualification et frontières

Profession, acte ou mission, convention ou devis, facture ou décompte,
paiements, dates, échanges et objet de la réclamation.

La relation avec le professionnel est ici. Le fond du dossier reste à son
domaine : succession → DOM-016, achat immobilier → DOM-017, famille →
DOM-013, procédure → litigation ; les taxes collectées par le notaire sont
lues ici et leur assiette relève de DOM-011. Frais d'exécution figurant dans
un acte de saisie → ENF-003. Faute pénale alléguée → DOM-002. Conséquence
fiscale ou sociale d'une erreur de l'expert-comptable → DOM-011 ou DOM-039 ;
ici seulement la relation avec le professionnel.

## Sources à prévoir et vérifier

Textes sur les tarifs réglementés des notaires (Code de commerce et arrêtés),
statut des notaires, des avocats et des experts-comptables, procédure de
contestation des honoraires d'avocat, aide juridictionnelle ; chambres des
notaires, ordres des avocats et des experts-comptables, médiateurs des
professions et service public comme sources d'information.

Les guides orientent le cadrage ; les textes et versions applicables seront
vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire un décompte de frais de notaire et séparer émoluments, débours, taxes et
honoraires, avec les questions à poser à l'étude.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de sa facture ou de son courrier sans connaître le tarif applicable.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; le fond des dossiers reste à son domaine.
- [ ] Aucun émolument ni taux recalculé sans texte lu et date établie ; une contestation ne présume pas une faute.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Des « frais de notaire » d'achat immobilier jugés trop élevés par l'acquéreur.
- Un avocat réclamant des honoraires sans convention écrite.
- Une succession qui n'avance pas, notaire sans réponse depuis des mois.
- Un expert-comptable qui ne rend pas les documents d'un artisan après la fin de sa mission.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas
résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, évaluer la qualité juridique du travail du
professionnel, engager sa responsabilité devant un juge ou contacter
l'instance ordinale à la place de la personne.

## Complément des frictions contentieuses — 16 octobre 2026

Exigences issues des [125 frictions contentieuses](../02-plugins-existants/exist-006-frictions-utilisateurs.md), sans implémentation ni sélection de tranche.

Points 72–77 et 81–82 : découper lecture de convention d’honoraires, rapprochement diligences/factures/provisions, contestation devant l’interlocuteur compétent, et préparation d’aide juridictionnelle pour une étape qualifiée. Recueillir convention et avenants, détail des diligences et paiements, mission première instance/appel/exécution, désignation éventuelle d’office, décision d’aide et dates des frais. Sorties : engagements couverts ou absents, décompte documenté, questions/réclamation locale, pièces d’aide et prise en charge encore incertaine. Distinguer forme de rémunération et résultat, montant contesté et faute alléguée.

CTX-040 consomme les coûts et prises en charge documentés sans décider les honoraires. Protection juridique → DOM-005. Scénarios : forfait excluant appel ; provisions sans détail ; avocat désigné d’office et aide non obtenue ; appel avec aide limitée à une autre étape. Rechercher textes professionnels, règles de contestation et d’aide applicables, sans tenir les financements pour acquis.

Les scénarios indiqués sont attendus, non exécutés. Sources/version, champ, déclencheur, exceptions et transitions restent à rechercher ; le texte fourni n’est pas une autorité juridique.
