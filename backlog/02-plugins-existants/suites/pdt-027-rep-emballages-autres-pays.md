---
id: PDT-027
titre: "Cartographier la REP emballages d'une vente directe dans un autre pays"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-004, PILOTE-003, BASE-005, BASE-006, PDT-020]
---

# PDT-027 — Cartographier la REP emballages d'une vente directe dans un autre pays

## Objectif et résultat attendu

Une entreprise française vend et expédie ses produits directement à des
clients d'autres États membres, voire de pays tiers. Le résultat est une
fiche pays × flux : l'entreprise est-elle « producteur » d'emballages dans
ce pays, doit-elle s'inscrire au registre national des producteurs, désigner
un mandataire REP, adhérer à un organisme et déclarer, ou ces obligations
reposent-elles sur un client ou une plateforme ; avec les pièces à réunir et
les inconnues.

## Origine

Remarque de l'utilisateur du 19 octobre 2026 sur la REP emballages et le PPWR,
dans le contexte de ventes de couteaux à l'étranger (DOU-017). PDT-020 qualifie
le rôle REP, sans traiter l'inscription et le mandataire dans chaque autre
État membre.

## Périmètre et fichiers à examiner

Propriétaire : `product-legal` ; identifiant `judge-fr-eu-product-legal`.

- `product-legal/skills/rep-emballages-pays/SKILL.md` : skill à créer lors du lot.
- `product-legal/references/rep-emballages-pays.md` : méthode et modèle de sortie (à créer).
- `product-legal/references/rep-emballages-pays/<pays>.md` : fiche par pays effectivement recherché, datée (à créer).

Première tranche proposée : Allemagne, Belgique, Espagne et Italie si
l'entreprise y vend, puis les pays effectivement concernés. Les pays tiers
(Canada et ses provinces, Australie…) sont traités en mode « recherche à
faire » tant qu'aucune fiche n'est livrée.

## Entrées nécessaires

Pays de livraison, canal (site propre, plateforme, revendeur local), qualité
des clients (utilisateurs finaux ou professionnels), types d'emballages
(vente, expédition, calage), poids par matériau et volumes par pays,
inscriptions et contrats existants, mandataire éventuel.

## Travail attendu

- Appliquer la définition du producteur (règlement (UE) 2025/40, article 3,
  point 15, en particulier les points c et d pour une mise à disposition
  directe aux utilisateurs finaux d'un autre État membre), l'article 44
  (registre des producteurs et date d'ouverture des registres nationaux) et
  l'article 45 (REP, mandataire REP par écrit dans chaque autre État membre).
- Vérifier la période transitoire : régimes nationaux encore issus de la
  directive 94/62/CE et date effective des nouveaux registres.
- Pour chaque pays de la tranche, lire la loi nationale et l'autorité du
  registre ; séparer obligation légale, offre d'un organisme et exigence d'une
  plateforme.
- Signaler les doublons possibles avec la déclaration française (PDT-028).

Appliquer BASE-013 et BASE-014 (date de relecture par fiche pays).

## Sources à rechercher

Règlement (UE) 2025/40 consolidé et actes d'exécution relatifs aux registres ;
directive 2008/98/CE, articles 8 et 8 bis ; lois nationales sur les
emballages des pays de la tranche ; pour les pays tiers, textes officiels
provinciaux ou nationaux.

Lu le 19 octobre 2026 lors du découpage, via `scripts/legal_sources.py eu
32025R0040` (statut documentaire non vérifié) : article 3, point 15 ; article
44, paragraphes 1 et 2 ; article 45, paragraphes 1 à 3.

## Critères d'acceptation

- [ ] Une vente en ligne à des particuliers allemands produit la qualification de producteur, l'inscription et le mandataire à vérifier, reliés aux sources lues.
- [ ] Une vente B2B à un distributeur local identifie qui met l'emballage à disposition pour la première fois, sans présumer que l'obligation repose sur l'entreprise.
- [ ] Un pays sans fiche produit les questions et sources à ouvrir, sans obligation présumée.
- [ ] La sortie se termine par la phrase BASE-013 (organisme ou mandataire REP du pays, juriste en droit de l'environnement).
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 et BASE-014 consignée.

## Scénarios de contrôle

- Cas normal : vente directe à des particuliers en Allemagne et en Espagne.
- Cas limite : vente via une plateforme qui annonce gérer la REP.
- Cas complémentaire : vente à des particuliers au Canada : mode recherche.
- Information manquante : poids par matériau inconnus.
- Sans source : loi nationale non lue ; aucune obligation présumée.

Scénarios attendus, non exécutés. La relecture humaine est prise en charge par
l'utilisateur selon CLAUDE.md.

## Hors périmètre

Inscription, adhésion ou déclaration effectives, calcul des contributions,
REP d'autres filières que les emballages, déclaration française (PDT-021).
