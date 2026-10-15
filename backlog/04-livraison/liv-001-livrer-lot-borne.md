---
id: LIV-001
titre: "Préparer une livraison limitée au périmètre adapté"
statut: proposee
priorite: P2
nature: livraison
dependances: [BASE-004, PILOTE-003]
---

# LIV-001 — Préparer une livraison limitée au périmètre adapté

## Objectif

Rendre installable et vérifiable un petit lot, sans laisser croire que tout le dépôt est adapté.

## Points de départ

- [.claude-plugin/marketplace.json](../../.claude-plugin/marketplace.json)
- [README.md](../../README.md)
- [QUICKSTART.md](../../QUICKSTART.md)
- [LICENSE](../../LICENSE)
- [backlog/](../../backlog/)

## Travail attendu

- Lister les skills et plugins effectivement adaptés, leur version et leurs limites. Choisir le lot après vérification des stories concernées.
- Vérifier que l'identité du fork, les chemins et la coexistence prévus en BASE-004 sont réellement en place pour ce lot ; sinon ouvrir les corrections nécessaires avant livraison.
- Aligner les métadonnées et les instructions d'installation du lot. Conserver les attributions et signaler les modifications conformément à la licence.
- Vérifier l'artefact installable et documenter les résultats des contrôles disponibles.
- Préparer les notes de version et les commandes éventuelles pour le fork, sans publication distante dans cette story.

## Critères d'acceptation

- [ ] Le périmètre annoncé correspond exactement aux stories terminées et vérifiées.
- [ ] L'installation ne récupère pas silencieusement les versions ou configurations de l'origine.
- [ ] Les manifestes du lot et le catalogue restent cohérents ; les contenus éditeur sont distingués des adaptations.
- [ ] Les commandes de publication éventuellement préparées ciblent le fork choisi et ne créent pas de PR vers l'origine.
- [ ] Aucune publication, aucun push ni aucun détachement de fork n'est effectué par cette story.

## Vérification

Installer seulement le lot depuis son artefact, ouvrir ses références, invoquer une commande adaptée et vérifier les scénarios retenus. Noter les outils indisponibles au lieu de les compter comme réussis.

## Hors périmètre

Attendre que tous les domaines soient terminés pour livrer, modifier un compte distant ou annoncer une validation juridique globale.

