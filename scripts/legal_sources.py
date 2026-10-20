#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Added by Judge FR/UE, 2026-10-15.
"""Read official legal publications, with bounded, traceable fallback routes.

Standard library only. Does not solve CAPTCHAs or certify legal applicability.
Prints JSON to stdout; writes no files and never prints credentials.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import io
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


MAX_BYTES = 8 * 1024 * 1024
HOSTS = {
    "www.legifrance.gouv.fr", "eur-lex.europa.eu",
    "code.travail.gouv.fr", "publications.europa.eu",
    "oauth.piste.gouv.fr", "api.piste.gouv.fr",
    "sandbox-oauth.piste.gouv.fr", "sandbox-api.piste.gouv.fr",
    "echanges.dila.gouv.fr",
}
FUNDS = ("LEGI", "KALI", "JORF", "CASS", "INCA", "CAPP", "JADE", "CONSTIT", "CNIL", "ACCO")
CODE_TRAVAIL = "LEGITEXT000006072050"
OPEN_END = "2999-01-01"
INACTIVE = {"MODIFIE_MORT_NE", "ANNULE", "DISJOINT"}  # never in force on their dates


def fund_archive(fund):
    """Complete stock (Freemium_<fund>_global_*) or daily delta (<FUND>_*) of one fund."""
    return re.compile(rf"https://echanges\.dila\.gouv\.fr/OPENDATA/{fund}/"
                      rf"(?:Freemium_{fund.lower()}_global_|{fund}_)(\d{{8}}-\d{{6}})\.tar\.gz")


LEGI_ARCHIVE = fund_archive("LEGI")
# Case-law funds readable by identifier, with the identifier family each one holds.
JURI_FUNDS = {"CASS": "JURITEXT", "INCA": "JURITEXT", "CAPP": "JURITEXT",
              "JADE": "CETATEXT", "CONSTIT": "CONSTEXT"}
JURI_MAX_MINUTES = 180
LABOUR_ARTICLE = re.compile(r"[LRD]\d+(?:-\d+)+")
# Streaming bounds for the complete LEGI stock (about 1.1 GB compressed in 2025).
STREAM_LIMITS = {"compressed": 4 * 1024 ** 3, "members": 20_000_000,
                 "scanned": 128 * 1024 ** 3, "xml": 2 * 1024 * 1024}


def now():
    return datetime.now(timezone.utc).isoformat()


def check_url(url):
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != "https" or parsed.hostname not in HOSTS
            or parsed.username or parsed.password or parsed.port not in (None, 443)):
        raise ValueError("Only the documented official HTTPS endpoints are allowed")


class OfficialRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # CELLAR currently advertises some of its own content URLs over HTTP.
        # Use the same official resource over TLS instead.
        if newurl.startswith("http://publications.europa.eu/"):
            newurl = "https://" + newurl[len("http://"):]
        check_url(newurl)
        if req.data is not None or req.has_header("Authorization"):
            raise ValueError("Authenticated/POST redirects are refused")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.links = []
        self.hidden = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.hidden.append(tag)
        if tag == "a":
            self.links.extend(v for k, v in attrs if k == "href" and v)

    def handle_endtag(self, tag):
        if self.hidden and self.hidden[-1] == tag:
            self.hidden.pop()

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.parts.append(data.strip())


def extract_text(body):
    parser = VisibleText()
    parser.feed(body)
    return "\n".join(parser.parts), parser.links


def request(url, *, headers=None, data=None, timeout=20, opener=None):
    check_url(url)
    req = urllib.request.Request(url, data=data, headers={
        "User-Agent": "Judge-FR-EU-legal-sources/1.0", **(headers or {}),
    })
    client = opener or urllib.request.build_opener(OfficialRedirects())
    with client.open(req, timeout=timeout) as response:
        raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("Response exceeds the 8 MiB limit; no partial document accepted")
        return {
            "http_status": response.status,
            "final_url": response.url,
            "content_type": response.headers.get_content_type(),
            "charset": response.headers.get_content_charset() or "utf-8",
            "raw": raw,
        }


def read_public(url, *, headers=None, expected=(), identity=None, timeout=20,
                transport=request):
    attempt = {"url": url, "attempted_at": now()}
    try:
        response = transport(url, headers=headers, timeout=timeout)
        raw = response.pop("raw")
        charset = response.pop("charset")
        attempt.update(response)
        text, links = extract_text(raw.decode(charset))
        normalized = " ".join(text.casefold().split())
        challenge = any(marker in normalized for marker in (
            "javascript is disabled", "verify that you're not a robot",
            "access denied", "incapsula incident",
        ))
        if challenge or response["http_status"] in (202, 403, 429):
            attempt.update(state="blocked", reason="Challenge/access restriction; not a legal document")
        elif response["http_status"] != 200:
            attempt.update(state="http-error", reason="Publication did not return HTTP 200")
        elif not raw or len(text.strip()) < 200:
            attempt.update(state="empty", reason="Empty or insufficient document body")
        elif response["content_type"] not in ("text/html", "application/xhtml+xml", "text/plain"):
            attempt.update(state="unexpected-format", reason="Metadata/binary response is not readable legal text")
        elif identity and not any(identity in link for link in links):
            attempt.update(state="identity-mismatch", reason="Expected Legifrance article ID missing from source links")
        elif any(" ".join(term.casefold().split()) not in normalized for term in expected):
            attempt.update(state="content-mismatch", reason="Expected article/reference or passage missing")
        else:
            attempt.update(state="retrieved", retrieved_at=now(), bytes=len(raw),
                           sha256=hashlib.sha256(raw).hexdigest())
            return attempt, text
    except urllib.error.HTTPError as exc:
        attempt.update(state="http-error", http_status=exc.code)
    except (OSError, ValueError, UnicodeError, LookupError) as exc:
        # Do not include response bodies, headers, or URLs from exception text.
        attempt.update(state="transport-error", reason=type(exc).__name__)
    return attempt, None


def retrieve(kind, reference, *, legifrance_id=None, expected=(), timeout=20,
             transport=request):
    attempts = []
    if kind == "travail":
        reference = reference.upper()
        if not re.fullmatch(r"[LRD]\d+(?:-\d+)+", reference):
            raise ValueError("Expected a Code du travail article, e.g. L2261-2")
        if legifrance_id and not re.fullmatch(r"LEGIARTI\d{12}", legifrance_id):
            raise ValueError("Invalid Legifrance article identifier")
        routes = []
        if legifrance_id:
            routes.append((f"https://www.legifrance.gouv.fr/codes/article_lc/{legifrance_id}", None, None))
        routes.append((f"https://code.travail.gouv.fr/code-du-travail/{reference.lower()}", None, legifrance_id))
        expected = (reference, *expected)
    elif kind == "eu":
        if not re.fullmatch(r"[0-9][0-9A-Z()_-]{5,60}", reference):
            raise ValueError("Expected an exact CELEX identifier, e.g. 32008R0593")
        # CELLAR answers 404 to unencoded OJ C-series parentheses, e.g. 52019XC0329(02).
        celex = urllib.parse.quote(reference, safe="")
        routes = [
            (f"https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:{celex}", None, None),
            (f"https://publications.europa.eu/resource/celex/{celex}",
             {"Accept": "application/xhtml+xml", "Accept-Language": "fra"}, None),
        ]
    else:
        raise ValueError("Unknown source family")
    for url, headers, identity in routes:
        attempt, text = read_public(url, headers=headers, identity=identity,
                                    expected=expected, timeout=timeout, transport=transport)
        attempts.append(attempt)
        if text is not None:
            return result(kind, reference, attempts, text)
    return result(kind, reference, attempts, None)


def result(kind, reference, attempts, text):
    return {
        "source_family": kind, "reference": reference,
        "state": "retrieved" if text else "unavailable",
        "documentary_status": "non-verifie", "applicability": "a-etablir",
        "version_warning": "Check identity, version, dates, amendments and context before relying; current reproduction is not a historical version.",
        "attempts": attempts, "text": text,
    }


def dila_list(fund, *, timeout=20, transport=request):
    """List the official public archives; no API subscription is used."""
    if fund not in FUNDS:
        raise ValueError("Unknown DILA fund")
    url = f"https://echanges.dila.gouv.fr/OPENDATA/{fund}/"
    attempt = {"url": url, "attempted_at": now()}
    output = result("dila-list", fund, [attempt], None)
    try:
        response = transport(url, timeout=timeout)
        if response["http_status"] != 200:
            raise ValueError("Unsuccessful archive listing")
        text = response["raw"].decode(response["charset"])
        _, links = extract_text(text)
        names = sorted({link for link in links if re.fullmatch(r"[A-Za-z0-9_.-]+\.tar\.gz", link)})
        if not names:
            raise ValueError("No archives in listing")
        attempt.update(state="retrieved", http_status=200, final_url=response["final_url"],
                       retrieved_at=now(), bytes=len(response["raw"]),
                       sha256=hashlib.sha256(response["raw"]).hexdigest())
        output.update(state="retrieved", archives=[{"name": name, "url": url + name} for name in names],
                      coverage="Archive listing only; daily deltas are not the complete corpus.")
    except urllib.error.HTTPError as exc:
        attempt.update(state="http-error", http_status=exc.code)
    except (OSError, ValueError, LookupError) as exc:
        attempt.update(state="transport-error", reason=type(exc).__name__)
    return output


def dila_read(url, identifier, *, timeout=20, transport=request):
    """Read an exact XML ID from one small public archive, without extracting files."""
    if not re.fullmatch(r"https://echanges\.dila\.gouv\.fr/OPENDATA/(?:" + "|".join(FUNDS) + r")/[A-Za-z0-9_.-]+\.tar\.gz", url):
        raise ValueError("Expected an official DILA archive URL")
    if not re.fullmatch(r"[A-Z]{4,12}\d{12}", identifier):
        raise ValueError("Expected an exact DILA document identifier")
    attempt = {"url": url, "attempted_at": now()}
    output = result("dila-xml", identifier, [attempt], None)
    try:
        response = transport(url, timeout=timeout)
        if response["http_status"] != 200:
            raise ValueError("Unsuccessful archive download")
        raw = response["raw"]
        attempt.update(http_status=200, final_url=response["final_url"], bytes=len(raw),
                       sha256=hashlib.sha256(raw).hexdigest())
        scanned = 0
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r|gz") as archive:
            for count, member in enumerate(archive, start=1):
                scanned += member.size
                if count > 100000 or scanned > 128 * 1024 * 1024:
                    raise ValueError("Archive scan limit exceeded")
                if member.name.rsplit("/", 1)[-1] != identifier + ".xml":
                    continue
                if not member.isfile() or member.size > 2 * 1024 * 1024:
                    raise ValueError("Expected a bounded regular XML member")
                with archive.extractfile(member) as source:
                    xml = source.read(2 * 1024 * 1024 + 1)
                root = ET.fromstring(xml)
                if root.findtext(".//ID") != identifier:
                    raise ValueError("XML identity mismatch")
                # Preserve XML metadata and full text, not just a search snippet.
                text = "\n".join(part.strip() for part in root.itertext() if part.strip())
                if not text:
                    raise ValueError("Empty XML document")
                attempt.update(state="retrieved", retrieved_at=now(), archive_member=member.name,
                               xml_sha256=hashlib.sha256(xml).hexdigest())
                output.update(state="retrieved", text=text, xml=xml.decode("utf-8"),
                              coverage="One identified XML document from one archive; not a complete or current corpus.")
                return output
        attempt.update(state="not-in-archive", reason="ID absent from this archive; not proof of absence from the corpus")
    except urllib.error.HTTPError as exc:
        attempt.update(state="http-error", http_status=exc.code)
    except (OSError, ValueError, tarfile.TarError, ET.ParseError) as exc:
        attempt.update(state="transport-error", reason=type(exc).__name__)
    return output


class HashingReader(io.RawIOBase):
    """Count and hash a downloaded stream; refuse it beyond the compressed limit."""

    def __init__(self, source, limit):
        self.source, self.limit = source, limit
        self.size, self.digest = 0, hashlib.sha256()

    def readable(self):
        return True

    def readinto(self, buffer):
        data = self.source.read(len(buffer))
        self.size += len(data)
        if self.size > self.limit:
            raise ValueError("Archive exceeds the streaming limit")
        self.digest.update(data)
        buffer[:len(data)] = data
        return len(data)


def open_stream(url, *, timeout=20, opener=None):
    """Open one official archive for streaming; the caller closes it."""
    check_url(url)
    req = urllib.request.Request(url, headers={"User-Agent": "Judge-FR-EU-legal-sources/1.0"})
    response = (opener or urllib.request.build_opener(OfficialRedirects())).open(req, timeout=timeout)
    if response.status != 200:
        response.close()
        raise ValueError("Archive download did not return HTTP 200")
    return response


def fund_archives(fund, *, transport=request, timeout=20):
    """Latest complete stock of a fund, then every daily delta published after it."""
    listing = dila_list(fund, timeout=timeout, transport=transport)
    pattern = fund_archive(fund)
    stamped = [(pattern.fullmatch(a["url"]), a["url"]) for a in listing.get("archives", [])]
    stamped = [(m.group(1), "Freemium" in url, url) for m, url in stamped if m]
    stocks = sorted(s for s in stamped if s[1])
    if not stocks:
        listing["attempts"][0].setdefault("reason", f"No complete {fund} stock in the official listing")
        return listing["attempts"][0], []
    stock = stocks[-1]
    deltas = sorted(s for s in stamped if not s[1] and s[0] > stock[0])
    return listing["attempts"][0], [stock[2]] + [url for _, _, url in deltas]


def legi_archives(*, transport=request, timeout=20):
    """Latest complete LEGI stock, then every daily delta published after it."""
    return fund_archives("LEGI", transport=transport, timeout=timeout)


def article_record(xml):
    """Version metadata of one Code du travail article XML, or None."""
    root = ET.fromstring(xml)
    text = root.find("CONTEXTE/TEXTE")
    if root.tag != "ARTICLE" or text is None or text.get("cid") != CODE_TRAVAIL:
        return None
    meta = root.find("META/META_SPEC/META_ARTICLE")
    record = {"id": root.findtext("META/META_COMMUN/ID", "").strip()}
    for key in ("NUM", "ETAT", "DATE_DEBUT", "DATE_FIN"):
        record[key.lower()] = (meta.findtext(key, "") if meta is not None else "").strip()
    record["num"] = record["num"].replace(" ", "").replace(".", "").upper()
    record["versions"] = [{"id": link.get("id"), "num": (link.get("num") or "").replace(" ", "").upper(),
                           "etat": link.get("etat"), "date_debut": link.get("debut"),
                           "date_fin": link.get("fin")}
                          for link in root.iterfind("VERSIONS/VERSION/LIEN_ART")]
    if not re.fullmatch(r"LEGIARTI\d{12}", record["id"]):
        raise ValueError("Article XML without a valid identifier")
    return record


def scan_legi_archive(url, wanted, store, *, timeout=20, stream=open_stream):
    """Update store {id: record} from one archive; return the attempt record."""
    attempt = {"url": url, "attempted_at": now()}
    marker = f"/{CODE_TRAVAIL}/article/"
    try:
        with stream(url, timeout=timeout) as response:
            reader = HashingReader(response, STREAM_LIMITS["compressed"])
            seen, deleted, members, scanned = set(), set(), 0, 0
            with tarfile.open(fileobj=io.BufferedReader(reader, 1024 * 1024), mode="r|gz") as archive:
                for member in archive:
                    members += 1
                    scanned += member.size
                    if members > STREAM_LIMITS["members"] or scanned > STREAM_LIMITS["scanned"]:
                        raise ValueError("Archive scan limit exceeded")
                    if members % 10000 == 0:
                        archive.members.clear()  # stream mode would keep every header in memory
                    name = member.name
                    if member.isfile() and name.endswith("liste_suppression_legi.dat"):
                        if member.size > 64 * 1024 * 1024:
                            raise ValueError("Oversized deletion list")
                        with archive.extractfile(member) as source:
                            deleted |= {line.rsplit("/", 1)[-1].strip() for line in
                                        source.read().decode("utf-8").splitlines() if marker in line}
                    elif member.isfile() and marker in name and name.endswith(".xml"):
                        if member.size > STREAM_LIMITS["xml"]:
                            raise ValueError("Oversized article XML")
                        with archive.extractfile(member) as source:
                            record = article_record(source.read())
                        if record and record["num"] in wanted:
                            record["archive"] = url.rsplit("/", 1)[-1]
                            store[record["id"]] = record
                            seen.add(record["id"])
            # A deletion applies to documents not republished by the same archive.
            removed = sorted(i for i in deleted - seen if i in store)
            for identifier in removed:
                del store[identifier]
            attempt.update(state="retrieved", http_status=200, retrieved_at=now(),
                           bytes=reader.size, sha256=reader.digest.hexdigest(),
                           members=members, matched=len(seen), deleted=removed)
    except urllib.error.HTTPError as exc:
        attempt.update(state="http-error", http_status=exc.code)
    except (OSError, ValueError, EOFError, tarfile.TarError, ET.ParseError, UnicodeError) as exc:
        attempt.update(state="transport-error", reason=type(exc).__name__)
    return attempt


def article_versions(number, store, on):
    """Version timeline of one article number as known from the scanned archives."""
    records = [r for r in store.values() if r["num"] == number]
    if not records:
        return {"article": number, "statut": "absent-des-archives-lues", "versions": []}
    versions = {}
    # Lists from the most recently published XML first; each XML then confirms its own fields.
    for record in sorted(records, key=lambda r: r["archive"]):
        for link in record["versions"]:
            if link["id"] and (not link["num"] or link["num"] == number):
                versions[link["id"]] = {**link, "source": "liste VERSIONS"}
    for record in records:
        versions[record["id"]] = {key: record[key] for key in ("id", "num", "etat", "date_debut", "date_fin")}
        versions[record["id"]].update(source="XML de la version", archive=record["archive"])
    timeline = sorted(versions.values(), key=lambda v: (v["date_debut"] or "", v["id"]))
    active = [v for v in timeline if v["etat"] not in INACTIVE]
    current = [v for v in active if v["date_debut"] and v["date_debut"] <= on < (v["date_fin"] or OPEN_END)]
    future = [v for v in active if (v["date_debut"] or "") > on or v["etat"] == "VIGUEUR_DIFF"]
    output = {"article": number, "versions": timeline, "en_vigueur": current, "versions_futures": future}
    if len(current) == 1 and current[0]["date_fin"] not in ("", OPEN_END):
        output["fin_de_vigueur"] = current[0]["date_fin"]
    if len(current) > 1:
        output["statut"] = "ambigu"
    elif not current:
        output["statut"] = "aucune-version-en-vigueur"
    elif future:
        output["statut"] = "version-future"
    elif "fin_de_vigueur" in output:
        output["statut"] = "fin-de-vigueur"
    else:
        output["statut"] = "sans-version-future-ni-fin"
    return output


def reference_articles(path):
    """Labour-code article numbers linked from a Markdown reference."""
    found = re.findall(r"code\.travail\.gouv\.fr/code-du-travail/([a-z]\d+(?:-\d+)+)",
                       Path(path).read_text(encoding="utf-8"))
    return sorted({n.upper() for n in found})


def legi_versions(numbers, *, archives=None, on=None, timeout=20, transport=request,
                  stream=open_stream, progress=None):
    """Future versions and end dates of Code du travail articles in LEGI open data."""
    wanted = sorted({n.strip().upper() for n in numbers})
    if not wanted or not all(LABOUR_ARTICLE.fullmatch(n) for n in wanted):
        raise ValueError("Expected Code du travail articles, e.g. L1221-19")
    on = on or datetime.now().date().isoformat()
    datetime.strptime(on, "%Y-%m-%d")
    attempts = []
    if archives is None:
        listing, archives = legi_archives(transport=transport, timeout=timeout)
        attempts.append(listing)
        selection = "Dernier stock LEGI complet et tous les lots quotidiens publiés après lui"
        if not archives:
            return result("legi-versions", CODE_TRAVAIL, attempts, None)
    else:
        selection = "Archives choisies par l'appelant ; couverture à justifier"
    if not archives or not all(LEGI_ARCHIVE.fullmatch(url) for url in archives):
        raise ValueError("Expected official LEGI archive URLs")
    store, read = {}, 0
    for url in archives:
        attempts.append(scan_legi_archive(url, set(wanted), store, timeout=timeout, stream=stream))
        if progress:
            progress(f"{read + 1}/{len(archives)} {url.rsplit('/', 1)[-1]} {attempts[-1]['state']}")
        if attempts[-1]["state"] != "retrieved":
            break  # a missing delta would hide later versions: no partial answer
        read += 1
    output = result("legi-versions", CODE_TRAVAIL, attempts, None)
    complete = read == len(archives)
    output.update(
        state="retrieved" if complete else "unavailable", reference_date=on, selection=selection,
        coverage=("Versions publiées dans les archives lues seulement : une modification adoptée mais "
                  "pas encore intégrée par la DILA, ou publiée après le dernier lot, n'est pas couverte."),
        version_warning="Métadonnées de version ; lire le texte et les dispositions transitoires avant usage.",
        articles=[article_versions(n, store, on) for n in wanted] if complete else [],
    )
    return output


def block_text(element):
    """Text of an XML block, keeping <br/> line breaks of DILA case-law content."""
    if element is None:
        return ""
    def flatten(node):
        parts = [node.text or ""]
        for child in node:
            parts.append("\n" if child.tag.lower() == "br" else flatten(child))
            parts.append(child.tail or "")
        return "".join(parts)
    lines = [" ".join(line.split()) for line in flatten(element).splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def decision_record(xml, identifier):
    """Identity, metadata and text of one DILA case-law XML whose ID is checked."""
    root = ET.fromstring(xml)
    if not root.tag.startswith("TEXTE_JURI_"):
        raise ValueError("Not a DILA case-law document")
    if root.findtext("META/META_COMMUN/ID", "").strip() != identifier:
        raise ValueError("XML identity mismatch")
    juri = root.find("META/META_SPEC/META_JURI")
    spec = next((child for child in root.iterfind("META/META_SPEC/*") if child.tag != "META_JURI"), None)
    def field(node, key):
        return (node.findtext(key, "") if node is not None else "").strip()
    record = {
        "id": identifier, "document": root.tag,
        "nature": field(root.find("META/META_COMMUN"), "NATURE"),
        "titre": field(juri, "TITRE"), "juridiction": field(juri, "JURIDICTION"),
        "date": field(juri, "DATE_DEC"), "numero": field(juri, "NUMERO"),
        "solution": field(juri, "SOLUTION"),
        "numeros_affaires": [n.text.strip() for n in (spec.iterfind("NUMEROS_AFFAIRES/NUMERO_AFFAIRE") if spec is not None else [])
                             if n.text and n.text.strip()],
        "ecli": field(spec, "ECLI"), "formation": field(spec, "FORMATION"),
    }
    bulletin = spec.find("PUBLI_BULL") if spec is not None else None
    record["publication"] = (f"bulletin: {bulletin.get('publie')}" if bulletin is not None
                             else field(spec, "PUBLI_RECUEIL") and f"recueil: {field(spec, 'PUBLI_RECUEIL')}")
    if field(spec, "FORM_DEC_ATT") or field(spec, "DATE_DEC_ATT"):
        record["decision_attaquee"] = {"juridiction": field(spec, "FORM_DEC_ATT"), "date": field(spec, "DATE_DEC_ATT")}
    text = "\n\n".join(filter(None, (block_text(b) for b in root.iterfind("TEXTE/BLOC_TEXTUEL/CONTENU"))))
    if not text:
        raise ValueError("Decision XML without text")
    # Headings (SCT), analyses (ANA) and related decisions (CITATION_JP) are editorial.
    summary = "\n\n".join(filter(None, [block_text(n) for n in root.iterfind("TEXTE/SOMMAIRE/*")]
                                + [block_text(n) for n in root.iterfind("TEXTE/CITATION_JP")]))
    return record, text, summary


def scan_juri_archive(url, identifier, *, timeout=20, stream=open_stream, deadline=None):
    """Find one decision ID in one archive; return (attempt, [(member, xml)], deleted)."""
    attempt = {"url": url, "attempted_at": now()}
    found, deleted = [], False
    try:
        with stream(url, timeout=timeout) as response:
            reader = HashingReader(response, STREAM_LIMITS["compressed"])
            members, scanned = 0, 0
            with tarfile.open(fileobj=io.BufferedReader(reader, 1024 * 1024), mode="r|gz") as archive:
                for member in archive:
                    members += 1
                    scanned += member.size
                    if members > STREAM_LIMITS["members"] or scanned > STREAM_LIMITS["scanned"]:
                        raise ValueError("Archive scan limit exceeded")
                    if deadline is not None and time.monotonic() > deadline:
                        raise TimeoutError("Duration limit exceeded")
                    if members % 10000 == 0:
                        archive.members.clear()  # stream mode would keep every header in memory
                    name = member.name.rsplit("/", 1)[-1]
                    if member.isfile() and re.fullmatch(r"liste_suppression_[a-z]+\.dat", name):
                        if member.size > 64 * 1024 * 1024:
                            raise ValueError("Oversized deletion list")
                        with archive.extractfile(member) as source:
                            lines = source.read().decode("utf-8").splitlines()
                        deleted |= any(line.strip().rsplit("/", 1)[-1].removesuffix(".xml") == identifier
                                       for line in lines)
                    elif name == identifier + ".xml":
                        if not member.isfile() or member.size > STREAM_LIMITS["xml"]:
                            raise ValueError("Expected a bounded regular XML member")
                        with archive.extractfile(member) as source:
                            found.append((member.name, source.read()))
            attempt.update(state="retrieved", http_status=200, retrieved_at=now(),
                           bytes=reader.size, sha256=reader.digest.hexdigest(),
                           members=members, matched=len(found), deleted=deleted)
    except urllib.error.HTTPError as exc:
        attempt.update(state="http-error", http_status=exc.code)
    except (OSError, ValueError, EOFError, tarfile.TarError, UnicodeError) as exc:
        attempt.update(state="transport-error", reason=type(exc).__name__)
    return attempt, found, deleted


def juri_read(fund, identifier, *, archives=None, timeout=20, transport=request,
              stream=open_stream, max_minutes=JURI_MAX_MINUTES, progress=None):
    """Read one decision by identifier from a case-law fund's stock and later deltas."""
    if fund not in JURI_FUNDS:
        raise ValueError("Expected a case-law fund: " + ", ".join(JURI_FUNDS))
    if not re.fullmatch(JURI_FUNDS[fund] + r"\d{12}", identifier):
        raise ValueError(f"Expected a {JURI_FUNDS[fund]} identifier for {fund}")
    if not 1 <= max_minutes <= 600:
        raise ValueError("Duration limit must be between 1 and 600 minutes")
    deadline = time.monotonic() + max_minutes * 60
    attempts = []
    if archives is None:
        listing, archives = fund_archives(fund, transport=transport, timeout=timeout)
        attempts.append(listing)
        selection = f"Dernier stock {fund} complet et tous les lots quotidiens publiés après lui"
        if not archives:
            return result("dila-juri", identifier, attempts, None)
    else:
        selection = "Archives choisies par l'appelant ; couverture à justifier"
    pattern = fund_archive(fund)
    if not archives or not all(pattern.fullmatch(url) for url in archives):
        raise ValueError(f"Expected official {fund} archive URLs")
    occurrences, current, read = [], None, 0
    for url in archives:
        attempt, found, deleted = scan_juri_archive(url, identifier, timeout=timeout,
                                                    stream=stream, deadline=deadline)
        attempts.append(attempt)
        if progress:
            progress(f"{read + 1}/{len(archives)} {url.rsplit('/', 1)[-1]} {attempt['state']}")
        if attempt["state"] != "retrieved":
            break  # a missing delta could hide a later version or a withdrawal: no partial answer
        read += 1
        name = url.rsplit("/", 1)[-1]
        for member, xml in found:
            occurrences.append({"archive": name, "archive_sha256": attempt["sha256"], "member": member,
                                "xml_sha256": hashlib.sha256(xml).hexdigest()})
        if found:
            # The most recent publication wins; distinct copies in one archive are not resolved.
            current = (name, found) if len({xml for _, xml in found}) == 1 else (name, None)
        elif deleted:
            current = None
            occurrences.append({"archive": name, "archive_sha256": attempt["sha256"], "deleted": True})
    output = result("dila-juri", identifier, attempts, None)
    output.update(
        fund=fund, selection=selection, occurrences=occurrences,
        coverage=("Décisions publiées dans les archives lues seulement ; une décision non encore "
                  "intégrée par la DILA, ou publiée après le dernier lot, n'est pas couverte."),
        version_warning="Reproduction open data ; contrôler identité, formation, date et texte avant de citer.",
    )
    if read != len(archives):
        output.update(statut="lecture-incomplete")
        return output
    if current is None:
        output.update(statut="absent-des-archives-lues")
        return output
    name, found = current
    if found is None:
        output.update(statut="copies-divergentes")
        return output
    member, xml = found[-1]
    try:
        record, text, summary = decision_record(xml, identifier)
    except (ValueError, ET.ParseError) as exc:
        output.update(statut="xml-invalide", reason=type(exc).__name__)
        return output
    record.update(archive=name, archive_member=member, xml_sha256=hashlib.sha256(xml).hexdigest(),
                  archive_sha256=next(o["archive_sha256"] for o in occurrences if o["archive"] == name))
    output.update(state="retrieved", statut="lu", decision=record, text=text, xml=xml.decode("utf-8"))
    if summary:
        output.update(sommaire=summary, sommaire_warning="Sommaire et analyses éditoriaux : ne pas les citer comme motifs.")
    return output


