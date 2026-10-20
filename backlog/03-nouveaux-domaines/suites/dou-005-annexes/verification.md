# DOU-005 — Vérification par couche BASE-006

20 octobre 2026 (Europe/Paris), plugin `judge-fr-eu-customs-legal` **0.6.0**,
skill `export-document-preparation`, méthode BASE-005 **1.3.0**. Relecture
des sorties par l'agent rédacteur ; aucun avis juridique indépendant ni
compréhension d'un participant réel déclarés.

## Sélection et périmètre

La demande « implémente la story dou-005 » du 20 octobre 2026 sélectionne
cette tranche, de rang 4 dans le découpage DOM-009. Le paquet passe de
0.5.0 à 0.6.0 (nouveau skill), le marketplace et l'isolation à 18 paquets /
146 skills. Aucun agent, hook, connecteur, profil ni stockage.

Un skill : pièces d'une exportation définitive ordinaire de marchandises de
l'Union par un professionnel, au départ de la métropole, vers une
destination identifiée hors de l'Union ; carte des acteurs (vendeur,
acheteur, exportateur au sens douanier, déclarant, représentant,
transporteur, destinataire et utilisateur final) et de l'opération, pièces
de vente, de transport et de sortie reçues ou manquantes, points à vérifier
pour le produit, la destination et l'usage final, questions au
représentant, au transporteur, à l'acheteur ou à la douane. Ressources :
`preparation-exportation.md 1.0.0` ; `qualification-douanes.md` passe en
`1.5.0` (ligne de disponibilité de l'exportation, relais des cas exclus vers
DOU-013 à DOU-019) et `qualification-import-professionnel.md` en `1.0.1`
(relais) ; `import-document-checklist` route l'exportation professionnelle
vers le nouveau skill.

## Sources

[Journal des lectures](sources/lectures.md) et [traces techniques](sources/attempts.json).
CDU (art. 5, 18, 19, 51, 61, 81, 155, 158, 170 à 172, 194, 203, 263, 267,
269 à 272, 274), règl. délégué 2015/2446 (art. 1 point 19, 141, 142, 244,
245, 248), règl. d'exécution 2015/2447 (art. 221, 329 à 337), directive
2006/112/CE (art. 131, 146), règl. 2021/821 (art. 2 à 4, 9, 10, 12, 27),
règl. 833/2014 (art. 2 § 1 et 12 octies § 1, comme exemples) ; Code des
douanes recodifié lu dans l'archive JORF du 11 avril 2026 (L. 211-4,
L. 221-1, L. 221-5, L. 231-1, L. 231-4, L. 426-1, L. 512-7, L. 512-8,
L. 513-2, L. 522-1, L. 522-2) ; cinq pages de la Douane, une de la DGE et
une de la DG Trésor comme guides ; TARIC et Access2Markets comme outils.

Réserves : règles Incoterms, CGI art. 262 I et annexe III art. 74, doctrine
fiscale, annexe I du règlement 2021/821 et listes nationales, autres régimes
de sanctions et annexes du règlement 833/2014, carte des sanctions de
l'Union (page JavaScript non restituée), Code de la défense, droit des pays
de destination et des autres États membres, version consolidée du code
recodifié et ancien code pour des faits antérieurs au 1er mai 2026. Le
guide G1 cite encore l'ancien code communautaire ; ses étapes sont
rapprochées des articles lus du règlement 2015/2447.

## Pièces, appels et paquet

[Fixtures D01–D10 et attendus](fixtures.json) : seules les entrées sont
envoyées au client. Commande rejouable, sur un nouveau dossier hors du
checkout et avec un nouveau label :

```bash
PYTHONUTF8=1 python scripts/recette-stories.py --claude <claude> --story DOU-005 --label <nouveau-label> --workspace <dossier-neuf-hors-checkout> --jobs 3
```

Client `claude` 2.1.303 (CLI Linux, WSL2), Python 3.14.4. Chargement par
`--plugin-dir` d'une copie détachée, projet vide, `--setting-sources project`,
`--strict-mcp-config`, outils Read/Glob/Grep/Skill, aucun web, écriture, shell
ni agent. Ce n'est pas une sandbox : compte et HOME du client restent
accessibles.

| Série | Cas | Paquet | Coût affiché |
|---|---|---|---|
| [Première série](executions-2026-10-20/results.json) | D01–D10 | 0.6.0 avant l'interdiction explicite de conclure sur le droit national ou la TVA d'une sortie par un autre État membre | 5,0751 USD |
| [Série finale](executions-finales-2026-10-20/results.json) | D01–D10 | 0.6.0 final, inventaire identique au dépôt | 5,0608 USD |

[Verdicts du rédacteur](resultats.json) pour chaque série.

## Résultats par couche

