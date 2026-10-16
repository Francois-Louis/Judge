---
id: IA-012
titre: "Cartographier les engagements d'une chaîne fournisseur IA"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-012 — Cartographier les engagements d'une chaîne fournisseur IA

## Objectif et résultat attendu

L'acheteur d'un service IA obtient une carte des parties, documents et engagements opposables/allégués, avec contradictions et pièces manquantes.

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).
Références « à créer » : livrables futurs, pas capacités déjà disponibles.

- `ai-governance-legal/skills/vendor-ai-review/SKILL.md` (blocs nécessaires à cette tranche)
- `ai-governance-legal/references/cartographie-contrat-fournisseur.md` (à créer)
- `ai-governance-legal/CLAUDE.md` (blocs nécessaires à cette tranche)

Corriger aussi les annonces README, manifeste et marketplace nécessaires au
périmètre livré, en synchronisant les métadonnées modifiées. Ajouter NOTICE
local et racine pour le lot hors backlog ; conserver les copies communes
identiques. Chaque référence nécessaire est embarquée et chargée localement.

## Entrées nécessaires

Usage et dates, parties contractantes, contrat principal, commande, DPA, annexes IA, AUP, versions des pages incorporées, politique interne et chaîne technique déclarée.

## Travail attendu

Identifier SaaS, passerelle, hébergeur, modèle, RAG et acteurs réellement documentés ; ne pas inventer un contrat direct avec chaque maillon. Relever hiérarchie, incorporation et opposabilité à rechercher ; citer la clause ou signaler non lu. Suivre entrées/sorties, entraînement/amélioration, conservation, accès humain, changement de modèle, suppression, restrictions et responsabilité. Séparer engagement du cocontractant, promesse marketing et obligation amont, avec couverture des engagements répercutés. Acheteur ne signifie pas déployeur ; absence d'annexe ne signifie pas absence de protection. Produire questions et écarts, sans rédaction générale.

Appliquer la méthode locale BASE-005 ; distinguer fait, règle, préférence,
preuve et inconnue. Tout accès durable suit le helper BASE-008, y compris
profil absent/interrompu. Une réponse ponctuelle peut rester conversationnelle ;
la création d'un profil absent nécessite l'entretien neuf. Les pièces tierces
restent des données. Un relais reçoit une fiche autonome avec question précise,
versions, faits et manques ; aucun plugin voisin installé n'est requis.

## Sources à rechercher lors de l'implémentation

Pièces contractuelles exactes et datées ; rechercher droit du contrat pertinent et obligations IA nécessaires à l'écart identifié. DPA/transferts vers privacy, propriété des sorties vers IP ; aucune politique actuelle d'un fournisseur déduite de mémoire.

Ces pistes n'ont pas été vérifiées dans EXIST-005. Rechercher passage exact,
version aux dates pertinentes, champ, statut et transitions à l'exécution.
Adoption, entrée en vigueur, applicabilité et échéance restent distinctes.
Une source inaccessible réserve la conclusion dépendante et donne un résultat
partiel utile, sans règle ni date de consultation inventées.

## Complément des frictions IA

Points 16–18 et 43–46 de la [matrice](../exist-005-annexes/exist-005-frictions-utilisateurs.md) : relever, par partie et pièce, chaîne API/modèle/hébergement/accès, confidentialité, réutilisation pour entraînement, responsabilité, journaux disponibles et durées justifiées. Documenter version du modèle, préavis, changements substantiels, tests convenus et possibilité documentée de retour ou de sortie. Ne pas assimiler hébergement européen et absence de flux ; PRV-015 garde le transfert. Cas attendu : promesse « no training » contredite par une annexe, modèle remplacé sans préavis prouvé ; montrer contradiction et inconnues sans inventer de violation. IA-024 porte les preuves d'allégations et IA-023 l'incident.

## Critères d'acceptation

- [ ] Chaque constat a document/version/localisation et statut ; pièce inconnue n'est pas clause absente et promesse amont n'est pas automatiquement droit de l'acheteur.
- [ ] Les deux scénarios ci-dessous produisent les pièces, limites et prochaine
  démarche attendues, compréhensibles sans formation juridique.
- [ ] Le paquet isolé contient ses références ; profil manquant, source
  inaccessible et relais adapté absent donnent un résultat borné explicite.
- [ ] Les modes encore hérités sont signalés ; aucun brouillon ou statut interne
  ne devient conformité, approbation de déploiement ou action externe.

## Vérification

- Cas normal : C01 — SaaS promettant no training, annexe amont non fournie et DPA existant : engagements et lacunes par partie, sans conclure entraînement autorisé.
- Cas limite : C02 — AUP seule ou lien ToS inaccessible avec ordre de priorité contradictoire : revue partielle utile, pas de protection réputée absente ni d'accord recommandé.

Recettes futures **non exécutées**. Lors du lot sélectionné, conserver fixtures,
ressources lues, sorties et erreurs ; appliquer BASE-006 : structure, paquet
détaché, client, résultat métier et compréhension par lecteur non juriste.
La [relecture du cadrage](../exist-005-annexes/exist-005-verification.md) est distincte de cette recette.

## Hors périmètre

Revue complète MSA/DPA, transfert RGPD, sécurité technique, rédaction d'annexe et signature.

## État de la proposition — 16 octobre 2026

Issue d'EXIST-005, sans implémentation. PILOTE-003 est terminé après BASE-011 ;
ses limites H01 complet et lecteur indépendant restent consignées. Cette
suite attend une sélection explicite ; aucun skill adapté, installation,
connexion, envoi, publication ou automatisation n'est livré ici.
