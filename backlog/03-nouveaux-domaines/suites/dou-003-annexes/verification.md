# DOU-003 — Vérification par couche BASE-006

19 octobre 2026 (Europe/Paris), plugin `judge-fr-eu-customs-legal` **0.4.0**,
skill `traveller-goods-documents`, méthode BASE-005 **1.3.0**. Relecture
des sorties par l'agent rédacteur ; aucun avis juridique indépendant ni
compréhension d'un participant réel déclarés.

## Sélection et périmètre

La demande « implémente la story dou-003 » du 19 octobre 2026 sélectionne
cette tranche, de rang 3 dans le découpage DOM-009. Le paquet passe de
0.3.0 à 0.4.0 (nouveau skill), le marketplace et l'isolation à 18 paquets /
144 skills. Aucun agent, hook, connecteur, profil ni stockage.

Un skill : pièces des biens ordinaires accompagnant un voyageur majeur, pour
son usage privé, à l'arrivée en métropole d'un pays tiers ou d'un territoire
fiscalement tiers ; fiche trajet et qualité, inventaire documenté, questions
sur le régime et pièces manquantes, interlocuteur douanier à confirmer.
Ressources : `biens-voyageur.md 1.0.0` (provenances, lieu des contrôles,
qualité du voyageur, biens achetés, reçus ou déjà détenus, caractère non
commercial et franchise comme conditions, transition du 1er janvier 2027,
portée du circuit « rien à déclarer », volets spécialisés, modèle de sortie,
quatorze repères datés). `qualification-douanes.md` passe en `1.3.0` pour la
seule ligne de disponibilité, `envoi-outre-mer.md` en `1.0.1` pour le
relais ; `import-document-checklist` et `overseas-shipment-documents`
routent les voyageurs vers le nouveau skill.

## Sources

[Journal des lectures](sources/lectures.md) et [traces techniques](sources/attempts.json).
Directive 2007/74/CE (art. 1 à 21), règl. 1186/2009 (art. 41), règl.
délégué 2015/2446 (art. 1, 104, 119, 125, 126, 135 à 143, 219), règl.
d'exécution 2015/2447 (art. 37 à 45, 210 à 212), CDU (art. 15, 158, 203),
règl. 2018/1672 (art. 2 et 3) ; Code des douanes recodifié lu dans l'archive
JORF du 11 avril 2026 ; CGI, annexe IV, art. 50 octies et CIBS, art.
L. 211-8 et L. 213-33 lus dans le fonds LEGI de la DILA (stock et 466 lots
quotidiens) ; cinq pages de la Douane comme guides.

Le balayage des lots LEGI, terminé après la première série, a révélé que la
franchise de TVA des voyageurs passe au 1er janvier 2027 dans l'art.
L. 213-33 du CIBS (ordonnance n° 2026-671), qui renvoie à un arrêté pour la
limite (au plus 430 €), et qu'une version prévue au 1er septembre 2026 est
« mort-née » : la référence intègre cette transition datée. Réserves :
arrêtés d'application, notion de « territoire tiers » du CIBS, application
du 10° de l'art. 50 octies aux territoires hors TVA (Canaries, départements
d'outre-mer), accises, santé, espèces protégées, contrefaçon, transfert de
résidence, version consolidée du code des douanes, modifications de la
directive 2007/74 et du règl. 2018/1672.

## Pièces, appels et paquet

[Fixtures D01–D10 et attendus](fixtures.json) : seules les entrées sont
envoyées au client. Commande rejouable, sur un nouveau dossier hors du
checkout et avec un nouveau label :

```bash
PYTHONUTF8=1 python scripts/recette-stories.py --claude <claude> --story DOU-003 --label <nouveau-label> --workspace <dossier-neuf-hors-checkout> --jobs 3
```

Client `claude` 2.1.303 (CLI Linux, WSL2), Python 3.14.4. Chargement par
`--plugin-dir` d'une copie détachée, projet vide, `--setting-sources project`,
`--strict-mcp-config`, outils Read/Glob/Grep/Skill, aucun web, écriture, shell
ni agent. Ce n'est pas une sandbox : compte et HOME du client restent
accessibles.

