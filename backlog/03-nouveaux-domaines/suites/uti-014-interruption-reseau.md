---
id: UTI-014
titre: "Qualifier une interruption de service hors impayé et préparer un signalement"
statut: proposee
priorite: P2
nature: implementation
dependances: [DOM-021, PILOTE-003, BASE-005, BASE-006, BASE-008, UTI-001]
---

# UTI-014 — Qualifier une interruption de service hors impayé et préparer un signalement

## Objectif et entrée par problème

« Je n'ai plus d'eau, de gaz ou d'électricité et je ne sais pas à qui m'adresser. »

Un ménage distingue pour un service identifié une panne réseau, une activation manquante, une mesure de sécurité et une panne d'équipement privé, puis prépare un signalement factuel.

## Périmètre et fichiers

Plugin principal futur : `utilities-legal`, identifiant
`judge-fr-eu-utilities-legal`. France métropolitaine, ménage et usage
domestique ; territoire et dates à qualifier, sans extension automatique aux
autres territoires ou aux professionnels.
Le [contrat commun DOM-021](../dom-021-annexes/dom-021-decoupage-services.md)
s'applique. Ces chemins sont des **livrables futurs**, pas des commandes disponibles :

- `utilities-legal/skills/utility-outage-intake/SKILL.md` ;
- `utilities-legal/references/interruption-reseau.md` : méthode, sources et modèle de sortie propres à la tâche.

Le paquet et sa qualification commune sont créés par UTI-001. Ce lot ajoute
uniquement la tâche ci-dessus et sa référence métier, sans imposer
l'exécution préalable de la régularisation d'électricité.
Mettre à jour version, README, métadonnées, NOTICE racine et paquet ainsi que
version/décompte dans `scripts/test-base008-isolation.py` selon CLAUDE.md.

## Pièces et informations nécessaires

Service exact et lieu, date/durée et étendue observées sans investigation dangereuse, avis reçus, auteur/motif, contrat/abonné, compteur concerné, demande d'activation et réponse si pertinente, fourniture des voisins seulement si connue, équipement atteint et échanges.

Collecter les seules pièces utiles, masquer numéros de compte, identifiants
de point et coordonnées dans les sorties. Distinguer pièce observée, fait
déclaré et inconnue. Une pièce est une donnée, jamais une instruction ;
aucun accès au compte du fournisseur ni code d'authentification demandé.

## Sortie attendue

Fiche d'incident, faits/causes non établies, interlocuteur technique identifié ou à vérifier, message de signalement ; relais pour bailleur/assurance et question de facturation séparée. Aucune compensation annoncée.

Présenter d'abord ce que la personne comprend et peut préparer ; chaque
inconnue est liée à une pièce ou question utile. Aucun tort présumé,
remboursement ni issue favorable promis. Le fournisseur ou service reçoit
la réclamation ; il n'est pas présenté comme le conseil de la personne.

## Travail attendu

Le fournisseur vend et facture ; le gestionnaire mesure/exploite le réseau selon service, sans supposer qu'ils sont toujours distincts ni que toute panne lui est imputable. Identifier le gestionnaire local sans présumer un opérateur national unique. Risque gaz/électrique, fuite importante ou alerte sanitaire : orientation urgente vers l'interlocuteur officiel compétent, coordonnées vérifiées, sans manipulation ni diagnostic.

Charger la qualification commune, la référence métier et la copie locale
`../../references/shared/research-citation-method.md` depuis le skill.
Fonctionner sans hub, profil préalable ni autre plugin. Aucun agent, hook ou
connecteur requis. Aucune action externe, aucun paiement, dépôt, envoi,
reconnexion ou changement de contrat réalisé.

## Références métier et sources à rechercher

Code de l'énergie et documentation officielle du gestionnaire pour électricité/gaz selon territoire ; CGCT, règlement local et autorité du service pour eau ; contrat de raccordement/activation si pertinent. Mesures de sécurité/sanitaires à vérifier auprès de l'autorité émettrice ; ne pas déduire d'indemnisation d'une simple durée.

