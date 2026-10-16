---
id: PRV-035
titre: "Préparer une opposition à un traitement hors prospection"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-003, PILOTE-003, BASE-005, BASE-006]
---

# PRV-035 — Préparer une opposition à un traitement hors prospection

## Objectif et résultat attendu

Une personne obtient une fiche et un brouillon d'opposition motivée à une finalité déterminée hors prospection, notamment entraînement ou profilage. Points 9–12, 14 et 36 de la [matrice IA](../exist-005-annexes/exist-005-frictions-utilisateurs.md) ; point 31 de la [matrice données](../exist-003-annexes/exist-003-frictions-utilisateurs.md). PRV-023 conserve la prospection ; PRV-007 conserve la réponse côté organisme.

## Périmètre et fichiers

Plugin principal : `privacy-legal` (`judge-fr-eu-privacy-legal`).

- `privacy-legal/skills/processing-objection/SKILL.md` : nouveau parcours proposé à créer.
- `privacy-legal/references/opposition-hors-prospection.md` : référence locale à créer.
- README et seuls blocs de routage concernés de CLAUDE.md ; examiner access-request et les contrats PRV-026/033, sans exécution préalable.

Appliquer le [contrat commun données](../exist-003-annexes/exist-003-decoupage-donnees.md), méthode BASE-005 locale, BASE-006 et BASE-008. Pièces manuelles et réponse ponctuelle sans profil professionnel, connecteur ou plugin voisin. Synchroniser les métadonnées modifiées et NOTICE racine/local lors de l'implémentation.

## Entrées nécessaires

Responsable connu/supposé, traitement et finalité, données/source, base revendiquée ou inconnue, information reçue et version, situation particulière et motifs de la personne, réglages, demandes et réponses datées. Ne pas demander d'informations sensibles sans nécessité.

## Travail attendu

Vérifier d'abord le régime de l'opposition hors prospection selon base/finalité et situation particulière. Rédiger un brouillon ciblé avec faits, motifs, informations manquantes, demande et interlocuteur à vérifier. Séparer opposition, retrait d'un consentement, option technique, effacement et limitation ; les autres droits restent dans leurs parcours. Base inconnue : demande de clarification et branches conditionnelles, sans droit absolu à l'arrêt présumé. Identifier les motifs de maintien à instruire et préparer le suivi PRV-033 sans anticiper leur bien-fondé. Pour entraînement IA, distinguer collecte future, réutilisation, données conservées et modèle existant ; aucune suppression universelle ni désapprentissage garanti. Le recours contre une décision affectant la personne suit son propre calendrier.

## Sources à rechercher

RGPD, LIL, CNIL/CEPD et jurisprudence officielle sur opposition, bases invoquées, garanties et entraînement/profilage selon faits. Vérifier conditions, exceptions, réponse et éventuelle limitation ; source/version, réception prouvée, déclencheur et échéance calculable ou inconnue. Aucun délai repris automatiquement du document fourni.

## Critères d'acceptation

- [ ] Brouillon limité à une finalité, avec motifs personnels nécessaires, responsable et questions utiles.
- [ ] Opposition hors prospection, retrait et effacement distingués ; absence de consentement ne suffit pas à qualifier le traitement.
- [ ] Base inconnue ou source inaccessible réserve la conclusion dépendante tout en fournissant une démarche utile.
- [ ] Calendrier propre documenté, sans suspension présumée des recours au fond ni effacement garanti du modèle.
- [ ] Paquet isolé avec références locales, sans profil obligatoire ; aucun envoi annoncé exécuté.
- [ ] La sortie applique BASE-013 avec professionnel compétent et urgence si nécessaire.

## Vérification

- Cas normal : F03, fournisseur invoquant intérêt légitime pour entraînement ; brouillon motivé et questions sur finalité/portée, sans résultat garanti.
- Cas limite : base non précisée, bouton d'opposition inaccessible ; conserver l'obstacle et préparer clarification par un canal officiel à vérifier.
- Traitement revendiqué fondé sur consentement : expliquer la branche de retrait pertinente sans renommer tout retrait « opposition ».

Recette future BASE-006 : sorties, paquet détaché, client et compréhension ; [contrôles documentaires](../exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Réponse côté organisme, prospection, audit complet de base légale, entraînement arrêté, effacement du modèle ou envoi d'une réclamation.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions IA ; `proposee`, préalable PILOTE-003 satisfait, sans sélection d'implémentation.
