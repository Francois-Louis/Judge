---
id: FUN-009
titre: "Préparer l'expression écrite de ses propres volontés funéraires"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-031, PILOTE-003, BASE-005, BASE-006, BASE-008, FUN-003]
---

# FUN-009 — Préparer l'expression écrite de ses propres volontés funéraires

## Objectif et résultat attendu

Une personne qui veut faire connaître ses volontés pour ses obsèques
(inhumation ou crémation, lieu, cérémonie, personne chargée de les faire
respecter) obtient un brouillon clair de ses volontés et la liste des
questions sur la forme et la conservation de cet écrit, sans que sa valeur
soit affirmée.

## Périmètre et fichiers

Plugin principal : `funeral-legal`. Les chemins « à créer » sont des
livrables futurs.

- `funeral-legal/skills/funeral-wishes-statement/SKILL.md` — le skill (à créer)
- `funeral-legal/skills/funeral-wishes-statement/references/modele-volontes.md` — trame de volontés (à créer)
- `funeral-legal/references/volonte-et-decision.md` — relue, créée par FUN-003
- `funeral-legal/README.md` — tâche livrée ajoutée
- `funeral-legal/NOTICE` — entrée datée du lot
- `NOTICE` — entrée racine du lot

## Pièces et informations nécessaires

- Souhaits exprimés par la personne, dans ses mots.
- Personne qu'elle souhaite charger de ses funérailles ; proches à informer.
- Écrits antérieurs, testament ou contrat obsèques existants.
- Mesure de protection éventuelle de la personne.

## Sortie attendue

1. Résumé des souhaits recueillis, dans les mots de la personne.
2. Brouillon de volontés, daté et à signer par la personne, sans formule présentée comme décisive.
3. Questions sur la forme, la conservation et la communication de l'écrit, avec la source lue ou réservées.
4. Points de cohérence avec un testament ou un contrat obsèques existants.
5. Suites : financement anticipé → FUN-006 ; testament et dispositions patrimoniales → DOM-016 ; mesure de protection → DOM-026.
6. Limites et phrase BASE-013.

## Travail attendu

Appliquer `volonte-et-decision.md` du point de vue de la personne vivante :
le skill recueille sans orienter les choix, n'affirme pas que l'écrit
s'imposera et ne mêle pas les volontés funéraires aux dispositions
patrimoniales. Aucun contrat n'est recommandé.

## Références métier et sources à rechercher

Loi du 15 novembre 1887 (pistes FUN-003) ; formes possibles d'expression des
volontés, à rechercher ; contrat obsèques comme alternative, renvoi FUN-006.

## Critères d'acceptation

- [ ] A01 produit un brouillon fidèle aux mots de la personne, sans valeur juridique affirmée.
- [ ] A02 sépare volontés funéraires et dispositions patrimoniales et oriente ces dernières vers DOM-016.
- [ ] Aucun choix religieux, philosophique ou commercial n'est suggéré.
- [ ] La sortie se termine par la phrase BASE-013 nommant un notaire ou un avocat.

## Vérification

- Cas normal : A01 — Personne souhaitant une crémation et la dispersion des cendres en mer, et désignant une amie pour s'en charger.
- Cas limite : A02 — Personne voulant, dans le même écrit, léguer sa maison et choisir sa sépulture.

Scénarios **attendus, non exécutés** ; [relecture DOM-031](../dom-031-annexes/dom-031-verification.md).

## Hors périmètre

Testament, souscription d'un contrat obsèques, conservation ou dépôt de
l'écrit par le plugin, envoi.

## Complément des frictions décès et obsèques — 16 octobre 2026

Points 36, 132 de la [matrice](../dom-031-annexes/dom-031-frictions-utilisateurs.md). Exigences supplémentaires de la proposition, sans sélection ni implémentation.

- [ ] FA01 — Préparer une expression des souhaits sans les confondre avec testament patrimonial, directives anticipées médicales ou contrat d’assurance ; relever contradictions avec les écrits connus.
- [ ] FA02 — Ajouter les questions de conservation accessible, copies et proches informés ; aucun dépôt, archivage durable ni garantie d’exécution par le plugin.

Scénarios supplémentaires **attendus, non exécutés** : volontés connues seulement d’un ami ; écrit conservé avec un testament inaccessible au moment des obsèques.

Sources à ouvrir lors de l’implémentation : formes, conservation et communication des volontés funéraires ; articulation avec testament, contrat obsèques et directives médicales.

Les règles, montants et délais du texte fourni restent à vérifier selon les faits, le régime et la version applicable. [Portée et contrôles de cette intégration](../dom-031-annexes/dom-031-frictions-verification.md).

## État de la proposition — 16 octobre 2026

Issue de DOM-031, sans implémentation. Contrat commun : [découpage](../dom-031-annexes/dom-031-decoupage-funeraire.md).
