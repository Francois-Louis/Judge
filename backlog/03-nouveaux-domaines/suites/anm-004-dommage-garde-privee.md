---
id: ANM-004
titre: "Documenter un dommage matériel pendant une garde privée de chien"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-033, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, ANM-001]
---

# ANM-004 — Documenter un dommage matériel pendant une garde privée de chien

## Objectif et résultat attendu

Propriétaire, gardien ou tiers prépare un dossier factuel après un dommage
matériel causé par un chien confié à un proche en France. La sortie aide à
poser la question de la garde et à joindre les pièces utiles, sans attribuer
la responsabilité ni confirmer une garantie d'assurance.

## Périmètre et fichiers

Plugin principal : futur `animal-legal` (`judge-fr-eu-animal-legal`).
Garde privée non professionnelle d'un chien, dommage matériel à un tiers,
aucune blessure humaine ni décision judiciaire.

- `animal-legal/skills/private-dog-care-incident/SKILL.md` (à créer).
- `animal-legal/references/dommage-garde-privee.md` (à créer).
- `animal-legal/references/qualification-animal.md` — créé par ANM-001, à relire.
- `animal-legal/README.md`, `animal-legal/NOTICE`, `NOTICE` — tâche et traçabilité.
- `animal-legal/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `scripts/test-base008-isolation.py` — version et métadonnées synchronisées.

Charger méthode BASE-005 locale et socle ; autonomie du
[découpage](../dom-033-annexes/dom-033-decoupage-animaux.md).

## Pièces et informations nécessaires

Rôles et accord de garde, remise/reprise, lieux et chronologie, instructions
données, personnes présentes, récit attribué à son auteur, photos pertinentes,
devis/facture du dommage et échanges reçus. Ne pas demander d'emblée la police
d'assurance complète ni des renseignements sur des tiers sans rapport.

## Sortie attendue

Chronologie de détention et de garde déclarée, faits établis/allégués/inconnus,
question de maîtrise effective à vérifier, pièces manquantes, note factuelle
à relire ; demande distincte à l'assureur via DOM-005 si souhaitée. Devis et
préjudice juridiquement réparable restent distincts.

## Travail attendu

Examiner qui pouvait agir sur l'animal au moment du dommage et les instructions
échangées ; ni propriétaire, ni détenteur enregistré, ni gardien nommé dans un
message ne suffisent seuls à désigner le responsable. Aucune reconnaissance
de responsabilité rédigée par défaut. Blessure humaine : orienter DOM-035 et
ANM-006, avec aide immédiate si besoin, avant le traitement documentaire.

## Références métier et sources à rechercher

Code civil : responsabilité du fait des animaux (piste article 1243), notion
de garde, preuve et engagements ; jurisprudence sur le transfert de garde à
rechercher et lire, sans solution mémorisée. Code rural selon détention.
Aucun texte ni arrêt ouvert dans DOM-033 ; version, champ, exceptions et
transitions à vérifier selon BASE-005 ; sources du lot selon BASE-014.

## Critères d'acceptation

- [ ] Le dossier conserve les rôles déclarés et les faits utiles sans déduire la garde juridique de la seule propriété ou inscription.
- [ ] Dommage, causalité, responsabilité et garantie sont quatre questions distinctes ; aucune somme due ou couverture promise.
- [ ] Le résultat reste factuel et prépare la question au conseil ; une blessure est orientée hors tranche.
- [ ] Le skill autonome est éprouvé selon BASE-006, notamment sans source, profil ni connecteur.
- [ ] Phrase finale BASE-013 avec avocat ou juriste compétent ; autorité, assureur et conseil distingués, renfort en tête si procédure ou urgence.
- [ ] Toute décision citée est lue ou qualifiée de fiche/piste selon BASE-005 ; aucun diagnostic ni conclusion pénale.

## Vérification

- Cas normal : chien confié un week-end à une amie, clôture d'un tiers endommagée : chronologie, instructions et devis, responsabilité réservée.
- Cas limite : propriétaire présent lors de l'incident malgré la garde annoncée : ne pas conclure au transfert de garde depuis le contrat seul.
- Cas limite : tiers mordu et facture médicale jointe : aide et orientation ANM-006/DOM-035, pas de calcul corporel dans cette story.
- Sans source : dossier factuel utile, notion de garde juridique et responsabilité laissées à vérifier.

Scénarios **attendus, non exécutés** ; pièces fictives et sorties à conserver
selon BASE-006 et USAGE-001 `1.0.0`. Relecture par l'utilisateur ; compréhension
réelle consignée seulement si observée. Aucune tranche sélectionnée.

## Hors périmètre

Pension professionnelle, dommage corporel, avis sur garantie, chiffrage du
préjudice, reconnaissance de responsabilité, déclaration ou envoi externe.
