# DOU-003 — Journal de recherche de maintenance

19 octobre 2026 (Europe/Paris). Sources de l'Union (CELLAR), Journal
officiel de la République française et fonds LEGI de la DILA, pages de la
Douane. Un résultat de moteur a servi à trouver une page de la Douane ; il
n'est pas retenu comme texte lu. Aucune décision de justice lue ou citée.
[Traces techniques](attempts.json) : URL, statut HTTP, horodatage et
empreinte SHA-256 de chaque reproduction obtenue (pages web : sans
empreinte, l'outil ne restituant qu'un résumé).

| Source | Voie | Observation et suite |
|---|---|---|
| Directive 2007/74/CE du Conseil (CELEX 32007L0074) | `legal_sources.py eu` : EUR-Lex 202 (défi), CELLAR 200. | Acte initial lu en entier, art. 1 à 21 : champ (pays tiers et territoires hors TVA ou accises), transit, bagages personnels, caractère non commercial, seuils de 300 et 430 €, valeur non fractionnable, limites de tabac et d'alcool, moins de 15 et 17 ans, cas frontaliers. Modifications ultérieures non recherchées. |
| Règl. (CE) n° 1186/2009, consolidé au 01.07.2026 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Chapitre X, art. 41 lu (franchise de droits subordonnée à l'exonération de TVA ; territoires de l'art. 6 § 1 de la directive TVA). Seule modification listée : règl. (UE) 2026/382. |
| Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026 | Téléchargement direct CELLAR (200, 29,6 Mo), le script étant borné à 8 Mio. | Art. 1 points 5 et 21, 104, 119 (présomption et preuve du statut, § 3 f pour les bagages), 125, 126, 135, 136, 138 à 143 (déclaration verbale, actes réputés déclaration, exclusions des prohibitions) et 219 lus. |
| Règl. d'exécution (UE) 2015/2447, consolidé au 01.07.2026 | Téléchargement direct CELLAR (200, 42 Mo) ; consolidations datées du 01.01.2026 et du 01.01.2025 tentées d'abord (404). | Art. 37 à 45 (lieu des contrôles des bagages en vol de transit et de transfert) et 210 à 212 (preuve du statut des marchandises des bagages d'un passager) lus. |
| CDU, règl. (UE) n° 952/2013, consolidé au 12.12.2022 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Art. 15, 158 et 203 lus. |
| Règl. (UE) 2018/1672 (argent liquide) | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Acte initial, art. 2 et 3 lus ; sert à la détection. Modifications non recherchées. |
| Code des douanes recodifié (ordonnance n° 2026-265) | Archive JORF du 11 avril 2026 (200), lue sans extraction ; articles filtrés sur « voyageur », « bagage » et « argent liquide ». | L. 222-3, L. 222-4, L. 422-7, L. 422-13 et R. 613-1 lus ; aucun article national sur les franchises des voyageurs repéré. |
| CGI, annexe IV, art. 50 octies ; CIBS, art. L. 211-8 et L. 213-33 | Fonds LEGI de la DILA : dernier stock complet (13 juillet 2025) puis 466 lots quotidiens jusqu'au 18 octobre 2026, lus en flux par un script de maintenance qui réutilise les fonctions de `legal_sources.py` (`legi-versions` étant limité au Code du travail) ; articles retenus par mots-clés. Légifrance non tenté. | 50 octies : versions du 25 juin 2009 et du 1er juillet 2021 lues, 10° identique ; republié sans date de fin les 28 août et 4 septembre 2026, avec concordances vers le CIBS. L. 213-33 : version au 1er septembre 2026 (ordonnance n° 2025-1247) devenue « mort-née » le 28 juillet 2026 ; version créée par l'ordonnance n° 2026-671 du 27 juillet 2026, en vigueur différée au 1er janvier 2027, lue (lots des 28 juillet et 28 août 2026), concordance « 50 octies, 10° sauf le 3 ». Arrêtés d'application non lus. |
| Douane : démarche « tabac, alcool ou autres marchandises achetées hors de l'Union », fiches « franchises douanières et fiscales », « objets personnels et justificatifs », « voyagez en toute tranquillité », démarche « médicaments », pages de navigation « Vous voyagez » | Outil web (pages publiques). | Guides datés (sans date, 06/08/2026, 12/09/2023, 30/06/2026, sans date) ; seuils, cerfa 10070, DéclareDouane, carte de libre circulation repris comme guides ; G1 et G2 citent l'art. 41 du règl. 1186/2009 et le 10° de l'art. 50 octies (arrêté du 18 juin 2009). |

Aucune clé PISTE utilisée ni demandée. Les arrêtés d'application de
l'art. L. 213-33 du CIBS, la définition du « territoire tiers » dans ce
code, les règles d'accises des voyageurs (CIBS, arrêté du 16 juillet 2009,
circulaires citées par les guides), les règles de santé, d'espèces
protégées (CITES) et de contrefaçon, le régime du transfert de résidence
et les textes allemands d'application n'ont pas été lus. Les lectures sont
intégrées à `biens-voyageur.md 1.0.0` ; elles ne certifient pas le droit
applicable à un voyage réel.
