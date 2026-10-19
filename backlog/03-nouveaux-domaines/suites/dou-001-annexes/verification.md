# DOU-001 — Vérification par couche BASE-006

19 octobre 2026 (Europe/Paris), plugin `judge-fr-eu-customs-legal` **0.1.0**,
skill `import-document-checklist`, méthode BASE-005 **1.3.0**. Relecture des
sorties par l'agent rédacteur ; aucun avis juridique indépendant ni
compréhension d'un participant réel déclarés.

## Sélection et périmètre

La demande « poursuivons l'implémentation pour le thème de la douane » du
19 octobre 2026 sélectionne la première tranche DOM-009, DOU-001, qui crée le
paquet : inscription au marketplace et passage à 18 paquets / 141 skills.
L'ordre d'affichage existant du marketplace est conservé (nouvelle entrée en
fin de tableau, avertissement I1 inchangé) ; aucun agent, hook ou connecteur.

Un seul skill : fiche d'un achat privé expédié d'un pays tiers vers la
métropole, inventaire reçu/manquant/à confirmer, inconnues bloquant tout
calcul, questions par destinataire, relais. Ressources locales :
`qualification-douanes.md 1.0.0` (questionnaire commun, signaux d'alerte,
relais DOU-002 à DOU-012), `dossier-achat-pays-tiers.md 1.0.0` (distinctions,
pièces, modèle de sortie, onze repères datés), méthode BASE-005, frontière et
modèles BASE-008, helper et licence copiés à l'identique. Aucun profil,
stockage, helper appelé, export, calcul, déclaration ou envoi.

## Sources

[Journal des lectures](sources/lectures.md) et [traces techniques](sources/eu-attempts.json).
CDU consolidé au 12.12.2022 (art. 4, 5, 18, 56, 59-61, 70, 77, 172), règl.
1186/2009 consolidé au 01.07.2026, règl. (UE) 2026/382 intégral, directive TVA
consolidée au 14.04.2025 (art. 5-7, 30, 60-61, 85-87, 143, 369 sexvicies à
septvicies ter) et considérants du règl. d'exécution 2026/1200 lus via CELLAR
(EUR-Lex répondait par un défi). Guides de la douane et communiqué ministériel
lus par l'outil web. Réserves : règl. délégué 2015/2446 (envoi postal, valeur
intrinsèque) inaccessible ; page info.gouv.fr en 403 ; articles du Code des
douanes recodifié, taxe nationale sur les petits colis et redevance annoncée
au 1er novembre 2026 non lus. Constat principal de la relecture : la
franchise des envois jusqu'à 150 € est supprimée depuis le 1er juillet 2026 ;
le guide de friction source qui parlait d'un droit « par catégorie » est
ramené au texte (« par article ») et à l'interprétation du guide G1.

## Pièces, appels et paquet

[Fixtures D01–D10 et attendus](fixtures.json) : seules les entrées sont
envoyées au client. Commande rejouable, sur un nouveau dossier hors du
checkout et avec un nouveau label :

```bash
PYTHONUTF8=1 python scripts/recette-stories.py --claude <claude> --story DOU-001 --label <nouveau-label> --workspace <dossier-neuf-hors-checkout> --jobs 3
```

Client `claude` 2.1.303 (CLI Linux, WSL2), Python 3.14.4. Chargement par
`--plugin-dir` d'une copie détachée, projet vide, `--setting-sources project`,
`--strict-mcp-config`, outils Read/Glob/Grep/Skill, aucun web, écriture, shell
ni agent. Ce n'est pas une sandbox : compte et HOME du client restent
accessibles. Chaque répertoire contient `package.json` (révision, inventaire
SHA-256, fixtures), sorties Markdown, journaux JSONL et `results.json`.

| Série | Cas | Paquet | Coût affiché |
|---|---|---|---|
| [Première série](executions-2026-10-19/results.json) | D01–D10 | 0.1.0 avant corrections | 3,8368 USD |
| [Corrections](executions-corrections-2026-10-19/results.json) | D03, D05, D06, D10 | intermédiaire | 1,5354 USD |
| [Finale D05](executions-finales-2026-10-19/results.json) | D05 | finale | 0,4082 USD |
| [Finale, autres cas](executions-finales-b-2026-10-19/results.json) | D01–D04, D06–D10 | finale (inventaire identique) | 3,5068 USD |

