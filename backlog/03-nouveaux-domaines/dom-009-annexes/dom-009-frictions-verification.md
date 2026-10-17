# DOM-009 — Vérification de l'intégration des 75 frictions

Lot du **17 octobre 2026 (Europe/Paris)** : [source fournie](../sources/douanes-frictions-2026-10-16.txt), [matrice](dom-009-frictions-utilisateurs.md), complément du découpage et de DOM-009, neuf propositions DOU, IND-027 et treize cadrages voisins. DOM-009 reste `terminee` ; les douze suites DOU restent `proposee`, sans sélection. C01–C26 et V01–V04 sont des codes locaux de tâches candidates, pas de nouvelles stories ni des commandes disponibles.

## Relecture documentaire des parcours

Lecture par le rédacteur des exigences sur demandes fictives ; les futurs skills ne sont pas exécutés. Les résultats ci-dessous indiquent le routage et les limites trouvés dans les documents, sans résoudre les consultations.

| Demande fictive | Résultat documentaire prévu |
|---|---|
| « TVA payée sur le site puis 25 € de douane à la porte » | DOU-001/C01 ventile TVA, droits et frais avec preuve des deux paiements ; C02/V04 et V01 distinguent correction fiscale/douanière et honoraires. Aucune somme remboursable confirmée. |
| « Mon colis vaut moins de 150 €, donc tout est exonéré » | Point 3 : date, régime et catégories à établir ; assertions 2026 réservées à la recherche. Aucun forfait 3 €, taxe 2 € ou exemple chiffré adopté. |
| « Le suivi dit douane ; mes pièces sont déjà envoyées mais le stockage continue » | DOU-001 demande auteur/statut et document réel ; V01 documente tarif, dates et causalité ; DOU-009 seulement si acte officiel. Aucune mainlevée promise. |
| « Le vendeur dit DDP, le représentant me nomme déclarant » | V03 traite la clause, C11 le mandat et les rôles, C12 l'éventuelle dette ; engagement du vendeur distinct de qualité de redevable. |
| « La déclaration ne peut plus être corrigée et j'ai renvoyé le produit » | C02 rectification, C03 invalidation, DOU-010/011 selon paiement et motif ; remboursement vendeur, TVA et frais privés ont leurs circuits et calendriers. |
| « Je suis micro en franchise et n'ai rien payé à la douane » | IND-027/V04 : flux, régime TVA, identification, déclaration et déduction à rechercher ; DOU-004 distingue EORI/TVA/habilitations, C20 EMEBI des états fiscaux. Aucun formulaire obligatoire universel. |
| « Mon couteau revient du client pour réparation, puis repartira » | K03/C05 : série, propriété, première sortie et motif ; retour en l'état C04, réparation hors UE C06 et échange ne sont pas confondus. Pas d'importation neuve présumée ni facture fictive. |
| « Je pars en salon avec des échantillons, je pourrai peut-être les vendre » | C07 : itinéraire, inventaire et intention de vente ; validité ATA, admission, réexportation et vente définitive distinctes, règles du pays à vérifier. |
| « Le manche est en mammouth et la palette est en bois, tout est libre ? » | K02/C22/C23 : identification matière/espèce et licéité, règles locales et CITES, emballage et produit distincts ; aucune exemption depuis le nom annoncé. |
| « Mon couteau français avec marquage CE peut partir au Canada ou au Royaume-Uni » | K01/K04, C24, EXIST-004 et DOU-007 : mécanique, destination et transporteur ; texte CE à identifier, fabrication et préférence séparées. Aucun passeport mondial ni interdiction générale. |
| « Projet de redressement, PV et proposition de transaction : que signer ? » | DOU-009 lit les actes ; C10 observations distinctes du recours final ; avocat douanier et découpage pénal DOM-002 pour PV/transaction. Aucune signature/refus systématique conseillé. |
| « La douane suspecte une contrefaçon ; j'ai une facture, je peux attendre » | C17/EXIST-008 : notification/réception et destruction en tête, titre et preuves d'authenticité séparés de la procédure ; suspicion non assimilée à preuve, aucun accord ou opposition envoyé. |
| « J'ai contesté l'AMR, le médiateur est saisi, la garantie vient d'être refusée » | C12/C13/C14/C15 : calendriers créance, suite judiciaire, sursis et garantie distincts, aide d'un avocat urgente ; médiation sans suspension générale présumée. |
| « C'est livré, donc le transit et le virement sont réglés » | C09 : apurement à prouver séparément de livraison ; BNK-014/019 selon contrat pour fonds bloqués, sans contournement des contrôles. |
| « L'indemnité est au poids ; je pensais être assuré pour toute la valeur » | V01/V02 : plafond de responsabilité et police d'assurance distincts ; contrat, exclusions, valeur/poids et déclaration à rapprocher sans garantie ni montant confirmés. |

