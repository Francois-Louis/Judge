# Santé — Vérification du complément des frictions

Complément du **16 octobre 2026 (Europe/Paris)** à DOM-007. Il conserve le
[texte utilisateur](../sources/sante-frictions-2026-10-16.txt), relie ses
155 points et sections 12–15 dans la [matrice](dom-007-frictions-utilisateurs.md),
complète SAN-001 à SAN-012 et propose SAN-013 à SAN-019. Le cadrage initial
reste terminé ; les 19 suites restent `proposee`, sans extension sélectionnée.

## Relecture des frontières sur les exigences

Les cas suivants ont été relus dans les propositions par le rédacteur :
il s'agit d'une vérification du découpage, pas de réponses produites par
des skills exécutés.

| Cas | Distinction vérifiée dans les propositions |
|---|---|
| Refus après mention C2S et consultation privée proposée | SAN-013 demande des soins ; DOM-029 doit découper indices/discrimination ; SAN-011 les tarifs, DOM-012 les droits. Aucun refus discriminatoire conclu sur le seul récit. |
| Dossier incomplet, versions différentes et accès soupçonné | SAN-004 demande les catégories manquantes et préserve les versions ; PRV-001/025 traitent accès/finalités ; aucun calendrier RGPD appliqué au dossier ni falsification inférée. |
| Devis dentaire modifié, acte entrepris, mutuelle refusant un code | SAN-015 compare devis/options ; SAN-009 traite les questions sur consentement ; INS-009 lit la garantie ; SAN-014 demande une correction justifiée, sans recodification pour garantir remboursement. |
| Chambre imposée, forfait et titre hospitalier malgré paiement | SAN-011 demande preuve du choix ; SAN-014 rapproche facture/paiement et qualifie titre ; DOM-012 garde exonération/droits. Pas de simple relance réputée préserver un recours contre titre. |
| Infection, expertise adverse incomplète et offre définitive | SAN-006 oriente, SAN-018 prépare le dossier CCI, SAN-019 les observations factuelles ; DOM-035 doit découper le chiffrage ; CTX-039 lit la transaction. Ni faute, ni consolidation, ni montant acceptable établis. |
| Refus CPAM, réponse informelle et silence | DOM-012 doit découper notification/objet, CRA ou CMRA, acte requis, réception et rejet implicite éventuel ; aucun délai commun, aucun effet automatique d'une médiation ou demande RGPD. |
| IJ reçues par employeur mais paie discordante | DOM-012 garde prestation/décision ; le cadrage travail doit découper attestation/subrogation/paie. Les suites de suivi d'arrêt ne sont pas annoncées comme couvrant ce résultat. |
| Rupture de médicament avec effet indésirable déclaré | SAN-016 place orientation médicale avant brouillon, relève produit/lot utiles et vérifie circuit de vigilance, sans conseil de dose ou de substitution. |
| Transport prescrit après trajet, ALD et refus du partage | DOM-012 doit vérifier séparément prescription, prise en charge, mode/accord et partage ; SAN-014 garde les kilomètres/frais contestés ; aucune couverture ALD ou silence-accord automatique. |
| EHPAD, soins non tracés et proche sans pouvoir | SAN-017 qualifie volonté, pouvoir et régime propre de structure ; DOM-025 garde accompagnement et documents sociaux ; DOM-026 l'étendue du pouvoir. Pas de CDU automatique ni incapacité présumée par âge. |
| Soins psychiatriques et contention | SAN-010 place avocat et contrôle à vérifier en tête ; difficultés de rendez-vous vers SAN-013 ; mesure de soins et protection juridique distinctes. |
| Mon espace santé incomplet et souhait de masquage | SAN-001 identifie détenteurs ; privacy garde traitement/traces ; contrôles numériques propres encore à découper DOM-007/EXIST-003, sans accès au compte ni réglage réalisé. |

## Contrôles reproductibles

Le [contrôleur du complément](dom-007-frictions-controles.py) vérifie :
copie de la source si `--source` est fourni, numérotation et titres des
155 points, colonnes et liens de la matrice, sections 12–15, métadonnées
et graphe des dépendances du backlog, 19 propositions, sept propriétaires
uniques de skill/référence futurs, scénarios normal/limite, liens locaux,
formatage, huit relais et absence de plugin santé créé. Il ne valide ni
le sens juridique ni les fragments d'ancre Markdown.

```powershell
python -X utf8 backlog/03-nouveaux-domaines/dom-007-annexes/dom-007-frictions-controles.py
python -X utf8 backlog/etat.py --check
python scripts/check-version-bump.py
git diff --check
```

Les résultats exécutés sont consignés dans le
[relevé du complément](dom-007-frictions-resultats.json).
La copie jointe est identique (SHA-256
`d709e0662639e243bf909e65d0b0d139bc0883877b921f9eaafe532d92b953d0`).
Les six groupes de contrôles passent sur une copie de préparation contenant
HEAD et les seuls changements santé : 155 lignes, 19 propositions dont sept
nouvelles, 457 liens locaux et huit relais. L'index destiné au commit est
régénéré et son actualité contrôlée dans cette copie pour exclure les
ajouts concurrents des autres domaines. Contrôle des versions, lint de portée
des cinq cookbooks avec `python -X utf8` et lecture des JSON du checkout
également réussis. Le diff du lot est relu avant commit.

Les contrôles et résultats du lot initial DOM-007 ne sont pas réécrits pour
faire disparaître leur attente de douze suites initiales.

## Portée

Intégration documentaire et contrôles structurels du rédacteur ; aucun texte
officiel consulté, barème ou délai validé, skill implémenté/exécuté, paquet
installé, client ou lecteur indépendant testé, diagnostic, calcul de
remboursement ou indemnité réalisé. Les assertions temporelles de 2026
restent à vérifier. Les relais sans suite restent des besoins à découper.
Aucune demande, plainte, saisine, transmission, signature ou modification
de compte exécutée. Les changements parallèles hors santé sont conservés
et exclus du commit de ce complément.
