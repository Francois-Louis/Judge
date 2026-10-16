---
id: EXIST-001
titre: "Découper l'adaptation des contrats commerciaux"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-001 — Découper l'adaptation des contrats commerciaux

## Objectif

Conserver les workflows de revue, négociation et suivi en les replaçant dans les contrats français B2B et leur éventuelle dimension européenne.

## Points de départ

- [commercial-legal/skills/review/SKILL.md](../../commercial-legal/skills/review/SKILL.md)
- [commercial-legal/skills/vendor-agreement-review/SKILL.md](../../commercial-legal/skills/vendor-agreement-review/SKILL.md)
- [commercial-legal/skills/nda-review/SKILL.md](../../commercial-legal/skills/nda-review/SKILL.md)
- [commercial-legal/skills/saas-msa-review/SKILL.md](../../commercial-legal/skills/saas-msa-review/SKILL.md)
- [commercial-legal/skills/renewal-tracker/SKILL.md](../../commercial-legal/skills/renewal-tracker/SKILL.md)

## Travail attendu

- Séparer revue de contrat, confidentialité, SaaS, avenants et échéances de renouvellement ; proposer une story par tâche.
- Identifier les points à revoir : responsabilité, résiliation, cession, preuve, imprévision, clauses déséquilibrées, données et sous-traitance selon l'objet.
- Distinguer B2B et consommation ; orienter les demandes de consommateurs vers leur futur plugin sans dupliquer toute la matière.
- Prévoir aussi le point de vue des indépendants, artisans et TPE : facture client impayée, contrat de prestation, frais ou pénalités contestés, rupture de relation. Ne pas limiter les sorties aux juristes d'une grande entreprise.
- Sources à prévoir et à vérifier lors des futures implémentations : Code civil, Code de commerce, droit UE pertinent et clauses effectivement fournies ; ne pas transformer un playbook commercial en règle de droit.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `commercial-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios.
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer le découpage sur un contrat fournisseur français et un SaaS transfrontalier ; distinguer les hypothèses de droit applicable des préférences de négociation.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire complet](exist-001-annexes/exist-001-inventaire-commercial.md) : 30 fichiers du
  plugin, dont 12 skills, 3 agents, profil, références, schéma du registre et
  métadonnées ; chaînes de contenu suivies jusqu'au cookbook de renouvellements
  et aux données durables. Décision et justification par tâche, sans renommage
  de commande ni retrait d'un skill entier.
- [Découpage COM-001 à COM-018](exist-001-annexes/exist-001-decoupage-commercial.md) : 18 stories
  d'implémentation proposées avec fichiers, résultat, sources à rechercher,
  exclusions, cas normal et limite. Revue, NDA, SaaS, avenants, enregistrement
  d'échéance et rapport sont séparés, ainsi que journal/propositions/décisions
  et chemin distant. Impayé B2B, frais contestés et préparation d'une rupture
  reçoivent chacun une tâche pour indépendants, artisans et TPE.
- [Vérification documentaire](exist-001-annexes/exist-001-verification.md) : contrat fournisseur
  français et SaaS transfrontalier fictifs, plus frontières/publics. Hypothèses
  de loi, clauses, pièces, règles à rechercher et préférences de négociation
  distinguées. Cette relecture n'est pas une exécution de skill.
- [Contrôles statiques et empreintes](exist-001-annexes/exist-001-resultats.json) : couverture,
  liens, frontmatter et dépendances, copies communes, absence de modification
  du plugin et du cookbook. Aucun contenu éditeur modifié.
- Le bilan PILOTE-003 est `terminee` après BASE-011 le 16 octobre 2026 ; son
  état et les limites restantes de PILOTE-002 sont repris dans le découpage.
  Ce cadrage ne sélectionne aucune extension : les 18 COM restent `proposee`.

Fichiers du lot : la présente story, inventaire, découpage, vérification,
résultats JSON, les 18 propositions sous `suites/com-*.md` et l'index
`backlog/README.md`. Tout reste sous `backlog/` ; aucune modification de NOTICE
n'est requise selon les consignes du dépôt.

**Limites :** aucune recherche juridique commerciale ni consultation de source
externe dans ce lot ; les pistes seront vérifiées lors des implémentations.
Aucun plugin commercial adapté, client ou scénario métier exécuté, participant
réel, connecteur, envoi ou déploiement. La story clôt le cadrage uniquement.

## Complément de besoins — formalités, 16 octobre 2026

La [matrice des 100 frictions](exist-002-annexes/exist-002-frictions-utilisateurs.md) ajoute COM-019 (demande de paiement présentée comme obligatoire) et COM-020 (abonnement ou mandat de formalités), toutes deux proposées. Le découpage compte désormais 20 COM : COM-001 reste `a-verifier`, les 19 autres `proposee`. Le bilan et les empreintes historiques ci-dessus portent sur les 18 propositions initiales. Aucun nouveau skill ni branche de COM-001 n'est implémenté par cet ajout ; portée et contrôles dans la matrice.

## Intégration marketing — 16 octobre 2026

La [matrice des 140 frictions](exist-004-annexes/exist-004-frictions-utilisateurs.md) relie les besoins aux tâches et relais. COM-021/022/023 ajoutent contrat d’influence, lecture des mesures/factures et sortie d’agence. Le découpage compte 23 COM : COM-001 reste `a-verifier`, les 22 autres `proposee`. Les résultats et empreintes historiques ci-dessus sont conservés. Portée de l’intégration et contrôles dans le [relevé dédié](exist-004-annexes/exist-004-frictions-verification.md).
