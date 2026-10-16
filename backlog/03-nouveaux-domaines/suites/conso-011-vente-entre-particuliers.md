---
id: CONSO-011
titre: "Préparer une demande dans une vente entre particuliers"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-004]
---

# CONSO-011 — Préparer une demande dans une vente entre particuliers

## Objectif et résultat attendu

Une personne qui a acheté ou vendu un bien à un autre particulier comprend que le droit de la consommation ne s'applique
pas en principe, quels fondements examiner, et obtient un brouillon de
demande au vendeur.

## Périmètre et fichiers

- `consumer-legal/skills/private-sale-dispute/SKILL.md` — le skill (à créer)
- `consumer-legal/references/vente-entre-particuliers.md` — régime civil, rôle des plateformes, sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée

## Pièces et informations nécessaires

Annonce ; échanges ; paiement et intermédiaire ; remise ou envoi ; état du
bien ; profil du vendeur (volume d'annonces, mentions).

## Sortie attendue

Fiche ; fondements civils à vérifier ; règles privées de la plateforme
distinguées du droit ; brouillon ; limites.

## Travail attendu

Un « particulier » vendant en volume reçoit une qualification
conditionnelle de vendeur professionnel, avec retour vers CONSO-001 ou
CONSO-002 si elle est établie. Escroquerie alléguée → DOM-002 ; paiement →
DOM-004.

## Références métier et sources à rechercher

Code civil, vente, délivrance, vices cachés ; obligations d'information des
places de marché sur la qualité du vendeur.

## Critères d'acceptation
- [ ] P01 n'applique pas le Code de la consommation au vendeur particulier.
- [ ] P02 laisse la qualité du vendeur conditionnelle et nomme les indices.
- [ ] P03 à P06 distinguent preuve, fondements civils, qualité et démarche interne ; aucune garantie consommateur ou exclusion de recours automatique.
- [ ] La sortie se termine par une phrase courte nommant le professionnel compétent (avocat ou juriste d’une association selon le besoin), avec renfort en tête en cas de délai, procédure ou enjeu irréversible, selon BASE-013.

## Vérification

- Cas normal : P01 — Console d'occasion différente de l'annonce.
- Cas limite : P02 — Vendeur « particulier » qui publie quarante annonces identiques.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Plainte pénale, procédure judiciaire, médiation de la plateforme exécutée.

## Complément issu des frictions utilisateur — 16 octobre 2026

Points 95, 99–107, 109, 113–115 de la [matrice des besoins](../dom-001-frictions-utilisateurs.md).
Ces exigences complètent le périmètre ; elles ne valident aucune règle du guide.

Inclure les deux positions : acheteur ou vendeur particulier, sans les confondre avec la TPE de CONSO-012. La sortie comporte annonce, délivrance, paiement allégué ou reçu, photos, état, numéros de série et messages ; pour le vendeur, contestation d’un retour ou colis déclaré vide sans qualifier l’acheteur de fraudeur. La protection contractuelle de plateforme va à CONSO-018 ; la demande civile entre parties reste ici.

Examiner défaut caché, apparent, antérieur et suffisamment grave, description trompeuse alléguée et clause d’exclusion ; demander expertise adaptée avant réparation susceptible d’effacer les indices. Dater découverte et vente ; rechercher prescription et plafond applicables sans durée constante. Préparer aussi une checklist de preuve avant expédition d’un objet coûteux, sans imposer une assurance universelle. Des indices de vente habituelle réouvrent la qualité professionnelle (CONSO-004), sans l’établir par un seuil inventé.

- Cas limite : P03 — Vice allégué avec clause « en l’état » et messages montrant une connaissance possible : qualification ouverte et pièces d’expertise.
- Cas limite : P04 — Vendeur recevant un autre appareil : fiche civile et relais CONSO-018 pour protection, aucune intention imputée.
- Cas limite : P05 — Capture de virement puis objet remis sans crédit constaté : distinguer paiement prouvé, litige civil et fraude alléguée.
- Cas limite : P06 — Défaut visible sur les photos mais découvert après paiement : ne pas le qualifier automatiquement de vice caché.

Scénarios complémentaires **attendus, non exécutés**. Les sources précises et
leurs versions restent à rechercher selon BASE-005 avant toute règle affirmée.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
