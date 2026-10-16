# DOM-023 — Vérification du complément des frictions véhicules

Intégration documentaire du **16 octobre 2026 (Europe/Paris)**, relue par le
rédacteur. La [matrice](dom-023-frictions-utilisateurs.md) rattache les 195
points du [texte fourni](../sources/vehicules-frictions-2026-10-16.txt), ses
16 lignes d'échéances et ses recommandations aux tâches du backlog. Huit
propositions sont ajoutées ; les douze propositions initiales et les
propriétaires voisins reçoivent leurs exigences complémentaires.

## Relecture du routage

Les cas ci-dessous ont été rapprochés des documents et de leurs sorties
prévues. Ils ne sont pas des exécutions de skill ; les scénarios métier des
stories restent **attendus, non exécutés**.

| Cas relu | Résultat documentaire |
|---|---|
| Diagnostic seul puis travaux facturés | VEH-013 borne l'autorisation ; VEH-001 compare accord et facture, accord téléphonique inconnu conservé comme tel. Aucun écrit présenté comme toujours obligatoire. |
| Pièce sous consigne et preuve menacée | VEH-013 demande les conditions, VEH-001 lit la consigne, VEH-010 prévoit rapport et photos avant restitution ; sécurité prioritaire, conservation absolue non promise. |
| Voiture retenue, frais et panne récurrente | VEH-002 passe en premier ; VEH-001 garde la facture, VEH-003 la réclamation après panne, VEH-014 le calendrier. Aucune cause ni rétention illicite déduite. |
| Voiture neuve immobilisée et garantie commerciale expirée | VEH-004 garde les voies contre le vendeur après livraison, VEH-011 le garant commercial, VEH-014 la mobilité alléguée. Durée, présomption et effet de réparation/remplacement doivent être recherchés séparément. |
| Particulier apparent, garage intermédiaire et import | VEH-007 collecte indices, VEH-019 sépare vendeur et mandataire ; VEH-004/005 restent conditionnelles. Arbitrage CONSO-011 non tranché ; droit français non appliqué automatiquement. |
| Achat réservé en ligne puis signé en concession | VEH-020 exige la chronologie de formation ; l'annonce seule ne crée aucun droit de rétractation. Crédit affecté et vente conservent deux calendriers. |
| Dépannage de nuit puis gardiennage | VEH-015 identifie voie, poids, date et inclusions avant tarif ; VEH-002 traite garde/rétention ; INS-004 l'assistance. Aucun forfait du texte copié comme règle. |
| Enlèvement décidé par autorité | DOM-010 doit découper fourrière, sortie et contestation ; CRIM-005 garde la contravention. Le paiement pour récupérer le véhicule ne choisit pas la voie de recours. |
| Contrôle favorable et panne, ou rappel avec consigne | VEH-016 demande explication au centre sans conclure à la complaisance ; VEH-010 prépare l'examen ; VEH-011 garde rappel et sécurité. Effets administratifs à découper DOM-010. |
| Location courte : dommage, carburant et dépôt | VEH-006 compare les états et la preuve ; VEH-017 garde prestation/frais ; BNK-016 garde préautorisation/débit ; nature assurantielle du rachat à établir avant INS-004. |
| LLD ou LOA, sortie puis restitution | VEH-018 borne LLD sans option et décompte demandé ; BNK-005 lit LOA/crédit ; rétractation et sortie LOA au fond encore à découper en DOM-004. VEH-009 conserve les frais matériels effectifs de restitution. |
| Offre de cession VEI et valeur contestée | INS-003 lit rapport/offre et comparables sans fixer de valeur ; INS-021 garde les échéances ; DOM-010 l'opposition. Aucun silence réputé acceptation ni tarif repris. |
| Import et modification E85/moteur | VEH-019 garde documents promis ; DOM-010 formalités/homologation, DOM-009 douane, DOM-011 quitus et INS-015 déclaration du risque ; aucun contrôle technique ou réglementaire certifié. |
| Négociation et échéance proche | Chaque tâche conserve son calendrier propre et ses inconnues. SignalConso, réclamation ou expertise ne sont pas réputés protéger toutes les actions ; renfort BASE-013 avec interlocuteur adapté. |

## Contrôles de l'intégration

Le [contrôleur du complément](dom-023-frictions-controles.py) vérifie
l'intégrité de la source (SHA-256
`d2f18240d1c45912b6df094cc1f34de573d59af35182c1842fba61300c7d23f7`),
les 195 correspondances, les 16 lignes d'échéances, la structure des vingt
suites, leurs dépendances et les liens du lot. Il vérifie aussi que le
découpage liste les vingt tâches avec leurs skills et dépendances métier,
que les relais ont leur complément, que l'index est généré et qu'aucun
plugin véhicules n'est créé. Le relevé daté est conservé dans
[les résultats](dom-023-frictions-resultats.json).

Des modifications santé et funéraire ont été observées pendant la tâche.
Les fichiers partagés sont préparés avec les seuls compléments véhicules ;
l'index destiné au commit est régénéré sur HEAD et le lot automobile dans
une copie temporaire. Cette copie permet de vérifier le lot sans embarquer
les travaux concurrents. Leurs fichiers et leurs modifications restent dans
le répertoire de travail.

```powershell
python -X utf8 backlog/03-nouveaux-domaines/dom-023-annexes/dom-023-frictions-controles.py
python -X utf8 backlog/etat.py --check
python scripts/check-version-bump.py
python scripts/lint-tool-scope.py
git diff --check
```

Le relevé précise les contrôles effectivement exécutés et le contexte de la
copie préparée. Les contrôles et résultats du lot initial DOM-023 attendent
douze suites : ils restent historiques et ne sont pas réécrits.

## Portée

Exigences de backlog et contrôles structurels du rédacteur. Aucun texte
officiel consulté, tarif, délai ou effet juridique validé, skill implémenté
ou exécuté, paquet installé, client testé, lecteur indépendant ou réponse
métier réelle vérifiée. Les affirmations du texte utilisateur restent des
besoins de recherche ; les cadrages et volets encore non découpés restent
des lacunes explicites. Aucun envoi, signature, paiement, contact ou dépôt
externe exécuté. Les vingt suites restent `proposee`.