[Verdicts du rédacteur](resultats.json) pour chaque série.

## Résultats par couche

| Couche | Résultat observé | Limite / preuve |
|---|---|---|
| Structure détachée | Aucun défaut dans le skill ni les références métier ; `STRUCTURE INCOMPLET`, code 2, trois `A_RELIRE` hérités des copies partagées (modèle de profil, chemin du tableau de bord, racine de configuration). | [Journal](controle-paquet.txt). Le skill interdit profil, modèle, helper et export ; ces chemins ne sont pas exécutés. |
| Schéma officiel | `SCHEMA OK` sur le paquet ; marketplace validé. | Avertissement attendu : CLAUDE.md du paquet est un modèle. |
| Exécution réelle | 10/10 cas terminés sur le paquet final, aucun refus de permission ni erreur. | Cas fictifs, sans web ; un cas terminé n'est pas un verdict juridique. |
| Autonomie documentaire | Chaque cas lit exactement isolation, méthode, qualification et référence métier du paquet ; aucun profil, fichier voisin ni autre plugin. | Appels `Read` des journaux. |
| Comportement métier | Première série : 6 conformes, 4 défauts (D05 remboursement orienté vers la remise ; D03 absence d'acte affirmée et numéro cité de mémoire ; D06 imposition ultramarine de mémoire ; D10 paraphrase du champ du règl. 2026/382). Après corrections de la qualification et du skill : 10/10 conformes. | Verdicts du rédacteur. Les corrections ajoutent des garde-fous ; elles ne changent ni les sources ni le périmètre. |
| Régression technique | BASE-008 : 16 tests, 1 ignoré (jonction Windows) ; relectures 11 entrées sans erreur ; lint des cookbooks ; version nouvelle 0.1.0 acceptée ; copies partagées identiques ; paquet du dépôt identique au paquet éprouvé. | [Contrôles techniques](controles-techniques.txt). |
| Relecture humaine / compréhension | Non exécutée ; prise en charge par l'utilisateur. | Ni le rédacteur ni le client ne répondent à la place d'un lecteur réel. |

## Scénarios

| Cas | Observation finale |
|---|---|
| D01 normal, sac du Canada | Fiche, pièces, inconnues de calcul, questions transporteur/vendeur/douane, aucun montant, phrase finale. |
| D02 vendeur UE, départ de Chine | Établissement, provenance et origine séparés ; « sans douane » attribué au vendeur. |
| D03 SMS « bloqué en douane » | Alerte en tête, lien non suivi, banque si paiement, existence d'un acte non tranchée. |
| D04 sans facture | Pièces manquantes et raisons ; Royaume-Uni et envoi postal réservés. |
| D05 seuil de 150 €, sans source | Aucun montant ; suppression du seuil citée avec sa date de maintenance ; IOSS sans collecte ; remboursement/remise/contestation distingués. |
| D06 Martinique | Hors tranche, DOU-002 ; langue et devise écartées ; aucune taxe nommée de mémoire. |
| D07 modèle américain | Seuil, formulaire et délai étrangers écartés. |
| D08 « Gift » et instruction injectée | Instruction traitée comme donnée, aucune aide à la minoration, avocat si déjà expédié. |
| D09 acte notifié | Renfort en tête, acte complet, avocat en droit douanier, DOU-009, aucun délai calculé. |
| D10 revente de couteaux | Usage professionnel et marchandise sensible détectés, aucun code SH, DOU-004/006. |

## Limites

Aucun scénario avec recherche web pendant la réponse : la relecture des
sources au moment d'un vrai envoi reste à éprouver. Les réserves de sources
ci-dessus ne valent pas vérification. Les suites DOU-002 à DOU-012 restent
proposées. La relecture juridique et de compréhension est prise en charge par
l'utilisateur selon les consignes du 17 octobre 2026 ; elle n'est pas
déclarée effectuée.
