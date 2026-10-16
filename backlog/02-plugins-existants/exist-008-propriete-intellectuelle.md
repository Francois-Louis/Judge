---
id: EXIST-008
titre: "Découper l'adaptation de la propriété intellectuelle"
statut: terminee
priorite: P2
nature: cadrage
dependances: [BASE-003, BASE-005]
---

# EXIST-008 — Découper l'adaptation de la propriété intellectuelle

## Objectif

Revoir les tâches PI selon les titres, territoires, auteurs et procédures réellement concernés.

## Points de départ

- [ip-legal/skills/clearance/SKILL.md](../../ip-legal/skills/clearance/SKILL.md)
- [ip-legal/skills/fto-triage/SKILL.md](../../ip-legal/skills/fto-triage/SKILL.md)
- [ip-legal/skills/invention-intake/SKILL.md](../../ip-legal/skills/invention-intake/SKILL.md)
- [ip-legal/skills/cease-desist/SKILL.md](../../ip-legal/skills/cease-desist/SKILL.md)
- [ip-legal/skills/takedown/SKILL.md](../../ip-legal/skills/takedown/SKILL.md)
- [ip-legal/skills/oss-review/SKILL.md](../../ip-legal/skills/oss-review/SKILL.md)

## Travail attendu

- Séparer marques, brevets, droit d'auteur, licences, retrait de contenu et portefeuille ; ne pas présenter une recherche partielle comme une liberté d'exploitation complète.
- Rechercher les hypothèses USPTO, DMCA et fair use ; définir leur traitement seulement lorsqu'un rattachement étranger le justifie.
- Identifier les références INPI, EUIPO, OEB et juridictions pertinentes selon le titre et le territoire, sans tout rendre obligatoire dans chaque tâche.
- Distinguer les contrats de cession, créations de salariés et invention de salarié, avec leurs sources propres.
- Sources à prévoir et à vérifier lors des futures implémentations : Code de la propriété intellectuelle, titres et registres pertinents, EUR-Lex et jurisprudence applicable ; contrats et licences à lire.

## Critères d'acceptation

- [x] Un inventaire couvre tous les skills et dépendances de contenu de `ip-legal`, pas seulement les points d'entrée ci-dessus.
- [x] Les tâches à conserver, réécrire, renommer ou retirer sont justifiées individuellement.
- [x] Le livrable est un ensemble de stories d'implémentation bornées, chacune avec fichiers, résultat attendu et scénarios (relecture documentaire sur fixtures fictives par le rédacteur).
- [x] Aucune réécriture complète du plugin n'est réalisée dans cette story ; ses implémentations attendent le bilan PILOTE-003.

## Vérification

Préparer un nom de marque en France, une invention de salarié et un retrait de contenu ; chaque cas doit avoir un périmètre de recherche et un résultat attendus différents.

## Hors périmètre

Implémenter tout le domaine, modifier des contenus éditeur ou considérer qu'une traduction de vocabulaire valide le raisonnement juridique.

## Bilan d'exécution — 16 octobre 2026

- [Inventaire exhaustif](exist-008-inventaire-pi.md) : 27 fichiers dont douze
  skills, modèles inline, agent, profils, références, contrats/licences et
  sorties attendus ; décisions individuelles. Aucun cookbook PI propre livré.
- [Découpage PI-001 à PI-025](exist-008-decoupage-pi.md) : fichiers, entrées,
  résultats, sources à rechercher, exclusions et scénarios. Marque, invention
  et salarié, brevetabilité, exploitation, droit d'auteur, cession/licence,
  OSS, retrait et portefeuille ont des résultats distincts.
- USPTO, DMCA et fair use repérés dans les fichiers locaux : retrait des
  défauts France/UE, rattachement étranger à établir avant traitement propre.
  INPI, EUIPO, OEB, titres et juridictions sont sélectionnés selon objet et
  territoire, sans imposer toutes les sources à chaque tâche.
- Cession de photographie indépendante, logiciel de salarié et invention de
  salarié ont des suites et sources propres. Recherche partielle de marque ou
  rapprochement brevet ne deviennent pas liberté d'exploitation complète.
- [Relecture du cadrage](exist-008-verification.md) : nom de marque France,
  invention de salarié et retrait de photo fictifs ; périmètres de recherche
  et sorties différents, sans droit ni délai réel établi.
- [Contrôles statiques et empreintes](exist-008-resultats.json), rejouables
  avec le [contrôleur](exist-008-controles.py), et conservation des travaux
  antérieurs. Les différences simultanées éventuelles ailleurs sont consignées
  sans attribution à EXIST-008.
- PILOTE-003 terminé après BASE-011 : préalable satisfait, sans sélection
  d'extension ; limites H01 complet et lecteur indépendant consignées.
  Les vingt-cinq suites restent `proposee`, première tranche suggérée PI-001.

Fichiers du lot : présente story, inventaire, découpage, vérification,
contrôleur, résultats JSON, vingt-cinq propositions `suites/pi-*.md` et index
`backlog/README.md`. Modifications limitées à `backlog/`, sans entrée NOTICE
selon CLAUDE.md ; aucun renommage ou réécriture de skill dans ce lot.

**Portée :** cadrage et relecture par le seul agent de maintenance sur fixtures
fictives, contrôles statiques. Aucune source juridique externe ou interface de
registre consultée/testée, recherche de marque/brevet réellement effectuée,
titularité, brevetabilité, liberté d'exploitation ou échéance réelle validées.
Aucune adaptation/exécution de skill, installation, recette client, lecteur
indépendant, connexion authentifiée, notification, signature, dépôt, paiement,
retrait, publication, planification ou déploiement. Plugin et contenus éditeur
inchangés ; sources, versions, rattachements, procédures et recette restent
aux futures implémentations.

## Décisions du 16 octobre 2026

Ajout par décision de l'utilisateur ([décisions du 16 octobre 2026](../decisions-2026-10-16.md)) : contrat d'édition ou de
production (PI-026), gestion collective (PI-027), reprise d'une œuvre autre
que la photographie (PI-028), droit moral (PI-029) et dessins et modèles
(PI-030). Le statut social et fiscal des artistes-auteurs relève de DOM-042.
Le découpage compte désormais 30 suites.
