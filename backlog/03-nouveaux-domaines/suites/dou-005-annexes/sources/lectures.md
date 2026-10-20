# DOU-005 — Journal de recherche de maintenance

20 octobre 2026 (Europe/Paris). Sources de l'Union (CELLAR), Journal
officiel de la République française (archive DILA), pages de la Douane, de
la DGE et de la DG Trésor, outils de la Commission. Les résultats de moteur
ont servi à trouver des pages ; ils ne sont pas retenus comme textes lus.
Aucune décision de justice lue ou citée. [Traces techniques](attempts.json) :
URL, statut HTTP, horodatage et empreinte SHA-256 de chaque reproduction
obtenue (pages web : sans empreinte, l'outil ne restituant qu'un résumé).

| Source | Voie | Observation et suite |
|---|---|---|
| Liste des consolidations | Requête SPARQL CELLAR (200). | Dernières consolidations : CDU au 12.12.2022, directive TVA au 14.04.2025, règl. 2015/2446 et 2015/2447 au 01.07.2026, règl. 2021/821 au 21.09.2026, règl. 833/2014 au 24.07.2026. |
| CDU, règl. (UE) n° 952/2013, consolidé au 12.12.2022 | `legal_sources.py eu` : EUR-Lex 202 (défi), CELLAR 200. | Art. 5 (points 6, 10, 12 à 16, 22 à 24), 18, 19, 51, 61, 81, 155, 158, 170, 171, 172, 194, 203, 263, 267, 269, 270, 271, 272 et 274 lus. |
| Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026 | Téléchargement direct CELLAR (200, 29,6 Mo). | Art. 1 point 19 (exportateur), 141 (§ 4 et 4 bis : envois postaux et express ≤ 1 000 EUR réputés déclarés), 142 (exclusion des marchandises prohibées ou restreintes), 244, 245 (déclaration préalable à la sortie) et 248 (invalidation, 150 jours) lus. |
| Règl. d'exécution (UE) 2015/2447, consolidé au 01.07.2026 | `legal_sources.py eu` : EUR-Lex 202, CELLAR erreur de transport (taille) ; téléchargement direct CELLAR (200, 42 Mo). | Art. 221 (bureau d'exportation, 3 000 EUR), 329 à 337 (bureau de sortie, présentation, notification par le transporteur, certification, procédure de recherche et preuves, envois fractionnés, déclaration a posteriori) lus. |
| Directive 2006/112/CE (TVA), consolidée au 14.04.2025 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Art. 131 et 146 lus ; transposition française (CGI art. 262 I, annexe III art. 74) non lue. |
| Règl. (UE) 2021/821, consolidé au 21.09.2026 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Art. 2 (points 1 à 3), 3, 4, 9, 10, 12 et 27 lus ; annexe I non consultée pour un produit. |
| Règl. (UE) n° 833/2014, consolidé au 24.07.2026 | `legal_sources.py eu` : EUR-Lex 202, CELLAR erreur de transport ; téléchargement direct CELLAR (200, 14,9 Mo). | Art. 2 § 1 (exportation directe ou indirecte de biens à double usage) et art. 12 octies § 1 (clause de non-réexportation vers la Russie pour des biens listés) lus comme exemples ; annexes non lues. |
| Code des douanes recodifié, partie législative (ordonnance n° 2026-265) | Archive JORF du 11 avril 2026 (200, 680 ko), lue sans extraction ; articles filtrés sur « export » et « sortie du territoire ». | L. 211-4, L. 221-1, L. 221-5, L. 231-1, L. 231-4, L. 426-1, L. 512-7, L. 512-8, L. 513-2, L. 522-1 et L. 522-2 lus ; parties réglementaire et arrêtés parcourues (précurseurs chimiques R. 243-x, double usage en transit R. 426-x), non retenues. |
| Douane : « Formalités à l'exportation, les notions essentielles » (23/11/2023), « S'assurer de la sortie effective… » (sans date), « Bénéficier de l'exonération à la TVA à l'exportation » (sans date), « Les nouvelles règles Incoterms® 2020 et la valeur en douane » (sans date), « Exporter des biens et technologies à double usage vers un pays tiers » (sans date) | Outil web (pages publiques). | Guides : étapes et certification électronique de sortie, formalités vers les DOM, mention de sortie comme justificatif de TVA et preuves alternatives, EXW compliquant la preuve de sortie, autorisation pour l'annexe I quel que soit le pays tiers. La page TVA mentionne aussi la situation des micro-entrepreneurs : non reprise comme règle, texte fiscal non lu. |
| DGE : « Mon bien est-il à double usage ? » (mise à jour du 6 décembre 2024) | Outil web. | Ordre de classement, outils indicatifs, demande hors licence au SBDU en cas de doute ou de clause attrape-tout. |
| DG Trésor : « Votre bien ou votre service est-il visé par des interdictions ou des restrictions commerciales ? » (18 juillet 2025) | Outil web. | Code tarifaire, catégories sensibles, autorités compétentes ; l'autorisation financière ne remplace pas les licences. |
| Carte des sanctions de l'Union (sanctionsmap.eu) | Outil web. | Page JavaScript : seul « Please wait » restitué ; non lue, non citée. |
| Commission : consultation TARIC ; Access2Markets (version du 14 octobre 2026) | Outil web. | Outils de consultation ; aucun produit ni pays consulté ; aucune valeur de règle. |

Aucune clé PISTE utilisée ni demandée. Non lus : règles Incoterms (Chambre
de commerce internationale), CGI art. 262 I et annexe III art. 74, BOFiP,
annexe I du règlement 2021/821 et listes nationales, autres régimes de
sanctions, Code de la défense, droit des pays de destination, ancien Code
des douanes pour des faits antérieurs au 1er mai 2026. Les lectures sont
intégrées à `preparation-exportation.md 1.0.0` ; elles ne certifient pas le
droit applicable à une exportation réelle.
