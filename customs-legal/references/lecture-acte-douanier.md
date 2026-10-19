# Lire un contrôle ou un avis douanier déjà notifié

Version `1.0.0` — 19 octobre 2026 (Europe/Paris), DOU-009.
Méthode métier, repères datés et modèle de sortie pour une personne qui a
reçu un document de la douane ou présenté comme tel : identifier sa nature,
son auteur et son stade, séparer ce qu'il demande, et préparer les pièces et
questions urgentes. Cette lecture ne rédige ni observations, ni contestation,
ni recours, ni défense ; elle ne calcule ni dette, ni pénalité, ni délai.

## Périmètre de la tâche

**Inclus** : un document déterminé, reçu par la personne ou son entreprise,
émanant ou se réclamant de l'administration des douanes française (bureau,
service, comptable public des douanes) : demande de pièces, communication des
motifs ou proposition de taxation, décision, avis de mise en recouvrement
(AMR), mise en demeure ou acte de poursuite du comptable, procès-verbal,
saisie ou retenue de marchandises, convocation, proposition de transaction.
Résultat : identité et stade de l'acte avec réserves, chronologie, tableau
des objets, mentions d'échéance reproduites, pièces et questions.

**Exclus** : rédaction d'observations, de contestation, de recours, de
demande de sursis, de remboursement ou de remise ; défense pénale ;
signature, acceptation ou refus d'une transaction ou d'une destruction ;
calcul de prescription, d'échéance, de droits ou de pénalités ; paiement et
déclaration. Un message de transporteur ou de prestataire sans acte de la
douane relève de la préparation de l'envoi (`import-document-checklist`).

## Ce qu'il faut séparer

