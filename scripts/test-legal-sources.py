#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Added by Judge FR/UE, 2026-10-15.
"""Offline transport/identity/credential tests. No legal reasoning assertions."""

import io
import json
import os
import tarfile
import unittest
from unittest.mock import patch
import urllib.error
import urllib.request

import legal_sources as sources


def response(text, content_type="text/html", status=200):
    return {"http_status": status, "final_url": "https://code.travail.gouv.fr/test",
            "content_type": content_type, "charset": "utf-8", "raw": text.encode()}


ARTICLE = '<h1>L2261-2</h1><p>' + 'Article content. ' * 30 + '</p><a href="https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006901780">Source</a>'


class OfficialSourcesTests(unittest.TestCase):
    @staticmethod
    def archive(identifier="LEGIARTI000006901780", xml_id=None):
        buffer = io.BytesIO()
        data = f'<ARTICLE><META><ID>{xml_id or identifier}</ID></META><BLOC_TEXTUEL><CONTENU>Texte officiel exemple</CONTENU></BLOC_TEXTUEL></ARTICLE>'.encode()
        with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
            member = tarfile.TarInfo("some/path/" + identifier + ".xml")
            member.size = len(data)
            archive.addfile(member, io.BytesIO(data))
        return {"http_status": 200, "final_url": "https://echanges.dila.gouv.fr/OPENDATA/LEGI/test.tar.gz", "content_type": "application/gzip", "charset": "utf-8", "raw": buffer.getvalue()}

    def test_dila_reads_exact_xml_without_extraction(self):
        output = sources.dila_read("https://echanges.dila.gouv.fr/OPENDATA/LEGI/test.tar.gz", "LEGIARTI000006901780", transport=lambda *a, **k: self.archive())
        self.assertEqual(output["state"], "retrieved")
        self.assertIn("Texte officiel exemple", output["text"])
        self.assertIn("xml_sha256", output["attempts"][0])
        self.assertEqual(output["documentary_status"], "non-verifie")

    def test_dila_wrong_xml_identity_is_not_a_success(self):
        output = sources.dila_read("https://echanges.dila.gouv.fr/OPENDATA/LEGI/test.tar.gz", "LEGIARTI000006901780", transport=lambda *a, **k: self.archive(xml_id="LEGIARTI000000000000"))
        self.assertEqual(output["state"], "unavailable")

    def test_dila_absence_in_delta_is_not_absence_from_corpus(self):
        output = sources.dila_read("https://echanges.dila.gouv.fr/OPENDATA/LEGI/test.tar.gz", "LEGIARTI000000000000", transport=lambda *a, **k: self.archive())
        self.assertEqual(output["attempts"][0]["state"], "not-in-archive")

    def test_dila_refuses_untrusted_archive(self):
        for url in ("https://example.com/test.tar.gz", "https://echanges.dila.gouv.fr/OPENDATA/LEGI/../secret.tar.gz"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                sources.dila_read(url, "LEGIARTI000006901780")

    def test_dila_listing_only_emits_official_archive_links(self):
        html = '<a href="LEGI_20261015.tar.gz">delta</a><a href="../secret.tar.gz">bad</a><a href="https://example.com/evil.tar.gz">bad</a>'
        output = sources.dila_list("LEGI", transport=lambda *a, **k: response(html))
        self.assertEqual(output["state"], "retrieved")
        self.assertEqual(len(output["archives"]), 1)
        self.assertIn("echanges.dila.gouv.fr", output["archives"][0]["url"])

    def test_request_rejects_oversized_body(self):
        class Headers:
            def get_content_type(self): return "text/html"
            def get_content_charset(self): return "utf-8"
        class Response(io.BytesIO):
            status = 200
            url = "https://code.travail.gouv.fr/test"
            headers = Headers()
        class Opener:
            def open(self, *a, **k): return Response(b"x" * (sources.MAX_BYTES + 1))
        with self.assertRaises(ValueError):
            sources.request("https://code.travail.gouv.fr/test", opener=Opener())

    def test_challenge_falls_back_without_certifying_law(self):
        with patch.object(sources, "request") as unused:
            def transport(url, **kwargs):
                if "legifrance" in url:
                    return response("JavaScript is disabled", status=202)
                return response(ARTICLE)
            result = sources.retrieve("travail", "L2261-2", legifrance_id="LEGIARTI000006901780", transport=transport)
            unused.assert_not_called()
        self.assertEqual(result["state"], "retrieved")
        self.assertEqual([a["state"] for a in result["attempts"]], ["blocked", "retrieved"])
        self.assertEqual(result["documentary_status"], "non-verifie")
        self.assertEqual(result["applicability"], "a-etablir")

    def test_http403_falls_back(self):
        def transport(url, **kwargs):
            if "legifrance" in url:
                raise urllib.error.HTTPError(url, 403, "Forbidden", {}, None)
            return response(ARTICLE)
        result = sources.retrieve("travail", "L2261-2", legifrance_id="LEGIARTI000006901780", transport=transport)
        self.assertEqual(result["state"], "retrieved")
        self.assertEqual(result["attempts"][0]["http_status"], 403)

    def test_wrong_article_id_is_refused(self):
        def transport(url, **kwargs):
            if "legifrance" in url:
                return response("", status=202)
            return response(ARTICLE.replace("LEGIARTI000006901780", "LEGIARTI000000000000"))
        result = sources.retrieve("travail", "L2261-2", legifrance_id="LEGIARTI000006901780", transport=transport)
        self.assertEqual(result["state"], "unavailable")
        self.assertEqual(result["attempts"][-1]["state"], "identity-mismatch")

    def test_missing_passage_is_refused(self):
        attempt, text = sources.read_public("https://code.travail.gouv.fr/test", expected=["absent"], transport=lambda *a, **k: response(ARTICLE))
        self.assertIsNone(text)
        self.assertEqual(attempt["state"], "content-mismatch")

    def test_empty200_is_not_a_success(self):
        attempt, text = sources.read_public("https://code.travail.gouv.fr/test", transport=lambda *a, **k: response(""))
        self.assertIsNone(text)
        self.assertEqual(attempt["state"], "empty")

    def test_rdf_metadata_is_not_legal_text(self):
        attempt, text = sources.read_public("https://publications.europa.eu/resource/celex/32008R0593", transport=lambda *a, **k: response(ARTICLE, "application/rdf+xml"))
        self.assertIsNone(text)
        self.assertEqual(attempt["state"], "unexpected-format")

    def test_cellar_receives_format_and_language_headers(self):
        calls = []
        def transport(url, **kwargs):
            calls.append((url, kwargs))
            return response("" if "eur-lex" in url else ARTICLE, status=202 if "eur-lex" in url else 200)
        result = sources.retrieve("eu", "32008R0593", transport=transport)
        self.assertEqual(result["state"], "retrieved")
        self.assertEqual(calls[1][1]["headers"], {"Accept": "application/xhtml+xml", "Accept-Language": "fra"})

    def test_timeout_records_failure_not_consultation(self):
        def transport(*args, **kwargs):
            raise TimeoutError("timed out")
        result = sources.retrieve("eu", "32008R0593", transport=transport)
        self.assertEqual(result["state"], "unavailable")
        self.assertTrue(all("retrieved_at" not in a for a in result["attempts"]))

    def test_untrusted_urls_and_identifiers_are_refused(self):
        for url in ("http://www.legifrance.gouv.fr/test", "https://localhost/test",
                    "https://user:secret@api.piste.gouv.fr/test", "https://api.piste.gouv.fr:8000/test"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                sources.check_url(url)
        for kind, ref in (("eu", "32008R0593?x=1"), ("travail", "../secret")):
            with self.subTest(ref=ref), self.assertRaises(ValueError):
                sources.retrieve(kind, ref)

    def test_cellar_http_redirect_upgraded_to_https(self):
        req = urllib.request.Request("https://publications.europa.eu/resource/celex/32008R0593")
        redirected = sources.OfficialRedirects().redirect_request(req, None, 302, "", {}, "http://publications.europa.eu/resource/cellar/example")
        self.assertEqual(redirected.full_url, "https://publications.europa.eu/resource/cellar/example")

    def test_authenticated_redirect_is_refused(self):
        req = urllib.request.Request("https://api.piste.gouv.fr/test", headers={"Authorization": "Bearer secret"})
        with self.assertRaises(ValueError):
            sources.OfficialRedirects().redirect_request(req, None, 302, "", {}, "https://www.legifrance.gouv.fr/")

    def test_no_credentials_no_network(self):
        with patch.dict(os.environ, {}, clear=True):
            result = sources.piste("list/ping", transport=lambda *a, **k: self.fail("network call"))
        self.assertEqual(result["state"], "needs-credentials")

    def test_oauth_credentials_stay_out_of_output(self):
        calls = []
        def transport(url, **kwargs):
            calls.append((url, kwargs))
            if "oauth" in url:
                return response(json.dumps({"access_token": "TOKEN-SECRET"}), "application/json")
            return response(json.dumps({"article": {"id": "LEGIARTI000006901780", "texte": "Document"}}), "application/json")
        with patch.dict(os.environ, {"JUDGE_PISTE_CLIENT_ID": "CLIENT-SECRET", "JUDGE_PISTE_CLIENT_SECRET": "PASSWORD-SECRET"}, clear=True):
            result = sources.piste("consult/getArticle", {"id": "LEGIARTI000006901780"}, sandbox=True, transport=transport)
        self.assertEqual(result["state"], "retrieved")
        self.assertIn("sandbox-oauth.piste.gouv.fr", calls[0][0])
        self.assertIn("sandbox-api.piste.gouv.fr", calls[1][0])
        self.assertEqual(calls[1][1]["headers"]["Authorization"], "Bearer TOKEN-SECRET")
        for secret in ("CLIENT-SECRET", "PASSWORD-SECRET", "TOKEN-SECRET"):
            self.assertNotIn(secret, json.dumps(result))

    def test_api_error_does_not_echo_response_or_secret(self):
        def transport(url, **kwargs):
            raise urllib.error.HTTPError(url, 401, "TOKEN-SECRET", {}, io.BytesIO(b"PASSWORD-SECRET"))
        with patch.dict(os.environ, {"JUDGE_PISTE_TOKEN": "TOKEN-SECRET"}, clear=True):
            result = sources.piste("list/ping", transport=transport)
        self.assertEqual(result["state"], "unavailable")
        self.assertNotIn("SECRET", json.dumps(result))

    def test_hidden_scripts_do_not_supply_expected_passage(self):
        text, _ = sources.extract_text("<script>fake law</script><p>real content</p>")
        self.assertEqual(text, "real content")


if __name__ == "__main__":
    unittest.main()
