---
id: ENF-004
titre: "S'orienter face à une saisie sur compte bancaire"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-003, PILOTE-003, BASE-005, BASE-006, ENF-001]
---

# ENF-004 — S'orienter face à une saisie sur compte bancaire

## Objectif et résultat attendu

Une personne dont le compte est saisi comprend la mesure, les sommes qui
peuvent rester disponibles selon la source lue, les démarches à vérifier et
les interlocuteurs.

## Périmètre et fichiers

- `enforcement-legal/skills/bank-seizure-orientation/SKILL.md` — le skill (à créer)
- `enforcement-legal/references/saisie-compte.md` — mesures, sommes protégées, interlocuteurs, sources lues (à créer)
- `enforcement-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Dénonciation ou avis de la banque ; émetteur ; titre visé ; comptes concernés ;
nature des sommes versées (salaire, prestations) ; date de la mesure.

## Sortie attendue

Nature de la mesure ; sommes à demander à la banque et justificatifs ;
contestation possible à vérifier et juge compétent à identifier, sans délai
calculé ; questions ; limites.

## Travail attendu

Distinguer saisie par commissaire de justice et saisie administrative à tiers
détenteur (régime propre, fond à DOM-011 ou DOM-002). Frais de la banque →
DOM-004. Plusieurs saisies ou dettes → DOM-024. Aucun conseil de vider ou
déplacer le compte.

## Références métier et sources à rechercher

Code des procédures civiles d'exécution, saisie-attribution et solde
insaisissable (pistes L211-1 et suivants, R162-2) ; juge de l'exécution
(piste L213-6 du Code de l'organisation judiciaire).

## Critères d'acceptation

- [ ] B01 explique la mesure et les sommes à demander, sans montant non sourcé.
- [ ] B02 distingue la saisie administrative et oriente le fond.

## Vérification

- Cas normal : B01 — Compte bloqué après une saisie-attribution ; prestations familiales versées sur ce compte.
- Cas limite : B02 — Saisie administrative à tiers détenteur pour une amende.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Contestation rédigée, mainlevée, relations avec la banque au-delà de la
demande, envoi.

## Complément issu des frictions bancaires

Points 71–74 de la [matrice utilisateur](../dom-004-frictions-utilisateurs.md).

- [ ] B03 — Solde devenu indisponible : recueillir solde, mouvements, origine des prestations et justificatifs ; distinguer minimum protégé, sommes insaisissables et limites liées aux fonds présents, selon les sources lues.
- [ ] B04 — SATD ou saisie-attribution : frise acte/notification/réception, autorité et canal de contestation à vérifier ; ne pas appliquer le délai d'une procédure à l'autre ni calculer sur une date inconnue.
- [ ] B05 — Demande de mainlevée ou d'échéancier : identifier l'autorité à contacter et les pièces à préparer, sans rédiger la contestation ni réaliser la mainlevée.

Scénarios B03–B05 **attendus, non exécutés** : prestations identifiables sur
un compte bloqué ; avis de SATD et dénonciation civile confondus ; créancier
prêt à examiner un échéancier. Sources supplémentaires à rechercher : régime
de la SATD, justificatifs et mise à disposition des sommes protégées, délais
et destinataires propres à chaque contestation. Frais bancaires → BNK-003 ;
les montants du document utilisateur ne sont pas des barèmes validés.

## Complément issu des frictions des commissaires de justice

Points 19–25 de la [matrice utilisateur](../dom-003-frictions-utilisateurs.md), en complément de B03–B05 issus de la banque.

- [ ] B06 — Compte bloqué avant découverte de l'acte : recueillir date de saisie auprès de la banque, acte de dénonciation, mode de remise et titre ; distinguer indisponibilité, attribution et versement sans déclarer l'information tardive irrégulière par principe.
- [ ] B07 — Compte joint : recueillir titulaires, débiteur visé, régime matrimonial pertinent, origine et propriété des fonds ; conserver preuves de versements et orienter les questions du cotitulaire.
- [ ] B08 — Document de renonciation ou de versement anticipé : restituer son contenu, l'objectif déclaré et les effets possibles à vérifier ; ne pas recommander sa signature pour obtenir un prétendu simple déblocage.
- [ ] B09 — Recours bancaire civil : expliquer que l'échange avec l'étude ne remplace pas la voie judiciaire ; ENF-019 possède le dossier et la checklist de contestation. Ne pas transposer cette procédure à une SATD.

Scénarios B06–B09 **attendus, non exécutés** : blocage sans acte encore disponible ; fonds du conjoint non débiteur sur compte joint ; renonciation présentée comme déblocage ; attente d'une réponse alors que la dénonciation est disponible. Sources supplémentaires à rechercher : dénonciation, cotitulaires, régime matrimonial, effets du consentement et des recours. Vérifier séparément SBI, prestations protégées et délai de justificatifs avec son unité ; aucun montant du texte utilisateur n'est repris comme règle.

## État de la proposition — 16 octobre 2026

Issue de DOM-003, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-003-decoupage-execution.md).
