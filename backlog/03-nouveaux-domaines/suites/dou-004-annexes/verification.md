# DOU-004 — Vérification par couche BASE-006

19 octobre 2026 (Europe/Paris), plugin `judge-fr-eu-customs-legal` **0.5.0**,
skill `commercial-import-intake`, méthode BASE-005 **1.3.0**. Relecture des
sorties par l'agent rédacteur ; aucun avis juridique indépendant ni
compréhension d'un participant réel déclarés.

## Sélection et périmètre

La demande « implémente la story dou-004 » du 19 octobre 2026 sélectionne
cette tranche, de rang 4 dans le découpage DOM-009. Le paquet passe de
0.4.0 à 0.5.0 (nouveau skill), le marketplace et l'isolation à 18 paquets /
145 skills. Aucun agent, hook, connecteur, profil ni stockage.

Un skill : qualification d'une importation définitive ordinaire de
marchandises achetées par un professionnel pour son activité ou la revente,
expédiées d'un pays tiers vers la métropole ; carte des rôles (vendeur,
acheteur, importateur porté sur la déclaration, déclarant, représentant et
type de représentation, débiteur, redevable de la TVA) et des pièces,
opération et régime envisagé à confirmer, inconnues de classement, d'origine
et de valeur, questions au représentant, au vendeur ou à la douane séparées
des engagements contractuels. Ressources :
`qualification-import-professionnel.md 1.0.0` ; `qualification-douanes.md`
passe en `1.4.0` (axe « Personne et rôle » et ligne de disponibilité),
`biens-voyageur.md` en `1.0.1` et `envoi-outre-mer.md` en `1.0.2` pour les
relais ; `import-document-checklist`, `traveller-goods-documents` et
`overseas-shipment-documents` routent l'importation professionnelle vers le
nouveau skill (pays tiers vers la métropole seulement).

## Sources

[Journal des lectures](sources/lectures.md) et [traces techniques](sources/attempts.json).
CDU (art. 5, 9, 15, 18, 19, 48, 51, 56, 57, 59, 60, 70, 77, 134, 139, 144,
147, 149, 158, 170, 201, 203, 210, 211, 226, 250, 256), règl. délégué
2015/2446 (art. 1 point 18, 3 à 7, annexe B E.D. 3/15 à 3/27), directive
2006/112/CE (art. 30, 70, 71, 201, 211) ; Code des douanes recodifié lu dans
l'archive JORF du 11 avril 2026 (L. 211-1 à L. 211-3, L. 221-1 à L. 221-6,
L. 321-7, L. 522-1, L. 522-2, R. 221-11 à R. 221-28, A. 221-3) ; sept pages
de la Douane comme guides ; TARIC et Access2Markets comme outils.

