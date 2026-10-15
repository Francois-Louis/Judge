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
FUNDS = ("LEGI", "KALI", "JORF", "CASS", "INCA", "JADE", "CONSTIT", "CNIL", "ACCO")


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
        routes = [
            (f"https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:{reference}", None, None),
            (f"https://publications.europa.eu/resource/celex/{reference}",
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