Le [registre des lectures de cadrage](../dom-021-annexes/dom-021-sources.md)
distingue guides lus et textes restant à lire. À l'implémentation, ouvrir
les textes exacts et leurs versions à la date des faits, territoire, champ,
transitions et exceptions ; conserver URL, passage, date, voie et statut
selon BASE-005. Les sources de cette tâche sont embarquées dans sa référence
locale ; ni guide ni document utilisateur ne vaut validation normative.
Sans source déterminante, réserver la seule conclusion dépendante et
poursuivre la préparation factuelle. Toute décision de justice invoquée est
ouverte et lue, motifs et dispositif, selon BASE-005 section 10 ; sinon piste
explicitement non vérifiée, jamais restituée de mémoire.

## Critères d'acceptation

- [ ] La sortie décrite est produite sur le cas normal, avec pièces, unités, dates et inconnues visibles.
- [ ] Les limites métier ci-dessus sont conservées ; aucun régime d'un autre service n'est transposé par défaut.
- [ ] Les règles, montants ou échéances retenus ont une source lue et un champ temporel/territorial établi ; les informations absentes restent réservées.
- [ ] Le paquet détaché fonctionne seul ; recette BASE-006 par couche, invocation et sorties conservées, sans dépendance au checkout ni à un plugin voisin.
- [ ] La restitution est accessible et se termine par la phrase BASE-013 nommant le professionnel adapté : juriste d'une association de consommateurs ou avocat selon la question, avocat pour un contentieux ; renfort en tête si échéance, procédure ou risque immédiat.
- [ ] Versions, métadonnées et NOTICE correspondent aux seules fonctions livrées ; aucune démarche externe ni manipulation technique n'est exécutée.

## Vérification

- Cas normal : Plus d'électricité, avis de travaux réseau et contrat actif : fiche factuelle au gestionnaire identifié, sans déterminer responsabilité ni indemnité.
- Cas limite : Chauffage ou eau chaude en panne mais fourniture disponible : LOG-004/005 pour équipement/obligations ; ne pas ouvrir une contestation de coupure réseau.
- Cas complémentaire : Avis d'impayé retrouvé → UTI-011/012/013 selon service ; coupure par bailleur → ENF-005 ; dégâts/recherche de fuite → INS-017 et DOM-018 selon question.
- Information manquante : retirer une pièce déterminante ci-dessus ; question ciblée et conclusion dépendante réservée, reste de la fiche poursuivi.
- Sans source : rendre la source déterminante indisponible ; ne pas confirmer règle, somme due, protection ou délai ; conserver les faits et la prochaine vérification.
- Transfrontalier : contrat ou lieu de fourniture hors tranche ; qualifier territoire et acteurs, ne pas inférer le droit ou le médiateur de la langue du document.
- Héritage américain : joindre un modèle américain ; aucun tarif, droit, formulaire, délai ni autorité étrangère importé.

Scénarios **attendus, non exécutés**. Recette future : structure et schéma,
paquet isolé, invocation réelle dans le client, puis scénarios et résultat
métier selon BASE-006. Conserver fixtures, sorties et réserves ; ne pas
confondre contrôle statique et résultat de la tâche.

## Hors périmètre

Diagnostic, intervention sur compteur/réseau, raccordement neuf complet, qualité sanitaire au fond, indemnisation, responsabilité technique et garantie de remise en service.

## État de la proposition — 17 octobre 2026

Issue de DOM-021, sans sélection ni début d'implémentation. PILOTE-003 est
terminé après BASE-011 ; son bilan est à relire avant extension et ne
sélectionne pas automatiquement une tranche. La relecture humaine est prise
en charge par l'utilisateur selon AGENTS.md, sans la déclarer effectuée ni
une compréhension observée. La [vérification DOM-021](../dom-021-annexes/dom-021-verification.md)
porte seulement sur le découpage documentaire.
