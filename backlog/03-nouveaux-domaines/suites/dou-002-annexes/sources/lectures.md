# DOU-002 — Journal de recherche de maintenance

19 octobre 2026 (Europe/Paris). Sources de l'Union (CELLAR), Journal
officiel de la République française et fonds LEGI de la DILA, pages de la
Douane. Les résultats de moteur ont servi à trouver les pages de la Douane ;
ils ne sont pas retenus comme textes lus. Aucune décision de justice lue ou
citée. [Traces techniques](attempts.json) : URL, statut HTTP, horodatage et
empreinte SHA-256 de chaque reproduction obtenue.

| Source | Voie | Observation et suite |
|---|---|---|
| CDU, règl. (UE) n° 952/2013, consolidé au 12.12.2022 | `legal_sources.py eu` : EUR-Lex 202 (défi), CELLAR 200. | Art. 1 § 3 (échanges entre parties du territoire douanier où la directive TVA s'applique ou non) et art. 4 (territoire douanier : France hors PTOM, Monaco) lus. |
| Directive 2006/112/CE, consolidée au 14.04.2025 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Art. 5 à 7 lus : art. 6 § 1 c exclut du champ de la directive les territoires français des art. 349 et 355 § 1 TFUE. |
| Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026 | Téléchargement direct de la ressource CELLAR (200, 29,6 Mo), le script étant borné à 8 Mio (constat DOU-009). | Art. 1 point 35 (territoire fiscal spécial), 114 (présentation à l'arrivée, y compris dans le même État membre), 134 (déclarations, document unique, facture ou document de transport) et 188 lus ; codes B4 et H5 de l'annexe B repérés. |
| Règl. (CE) n° 1186/2009, consolidé au 01.07.2026 | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Art. 25 et 26 lus (envois de particulier à particulier depuis un pays tiers) : définition de comparaison seulement. |
| TFUE, art. 349 et 355 (CELEX 12016E349, 12016E355) | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Liste des régions ultrapériphériques françaises ; renvoi à l'annexe II. |
| TFUE consolidé 2016, annexe II (CELEX 12016E/TXT) | Le script refuse un CELEX contenant « / » ; téléchargement direct CELLAR (200, 1,65 Mo). | Annexe II lue : PTOM français (Nouvelle-Calédonie, Polynésie française, TAAF, Wallis-et-Futuna, Saint-Pierre-et-Miquelon, Saint-Barthélemy) et Sint Maarten. Les identifiants `12016EAN02` (EUR-Lex 202, CELLAR 404) et `12016E/AN2` (refusé par le script) ont été tentés d'abord. |
| Décisions 2010/718/UE (Saint-Barthélemy) et 2012/419/UE (Mayotte) | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Saint-Barthélemy PTOM au 1er janvier 2012 ; Mayotte région ultrapériphérique au 1er janvier 2014. |
| Décision (UE) 2021/991 du Conseil | `legal_sources.py eu` : EUR-Lex 202, CELLAR 200. | Considérant 1 et art. 1 lus (différentiels d'octroi de mer jusqu'au 31 décembre 2027) ; modifications ultérieures non recherchées. |
| Code des douanes recodifié (ordonnance n° 2026-265, décret n° 2026-266) | Archive JORF du 11 avril 2026 (200), lue sans extraction ; articles de l'annexe filtrés sur les mots « Guadeloupe », « outre-mer », « octroi de mer », « Mayotte », « Saint-Martin », « Saint-Barthélemy », « Saint-Pierre ». | 193 articles repérés ; L. 121-1 à L. 121-3, L. 710-1, L. 720-1, L. 721-2, L. 730-1 et L. 741-2 lus en entier ; livre VII parcouru par ses intitulés. Aucun article pour la Nouvelle-Calédonie, la Polynésie française ou Wallis-et-Futuna. |
| CGI art. 291, 294, 295, 296, 262 ; annexe IV art. 50 octies à 50 octies C ; loi n° 2004-639 relative à l'octroi de mer | Fonds LEGI de la DILA : dernier stock complet (13 juillet 2025) puis 466 lots quotidiens jusqu'au 19 octobre 2026, lus en flux par un script de maintenance qui réutilise les fonctions de `legal_sources.py` (outil `legi-versions` limité au Code du travail). Légifrance non tenté : refus des requêtes scriptées constaté par BASE-010/BASE-018. | Versions en vigueur lues (CGI 294 et 296 depuis le 1er janvier 2014 ; loi 2004-639 art. 8 depuis le 1er avril 2023 ; annexe IV art. 50 octies depuis le 1er juillet 2021). Voir la ligne de contrôle des lots ci-dessous. |
| Douane : fiche Guadeloupe, démarche « envois non commerciaux », FAQ Guyane, actualité du 31 mars 2023 | Outil web (pages publiques). | Guides datés (01/04/2026, sans date, 22/11/2019, 31/03/2023) ; seuils et conditions repris comme guides ; G3 périmé sur le seuil de 205 €, G1 antérieur à la suppression de la franchise de 150 € pour les achats hors Union. |

Aucune clé PISTE utilisée ni demandée. Les délibérations locales fixant les
taux d'octroi de mer, les textes de renvoi de l'annexe IV (règl. (CEE)
n° 918/83, arrêté du 16 septembre 2004), les régimes fiscaux de Saint-Martin,
Saint-Barthélemy et Saint-Pierre-et-Miquelon et les régimes douaniers et
fiscaux des collectivités du Pacifique n'ont pas été lus. Les lectures sont
intégrées à `envoi-outre-mer.md 1.0.0` ; elles ne certifient pas le droit
applicable à un envoi réel.
