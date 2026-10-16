# DOM-001 — Vérification documentaire du cadrage

Relecture du **16 octobre 2026** par l'agent de maintenance : suivre des
pièces inventées dans le [découpage](dom-001-decoupage-consommation.md) et
les 13 propositions CONSO, pour vérifier le routage et les informations à
demander. La story interdit de résoudre ces consultations : aucun délai,
montant ou droit n'est conclu. Le [relevé machine](dom-001-resultats.json)
consigne séparément les contrôles statiques.

## Dossier fictif N — commande en ligne jamais livrée

- `N-commande` : casque audio commandé le 2 septembre 2026 sur un site en
  français ; page produit « livraison sous 5 jours ouvrés ».
- `N-suivi` : « livré en point relais » le 8 septembre ; la personne n'a
  rien retiré et le point relais dit ne rien avoir.
- `N-paiement` : carte débitée le jour de la commande.
- `N-echanges` : deux messages au service client, sans réponse.
- Mentions légales du site non fournies ; la confirmation porte un nom
  commercial sans pays. La personne demande aussi : « je fais opposition ? ».

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `consumer-legal`, CONSO-001 : achat à distance d'un bien pour un usage privé, non reçu. | Vendeur professionnel et pays à établir depuis les mentions légales ou la facture. |
| Plateforme | La confirmation désigne le cocontractant ; s'il s'agit d'un vendeur tiers, la plateforme n'est pas présumée vendeuse. | Facture et page vendeur. |
| Statut « livré » | Fait contesté noté comme tel ; questions au point relais et au vendeur sur la preuve de remise. | Qui supporte le risque du transport : piste L216-1 et suivants à lire, aucune conclusion. |
| Délai | « 5 jours ouvrés » est un engagement déclaré par la page, conservé avec sa capture. | Aucun délai légal affirmé ; date de départ à prouver. |
| Paiement | Opposition ou contestation : DOM-004, tâche distincte. Le brouillon au vendeur ne promet pas de remboursement bancaire. | Moyen et date du débit. |
| Suite | Brouillon de réclamation, puis médiation (CONSO-006) si la réponse ne règle pas le litige. | Médiateur indiqué par le vendeur. |

**Constat :** CONSO-001 suffit à produire fiche, pièces manquantes et
brouillon. Le volet bancaire est identifié sans être absorbé. La relecture
ne décide pas qui doit rembourser.

## Dossier fictif G — produit défectueux et garantie commerciale invoquée

- `G-facture` : machine à café achetée en magasin il y a quatorze mois.
- `G-garantie` : « garantie constructeur 1 an » et extension « Sérénité+ »
  de deux ans achetée en caisse ; le document de l'extension nomme une
  société sans préciser si c'est un assureur.
- `G-reponse` : le magasin répond « garantie expirée, voyez avec Sérénité+ ».
- `G-defaut` : la machine fuit sous l'appareil depuis une semaine.

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Domaine et tâche | `consumer-legal`, CONSO-002 : défaut d'un bien acheté à un professionnel. | Date de délivrance prouvée, description du défaut, photos. |
| Sécurité | Une fuite d'eau sur un appareil électrique est posée en premier : arrêt de l'usage, question de danger avant la demande ordinaire. | Aucun danger ni absence de danger affirmé. |
| Garanties | Légale de conformité, vices cachés et garantie commerciale présentées comme régimes distincts. « Garantie expirée » ne vise que la garantie constructeur. | Durées et conditions à lire à la date d'achat ; aucune affirmée. |
| Extension | CONSO-005 lit le document. S'il nomme un assureur, le refus éventuel relève de DOM-005, question distincte. | Identité et qualité du garant. |
| Demande | Brouillon au magasin, sans suivre le renvoi vers l'extension. | Réponse du vendeur. |

**Constat :** le découpage distingue la garantie due par le vendeur de la
garantie commerciale et de l'assurance. Il ne dit pas si la demande aboutira.

