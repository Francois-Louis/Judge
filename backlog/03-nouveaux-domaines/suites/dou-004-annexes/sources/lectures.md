# DOU-004 — Journal de recherche de maintenance

19 octobre 2026 (Europe/Paris). Sources de l'Union (CELLAR), Journal
officiel de la République française (archive DILA), pages de la Douane et
outils de la Commission. Les résultats de moteur ont servi à trouver des
pages de la Douane ; ils ne sont pas retenus comme textes lus. Aucune
décision de justice lue ou citée. [Traces techniques](attempts.json) : URL,
statut HTTP, horodatage et empreinte SHA-256 de chaque reproduction obtenue
(pages web : sans empreinte, l'outil ne restituant qu'un résumé).

| Source | Voie | Observation et suite |
|---|---|---|
| CDU, règl. (UE) n° 952/2013, consolidé au 12.12.2022 | `legal_sources.py eu` : EUR-Lex 202 (défi), CELLAR 200. | Art. 5 (points 4 à 6, 12, 15 à 19, 37), 9, 15, 18, 19, 48, 51, 56, 57, 59, 60, 70, 77, 134, 139, 144, 147, 149, 158, 170, 201, 203, 210, 211, 226, 250 et 256 lus. Le CDU ne définit pas l'« importateur » ; le mot apparaît à l'art. 5 point 41 (commission d'achat) et dans des dispositions sur la déclaration sommaire. |
| Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026 | Téléchargement direct CELLAR (200, 29,6 Mo), le script étant borné à 8 Mio. | Art. 1 point 18 et art. 3 à 7 (EORI : données, mise à niveau du système, non-établis, personnes autres que les opérateurs, invalidation) ; annexe B, titre II, E.D. 3/15 à 3/27 (importateur, déclarant, représentant et son statut, vendeur, acheteur) lus. |
| Directive 2006/112/CE (TVA), consolidée au 14.04.2025 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Art. 30, 70, 71, 201 et 211 lus ; transposition française non lue. |
| Code des douanes recodifié : partie législative (ordonnance n° 2026-265), réglementaire (décret n° 2026-266), arrêtés (arrêté du 8 avril 2026) | Archive JORF du 11 avril 2026 (200, 680 ko), lue sans extraction ; articles filtrés sur « représentant en douane », « procuration », « mandat », « EORI », « 293 A ». | L. 211-1 à L. 211-3, L. 221-1 à L. 221-6, L. 321-7, L. 522-1, L. 522-2, R. 221-11 à R. 221-17, R. 221-20 à R. 221-28 et A. 221-3 lus. L. 211-3 et L. 321-7 renvoient aux art. 292 et 293 A du CGI, non lus. |
| Douane : fiches « Le numéro EORI » (09/12/2025), « Vers un EORI SIREN unique… » (sans date), « Le représentant en douane enregistré » (31/05/2022), « Les nouvelles règles Incoterms® 2020 et la valeur en douane » (sans date), « À l'import ou à l'export : une obligation, déclarer sa marchandise » (22/05/2019) ; démarche « autoliquidation de la TVA à l'import » (sans date) ; page « Vous souhaitez importer » (sans date) | Outil web (pages publiques). | Guides datés : désactivation des EORI SIRET annoncée pour le second semestre 2026 sans date fixée ; Incoterm présenté comme répartition contractuelle des formalités et frais, sans désignation du déclarant ni du débiteur ; autoliquidation automatique depuis 2022 pour les assujettis ; entreprises sans numéro de TVA, au régime simplifié ou en franchise renvoyées au service des impôts. |
| Commission : consultation TARIC ; Access2Markets (version du 14 octobre 2026) | Outil web. | Outils de consultation par code, origine et date ; aucun produit consulté ; aucune valeur de règle. |

Aucune clé PISTE utilisée ni demandée. Non lus : règles Incoterms (Chambre
de commerce internationale, texte payant), CGI art. 292 et 293 A et leur
recodification éventuelle dans le CIBS au 1er janvier 2027 (non recherchée
dans le fonds LEGI pour cette tâche, la TVA restant hors périmètre),
règlement d'exécution 2015/2447, textes du mécanisme d'ajustement carbone
aux frontières, réglementations propres aux produits, modèle de procuration
publié par la douane, circulaire du 23 mai 2022 sur les représentants
enregistrés. Les lectures sont intégrées à
`qualification-import-professionnel.md 1.0.0` ; elles ne certifient pas le
droit applicable à une importation réelle.