| Objet | Ce qui est établi par les repères lus | Ce qui reste à vérifier sur l'acte |
|---|---|---|
| Contrôle / décision | Les autorités douanières peuvent exercer tout contrôle, y compris après la mainlevée, sur la déclaration, les documents, la comptabilité et les marchandises (U1, art. 46 et 48 ; F1, L. 421-1 droit de communication). Un contrôle n'est pas en soi une décision sur la dette. | Le document demande-t-il des pièces, annonce-t-il des constatations, ou décide-t-il ? Quelles opérations, déclarations et période sont visées ? |
| Communication des motifs / proposition de taxation | Avant une décision défavorable, la douane communique ses motifs et la personne peut exprimer son point de vue dans un délai courant de la réception, sauf exceptions (U1, art. 22 § 6 ; art. 29 pour les décisions sans demande) ; délai fixé à 30 jours, 24 heures possible pour certaines marchandises non déclarées (U2, art. 8). Pour les droits dont le fait générateur est l'importation ou l'exportation, l'échange contradictoire suit le CDU ; sinon, proposition écrite et 30 jours à compter de sa réception (F1, L. 311-1, L. 311-3, L. 311-7, L. 311-8). | Intitulé exact (projet, communication des motifs, proposition) ; date de réception et preuve ; annexes et pièces communiquées ; délai indiqué par l'acte. Les observations sont une tâche distincte, non livrée. |
| Décision et dette douanière | Une décision défavorable est motivée et mentionne le droit de recours (U1, art. 22 § 7). La dette est notifiée au débiteur ; elle ne peut l'être après trois ans à compter de sa naissance, sauf cas prévus (U1, art. 102-103) ; montant à acquitter dans le délai fixé, en principe dix jours au plus, avec suspensions prévues (U1, art. 108). Tout recours est ouvert contre une décision qui concerne la personne ; il n'est pas suspensif, sauf sursis accordé, en principe contre garantie (U1, art. 44-45). | Nature (décision, notification de dette, simple information), auteur et service, date, motifs, mention des voies de recours, montants par poste, base. Aucun montant dû confirmé ni prescription calculée. |
| Avis de mise en recouvrement (AMR) | Notifié lorsque des créances n'ont pas été payées à leur exigibilité ; il indique fait générateur, nature, montant et éléments de liquidation (F1, L. 323-6 ; F2, R. 323-2, D. 323-3). Les recours ne suspendent pas son exécution (F1, L. 323-7). Contestation de la créance adressée à l'autorité émettrice dans un délai de trois ans suivant la notification de l'AMR, sous réserve des délais du CDU en matière de remise ; l'autorité statue dans les six mois de la réception ; tribunal judiciaire dans les deux mois suivant la réponse ou l'expiration de ces six mois ; paiement différé seulement sur demande et avec garanties (F1, L. 331-1 à L. 331-3, L. 332-1, L. 332-2, L. 332-5 ; F2, R. 331-1, R. 331-2). Un délai long de contestation n'enlève pas l'urgence : exigibilité, poursuites et garanties suivent leur propre calendrier. | Intitulé « avis de mise en recouvrement », émetteur, date de notification et preuve, fait générateur, postes, éléments de liquidation, paiements déjà faits. La contestation et le sursis sont des tâches distinctes, non livrées. |
| Poursuites du comptable et garanties | Contestation des actes de poursuite ou des décisions d'affectation adressée au comptable dans les deux mois de leur notification, puis juge de l'exécution dans les deux mois de sa réponse ou de son silence (F1, L. 331-7) ; décisions sur les garanties contestables en référé dans les quinze jours (F1, L. 332-3) ; les agents peuvent exercer les compétences des commissaires de justice (F1, L. 323-1). | Mise en demeure, saisie administrative à tiers détenteur, décision sur garanties : date de notification, auteur, montant, mesures en cours. Urgence et avocat ; exécution forcée : domaine voisin. |
| Procès-verbal, infraction et transaction | Le procès-verbal de constatation ou de saisie contient des mentions obligatoires, dont la lecture et la demande de signature si la personne est présente (F1, L. 443-3) ; établi par deux agents, il fait foi jusqu'à inscription de faux des constatations matérielles, et jusqu'à preuve contraire des déclarations rapportées (F1, L. 444-1). La transaction est accordée sur demande de l'auteur d'une infraction, sous conditions d'autorisation (F1, L. 613-1, L. 613-2). Les sanctions sont prévues par l'État membre (U1, art. 42). | Titre et objet du document, faits reprochés, déclarations attribuées, signature demandée ou faite, proposition de transaction et ses termes. Une dette n'implique pas une infraction ; une sanction n'est pas un simple supplément de droits. Avocat en droit douanier avant tout engagement. |
| Marchandises consignées, saisies ou retenues | Consignation pour vérification (F1, L. 441-1) ; saisie des objets passibles de confiscation lors d'une infraction (F1, L. 442-1) ; mesures sur les marchandises, y compris confiscation, vente ou destruction, dans les cas du CDU (U1, art. 198). Retenue pour atteinte présumée à un droit de propriété intellectuelle : notification au déclarant ou détenteur, délais courts en jours ouvrables, et silence pouvant valoir accord à la destruction (U3, art. 17 et 23). | Fondement indiqué (vérification, infraction, propriété intellectuelle, prohibition), inventaire, lieu, gardien, réponse attendue et son délai tel qu'écrit. Ne rien accepter ni refuser sans examen ; propriété intellectuelle : avocat sans attendre. |
| Mesure visant une personne | Retenue douanière seulement en cas de délit douanier flagrant puni d'emprisonnement ; droit à l'assistance d'un avocat dans les conditions du code de procédure pénale (F1, L. 432-1, L. 432-5) ; audition libre après notification des informations prévues (F1, L. 433-1) ; retenue provisoire pour mise à disposition d'un officier de police judiciaire (F1, L. 431-1). | Convocation, statut annoncé (audition libre, retenue), date et lieu. Avocat en premier, volet pénal à coordonner ; aucune stratégie de défense ici. |
| Frais privés | Les sommes facturées par un transporteur, un prestataire de dédouanement ou un entrepôt ne sont pas des actes de la douane (voir la [qualification commune](qualification-douanes.md)). | Intitulé et auteur de chaque somme ; à séparer ligne par ligne des droits, taxes et pénalités. |

## Échéances : reproduire, jamais calculer

1. Recopier chaque mention de délai **telle qu'elle figure dans l'acte**,
   avec la page et la phrase : « l'acte indique : … ». La signaler comme
   mention de l'acte, non comme délai vérifié.
2. Séparer date imprimée, date d'envoi, date de remise ou de première
   présentation, date de réception déclarée et date de découverte. Plusieurs
   textes lus font partir le délai de la **réception** ou de la
   **notification**, pas de la date imprimée : demander la preuve (avis de
   réception, enveloppe, horodatage électronique).
3. Ne calculer aucune date de fin et ne compter ni jours écoulés ni jours
   restants ; ne dire ni « il vous reste », ni « c'est trop tard ». Un repère
   lu ci-dessus peut être cité avec sa source comme durée prévue par un texte
   pour ce type d'acte et son point de départ légal ; il ne fixe pas
   l'échéance du dossier tant que nature, notification et version ne sont
   pas établies. Ne pas présenter comme court un délai que le repère donne
   long ; l'urgence peut venir d'ailleurs (paiement non suspendu, poursuites,
   garanties, destruction, audition).
4. Acte sans mention de délai ou incomplet : ne pas en déduire l'absence de
   délai ; demander les pages manquantes et le faire examiner rapidement.
