---
id: EXIST-003
titre: "Découper l'adaptation de la protection des données"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-003 — Découper l'adaptation de la protection des données

## Objectif

Faire du droit applicable en France, du RGPD et de la loi Informatique et Libertés le cadre des tâches de protection des données.

## Points de départ

- [privacy-legal/skills/dsar-response/SKILL.md](../../privacy-legal/skills/dsar-response/SKILL.md)
- [privacy-legal/skills/dpa-review/SKILL.md](../../privacy-legal/skills/dpa-review/SKILL.md)
- [privacy-legal/skills/pia-generation/SKILL.md](../../privacy-legal/skills/pia-generation/SKILL.md)
- [privacy-legal/skills/use-case-triage/SKILL.md](../../privacy-legal/skills/use-case-triage/SKILL.md)
- [privacy-legal/references/currency-watch.md](../../privacy-legal/references/currency-watch.md)

## Travail attendu

- Séparer exercice des droits, sous-traitance, AIPD, qualification d'un traitement et suivi de conformité.
- Rechercher les hypothèses américaines présentes dans les profils, exemples et grilles, même lorsque le workflow est déjà compatible avec le RGPD.
- Identifier les compléments français, les rôles, les données sensibles, transferts et secteurs particuliers à couvrir par des références ciblées.
- Sources à prévoir et à vérifier lors des futures implémentations : EUR-Lex, CNIL, loi Informatique et Libertés, CEPD et jurisprudence pertinente ; vérifier chaque délai selon son événement déclencheur.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `privacy-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Complément des frictions IA — 16 octobre 2026

La [matrice IA](exist-005-frictions-utilisateurs.md) ajoute [PRV-035](suites/prv-035-opposition-hors-prospection.md), parcours du demandeur pour une opposition hors prospection, notamment entraînement ou profilage. PRV-023 garde la prospection et PRV-007 la réponse organisme. Le découpage courant passe à 35 suites proposées ; les décomptes des bilans antérieurs décrivent leur lot. PRV-031 précise rôle humain réel, score et information intelligible ; PRV-022 précise copies et destinataires. La réponse à une violation de données côté organisme reste à découper, distincte de PRV-032 côté victime et de la fiche incident IA-023. [Contrôles de ce complément](exist-005-frictions-verification.md).

## Vérification

Préparer des scénarios de demande d'accès, contrat de sous-traitance et traitement de données de santé ; un opt-out américain ne doit pas être appliqué par défaut.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire complet](exist-003-inventaire-donnees.md) : 23 fichiers dont
  9 skills, profils, exemples, grilles inline, références, sorties attendues,
  connecteurs et dépendances croisées. Chaque tâche et fichier a une décision
  motivée ; identifiants techniques conservés.
- [Découpage PRV-001 à PRV-021](exist-003-decoupage-donnees.md) : 21 propositions
  d'implémentation avec fichiers, entrées, résultats bornés, sources à rechercher,
  exclusions et cas normaux/limites. Demande d'accès côté particulier séparée
  de la réponse organisme ; droits, traitement, AIPD, sous-traitance, transferts
  et suivi ont des résultats distincts.
- [Vérification documentaire](exist-003-verification.md) sur demande d'accès,
  contrat de sous-traitance et suivi de santé fictifs, avec contrôle de l'absence
  d'opt-out américain par défaut. Cette relecture par le rédacteur vérifie le
  cadrage, pas les futurs résultats juridiques des skills.
- [Résultats statiques et empreintes](exist-003-resultats.json) : couverture,
  identifiants/dépendances, liens, copies communes et périmètre ; plugin et
  contenu éditeur inchangés, travaux EXIST-001/002 préservés.
- Bilan PILOTE-003 terminé après BASE-011 : préalable satisfait, sans choix
  d'extension. Les 21 PRV restent `proposee` ; les limites H01 complet et
  lecteur indépendant du pilote restent consignées.

Fichiers du lot : présente story, inventaire, découpage, vérification,
résultats JSON, 21 propositions `suites/prv-*.md` et index `backlog/README.md`.
Le lot reste sous `backlog/`, sans entrée NOTICE selon CLAUDE.md.

**Portée :** cadrage sur le checkout, relecture par l'agent de maintenance sur
pièces fictives et contrôles statiques ; aucune source juridique externe lue,
aucun délai ou raisonnement juridique validé, aucun skill adapté/exécuté,
installation/client ou lecteur réel/indépendant testé, connexion, envoi,
effacement, signature ou déploiement. Les suites portent leurs futures recherches
et recettes, sans annonce de fonctionnalité France/UE déjà disponible.

## Complément de besoins — registres d'entreprise, 16 octobre 2026

Les points 10 et 21 de la [matrice formalités](exist-002-frictions-utilisateurs.md) ajoutent une frontière pour les suites PRV : non-diffusion de données de registre, occultation d'adresse et extraits d'actes doivent être vérifiés dans le parcours sociétés/EI (SOC-023/024 ou DOM-039). Une demande de droits concernant la réutilisation par un annuaire privé constitue une autre tâche ; le parcours du demandeur au-delà de l'accès PRV-001 reste à découper. PRV-004/005/007 traitent le côté organisme et ne doivent pas être présentés comme des démarches déjà disponibles pour le dirigeant. Identifier registre, acte, donnée, demandeur, réutilisateur et finalité ; aucune suppression universelle de l'adresse publique ni confidentialité de comptes déduite du RGPD. Ce complément n'adapte pas le plugin ; portée : matrice.

## Complément des frictions données personnelles — 16 octobre 2026

La [matrice des 60 points](exist-003-frictions-utilisateurs.md) et son [archive source](sources/donnees-personnelles-frictions-2026-10-16.txt) complètent les parcours du demandeur : PRV-022 à PRV-034 ajoutent treize propositions au [découpage désormais de 34 suites](exist-003-decoupage-donnees.md). Rectification, opposition commerciale, effacement et limitation sont séparés de la réponse organisme ; collecte, traceurs, publications, surveillance, décision automatisée, fuite, relance et dossier CNIL ont chacun un résultat borné. PRV-028 traite la copie d'annuaire privé évoquée dans le complément registres ci-dessus.

Les régimes médicaux, professionnels, bancaires, de registre et de procédure gardent leurs propriétaires et leurs tâches encore à découper. Correction de routage : santé/dossier médical → DOM-007 ; DOM-009 porte les douanes. Le découpage courant est corrigé ; les mentions DOM-009 dans l'inventaire et la vérification historiques sont conservées comme traces du lot initial, avec le présent erratum.

Les chiffres et règles fournis restent à vérifier lors des implémentations. Contrôles et portée dans le [relevé distinct](exist-003-frictions-verification.md), sans modification des preuves historiques ni du plugin.
