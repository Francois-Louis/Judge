---
id: ANM-006
titre: "Orienter un incident ou signalement concernant un chien"
statut: proposee
priorite: P3
nature: implementation
dependances: [DOM-033, PILOTE-003, BASE-005, BASE-006, BASE-008, BASE-013, ANM-001]
---

# ANM-006 — Orienter un incident ou signalement concernant un chien

## Objectif et résultat attendu

Une personne concernée par un chien détenu en France décrit morsure,
danger ou maltraitance alléguée, ou lit un courrier reçu à ce sujet. Elle
repère l'aide immédiate, les faits et la question à confier au bon interlocuteur,
sans verdict pénal ni certification d'une obligation locale.

## Périmètre et fichiers

Plugin principal : futur `animal-legal` (`judge-fr-eu-animal-legal`).
Fiche d'orientation d'un incident concret concernant un chien ; différencier
observation, signalement, décision administrative et convocation pénale.

- `animal-legal/skills/dog-incident-orientation/SKILL.md` (à créer).
- `animal-legal/references/incident-signalement-chien.md` (à créer).
- `animal-legal/references/qualification-animal.md` — créé par ANM-001, à relire.
- `animal-legal/README.md`, `animal-legal/NOTICE`, `NOTICE` — tâche et traçabilité.
- `animal-legal/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `scripts/test-base008-isolation.py` — version et métadonnées synchronisées.

Charger copie BASE-005 et qualification locale ; appliquer le
[découpage](../dom-033-annexes/dom-033-decoupage-animaux.md).

## Pièces et informations nécessaires

Danger actuel et lieu avant toute pièce ; rôle de la personne, chien concerné,
faits/dates/lieux et auteur de chaque récit, témoins et photos déjà disponibles
sans prise de risque ; courrier complet si reçu, émetteur, objet, réception
et échéance écrite. Données de victime et de détenteur réduites au nécessaire.

## Sortie attendue

Aide humaine prioritaire selon danger, fiche factuelle, nature du document,
inconnues et orientation motivée. Morsure avec blessure → santé humaine et
DOM-035 ; santé de l'animal → vétérinaire ; détention/mesure locale → autorité
compétente à vérifier ; plainte/convocation → DOM-002 et avocat ; recours
administratif distinct → DOM-010 ; assurance → DOM-005 si demande autonome.

## Travail attendu

Ne pas attendre une photo ou un contrat pour orienter un danger immédiat.
Ne pas conseiller d'approcher, de saisir l'animal, d'entrer chez un tiers
ou de publier son identité. Lire le courrier avant de qualifier la démarche ;
préserver dates et preuve de réception. Vérifier séparément les obligations
éventuelles liées à l'incident et celles d'un statut particulier du chien,
sans catégorie déduite d'une photo, numéro d'urgence inventé ou délai mémorisé.

## Références métier et sources à rechercher

Code rural et de la pêche maritime : détention, chien dangereux, morsure,
protection animale et pouvoirs de l'autorité ; arrêtés locaux selon commune
et date ; Code pénal et procédure pour orientation seulement. Ministère de
l'Agriculture, Service-Public et préfecture/mairie comme points d'accès à
vérifier. Pistes non ouvertes dans DOM-033 : texte, compétence, version,
exceptions et transitions à lire selon BASE-005, relecture BASE-014 avant lot.

## Critères d'acceptation

- [ ] Danger et besoin de soins humains/vétérinaires passent avant la demande documentaire, sans conseil clinique ni prise de risque.
- [ ] Signalement, décision et convocation restent distincts ; auteur d'un courrier et conseil juridique ne sont pas confondus.
- [ ] Les seules pièces utiles accompagnent chaque question orientée ; aucune maltraitance, infraction, responsabilité ou catégorie déclarée acquise.
- [ ] L'urgence documentaire est signalée sans durée inventée ; toute compétence locale non vérifiée reste à confirmer.
- [ ] Exécution autonome BASE-006, y compris sans profil/source/connecteur ; aucun signalement ni transmission automatique.
- [ ] Phrase finale BASE-013 et renfort de tête selon danger/procédure ; avocat en pénal, professionnel de santé ou vétérinaire selon besoin de soins.
- [ ] Textes et décisions sont tracés selon BASE-005, les sources non lues restent des pistes.

## Vérification

- Cas normal : signalement d'un chien régulièrement laissé sans eau, sans danger actuel déclaré : faits observés et interprétation distingués, destinataire à vérifier.
- Cas limite : morsure récente et blessure humaine : aide immédiate puis orientation, pas d'attente du certificat pour agir ni d'indemnisation calculée.
- Cas limite : courrier du maire et convocation de police joints : deux questions distinctes, dates conservées, avocat pour la procédure pénale.
- Sans source : faits et orientation vers service humain, aucune obligation locale, délai ou qualification juridique confirmé.

Scénarios **attendus, non exécutés** ; recette BASE-006 et USAGE-001 `1.0.0`
à conserver avec sorties et lectures. Relecture par l'utilisateur ; aucun
résultat de compréhension présumé. Aucune tranche sélectionnée.

## Hors périmètre

Diagnostic, investigation, capture, publication, signalement envoyé, plainte
rédigée au fond, recours administratif ou pénal, classement d'une race sur photo.
