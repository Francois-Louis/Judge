---
id: SOC-026
titre: "Préparer les questions d'une fermeture volontaire de société"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-002, PILOTE-003, BASE-005, BASE-006]
---

# SOC-026 — Préparer les questions d'une fermeture volontaire de société

## Objectif et résultat attendu

Fiche d'orientation documentée : arrêt d'activité, mise en sommeil ou fermeture définitive envisagée ; questions de solvabilité ; étapes/pièces/frais à vérifier et relais fiscaux ou sociaux.

Issue des [frictions sur les formalités d'entreprise](../exist-002-annexes/exist-002-frictions-utilisateurs.md), points 79–83. Cette proposition du 16 octobre 2026 ne lance aucune implémentation.

## Périmètre et fichiers à examiner

Propriétaire : corporate-legal. Nouveau skill proposé `corporate-legal/skills/closure-intake/SKILL.md` et référence locale `fermeture-volontaire.md` à créer ; liens depuis l'orientation et README du plugin à examiner.

Les chemins « à créer » sont des livrables futurs. Les références métier seront embarquées dans le paquet de leur propriétaire, sans dépendre d'un plugin voisin. Un relais encore indisponible produit une fiche manuelle, jamais un appel au skill hérité.

## Entrées nécessaires

SAS/SASU ou SARL/EURL, objectif temporaire/définitif, activité et dates, associés, créances, dettes, trésorerie disponible, salariés, contrats et garanties, pièces/décisions déjà reçues.

La lecture ponctuelle reste possible sans profil de cabinet, registre initialisé ou connecteur. Demander seulement les pièces nécessaires, conserver leur provenance et les contradictions.

## Travail attendu

Rester à la qualification et préparation documentaire ; la rédaction des décisions de dissolution, la liquidation et la radiation demandent des tranches séparées. Ne pas choisir la procédure à partir de la seule volonté du dirigeant. Doute sur paiement des dettes : réserver le parcours amiable, demander les données disponibles et orienter vers le cadrage SOC-027 et un conseil compétent. Séparer formalité de registre, obligations contractuelles et déclarations finales. Aucun effacement de dette déduit de la fermeture.

Le lot suit BASE-003, BASE-005 (méthode locale), BASE-006 et l'isolation BASE-008. Appliquer BASE-013 pour la limite de la réponse et le conseil compétent, puis BASE-014 avant livraison. Un interlocuteur administratif n'est pas assimilé au conseil de la personne.

## Sources à rechercher

Code civil, Code de commerce et textes relatifs à cessation temporaire, dissolution/liquidation amiable et radiation ; informations officielles Guichet unique et juridiction compétente ; sources fiscales/sociales chez leurs propriétaires.

Pistes non vérifiées dans cette intégration documentaire. Lire textes exacts, versions, champ, transitions et faits à la date du dossier ; tracer lectures et échecs selon BASE-005 et les voies officielles BASE-010. Les affirmations du texte utilisateur ne constituent pas des règles validées.

## Critères d'acceptation

- [ ] La sortie annoncée est observable sur le cas normal et cite les pièces/localisations utiles.
- [ ] Le cas limite conserve les inconnues déterminantes et donne une prochaine démarche compréhensible.
- [ ] Aucun délai, montant, effet suspensif ou état administratif n'est affirmé sans fondement applicable et preuve suffisante.
- [ ] Le paquet détaché reste autonome ; recette client, résultat métier et compréhension sont vérifiés selon BASE-006.
- [ ] L'avertissement et le professionnel pouvant conseiller sont adaptés au domaine selon BASE-013.
- [ ] Un brouillon ou un contrôle documentaire n'est jamais présenté comme une démarche exécutée.

## Scénarios de contrôle

- Cas normal : SASU souhaitant arrêter sans salarié, pièces de trésorerie et dettes fournies : questions, étapes et justificatifs sans déclarer une liquidation achevée.
- Cas limite : SARL sans trésorerie connue, dettes échues et projet de liquidation amiable : parcours réservé, besoin de qualification urgente et pièces demandées ; EI dirigée vers DOM-039.

Scénarios attendus, non exécutés. Le futur lot conserve sorties, pièces et sources réellement lues ; une relecture documentaire ne vaut pas une exécution du skill.

## Hors périmètre

Diagnostic définitif d'insolvabilité, conduite de liquidation, rédaction de tout acte de fermeture, calcul de boni/mali ou déclarations finales.

## État de la proposition

Statut `proposee`. Le bilan PILOTE-003 est terminé, avec ses limites documentées ; aucune extension n'est sélectionnée par cette intégration. Pour les contrôles documentaires et leur portée, voir la [vérification de l'intégration](../exist-002-annexes/exist-002-frictions-verification.md).
