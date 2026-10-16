---
id: SAN-001
titre: "Préparer une demande d'accès au dossier médical par le patient"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008]
---

# SAN-001 — Préparer une demande d'accès au dossier médical par le patient

## Objectif et résultat attendu

Un patient majeur qui veut obtenir les informations de santé le concernant
sait à qui s'adresser, quelles informations viser, quelles pièces joindre et
ce qui reste à vérifier, et obtient un brouillon de demande. Cette tranche
crée le paquet `health-legal` avec ce seul skill.

## Périmètre et fichiers

Plugin principal : `health-legal` (`judge-fr-eu-health-legal`). Les chemins
« à créer » sont des livrables futurs.

- `health-legal/.claude-plugin/plugin.json` — manifeste, version `0.1.0` (à créer)
- `health-legal/README.md` — tâche livrée, public, garde-fous, limites (à créer)
- `health-legal/CLAUDE.md` — modèle minimal, aucun profil requis (à créer)
- `health-legal/NOTICE` — entrée datée du lot (à créer)
- `health-legal/LICENSE` — copie de la licence du dépôt (à créer)
- `health-legal/references/shared/research-citation-method.md` — copie BASE-005 identique (à créer)
- `health-legal/references/isolation.md` — copie BASE-008 identique (à créer)
- `health-legal/scripts/judge_store.py` — copie BASE-008 identique (à créer)
- `health-legal/references/company-profile-template.md` — copie BASE-008 identique (à créer)
- `health-legal/references/dashboard-template.md` — copie BASE-008 identique (à créer)
- `health-legal/references/qualification-sante.md` — qualification commune et garde-fous (à créer)
- `health-legal/references/acces-dossier.md` — régime d'accès du patient, sources lues, réserves (à créer)
- `health-legal/skills/medical-record-request/SKILL.md` — le skill (à créer)
- `health-legal/skills/medical-record-request/references/demande-acces.md` — modèle de demande (à créer)
- `.claude-plugin/marketplace.json` — entrée du plugin, après décision explicite
- `scripts/test-base008-isolation.py` — décompte des paquets, après la même décision
- `NOTICE` — entrée racine du lot

Le skill n'utilise aucun stockage durable ; les copies BASE-008 sont
présentes pour le contrat de paquet.

## Pièces et informations nécessaires

- Qualité : patient majeur agissant pour lui-même ; aucune mesure de protection connue.
- Structure : nom, adresse, statut public ou privé s'il est connu, service ou professionnel.
- Informations visées : période, séjour ou consultation, nature (comptes rendus, résultats, imagerie, courriers).
- Mode de communication souhaité : consultation sur place ou copie, support.
- Pièce d'identité à joindre ; demande antérieure et réponse s'il y en a.

## Sortie attendue

1. Résumé : à qui demander, quoi, comment, en quelques phrases.
2. Fiche de qualification : demandeur, structure, statut établi ou à vérifier, informations visées, période.
3. Pièces à joindre.
4. Brouillon de demande, sans délai ni coût affirmé faute de source lue.
5. Ce qui reste à vérifier : modalités, délai et frais éventuels, avec la source lue ou réservés.
6. Suites : sans réponse ou réponse incomplète → SAN-004 ; volet RGPD distinct → PRV-001.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `qualification-sante.md` et `acces-dossier.md` selon le
[découpage](../dom-007-annexes/dom-007-decoupage-sante.md) et les appliquer :

- parent, représentant, proche ou personne de confiance → qualification puis SAN-002 ;
- ayant droit d'un patient décédé → SAN-003 ;
- hospitalisation sans consentement en cause → modalités à rechercher, orientation SAN-010 ;
- médecine du travail, assureur, caisse, structure médico-sociale → orientation, régime non traité ;
- soupçon de consultation injustifiée → objet distinct, PRV-001 ou PRV-025.

Charger la méthode locale BASE-005 et citer les sources réellement lues.

## Références métier et sources à rechercher

Code de la santé publique, accès aux informations de santé (pistes L1111-7,
R1111-1 et suivants) et obligations des établissements (piste L1112-1) ;
pour un établissement public, articulation avec le Code des relations entre
le public et l'administration à vérifier.

## Critères d'acceptation

- [ ] A01 qualifie un patient majeur et produit un brouillon adressé à la bonne structure, sans délai non sourcé.
- [ ] A02 détecte une demande d'un proche et ne produit pas de demande avant que la qualité soit établie.
- [ ] A03 sépare la copie du dossier et le soupçon de consultation en deux objets.
- [ ] La sortie se comprend sans formation juridique ; le paquet détaché fonctionne seul.
- [ ] La sortie se termine par la phrase BASE-013 nommant l'établissement, une association d'usagers ou un avocat selon la situation.

## Vérification

- Cas normal : A01 — Patiente majeure demandant la copie du compte rendu d'une opération dans une clinique privée.
- Cas limite : A02 — Fils demandant le dossier de sa mère vivante, sans mesure de protection connue.
- Cas limite : A03 — Copie du dossier demandée et soupçon qu'un collègue soignant l'a consulté.
- Sans source lue : fiche et brouillon, délais et frais réservés.

Exécuter sur fixtures, conserver ressources lues, sorties et erreurs, et
appliquer les couches BASE-006. La [relecture DOM-007](../dom-007-annexes/dom-007-verification.md)
porte sur le cadrage ; ces scénarios restent **attendus, non exécutés**.

## Hors périmètre

Autres qualités de demandeur, relance et contestation, hospitalisation sans
consentement, dossiers détenus hors établissement ou professionnel de santé,
droits RGPD, lecture médicale des pièces, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Préalable PILOTE-003 satisfait après
BASE-011 ; aucune tranche sélectionnée. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).
