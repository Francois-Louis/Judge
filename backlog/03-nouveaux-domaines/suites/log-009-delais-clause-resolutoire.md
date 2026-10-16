---
id: LOG-009
titre: "Vérifier les conditions d'une demande de délais et de suspension de clause"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-008]
---

# LOG-009 — Vérifier les conditions d'une demande de délais et de suspension de clause

## Objectif et résultat attendu

Un locataire en impayé comprend les conditions à rechercher pour solliciter
des délais de paiement et, si pertinente, la suspension de la clause
résolutoire. Bail privé vide de résidence principale, France métropolitaine.
La sortie prépare un rendez-vous, pas une demande judiciaire.

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/rent-relief-conditions/SKILL.md` — tâche (à créer)
- `housing-legal/references/delais-clause-resolutoire.md` — conditions, transitions et pièces (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Réutiliser qualification LOG-001 et décompte LOG-008 ; ENF-005 reste un
relais documentaire, sans dépendance d'installation.

## Pièces et informations nécessaires

Bail et clause, régime, commandement et preuve de signification, décompte
et paiements, assignation/décision éventuelles et état du procès, reprise
du loyer courant avec preuves, ressources/charges par catégories utiles,
aides sollicitées et réponses. Pas de collecte d'un dossier social complet.

## Sortie attendue

Stade et urgence ; tableau condition/source/version/fait/pièce/inconnue ;
distinction étalement amiable, délais judiciaires et suspension de clause ;
pièces et questions pour avocat ou juriste de l'ADIL. Aucune suspension ni
durée accordée annoncées ; préparation judiciaire distincte LOG-010.

## Travail attendu

Répondre aux points 35–36 de la [matrice exécution](../dom-003-annexes/dom-003-frictions-utilisateurs.md).
Lire les textes applicables et dispositions transitoires ; distinguer
conditions du pouvoir du juge, demande des parties et éléments de situation.
Reprise du loyer courant : fait à documenter, pas preuve suffisante d'un droit.
Commandement, jugement, commandement de quitter et expulsion matérielle
restent distincts ; acte et urgence → ENF-001/005. Sans pièces, réserver
la condition concernée ; ne pas reporter une consultation urgente.

## Références métier et sources à rechercher

Loi du 6 juillet 1989, clause résolutoire et délais, dispositions modificatives
et transitoires ; Code civil et procédure civile pour les demandes envisagées,
pouvoir du juge selon stade ; ANIL/ADIL et prévention locale des expulsions.
Vérifier chaque condition et exception, sans reprendre les durées d'un guide.

## Critères d'acceptation

- [ ] E01 distingue commandement et expulsion, avec routage urgent de l'acte.
- [ ] E02 documente reprise du loyer, ressources, charges et aides sans suspension automatique.
- [ ] E03 réserve une transition incertaine et oriente vers le conseil ; aucune demande judiciaire présentée comme livrée.
- [ ] Sources locales et paquet seul vérifiés selon BASE-006 ; absence de source rend la règle conditionnelle ou réservée.
- [ ] Renfort en tête pour la procédure et avocat en droit du logement nommé ; phrase finale d'information selon BASE-013.

## Vérification

- Cas normal : E02 — Loyer courant repris, arriéré restant et volonté d'étalement ; tableau de conditions et pièces pour un rendez-vous.
- Cas limite : E01 — Commandement assimilé à une expulsion immédiate ; distinguer étapes sans date de départ promise.
- Cas limite : E03 — Bail antérieur à une modification alléguée, acte récent ; rechercher dispositions transitoires, aucun régime déduit de mémoire.

Scénarios **attendus, non exécutés** ; fixtures, sorties et sources à
conserver lors des couches BASE-006.

## Hors périmètre

Autres régimes locatifs, rédaction ou dépôt de demande judiciaire, contestation
de l'acte, délais pour quitter les lieux, budget global et envoi.
