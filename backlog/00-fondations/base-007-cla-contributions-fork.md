---
id: BASE-007
titre: "Retirer le contrôle CLA hérité et préciser les contributions au fork"
statut: terminee
priorite: P0
nature: implementation
dependances: [BASE-001]
---

# BASE-007 — Retirer le contrôle CLA hérité et préciser les contributions au fork

## Objectif

Appliquer la correction minimale proposée par l’audit BASE-001 : cesser de
demander automatiquement aux contributeurs du fork de signer le CLA du
projet d’origine et rendre explicite la destination des contributions.

## Périmètre

- `.github/workflows/cla.yaml`.
- Sections de contribution de `CONTRIBUTING.md` et `README.md`.
- Identification du rôle historique de `CLA.md`, sans réécriture de l’accord.
- Point de départ : [relevé BASE-001](base-001-releve-audit.md).

## Travail attendu

- Retirer le workflow CLA hérité du fork dans les fichiers locaux.
- Remplacer l’obligation de signature héritée par les consignes propres au
  fork ; préciser que les PR visent `Francois-Louis/Judge` et qu’une contribution
  à l’origine reste une démarche distincte et volontaire.
- Identifier `CLA.md` comme le document hérité du projet d’origine ; préserver
  son texte et les attributions/licences des contenus existants.
- Consigner qu’un contrôle CLA éventuellement exigé dans les protections
  GitHub devra être examiné séparément ; ne pas modifier ces protections.

## Critères d’acceptation

- [x] Aucun workflow local ne lance le contrôle CLA hérité.
- [x] Les consignes de contribution n’exigent plus cette signature pour le fork.
- [x] Le dépôt cible des contributions et le rôle historique de `CLA.md` sont explicites.
- [x] Le texte de l’accord, `LICENSE` et les attributions existantes sont préservés.
- [x] Aucun push, aucune PR ni modification de réglage GitHub n’est nécessaire à la vérification locale.

## Vérification

Lire le diff des fichiers ciblés, inventorier les workflows restants et
chercher les invitations résiduelles à signer dans les consignes de
contribution. Vérifier les liens Markdown et la préservation des textes
historiques. Signaler la limite concernant les protections distantes.

## Hors périmètre

Créer un CLA propre au fork, modifier les réglages GitHub ou une branche de
signatures distante, publier, détacher le fork, renommer les plugins ou
corriger les mises à jour du hub. Les corrections sont appliquées au titre de
BASE-007 ; le relevé BASE-001 reste le constat historique antérieur au retrait.

## Bilan d'exécution — 15 octobre 2026

- Suppression locale de `.github/workflows/cla.yaml` : aucun workflow GitHub
  Actions ne reste dans le checkout.
- [CONTRIBUTING.md](../../CONTRIBUTING.md) et la section « Contributing » du
  [README.md](../../README.md) désignent `Francois-Louis/Judge` comme dépôt
  cible des PR. La contribution à l'origine est distincte et volontaire ;
  la signature du CLA hérité n'est plus demandée pour le fork.
- [CLA.md](../../CLA.md) est identifié dans ces consignes comme le document
  historique de Claude for Legal désignant Anthropic PBC, sans modifier son
  texte. Ses octets et ceux de [LICENSE](../../LICENSE) sont identiques à HEAD ;
  les attributions existantes sont conservées.
- Vérifications locales : relecture du diff, inventaire des workflows,
  recherche des anciennes invitations à signer dans les consignes de
  contribution, résolution des liens Markdown locaux modifiés et contrôle
  du format avec `git diff --check`.
- Limite : les protections de branches et rulesets GitHub n'ont pas été
  inspectés ni modifiés. Si un contrôle CLA y reste requis, son exigence devra
  être examinée séparément par le mainteneur. La suppression locale ne prouve
  pas sa désactivation distante ; aucun push, PR ou changement de la branche
  de signatures n'a été effectué.
