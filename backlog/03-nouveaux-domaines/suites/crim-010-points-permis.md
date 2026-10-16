---
id: CRIM-010
titre: "Lire un courrier sur les points du permis de conduire"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-002, PILOTE-003, BASE-005, BASE-006, CRIM-003]
---

# CRIM-010 — Lire un courrier sur les points du permis de conduire

## Objectif et résultat attendu

Un conducteur qui reçoit un courrier sur ses points comprend ce qu'il
annonce, d'où vient le retrait et ce qu'il peut vérifier ou demander.

## Périmètre et fichiers

- `criminal-legal/skills/licence-points-reading/SKILL.md` — le skill (à créer)
- `criminal-legal/references/points-permis.md` — courriers, relevé, sources lues (à créer)
- `criminal-legal/README.md` — ajout de la tâche livrée

`amendes.md` (CRIM-003) est relu, pas réécrit.

## Pièces et informations nécessaires

Courrier complet ; infractions et dates mentionnées ; paiements ou
condamnations liés ; relevé d'information intégral s'il existe.

## Sortie attendue

Fiche du courrier ; lien avec les infractions ; démarches de vérification ;
limites. Une invalidation ou une suspension est lue et orientée, sans recours
préparé.

## Travail attendu

Ne pas recompter un solde ni annoncer une date de récupération sans texte lu
et relevé complet. Recours contre une décision administrative : orientation à
vérifier (DOM-010).

## Références métier et sources à rechercher

Code de la route, permis à points (piste L223-1 et suivants) ; service
officiel de consultation du solde.

## Critères d'acceptation

- [ ] E01 relie le courrier aux infractions sans recompter le solde.
- [ ] E02 lit une invalidation et oriente sans préparer de recours.

## Vérification

- Cas normal : E01 — Lettre annonçant un retrait après un excès de vitesse payé.
- Cas limite : E02 — Lettre d'invalidation pour solde nul.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Recours administratif, stage, conduite sans permis.

## État de la proposition — 16 octobre 2026

Issue de DOM-002, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-002-decoupage-penal.md).
