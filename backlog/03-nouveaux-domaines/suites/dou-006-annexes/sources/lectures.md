# DOU-006 — Journal de recherche de maintenance

20 octobre 2026 (Europe/Paris). Sources de l'Union (CELLAR), Journal
officiel de la République française (archive DILA), pages de la Douane et
outils de la Commission. Les résultats de moteur ont servi à trouver des
pages de la Douane ; ils ne sont pas retenus comme textes lus. Aucune
décision de justice lue ou citée. [Traces techniques](attempts.json) : URL,
statut HTTP, horodatage et empreinte SHA-256 de chaque reproduction obtenue
(pages web : sans empreinte, l'outil ne restituant qu'un résumé).

| Source | Voie | Observation et suite |
|---|---|---|
| Consolidations et modifications du règl. (CEE) n° 2658/87 | Requête SPARQL CELLAR (200). | Dernière consolidation au 01.01.2026 ; seul acte modificatif depuis 2025 : règl. d'exécution (UE) 2025/1926 du 22 septembre 2025 (NC 2026). Aucun acte de 2026 (NC 2027) trouvé à la date de lecture, alors que l'art. 12 prévoit une publication au plus tard le 31 octobre. |
| Règl. (CEE) n° 2658/87, consolidé au 01.01.2026 | Téléchargement direct CELLAR (200, 22,5 Mo). | Art. 1, 2, 3, 5, 9, 12 ; annexe I, première partie, titre I A (règles générales 1 à 6), B et C parcourus ; section XV, notes 1 et 2 ; chapitre 82, notes 1 à 3 et position 8211 (sous-positions à lame fixe et autres qu'à lame fixe) lus. Taux de la colonne 3 non repris. |
| Notes explicatives de la NC, JOUE C 119 du 29.3.2019 | `legal_sources.py eu` : EUR-Lex 202 (défi), CELLAR 404 (parenthèses du CELEX non encodées) ; téléchargement direct avec CELEX encodé (200, 3,7 Mo). | Préface lue ; chapitre 82 parcouru, sans note sur la position 8211. Les notes publiées depuis le 4 janvier 2019 ne sont pas recensées. Le document 2019/C 118, de même date, est sans rapport et écarté. |
| CDU, règl. (UE) n° 952/2013, consolidé au 12.12.2022 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Art. 15, 22, 23, 27, 28, 33, 34, 56, 57 et 188 lus. |
| Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026 | Téléchargement direct CELLAR (200, 29,6 Mo). | Art. 19 à 22 ; annexe A, notes des E.D. 31 02, 32 01, 32 02, 35 01 010, 35 01 020 et 38 04 pour la colonne RTC lues. Nouveaux éléments « [NOUVEAU] » du tableau non retenus, leur colonne n'ayant pas été établie. |
| Règl. d'exécution (UE) 2015/2447, consolidé au 01.07.2026 | Téléchargement direct CELLAR (200, 42 Mo). | Art. 16 à 23 lus. |
| Code des douanes recodifié (ordonnance n° 2026-265, décret n° 2026-266) | Archive JORF du 11 avril 2026 (200, 680 ko), lue sans extraction ; recherche plein texte sur « classement tarifaire », « renseignement tarifaire », « espèce », « nomenclature », « tarif douanier ». | R. 515-5 (contraventions, 2° fausse déclaration dans l'espèce, la valeur ou l'origine) lu. Aucune disposition propre au classement ni définition de l'espèce relevée ; décret n° 2010-428 (commission de conciliation et d'expertise douanière) abrogé par le décret n° 2026-266, son successeur non recherché (contentieux hors tâche). |
| Douane : « Obtenir un renseignement tarifaire contraignant (RTC)… » (sans date), « Connaître la nomenclature de votre marchandise » (sans date), « Informations et aides complémentaires à l'encyclopédie tarifaire RITA » (13/10/2026), « Espèce tarifaire des marchandises » (24/04/2026), service en ligne « EBTI » (29/09/2026) | Outil web (pages publiques). | Guides : pièces d'une demande, échantillons, français, gratuité, validité et portée pour le titulaire, export non opposable aux pays tiers ; espèce tarifaire et niveaux SH/NC/TARIC ; valeur des notes de l'OMD, des NENC et des règlements de classement ; dépôt dans EBTI depuis le 15 octobre 2024 et EORI SIREN depuis le 11 juin 2025. Le service instructeur est nommé CSMR sur une page et SND2R sur une autre : coordonnées non reprises, renvoi au site. Délai de recours indiqué par une page non repris (contestation hors tâche). |
| Commission : consultation TARIC (mise à jour du 19/10/2026), consultation des RTC (EBTI), Access2Markets (version 2026.10.1.3 du 14 octobre 2026) | Outil web. | Outils de consultation ; aucun produit consulté ; aucune valeur de règle. |

Aucune clé PISTE utilisée ni demandée. Non lus : notes explicatives et avis
de classement de l'Organisation mondiale des douanes (accès sur abonnement),
notes explicatives de la NC publiées depuis le 29 mars 2019, règlements de
classement de la Commission pour un produit donné, jurisprudence de la Cour
de justice, nomenclature de 2027, ancien Code des douanes pour des faits
antérieurs au 1er mai 2026, voies de recours contre une décision RTC. Les
lectures sont intégrées à `dossier-classement.md 1.0.0` ; elles ne
certifient pas le classement d'une marchandise réelle.
