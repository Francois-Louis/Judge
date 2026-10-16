---
id: DOM-031
titre: "Cadrer un plugin décès et prestations funéraires"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# DOM-031 — Cadrer un plugin décès et prestations funéraires

## Objectif

Aider les proches à lire des devis et contrats et à organiser les démarches au moment d'un décès.

Nom de plugin proposé : `funeral-legal`. Aucun plugin n'est créé par cette story.

## Tâches métier à découper

- Comparer un devis funéraire aux prestations demandées et documents contractuels.
- Préparer une réclamation sur une prestation, un financement ou une facture.
- Distinguer volonté du défunt, pouvoir de décision, concession et questions de prise en charge.

## Qualification et frontières

Qualité et souhaits des personnes, volontés connues, urgence, devis/contrats, signataire, facture et intervenants.

Les prestations et décisions funéraires sont ici ; le règlement de la succession reste en DOM-016 et la garantie d'un contrat d'assurance en DOM-005.

## Sources à prévoir et vérifier

Code général des collectivités territoriales pour le funéraire, Code civil, Code de la consommation et textes sectoriels ; informations officielles des collectivités et de la DGCCRF.

- [DGCCRF](https://www.economie.gouv.fr/dgccrf)
- [Service Public — frais d'obsèques](https://www.service-public.gouv.fr/particuliers/vosdroits/F17059?lang=fr)

Les guides orientent le cadrage ; les textes et versions applicables seront vérifiés lors de chaque implémentation.

## Première tranche proposée

Lire un devis funéraire et préparer les demandes d'explication avant engagement, avec un besoin limité et explicite.

## Critères d'acceptation

- [x] Les tâches sont découpées en stories d'implémentation avec entrées, sortie, pièces, limites et scénarios.
- [x] Un utilisateur peut partir de son problème sans connaître le nom du code ou sa qualification juridique.
- [x] Le domaine garde ses références métier et son autonomie de paquetage ; les frontières ci-dessus évitent les doublons.
- [x] Le cadrage distingue signataire du contrat, personne habilitée à décider et personne éventuellement tenue au paiement ; aucune réponse unique n'est déduite du seul lien familial.
- [x] Le cadrage ne présume pas que l'autre partie a tort et ne promet pas un remboursement ou une issue favorable.
- [x] Les implémentations attendent le bilan PILOTE-003 ; aucune adaptation complète n'est lancée ici.

## Scénarios de contrôle

- Des prestations apparaissent sans avoir été demandées.
- Plusieurs proches sont en désaccord sur une décision.
- Un opérateur réclame un paiement et les signataires ne sont pas identifiés.

Vérifier l'orientation, les pièces à demander et le résultat attendu ; ne pas résoudre ces dossiers pendant le cadrage.

## Hors périmètre

Créer un plugin vide, couvrir toute la matière en une seule story ou exécuter une démarche externe.


## Bilan d'exécution — 16 octobre 2026

- [Découpage](dom-031-annexes/dom-031-decoupage-funeraire.md) : nom
  `funeral-legal` conservé (`judge-fr-eu-funeral-legal`) ; installation
  seule, sans profil, agent, hook, connecteur ni accès à l'état civil, à la
  liste des opérateurs habilités ou à un registre de concessions ;
  garde-fous (moment de deuil, trois qualités non confondues, volonté écrite,
  rapportée ou supposée, aucune présomption contre l'autre partie, aucune
  promesse d'issue, aucun délai, plafond, prix ni montant inventé, urgence
  d'abord, aucun choix d'opérateur, collecte minimale) ; table des points
  d'entrée en langage courant ; qualification commune ; frontières avec
  successions, assurance, consommation, banque, protection sociale, santé,
  protection des majeurs, pénal, contentieux, exécution, administratif,
  famille, dettes, construction, animaux et données.
- Section dédiée au signataire du contrat, à la personne habilitée à décider
  et à la personne éventuellement tenue au paiement : chacune fondée par une
  pièce ou un fait déclaré, ou « à établir », jamais par le seul lien
  familial.
- 12 propositions FUN-001 à FUN-012 sous `suites/`, en quatre rangs.
  Première tranche : FUN-001, devis funéraire lu avant engagement, qui crée
  le paquet avec ce seul skill. Facture et prestations non demandées,
  désaccord entre proches, demande de paiement et carte des financements au
  rang 2 ; contrat obsèques, concession, premières démarches, marbrerie et
  destination des cendres au rang 3 ; volontés anticipées et exhumation ou
  transfert au rang 4.
- Cinq points ouverts sans story : décès ou sépulture hors de France, don
  du corps, décès périnatal, saisine urgente du juge sur les funérailles,
  contribution des proches aux frais sans actif successoral.
- [Vérification documentaire](dom-031-annexes/dom-031-verification.md) :
  les trois scénarios de la story et seize cas limites, sans délai, montant
  ni droit conclu.
- Ligne `funeral-legal` de la [matrice BASE-003](../00-fondations/base-003-annexes/base-003-dossier-architecture.md)
  précisée ; famille FUN ajoutée au générateur de l'index et index régénéré.
- [Contrôles statiques](dom-031-annexes/dom-031-resultats.json), produits par
  [le contrôleur du lot](dom-031-annexes/dom-031-controles.py), sur le modèle de DOM-023.

Fichiers du lot : présente story, découpage, vérification, contrôleur,
relevé JSON, 12 propositions `suites/fun-*.md`, ligne de BASE-003,
`backlog/etat.py` et `backlog/ETAT.md`. Le lot reste sous `backlog/`, sans
entrée NOTICE.

**Portée :** cadrage documentaire relu par l'agent de maintenance sur pièces
fictives, avec contrôles statiques. Aucune source juridique lue : les
articles cités sont des pistes. Aucun plugin créé, skill exécuté, paquet
installé, lecteur réel ou indépendant. Le préalable PILOTE-003 est satisfait
après BASE-011 ; aucune tranche n'est sélectionnée.
