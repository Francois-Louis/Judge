#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Added by Judge FR/UE, 2026-10-17 (BASE-015).
"""Probe public case-law sources over plain HTTPS, without account or API key.

Records, for each fixed target, HTTP status, final URL, content type, size,
SHA-256 and whether the expected identifiers appear in the visible text.
A probe is transport evidence only: it never verifies a decision's content,
its version or its applicability. Prints JSON to stdout; writes no files.

    python -X utf8 backlog/00-fondations/base-015-annexes/base-015-sonde.py
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from legal_sources import extract_text  # noqa: E402

MAX_BYTES = 8 * 1024 * 1024
UA = "Judge-FR-EU-base015-probe/1.0"
XHTML = {"Accept": "application/xhtml+xml", "Accept-Language": "fra"}

# (identifiant, source, URL, en-têtes, marqueurs attendus dans le texte visible)
TARGETS = [
    ("legifrance-juri-decision", "Légifrance JURI",
     "https://www.legifrance.gouv.fr/juri/id/JURITEXT000049053200", {},
     ["22-20.926", "PAR CES MOTIFS"]),
    ("legifrance-juri-recherche", "Légifrance JURI",
     "https://www.legifrance.gouv.fr/search/juri?tab_selection=juri&searchField=ALL"
     "&query=clause+de+non-concurrence+contrepartie+financi%C3%A8re&page=1&init=true",
     {}, ["JURITEXT"]),
    ("legifrance-ceta-decision", "Légifrance CETAT",
     "https://www.legifrance.gouv.fr/ceta/id/CETATEXT000048734416", {}, ["489206"]),
    ("cassation-decision", "Cour de cassation",
     "https://www.courdecassation.fr/decision/6079b1ab9ba5988459c53061", {},
     ["00-45.135"]),
    ("cassation-judilibre-recherche", "Cour de cassation",
     "https://www.courdecassation.fr/recherche-judilibre?search_api_fulltext="
     "clause+de+non-concurrence&op=Rechercher", {}, ["non-concurrence"]),
    ("conseil-etat-arianeweb", "Conseil d'État",
     "https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2024-05-23/494320", {},
     ["494320"]),
    ("conseil-constitutionnel-decision", "Conseil constitutionnel",
     "https://www.conseil-constitutionnel.fr/decision/2010/201014_22QPC.htm", {},
     ["2010-14/22 QPC"]),
    ("curia-document", "CJUE (CURIA)",
     "https://curia.europa.eu/juris/document/document.jsf?docid=169195&doclang=FR",
     {}, ["Schrems"]),
    ("eurlex-celex-arret", "CJUE (EUR-Lex)",
     "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62014CJ0362", {},
     ["Schrems"]),
    ("cellar-celex-arret", "CJUE (CELLAR)",
     "https://publications.europa.eu/resource/celex/62014CJ0362", XHTML,
     ["Schrems"]),
    ("hudoc-page", "Cour EDH (HUDOC)",
     "https://hudoc.echr.coe.int/fre?i=001-57619", {}, ["Soering"]),
    ("hudoc-conversion", "Cour EDH (HUDOC)",
     "https://hudoc.echr.coe.int/app/conversion/docx/html/body?library=ECHR&id=001-57619",
     {}, ["Soering", "14038/88"]),
    ("hudoc-requete", "Cour EDH (HUDOC)",
     "https://hudoc.echr.coe.int/app/query/results?query=contentsitename%3AECHR%20AND%20"
     "itemid%3A%22001-57619%22&select=itemid,docname,ecli,appno,kpdate&sort=&start=0"
     "&length=1", {}, ["Soering"]),
    ("dila-cass", "Données ouvertes DILA",
     "https://echanges.dila.gouv.fr/OPENDATA/CASS/", {}, [".tar.gz"]),
    ("dila-capp", "Données ouvertes DILA",
     "https://echanges.dila.gouv.fr/OPENDATA/CAPP/", {}, [".tar.gz"]),
    ("dila-inca", "Données ouvertes DILA",
     "https://echanges.dila.gouv.fr/OPENDATA/INCA/", {}, [".tar.gz"]),
    ("dila-jade", "Données ouvertes DILA",
     "https://echanges.dila.gouv.fr/OPENDATA/JADE/", {}, [".tar.gz"]),
    ("dila-constit", "Données ouvertes DILA",
     "https://echanges.dila.gouv.fr/OPENDATA/CONSTIT/", {}, [".tar.gz"]),
    ("conseil-etat-opendata", "Données ouvertes Conseil d'État",
     "https://opendata.conseil-etat.fr/", {}, ["CE"]),
]


def now():
    return datetime.now(timezone.utc).isoformat()


def probe(ident, source, url, headers, markers, timeout=25):
    entry = {"id": ident, "source": source, "url": url, "attempted_at": now()}
    req = urllib.request.Request(url, headers={"User-Agent": UA, **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(MAX_BYTES + 1)
            entry.update(http_status=resp.status, final_url=resp.geturl(),
                         content_type=resp.headers.get("Content-Type", ""))
    except urllib.error.HTTPError as exc:
        body = exc.read(MAX_BYTES + 1) if exc.fp else b""
        entry.update(http_status=exc.code, final_url=exc.geturl(),
                     content_type=exc.headers.get("Content-Type", "") if exc.headers else "")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        entry.update(state="erreur-reseau", reason=type(exc).__name__ + ": " + str(exc)[:200])
        return entry
    entry["bytes"] = len(body)
    entry["sha256"] = hashlib.sha256(body).hexdigest()
    ctype = entry["content_type"]
    text = body.decode("utf-8", "replace")
    if not ("json" in ctype or ("xml" in ctype and "html" not in ctype)):
        text, _links = extract_text(text)
    entry["visible_chars"] = len(text)
    entry["markers"] = {m: (m in text) for m in markers}
    found = all(entry["markers"].values())
    if entry["http_status"] != 200:
        entry["state"] = "refus-ou-erreur-http"
    elif found:
        entry["state"] = "marqueurs-presents"
    elif entry["visible_chars"] < 500:
        entry["state"] = "corps-vide-ou-javascript"
    else:
        entry["state"] = "marqueurs-absents"
    return entry


def main():
    results = [probe(*target) for target in TARGETS]
    print(json.dumps({
        "story": "BASE-015",
        "outil": "urllib (voie Bash/Python d'une session)",
        "user_agent": UA,
        "portee": "Transport seulement : un marqueur présent ne vaut pas lecture "
                  "de la décision ni applicabilité.",
        "resultats": results,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
