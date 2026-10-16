---
id: SOC-024
titre: "Qualifier une modification de société et ses pièces manquantes"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-024 — Qualifier une modification de société et ses pièces manquantes

## Objectif et résultat attendu

Fiche d'un seul changement : faits avant/après, décision et pouvoirs à vérifier, registres affectés, pièces par étape, destinataire et échéance établis ou réservés.

Issue des [frictions sur les formalités d'entreprise](../exist-002-annexes/exist-002-frictions-utilisateurs.md), points 14–15, 19, 21, 24–31. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : corporate-legal. `corporate-legal/skills/entity-compliance/SKILL.md` : lecture d'un événement ; référence locale `modification-societe.md` à créer. SOC-004/005/006 restent propriétaires du registre, des preuves et du rapport.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

SAS/SASU ou SARL/EURL, extrait de registre daté, événement unique, décision et date, statuts à jour et antérieurs utiles, établissements, contrôle et bénéficiaires déclarés, publications, dépôts et mandat éventuels.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Qualifier un événement fourni : adresse, dirigeant, activité, établissement, répartition du capital ou données de bénéficiaire effectif. Séparer changement de siège et d'établissement, code APE et activité réelle, statut et pacte, acte social et enregistrement fiscal. Demander la chaîne décision/acte/publication/dépôt/validation propre au cas sans imposer toutes les étapes à chaque modification. Qualifier explicitement la société unipersonnelle. Distinguer publication légale et réutilisation de l'adresse par un tiers ; vérifier le mécanisme propre avant de préparer une demande. Chaque rédaction ou dépôt de fond reste une tranche séparée.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code civil, Code de commerce et textes de formalités/publicité/bénéficiaires effectifs ; INPI, INSEE et registre compétent ; fiscalité d'enregistrement en relais DOM-011.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : SARL changeant de gérant : décision fournie mais extrait ancien et aucune preuve de dépôt. Distinguer nomination documentée et registre non actualisé.
- Cas limite : SASU changeant d'adresse personnelle et de lieu d'activité : demander ce qui concerne siège, établissement et bénéficiaire ; ne pas déduire une formalité unique. Cession avec contrôle incertain : pas de déclaration préremplie.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Rédiger tout acte modificatif, déposer ou payer une formalité, valider une cession, calculer les droits fiscaux ou adapter le registre de SOC-004.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../exist-002-annexes/exist-002-frictions-verification.md).
