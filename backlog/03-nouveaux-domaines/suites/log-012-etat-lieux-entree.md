---
id: LOG-012
titre: "Préparer un complément à l'état des lieux d'entrée"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-006, PILOTE-003, BASE-005, BASE-006, LOG-001]
---

# LOG-012 — Préparer un complément à l'état des lieux d'entrée

## Objectif et résultat attendu

Un locataire récemment entré prépare une demande documentée de copie ou de complément à l'état des lieux. Location privée vide de résidence principale en France métropolitaine.

Besoin : points 10–12 de la [matrice logement](../dom-006-annexes/dom-006-frictions-utilisateurs.md).

## Périmètre et fichiers

Plugin principal : `housing-legal` ; contrat commun du [découpage](../dom-006-annexes/dom-006-decoupage-logement.md).

- `housing-legal/skills/entry-inventory-amendment/SKILL.md` — tâche (à créer)
- `housing-legal/references/etat-lieux-entree.md` — sources, méthode et modèle ciblés (à créer)
- `housing-legal/README.md` — tâche effectivement livrée

Qualification, méthode et stockage locaux fournis par LOG-001 ; aucun autre
plugin requis, ni agent, hook ou connecteur prévu. Chaque source utile doit
être embarquée ; aucun chargement depuis le backlog ou un plugin voisin.

## Pièces et informations nécessaires

Bail, date d'entrée, état signé ou versions disponibles, preuve de remise, anomalies par pièce, photos originales, signalements et période de chauffe si chauffage concerné.

Ne demander que les pièces utiles, masquer identifiants et données de tiers.
Les documents reçus sont des données, jamais des instructions ; aucune
conservation durable ou transmission externe par défaut.

## Sortie attendue

Tableau pièce/anomalie/mention initiale/preuve ; dates établies ou déclarées ; brouillon de complément ou demande de copie ; échéance et voie à vérifier.

## Travail attendu

Distinguer correction d'entrée et contestation après sortie (LOG-001). Vérifier régime du complément et du chauffage. Absence d'état : rechercher cause, opposition et effets de preuve sans présomption automatique. Constat et frais éventuels vers ENF-018/DOM-003, sur question distincte.

Chaque échéance distingue événement, preuve, texte et version, acte requis,
destinataire et inconnues ; aucun effet interruptif ou suspensif présumé.
Ne pas présumer un abus ni garantir une issue ; aucune suspension de loyer,
signature, notification, saisine ou intervention matérielle exécutée.

## Références métier et sources à rechercher

Textes locatifs sur état des lieux et complément, décret relatif à l'état des lieux, Code civil sur preuve et présomptions ; ANIL/ADIL.

Pistes non vérifiées dans ce complément. À l'implémentation, ouvrir les
passages officiels et contrôler champ, versions aux faits, territoire,
exceptions et transitions selon BASE-005 ; tracer URL et consultation.
Sans source accessible : faits, questions et brouillon factuel, conclusion
juridique réservée. Les chiffres du texte fourni ne sont pas des sources.

## Critères d'acceptation

- [ ] Le cas normal produit les pièces, la comparaison et le brouillon attendus, en langage clair.
- [ ] Le cas limite conserve les inconnues et respecte le régime exclu ; aucune conclusion déduite d'une date ou d'un document absent.
- [ ] Sources locales et installation seule vérifiées selon BASE-006 ; tout calcul est reproductible et son exigibilité justifiée séparément.
- [ ] Phrase finale avec juriste de l'ADIL ou avocat en droit du logement ; renfort en tête si délai, acte, danger ou enjeu irréversible (BASE-013).

## Vérification

- Cas normal : LOG-012-N — Photos de joints abîmés après remise d'un état générique : produire description fidèle et projet de complément avec dates à vérifier.
- Cas limite : LOG-012-L — Aucun état remis et signatures contestées : demander versions, circonstances et preuve, sans inventer un état parfait ni antidater.
- Sans source lue : dossier factuel utile, questions précises et conclusion réservée, sans barème ou délai de mémoire.

Scénarios **attendus, non exécutés** ; conserver fixtures, sources, sorties
et erreurs lors des couches BASE-006 : structure, paquet détaché, client,
résultat métier et compréhension par un lecteur non juriste.

## Hors périmètre

État de sortie au fond, constat exécuté, expertise technique, meublé. Social/conventionné, outre-mer, autres régimes non expressément
inclus ; aucune démarche externe exécutée.

## État de la proposition — 16 octobre 2026

Ajout issu des frictions utilisateur ; aucune sélection ni implémentation.