## Dossier fictif P — achat professionnel présenté comme achat de consommateur

- `P-facture` : ordinateur portable commandé en ligne, facturé à une SARL de
  coiffure, TVA mentionnée.
- `P-recit` : la gérante « l'utilise aussi chez elle » et demande la
  rétractation « comme tout le monde ».
- Variante `P-inverse` : un particulier achète une perceuse pour son
  domicile ; les CGV du vendeur le déclarent « acheteur professionnel ».

| Point relu | Résultat du parcours | Reste à obtenir ou réservé |
|---|---|---|
| Qualité | CONSO-004 ou la qualification de CONSO-001 : achat au nom de la société pour son activité → orientation vers commercial (EXIST-001/COM). Pas de brouillon de rétractation « consommateur ». | Usage réel, rapport avec l'activité principale, effectif. |
| Protection particulière | Canal à distance ou hors établissement noté ; piste L221-3 à lire avant d'accorder ou d'écarter une protection. Usage mixte laissé conditionnel. | Texte et version à la date d'achat. |
| Variante inverse | L'étiquette posée par les CGV ne décide pas : les faits d'achat privé priment pour la qualification, à confirmer par la source. | Pièces de l'usage privé. |

**Constat :** le statut affirmé par l'une ou l'autre partie ne fixe pas le
domaine. Les questions qui tranchent sont nommées, sans conclusion.

## Cas limites

| Cas fictif | Routage retenu |
|---|---|
| Colis retenu en douane, droits réclamés | DOM-009 pour l'acte ; la demande au vendeur sur les frais annoncés reste chez CONSO-001. |
| Vendeur hors UE sur une place de marché | CONSO-001 puis CONSO-007 : limites explicites, aucun recours promis. |
| Console achetée à un particulier | CONSO-011, Code civil seulement. |
| Faux site, aucun vendeur identifiable | Banque (DOM-004) et pénal (DOM-002) en tâches distinctes ; aucune réclamation à un vendeur inexistant. |
| Box internet, régularisation d'électricité, devis de rénovation | DOM-022, DOM-021, DOM-015 : orientation seule, même si le plugin du secteur n'est pas disponible. Règle modifiée le 16 octobre 2026 : sans plugin du secteur, réclamation sur les règles générales (CONSO-014). |
| Trottinette dont la batterie a brûlé un tapis | Danger d'abord ; dommage → DOM-035 ; défaut du bien → CONSO-002. |
| Vol annulé acheté sur un comparateur | DOM-008. |
| Relance d'une société de recouvrement | DOM-003 ou DOM-024 : le modèle « consumer » de la clinique, centré sur le recouvrement américain, n'est pas repris. |
| Demande d'envoyer la réclamation au vendeur | Brouillon seulement ; aucun envoi. |

## Couverture des critères de la story

| Critère DOM-001 | Où il est traité |
|---|---|
| Plugin propre et frontières | Découpage, sections plugin et frontières ; ligne mise à jour dans la matrice BASE-003. |
| Tâches hiérarchisées, premier skill borné | Rangs 1 à 4 ; inclus et exclus de CONSO-001. |
| Références, pièces, sortie, scénarios par story | Sections dédiées des 13 propositions, contrôlées par le relevé. |
| Installation seule, pas d'agent ni connecteur par principe | Contrat d'installation du découpage. |
| Implémentations non lancées | Aucun fichier sous `consumer-legal/` ; marketplace inchangé. |

## Portée

Cadrage du checkout et relecture par le seul agent de maintenance, sur
pièces entièrement fictives ; contrôles statiques uniquement. Aucune source
juridique lue : les articles cités sont des pistes de recherche, pas des
règles vérifiées. Aucun délai ni montant établi, aucun skill créé ou exécuté,
aucun paquet installé, aucun lecteur réel ou indépendant, aucun envoi. Le
préalable PILOTE-003 est satisfait après BASE-011 ; aucune tranche n'est
sélectionnée par ce cadrage.
