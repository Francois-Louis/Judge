# DOM-040 — Vérification du cadrage

Relecture documentaire du 17 octobre 2026 (Europe/Paris), par l'agent de
maintenance. Parcours suivis dans le
[découpage](dom-040-decoupage-chasse-peche.md) et les sept propositions CHP.
Les pièces décrites ci-dessous sont fictives. « Observé » désigne le résultat
de la lecture des contrats écrits, sans sortie produite par un skill.

## Scénarios de la story et limites

| Cas et entrée fictive | Parcours observé | Pièces et questions manquantes | Résultat borné et limite vérifiés dans le contrat |
|---|---|---|---|
| C01 — Chasseur avec avis pour validation annuelle dite expirée, copie du permis seulement | CHP-001 en premier ; CHP-002 pour les documents | Acte complet, preuve de réception, validation, date/lieu du contrôle et attestation | Fiche d'allégation et de stade, mentions recopiées ; ni infraction prouvée ni paiement conseillé ; avocat pour procédure. |
| C02 — Propriétaire ne voulant plus du passage de l'association, titre seul | CHP-005 | Nature ACCA/autre, conventions, actes locaux, droits détenus et objectif | Demande d'explication préparatoire ; propriété seule non traitée comme opposition effective, aucun délai ou effet annoncé. |
| C03 — Avis pour taille d'un poisson, arrêté local absent | CHP-001, puis CHP-003 ou CHP-004 selon lieu | Acte, lieu/date, espèce alléguée, texte local applicable | Lecture poursuivie mais taille applicable réservée ; aucune taille nationale substituée, recours pénal chez DOM-002. |
| C04 — Jardin retourné, traces attribuées aux sangliers, devis fourni | CHP-007 | Usage privé/agricole, indices d'origine, photos/constat existants, dates, courriers | Dossier factuel, devis recopié sans indemnité ; voie et payeur à établir, aucune garantie fédérale présumée. |
| C05 — Permis et reçu de paiement pour une sortie de chasse | CHP-002 | Validation effective, attestation, date et territoire | Documents séparés, reçu non traité comme certification générale ; droit sur terrain chez CHP-005. |
| C06 — Titre présenté pour chasse en Guyane, autre territoire porté sur la pièce | CHP-002 | Régime local, pièces et service territorial | Conclusion territoriale réservée ; absence de transposition automatique, demande ciblée. |
| C07 — Carte avec réciprocité, lac non identifié | CHP-003 | Localisation, convention, secteur et autorisation invoquée | Tableau des mentions et des inconnues ; carte seule ne produit pas une permission sur tout lac. |
| C08 — Pratique projetée en rivière connue, arrêté non fourni | CHP-003 | Arrêté applicable à date/espèce/secteur et classement | Source recherchée ou règle réservée ; taille/période non inventées. |
| C09 — Contrôle oralement raconté, arme retenue selon la personne | CHP-001, CRIM-017/DOM-002 pour mesure | Acte de saisie ou autre mesure, auteur, dates, documents utiles | Récit marqué déclaré, acte demandé, avocat et urgence en tête ; aucune instruction sur l'arme. |
| C10 — Récépissé d'enregistrement et pêche embarquée sur une autre façade | CHP-004 | Espèce, zone, date, champ du récépissé et textes | Enregistrement et déclaration séparés ; aucune extension automatique à l'autre zone, aucun dépôt. |
| C11 — Pêche à pied en embouchure, capture d'écran ancienne | CHP-004, branche CHP-003 si eau douce établie | Limite de zone, date, espèce et source sanitaire locale | Qualification ouverte, demande au service identifié ; aucune autorisation ni conclusion sanitaire. |
| C12 — Indivisaire invité à signer un retrait de terrain, régime local inconnu | CHP-005 ; droits indivis à transmettre au domaine compétent | Pouvoirs, titre, acte proposé, régime et conventions | Renfort avec avocat avant signature, aucune opposition rédigée comme acquise. |
| C13 — Riverain recevant un courrier d'AAPPMA évoquant un passage | CHP-006 | Convention, fondement et emprise du passage, titre | Propriété, pêche et passage séparés ; aucune entrave conseillée. |
| C14 — Étang privé relié à un ruisseau, propriétaire concluant qu'aucune carte n'est nécessaire | CHP-006, puis CHP-003 si question documentaire | Qualification des eaux, actes et conventions | « Privé » ne clôt pas l'analyse ; régime réservé sans expertise déduite d'une photo. |
| C15 — Jardin privé et maïs d'exploitation endommagés sur un même ensemble | CHP-007 pour dossier ; DOM-014 pour cultures | Usage de chaque partie, dégâts, qualité de l'exploitant, garantie invoquée | Usages et voies séparés ; données transférables, aucun double calcul ni payeur désigné. |

Les quatre demandes initiales ont un point d'entrée et un résultat utile
sans connaissance du code. Les onze limites supplémentaires couvrent
l'absence de pièce, le territoire, l'eau douce/mer, les droits fonciers et
l'orientation agricole. Aucun de ces parcours ne résout le dossier.

## Couverture des critères DOM-040

| Critère | Élément contrôlé |
|---|---|
| Découpage avec entrées, sortie, pièces, limites et scénarios | Sept stories CHP-001 à CHP-007 ; une tâche et une référence métier principale par suite, cas nominal et limite identifiés. |
| Départ par le document | Table des paroles usuelles, CHP-001 et C01/C03/C09 ; récit accepté comme déclaré en l'absence de pièce. |
| Autonomie et frontières | Contrat du futur paquet, copies locales BASE-005/008, pas de connecteur ou autre plugin obligatoire ; table des transmissions CRIM-017, DOM-002/014/030 et autres objets distincts. |
| Aucun nombre juridique sans source locale lue | Garde-fou commun et sorties des suites ; nombres d'une pièce seulement recopiés, jamais présentés comme règle établie ; C03/C08/C11. |
| Préalable pilote et aucune adaptation complète | PILOTE-003 lue, statut `terminee` après BASE-011 ; toutes les CHP restent `proposee`, aucun paquet ou skill créé. |

## Contrôles techniques

Le relevé [DOM-040](dom-040-resultats.json) consigne les contrôles documentaires
réellement exécutés : frontmatters et identifiants, dépendances existantes
sans cycle, résolution des liens locaux du lot, inventaire des sept suites,
format, index généré à jour et périmètre des changements. Ces contrôles
portent sur le backlog, sans test de raisonnement juridique.

Les commandes `python backlog/etat.py`, `python backlog/etat.py --check`,
`python scripts/check-version-bump.py` et `git diff --check` complètent ce
relevé. Aucun manifeste de plugin modifié : validation de schéma et recette
BASE-006/008 d'un nouveau paquet seront dues par CHP-001, pas par ce cadrage.

## Portée

Cadrage documentaire et parcours fictifs relus par le seul agent de
maintenance ; aucune exécution de skill, installation ou invocation en
client, consultation résolue, délai calculé, démarche envoyée ni contrôle
de compréhension par un participant. Trois pages officielles d'information
ont été ouvertes : S01–S03, avec usage, date et statut `partiel` dans le
découpage ; leurs textes liés, versions, transitions et règles locales ne
sont pas vérifiés. Les autres sources restent des pistes. La relecture
humaine et juridique est prise en charge par l'utilisateur conformément à
la décision du 17 octobre 2026, sans être déclarée effectuée. Aucun défaut
documentaire connu ne reste ouvert ; les recettes futures figurent dans
les critères non cochés des propositions, sans être requises pour livrer ce
seul cadrage.
