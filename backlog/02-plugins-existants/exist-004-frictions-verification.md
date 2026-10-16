# Marketing et emballages — Vérification de l’intégration des besoins

Intégration documentaire du **16 octobre 2026**, liée à la [matrice des 140 points](exist-004-frictions-utilisateurs.md). Relevé distinct de la vérification historique d’EXIST-004 : les résultats et empreintes initiaux sont conservés.

## Contrôles exécutés

Contrôles ponctuels Python en UTF-8 avec PyYAML, comparaison des octets et empreintes, vérification des liens, puis `git diff --check`.

| Contrôle | Résultat |
|---|---|
| Archive source | Copie identique octet pour octet à la pièce jointe. SHA-256 : `09ec84400ce00adf266b9092fff04490a3bea7ddaba7f43efa19aa4b27c6a1f4`. |
| Couverture | Source et matrice contiennent exactement 1 à 140 dans le même ordre ; libellés conservés, sans manque ni doublon. Huit familles et quatorze scénarios de recette attendus. |
| Nouvelles propositions | Treize stories : PDT-018 à PDT-025, COM-021 à COM-023, PI-031 et CONSO-021 ; toutes `proposee`, nature `implementation`. Champs requis, entrées, travail, recherches, critères, exclusions et cas normal/limite présents. |
| Dépendances | 483 identifiants uniques au moment du contrôle ; aucune dépendance absente ni cycle sur le backlog courant. |
| Statuts et index | 36 `terminee`, une `en-cours`, une `a-verifier`, 445 `proposee` ; compteur du README recalculé sur les fichiers courants, ajouts simultanés compris. |
| Découpages | PDT-001 à PDT-025, COM-001 à COM-023 et PI-001 à PI-031 présents une fois dans l’ordre ; CONSO-001 à CONSO-021 présents une fois, en conservant le classement par rang. |
| Situations quotidiennes | S-01 à S-56 présentes une fois ; quatre ajouts S-53 à S-56 pour publicité après achat, partenariat d’influence, agence et emballages. |
| Liens et format | 775 liens Markdown locaux résolus sur les 32 fichiers Markdown du lot ; aucun caractère de remplacement, espace final ou fin de fichier manquante. `git diff --check` passe. |
| Périmètre | 33 fichiers du lot : 32 Markdown et une archive texte, tous sous `backlog/`. Pas de modification de paquet, manifeste, référence embarquée, script ou NOTICE par cette intégration. |

## Relecture documentaire

La relecture a séparé publicité avant diffusion et réclamation après achat ; contrat d’influence et mentions du contenu ; authenticité d’un témoignage et transparence IA ; licence du générateur, droits sur les sources et image/voix ; choix contractuel et traitement de données. CONSO-021 réutilise la qualification d’achat CONSO-004 ou son équivalent manuel. Sans achat, le besoin est un signalement à qualifier, sans remboursement inventé.

Les obligations REP et PPWR restent chez produit, avec des fiches de rôles distinctes et des références métier embarquées. PDT-020 porte flux/pays/filière ; PDT-021 le rapprochement de déclaration ; PDT-022 l’identification et sa communication ; PDT-023 la maquette par marché ; PDT-024 le dossier d’emballage ; PDT-025 le calendrier par disposition. La relation avec l’éco-organisme reste contractuelle chez commercial ; DOM-030 garde pollution et nuisances à cadrer. La promotion des jeux d’argent hors banque reste explicitement à cadrer, sans être absorbée par un domaine sans rapport.

Les scénarios décrivent les sorties à éprouver, notamment cadeau spontané, cumul d’avantages, avatar, voix usurpée, avis modéré, allégation partielle, fournisseur supposé couvrir la REP, petite boîte export, composition alimentaire et stock à plusieurs échéances. Aucune règle du document utilisateur n’est transformée en exigence légale validée. Les sources, la transposition, les reports et les actes d’application seront recherchés dans les lots correspondants.

## Travaux présents et changements simultanés

L’état de départ contenait déjà des modifications et fichiers non suivis. Les éditions de ce lot ajoutent ou précisent les besoins sans remettre ces travaux à zéro. Une comparaison d’empreintes avec l’instantané pris avant les écritures a aussi relevé des ajouts simultanés sur l’intégration des frictions de gouvernance IA, sa source, IA-021 à IA-024 et PRV-035. Ils sont conservés et ne sont pas attribués à cette intégration marketing. Les compteurs globaux sont un état observé, susceptible d’évoluer avec ces travaux parallèles. Un recontrôle après leurs éditions a résolu 787 liens dans les fichiers partagés du lot et relevé un lien nouvellement ajouté dans EXIST-005 vers `exist-005-frictions-verification.md`, absent à cet instant. Ce rapport IA attendu appartient au travail simultané ; sa création et sa vérification ne sont pas revendiquées ici. Les liens introduits par le lot marketing sont résolus.

## Portée

Contrôles documentaires et statiques, relecture par l’agent de maintenance ; aucune recherche juridique externe, validation du droit/des seuils/des dates fournis, exécution de skill, recette client ou lecture indépendante. Les treize nouvelles stories restent proposées ; les quatorze scénarios sont des recettes attendues. Aucun plugin n’est adapté et aucune tranche n’est sélectionnée. Aucun envoi, dépôt externe, impression, modification d’accès, paiement, adhésion, déclaration REP ou publication n’est exécuté.