5. Rétention de marchandises pour propriété intellectuelle, décision sur les
   garanties, convocation ou retenue d'une personne : **urgence immédiate en
   tête**, avant toute fiche.

## Pièces et questions selon le cas

Demander seulement ce qui fait avancer, données superflues masquées :

1. L'acte intégral, toutes pages et annexes, recto verso ; références
   (dossier, déclaration ou MRN, AMR, procès-verbal), sans identifiant de
   connexion ni signature à recopier.
2. Preuve et mode de réception : avis de réception, enveloppe, remise en main
   propre, messagerie ou espace en ligne avec horodatage.
3. Déclaration en douane et justificatifs visés (facture, transport, origine)
   seulement s'ils sont cités par l'acte.
4. Montants par poste tels qu'écrits (droits, TVA, autres taxes, intérêts,
   amendes, frais) et paiements déjà faits avec leur preuve.
5. Échanges antérieurs : demande de pièces, réponses, observations, PV
   signés, propositions reçues.
6. Suite annoncée par l'acte : date de rendez-vous, mesure prévue, destruction
   ou vente annoncée, demande de garantie.

Questions types, à adapter au destinataire réel :

- Au service émetteur, par ses coordonnées officielles vérifiées : « Pouvez-
  vous me confirmer la nature de ce document (demande d'information,
  communication des motifs, décision, avis de mise en recouvrement) et me
  transmettre les annexes et pièces sur lesquelles il s'appuie ? »
- « À quelle date votre service considère-t-il ce document comme reçu, et
  par quel moyen ? » ; « Quelles opérations et quelle période sont visées ? »
- Au représentant en douane ou au transporteur qui a déclaré : « Avez-vous
  reçu un document de la douane pour cette déclaration, et quelles pièces lui
  avez-vous transmises ? »
- À un avocat en droit douanier : « Quelle est la nature exacte de cet acte,
  quelle voie et quel délai s'appliquent, et faut-il agir avant telle étape
  annoncée ? »

## Interlocuteurs et orientations

La douane renseigne sur son dossier ; elle n'est pas le conseil de la
personne. Le représentant en douane agit pour son mandant dans les limites
de son mandat. Avocat en droit douanier dès qu'un acte décide, recouvre,
constate une infraction, saisit, retient ou propose une transaction ; en
premier si une personne est convoquée ou retenue, ou si une destruction est
annoncée. Les tâches suivantes sont **proposées, non livrées** : observations
avant décision, contestation d'une créance, sursis et garanties, remboursement
(DOU-010), remise (DOU-011), lecture du droit de propriété intellectuelle
invoqué. Recouvrement forcé et pénal : domaines voisins distincts, après
qualification de l'acte. Ne jamais présenter une tâche proposée comme une
commande disponible.

## Acte d'une autre administration ou d'un autre État

Le recours contre une décision douanière s'exerce dans l'État membre où elle
a été prise (U1, art. 44 § 3). Un acte d'une douane d'un autre État membre,
d'un pays tiers ou d'une administration fiscale française relève d'un autre
régime : le noter, ne pas y appliquer le Code des douanes français et
orienter vers un conseil compétent dans ce pays ou cette matière. Ni la
langue, ni la monnaie, ni l'adresse du document ne fixent seules le régime
ou le juge.

## Modèle de sortie

