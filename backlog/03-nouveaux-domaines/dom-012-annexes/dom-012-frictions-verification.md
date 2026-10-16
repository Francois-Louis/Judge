# DOM-012 — Vérification de l'intégration des frictions allocations et aides

Lot du **16 octobre 2026** : [guide intégral](../sources/aides-sociales-frictions-2026-10-16.txt), [matrice des besoins](dom-012-frictions-utilisateurs.md) et compléments de douze cadrages/propositions. DOM-012 reste `proposee` ; aucune story d'implémentation créée ou sélectionnée. Les codes locaux de la matrice sont des tâches candidates à découper.

## Relecture documentaire des parcours

Relecture par le rédacteur sur demandes fictives. Les observations portent sur les exigences écrites ; les futurs skills ne sont pas exécutés.

| Demande fictive | Résultat prévu par les exigences |
|---|---|
| « J'ai travaillé assez, mais l'attestation dit démission et je n'ai rien reçu » | FT01/02 et TRAV-021 : attestation confrontée à la rupture et aux périodes, correction employeur distincte de l'admission ARE ; pas d'ouverture garantie. |
| « J'ai démissionné pour créer ; le projet sera validé ensuite » | Points 5–6, FT01 et TRAV-049 : chronologie préalable et rupture recueillies, risque et conseil avant décision ; aucune régularisation supposée possible. |
| « Mon ancien droit est repris et le premier virement est très tardif » | FT03/04 : reliquat/option et différés/attente/paiement distingués ; aucune comparaison de montants improvisée. |
| « La CAF a corrigé le salaire mais le trop-perçu existe encore » | PA01, IN01/03 et RC01 : preuve de correction, décompte et acte formel séparés ; demande de correction sans effet conservatoire présumé. |
| « Je suis colocataire, les virements viennent de mon autre compte » | RS01 et CT01 : faits de vie commune et origine des flux documentés séparément ; ni couple ni revenu déduits du seul mouvement bancaire. |
| « On m'impose les mêmes heures malgré ma santé et deux référents » | RS02 : contrat, contraintes et référent à établir ; demande d'adaptation et éventuelle sanction séparées, sans obligation uniforme importée du guide. |
| « J'ai l'ARCE, donc le second versement et le reste des droits sont acquis » | CR02/03 : conditions de chaque fraction, emploi/activité et reprise de droits à vérifier ; ACRE DOM-039 et fiscalité DOM-011 séparées. |
| « Ma SASU ne me paie pas, mon ami déclare son CA de micro : on fait pareil ? » | CR04/05, PA01 et DOM-039 : statut, revenus, rubriques et régularisation propres ; zéro rémunération ne dispense pas automatiquement de déclaration. |
| « La région était d'accord, j'ai acheté ; France Travail remboursera la formation » | CR06 et FD02 : financeurs, accord de principe, attribution, dépenses et contrat distincts ; DOM-010/027 reçoivent les tâches à découper, aucun remboursement promis. |
| « L'APL est versée mais le bailleur réclame le loyer entier ; le FSL est un prêt » | LG01/02 et SA04 : compte locatif, décision caisse et règlement local rapprochés ; prêt/subvention distincts, sans effet automatique sur dette ou maintien d'aide. |
| « L'AAH est reconnue, la caisse refuse de payer ; mon arrêt suffit pour les IJ ? » | SA01/03 et V05/V06/V09 : auteur, objet et conditions propres ; reconnaissance, paiement et arrêt médical séparés, pas de CRA/CMRA choisie sur le seul nom de l'aide. |
| « Je ne sais pas si je dois cette somme, le site propose une remise » | IN01/03/04 : position sur dette demandée, calcul et recours à examiner avant brouillon ; aucun effet de reconnaissance universel affirmé. |
| « Le médiateur s'en occupe, j'ai reçu une contrainte et n'ai plus de ressources » | IN05, RC01/02, D09/D10 : acte intégral, réception, opposition et conseil urgent en tête ; aides/urgence parallèles, aucune suspension générale attribuée à la médiation. |
| « Le contrôle est déclenché par un score, donc il prouve ma fraude » | CT01/02 et relais PRV/IA : sélection, données, constatations, décision et pénalité séparées ; correction des données distincte du recours de prestation. |

## Contrôles documentaires

- Copie intégrale comparée à la pièce jointe, SHA-256 identique : `407095492fe4a4f6ad0c24e199d81eb5b964492c8708292ff3c1b2bff1760bb2`.
- Points source/matrice : séquence 1–185 complète, sans doublon. Les références des points renvoient aux 38 tâches candidates définies dans l'annexe. Séquences P01–P03, V01–V09, D01–D12, R01–R10 et A01–A07 complètes.
- Contrôle des quatorze fichiers Markdown du complément : 128 liens locaux existants et onze tableaux de largeur constante ; UTF-8 sans BOM, fin de ligne et absence d'espaces finaux. Source conservée telle quelle, sans normalisation.
- Les douze fichiers complétés conservent leur contenu initial à l'octet près avant l'ajout et leur frontmatter inchangé. La réorganisation préexistante de DOM-012 est conservée dans le fichier de travail et exclue de l'index Git ; le commit ajoute seulement le complément à sa version HEAD.
- `python -X utf8 backlog/etat.py` puis `--check` : index régénéré et cohérent, source ajoutée aux documents de l'epic. Les deux annexes sont accessibles depuis DOM-012 ; le générateur les rattache à cette story mais n'affiche ses annexes que lorsqu'elle quitte les tableaux des propositions. Aucun statut ni priorité modifié.
- Vérifications de dépôt : contrôle des versions de paquets et lint de portée des outils passés ; JSON du dépôt lisibles ; diff contrôlé. Aucun fichier de plugin n'est modifié : validation de paquet et recette client ne s'appliquent pas à ce lot documentaire.

Couverture, liens, format et préservation sont vérifiés par des commandes temporaires de maintenance, sans ajouter de test au dépôt. La relecture des parcours ci-dessus reste une revue des exigences par le rédacteur ; elle ne prouve pas le fonctionnement de skills futurs.

## Portée

Intégration de besoins et relecture par le rédacteur. Aucun texte de droit consulté ou règle validée, aucun délai, taux, montant ou juge du guide adopté comme solution. Sources et nouveautés restent des recherches futures. Aucun plugin créé, paquet modifié/installé, skill exécuté, scénario métier recetté ou lecteur indépendant ; aucune démarche ou communication externe. La sélection d'un régime, le découpage en stories et certains propriétaires/procédures restent ouverts dans la matrice. Les contrôles statiques établissent la cohérence documentaire, pas la validité juridique d'une future réponse.
