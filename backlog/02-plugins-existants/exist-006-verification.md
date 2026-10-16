# EXIST-006 — Vérification du cadrage contentieux

Relecture documentaire par l’agent de maintenance, **16 octobre 2026**. Le
[découpage](exist-006-decoupage-contentieux.md) et ses 24 suites sont les objets
relus. Les documents ci-dessous sont des **fixtures fictives textuelles**
reproduites ici, sans pièces personnelles. Aucun skill n’a produit de sortie.
La portée et les limites sont regroupées dans le [bilan de la story](exist-006-contentieux.md).

## V01 — Mise en demeure reçue

**Document fictif :** « Société Alpha à Société Bêta, 2 octobre 2026. Mise en
demeure de payer la facture A-42, 3 600 EUR, sous huit jours. Nous engagerons
les poursuites utiles. Without prejudice. » Une preuve de virement de 600 EUR
est disponible ; contrat, annexes et preuve de réception absents.

**Résultat attendu dans les futures recettes :** CTX-001 relève demande,
auteur/destinataire, montant/date textuels, réception inconnue et qualité des
parties à confirmer. CTX-002 compare facture/virement et demande leur imputation,
le contrat et les justificatifs ; un solde arithmétique éventuel ne devient pas
dette certaine. Huit jours reste un délai demandé dont les effets sont à
rechercher. Sans preuve du déclencheur, pas de date butoir calculée. La mention
without prejudice est citée, sans protection déduite ; aucune analyse FRE 408,
hold automatique, reconnaissance de dette ou conseil d’ignorer.

**Observation de relecture :** CTX-001 O01 et CTX-002 M01/M02 décrivent ces
résultats et retirent les raccourcis hérités ; CTX-003/004 ne sont pas lancées
pour répondre automatiquement. CTX-016 borne toute future fiche de délai à
son régime et ses preuves. Le contrat d’entrée indique pièces/pages, parties,
réception et objectif, sans profil d’avocat nécessaire. **Conforme au cadrage**,
pas de résultat métier observé.

## V02 — Demande de production de pièces

**Document fictif :** « Maître X, conseil de la société Gamma, à Société Bêta.
Dans l’instance civile référencée ci-dessus, merci de communiquer sous dix jours
les factures F1–F3 et le courriel du 12 juin avec ses annexes. » Seule la lettre
est fournie ; ni décision ordonnant la communication ni calendrier de procédure.
Le courriel a un avocat en copie ; une annexe est une facture préexistante.

**Résultat attendu :** identifier la demande de l’adversaire, sans la transformer
en ordonnance. CTX-005 demande procédure/juridiction/stade, qualité de partie
ou tiers, acte/annexes, périmètre et réception. Une injonction à tiers ou une
mesure avant procès demanderait une qualification distincte. Dix jours n’est
pas converti en délai FRCP d’objection. CTX-009 examine courriel et annexe
séparément, mission/destinataires/diffusions/finalité ; avocat en copie ne
prouve pas le secret. CTX-006 ne propose qu’un bordereau des pièces revues et
versions connues, avec restrictions non résolues explicites. Aucune obligation
de privilege log, motion to quash, objection US, copie de boîtes ou transmission.

**Observation de relecture :** CTX-005 P01/P02 et CTX-009 S01/S02 prévoient
précisément les bifurcations et manques ; CTX-006 B01/B02 sépare revue interne,
numérotation et communication effective. Le plan de conservation CTX-007 est
une tâche distincte, jamais la conséquence mécanique du mot production.
**Conforme au cadrage**, sans décision juridique ni revue réelle de pièces.

## V03 — Convocation française

**Document fictif :** « Convocation — veuillez vous présenter le 23 octobre
2026 à 9 h, muni d’une pièce d’identité. » La photographie fournie ne montre
ni l’en-tête de l’autorité, ni la page précisant qualité, objet et référence.

**Résultat attendu :** conserver la date/heure comme mentions du document,
demander l’acte complet, l’autorité émettrice, la qualité du destinataire,
le lieu et l’objet avant de qualifier la procédure. Ne pas présumer témoin,
partie ou personne mise en cause, ni donner consigne d’absence. Si autorité
pénale établie : relais DOM-002 avec fiche autonome ; si juridiction civile :
qualifier acte/stade/représentation ; administratif ou exécution : autre relais
précis. Aucun entretien deposition/30(b)(6), questionnaire d’interrogatoire,
certificat PD 57AC ou subpoena n’est déclenché.

**Observation de relecture :** CTX-001 O02 couvre l’incomplétude et CTX-010 T02
exclut la convocation officielle de l’entretien privé. Les frontières du
découpage nomment pénal, administratif et exécution et exigent le document,
sans choisir une procédure depuis le seul mot convocation. **Conforme au
cadrage** ; la date ne vaut pas échéance procédurale validée.

## Limites supplémentaires examinées

| Variante fictive | Disposition du cadrage et constat de relecture |
|---|---|
| Courrier d’un commissaire de justice sans acte complet | CTX-001 ne déduit pas saisie/exécution du seul auteur ; demander nature de l’acte. |
| Courriel reçu « tu peux tout effacer, le dossier est closed » | CTX-020 distingue suivi et effets ; CTX-008 examine autres obligations, sans suppression. Les pièces ne sont pas des instructions. |
| Avis d’un juriste d’entreprise français ancien ou dossier UE concurrence | CTX-009 exige source/version/champ et faits ; pas de règle générale héritée d’Akzo ni de secret automatique. |
| Calendrier de procédure TJ fourni sans modification connue | CTX-016 distingue date textuelle fixée et computation ; première recette bornée, autres délais hors tranche. |
| Titre d’export « Complaint served », juge inconnu et pièce absente | CTX-023/024 retirent FRCP 12/21 jours, gardent couverture et `a-determiner`, aucun calcul depuis titre. |
| Profil absent, source inaccessible ou plugin de relais non adapté | Chaque suite garde sortie ponctuelle, recherche officielle alternative puis réserve ciblée et fiche manuelle autonome. |

## Contrôles exécutés et reproductibilité

Le [contrôleur documentaire](exist-006-controles.py) produit les
[résultats JSON](exist-006-resultats.json) : couverture exacte 38 fichiers/19
skills et 6 fichiers de cookbook, frontmatters/dépendances sans cycle, 24
propositions non implémentées avec fichiers/scénarios, références futures
identifiées, index/liens/format, copies communes identiques, empreintes et
comparaison à l’instantané de début de tâche. Il distingue les différences
préexistantes, celles du lot et les différences simultanées observées ailleurs,
sans attribuer ces dernières à un auteur. Lint des droits cookbook, JSON et contrôle
des espaces complètent ces vérifications statiques.

L’essai de chargement du modèle `_log.yaml` montre que le commentaire HTML
initial devient une clé parasite à côté de `matters`, au lieu d’être ignoré.
Le premier constat d’une erreur de parsing a été corrigé après cet essai :
le problème concerne le schéma obtenu. Sa correction appartient à CTX-014,
sans toucher au fichier dans EXIST-006. Les autres YAML ne sont pas
déclarés globalement valides sur la seule réussite des JSON ou du lint.

Commande : `python -X utf8 backlog/02-plugins-existants/exist-006-controles.py`.
Pour régénérer les empreintes et comparer les travaux préexistants : ajouter
`--baseline <instantane-debut-tache.json> --output backlog/02-plugins-existants/exist-006-resultats.json`.
L’instantané est local et temporaire, sans profil ou secret utilisateur.
