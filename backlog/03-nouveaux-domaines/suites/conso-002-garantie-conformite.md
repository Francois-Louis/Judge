---
id: CONSO-002
titre: "Demander la mise en conformité d'un bien défectueux"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-001, PILOTE-003, BASE-005, BASE-006, CONSO-001]
---

# CONSO-002 — Demander la mise en conformité d'un bien défectueux

## Objectif et résultat attendu

Une personne dont le bien acheté à un professionnel présente un défaut
comprend quelles garanties peuvent jouer, quelles pièces réunir, et obtient un
brouillon de demande au vendeur. Le vendeur qui renvoie vers le fabricant ou
vers une garantie commerciale payante n'est pas suivi sans examen.

## Périmètre et fichiers

- `consumer-legal/skills/conformity-claim/SKILL.md` — le skill (à créer)
- `consumer-legal/references/garanties-legales.md` — garanties légales et commerciale, régimes dans le temps, sources lues (à créer)
- `consumer-legal/README.md` — ajout de la tâche livrée
- `consumer-legal/.claude-plugin/plugin.json` — version

`garanties-legales.md` est relu par CONSO-005, CONSO-010 et CONSO-012, qui
ne le réécrivent pas.

## Pièces et informations nécessaires

Facture et date de délivrance ; bien neuf, d'occasion ou reconditionné ;
défaut, date d'apparition, photos ; usage fait du bien ; démarches et
réponses du vendeur ; document de garantie commerciale s'il existe.

## Sortie attendue

Résumé clair ; tableau des garanties possibles (légale de conformité, vices
cachés, garantie commerciale) avec, pour chacune, les conditions à vérifier
et les faits qui manquent ; pièces à réunir ; brouillon de demande au vendeur ;
prochaines étapes ; limites. Aucune durée, présomption ou remède affirmé sans
texte lu à la date d'achat.

## Travail attendu

Appliquer `qualification-achat.md`. Traiter en premier un signal de danger
(surchauffe, fumée, blessure) : arrêter l'usage, orienter vers les canaux de
sécurité à vérifier et vers DOM-035 en cas de dommage, avant la revue
ordinaire. Orienter véhicule (DOM-023), travaux (DOM-015), animal (DOM-033),
contenu numérique (CONSO-010) et vendeur particulier (CONSO-011).

## Références métier et sources à rechercher

Code de la consommation, garantie légale de conformité et garantie
commerciale, numérotation et version à la date d'achat ; Code civil, vices
cachés (piste 1641 et suivants) ; directive (UE) 2019/771. Un régime
antérieur peut viser les contrats plus anciens : le rechercher plutôt que
l'écarter.

## Critères d'acceptation

- [ ] G01 distingue les garanties et ne suit pas le renvoi au fabricant sans examen.
- [ ] G02 traite le signal de danger avant toute demande ordinaire.
- [ ] G03 n'applique pas le Code de la consommation à un vendeur particulier.
- [ ] La sortie se comprend sans formation juridique, sans garantir l'issue.

## Vérification

- Cas normal : G01 — Aspirateur neuf en panne après quelques mois ; le magasin renvoie au fabricant et propose une extension payante.
- Cas limite : G02 — Batterie de trottinette qui chauffe et a brûlé un tapis.
- Cas limite : G03 — Console d'occasion achetée à un particulier.

Scénarios **attendus, non exécutés** ; couches BASE-006 à appliquer.

## Hors périmètre

Expertise technique, chiffrage d'un préjudice, dommage corporel, procédure
judiciaire, envoi du courrier.

## État de la proposition — 16 octobre 2026

Issue de DOM-001, sans implémentation ni sélection. Contrat commun :
[découpage](../dom-001-decoupage-consommation.md).
