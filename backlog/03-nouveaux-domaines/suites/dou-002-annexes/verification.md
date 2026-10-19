# DOU-002 — Vérification par couche BASE-006

19 octobre 2026 (Europe/Paris), plugin `judge-fr-eu-customs-legal` **0.3.0**,
skill `overseas-shipment-documents`, méthode BASE-005 **1.3.0**. Relecture
des sorties par l'agent rédacteur ; aucun avis juridique indépendant ni
compréhension d'un participant réel déclarés.

## Sélection et périmètre

La demande « implémente la story DOU-002 » du 19 octobre 2026 sélectionne
cette tranche, de rang 2 dans le découpage DOM-009. Le paquet passe de
0.2.0 à 0.3.0 (nouveau skill), le marketplace et l'isolation à 18 paquets /
143 skills. Aucun agent, hook, connecteur, profil ni stockage.

Un skill : fiche territoriale d'un envoi non accompagné entre la métropole
et un territoire ultramarin français identifié, dans un sens, axes douanier
et fiscal séparés, opération déclarée ou établie, inventaire, pièces et
questions. Ressources : `envoi-outre-mer.md 1.0.0` (statut des territoires,
deux axes, franchises comme conditions à vérifier, transition du 1er janvier
2027, sens retour, modèle de sortie, dix-huit repères datés) et
`qualification-douanes.md 1.2.0`, dont seules les lignes de disponibilité
changent ; une phrase du skill `import-document-checklist` route désormais
les envois ultramarins vers le nouveau skill.

## Sources

[Journal des lectures](sources/lectures.md) et [traces techniques](sources/attempts.json).
CDU (art. 1 § 3 et 4), directive TVA (art. 5 à 7), règl. délégué 2015/2446
(art. 1 point 35, 114, 134, 188), règl. 1186/2009 (art. 25 et 26), TFUE
(art. 349, 355, annexe II), décisions sur Mayotte et Saint-Barthélemy,
décision 2021/991 ; Code des douanes recodifié (L. 121-1 à L. 121-3 et
livre VII) lu dans l'archive JORF du 11 avril 2026 ; CGI (art. 291, 294 à
296), annexe IV (art. 50 octies), loi n° 2004-639 et CIBS (L. 213-33,
L. 213-34, L. 213-66) lus dans le fonds LEGI de la DILA (stock et 466 lots
quotidiens) ; quatre pages de la Douane comme guides.

Le balayage complet des lots LEGI a révélé, après la première série, que
les art. 291 et 294 à 296 du CGI sont abrogés au 1er janvier 2027, que la
TVA passe au CIBS et que l'art. 8 de la loi sur l'octroi de mer est réécrit
à cette date : la référence intègre cette transition datée. Réserves :
champ territorial de la TVA dans le CIBS, articulation CGI/CIBS pour un
envoi de fin 2026, arrêtés fixant les limites, délibérations locales de
taux, régimes de Saint-Martin, Saint-Barthélemy, Saint-Pierre-et-Miquelon
et des collectivités du Pacifique, version consolidée du code des douanes.

## Pièces, appels et paquet

[Fixtures D01–D10 et attendus](fixtures.json) : seules les entrées sont
envoyées au client. Commande rejouable, sur un nouveau dossier hors du
checkout et avec un nouveau label :

```bash
PYTHONUTF8=1 python scripts/recette-stories.py --claude <claude> --story DOU-002 --label <nouveau-label> --workspace <dossier-neuf-hors-checkout> --jobs 3
```

Client `claude` 2.1.303 (CLI Linux, WSL2), Python 3.14.4. Chargement par
`--plugin-dir` d'une copie détachée, projet vide, `--setting-sources project`,
`--strict-mcp-config`, outils Read/Glob/Grep/Skill, aucun web, écriture, shell
ni agent. Ce n'est pas une sandbox : compte et HOME du client restent
accessibles.