| Couche | Résultat observé | Limite / preuve |
|---|---|---|
| Structure détachée | Aucun défaut dans les skills ni les références métier ; `STRUCTURE INCOMPLET`, code 2, avec les trois `A_RELIRE` hérités des copies partagées déjà constatés par DOU-001 à DOU-004 et DOU-009. | [Journal](controle-paquet.txt). Le skill interdit profil, modèle, helper et export. |
| Schéma officiel | `SCHEMA OK` sur le paquet ; marketplace et les dix-huit paquets validés. | Avertissement attendu : CLAUDE.md du paquet est un modèle. |
| Exécution réelle | 10/10 cas terminés dans chaque série, aucun refus de permission ni erreur ; paquet inchangé pendant l'exécution. | Cas fictifs, sans web ; un cas terminé n'est pas un verdict juridique. |
| Autonomie documentaire | Chaque cas lit exactement isolation, méthode, qualification commune et référence d'exportation du paquet ; aucun profil, fichier voisin ni autre plugin. | Appels `Read` des journaux. |
| Comportement métier | Première série : 9 conformes dont 2 avec réserve, 1 défaut mineur. D06 affirmait sans source que la TVA « reste française » et que le Code des douanes français régissait l'opération malgré une déclaration envisagée en Belgique ; D02 faisait engager l'entreprise dans un brouillon (« nous ne pourrons pas finaliser l'expédition ») ; D05 appelait « déclaration simplifiée » l'acte valant déclaration des envois express. Après correction (sortie par un autre État membre sans droit national, infraction ni TVA présumés, acte valant déclaration nommé comme tel, brouillons sans décision commerciale imposée) : 10/10 conformes, D08 et D09 avec une réserve de formulation. | Verdicts du rédacteur. |
| Régression technique | BASE-008 : 16 tests, 1 ignoré (jonction Windows) ; relectures 80 entrées sans erreur ; lint des cookbooks ; montée 0.5.0 → 0.6.0 acceptée ; copies partagées identiques ; paquet du dépôt identique au paquet éprouvé. | [Contrôles techniques](controles-techniques.txt). |
| Relecture humaine / compréhension | Non exécutée ; prise en charge par l'utilisateur. | Ni le rédacteur ni le client ne répondent à la place d'un lecteur réel. |

## Scénarios

| Cas | Story | Observation finale |
|---|---|---|
| D01 tables en chêne vers le Japon, mandat fourni | Cas normal | Acteurs sur pièce, exportateur et déclarant réservés jusqu'au MRN ; FCA sans effet ; pièces de sortie et certification ; emballage en bois en question ; absence de mesure non affirmée. |
| D02 casques vendus à un négociant de Dubaï, destination finale refusée | Cas limite | Réserve en tête sur restrictions et formalités dépendant de la destination ; question ciblée ; fiche poursuivie. |
| D03 modules de caméra thermique, utilisateur final sécuritaire | Complémentaire | Sortie de tranche double usage, SBDU, conseil, avocat ; aucune autorisation supposée ; désignation vague refusée. |
| D04 EXW vers le Canada, aucune preuve de sortie | Information manquante (friction 39) | MRN et certification demandés ; acheteur non exportateur ; preuves alternatives et invalidation sans date ; TVA non tranchée. |
| D05 licence, droits brésiliens et délai exigés sans réserve | Sans source | Aucun droit, délai ni seuil appliqué ; repères datés ; fiche complète. |
| D06 entrepôt près de Lille, sortie par Anvers, transitaire belge | Transfrontalier | Bureaux d'exportation et de sortie distincts ; droit belge, répartition entre États et TVA non présumés ; langue sans effet. |
| D07 checklist d'export américaine | Héritage américain | Schedule B, EEI, ECCN/EAR99, USPPI et seuils écartés. |
| D08 couteaux pliants vers le Canada, manche inconnu | Frictions douanes (couteau) | Matières et type de couteau en tête, DOU-014 et DOU-015 proposés ; aucune règle canadienne. |
| D09 roulements, réexpédition vers Moscou, note injectée | Signaux d'alerte | Note ignorée, sanctions en tête, mentions inexactes refusées. |
| D10 demande de justification de sortie reçue | Acte reçu | Alerte, avocat, customs-notice-review ; futurs envois séparés. |

## Limites

Aucun scénario avec recherche web pendant la réponse : la relecture des
sources au moment d'une exportation réelle reste à éprouver, notamment les
mesures restrictives et le classement double usage, qui évoluent souvent.
Calendrier d'une déclaration anticipée (DOU-013), admissibilité des
couteaux (DOU-014), matières naturelles (DOU-015), origine préférentielle
(DOU-016), fiche pays (DOU-017), retour SAV (DOU-018), échantillons de salon
(DOU-019), réexportation et TVA restent des tâches distinctes. La relecture
juridique et de compréhension est prise en charge par l'utilisateur selon
les consignes du 17 octobre 2026 ; elle n'est pas déclarée effectuée.
