---
id: DOM-025
titre: "Cadrer un plugin handicap et autonomie"
statut: proposee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-025 — Cadrer un plugin handicap et autonomie

## Objectif

Aider les personnes concernées et les aidants à comprendre une décision et à faire valoir un besoin d'accessibilité ou d'accompagnement.

Nom de plugin proposé : `disability-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Lire une décision liée au handicap ou à l'autonomie et préparer les pièces manquantes.
- Préparer une demande d'aménagement ou d'accès à un service.
- Orienter un désaccord concernant l'accompagnement à domicile ou en établissement.

## Qualification et frontières

Auteur de la décision, demande précise, qualité du représentant, dates, besoins exprimés, justificatifs strictement utiles et recours déjà tenté.

La reconnaissance et l'accompagnement sont ici ; le calcul d'une prestation par une caisse se coordonne avec DOM-012, la scolarité avec DOM-027, l'emploi avec le plugin travail et la capacité juridique avec DOM-026.

## Sources à prévoir et vérifier

Code de l'action sociale et des familles, textes sur l'accessibilité, Code de la sécurité sociale selon l'objet et sources officielles des organismes compétents.

- [Mon Parcours Handicap](https://www.monparcourshandicap.gouv.fr/)
- [Défenseur des droits](https://www.defenseurdesdroits.fr/)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Décrypter une notification administrative choisie et préparer les questions et pièces d'une contestation, sans multiplier les procédures.

## Critères d'acceptation

- [ ] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [ ] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [ ] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [ ] La personne conserve sa place dans les choix et échanges ; handicap, incapacité juridique et pouvoir du proche ne sont pas assimilés.
- [ ] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [ ] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Une personne ne comprend pas le motif d'un refus.
- Un usager ne peut pas accéder au service prévu.
- Un aidant souhaite faire une démarche sans mandat fourni.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.

## Complément des frictions santé — 16 octobre 2026

Points 15 et 151–155 de la [matrice santé](dom-007-annexes/dom-007-frictions-utilisateurs.md).
À découper ici : demande d'aménagement d'accès, accompagnement/hébergement,
prestations contractuelles et accès aux documents sociaux d'une structure.
Recueillir volonté de la personne, besoin exprimé, structure/statut, contrat,
pièces utiles et pouvoir du proche. Résultat : questions, demande ciblée et
circuit propre à vérifier. SAN-017 garde réclamation sur les soins et demande
d'informations de santé selon régime ; SAN-009 le consentement ; DOM-026
l'étendue du pouvoir ; DOM-029 la discrimination alléguée. Aucun accès au
dossier médical par simple qualité d'aidant et aucune CDU hospitalière
appliquée automatiquement au médico-social. Sources : CASF, accessibilité,
textes propres à la structure et CSP pour la frontière soins, à ouvrir.

Scénarios **attendus, non exécutés** : cabinet inaccessible malgré demande
écrite ; proche signalant soins et accompagnement manquants en EHPAD sans
mandat. Séparer demande du résident, soins (SAN-017), accompagnement ici et
urgence avant réclamation. [Portée et contrôles](dom-007-annexes/dom-007-frictions-verification.md).

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 33–34, 127–129 de la [matrice](dom-031-annexes/dom-031-frictions-utilisateurs.md). Tâches candidates à découper ; aucune nouvelle capacité livrée.

- [ ] Prévoir une tâche candidate de contestation de la facture finale et du dépôt d’un EHPAD : établissement/régime, contrat, décès, retrait des effets, chambre libérée, états d’entrée/sortie, photos, sommes et preuves ; sortie : décompte périodes/postes/justificatifs et brouillon de demande de régularisation, sans appliquer automatiquement le bail d’habitation.
- [ ] Pour effets personnels : demander inventaire, dépositaire, destinataire et remise documentée ; DOM-016 garde la répartition successorale. Questions de soins et dossier vers DOM-007, frais funéraires/transfert vers FUN-002/008. Propriétaire proposé du volet facturation médico-sociale à confirmer lors du découpage avec DOM-007.

Scénarios supplémentaires **attendus, non exécutés** : chambre vidée mais facturation poursuivie ; dépôt retenu pour usure sans états des lieux ; inventaire de bijoux non remis aux proches.

Sources à ouvrir lors de l’implémentation : CASF et règles propres à la facturation après décès, dépôt, états des lieux et remise des effets en établissement ; contrat et statut de la structure, sans généralisation depuis la location privée.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](dom-031-annexes/dom-031-frictions-verification.md).

## Complément des frictions allocations et aides sociales — 16 octobre 2026

Points 146–147 et ligne V06 de la [matrice](dom-012-annexes/dom-012-frictions-utilisateurs.md).
SA03 reste à découper : reconnaissance handicap, renouvellement et recours
sur décision MDPH/CDAPH, avec auteur, droit demandé, notification/réception,
fin de validité, demande et preuve de dépôt. Sortie : lecture du motif,
pièces, voie préalable et calendrier propres à la décision. Le paiement,
ressources ou indu de caisse relèvent de DOM-012 même si le droit se nomme AAH.
Aucun transfert automatique de pièces ni continuité de versement garantie.

Sources futures : CASF/CSS et textes propres au droit et au recours identifié.
Cas attendus : AAH reconnue mais paiement refusé ; renouvellement déposé avec
réception incertaine avant expiration. Scénarios non exécutés ;
[portée et contrôles](dom-012-annexes/dom-012-frictions-verification.md).
