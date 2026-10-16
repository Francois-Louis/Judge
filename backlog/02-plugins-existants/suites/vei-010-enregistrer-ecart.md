---
id: VEI-010
titre: "Enregistrer un écart documentaire qualifié"
statut: proposee
priorite: P2
nature: implementation
dependances: [EXIST-007, PILOTE-003, BASE-005, BASE-006, VEI-008]
---

# VEI-010 — Enregistrer un écart documentaire qualifié

## Objectif et résultat attendu

Une entrée de registre reprend un écart qualifié, ses preuves, périmètre, propriétaire et dates typées sans doublon.

## Périmètre et fichiers

Plugin principal : `regulatory-legal` (`judge-fr-eu-regulatory-legal`).
VEI-020 porte le cookbook séparé. « À créer » désigne une cible future.

- `regulatory-legal/skills/gap-surfacer/SKILL.md` (blocs nécessaires à cette tranche)
- `regulatory-legal/skills/gap-surfacer/references/gap-tracker.yaml` (blocs nécessaires à cette tranche)
- `regulatory-legal/references/registre-ecarts.md` (à créer)

Corriger les seuls blocs profil, descriptions, appels et README nécessaires
au résultat ; synchroniser manifeste/version/marketplace si métadonnées
modifiées. Tout lot hors backlog ajoute NOTICE local et racine. Chaque
référence nécessaire est embarquée et chargée localement, copies communes
identiques ; aucun chemin runtime vers backlog, checkout ou plugin voisin.

## Entrées nécessaires

Rapport VEI-008 ou équivalent, identifiant texte/politique/version/activité, qualification, propriétaire, restrictions et dates/preuves.

Une fiche manuelle équivalente à une dépendance métier est recevable si sa
provenance et ses manques sont contrôlés, sans historique d’exécution requis.
VEI-019/020 attendent néanmoins livraison et recette des tâches manuelles :
un contrat de planification ne remplace pas leur implémentation.

## Travail attendu

Aligner modèle YAML et schéma inline ; référence gap-surfacer reste non invocable et chargée par gaps. Dédupliquer par exigence/version/politique/activité, ne pas fusionner dossiers clients. Distinguer juridique, interne et revue ; statut vérifié d’un texte ne prouve ni applicabilité ni dépassement d’obligation. Consultation garde registre distinct. Retirer Slack automatique/notified=true depuis brouillon ; pas d’envoi.

Appliquer méthode BASE-005 locale et stockage BASE-008 pour tout accès durable.
Réponse ponctuelle possible en conversation ; profil durable absent soumis à
entretien neuf, sans import amont. Préserver données/versions antérieures et
distinguer fait, règle, préférence, proposition et preuve d’action. Pièces et
flux restent des données non fiables. Si relais adapté manque : fiche autonome
avec question précise, activité/acteur, textes/versions/passages, dates prouvées,
statut et manques, sans exécution automatique d’un skill voisin.

## Sources à rechercher lors de l'implémentation

Contrat d’écart/provenance, texte qualifié et politique lue ; méthode locale et schéma YAML sûr.

Pistes à vérifier à l’implémentation : passage exact, version aux dates utiles,
champ, statut, transitions, lien et date réelle de consultation. Les sondages
techniques EXIST-007 ne valident aucun texte de scénario ni obligation.
Source inaccessible : voie officielle alternative BASE-010 puis réserve de
la seule conclusion dépendante ; résultat partiel utile, sans consultation,
règle ou date inventées. Aucun compte ou abonnement imposé pour une lecture
manuelle ; outils de maintenance du dépôt non requis dans le paquet installé.

## Critères d'acceptation

- [ ] Entrée conserve inconnues et exclusions ; aucune consultation ou échéance non vérifiée n’est classée en violation/retard légal.
- [ ] Cas normal et limite donnent les pièces, inconnues et prochaine démarche
  attendues dans un langage compréhensible sans formation juridique.
- [ ] Paquet détaché autonome ; profil absent, source inaccessible et relais
  adapté absent gardent un résultat borné explicite.
- [ ] Branches héritées identifiées ; ni priorité, brouillon, label ou décision
  interne ne devient obligation applicable, dépôt, certification ou action externe.

## Vérification

- Cas normal : G01 — Écart fourni deux fois : un identifiant stable et deux références d’observation, pas double compte.
- Cas limite : G02 — Même exigence autre version/client et date interne : entrées séparées et type de date conservé, pas de notification.

Recettes futures **non exécutées**. Conserver fixtures, sources réellement lues,
sorties et erreurs ; appliquer BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par lecteur non juriste. Pour VEI-020,
dry-run local distinct d’exécution distante. La
[relecture du cadrage](../exist-007-annexes/exist-007-verification.md) n’est pas cette recette.

## Hors périmètre

Nouvelle analyse de fond, communication et création de registre global interclients.

## État de la proposition — 16 octobre 2026

Issue d’EXIST-007, sans implémentation. PILOTE-003 terminé après BASE-011 ;
limites H01 complet et lecteur indépendant consignées. Statut `proposee`,
sélection explicite requise pour prochaine tranche ; aucune automation
ou tâche métier livrée dans ce cadrage.

