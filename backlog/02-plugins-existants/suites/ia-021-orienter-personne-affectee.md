---
id: IA-021
titre: "Orienter une personne affectée par une décision ou un usage IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-021 — Orienter une personne affectée par une décision ou un usage IA

## Objectif et résultat attendu

Une personne ou son aidant obtient une fiche d'orientation à partir d'un refus, d'un score, d'un contenu ou d'un échange contesté : faits connus, demandes distinctes, pièces, interlocuteurs à vérifier et prochaine action. Points 1–8, 19–29, 48–50 de la [matrice des frictions](../exist-005-annexes/exist-005-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).

- `ai-governance-legal/skills/affected-person-intake/SKILL.md` : parcours proposé à créer.
- `ai-governance-legal/references/orientation-personne-affectee.md` : référence locale à créer.
- README et seuls blocs d'annonce/routage concernés de CLAUDE.md ; examiner use-case-triage sans imposer son parcours organisation.

Appliquer le [contrat commun IA](../exist-005-annexes/exist-005-decoupage-ia.md), USAGE-001, BASE-008 et la méthode BASE-005 embarquée. Ni compte professionnel, profil, inventaire IA-001, connecteur ni exécution d'un plugin voisin requis. Références autonomes ; annonces et métadonnées modifiées synchronisées ; NOTICE racine/local lors de l'implémentation.

## Entrées nécessaires

Récit, objectif recherché, secteur, personne concernée et mandat éventuel, décision ou contenu, auteur connu/supposé, notification et réception, effets, démarches et réponses. Accepter les inconnues et une description sans preuve technique d'IA.

## Travail attendu

- Repérer d'abord mesure en cours, date de recours possible, atteinte intime ou fraude ; orienter vers le professionnel et le canal pertinents sans attendre une qualification complète de l'IA.
- Séparer explication du système, accès/correction de données, signalement réglementaire, contestation au fond et réparation. Une fiche par objectif, avec domaine propriétaire et statut réel du relais.
- Préparer un tableau des démarches et calendriers : acte, source/version, compétence, préalable, déclencheur et réception prouvés, effet sur les autres délais vérifié ou inconnu. Sans faits suffisants, prochaine vérification explicite et aucun calcul par défaut.
- Si une discrimination est alléguée, DOM-029 garde qualification et dossier d'indices ; travail, banque, école ou autre secteur conservent la contestation de leur décision, avec calendrier distinct.
- Remettre un dossier minimal transmissible manuellement : question, faits et pièces, dates, hypothèses et points ouverts. PRV-031 garde le brouillon relatif à la décision automatisée ; le secteur garde son recours. Un relais absent donne les questions et pièces utiles, pas un appel vers une branche héritée.

## Sources à rechercher

Textes officiels du règlement IA pour les seuls droits et compétences utiles ; RGPD/LIL et CNIL pour données ; CRPA/CJA/CADA pour accès administratif ; règles sectorielles et sites officiels des autorités selon objectif. Vérifier à la date des faits champ, exceptions, procédure et canal. Le calendrier et les autorités du texte utilisateur restent à contrôler ; CNIL et CADA ne sont pas des recours universels.

## Critères d'acceptation

- [ ] Un particulier sans vocabulaire juridique identifie sa prochaine action et les pièces utiles.
- [ ] Demande d'information et recours contre la décision apparaissent séparément, sans effet suspensif présumé d'un ticket ou signalement.
- [ ] Une intervention humaine n'est proposée comme droit qu'après vérification de son régime ; l'IA n'est pas déduite du seul refus.
- [ ] Le paquet isolé fonctionne avec pièces manuelles et références locales ; profil et relais absents ne bloquent pas l'orientation.
- [ ] Aucun envoi, recours déposé, délai préservé ou retrait obtenu n'est annoncé sans preuve.
- [ ] La sortie applique BASE-013 : rappel court avec professionnel compétent nommé, renforcé en tête en cas d'urgence.

## Vérification

- Cas normal : F01/F12, refus opaque et réponses automatiques répétées ; fiche séparant demande de données, contestation et escalade pertinente.
- Cas limite : F02/F06, décision publique et date de réception manquante ; régime sectoriel à établir, pas de délai générique calculé.
- Sans preuve d'automatisation : conserver le problème réel et les questions au décideur, sans inventer un système.

Recette future BASE-006 : fixtures, sorties, paquet détaché, client et compréhension. Aucun scénario métier exécuté dans cette intégration ; [contrôles documentaires](../exist-005-annexes/exist-005-frictions-verification.md).

## Hors périmètre

Rédiger tous les recours, qualifier définitivement discrimination ou infraction, authentifier une image, certifier la conformité ou accomplir une démarche externe.

## État de la proposition — 16 octobre 2026

Issue des 50 frictions ; `proposee`, sans sélection de tranche. PILOTE-003 est terminé ; ses limites demeurent consignées.
