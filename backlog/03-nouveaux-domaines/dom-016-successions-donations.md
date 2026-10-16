---
id: DOM-016
titre: "Cadrer un plugin successions et donations"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-016 — Cadrer un plugin successions et donations

## Objectif

Aider les héritiers et les donateurs à comprendre les pièces, les options et les étapes d'une transmission patrimoniale.

Nom de plugin proposé : `inheritance-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire un courrier de notaire ou une demande de pièce et préparer des questions précises.
- Organiser l'actif, le passif et les informations nécessaires avant une décision successorale.
- Préparer un dossier de désaccord entre héritiers, de partage ou de donation à analyser.

## Qualification et frontières

Date du décès, liens familiaux, régime matrimonial, résidence habituelle, testament ou donations connus, biens/dettes, actes déjà signés et élément étranger.

Ce domaine traite la transmission et l'indivision successorale ; les obsèques relèvent de DOM-031, la fiscalité de DOM-011, le patrimoine du couple de DOM-013 et la protection d'un majeur de DOM-026.

## Sources à prévoir et vérifier

Code civil, Code de procédure civile, textes fiscaux pour leur seule articulation, instruments transfrontaliers pertinents et sources officielles Justice et Service Public.

- [Règlement d'une succession — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/N171?lang=fr)
- [Indivision entre héritiers — Service Public](https://www.service-public.gouv.fr/particuliers/vosdroits/F1296)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Décrypter un courrier de règlement de succession et produire une liste de pièces, de points à éclaircir et de décisions à ne pas confondre.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] L'option successorale, le partage et la déclaration fiscale sont traités comme des tâches distinctes ; aucun partage définitif n'est calculé sur un dossier incomplet.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Un héritier est invité à signer un document qu'il ne comprend pas.
- Une succession comporte des dettes mal identifiées.
- Des héritiers sont en désaccord sur l'occupation ou la vente d'un bien.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Complément à découper — frictions bancaires

Points 86–88 de la [matrice utilisateur](dom-004-annexes/dom-004-frictions-utilisateurs.md) :
prévoir une tâche bornée de lecture des frais et demandes bancaires d'une
succession, et une tâche de recherche de comptes oubliés. Pièces : date du
décès, qualité de l'héritier, avoirs et produits concernés, tarif daté,
décompte des frais et échanges ; notifications de transfert pour la recherche.
Sorties : tableau avoir/frais/fondement à vérifier, demande de justification
ou de restitution, et liste des recherches utiles avec interlocuteurs.

- [ ] Le futur découpage distingue frais bancaires successoraux, honoraires du notaire et fiscalité ; la frontière DOM-004 garde ici le décompte successoral.
- [ ] Un décompte sans détail ou une gratuité revendiquée reçoit une demande de pièces et une vérification du régime à la date pertinente, sans plafond ni gratuité affirmés sans texte lu.
- [ ] La recherche de comptes distingue banque et Ciclade, qualité du demandeur et assurance-vie (INS-011) ; aucun accès promis aux fonds.

Cas à prévoir : frais successoraux globaux sans assiette ; héritier invoquant
une modification de droit de 2026 ; compte ancien sans preuve de transfert.
L'affirmation du texte utilisateur sur une décision constitutionnelle de juin
2026 reste à vérifier dans la décision officielle et ses effets dans le temps.
Rechercher aussi les textes bancaires et tarifs applicables ; aucun droit
nouveau ni suppression de droit déduit de ce seul texte. Ce cadrage reste
`proposee` : aucune story d'implémentation successorale créée ici.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 33, 55–89, 99, 117, 120–122, 137 de la [matrice](dom-031-annexes/dom-031-frictions-utilisateurs.md). Tâches candidates à découper ; aucune nouvelle capacité livrée.

- [ ] Découper séparément option/sommation/acceptation tacite, acceptation à concurrence de l’actif net et inventaire, renonciation avec descendants mineurs, dette découverte et créance réclamée. Entrées : décès, qualité, actes, notification/réception, actif/passif et preuves ; sortie : choix à faire vérifier, pièces et échéances propres, sans option conseillée.
- [ ] Préciser les tâches bancaires candidates : facture obsèques/règlement direct, carte et procuration, compte joint et propriété des fonds, frais/tarifs datés, petite succession, recherche FICOBA/Ciclade, coffres et opérations autour du décès. Aucun accès automatique aux comptes ; aucun seuil, plafond ou effet d’une décision constitutionnelle de 2026 annoncé sans source officielle lue.
- [ ] Découper inventaire/remise des effets, donations et testament omis, évaluations, comptes d’indivision, pouvoirs sur une vente et contestation du partage. Entrées : acte, titulaires, accords, évaluations, recettes/dépenses et dates ; sortie : tableau documenté et questions, sans partage calculé ni recel établi.
- [ ] Découper droits du conjoint au logement et manifestation de volonté, séparés du transfert du bail DOM-006 et du statut du couple DOM-013 ; fiscalité chez DOM-011 et réclamation notariale chez DOM-041.
- [ ] Ajouter une tâche candidate de lecture du contrat de révélation d’un généalogiste : identité, mission, mandat allégué, information successorale et honoraires ; aucune dette ni authenticité admise sans pièce. DOM-001 garde les questions générales de consentement, DOM-002 une infraction alléguée.

Scénarios supplémentaires **attendus, non exécutés** : sommation reçue alors que la déclaration fiscale approche ; vente d’un objet avant connaissance du passif ; inventaire manquant après une acceptation protégée ; compte joint dont fonctionnement et propriété sont confondus ; facture d’un généalogiste inconnu ; conjoint menacé d’un départ immédiat.

Sources à ouvrir lors de l’implémentation : Code civil successions/option/indivision/logement, procédures et formalités, Code monétaire et financier paiement des obsèques/frais/recherches, décisions officielles avec effets temporels ; ne pas fusionner délais civils, fiscaux et bancaires.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](dom-031-annexes/dom-031-frictions-verification.md).
