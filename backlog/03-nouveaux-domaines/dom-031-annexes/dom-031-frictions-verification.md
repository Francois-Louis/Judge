# DOM-031 — Vérification de l'intégration des frictions décès et obsèques

Lot du **16 octobre 2026** : [matrice des besoins](dom-031-frictions-utilisateurs.md), [texte intégral](../sources/deces-obseques-frictions-2026-10-16.txt), compléments des douze propositions FUN et des propriétaires voisins. Aucun statut, rang, manifeste ou fichier de plugin modifié par ce lot. Le contrôleur et le relevé JSON du cadrage initial restent historiques.

## Relecture documentaire des parcours

Relecture par le rédacteur, sur demandes fictives : les observations portent sur les exigences écrites, sans exécution de skill ni réponse juridique à ces dossiers.

| Demande fictive | Observation sur le backlog après complément |
|---|---|
| « Il faut signer ce soir, sans devis ; deux offres annoncent des soins obligatoires » | Points 1–5 et 15, FQ01–FQ04 : demande de documents, pression et urgence distinguées ; comparaison à prestations comparables sans classement des entreprises ni obligation confirmée sans source. |
| « L'EHPAD a demandé le transfert et le funérarium me facture » | Points 29–30, FI02 et FM02 : initiateur, qualité, commande, dates, accueil et prise en charge à documenter ; la seule qualité de proche ne tranche pas la dette. |
| « Nous devons déclarer le décès à domicile sous le même délai qu'à l'hôpital ? » | Points 24–28 et FM01 : lieu et fonctions certificat/déclaration/acte distingués, règle à vérifier ; aucun délai importé d'un lieu à l'autre. |
| « Crémation demain, papa voulait être enterré ; le juge a déjà répondu » | Points 36 et 140, FW01–FW03 et D05 : décision irréversible et avocat en tête, jugement/notification demandés ; saisine spéciale et appel restent à découper, aucun recours général substitué. |
| « Je renonce à la succession, donc je ne dois rien pour les obsèques » | Points 74 et 134, FF03/FP01 : engagement, option et contribution séparés ; le point ouvert DOM-013/016 demeure, aucune dispense ou obligation de payer affirmée. |
| « Je peux attendre le partage pour répondre à la sommation et déclarer au fisc » | Points 69–72 et 78–80, D09–D12 : urgence et trois objets distincts ; DOM-016 et DOM-011 ont des tâches candidates, sans calendrier unique ni option conseillée. |
| « Le capital obsèques couvre tout, et l'AGIRA doit répondre comme pour une assurance-vie » | Points 90–103, FC01–FC03 et FO03–FO05 : capital, prestations, versement et facture séparés ; recherches obsèques/vie/fonds transférés qualifiées sans délai copié entre dispositifs. |
| « Les frais bancaires doivent être gratuits, une décision de 2026 a changé la loi » | Points 61–63 et tableau des affirmations : DOM-016 demande décision, publication, dispositif, effets temporels et décompte ; la réforme alléguée n'est ni confirmée ni écartée sans recherche officielle. |
| « Je suis pacsée, j'aurai automatiquement la réversion et le logement » | Points 109–112 et 120–124 : DOM-036/016/006 séparent régime de retraite, dévolution et occupation/bail ; tâches à découper, aucun droit automatique promis. |
| « La chambre EHPAD est vidée, on garde le dépôt et facture encore l'occupation » | Points 34 et 127–129 : tâche candidate DOM-025, dates, contrat, états et justificatifs ; la règle d'un dépôt locatif privé n'est pas transposée. |
| « On partage les cendres et on paie l'exhumation comme un transport initial » | Points 47–54, FE01/FU01–FU03 et D03 : restes, urne, opérations et autorisations distincts ; FUN-008, FUN-011 et FUN-012 ne sont pas fusionnés. |
| « Mon employeur refuse le congé, et je dois récupérer le salaire de mon père » | Points 115, 117 et 119 : deux tâches emploi candidates, statut privé/public qualifié (DOM-037 pour le public), qualité du demandeur et succession séparées ; aucune couverture annoncée par les skills d'embauche. |

## Contrôles statiques du complément

- Copie de la pièce jointe contrôlée par SHA-256 : `9775bc22c9975295248afb6f08e2443d244326214b19f612bf38278f7e5f155a`, identique à l'original.
- Les séquences des points source et matrice sont identiques : 1 à 142, sans trou ni doublon ; les deux séquences D01–D19 et R01–R19 sont complètes.
- Contrôle ciblé des 33 fichiers Markdown du complément : 526 liens locaux existants, tableaux de largeur constante, UTF-8 sans BOM, fin de ligne et espaces ; les douze propositions FUN gardent leur statut et leur frontmatter. Aucun répertoire `funeral-legal` créé.
- `python -X utf8 backlog/03-nouveaux-domaines/dom-031-annexes/dom-031-controles.py` : contrôles de frontmatter/dépendances, douze suites bornées, table de découpage, scénarios/qualités, absence de plugin, format/liens, tableaux, index/préalables, JSON du dépôt, lint des outils et diff passés. Le contrôle des chiffres reste une relecture manuelle ; aucune règle chiffrée ajoutée dans les exigences. Comparaison par instantané du contrôleur non exécutée : la portée est contrôlée sur le diff propre à ce complément.
- `python -X utf8 scripts/check-version-bump.py` : passé, aucun paquet livré modifié. Les validateurs de paquets et recettes client ne sont pas pertinents pour ce lot de backlog.
- Index `ETAT.md` régénéré ; les ajouts des deux annexes de ce lot sont distingués des évolutions santé/véhicules simultanées. L'index Git du commit est vérifié séparément pour préserver ces autres travaux.

Les contrôles de couverture, liens et format du complément sont exécutés par un script temporaire de maintenance, sans ajouter un nouveau test au dépôt. Ils n'établissent pas la validité juridique des réponses futures ni une recette des scénarios métier.

## Portée

Intégration documentaire et relecture par le rédacteur de scénarios fictifs. Aucun texte de droit consulté ou validé, aucun délai/plafond/montant adopté, aucune statistique utilisée comme mesure de fraude ou de priorité. Les références supplémentaires sont des pistes de recherche. Aucun plugin créé, skill exécuté, paquet installé ou lecteur indépendant ; aucune démarche ni communication externe. Les domaines et procédures restant à découper sont explicitement signalés dans la matrice et leurs cadrages ; les points ouverts ne sont pas résolus par un simple lien.
