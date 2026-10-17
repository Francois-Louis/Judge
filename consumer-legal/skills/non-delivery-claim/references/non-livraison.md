# Commande non livrée : repères et brouillons

Version `1.0.0` — 17 octobre 2026 (Europe/Paris), CONSO-001.

Ces lectures de maintenance préparent la recherche, sans établir la loi
applicable à un dossier. Revenir aux textes et à leurs versions utiles selon
la [méthode locale](../../../references/shared/research-citation-method.md).
Faits antérieurs au 1er janvier 2022 : retrouver le régime ancien ; ne pas
projeter la numérotation et la séquence ci-dessous sur ce contrat.

## Sources effectivement lues et réserves

Lecture en français le 17 octobre 2026. Applicabilité `a-etablir` pour tout
futur dossier. Les pages Légifrance accessibles affichent parfois une date
antérieure à la demande : cette borne est conservée. Les tentatives directes
au 17 octobre échouent (403 ou contenu inaccessible). Les versions futures
françaises, rectificatifs et jurisprudences nouvelles ne sont pas vérifiés
exhaustivement ; aucune absence de modification n'est garantie. Ne pas
présenter ces lectures comme une veille juridique complète.

| Source officielle et nature | Passage et version réellement lus | Vérification / portée | Relecture |
|---|---|---|---|
| S1 — [Code de la consommation, chapitre VI, L216-1 à L216-8](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221247) — texte français consolidé | Chapitre entier ; page affichée au 7 octobre 2026 ; articles depuis le 1er octobre 2021, ordonnance 2021-1247, art. 8 et note art. 21 : contrats conclus à compter du 1er janvier 2022. | `verifie` pour les passages lus ; application temporelle au dossier conditionnelle. L216-1 : engagement puis défaut de date ; L216-2/3 : risques ; L216-6 : séquence et exceptions ; L216-7 : remboursement ; L216-8 : non-professionnels. | 2026-10-17 · inchangee · Légifrance, outil web connecté · page au 7 octobre, versions ultérieures à contrôler |
| S2 — [Directive 2011/83/UE du 25 octobre 2011, consolidation CELEX 02011L0083-20260927](https://publications.europa.eu/resource/celex/02011L0083-20260927) — instrument UE, consolidation documentaire | Articles 1 à 4 (champ), 18 (livraison), 20 (risque), 28 (transposition/application), en français via CELLAR ; consolidation au 27 septembre 2026. | `verifie` pour ces passages, pas tout l'instrument ; contexte européen uniquement, ne pas en déduire seule une obligation entre parties privées. Consolidation non authentique ; actes modificatifs/rectificatifs et transition à recontrôler au besoin. | 2026-10-17 · inchangee · CELLAR via legal_sources.py · EUR-Lex 202 puis CELLAR 200 |
| S3 — [Code civil, article 1217](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036829854/2025-03-31) — texte français | Texte entier, version depuis le 1er octobre 2018 ; loi 2018-287 art. 10 et note sur le caractère interprétatif, page au 31 mars 2025. | `verifie` pour le catalogue des remèdes ; ne suffit pas à en vérifier les conditions. Ne pas proposer suspension du paiement, réduction de prix ou indemnisation dans ce skill. | 2026-10-17 · inchangee · Légifrance, outil web connecté · portée temporelle à confirmer |
| S4 — [Code civil, 1344 à 1344-2](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070721/LEGISCTA000032035271) — texte français | Paragraphe entier, page au 5 octobre 2026 ; versions depuis le 1er octobre 2016, ordonnance 2016-131 art. 3. | `verifie` pour formes de mise en demeure et effet mentionné sur les risques ; ne pas présumer qu'une relance suffit ni cumuler mécaniquement avec les règles spéciales. Pas de calcul d'intérêt. | 2026-10-17 · inchangee · Légifrance, outil web connecté · articulation à vérifier au dossier |
| S5 — [DGCCRF, Livraison : obligations du professionnel et recours](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/livraison-quelles-sont-les-obligations-du-professionnel-et-les-recours) — guide public | Page affichée « écrit le 05/10/2026 », rubriques livraison, résolution, remboursement et risques lues. | `verifie` comme guide d'orientation, sans autorité normative autonome. Ses raccourcis ne remplacent pas S1 ; sa rubrique fraude vise aussi des victimes professionnelles, ne pas la transposer au client. | 2026-10-17 · inchangee · DGCCRF, outil web |
| S6 — [Code de la consommation, L221-15](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226852) — piste sur vente à distance | Ouvertures directes et variantes tentées le 17 octobre 2026 : aucun texte utile obtenu, HTTP 403. | `inaccessible` ; responsabilité et causes d'exonération non vérifiées à partir de cette piste. Aucune condamnation du vendeur ni transfert automatique vers le transporteur. | 2026-10-17 · inaccessible · Légifrance, deux outils web · réserve |

## Choisir la démarche sans confondre les étapes

Les indications qui suivent sont conditionnelles à la qualification, aux
pièces et à la relecture de la version applicable de S1. Elles ne doivent
pas devenir un délai ou un droit affirmé si la source n'a pas été lue pour
la réponse.

- **Engagement de livraison (L216-1).** Rechercher la date ou le délai annoncé,
  l'accord initial et une éventuelle modification acceptée. Délivrance :
  possession physique ou contrôle du bien. À défaut de date ou d'accord,
  le passage lu prévoit sans retard injustifié et au plus tard trente jours
  après conclusion. Ne pas ajouter trente jours à une date déjà promise.
- **Remise et risques (L216-2/3).** Identifier qui a reçu physiquement le bien
  ou était désigné pour le recevoir. Pour le transporteur extérieur mandaté
  par l'acheteur, examiner la remise au transporteur ; le choix d'une option
  du panier proposée par le vendeur ne suffit pas à caractériser cette exception.
  Une conclusion sur le risque ne décide pas seule de la bonne délivrance,
  d'une faute ou d'une résolution. L216-8 vise aussi les non-professionnels :
  ne pas assimiler cette catégorie au consommateur ou à tout petit professionnel.
- **Délai supplémentaire (L216-6 I).** Vérifier une demande formelle d'effectuer
  la livraison dans un délai raisonnable adapté aux circonstances, son
  contenu, sa réception et l'absence d'exécution à son terme. Une simple
  demande « où est mon colis ? » ne prouve pas que cette étape a eu lieu.
  Aucun nombre standard de jours n'est fixé ici.
- **Résolution (L216-6).** Mettre fin au contrat est une démarche distincte.
  Vérifier les conditions et l'écrit qui l'annonce ; le texte lu retient sa
  réception par le professionnel, sauf exécution entre-temps. Refus de livrer,
  non-livraison manifeste ou date essentielle peuvent appeler la branche II,
  sans délai supplémentaire ; établir la circonstance ou la demande expresse
  avant conclusion et le manquement, sans automaticité.
- **Remboursement (L216-7).** Seulement après résolution dans les conditions
  vérifiées : le passage lu prévoit la totalité des sommes versées, au plus
  tard quatorze jours suivant la date de dénonciation. Sans preuve de la
  résolution et des dates, ne pas annoncer de date butoir. Un remboursement
  non reçu relève de CONSO-019 proposée ; pas de majoration calculée ici.

## Remise contestée : branches à conserver

| Situation | Pièces/questions utiles | Conclusion à réserver |
|---|---|---|
| N02 : tiers de marketplace, pays inconnu, « livré en relais », jamais retiré | Confirmation et facture pour identifier le vendeur/pays ; relais convenu et effectif ; avis de disponibilité, délai contractuel de retrait, possibilité réelle de retirer, preuve de remise à qui et quand. | Ni la responsabilité ni le remboursement ; ne pas assimiler disponibilité, retrait et retour au vendeur. Garder fiche et question ciblée avant lettre consommateur. |
| N04 : devant la porte / chez un voisin | Instructions données ou leur absence, tiers désigné ou non, photos et justificatif de dépôt, lieu et circonstances ; les instructions ne sont pas présumées. | Pas de remise régulière ou irrégulière présumée, pas d'accusation de vol ; demander les justificatifs au vendeur. |
| N05 : signature contestée / relais déplacé | Contrat et relais choisi, information/accord sur changement, accessibilité, preuve de signature et identité/qualité du réceptionnaire ; conserver les pièces contradictoires. | La signature peut être contestée sans désigner un auteur de faux ; le changement de relais ne tranche pas seul l'exécution. |
| N06 : commande pour mariage | Date annoncée, message antérieur à la commande, circonstances de conclusion, réponse du vendeur et manquement à l'engagement. | Date essentielle et résolution immédiate à vérifier ; ne pas imposer mécaniquement un délai supplémentaire ni déclarer la résolution acquise. |
| N07 : transporteur extérieur | Mandat de l'acheteur, choix réellement extérieur à l'offre, preuve de prise en charge, lieu/date de perte alléguée. | Séparer risques, délivrance et recours transport, sans conclure que le vendeur n'a plus aucune obligation. |

## Modèles à adapter, jamais à envoyer automatiquement

Choisir une seule demande cohérente avec le souhait exprimé et le stade
documenté. Les champs manquants restent visibles. Ne pas signer pour la
personne et ne pas inventer de pièce jointe.

### A — Réclamation factuelle, utilisable sans source normative lue

> À [vendeur identifié, coordonnées à vérifier]
>
> Objet : commande [référence] — bien non reçu
>
> Le [date], j'ai commandé [bien]. Selon [confirmation], la livraison était
> annoncée [date/délai, ou « aucune date retrouvée »]. [Paiement selon pièce,
> ou déclaré, montant sans coordonnées bancaires complètes.] À ce jour, je
> déclare ne pas avoir reçu ce bien. [Suivi et contestation attribués ;
> relances datées et réponse éventuelle.]
>
> Je vous demande [de livrer le bien conformément à la commande / de me
> communiquer les justificatifs de la remise alléguée et une solution].
> Merci de me préciser par écrit la situation et la date de livraison proposée.
> [Si la personne souhaite un remboursement sans droit établi : « Je souhaite
> convenir avec vous de l'annulation de la commande et du remboursement de
> [somme payée à confirmer]. Merci de me répondre sur cette demande. »]
>
> Pièces à joindre après relecture : [liste des seules pièces disponibles].
> [Nom à compléter par la personne]

Présenter cette dernière option comme une demande amiable, sans prétendre
que le contrat est déjà résolu ni que le remboursement est acquis.

### B — Demande formelle de livraison après vérification

Reprendre A et remplacer la demande par une demande formelle de livrer dans
un délai supplémentaire raisonnable [durée/date à établir et à faire
confirmer selon les circonstances]. Expliquer à la personne le fondement
effectivement lu et ce qu'il reste à vérifier avant utilisation. Un champ
de délai vide rend le brouillon incomplet. Distinguer ce délai supplémentaire
du délai légal subsidiaire de trente jours. Prévoir de conserver l'écrit
et sa preuve de réception. Ne pas annoncer que cette lettre met déjà fin au contrat.

### C — Fin du contrat et demande de remboursement après vérification

Uniquement si les conditions ordinaires ou la branche immédiate sont établies
après lecture du texte applicable : remplacer la demande par l'annonce claire
de la résolution et la demande de remboursement des sommes versées prouvées,
avec la séquence ou l'exception précise et les pièces. Ne pas demander dans
le même courrier la livraison future et une résolution immédiate. Si les
conditions manquent, garder A et les questions, pas une résolution hypothétique
prête à signer. Suivi d'un remboursement bloqué : orientation CONSO-019 proposée.

Pour la prochaine étape : juriste d'une association de consommateurs pour la
réclamation simple ; avocat si procédure, difficulté de rattachement, délai
possible ou enjeu irréversible. Aucun professionnel ni canal précis n'est
annoncé comme disponible sans vérification. Terminer par la phrase de portée
prescrite dans le skill et la méthode.
