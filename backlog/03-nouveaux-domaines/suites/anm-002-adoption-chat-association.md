---
id: ANM-002
titre: "Lire une convention d'adoption de chat avec une association"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-033, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, ANM-001]
---

# ANM-002 — Lire une convention d'adoption de chat avec une association

## Objectif et résultat attendu

Une personne comprend ce qu'elle signe ou a signé auprès d'une association
en France pour accueillir un chat, les frais, les engagements et les questions
à clarifier. Elle n'a pas à distinguer seule vente, don, placement et adoption.

## Périmètre et fichiers

Plugin principal : futur `animal-legal` (`judge-fr-eu-animal-legal`).
Un chat de compagnie, convention associative et remise en France ; propriétaire,
détenteur et famille d'accueil distingués. Dépend du paquet ANM-001.

- `animal-legal/skills/cat-adoption-agreement-review/SKILL.md` (à créer).
- `animal-legal/references/adoption-chat-association.md` (à créer).
- `animal-legal/references/qualification-animal.md` — socle créé par ANM-001, à relire.
- `animal-legal/README.md`, `animal-legal/NOTICE`, `NOTICE` — tâche et traçabilité.
- `animal-legal/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `scripts/test-base008-isolation.py` — version et métadonnées synchronisées.

Charger la copie locale BASE-005 et le socle ; autonomie définie dans le
[découpage](../dom-033-annexes/dom-033-decoupage-animaux.md), sans dépendance runtime au backlog.

## Pièces et informations nécessaires

Convention et annexes, annonce, échanges, qualité de l'association et du
signataire, dates de remise/signature, identification disponible, frais/don
et reçus, clauses de soins, stérilisation, suivi, visite et reprise contestées.
Extraits utiles seulement ; masquer adresses et données de tiers inutiles.

## Sortie attendue

Qualification établie ou branches conditionnelles, tableau des engagements
réciproques, frais obligatoires allégués et don distingués, questions sur
propriété/garde et portée des clauses, brouillon neutre à l'association.
Une clause de reprise n'est déclarée ni valable ni abusive sur son seul titre.

## Travail attendu

Lire l'opération réelle avant d'appliquer un régime de vente. Qualifier le
pouvoir du signataire, la remise et la situation de famille d'accueil si
alléguée. Distinguer demande d'explication, volonté de restituer et conflit
de propriété. Signature ou reprise imminente : renfort de tête et conseil
humain, sans demander de remettre l'animal ni de cesser les soins.

## Références métier et sources à rechercher

Code rural et de la pêche maritime : cession, identification et détention
du chat ; Code civil : convention, preuve et engagements ; statut de
l'association et éventuel champ du droit de la consommation à établir.
Ministère de l'Agriculture et Service-Public comme information. Pistes non
ouvertes dans DOM-033 : textes, versions, exceptions, transitions et décisions
utiles à lire selon BASE-005 ; sources du lot relues selon BASE-014.

## Critères d'acceptation

- [ ] Le mot « adoption » et les frais ne suffisent pas à conclure à une vente, un don ou un transfert de propriété.
- [ ] Le tableau distingue obligations des deux parties, frais/don, documents reçus/manquants et points conditionnels.
- [ ] Les clauses sensibles produisent une question sourcée ou réservée, sans abus présumé ni remboursement garanti.
- [ ] Le skill fonctionne sans autre plugin ni profil ; BASE-006 consigne les résultats par couche, dont exécution sans source.
- [ ] La sortie finit par la phrase BASE-013 avec avocat ou juriste compétent ; renfort en tête si remise, signature ou procédure urgente.
- [ ] Les références sont locales ; chaque décision citée est lue ou signalée comme fiche/piste selon BASE-005 ; aucun diagnostic vétérinaire.

## Vérification

- Cas normal : convention pour un chat avec frais et engagement de suivi : tableau des engagements et questions sur les pièces effectivement remises.
- Cas limite : famille d'accueil demandant de conserver le chat : statut et pouvoir de cession réservés, aucun transfert présumé.
- Cas limite : reprise exigée immédiatement sur une clause contestée : urgence et conseil, sans ordre de restitution ni clause déclarée nulle.
- Sans source : lecture factuelle de la convention, portée des clauses réservée.

Scénarios **attendus, non exécutés** ; sorties et ressources à conserver selon
BASE-006 et USAGE-001 `1.0.0`. Relecture prise en charge par l'utilisateur,
compréhension à consigner seulement si observée. Aucune tranche sélectionnée.

## Hors périmètre

Vente de chien ANM-001, diagnostic, soins ou stérilisation conseillés,
contentieux de propriété, reprise forcée, enquête ou envoi à l'association.