1. **Maintenant** : urgence éventuelle en tête, deux ou trois actions
   concrètes sans délai calculé (obtenir l'acte complet, vérifier l'émetteur
   par ses coordonnées officielles, faire examiner par un avocat en droit
   douanier si l'acte décide, recouvre, sanctionne, saisit ou vise une personne).
2. **Identité de l'acte** : auteur et service, intitulé, référence, date,
   destinataire ; nature probable et indices ; stade (contrôle, avant
   décision, décision, recouvrement, poursuite, infraction) ; réserves.
3. **Chronologie** : dates séparées (imprimée, envoi, réception, échanges,
   étapes annoncées), avec la pièce qui établit chacune.
4. **Tableau des objets** : contrôle / formalités / dette / sanction / frais
   privés, avec pour chaque ligne la mention lue, la pièce et ce qui reste à
   vérifier.
5. **Mentions d'échéance** : reproduites telles quelles, avec ce qui doit être
   vérifié ; aucune date de fin.
6. **Pièces** reçues, manquantes et à confirmer, avec la raison.
7. **Questions** par destinataire (service émetteur, déclarant ou
   représentant, avocat), prêtes à copier.
8. **Sources et limites** : repères utilisés avec date de lecture, réserves ;
   aucun calcul, aucune réponse au fond ; puis la phrase finale :
   « Cette lecture aide à comprendre l'acte reçu et à préparer les questions ;
   elle ne remplace pas l'avis d'un avocat en droit douanier. »

## Sources et relecture de maintenance

Textes lus le **19 octobre 2026**. Le Code des douanes français a été
recodifié par l'ordonnance n° 2026-265 et le décret n° 2026-266 du 8 avril
2026, en vigueur le 1er mai 2026 ; ses articles ont été lus dans leur
publication au Journal officiel du 11 avril 2026 (fonds JORF de la DILA),
sans version consolidée postérieure. Un projet de loi de ratification
déposé au Sénat le 1er juillet 2026 annonce des corrections ; à la page lue,
aucun vote ni promulgation n'apparaît. Les consolidations de l'Union sont des
outils de documentation ; seules les publications au Journal officiel font
foi. Les numéros d'articles nationaux antérieurs au 1er mai 2026 ne sont pas
repris : pour un acte antérieur, la version applicable est à rechercher.

| Repère et source officielle | Lecture, version et portée | Relecture |
|---|---|---|
| U1 — [Code des douanes de l'Union, règl. (UE) n° 952/2013, consolidé au 12.12.2022](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02013R0952-20221212) | Art. 22, 29, 42-46, 48, 101-103, 108 et 198 lus. Dernière consolidation listée lors de la lecture DOU-001 ; réforme ultérieure à rechercher à la date des faits. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · lecture complémentaire de la tâche |
| U2 — [Règl. délégué (UE) 2015/2446, consolidé au 01.07.2026](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:02015R2446-20260701) | Art. 8 à 10 (délai et exceptions du droit d'être entendu) lus. EUR-Lex par défi et script borné à 8 Mio en échec ; reproduction CELLAR complète (29,6 Mo) lue par téléchargement direct. | 2026-10-19 · inchangee · CELLAR, téléchargement direct · lecture limitée aux art. 8-10 |
| U3 — [Règl. (UE) n° 608/2013, protection des droits de propriété intellectuelle par les autorités douanières](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32013R0608) | Art. 17 et 23 lus dans le texte initial ; consolidations éventuelles non recherchées. Sert à reconnaître une retenue et son urgence, pas à traiter le droit invoqué. | 2026-10-19 · inchangee · legal_sources.py eu, CELLAR · texte initial, versions à vérifier |
| F1 — [Code des douanes, partie législative, annexe à l'ordonnance n° 2026-265 du 8 avril 2026 (JORFTEXT000053791010), archive JORF du 11 avril 2026](https://echanges.dila.gouv.fr/OPENDATA/JORF/JORF_20260411-003912.tar.gz) | L. 311-1 à L. 311-9, L. 322-1, L. 322-2, L. 323-1, L. 323-6 à L. 323-8, L. 331-1 à L. 331-8, L. 332-1 à L. 332-5, L. 421-1, L. 431-1, L. 432-1, L. 432-5, L. 433-1, L. 441-1, L. 442-1, L. 442-2, L. 443-3, L. 444-1, L. 444-6, L. 611-1, L. 613-1 à L. 613-4 et art. 11 de l'ordonnance (entrée en vigueur au 1er mai 2026) lus. Version publiée, non consolidée. | 2026-10-19 · inchangee · DILA JORF, archive lue hors outil · réserve : ratification et corrections annoncées à suivre |
| F2 — [Code des douanes, partie réglementaire, annexe au décret n° 2026-266 du 8 avril 2026 (JORFTEXT000053793585), même archive](https://echanges.dila.gouv.fr/OPENDATA/JORF/JORF_20260411-003912.tar.gz) | R. 323-2, D. 323-3, R. 331-1 et R. 331-2 lus ; entrée en vigueur le 1er mai 2026. Le texte publié de R. 331-1 se lit « l'autorité compétente et le directeur régional des douanes » : désignation à confirmer. | 2026-10-19 · inchangee · DILA JORF, archive lue hors outil · réserve : version consolidée non lue |
| G1 — [Sénat, projet de loi n° 836 (2025-2026) ratifiant l'ordonnance n° 2026-265](https://www.senat.fr/leg/pjl25-836.html) | Dépôt du 1er juillet 2026, procédure accélérée, renvoi en commission des finances ; aucun vote affiché (page mise à jour le 2 juillet 2026). | 2026-10-19 · inchangee · outil web · réserve : état de la procédure à revérifier |

Pendant une réponse, relire les sources utiles si un outil de lecture existe
et vérifier la version à la date de l'acte. Sans lecture possible, citer les
repères ci-dessus avec leur date de maintenance et leur limite (méthode,
section 10.6), et garder la lecture factuelle complète : aucune règle de
mémoire, aucun délai, montant, pénalité ou prescription appliqué au dossier.
