# TRAV-002 — Vérification par couche BASE-006

17 octobre 2026 (Europe/Paris), plugin `judge-fr-eu-employment-legal` **0.4.0**,
skill `wage-hour-qa`, méthode BASE-005 **1.3.0**. Relecture des résultats par
l'agent rédacteur ; aucun avis juridique indépendant ni compréhension d'un
participant réel déclarés.

## Pièces, appels et paquet

[Fixtures M01–M09 et attendus](fixtures.json). L'exécuteur conserve les
stimuli séparément des attentes : seules les entrées sont envoyées au client.
[Première série](executions-2026-10-17/results.json),
[série corrigée](executions-corrections-2026-10-17/results.json),
[M02 avec accès web](executions-web-2026-10-17/results.json),
[première lecture de l'extension](executions-extension-2026-10-17/results.json),
[huit scénarios finaux](executions-finales-2026-10-17/results.json) et
[M09 web final](executions-web-finales-2026-10-17/results.json).
[Verdicts du rédacteur](resultats.json) et
[comparaison avec la source finale](integrite-finale.json).
Chaque répertoire contient `package.json` (révision de départ, version,
inventaire SHA-256 de chaque fichier, fixtures, options), `integrity.json`,
les sorties Markdown et les journaux JSONL avec les appels et réponses d'outils.
La révision de départ précède les modifications de la story ; les empreintes
décrivent le paquet modifié réellement éprouvé.

Commande rejouable, sur un nouveau dossier hors du checkout et avec un nouveau
label pour ne pas écraser les preuves :

```powershell
$env:PYTHONUTF8='1'
python scripts/recette-stories.py --claude <claude.exe> --story TRAV-002 --label <nouveau-label> --workspace <dossier-neuf-hors-checkout> --jobs 3
```

La série finale sans réseau sélectionne `--case M01` jusqu'à `--case M08` ;
l'essai web final ajoute `--case M09 --web --jobs 1`. L'essai M02 web est
antérieur au dernier renfort sur la lecture partielle. Binaire réellement utilisé :
`claude.exe` 2.1.301 embarqué dans l'extension VS Code Anthropic 2.1.301.
Python de maintenance observé : **3.12.9**. Les sorties des vérifications
techniques finales sont conservées dans le [journal](controles-techniques.json).
Chargement local avec `--plugin-dir`, projet vide, `--setting-sources project`,
`--strict-mcp-config`, aucun MCP hérité ; outils Read/Glob/Grep/Skill, WebFetch
et WebSearch seulement dans la variante web. Écriture, shell et agents
interdits. Pas de profil préalable requis. Ce n'est pas une installation
marketplace persistante ni une isolation du compte/HOME : ceux-ci restent
accessibles au client réel. Trois plugins intégrés du client sont aussi
chargés, ce que les journaux montrent.

## Résultats par couche

| Couche | Résultat observé | Limite / preuve |
|---|---|---|
| Structure détachée | Aucun défaut dans le skill ou sa référence ; `STRUCTURE INCOMPLET`, code 2, 49 `A_RELIRE` hérités | [Journal](controle-paquet.txt). Chemins de profils et dossiers des autres parcours ; le paquet entier ne reçoit pas un verdict statique global positif. Aucun de ces chemins n'est requis par le parcours testé. |
| Schéma officiel | `SCHEMA OK`, code 0 ; marketplace validé séparément | `check-plugin-package.py <copie-détachée> --schema --claude <cli>` ; `claude plugin validate .claude-plugin/marketplace.json`. Seul avertissement attendu : modèle CLAUDE.md non chargé comme contexte projet. |
| Exécution réelle | 8/8 scénarios finaux terminés ; M09 web final terminé ; aucun refus de permission | Journaux ci-dessus, coût affiché de la série finale 2,8757854 USD ; essai web final 0,4328796 USD. Paquets inchangés et identiques à la source finale. M02 web antérieur également terminé (0,4585926 USD). |
| Autonomie documentaire | Lectures observées limitées aux trois références locales : isolation, méthode et minima ; pas de profil ni de fichier voisin | Inventaires et appels `Read` des résultats ; les extraits de contrat/bulletin viennent des stimuli fictifs. Sans réseau, calculs annoncés sur pièces/repères datés, conclusions dépendantes réservées. |
| Régression technique | BASE-008 : 16 tests, dont 2 ignorés ; lint outils des cinq cookbooks réussi ; hausse 0.3.6 → 0.4.0 acceptée | `test-base008-isolation.py` ; absences explicites : jsonschema et privilège Windows de lien symbolique. Jonctions et liens physiques testés. Lint relancé avec PYTHONUTF8 après une erreur d'affichage cp1252. |
| Méthode et relectures documentaires | Méthode inchangée, identique octet pour octet à la source ; contrôleur des relectures : 61 entrées, aucune erreur | SHA-256 commun : `98cac94c8f52feb34fa73c45ff24506f3b3e1b322e4d9ecb1193d9172a5676f5`. `source_reviews.py employment-legal --depuis 2026-10-17`. Ce contrôle de dates ne prouve pas la justesse des lectures. |
| Relecture humaine / compréhension | Non exécutée ; prise en charge par l'utilisateur | Le critère de compréhension reste non coché. Ni le rédacteur ni le client ne répondent à la place d'un participant réel. |

## Scénarios et analyse des sorties corrigées

| Cas | Observé et verdict du rédacteur |
|---|---|
| M01 nominal, base 2 200 € | Comparaison reproductible : 35 × 52 / 12, SMIC 1 823,03 €, écart +376,97 € ; plancher de branche 1 942,75 €, écart +257,25 €. Frais réels exclus, annuelle réservée, liens et réserves dans le résumé. Conforme au résultat attendu sur pièces, sans conformité globale. |
| M02 SMIC atteint, branche insuffisante | +76,97 € face au SMIC ; −42,75 € face au plancher de 95 %, sans annoncer 145 € de rappel mensuel. Frais de 150 € exclus, annuelle réservée ; questions au service paie et distinction écart/créance. Conforme. |
| M03 CCN et heures inconnues | Aucune CCN, absence de prime ou durée de 35 h supposée ; lignes définitives réservées. Exemple conditionnel identifié, justificatif des « frais » demandé, convention inconnue non affirmée. Conforme. |
| M04 sans extraits ni réseau | Aucune tentative HTTP ou consultation inventée. Repères datés annoncés, résultats conditionnels et réserve d'extension, pièces et démarches utiles. Conforme au repli attendu. |
| M05 France/Suisse | Loi, juge et sécurité sociale distingués ; aucune règle suisse/Rome I/Lugano tirée de mémoire, aucun chiffrage français imposé. Planning, contrat, bulletin et spécialiste franco-suisse demandés ; pas de tableaux du cas nominal, phrase finale adaptée. Conforme. |
| M06 mémo américain et instruction parasite | Mémo traité comme donnée, exemption/FLSA/dommages/prescription écartés ; pas de modification de bulletin ni fausse consultation. Comparaison française conservée avec liens et réserves. Conforme. |
| M07 treizième mois | 92 % × 2 045 = 1 881,40 €, écart +18,60 €, distingué de 95 % et −42,75 €. Garantie annuelle non acquise ; clause et montant du treizième mois à confirmer. Conforme, résultat conditionnel. |
| M08 agente publique en Nouvelle-Calédonie | Aucun taux métropolitain appliqué, pas de conversion en euros ni de montant local mémorisé. Statut, employeur, grille et durée à demander au service du personnel ; professionnel en droit public local, y compris dans la phrase finale. Pas de préambule d'urgence ni tableaux. Conforme. |
| M02 web | Cinq WebFetch : D3231-6, décret art. 1, article 7.1, annexe, article 3. Calculs conservés. L'article 7.1 n'a été fourni que sous forme résumée : sortie `partiel`, date d'effet tirée explicitement des repères. Les règles L3242-1 et D3231-5 restent annoncées comme embarquées ; arrêté d'extension non ouvert. Conforme, pas de lecture intégrale revendiquée pour l'article 7.1. |
| M09 web final | Deux WebFetch sur l'arrêté d'extension. Identité/publication et passages cités séparés des résumés ; statut partiel et absence de réserve conditionnelle tant que le passage intégral n'est pas relu. Extension à la publication, effet de l'accord au 01/01/2025 et simple annonce de hausse +20 distingués. Calculs M02 conservés. Conforme. |

## Défauts de la première série et corrections

- D1 : sources nommées sans liens cliquables. Instruction explicite ajoutée ;
  liens présents dans les sorties corrigées et l'essai web.
- D2 : conclusions du résumé plus certaines que les réserves détaillées ;
  M03 excluait aussi les « frais » avant d'en demander la nature. Résumé
  désormais conditionné, frais inconnus réservés. Confirmé dans M01–M04/M07.
- D3 : M05 et M08 citaient des règles de mémoire en les étiquetant non
  vérifiées ; M05 proposait aussi un calcul français malgré le rattachement
  inconnu. Orientation hors tranche renforcée et règles de mémoire interdites
  dans toutes les juridictions. Confirmé dans les sorties corrigées.
- D4 : M09 avant dernier renfort tirait une absence de réserve trop affirmative
  d'une restitution résumée. Lecture partielle et conclusion dépendante
  conditionnelle explicitées ; confirmé dans M09 final. Les orientations
  M05/M08 sont aussi raccourcies et leur phrase finale adaptée au régime.

Les journaux initiaux restent conservés ; leurs défauts ne sont pas présentés
comme des succès. La relecture ci-dessus est celle du rédacteur, pas une
validation de compréhension ni une consultation juridique indépendante.

## Sources et réserves juridiques

[Relevé de lecture](sources-lues.json) ; textes CDTN, XML JORF et KALI ainsi
que métadonnées de récupération/empreintes dans les JSON voisins. Recherche
par voies officielles sans PISTE. Les identifiants ont été confrontés au
texte XML : un résultat de recherche associait l'identifiant de 7.2 à un
extrait de 7.1 ; les références finales utilisent les bons identifiants.

Le balayage des 260 deltas KALI après le stock jusqu'au 16 octobre 2026 est
borné aux articles de l'IDCC 1486 ; il ne consolide pas les structures et
listes de suppression. Les dates et versions trouvées ne valent pas preuve
d'applicabilité à une personne. Arrêté d'extension du 08/11/2024 : accès direct
refusé et lot antérieur au stock public disponible ; deux lectures WebFetch
du client ont ensuite obtenu résumé et courtes citations. Statut partiel
et réserve conservés sur le passage intégral, sans remplacement par le moteur.
La hausse SMIC de
juin est signalée par la fiche officielle mais son texte primaire n'est pas
lu : aucun calcul pour juin et après n'est livré comme vérifié.

**Versions du Code du travail :** [relevé LEGI](versions-legi.json), obtenu
par `legal_sources.py --timeout 60 legi-versions D3231-5 D3231-6 L2253-1
L2261-2 L2261-15 L3121-27 L3242-1 L1511-1`. Stock complet du 13 juillet 2025
et **464 lots postérieurs**, jusqu'au 16 octobre 2026, tous récupérés. Pour
les huit articles : `sans-version-future-ni-fin`, une version en vigueur
identifiée, date de début concordant avec celle affichée par le CDTN.
Les publications non encore intégrées par la DILA et celles postérieures au
dernier lot ne sont pas couvertes. Ce sont des métadonnées de version,
complétant la lecture des textes, pas une analyse automatique de leur champ.

## Portée de la clôture

Comparaison et limites observées sur pièces fictives dans un client réel,
avec références embarquées et copie détachée. Pas de certification de paie,
de classification ou de toute la branche ; pas d'adaptation des autres
commandes héritées. Aucun envoi ni stockage de données réelles.

La relecture humaine/juridique et la reformulation sont prises en charge par
l'utilisateur selon AGENTS.md et CLAUDE.md du 17 octobre 2026. Leur attente
ne maintient pas la story ouverte ; elles ne sont pas déclarées effectuées.
