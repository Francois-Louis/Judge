---
id: EXIST-006
titre: "Découper l'adaptation des workflows de contentieux"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-006 — Découper l'adaptation des workflows de contentieux

## Objectif

Reconstruire les tâches de contentieux selon les procédures concernées, au lieu de traduire les noms des actes américains.

## Points de départ

- [litigation-legal/skills/subpoena-triage/SKILL.md](../../litigation-legal/skills/subpoena-triage/SKILL.md)
- [litigation-legal/skills/deposition-prep/SKILL.md](../../litigation-legal/skills/deposition-prep/SKILL.md)
- [litigation-legal/skills/privilege-log-review/SKILL.md](../../litigation-legal/skills/privilege-log-review/SKILL.md)
- [litigation-legal/skills/legal-hold/SKILL.md](../../litigation-legal/skills/legal-hold/SKILL.md)
- [litigation-legal/skills/demand-draft/SKILL.md](../../litigation-legal/skills/demand-draft/SKILL.md)
- [litigation-legal/skills/claim-chart/references/element-templates.md](../../litigation-legal/skills/claim-chart/references/element-templates.md)

## Travail attendu

- Classer les tâches réutilisables (chronologie, dossier, suivi) et celles nécessitant une refonte juridique.
- Décider du devenir et du nom des tâches subpoena, deposition et privilege log : absence d'équivalent automatique à documenter, tâche française à définir avant renommage.
- Séparer mise en demeure, conservation/production des preuves, rédaction d'écritures et suivi de procédure ; préciser les frontières avec pénal, administratif et exécution.
- Identifier les mentions de work product, discovery et without prejudice qui supposent une analyse de droit applicable.
- Sources à prévoir et à vérifier lors des futures implémentations : Codes de procédure selon la matière, Code civil, règles professionnelles et textes de compétence ; vérifier acte, notification et représentation.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `litigation-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios (relecture documentaire sur cas fictifs par le rédacteur).
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Utiliser une mise en demeure reçue, une demande de production de pièce et une convocation française ; aucun de ces documents ne doit déclencher mécaniquement une procédure américaine.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire exhaustif](exist-006-annexes/exist-006-inventaire-contentieux.md) : 38 fichiers,
  dont 19 skills, références, modèles inline, registre, agent et dépendances
  de sortie ; six fichiers du cookbook associés et décisions individuelles.
- [Découpage CTX-001 à CTX-024](exist-006-annexes/exist-006-decoupage-contentieux.md) : fichiers,
  entrées, résultats, sources à rechercher, exclusions et scénarios. Mise en
  demeure, conservation/communication des preuves, écritures et suivi sont
  séparés ; pénal, administratif, exécution et secteurs ont des relais précis.
- Subpoena, deposition et privilege log : aucune équivalence automatique ;
  CTX-005/010/009 définissent d'abord la tâche française et son intitulé futur,
  sans renommer les commandes dans ce lot. Work product, discovery et without
  prejudice sont localisés et traités comme points de recherche, sans effets
  juridiques déduits d'une traduction ou d'un en-tête.
- [Relecture du cadrage](exist-006-annexes/exist-006-verification.md) sur mise en demeure reçue,
  demande de production de pièces et convocation française fictives : aucune
  procédure US n'est prescrite par les suites ; pas de délai calculé.
- [Contrôles statiques et empreintes](exist-006-annexes/exist-006-resultats.json), exécutables
  avec le [contrôleur documentaire](exist-006-annexes/exist-006-controles.py). Le commentaire
  HTML du modèle `_log.yaml` est interprété comme une clé YAML parasite ;
  sa correction bornée est assignée à CTX-014 et non réalisée ici.
- PILOTE-003 est terminé après BASE-011 : préalable satisfait, sans sélection
  d'extension. Limites H01 complet et lecteur indépendant consignées. Les 24
  suites restent `proposee` ; première tranche suggérée CTX-001, non lancée.

Fichiers du lot : présente story, inventaire, découpage, vérification,
contrôleur, résultats JSON, 24 propositions `suites/ctx-*.md` et index
`backlog/README.md`. Modifications limitées à `backlog/`, sans entrée NOTICE
selon CLAUDE.md ; empreintes des plugins et des travaux EXIST précédents
préservées. Des différences simultanées sur DOM-001 et l'architecture sont
consignées séparément, sans les attribuer à EXIST-006 ou les modifier.

**Portée :** cadrage et relecture par le seul agent de maintenance sur fixtures
fictives reproduites dans la vérification, contrôles statiques. Aucune source
juridique externe consultée, règle ou échéance réelle validée, adaptation ou
exécution de skill, installation, recette client, lecteur indépendant,
connexion, envoi, renommage, publication ou déploiement. Les textes, versions,
compétences, actes, notifications, représentation et régimes de confidentialité
restent à rechercher lors des futures implémentations. Plugin, cookbook et
contenus éditeur inchangés ; aucune capacité France/UE nouvelle livrée ici.

## Décisions du 16 octobre 2026

Ajout par décision de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) du parcours du particulier qui
intente ou subit un procès civil : CTX-025 (assignation reçue), CTX-026
(saisir le juge pour un petit litige), CTX-027 (audience sans avocat) et
CTX-028 (jugement reçu). Le découpage compte désormais 28 suites.

## Complément des frictions données personnelles — 16 octobre 2026

Points 59–60 de la [matrice données personnelles](exist-003-annexes/exist-003-frictions-utilisateurs.md) : PRV-034 prépare la plainte CNIL, DOM-035 organise dommage et causalité à découper ; contentieux garde compétence, représentation, saisine et échéances de la procédure qualifiée. Les tranches CTX de petit litige ne couvrent pas automatiquement tout recours RGPD. Action indemnitaire et recours contre une décision de l'autorité doivent être qualifiés avant choix de voie et découpage spécialisé, avec DOM-010 si pertinent. Préserver le calendrier de fond indépendamment de la demande RGPD, sans suspension automatique déduite. Aucune tranche CTX lancée ; portée et contrôles dans la matrice.

## Intégration des frictions contentieuses — 16 octobre 2026

La [matrice des 125 frictions](exist-006-annexes/exist-006-frictions-utilisateurs.md) conserve l’ordre du [texte fourni](sources/contentieux-frictions-2026-10-16.txt), ses tableaux et sa checklist. Le découpage compte désormais **41 suites CTX proposées** : CTX-030 à CTX-041 ajoutent prescription civile, demandes chiffrées, mission et observations d’expertise, réponse adverse, temps de réponse, préparation de vérification d’appel TJ, erreur matérielle, omission de statuer, transaction, budget et ordonnance d’injonction côté créancier.

Les besoins administratifs, pénaux, d’exécution, de financement et de procédures collectives sont attribués à leurs domaines ; les tâches non découpées restent explicitement ouvertes. CTX-016 ne devient pas un calculateur universel et CTX-028 reste une lecture sans calcul de délai. Les assertions normatives du texte, notamment les réformes annoncées en 2026, ne sont pas validées par cette intégration. [Contrôles documentaires](exist-006-annexes/exist-006-frictions-verification.md) ; aucune tranche lancée, aucun plugin modifié. Les inventaire, vérification et résultats historiques du cadrage initial sont conservés à leur périmètre d’origine.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 140–141 et D05 de la [matrice](../03-nouveaux-domaines/dom-031-annexes/dom-031-frictions-utilisateurs.md). Tâches candidates à découper ; aucune nouvelle capacité livrée.

- [ ] Enregistrer une candidature de découpage pour saisine funéraire urgente et appel : décision contestée, volontés, qualité, corps/urne, opération prévue, autorisations, jugement et notification/réception ; sortie candidate : dossier pour l’avocat et calendrier de la procédure spéciale après recherche.
- [ ] Le point ouvert DOM-031 reste ouvert pour l’attribution finale et la tranche : FUN-003 prépare les éléments et oriente ; CTX-025/026 ne deviennent pas une saisine funéraire par simple renvoi. Ne pas assimiler délais du jugement, notification et appel ni présumer l’effet suspensif d’une démarche amiable.

Scénarios supplémentaires **attendus, non exécutés** : crémation annoncée avant résolution du conflit ; décision déjà rendue mais date de notification inconnue ; médiation proposée alors qu’une opération irréversible est imminente.

Sources à ouvrir lors de l’implémentation : CPC procédure spéciale des funérailles, compétence, saisine, délais, notification et appel ; voie et version exactes avant toute rédaction procédurale.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../03-nouveaux-domaines/dom-031-annexes/dom-031-frictions-verification.md).
