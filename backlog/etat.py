#!/usr/bin/env python3
"""Génère backlog/ETAT.md à partir du champ `statut:` de chaque story.

    python backlog/etat.py          # régénère ETAT.md
    python backlog/etat.py --check  # échoue si ETAT.md n'est pas à jour

Les fichiers sans en-tête de story (vérifications, résultats, scripts de
contrôle, sources) sont rattachés comme annexes à la story dont ils portent
le préfixe (`exist-002-…` → EXIST-002, `com-001-annexes/` → COM-001).
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

BACKLOG = Path(__file__).resolve().parent
SORTIE = BACKLOG / "ETAT.md"

EPICS = {
    "00-fondations": "00 — Fondations",
    "01-pilote-travail": "01 — Pilote travail",
    "02-plugins-existants": "02 — Plugins existants",
    "03-nouveaux-domaines": "03 — Nouveaux domaines",
    "04-livraison": "04 — Livraison",
    "05-usages-quotidiens": "05 — Usages quotidiens",
}

FAMILLES = {
    "BASE": "Fondations",
    "PILOTE": "Pilote travail",
    "TRAV": "Travail (suites du pilote)",
    "EXIST": "Cadrages des plugins existants",
    "CLN": "Clinique juridique",
    "COM": "Contrats commerciaux",
    "CTX": "Contentieux",
    "ETU": "Formation juridique",
    "HUB": "Gestion des skills",
    "IA": "Gouvernance IA",
    "PDT": "Produits et publicité",
    "PI": "Propriété intellectuelle",
    "PRV": "Données personnelles",
    "SOC": "Sociétés et opérations",
    "VEI": "Veille réglementaire",
    "DOM": "Cadrages des nouveaux domaines",
    "CONSO": "Consommation",
    "CRIM": "Police et pénal",
    "ENF": "Commissaires de justice et exécution",
    "BNK": "Banque",
    "INS": "Assurance",
    "SAN": "Santé et droits des patients",
    "TPT": "Transports et voyages",
    "DOU": "Douanes et import-export",
    "TEL": "Télécoms et services postaux",
    "LOG": "Logement locatif et habitat",
    "VEH": "Véhicules, garages et réparations",
    "FUN": "Décès et prestations funéraires",
    "IND": "Micro-entreprise et travail indépendant",
    "ANM": "Animaux et responsabilités",
    "CHP": "Chasse et pêche de loisir",
    "LIV": "Livraison",
    "USAGE": "Usages quotidiens",
}

STATUTS = {
    "en-cours": "En cours",
    "a-verifier": "À vérifier",
    "bloquee": "Bloquée",
    "terminee": "Terminée",
    "prete": "Prête",
    "proposee": "À faire",
    "abandonnee": "Abandonnée",
}

ORDRE_PRIORITE = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


def lire_entete(chemin):
    texte = chemin.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texte, re.S)
    if not m:
        return None
    champs = {}
    for ligne in m.group(1).splitlines():
        if ":" in ligne:
            cle, valeur = ligne.split(":", 1)
            champs[cle.strip()] = valeur.strip().strip('"')
    if "id" not in champs or "statut" not in champs:
        return None
    deps = champs.get("dependances", "[]").strip("[]")
    champs["dependances"] = [d.strip() for d in deps.split(",") if d.strip()]
    return champs


def cle_id(story_id):
    prefixe, _, num = story_id.rpartition("-")
    return (prefixe, int(num) if num.isdigit() else 0)


def lien(chemin):
    return chemin.relative_to(BACKLOG).as_posix()


def collecter():
    stories, annexes, orphelins = {}, defaultdict(list), defaultdict(list)
    fichiers = sorted(
        p for p in BACKLOG.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
        and p.relative_to(BACKLOG).parts[0] in EPICS
    )
    for p in fichiers:
        epic = p.relative_to(BACKLOG).parts[0]
        entete = lire_entete(p) if p.suffix == ".md" else None
        if entete:
            entete["chemin"] = p
            entete["epic"] = epic
            stories[entete["id"]] = entete
            continue
        candidats = [p.name] + [d for d in p.relative_to(BACKLOG).parts[1:-1]]
        rattache = None
        for nom in candidats:
            m = re.match(r"([a-z]+-\d{3})", nom)
            if m:
                rattache = m.group(1).upper()
        if rattache:
            annexes[rattache].append(p)
        else:
            orphelins[epic].append(p)
    return stories, annexes, orphelins


def generer():
    stories, annexes, orphelins = collecter()
    par_statut = defaultdict(list)
    for s in stories.values():
        par_statut[s["statut"]].append(s)

    def termine(dep):
        return dep in stories and stories[dep]["statut"] == "terminee"

    a_faire = par_statut["proposee"] + par_statut["prete"]
    pretes = [s for s in a_faire if s["statut"] == "prete"
              or all(termine(d) for d in s["dependances"])]
    ids_pretes = {s["id"] for s in pretes}

    def tri(s):
        return (ORDRE_PRIORITE.get(s.get("priorite"), 9), cle_id(s["id"]))

    def puce(s):
        return f"[{s['id']}]({lien(s['chemin'])})"

    def ligne_annexes(s):
        docs = annexes.get(s["id"], [])
        if not docs:
            return []
        return ["  <br>Annexes : " + " · ".join(
            f"[{p.name}]({lien(p)})" for p in docs)]

    l = [
        "# État du backlog",
        "",
        "> Fichier généré par `python backlog/etat.py` à partir du champ "
        "`statut:` de chaque story. Ne pas l'éditer à la main : changer le "
        "statut dans la story, puis relancer le script.",
        "",
        "| Statut | Stories |",
        "| --- | ---: |",
    ]
    for code, libelle in STATUTS.items():
        l.append(f"| {libelle} | {len(par_statut[code])} |")
    l.append(f"| dont prêtes à démarrer | {len(pretes)} |")
    l.append(f"| Total | {len(stories)} |")
    inconnus = sorted(set(par_statut) - set(STATUTS))
    for code in inconnus:
        l.append(f"| `{code}` (statut non reconnu) | {len(par_statut[code])} |")
    l += [
        "",
        "Sommaire : [en cours](#en-cours-à-vérifier-ou-bloquées) · "
        "[prêtes](#prêtes-à-démarrer) · [terminées](#terminées) · "
        "[à faire](#à-faire-par-famille)",
        "",
        "## En cours, à vérifier ou bloquées",
        "",
    ]
    for s in sorted(par_statut["en-cours"] + par_statut["a-verifier"]
                    + par_statut["bloquee"], key=tri):
        l.append(f"- {puce(s)} — **{STATUTS[s['statut']]}** · "
                 f"{s.get('priorite', '')} · {s.get('titre', '')}")
        l += ligne_annexes(s)

    l += [
        "",
        "## Prêtes à démarrer",
        "",
        "Stories à faire dont toutes les dépendances sont terminées.",
        "",
        "| Story | Titre | Priorité | Nature |",
        "| --- | --- | --- | --- |",
    ]
    for s in sorted(pretes, key=tri):
        l.append(f"| {puce(s)} | {s.get('titre', '')} | {s.get('priorite', '')} "
                 f"| {s.get('nature', '')} |")

    l += ["", "## Terminées", ""]
    for epic, titre_epic in EPICS.items():
        faites = sorted((s for s in par_statut["terminee"] if s["epic"] == epic),
                        key=lambda s: cle_id(s["id"]))
        if not faites and not orphelins[epic]:
            continue
        l += [f"### {titre_epic}", ""]
        for s in faites:
            l.append(f"- {puce(s)} — {s.get('titre', '')}")
            l += ligne_annexes(s)
        if orphelins[epic]:
            l.append("- Autres documents : " + " · ".join(
                f"[{p.name}]({lien(p)})" for p in orphelins[epic]))
        l.append("")

    l += [
        "## À faire, par famille",
        "",
        "✅ = prête à démarrer. Sinon, la colonne indique les dépendances "
        "non terminées.",
        "",
    ]
    familles = defaultdict(list)
    for s in a_faire:
        familles[(s["epic"], cle_id(s["id"])[0])].append(s)
    for (epic, prefixe), groupe in sorted(
            familles.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        nb_pretes = sum(s["id"] in ids_pretes for s in groupe)
        nom = FAMILLES.get(prefixe, prefixe)
        l += [
            "<details>",
            f"<summary><b>{prefixe}</b> — {nom} ({EPICS[epic]}) : "
            f"{len(groupe)} à faire, {nb_pretes} prêtes</summary>",
            "",
            "| Story | Titre | Priorité | Bloquée par |",
            "| --- | --- | --- | --- |",
        ]
        for s in sorted(groupe, key=lambda s: cle_id(s["id"])):
            bloquantes = [d for d in s["dependances"] if not termine(d)]
            etat = ", ".join(bloquantes) if bloquantes else "✅"
            l.append(f"| {puce(s)} | {s.get('titre', '')} "
                     f"| {s.get('priorite', '')} | {etat} |")
        l += ["", "</details>", ""]

    abandonnees = sorted(par_statut["abandonnee"], key=lambda s: cle_id(s["id"]))
    if abandonnees:
        l += [
            "## Abandonnées",
            "",
            "Stories retirées sur décision ; chacune indique la raison.",
            "",
            "<details>",
            f"<summary><b>Abandonnées</b> : {len(abandonnees)}</summary>",
            "",
            "| Story | Titre |",
            "| --- | --- |",
        ]
        l += [f"| {puce(s)} | {s.get('titre', '')} |" for s in abandonnees]
        l += ["", "</details>", ""]

    a_ranger = [p for sid, docs in annexes.items() for p in docs
                if f"{sid.lower()}-annexes" not in p.parts]
    if a_ranger:
        l += ["## Annexes à ranger", "",
              "Ces fichiers appartiennent à une story mais ne sont pas dans "
              "son dossier `<story>-annexes/`.", ""]
        l += [f"- [{lien(p)}]({lien(p)})" for p in sorted(a_ranger)]

    return "\n".join(l).rstrip() + "\n"


def main():
    contenu = generer()
    if "--check" in sys.argv:
        actuel = SORTIE.read_text(encoding="utf-8") if SORTIE.exists() else ""
        if actuel != contenu:
            print("ETAT.md n'est pas à jour : lancer python backlog/etat.py")
            return 1
        print("ETAT.md est à jour.")
        return 0
    SORTIE.write_text(contenu, encoding="utf-8", newline="\n")
    print(f"ETAT.md régénéré ({contenu.count(chr(10))} lignes).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
