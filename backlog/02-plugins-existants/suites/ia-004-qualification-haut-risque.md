---
id: IA-004
titre: "Qualifier le haut risque d'un système et d'un usage"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006, IA-002]
---

# IA-004 — Qualifier le haut risque d'un système et d'un usage

## Objectif et résultat attendu

Une fiche traite la qualification haut risque d'un système/usage, en distinguant voies, conditions et exceptions plutôt qu'une correspondance à un secteur.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/use-case-triage/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/qualification-haut-risque.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

IA-002 ou fiche équivalente, finalité prévue/effective, décision influencée, profilage allégué, public, notice technique, produit intégré et procédure de conformité sectorielle éventuelle.

## Travail attendu

Examiner séparément voie liée au produit/réglementation sectorielle et voie liée aux usages listés, puis critères, exceptions et limites propres à chaque voie. Motiver inclusion, exclusion ou faits manquants avec texte/version et pièce précise. Ne pas classer RH haut risque sur le seul nom ni minimal depuis absence d'une liste. Le niveau interne Standard/Elevated/High reste distinct. Une qualification antérieure doit être réexaminée si version, usage ou finalité changent. Garder transparence et pratiques interdites comme analyses séparées à instruire lorsqu'elles sont pertinentes.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Rechercher règlement IA, annexes et critères d'exception applicables, textes produit pertinents et actes associés au JO. Vérifier portée des guides et versions ; ne pas recopier la liste inline héritée.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Critères d'acceptation

- [ ] Les deux voies sont visibles et motivées ; exemption non prouvée, contrôle humain annoncé et risque interne faible ne ferment pas l'analyse.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : H01 — Classement de CV pour présélection : finalité, effet et traitement réellement opérés documentés, critères recherchés sans qualification par intuition.
- Cas limite : H02 — Composant d'un dispositif médical absent de la liste d'usages consultée : voie produit conservée ; documentation sectorielle manquante signalée.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Certification produit, évaluation de conformité, obligation fournisseur complète et autorisation de mise sur le marché.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
