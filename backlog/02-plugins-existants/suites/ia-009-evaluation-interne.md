---
id: IA-009
titre: "Évaluer les impacts internes d'un usage IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-002]
---

# IA-009 — Évaluer les impacts internes d'un usage IA

## Objectif et résultat attendu

Une évaluation interne relie dommages plausibles, personnes affectées, contrôle réel et mesures prouvées/proposées pour un usage déterminé.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/aia-generation/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/evaluation-interne.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

IA-002 ou fiche équivalente, périmètre/stade, tests fournis, taux d'erreur et limites, recours, incidents allégués, responsables et contraintes internes.

## Travail attendu

Renommer le livrable visible évaluation interne IA et conserver l'identifiant aia-generation. Décrire scénarios d'erreur, effets et portée des tests sans inventer scores ou probabilités. Distinguer mesure conçue, décidée, déployée et vérifiée ; maintien d'un humain ne suffit pas à valider l'usage. Ne pas conclure revue fictive depuis seul taux d'override. Garder gravité amont ou motiver sa révision. Séparer décision attribuée d'un auteur humain, recommandations et questions juridiques réservées. Réutiliser les faits fournis sans nouvelle collecte générale ni AIPD/FRIA imposée.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Sources factuelles : tests et procédures réellement fournis. Pour toute obligation invoquée, rechercher règlement IA et qualification pertinente ; guides de gestion des risques ou normes restent de statut distinct et ne créent pas seuls une obligation.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] La sortie annonce sa nature interne et les évaluations distinctes non réalisées ; aucun résumé exécutif ne transforme brouillon ou recommandation en approbation.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : E01 — Assistant de rédaction interne : erreurs plausibles, destinataires et contrôles proposés/prouvés distingués, sans feu vert.
- Cas limite : E02 — Système RH déjà déployé, test portant sur une ancienne version et condition amont rouge : couverture insuffisante et gravité conservée ou révision explicitement justifiée.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

AIPD, FRIA, évaluation de conformité, validation statistique des tests et décision de déploiement.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