def piste(endpoint, body=None, *, sandbox=False, timeout=20, transport=request):
    """Read-only API calls, including POST searches. No tokens on CLI/stdout."""
    if endpoint not in ("search", "consult/getArticle", "consult/legiPart", "list/ping"):
        raise ValueError("Unsupported read-only PISTE endpoint")
    prefix = "sandbox-" if sandbox else ""
    base = f"https://{prefix}api.piste.gouv.fr/dila/legifrance/lf-engine-app/"
    token = os.environ.get("JUDGE_PISTE_TOKEN")
    client_id = os.environ.get("JUDGE_PISTE_CLIENT_ID")
    secret = os.environ.get("JUDGE_PISTE_CLIENT_SECRET")
    output = result("piste", endpoint, [], None)
    if not token and not (client_id and secret):
        output.update(state="needs-credentials", next_step="Configure PISTE credentials locally; never put them in chat or Git.")
        return output
    try:
        if not token:
            oauth_url = f"https://{prefix}oauth.piste.gouv.fr/api/oauth/token"
            auth = transport(oauth_url, headers={"Content-Type": "application/x-www-form-urlencoded"},
                             data=urllib.parse.urlencode({"grant_type": "client_credentials",
                                "client_id": client_id, "client_secret": secret, "scope": "openid"}).encode(),
                             timeout=timeout)
            if auth["http_status"] != 200:
                raise ValueError("OAuth response was not HTTP 200")
            token = json.loads(auth["raw"])["access_token"]
            if not isinstance(token, str) or not token:
                raise ValueError("Invalid access token")
        url = base + endpoint
        attempt = {"url": url, "attempted_at": now()}
        output["attempts"].append(attempt)
        response = transport(url, headers={"Authorization": f"Bearer {token}",
                             "Accept": "application/json", "Content-Type": "application/json"},
                             data=None if endpoint == "list/ping" else json.dumps(body).encode(), timeout=timeout)
        raw = response["raw"]
        attempt.update(http_status=response["http_status"], final_url=response["final_url"])
        if response["http_status"] != 200 or not raw:
            raise ValueError("Empty or unsuccessful API response")
        payload = json.loads(raw) if endpoint != "list/ping" else raw.decode("utf-8")
        # Only official document data are returned; auth responses stay in memory.
        attempt.update(state="retrieved", retrieved_at=now(), bytes=len(raw),
                       sha256=hashlib.sha256(raw).hexdigest())
        output.update(state="retrieved", payload=payload)
        return output
    except urllib.error.HTTPError as exc:
        output.update(state="unavailable", error=f"HTTP {exc.code}; check PISTE environment, subscription and quota")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        output.update(state="unavailable", error=type(exc).__name__)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=int, default=20, choices=range(1, 61), metavar="1..60")
    commands = parser.add_subparsers(dest="kind", required=True)
    labour = commands.add_parser("travail", help="French labour article; official CDTN fallback")
    labour.add_argument("reference")
    labour.add_argument("--legifrance-id")
    labour.add_argument("--expect", action="append", default=[])
    eu = commands.add_parser("eu", help="Exact CELEX document, French XHTML via CELLAR fallback")
    eu.add_argument("reference")
    eu.add_argument("--expect", action="append", default=[])
    listing = commands.add_parser("dila-list", help="List public DILA archives without an account")
    listing.add_argument("fund", choices=FUNDS)
    archive = commands.add_parser("dila-read", help="Read one exact XML ID from an official archive up to 8 MiB")
    archive.add_argument("url")
    archive.add_argument("identifier")
    juri = commands.add_parser("juri-read", help="One decision by identifier from a DILA case-law stock and later deltas")
    juri.add_argument("fund", choices=tuple(JURI_FUNDS))
    juri.add_argument("identifier", help="JURITEXT (CASS, INCA, CAPP), CETATEXT (JADE) or CONSTEXT (CONSTIT)")
    juri.add_argument("--archive", action="append", help="Official archive of the fund, in order (default: latest stock and later deltas)")
    juri.add_argument("--max-minutes", type=int, default=JURI_MAX_MINUTES, choices=range(1, 601), metavar="1..600")
    versions = commands.add_parser("legi-versions", help="Code du travail: future versions and end dates from the LEGI stock and deltas")
    versions.add_argument("articles", nargs="*", help="Article numbers, e.g. L1221-19")
    versions.add_argument("--reference", action="append", default=[], type=Path,
                          help="Markdown reference whose code.travail.gouv.fr links name the articles")
    versions.add_argument("--archive", action="append", help="Official LEGI archive, in order (default: latest stock and later deltas)")
    versions.add_argument("--date", help="Reference date AAAA-MM-JJ (default: today)")
    api = commands.add_parser("piste", help="Read-only Legifrance API; credentials from environment")
    api.add_argument("endpoint", choices=("search", "consult/getArticle", "consult/legiPart", "list/ping"))
    api.add_argument("--body", type=Path, help="UTF-8 JSON request body, containing no credentials")
    api.add_argument("--sandbox", action="store_true")
    args = parser.parse_args()
    try:
        if args.kind == "dila-list":
            output = dila_list(args.fund, timeout=args.timeout)
        elif args.kind == "dila-read":
            output = dila_read(args.url, args.identifier, timeout=args.timeout)
        elif args.kind == "juri-read":
            output = juri_read(args.fund, args.identifier, archives=args.archive, timeout=args.timeout,
                               max_minutes=args.max_minutes,
                               progress=lambda line: print(line, file=sys.stderr, flush=True))
        elif args.kind == "legi-versions":
            numbers = list(args.articles)
            for path in args.reference:
                numbers += reference_articles(path)
            output = legi_versions(numbers, archives=args.archive, on=args.date, timeout=args.timeout,
                                   progress=lambda line: print(line, file=sys.stderr, flush=True))
        elif args.kind == "piste":
            if args.endpoint != "list/ping" and not args.body:
                parser.error("--body is required for this endpoint")
            body = json.loads(args.body.read_text(encoding="utf-8")) if args.body else None
            output = piste(args.endpoint, body, sandbox=args.sandbox, timeout=args.timeout)
        else:
            output = retrieve(args.kind, args.reference, legifrance_id=getattr(args, "legifrance_id", None),
                              expected=args.expect, timeout=args.timeout)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    # ensure_ascii keeps JSON lossless through Windows PowerShell redirection.
    print(json.dumps(output, ensure_ascii=True, indent=2))
    return 0 if output["state"] == "retrieved" else 1


if __name__ == "__main__":
    sys.exit(main())
