---
id: ANM-007
titre: "Qualifier les pièces d'une cession pour une autre espèce"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-033, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, ANM-001]
---

# ANM-007 — Qualifier les pièces d'une cession pour une autre espèce

## Objectif et résultat attendu

Une personne qui veut acquérir ou a reçu un animal autre qu'un chien ou un
chat identifie l'espèce déclarée, l'usage, l'opération et les pièces à faire
vérifier avant toute conclusion. Cette tranche prépare une recherche spécialisée,
sans valider la cession ou la détention de toutes les espèces.

## Périmètre et fichiers

Plugin principal : futur `animal-legal` (`judge-fr-eu-animal-legal`).
Qualification documentaire d'une cession d'une seule espèce par dossier,
en France, sans certification technique de l'espèce ni avis de légalité.

- `animal-legal/skills/other-species-transfer-orientation/SKILL.md` (à créer).
- `animal-legal/references/cession-autre-espece.md` (à créer).
- `animal-legal/references/qualification-animal.md` — créé par ANM-001, à relire.
- `animal-legal/README.md`, `animal-legal/NOTICE`, `NOTICE` — tâche et traçabilité.
- `animal-legal/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `scripts/test-base008-isolation.py` — version et métadonnées synchronisées.

Charger BASE-005 locale et socle ANM-001 ; autonomie du
[découpage](../dom-033-annexes/dom-033-decoupage-animaux.md).

## Pièces et informations nécessaires

Nom commun et nom scientifique indiqués dans les documents si disponibles,
origine déclarée, identification, usage compagnie/loisir/reproduction/activité,
acteurs et qualités, lieu/dates, contrat/annonce et justificatifs de cession,
certificat ou autorisation seulement si déjà disponible et utile. Ne pas
demander de capturer ou manipuler l'animal pour le photographier.

## Sortie attendue

Fiche de qualification, incertitudes d'identification, carte des documents
fournis et points à faire vérifier, interlocuteur spécialisé et future tranche
de fond à cadrer. Statut domestique, protection, commerce, détention et
mouvement international sont des questions distinctes ; aucun document n'est
déclaré universel ou suffisant pour l'ensemble.

## Travail attendu

Ne pas réutiliser la liste des pièces du chien pour cheval, lapin, oiseau
ou reptile. Suspendre la conclusion si espèce ou origine indéterminée ;
conserver les questions factuelles utiles. Orienter activité agricole vers
DOM-014, protection d'espèce vers DOM-030, capture/chasse/pêche vers DOM-040,
importation vers DOM-009. Ces relais ne remplacent pas le contrat de cession
et ne supposent pas un plugin installé. Une tranche au fond sera choisie
pour une espèce et un contexte après ce travail, sans extension automatique.

## Références métier et sources à rechercher

Code rural et de la pêche maritime ; Code de l'environnement ; Code civil ;
textes d'identification et de détention propres à l'espèce. Textes UE et
conventions de protection/commerce si le rattachement l'exige, publications
du ministère de l'Agriculture et de l'autorité environnementale compétente.
Aucune source ouverte dans DOM-033 : identification du texte, champ, version,
exceptions et transitions à vérifier selon BASE-005 ; lot selon BASE-014.

## Critères d'acceptation

- [ ] L'espèce et l'usage sont documentés ou inconnus, jamais certifiés par l'assistant depuis une photo ou un nom approximatif.
- [ ] La sortie n'étend ni documents du chien/chat ni garantie d'objet courant à une autre espèce.
- [ ] Le dossier donne des questions et un destinataire utiles sans avis de légalité, autorisation de détention ou issue favorable promis.
- [ ] Les références spécialisées restent locales ; recette BASE-006 autonome, sans source et sans connecteur obligatoire.
- [ ] Phrase BASE-013 avec avocat ou juriste compétent ; autorité d'identification/protection et vétérinaire pour santé distingués du conseil, renfort si enjeu irréversible.
- [ ] Les citations ont un statut réel selon BASE-005 ; aucune règle, liste de pièces ou décision générée de mémoire.

## Vérification

- Cas normal : cession d'un équidé de loisir avec pièces d'identification : qualification et questions propres à l'espèce, pas de liste canine.
- Cas limite : reptile vendu sous un nom commun ambigu : espèce et statut réservés, aucune détention déclarée autorisée.
- Cas limite : oiseau provenant d'un pays tiers ou animal pour élevage : questions distinctes protection/douane/activité, sans dossier entier transféré.
- Sans source : fiche factuelle et professionnel/service à consulter, aucune formalité ni autorisation confirmée.

Scénarios **attendus, non exécutés** ; recette BASE-006 et USAGE-001 `1.0.0`
avec sorties et lectures conservées lors de l'implémentation. Relecture par
l'utilisateur ; aucune compréhension attestée sans résultat observé.
Aucune tranche sélectionnée.

## Hors périmètre

Garantie ou contrat au fond pour toutes les espèces, identification biologique,
conseil vétérinaire, autorisation, commerce d'espèce protégée validé,
formalités internationales ou démarche externe.
