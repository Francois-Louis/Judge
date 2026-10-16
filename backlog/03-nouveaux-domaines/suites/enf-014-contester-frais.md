---
id: ENF-014
titre: "Préparer la contestation de frais d'un commissaire de justice"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001, ENF-003]
---

# ENF-014 — Préparer la contestation de frais d'un commissaire de justice

## Objectif et résultat attendu

Une personne qui reçoit une facture ou un décompte prépare une demande motivée d'explication ou de révision des frais et identifie la voie de contestation à faire vérifier.

## Périmètre et fichiers

- `enforcement-legal/skills/fee-dispute-preparation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/contestation-frais.md` — qualification, pièces, modèle de sortie et sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

Le paquet et `qualification-acte.md` sont créés par ENF-001. Chaque référence consommée est embarquée dans le paquet ; aucun plugin voisin n'est requis. Appliquer le contrat commun du [découpage](../dom-003-decoupage-execution.md).

## Pièces et informations nécessaires

Facture et décompte détaillés ; actes facturés avec leurs dates ; titre et décision sur les dépens ; devis ou convention ; qualité de client, débiteur ou créancier ; paiements et réclamations.

## Sortie attendue

Tableau ligne, prestation, date, type de prix, fondement, charge et écart documenté ; brouillon au professionnel ; interlocuteur et voie de vérification ou de contestation à confirmer ; urgence du recours sur la mesure conservée à part.

## Travail attendu

ENF-003 possède le rapprochement des paiements et la demande de ventilation. Ici, qualifier frais amiables, émoluments, débours et honoraires libres ; rechercher tarif et dispositions transitoires selon la date pertinente. Examiner utilité et répétition des actes sans en déduire automatiquement une faute. Distinguer vérification des dépens, contestation d'honoraires et litige sur l'exécution : ne pas attribuer universellement toute facture au greffe ou au JEX. Frais bancaires : BNK-003. Réclamation professionnelle : ENF-015.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, charge et nécessité des frais (piste L111-8) ; Code de commerce et arrêtés tarifaires applicables aux dates pertinentes ; Code de procédure civile, vérification et taxe des dépens ; règles propres aux honoraires libres. Le tarif annoncé pour 2026–2028 dans le texte utilisateur reste à vérifier.

## Critères d'acceptation

- [ ] Le cas normal produit la sortie utile avec chaque fait attribué à sa pièce ou marqué comme déclaré.
- [ ] Le cas limite explicite les manques et distingue les procédures sans promettre d'issue favorable.
- [ ] Aucune règle, somme, compétence ou échéance n'est affirmée sans source lue et faits nécessaires ; un point réservé garde une action utile.
- [ ] Le résultat est compréhensible sans formation juridique ; le paquet installé seul contient les références et la méthode BASE-005 nécessaires.

## Vérification

- Cas normal : F01 — Deux actes présentés comme identiques et un tarif sans référence : demander les pièces et motiver les postes contestés sans décider de leur inutilité.
- Cas limite : F02 — Facture de constat commandé par le client avec déplacement et honoraires libres : ne pas appliquer le tarif d'un acte réglementé ni la même voie de contestation par défaut.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Calculateur général de tarifs ou intérêts, acte de saisine, contestation de la saisie elle-même, envoi.

## État de la proposition — 16 octobre 2026

Issue des points 41–43 de la [matrice des frictions](../dom-003-frictions-utilisateurs.md). Exigence de backlog, sans sélection ni implémentation.