## Contrôles documentaires

- Copie de la pièce jointe comparée à l'octet près ; SHA-256 : `21d74c0d0da96bb9cef35ab35e66fe708a7039426d3a72c4b031762ff3518dc8`.
- Matrice : titres identiques au guide et séquence 1–75 complète sans doublon. C01–C26, V01–V04, D01–D15, R01–R10 et K01–K05 complets et uniques ; les douze propositions DOU sont liées. Le calcul conditionnel C26 reste distinct de toute préparation documentaire.
- Lot : 29 fichiers dont 28 Markdown ; 1 758 liens locaux existants et 46 tableaux de largeur constante. Markdown en UTF-8 sans BOM, avec saut de ligne final et sans espaces finaux. Source brute conservée sans normalisation selon `.gitattributes`.
- Les textes initiaux des 25 documents complétés et les 24 frontmatters sont conservés (comparaison après normalisation CRLF/LF). L'index ETAT est régénéré ; aucun statut, priorité ou dépendance modifié, aucune nouvelle story ni changement de plugin.
- `python -X utf8 backlog/etat.py`, puis `--check` : index cohérent, source et annexes accessibles depuis DOM-009/ETAT. `git diff --check` passé après correction du format du complément consommation ; diff relu.
- `python scripts/check-version-bump.py` : passé contre `origin/main`. `python -X utf8 scripts/lint-tool-scope.py` : cinq cookbooks passés ; première invocation sans UTF-8 interrompue par l'encodage Windows du caractère de résultat, puis relancée avec succès. Les 178 JSON suivis par Git sont lisibles.
- Validation de paquet et recette client non exécutées : aucun paquet ni skill modifié dans ce lot documentaire. Les scénarios des suites et candidats restent futurs.

Ces vérifications de couverture, liens, format et préservation sont exécutées avec des commandes temporaires de maintenance, sans ajouter un test miroir au dépôt. Les relevés et empreintes du cadrage initial restent historiques et ne sont pas régénérés pour faire passer cette intégration pour une exécution métier.

## Portée et reste à faire

Intégration documentaire des besoins et lecture par le seul rédacteur. Aucun texte de droit externe ouvert, aucune version/règle, taxe, montant, délai, juridiction, coordonnée ou admissibilité de produit validés. Les références officielles citées dans la source restent des pistes non consultées. Aucune implémentation/exécution de skill, installation, validation client, recherche réelle d'origine/classement, déclaration, transmission, signature, paiement ou démarche externe.

Les 26 candidats douaniers et quatre candidats voisins exigent encore découpage, propriétaires confirmés, sources et recettes ; PV/transaction/défense pénale, médiation et volet PI/conformité nécessitent leurs stories propres. Les suites existantes ne deviennent pas des fonctions livrées du fait de leurs compléments. Les contrôles statiques établissent la cohérence de ces exigences, pas la qualité juridique de réponses futures.

La relecture humaine est prise en charge par l'utilisateur conformément à AGENTS.md du 17 octobre 2026 ; elle n'est pas déclarée effectuée, ni la compréhension d'un lecteur réel observée. Elle ne maintient pas le cadrage DOM-009 ouvert et ne dispense pas des validations techniques des futures implémentations.
