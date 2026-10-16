---
id: IA-024
titre: "Confronter une allégation IA aux justificatifs du fournisseur"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-005, PILOTE-003, BASE-005, BASE-006]
---

# IA-024 — Confronter une allégation IA aux justificatifs du fournisseur

## Objectif et résultat attendu

Un acheteur, particulier ou petite organisation, obtient un tableau comparant une promesse de capacité, de certification ou de conformité aux pièces réellement disponibles, puis les questions à poser. Points 17, 37, 40–41 de la [matrice des frictions](../exist-005-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `ai-governance-legal` (`judge-fr-eu-ai-governance-legal`).

- `ai-governance-legal/skills/vendor-ai-review/SKILL.md` : mode borné à cette tâche.
- `ai-governance-legal/references/allegations-fournisseur.md` : référence locale à créer.
- README et seuls blocs de routage concernés de CLAUDE.md ; IA-012 garde les engagements contractuels et IA-013 la clause à négocier.

Appliquer le [contrat commun IA](../exist-005-decoupage-ia.md), BASE-005 locale, BASE-006 et BASE-008. Une page ou offre manuelle suffit ; aucun profil ni dossier IA-008 préalable. Embarquer les références ; synchroniser les métadonnées modifiées et ajouter NOTICE racine/local lors de l'implémentation.

## Entrées nécessaires

Allégation exacte et support daté, offre, produit/usage/version, auteur, logo ou certificat, rapport d'audit, référentiel, démonstration et contrat disponibles. Identifier destinataire particulier/professionnel et objectif : vérifier, acheter ou contester.

## Travail attendu

Limiter la passe à une allégation : texte exact, portée annoncée, émetteur, référentiel invoqué, version/usage évalués, méthode, exclusions, date/validité et preuve. Distinguer auto-déclaration, audit privé, certification revendiquée et procédure réglementaire à vérifier. Une attestation sur une version antérieure ne couvre pas automatiquement la version vendue ; une pièce non fournie reste inconnue. Une API tierce ne prouve pas l'absence d'IA ni une tromperie. Produire les écarts et une demande de justificatifs ou de démonstration bornée, sans tester sur des données personnelles réelles. Relais CONSO-021 pour le destinataire d'une publicité ; PDT-009 pour l'annonceur ; commercial pour le contrat B2B. Aucun verdict général de conformité ou fraude.

## Sources à rechercher

Document exact et daté, référentiel et organisme revendiqués, textes officiels du règlement IA et procédures d'évaluation pertinentes, droit des pratiques commerciales selon destinataire. Distinguer authentification d'une attestation, pertinence de son champ et conformité effective ; un logo ou un guide ne remplace pas le texte applicable.

## Critères d'acceptation

- [ ] Chaque constat cite support, passage, version et statut prouvé/manquant ; les questions visent les lacunes déterminantes.
- [ ] Un rapport ancien ou partiel n'est pas extrapolé à tout le service ; aucune certification créée par la sortie.
- [ ] Type de preuve et voie de contestation sont distincts ; absence de preuve fournie ne devient pas preuve de fraude.
- [ ] Lecture utile sans profil, compte, plugin voisin ni contrat complet ; références locales du paquet isolé.
- [ ] Sources, limites et prochaine action lisibles ; rappel BASE-013 avec professionnel adapté.

## Vérification

- Cas normal : F10, « conforme AI Act » accompagné d'un rapport privé sur une ancienne version ; relever les écarts de portée et préparer les questions.
- Cas limite : certificat accessible seulement par un lien indisponible et API tierce mentionnée ; conclusion réservée sans absence ni falsification présumées.

Recette future BASE-006 : sorties, paquet détaché, client et compréhension ; [portée de l'intégration](../exist-005-frictions-verification.md).

## Hors périmètre

Certification, audit de conformité technique, benchmark de performances, expertise de faux, négociation complète du contrat ou signalement externe exécuté.

## État de la proposition — 16 octobre 2026

`proposee`, préalable PILOTE-003 satisfait ; aucune implémentation sélectionnée.