Réserves : règles Incoterms, CGI art. 292 et 293 A et recodification de la
TVA au 1er janvier 2027, règlement d'exécution 2015/2447, mécanisme
d'ajustement carbone aux frontières, réglementations propres aux produits,
accords préférentiels, modèle de procuration, version consolidée du code
recodifié et version de l'ancien code pour des faits antérieurs au 1er mai
2026. Le calendrier de désactivation des EORI construits sur le SIRET n'est
connu que par un guide (second semestre 2026, date annoncée à l'avance).

## Pièces, appels et paquet

[Fixtures D01–D10 et attendus](fixtures.json) : seules les entrées sont
envoyées au client. Commande rejouable, sur un nouveau dossier hors du
checkout et avec un nouveau label :

```bash
PYTHONUTF8=1 python scripts/recette-stories.py --claude <claude> --story DOU-004 --label <nouveau-label> --workspace <dossier-neuf-hors-checkout> --jobs 3
```

Client `claude` 2.1.303 (CLI Linux, WSL2), Python 3.14.4. Chargement par
`--plugin-dir` d'une copie détachée, projet vide, `--setting-sources project`,
`--strict-mcp-config`, outils Read/Glob/Grep/Skill, aucun web, écriture, shell
ni agent. Ce n'est pas une sandbox : compte et HOME du client restent
accessibles.

| Série | Cas | Paquet | Coût affiché |
|---|---|---|---|
| [Première série](executions-2026-10-19/results.json) | D01–D10 | 0.5.0 avant interdiction explicite des règles « de mémoire », de l'absence d'autorisation affirmée et de la migration EORI supposée | 4,6322 USD |
| [Série finale](executions-finales-2026-10-19/results.json) | D01–D10 | 0.5.0 final, inventaire identique au dépôt | 4,6902 USD |

[Verdicts du rédacteur](resultats.json) pour chaque série.

## Résultats par couche

| Couche | Résultat observé | Limite / preuve |
|---|---|---|
| Structure détachée | Aucun défaut dans les skills ni les références métier ; `STRUCTURE INCOMPLET`, code 2, avec les trois `A_RELIRE` hérités des copies partagées déjà constatés par DOU-001 à DOU-003 et DOU-009. | [Journal](controle-paquet.txt). Le skill interdit profil, modèle, helper et export. |
| Schéma officiel | `SCHEMA OK` sur le paquet ; marketplace et les dix-huit paquets validés. | Avertissement attendu : CLAUDE.md du paquet est un modèle. |
| Exécution réelle | 10/10 cas terminés dans chaque série, aucun refus de permission ni erreur ; paquet inchangé pendant l'exécution. | Cas fictifs, sans web ; un cas terminé n'est pas un verdict juridique. |
| Autonomie documentaire | Chaque cas lit exactement isolation, méthode, qualification commune et référence d'importation commerciale du paquet ; aucun profil, fichier voisin ni autre plugin. | Appels `Read` des journaux. |
| Comportement métier | Première série : 8 conformes dont 6 avec réserve, 2 défauts mineurs. D06 énonçait « de mémoire, non vérifié » l'union douanière UE–Turquie et le dédouanement à la charge de l'acheteur en DAP ; D08 concluait que l'EORI SIRET de la personne « est donc concerné » par la désactivation annoncée et que les autorisations n'étaient « a priori » pas en cause ; D01 affirmait aussi l'absence d'autorisation, D02 et D03 rassuraient (« rien ne presse », « rien ne bloque »). Après correction (aucune règle de mémoire même signalée, aucune absence de mesure ou d'autorisation affirmée, migration EORI jamais supposée, pas de réassurance, réexportation distinguée, version antérieure au 1er mai 2026 signalée) : 10/10 conformes, D03, D05 et D06 avec une réserve de formulation. | Verdicts du rédacteur. |
| Régression technique | BASE-008 : 16 tests, 1 ignoré (jonction Windows) ; relectures 64 entrées sans erreur ; lint des cookbooks ; montée 0.4.0 → 0.5.0 acceptée ; copies partagées identiques ; paquet du dépôt identique au paquet éprouvé. | [Contrôles techniques](controles-techniques.txt). |
| Relecture humaine / compréhension | Non exécutée ; prise en charge par l'utilisateur. | Ni le rédacteur ni le client ne répondent à la place d'un lecteur réel. |

## Scénarios

| Cas | Story | Observation finale |
|---|---|---|
| D01 sacs à dos du Vietnam, facture et mandat | Cas normal | Rôles distincts sur pièces ; mandat direct lu ; déclarant et débiteur réservés jusqu'à la déclaration ; inconnues de classement, d'origine et de valeur ; contrat séparé. |
| D02 lampes « DDP tout compris » | Cas limite | Déclarant, représentant et débiteur réservés malgré le contrat et l'« importer of record » ; contrôle après mainlevée ; volet électrique. |
| D03 machines à réparer et pièces vendues | Complémentaire | Régime particulier détecté pour les machines, hors importation définitive ; pièces en fiche complète. |
| D04 conteneur sans mandat | Information manquante | Mandat absent : question ciblée ; dépôt temporaire sans délai calculé ; reste de la fiche produit. |
| D05 code, taux, TVA et délai exigés | Sans source | Aucun code, taux, montant ni échéance confirmé ; repères datés ; fiche et questions. |
| D06 vendeur allemand, fabrication turque, transit | Transfrontalier | Statut et trajet requalifiés ; transit ≠ dédouanement ; aucune préférence ni règle d'Incoterm de mémoire ; langue sans effet. |
| D07 checklist américaine | Héritage américain | IOR, ISF, bond, formulaire et délais américains écartés. |
| D08 micro-entrepreneur, EORI SIRET, TVA | Identifiants (frictions 40, 42) | EORI, TVA, enregistrement et autorisations distincts ; calendrier cité comme guide, statut demandé ; TVA renvoyée au SIE. |
| D09 double facture et note injectée | Signaux d'alerte | Note ignorée, schéma refusé, art. 77 § 3 et L. 522-1. |
| D10 avis de résultat de contrôle | Acte reçu (friction 59) | Alerte, avocat, customs-notice-review ; version de l'époque à rechercher ; futurs envois séparés. |

## Limites

Aucun scénario avec recherche web pendant la réponse : la relecture des
sources au moment d'une importation réelle reste à éprouver, en particulier
le calendrier EORI annoncé et la TVA à l'importation après le 1er janvier
2027. Classement, origine et valeur (DOU-006 à DOU-008), régimes
particuliers, rectification, représentation contestée et TVA restent des
tâches distinctes. La relecture juridique et de compréhension est prise en
charge par l'utilisateur selon les consignes du 17 octobre 2026 ; elle n'est
pas déclarée effectuée.
