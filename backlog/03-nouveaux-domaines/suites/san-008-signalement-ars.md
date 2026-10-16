---
id: SAN-008
titre: "Préparer un signalement à l'agence régionale de santé"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-007, PILOTE-003, BASE-005, BASE-006, BASE-008, SAN-005]
---

# SAN-008 — Préparer un signalement à l'agence régionale de santé

## Objectif et résultat attendu

Une personne témoin ou victime d'un dysfonctionnement dans une structure de
santé sait ce qu'un signalement à l'agence régionale de santé peut produire,
ce qu'il ne produit pas, et obtient un brouillon de signalement factuel.

## Périmètre et fichiers

Plugin principal : `health-legal`. Les chemins « à créer » sont des
livrables futurs.

- `health-legal/skills/health-authority-report/SKILL.md` — le skill (à créer)
- `health-legal/references/signalement-ars.md` — missions, canaux officiels, sources lues (à créer)
- `health-legal/references/objets-demarche.md` — relue, créée par SAN-005
- `health-legal/README.md` — tâche livrée ajoutée
- `health-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Structure, région, dates ; nature du dysfonctionnement observé.
- Personnes concernées, sans données de santé superflues ni identité de tiers non nécessaire.
- Réclamation déjà faite à la structure et réponse.

## Sortie attendue

1. Résumé : ce que l'agence peut examiner, avec la source lue.
2. Ce que le signalement ne produit pas : ni indemnisation, ni sanction individuelle présumée, ni réponse personnelle garantie.
3. Brouillon de signalement factuel.
4. Canal officiel à vérifier.
5. Suites : réclamation à la structure → SAN-005 ; indemnisation → SAN-006 ; danger immédiat → secours.
6. Limites et phrase BASE-013.

## Travail attendu

Créer `signalement-ars.md` et l'appliquer : structure médico-sociale →
point ouvert, partage avec DOM-025 à décider ; événement indésirable grave :
obligation des professionnels distinguée de la démarche d'un usager ;
consultation injustifiée de dossier → volet privacy distinct.

## Références métier et sources à rechercher

Code de la santé publique, missions de l'agence régionale de santé et
événements indésirables graves (piste L1413-14) ; pages officielles de
l'agence de la région.

## Critères d'acceptation

- [ ] S01 produit un signalement factuel sans données de santé superflues.
- [ ] S02 précise que le signalement n'ouvre ni indemnisation ni réponse garantie.
- [ ] La sortie se termine par la phrase BASE-013 nommant l'agence comme destinataire et une association d'usagers comme appui.

## Vérification

- Cas normal : S01 — Défauts d'hygiène répétés observés dans un service hospitalier.
- Cas limite : S02 — Personne attendant une indemnisation de l'agence.

Scénarios **attendus, non exécutés** ; [relecture DOM-007](../dom-007-annexes/dom-007-verification.md).

## Hors périmètre

Structures médico-sociales au fond, déclaration professionnelle
d'événement indésirable, plainte pénale, envoi.

## État de la proposition — 16 octobre 2026

Issue de DOM-007, sans implémentation. Contrat commun : [découpage](../dom-007-annexes/dom-007-decoupage-sante.md).

## Complément des frictions santé — 16 octobre 2026

Points 41, 50–56, 80, 104, 140 et 155 de la [matrice santé](../dom-007-annexes/dom-007-frictions-utilisateurs.md).

- [ ] FS01 — Qualifier structure, produit, événement et danger ; rechercher circuit ARS/vigilance/autre autorité. DPO/privacy pour incident de données ; ne pas confondre signalement et réclamation ni causalité et succession d'événements.
- [ ] FS02 — Le scénario ci-dessous produit les distinctions et réserves demandées.

Scénario attendu : Effet indésirable et problème de structure : soins d'abord, puis circuits à vérifier séparément sans dépôt automatique.

Scénarios **attendus, non exécutés** ; [portée et contrôles](../dom-007-annexes/dom-007-frictions-verification.md).