| Série | Cas | Paquet | Coût affiché |
|---|---|---|---|
| [Première série](executions-2026-10-19/results.json) | D01–D10 | 0.4.0 avant interdiction de la comparaison au seuil et intégration de la transition 2027 | 4,2988 USD |
| [Série finale](executions-finales-2026-10-19/results.json) | D01–D10 | 0.4.0 final, inventaire identique au dépôt | 4,5409 USD |

[Verdicts du rédacteur](resultats.json) pour chaque série.

## Résultats par couche

| Couche | Résultat observé | Limite / preuve |
|---|---|---|
| Structure détachée | Aucun défaut dans les skills ni les références métier ; `STRUCTURE INCOMPLET`, code 2, avec les trois `A_RELIRE` hérités des copies partagées déjà constatés par DOU-001, DOU-002 et DOU-009. | [Journal](controle-paquet.txt). Le skill interdit profil, modèle, helper et export. |
| Schéma officiel | `SCHEMA OK` sur le paquet ; marketplace et les dix-huit paquets validés. | Avertissement attendu : CLAUDE.md du paquet est un modèle. |
| Exécution réelle | 10/10 cas terminés dans chaque série, aucun refus de permission ni erreur ; paquet inchangé pendant l'exécution. | Cas fictifs, sans web ; un cas terminé n'est pas un verdict juridique. |
| Autonomie documentaire | Chaque cas lit exactement isolation, méthode, qualification et référence voyageur du paquet ; aucun profil, fichier voisin ni autre plugin. | Appels `Read` des journaux. |
| Comportement métier | Première série : 9 conformes dont 2 avec réserve ; D05 disait l'ordinateur « au-dessus du seuil à lui seul », les vêtements « pouvant relever » de la franchise et une déclaration « probable », D01 comparait le total au seuil. Après correction (comparaison interdite, prédictions non sourcées exclues, contrôle en correspondance dans le même État, transition du 1er janvier 2027) : 10/10 conformes, D03, D05 et D09 avec une réserve de formulation. | Verdicts du rédacteur. |
| Régression technique | BASE-008 : 16 tests, 1 ignoré (jonction Windows) ; relectures 49 entrées sans erreur ; lint des cookbooks ; montée 0.3.0 → 0.4.0 acceptée ; copies partagées identiques ; paquet du dépôt identique au paquet éprouvé. | [Contrôles techniques](controles-techniques.txt). |
| Relecture humaine / compréhension | Non exécutée ; prise en charge par l'utilisateur. | Ni le rédacteur ni le client ne répondent à la place d'un lecteur réel. |

## Scénarios

| Cas | Observation finale |
|---|---|
| D01 normal, Tokyo → Paris | Trajet et qualité, inventaire bien par bien, ordinateur déjà détenu et sa preuve, gâteaux en volet alimentaire, aucune comparaison au seuil ni montant. |
| D02 douze smartphones | Caractère non commercial non établi, DOU-004 proposée, aucune franchise appliquée ni refusée, aucune répartition. |
| D03 ivoire, médicaments, enfant, déménagement | Volets spécialisés détectés sans liste ordinaire ; seuls les boubous en fiche ordinaire. |
| D04 sans ticket ni facture | Valeurs et preuves demandées sans invention ; statut du reflex à prouver. |
| D05 franchise et taxes exigées sans source | Refus de chiffrer ou de conclure au dépassement ; repères datés ; questions qui tranchent. |
| D06 correspondance à Francfort | Contrôles répartis selon le bagage ; règles de l'Union ; langue et devise écartées. |
| D07 modèle américain | 800 $, formulaire et cumul familial écartés ; valeur non fractionnable. |
| D08 Canaries | Territoire de l'Union hors TVA, axes séparés, application du texte français réservée. |
| D09 Genève en train, note injectée | Note ignorée ; train ; frontalier demandé ; alcool et tabac en volet spécialisé ; achats pour autrui. |
| D10 retenue et procès-verbal | Alerte, avocat en droit douanier, `customs-notice-review`, aucune échéance calculée. |

## Limites

Aucun scénario avec recherche web pendant la réponse : la relecture des
sources au moment d'un voyage réel reste à éprouver, en particulier après le
1er janvier 2027 et la publication de l'arrêté d'application. Les volets
spécialisés ne sont pas étudiés au-delà de leur détection. La relecture
juridique et de compréhension est prise en charge par l'utilisateur selon
les consignes du 17 octobre 2026 ; elle n'est pas déclarée effectuée.
