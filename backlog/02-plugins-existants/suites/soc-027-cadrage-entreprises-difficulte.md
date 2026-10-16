---
id: SOC-027
titre: "Découper l'aide aux entreprises en difficulté et ses frontières"
statut: proposee
priorite: P2
nature: cadrage
dependances: [EXIST-002, BASE-003, BASE-005]
---

# SOC-027 — Découper l'aide aux entreprises en difficulté et ses frontières

## Objectif et résultat attendu

Proposition de propriétaire pour chaque tâche, stories bornées avec entrées/sorties/scénarios, et premier parcours proposé de qualification d'une difficulté de paiement. Les attributions de cette matrice restent des besoins à cadrer.

Issue des [frictions sur les formalités d'entreprise](../exist-002-frictions-utilisateurs.md), points 83–87, 95. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : corporate-legal (propriétaire du cadrage ; implantation des futures tâches à arrêter). Présente story et complément du découpage EXIST-002 ; examiner BASE-003, DOM-024, DOM-039 et DOM-011. Aucun fichier de plugin ni nouveau plugin créé par ce cadrage.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

Récits ou pièces fictives séparant société, EI et dettes personnelles ; créanciers, passif exigible, actif disponible, dates, garanties, mesures en cours et demande d'aide.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Découper séparément : chronologie de trésorerie et qualification de cessation des paiements ; préparation documentaire de prévention (mandat ad hoc, conciliation, sauvegarde selon champ) ; lecture d'une décision de procédure ; préparation de saisine et calendrier propre ; sort des dettes/garanties ; effets patrimoniaux de la cessation d'EI. Ne pas fondre toutes ces questions dans un skill. Prévoir urgence et interlocuteur pour chacun ; distinguer dette isolée, difficulté globale, fermeture volontaire et surendettement personnel. Arrêter les frontières avec DOM-024/039/011 et exécution avant toute implémentation.

Produire le découpage et ses frontières avant de choisir une implémentation. Les futurs lots suivront BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code de commerce et textes d'application sur entreprises en difficulté ; textes du statut/patrimoine de l'EI et articulation avec surendettement ; sources officielles judiciaires. Aucun délai ni critère du document fourni n'est tenu pour vérifié.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] Chaque tâche a un propriétaire proposé, des frontières, entrées, résultat borné, sources et scénarios, sans plugin créé.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Les premières tranches et les arbitrages de domaine encore nécessaires sont nommés ; aucune couverture au fond présumée.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : Petite société avec échéances impayées : le découpage distingue demande d'échéancier, diagnostic à documenter, prévention et procédures ; aucun simple bilan assimilé au test de cessation des paiements.
- Cas limite : EI radiée avec dettes nées à des dates différentes et sûreté personnelle : analyse patrimoniale prévue comme tâche distincte ; aucune extinction automatique des dettes.

Scénarios attendus, non exécutés. Relire les frontières et résultats sur pièces fictives, sans résoudre les consultations.

## Hors périmètre

Résoudre les consultations, déterminer une date réelle de cessation des paiements, lancer une procédure, créer un plugin ou appliquer le surendettement personnel à toute dette professionnelle.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../exist-002-frictions-verification.md).

## Complément des frictions contentieuses — 16 octobre 2026

Exigences issues des [125 frictions contentieuses](../exist-006-frictions-utilisateurs.md), sans implémentation ni sélection de tranche.

Points 96–97 et 104 : prévoir explicitement le parcours du **créancier d’un client en procédure collective**, distinct de celui de l’entreprise débitrice. Découper lecture d’annonce BODACC, préparation d’une déclaration de créance, preuve de transmission et traitement d’un délai possiblement manqué. Entrées : annonce et publication, décision, identité actuelle du débiteur, créance et justificatifs, sûretés éventuelles, correspondances avec mandataire et reçus. Sorties attendues : procédure/qualité, destinataire à vérifier, composantes de créance, pièces et calendrier conditionnel ; aucun paiement ni relevé de forclusion garanti.

Scénarios : découverte par annonce sans courrier ; créance partiellement payée ; fusion ou liquidation rendant une poursuite envisagée inadéquate. Examiner Code de commerce, procédures collectives, effets sur poursuites individuelles et déclaration, exceptions et voies éventuelles. CTX-041 et ENF-010 passent une fiche manuelle sans exiger plugin voisin installé.

Les scénarios indiqués sont attendus, non exécutés. Sources/version, champ, déclencheur, exceptions et transitions restent à rechercher ; le texte fourni n’est pas une autorité juridique.
