---
id: VEH-004
titre: "Documenter un défaut après l'achat d'un véhicule auprès d'un professionnel"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-023, PILOTE-003, BASE-005, BASE-006, BASE-008, VEH-001]
---

# VEH-004 — Documenter un défaut après l'achat d'un véhicule auprès d'un professionnel

## Objectif et résultat attendu

Un acheteur particulier dont le véhicule neuf ou d'occasion acheté à un
professionnel présente un défaut après livraison sait quelles garanties examiner, lesquelles
dépendent de quelle pièce, ce qui reste à établir, et obtient un brouillon
de demande au vendeur.

## Périmètre et fichiers

Plugin principal : `vehicle-legal`. Les chemins « à créer » sont des
livrables futurs.

- `vehicle-legal/skills/used-vehicle-dealer-defect/SKILL.md` — le skill (à créer)
- `vehicle-legal/references/vente-vehicule.md` — régimes de vente, qualité du vendeur, pièces remises, sources lues (à créer)
- `vehicle-legal/references/qualification-vehicule.md` — relue, créée par VEH-001
- `vehicle-legal/README.md` — tâche livrée ajoutée
- `vehicle-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Annonce, bon de commande, facture ; identité et qualité du vendeur.
- Date de remise du véhicule, kilométrage à la remise et à la panne.
- Procès-verbal de contrôle technique remis, historique d'entretien déclaré.
- Garantie commerciale ou contrat d'extension : document et garant indiqué.
- Description de la panne, diagnostic, devis de réparation ; échanges avec le vendeur.

## Sortie attendue

1. Résumé : vendeur, véhicule, panne, demande envisagée.
2. Fiche de qualification : qualité du vendeur établie ou à vérifier, dates, kilométrage.
3. Tableau des voies à examiner : garantie légale de conformité, garantie commerciale, vices cachés ; pour chacune, pièce utile, question ouverte, source lue ou réservée.
4. Pièces à réunir et état du véhicule à conserver.
5. Brouillon de demande au vendeur, sans durée de garantie ni présomption affirmées faute de source lue.
6. Suites : vendeur particulier → VEH-005 ; garant distinct du vendeur → VEH-011 ; expertise → VEH-010 ; crédit lié → DOM-004.
7. Limites et phrase BASE-013.

## Travail attendu

Créer `vente-vehicule.md` et l'appliquer : la qualité de professionnel est
établie par les pièces, jamais déduite d'une annonce ; garantie légale et
garantie commerciale ne sont pas confondues, le garant indiqué sur le
document décidant de la voie. Aucune durée de garantie ni présomption n'est
donnée sans texte lu et date de remise prouvée. L'antériorité de la panne
reste une question, jamais une conclusion. Un compteur soupçonné d'avoir
été modifié est signalé comme fait à établir, avec relais DOM-002 si une
plainte est envisagée.

## Références métier et sources à rechercher

Code de la consommation, garantie légale de conformité (pistes L217-3 et
suivants), garantie commerciale (pistes L217-21 et suivants) et pratiques
commerciales trompeuses (piste L121-2) ; textes propres aux véhicules
d'occasion (piste décret du 4 octobre 1978) ; Code civil, vices cachés
(pistes 1641 à 1649).

## Critères d'acceptation

- [ ] O01 présente les voies à examiner et un brouillon au vendeur, sans durée de garantie non sourcée.
- [ ] O02 laisse conditionnelle la qualité d'un vendeur présenté comme particulier et oriente vers VEH-005 si elle n'est pas établie.
- [ ] O03 sépare garantie commerciale d'un tiers garant et obligation du vendeur.
- [ ] Le vendeur n'est pas présumé de mauvaise foi ; aucune annulation ni remboursement n'est promis.
- [ ] La sortie se termine par la phrase BASE-013 nommant une association de consommateurs, le médiateur du secteur ou un avocat, et un expert automobile pour la question technique.

## Vérification

- Cas normal : O01 — Boîte de vitesses défaillante peu après l'achat chez un garage.
- Cas limite : O02 — Vendeur sur une plateforme se disant particulier mais publiant de nombreuses annonces.
- Cas limite : O03 — Garantie commerciale émise par une société tierce qui refuse la prise en charge.

Scénarios **attendus, non exécutés** ; [relecture DOM-023](../dom-023-annexes/dom-023-verification.md).

## Hors périmètre

Diagnostic de la panne, calcul d'une durée de garantie non sourcée, crédit
affecté, plainte, procédure, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-023, sans implémentation. Contrat commun : [découpage](../dom-023-annexes/dom-023-decoupage-vehicules.md).

## Complément des frictions véhicules — 16 octobre 2026

Points 33–43, 51–54, 73–76, 92, 94, 98–99 et 101–115 de la [matrice](../dom-023-annexes/dom-023-frictions-utilisateurs.md). Exigences supplémentaires du futur skill, sans implémentation.

- [ ] F01 — Vente professionnelle neuve ou d'occasion : tableau séparant conformité, vices cachés, garantie commerciale et garant ; documenter demande au vendeur, refus et passages en atelier. Cette extension porte sur les défauts après livraison ; commande/prix/livraison → VEH-008.
- [ ] F02 — Garantie commerciale expirée, moteur-boîte-pont, usure et entretien hors réseau invoqués : comparer fondement du refus et pièces sans confondre durée de garantie, présomption, cause technique et garantie du constructeur VEH-011.
- [ ] F03 — Diagnostic payant, mises à jour sans effet, défaut persistant : dater demande, réception, reprises et immobilisation ; rechercher gratuité, délai, recours et effets de réparation/remplacement dans la version applicable. L'extension de durée alléguée au point 115 n'est jamais recopiée comme règle.
- [ ] F04 — Vente pour compte d'un tiers, société différente ou vendeur disparu : qualifier parties et contrat ; médiation et prescription séparées ; procédure collective → SOC-027, voie créancier consommateur encore à découper ; aucune conformité professionnelle appliquée automatiquement à un particulier.

Les cas F ci-dessus constituent les scénarios complémentaires **attendus, non exécutés**. Recueillir les pièces nommées, produire la comparaison et le brouillon prévus par la story ; sans source accessible, réserver droit, tarif, calendrier et effet de la clause. Rechercher les textes sectoriels et jurisprudence pertinents avec version, champ et dates ; le texte utilisateur n'est pas une source juridique. [Portée et vérification](../dom-023-annexes/dom-023-frictions-verification.md).
