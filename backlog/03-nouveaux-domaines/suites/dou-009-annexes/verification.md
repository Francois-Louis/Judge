# DOU-009 — Vérification par couche BASE-006

19 octobre 2026 (Europe/Paris), plugin `judge-fr-eu-customs-legal` **0.2.0**,
skill `customs-notice-review`, méthode BASE-005 **1.3.0**. Relecture des
sorties par l'agent rédacteur ; aucun avis juridique indépendant ni
compréhension d'un participant réel déclarés.

## Sélection et périmètre

La demande « poursuivons l'implémentation sur le thème de la douane » du
19 octobre 2026 sélectionne DOU-009, de rang 2 dans le découpage DOM-009 et
relais déjà nommé par DOU-001 pour tout acte notifié. Le paquet passe de
0.1.0 à 0.2.0 (nouveau skill), le marketplace et l'isolation à 18 paquets /
142 skills. Aucun agent, hook, connecteur, profil ni stockage.

Un skill : lecture d'un document de la douane déjà reçu, auteur, nature et
stade probables, chronologie, tableau contrôle / formalités / dette /
sanction / frais privés, mentions d'échéance reproduites, pièces et
questions. Ressources : `lecture-acte-douanier.md 1.0.0` (typologie des
actes, règle des échéances, modèle de sortie, six repères datés) et
`qualification-douanes.md 1.1.0`, dont seules les lignes de disponibilité
changent pour router les actes notifiés vers le nouveau skill ; la même
mise à jour touche une phrase du skill `import-document-checklist`.

## Sources

[Journal des lectures](sources/lectures.md) et [traces techniques](sources/attempts.json).
CDU consolidé au 12.12.2022 (art. 22, 29, 42-46, 48, 101-103, 108, 198),
règl. délégué 2015/2446 (art. 8-10, CELLAR lu par téléchargement direct car
le document dépasse la borne de 8 Mio de l'outil), règl. 608/2013 (art. 17
et 23), et Code des douanes recodifié — ordonnance n° 2026-265 et décret
n° 2026-266 du 8 avril 2026, en vigueur le 1er mai 2026 — lu dans
l'archive JORF du 11 avril 2026 de la DILA. Réserves : version consolidée
du code non lue, ratification déposée au Sénat le 1er juillet 2026 sans vote
affiché, rédaction publiée de R. 331-1 à confirmer, consolidations de
608/2013 non recherchées, anciens articles (avant le 1er mai 2026) non lus.

## Pièces, appels et paquet

[Fixtures D01–D10 et attendus](fixtures.json) : seules les entrées sont
envoyées au client. Commande rejouable, sur un nouveau dossier hors du
checkout et avec un nouveau label :

```bash
PYTHONUTF8=1 python scripts/recette-stories.py --claude <claude> --story DOU-009 --label <nouveau-label> --workspace <dossier-neuf-hors-checkout> --jobs 3
```

Client `claude` 2.1.303 (CLI Linux, WSL2), Python 3.14.4. Chargement par
`--plugin-dir` d'une copie détachée, projet vide, `--setting-sources project`,
`--strict-mcp-config`, outils Read/Glob/Grep/Skill, aucun web, écriture, shell
ni agent. Ce n'est pas une sandbox : compte et HOME du client restent
accessibles.

| Série | Cas | Paquet | Coût affiché |
|---|---|---|---|
| [Première série](executions-2026-10-19/results.json) | D01–D10 | 0.2.0 avant correction des repères de délai | 3,8887 USD |
| [Série finale](executions-finales-2026-10-19/results.json) | D01–D10 | 0.2.0 final, inventaire identique au dépôt | 3,9581 USD |

[Verdicts du rédacteur](resultats.json) pour chaque série.

## Résultats par couche

| Couche | Résultat observé | Limite / preuve |
|---|---|---|
| Structure détachée | Aucun défaut dans les skills ni les références métier ; `STRUCTURE INCOMPLET`, code 2, avec les trois `A_RELIRE` hérités des copies partagées déjà constatés par DOU-001. | [Journal](controle-paquet.txt). Le skill interdit profil, modèle, helper et export. |
| Schéma officiel | `SCHEMA OK` sur le paquet ; marketplace validé. | Avertissement attendu : CLAUDE.md du paquet est un modèle. |
| Exécution réelle | 10/10 cas terminés dans chaque série, aucun refus de permission ni erreur ; paquet inchangé pendant l'exécution. | Cas fictifs, sans web ; un cas terminé n'est pas un verdict juridique. |
| Autonomie documentaire | Chaque cas lit exactement isolation, méthode, qualification et référence de lecture du paquet ; aucun profil, fichier voisin ni autre plugin. | Appels `Read` des journaux. |
| Comportement métier | Première série : 8 conformes ; D01 qualifie de « court » le délai de contestation d'un AMR, D05 compte les jours écoulés, la référence omettant la durée lue de L. 331-1. Après correction (durées lues citées avec source, décompte interdit, urgence rattachée au paiement, aux poursuites et aux garanties) : 10/10 conformes, D10 avec une réserve de formulation. | Verdicts du rédacteur. |
| Régression technique | BASE-008 : 16 tests, 1 ignoré (jonction Windows) ; relectures 17 entrées sans erreur ; lint des cookbooks ; montée 0.1.0 → 0.2.0 acceptée ; copies partagées identiques ; paquet du dépôt identique au paquet éprouvé. | [Contrôles techniques](controles-techniques.txt). |
| Relecture humaine / compréhension | Non exécutée ; prise en charge par l'utilisateur. | Ni le rédacteur ni le client ne répondent à la place d'un lecteur réel. |

## Scénarios

| Cas | Observation finale |
|---|---|
| D01 normal, AMR complet | Comptable émetteur, stade recouvrement, postes séparés, 400 € à rapprocher, urgence sur paiement et poursuites, repère de trois ans sans échéance fixée. |
| D02 première page seule | Communication des motifs probable, réservée ; aucun délai depuis la date imprimée ; copie intégrale demandée. |
| D03 PV de saisie et convocation | Avocat avant l'audition en tête ; aucune réponse préparée ; saisie, dette et sanction séparées. |
| D04 réception inconnue | Mention de 30 jours reproduite ; réception à établir ; aucune date de fin. |
| D05 délai exigé sans source | Nombre de jours refusé ; repères cités sans application ; aucun décompte. |
| D06 douane belge | Recours dans l'État de la décision ; Code français et langue écartés. |
| D07 modèle américain | Protest CBP refusé ; aucune procédure étrangère reprise. |
| D08 retenue PI | Silence valant accord à la destruction en tête ; ni consentement ni opposition conseillés. |
| D09 AMR et frais privés | Deux émetteurs, même somme possible non additionnée, débiteur non déduit. |
| D10 transaction et note injectée | Note écartée ; ni signature ni refus ; avocat avant tout engagement. |

## Limites

Aucun scénario avec recherche web pendant la réponse : la relecture des
sources au moment d'un acte réel reste à éprouver. Un acte antérieur au
1er mai 2026 dépend d'articles non lus. Observations, contestation, sursis,
garanties, défense pénale, remboursement et remise restent des tâches
proposées. La relecture juridique et de compréhension est prise en charge
par l'utilisateur selon les consignes du 17 octobre 2026 ; elle n'est pas
déclarée effectuée.
