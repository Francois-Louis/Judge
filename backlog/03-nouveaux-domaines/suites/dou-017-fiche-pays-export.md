---
id: DOU-017
titre: "Établir la fiche pays d'une vente de produits vers un pays tiers"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-009, PILOTE-003, BASE-005, BASE-006, BASE-008, DOU-001, DOU-005]
---

# DOU-017 — Établir la fiche pays d'une vente de produits vers un pays tiers

## Objectif et résultat attendu

Un vendeur français demande « que dois-je faire pour vendre mes produits dans
tel pays ? ». Le résultat est une fiche pays unique, datée, qui répond dans
l'ordre utile : peut-on y vendre ce produit (DOU-014, DOU-015), quelles
formalités de sortie de l'Union (DOU-005, DOU-013), qui importe et qui paie
droits et taxes à l'arrivée selon le contrat (DAP, DDP), le vendeur doit-il
s'enregistrer à l'étranger pour une taxe à la consommation, existe-t-il une
préférence d'origine (DOU-016), quelles conditions de transporteur, et quels
documents accompagnent l'envoi. Les volets dont la tâche n'est pas livrée
restent des questions explicites, sans réponse de mémoire.

## Origine

Demande de l'utilisateur du 19 octobre 2026 : « je dois faire quoi si je veux
vendre des couteaux aux USA, Canada, Australie, Tunisie, Brésil, Mexique,
Chili, Afrique du Sud, Cambodge… ». Reprend K05 et les points 35 à 39 et 53 de
la [matrice des frictions](../dom-009-annexes/dom-009-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `customs-legal`. Fichiers futurs :
`customs-legal/skills/destination-market-file/SKILL.md` et
`customs-legal/references/fiche-pays-export.md` (méthode et modèle), réutilisant
les fiches pays de DOU-014 lorsqu'elles existent. Contrat commun DOM-009.

Une fiche porte sur un pays, un produit ou une famille de produits et un canal
(B2B à un importateur, B2C en ligne, plateforme). Plusieurs pays donnent
plusieurs fiches et un tableau de synthèse, sans fusion des règles.

## Pièces et informations nécessaires

Produit et fiche technique, classement envisagé, pays et région de livraison,
canal et qualité de l'acheteur, volume annuel estimé vers ce pays, Incoterm ou
conditions de vente, transporteur, existence d'un importateur ou d'un
représentant local, numéros EORI et statut TVA (sans demander de secret).

## Sortie attendue

Synthèse en tête : « vendable / à vérifier / bloquant » par volet avec la
raison. Puis volets : admissibilité, sortie UE, droits et taxes à destination
(qui est redevable selon le contrat ; aucun taux sans source datée),
enregistrement éventuel du vendeur étranger (par exemple régime de la TVA ou
GST sur les biens de faible valeur), origine préférentielle, transporteur,
documents (facture commerciale, liste de colisage, preuve d'origine, permis).
Questions à poser au transporteur, à l'importateur ou au courtier local.
Signalement des régimes instables (droits de douane américains modifiés en
2025-2026, statut des exemptions de faible valeur) avec date de lecture.

## Travail attendu

- Définir le modèle de fiche et la synthèse multi-pays.
- Pour chaque pays de la tranche, ouvrir les sources officielles du pays sur
  les droits et taxes à l'importation et sur l'enregistrement des vendeurs
  étrangers. Pistes non vérifiées relevées le 19 octobre 2026 : régime
  australien de GST sur les biens de faible valeur (seuil de valeur et seuil
  de chiffre d'affaires du vendeur) ; suspension américaine de l'exemption de
  faible valeur depuis août 2025 et régime tarifaire applicable aux biens de
  l'Union après la décision de la Cour suprême du 20 février 2026.
- Signaler les obligations de responsabilité élargie du producteur pour les
  emballages dans le pays de destination et renvoyer leur qualification à
  PDT-027 (`product-legal`), sans les traiter dans cette fiche.
- Séparer contrat (V03), fiscalité française de l'export (V04), formalités
  douanières UE et droit du pays de destination.
- Ne présenter aucun taux, seuil ou régime étranger sans source officielle
  lue et datée ; une page de transporteur ou de prestataire est une piste.

Méthode BASE-005 locale, BASE-013 et BASE-014.

## Critères d'acceptation

- [ ] Une demande multi-pays produit une fiche par pays et une synthèse, sans règle commune inventée.
- [ ] Le volet droits et taxes distingue redevable légal et partie qui supporte le coût selon DAP ou DDP.
- [ ] Un volet dont la tâche n'est pas livrée reste une question explicite avec sources à ouvrir.
- [ ] Les régimes instables portent leur date de lecture et un avertissement de mise à jour.
- [ ] La sortie se termine par la phrase BASE-013 (commissionnaire en douane, courtier ou avocat du pays, expert-comptable pour la TVA).
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 consignée.

## Vérification

- Cas normal : couteaux de cuisine vendus en ligne à des particuliers australiens.
- Cas limite : vente DDP aux États-Unis : redevable et coût supporté distingués, régime tarifaire daté.
- Cas complémentaire : vente B2B à un importateur tunisien : préférence et documents.
- Multi-pays : neuf pays demandés en une fois : fiches séparées et synthèse.
- Information manquante : canal inconnu ; question ciblée.
- Sans source : taxe du pays non lue ; volet réservé.
- Héritage américain : guide « international shipping » américain fourni ; non transposé.

Scénarios **attendus, non exécutés**. La relecture humaine est prise en charge
par l'utilisateur selon CLAUDE.md.

## Hors périmètre

Enregistrement fiscal effectif à l'étranger, déclaration ou paiement de taxes
étrangères, rédaction des CGV export (V03), contentieux à destination,
études de marché et prix.