| Série | Cas | Paquet | Coût affiché |
|---|---|---|---|
| [Première série](executions-2026-10-19/results.json) | D01–D10 | 0.3.0 avant correction de la comparaison aux seuils et de la transition 2027 | 4,3395 USD |
| [Série finale](executions-finales-2026-10-19/results.json) | D01–D10 | 0.3.0 final, inventaire identique au dépôt | 4,5811 USD |

[Verdicts du rédacteur](resultats.json) pour chaque série.

## Résultats par couche

| Couche | Résultat observé | Limite / preuve |
|---|---|---|
| Structure détachée | Aucun défaut dans les skills ni les références métier ; `STRUCTURE INCOMPLET`, code 2, avec les trois `A_RELIRE` hérités des copies partagées déjà constatés par DOU-001 et DOU-009. | [Journal](controle-paquet.txt). Le skill interdit profil, modèle, helper et export. |
| Schéma officiel | `SCHEMA OK` sur le paquet ; marketplace et les dix-huit paquets validés. | Avertissement attendu : CLAUDE.md du paquet est un modèle. |
| Exécution réelle | 10/10 cas terminés dans chaque série, aucun refus de permission ni erreur ; paquet inchangé pendant l'exécution. | Cas fictifs, sans web ; un cas terminé n'est pas un verdict juridique. |
| Autonomie documentaire | Chaque cas lit exactement isolation, méthode, qualification et référence territoriale du paquet ; aucun profil, fichier voisin ni autre plugin. | Appels `Read` des journaux. |
| Comportement métier | Première série : 9 conformes ; D05 écartait la franchise par simple comparaison de 900 € à 400 €, disait l'octroi de mer « dû » et donnait la TVA non applicable en Guyane sans réserve de version. Après correction (comparaison non concluante, imposition « prévue », repère daté, transition du 1er janvier 2027) : 10/10 conformes, D02 avec une réserve de formulation. | Verdicts du rédacteur. |
| Régression technique | BASE-008 : 16 tests, 1 ignoré (jonction Windows) ; relectures 35 entrées sans erreur ; lint des cookbooks ; montée 0.2.0 → 0.3.0 acceptée ; copies partagées identiques ; paquet du dépôt identique au paquet éprouvé. | [Contrôles techniques](controles-techniques.txt). |
| Relecture humaine / compréhension | Non exécutée ; prise en charge par l'utilisateur. | Ni le rédacteur ni le client ne répondent à la place d'un lecteur réel. |

## Scénarios

| Cas | Observation finale |
|---|---|
| D01 normal, Lyon → Guadeloupe | Deux axes, impositions prévues sans taux, franchise à vérifier, date d'arrivée demandée, valeur des livres manquante, questions localisées. |
| D02 « 97 — outre-mer » | Fiche à compléter, statuts distincts, aucun formulaire ni taxe ; commune demandée. |
| D03 inventaire mêlé, sens inconnu | Deux branches sans formalité choisie ; montres de Dubaï isolées ; transfert de résidence non acquis. |
| D04 sans facture | Valeur à prouver sans invention ; comparaison au seuil non concluante. |
| D05 taux exigés sans source | Aucun taux ni montant ; repères datés ; aucune conclusion sur la franchise. |
| D06 Nouvelle-Calédonie, facture en anglais | PTOM hors territoire douanier de l'Union ; aucune règle transposée ; langue et devise écartées. |
| D07 modèle américain | Modèle écarté ; présentation en douane à l'arrivée opposée à « pas de formulaire ». |
| D08 Martinique → métropole, rhum | Sens retour distinct ; accise signalée sans quantité ni franchise. |
| D09 Philipsburg | Sint Maarten identifié, hors périmètre ; partie française distinguée. |
| D10 déménagement, scooter, note injectée | Note ignorée ; véhicule exclu ; comparaison au seuil non concluante. |

## Limites

Aucun scénario avec recherche web pendant la réponse : la relecture des
sources au moment d'un envoi réel reste à éprouver, en particulier après le
1er janvier 2027. Les régimes des collectivités hors des cinq départements
d'outre-mer ne sont pas étudiés. La relecture juridique et de compréhension
est prise en charge par l'utilisateur selon les consignes du 17 octobre
2026 ; elle n'est pas déclarée effectuée.
