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

    def test_celex_parentheses_are_percent_encoded(self):
        calls = []
        def transport(url, **kwargs):
            calls.append(url)
            return response("", status=202)
        result = sources.retrieve("eu", "52019XC0329(02)", transport=transport)
        self.assertEqual(calls, [
            "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:52019XC0329%2802%29",
            "https://publications.europa.eu/resource/celex/52019XC0329%2802%29",
        ])
        self.assertEqual(result["reference"], "52019XC0329(02)")

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

    STOCK = "https://echanges.dila.gouv.fr/OPENDATA/LEGI/Freemium_legi_global_20250713-140000.tar.gz"
    DELTA = "https://echanges.dila.gouv.fr/OPENDATA/LEGI/LEGI_20260601-210000.tar.gz"

    @staticmethod
    def legi_article(identifier, num, etat, debut, fin, versions=(), cid="LEGITEXT000006072050"):
        links = "".join(f'<VERSION etat="{e}"><LIEN_ART debut="{d}" etat="{e}" fin="{f}" id="{i}" num="{num}" origine="LEGI"/></VERSION>'
                        for i, e, d, f in versions)
        return (f'<ARTICLE><META><META_COMMUN><ID>{identifier}</ID></META_COMMUN><META_SPEC><META_ARTICLE>'
                f'<NUM>{num}</NUM><ETAT>{etat}</ETAT><DATE_DEBUT>{debut}</DATE_DEBUT><DATE_FIN>{fin}</DATE_FIN>'
                f'</META_ARTICLE></META_SPEC></META><CONTEXTE><TEXTE cid="{cid}"/></CONTEXTE>'
                f'<VERSIONS>{links}</VERSIONS></ARTICLE>').encode()

    @staticmethod
    def legi_archive(members):
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
            for name, data in members:
                member = tarfile.TarInfo(name)
                member.size = len(data)
                archive.addfile(member, io.BytesIO(data))
        return buffer.getvalue()

    @staticmethod
    def path(identifier, text="LEGITEXT000006072050"):
        return f"x/legi/global/code_et_TNC_en_vigueur/code_en_vigueur/LEGI/TEXT/{text}/article/LEGI/ARTI/{identifier}.xml"

    def streams(self, archives):
        def stream(url, **kwargs):
            if archives[url] is None:
                raise TimeoutError("timed out")
            return io.BytesIO(archives[url])
        return stream

    def test_legi_delta_reveals_future_version_and_end_of_current(self):
        old = ("LEGIARTI000000000001", "VIGUEUR", "2008-05-01", "2999-01-01")
        stock = self.legi_archive([(self.path(old[0]), self.legi_article(old[0], "L1221-19", *old[1:], versions=[old]))])
        new = ("LEGIARTI000000000002", "VIGUEUR_DIFF", "2027-01-01", "2999-01-01")
        ended = ("LEGIARTI000000000001", "VIGUEUR", "2008-05-01", "2027-01-01")
        delta = self.legi_archive([
            (self.path(new[0]), self.legi_article(new[0], "L1221-19", *new[1:], versions=[ended, new])),
            (self.path(old[0]), self.legi_article(old[0], "L1221-19", *ended[1:], versions=[ended, new])),
        ])
        output = sources.legi_versions(["l1221-19"], archives=[self.STOCK, self.DELTA], on="2026-10-17",
                                       stream=self.streams({self.STOCK: stock, self.DELTA: delta}))
        self.assertEqual(output["state"], "retrieved")
        article = output["articles"][0]
        self.assertEqual(article["statut"], "version-future")
        self.assertEqual(article["fin_de_vigueur"], "2027-01-01")
        self.assertEqual([v["id"] for v in article["versions_futures"]], [new[0]])
        self.assertEqual(output["attempts"][1]["matched"], 2)
        self.assertEqual(len(output["attempts"][1]["sha256"]), 64)
        self.assertEqual((output["documentary_status"], output["applicability"]), ("non-verifie", "a-etablir"))

    def test_legi_scheduled_abrogation_is_an_end_date(self):
        row = ("LEGIARTI000000000003", "ABROGE_DIFF", "2016-08-10", "2027-03-01")
        archive = self.legi_archive([(self.path(row[0]), self.legi_article(row[0], "L3121-27", *row[1:], versions=[row]))])
        output = sources.legi_versions(["L3121-27"], archives=[self.STOCK], on="2026-10-17",
                                       stream=self.streams({self.STOCK: archive}))
        self.assertEqual(output["articles"][0]["statut"], "fin-de-vigueur")
        self.assertEqual(output["articles"][0]["fin_de_vigueur"], "2027-03-01")

    def test_legi_same_number_in_another_code_is_ignored(self):
        row = ("LEGIARTI000000000004", "VIGUEUR_DIFF", "2027-01-01", "2999-01-01")
        current = ("LEGIARTI000000000005", "VIGUEUR", "2008-05-01", "2999-01-01")
        archive = self.legi_archive([
            (self.path(row[0], "LEGITEXT000006073189"), self.legi_article(row[0], "L1221-1", *row[1:], cid="LEGITEXT000006073189")),
            (self.path(row[0] + "9"), self.legi_article(row[0], "L1221-1", *row[1:], cid="LEGITEXT000006073189")),
            (self.path(current[0]), self.legi_article(current[0], "L1221-1", *current[1:], versions=[current])),
        ])
        output = sources.legi_versions(["L1221-1"], archives=[self.STOCK], on="2026-10-17",
                                       stream=self.streams({self.STOCK: archive}))
        self.assertEqual(output["articles"][0]["statut"], "sans-version-future-ni-fin")
        self.assertEqual([v["id"] for v in output["articles"][0]["versions"]], [current[0]])

    def test_legi_deletion_list_removes_withdrawn_version(self):
        row = ("LEGIARTI000000000006", "VIGUEUR_DIFF", "2027-01-01", "2999-01-01")
        stock = self.legi_archive([(self.path(row[0]), self.legi_article(row[0], "L8221-6", *row[1:]))])
        delta = self.legi_archive([("x/liste_suppression_legi.dat",
                                    b"legi/global/code_et_TNC_en_vigueur/code_en_vigueur/LEGI/TEXT/LEGITEXT000006072050/article/LEGI/ARTI/" + row[0].encode() + b"\n")])
        output = sources.legi_versions(["L8221-6"], archives=[self.STOCK, self.DELTA], on="2026-10-17",
                                       stream=self.streams({self.STOCK: stock, self.DELTA: delta}))
        self.assertEqual(output["attempts"][1]["deleted"], [row[0]])
        self.assertEqual(output["articles"][0]["statut"], "absent-des-archives-lues")

    def test_legi_missing_delta_gives_no_partial_answer(self):
        row = ("LEGIARTI000000000007", "VIGUEUR", "2008-05-01", "2999-01-01")
        stock = self.legi_archive([(self.path(row[0]), self.legi_article(row[0], "L1221-1", *row[1:]))])
        output = sources.legi_versions(["L1221-1"], archives=[self.STOCK, self.DELTA], on="2026-10-17",
                                       stream=self.streams({self.STOCK: stock, self.DELTA: None}))
        self.assertEqual(output["state"], "unavailable")
        self.assertEqual(output["articles"], [])
        self.assertEqual(output["attempts"][-1]["state"], "transport-error")

    def test_legi_selects_latest_stock_and_later_deltas(self):
        html = "".join(f'<a href="{n}">{n}</a>' for n in (
            "Freemium_legi_global_20240101-000000.tar.gz", "Freemium_legi_global_20250713-140000.tar.gz",
            "LEGI_20250712-211706.tar.gz", "LEGI_20261016-213852.tar.gz", "LEGI_20250713-205013.tar.gz"))
        _, archives = sources.legi_archives(transport=lambda *a, **k: response(html))
        self.assertEqual([a.rsplit("/", 1)[-1] for a in archives], [
            "Freemium_legi_global_20250713-140000.tar.gz", "LEGI_20250713-205013.tar.gz", "LEGI_20261016-213852.tar.gz"])
        output = sources.legi_versions(["L1221-1"], transport=lambda *a, **k: response("<a href='LEGI_20261016-213852.tar.gz'>x</a>"),
                                       stream=lambda *a, **k: self.fail("network call"))
        self.assertEqual(output["state"], "unavailable")

    def test_legi_refuses_untrusted_archives_and_articles(self):
        for archives, numbers in (([self.STOCK.replace("LEGI/", "KALI/")], ["L1221-1"]),
                                  (["https://example.com/LEGI_20261016-213852.tar.gz"], ["L1221-1"]),
                                  ([self.STOCK], ["../secret"]), ([self.STOCK], [])):
            with self.subTest(archives=archives, numbers=numbers), self.assertRaises(ValueError):
                sources.legi_versions(numbers, archives=archives, stream=lambda *a, **k: self.fail("network call"))

    def test_legi_stream_limit_is_enforced(self):
        reader = sources.HashingReader(io.BytesIO(b"x" * 10), 5)
        with self.assertRaises(ValueError):
            reader.read(10)

    def test_reference_articles_reads_labour_code_links(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "employment-legal",
                            "references", "hiring-review-fr.md")
        numbers = sources.reference_articles(path)
        self.assertIn("L1221-19", numbers)
        self.assertTrue(all(sources.LABOUR_ARTICLE.fullmatch(n) for n in numbers))

    CASS_STOCK = "https://echanges.dila.gouv.fr/OPENDATA/CASS/Freemium_cass_global_20250713-140000.tar.gz"
    CASS_DELTA = "https://echanges.dila.gouv.fr/OPENDATA/CASS/CASS_20260930-215413.tar.gz"
    DECISION = "JURITEXT000007046365"

    @staticmethod
    def decision(identifier, solution="Cassation partielle", text="Attendu que la clause<br/>est nulle ;", summary=""):
        sommaire = (f'<SOMMAIRE><SCT ID="8A" TYPE="PRINCIPAL">CONTRAT DE TRAVAIL</SCT><ANA ID="8A">{summary}</ANA>'
                    f'</SOMMAIRE><CITATION_JP><CONTENU>A RAPPROCHER : Soc., 1998-04-07</CONTENU></CITATION_JP>') if summary else ""
        return (f'<TEXTE_JURI_JUDI><META><META_COMMUN><ID>{identifier}</ID><NATURE>ARRET</NATURE></META_COMMUN>'
                f'<META_SPEC><META_JURI><TITRE>Cour de cassation, chambre sociale, 10 juillet 2002, 00-45.135</TITRE>'
                f'<DATE_DEC>2002-07-10</DATE_DEC><JURIDICTION>Cour de cassation</JURIDICTION><NUMERO>50202723</NUMERO>'
                f'<SOLUTION>{solution}</SOLUTION></META_JURI><META_JURI_JUDI><NUMEROS_AFFAIRES>'
                f'<NUMERO_AFFAIRE>00-45135</NUMERO_AFFAIRE></NUMEROS_AFFAIRES><PUBLI_BULL publie="oui"/>'
                f'<FORMATION>CHAMBRE_SOCIALE</FORMATION><FORM_DEC_ATT>Cour d\'appel de Reims</FORM_DEC_ATT>'
                f'<DATE_DEC_ATT>2000-06-28</DATE_DEC_ATT><ECLI>ECLI:FR:CCASS:2002:SO02723</ECLI></META_JURI_JUDI>'
                f'</META_SPEC></META><TEXTE><BLOC_TEXTUEL><CONTENU>{text}</CONTENU></BLOC_TEXTUEL>{sommaire}</TEXTE>'
                f'</TEXTE_JURI_JUDI>').encode()

    @staticmethod
    def juri_path(identifier, root="x/juri/cass/global/sociale"):
        return f"{root}/JURI/TEXT/00/00/07/04/63/{identifier}.xml"

    def juri(self, archives, **kwargs):
        return sources.juri_read("CASS", self.DECISION, archives=list(archives),
                                 stream=self.streams(archives), **kwargs)

    def test_juri_reads_latest_publication_with_identity_text_and_hashes(self):
        stock = self.legi_archive([(self.juri_path(self.DECISION), self.decision(self.DECISION, solution="Rejet"))])
        delta = self.legi_archive([(self.juri_path(self.DECISION), self.decision(self.DECISION, summary="Analyse éditoriale"))])
        output = self.juri({self.CASS_STOCK: stock, self.CASS_DELTA: delta})
        self.assertEqual((output["state"], output["statut"]), ("retrieved", "lu"))
        decision = output["decision"]
        self.assertEqual(decision["solution"], "Cassation partielle")
        self.assertEqual(decision["archive"], self.CASS_DELTA.rsplit("/", 1)[-1])
        self.assertEqual((decision["date"], decision["ecli"], decision["numeros_affaires"]),
                         ("2002-07-10", "ECLI:FR:CCASS:2002:SO02723", ["00-45135"]))
        self.assertEqual(decision["decision_attaquee"], {"juridiction": "Cour d'appel de Reims", "date": "2000-06-28"})
        self.assertEqual(decision["publication"], "bulletin: oui")
        self.assertEqual(output["text"], "Attendu que la clause\nest nulle ;")
        self.assertEqual(output["sommaire"], "CONTRAT DE TRAVAIL\n\nAnalyse éditoriale\n\nA RAPPROCHER : Soc., 1998-04-07")
        self.assertNotIn("Analyse", output["text"])
        self.assertNotIn("RAPPROCHER", output["text"])
        self.assertEqual(len(output["occurrences"]), 2)
        self.assertEqual(len(decision["xml_sha256"]), 64)
        self.assertEqual(len(decision["archive_sha256"]), 64)
        self.assertEqual((output["documentary_status"], output["applicability"]), ("non-verifie", "a-etablir"))

    def test_juri_absent_identifier_is_not_a_success(self):
        stock = self.legi_archive([(self.juri_path("JURITEXT000000000001"), self.decision("JURITEXT000000000001"))])
        output = self.juri({self.CASS_STOCK: stock})
        self.assertEqual((output["state"], output["statut"]), ("unavailable", "absent-des-archives-lues"))
        self.assertNotIn("decision", output)

    def test_juri_failed_archive_gives_no_partial_answer(self):
        stock = self.legi_archive([(self.juri_path(self.DECISION), self.decision(self.DECISION))])
        output = self.juri({self.CASS_STOCK: stock, self.CASS_DELTA: None})
        self.assertEqual((output["state"], output["statut"]), ("unavailable", "lecture-incomplete"))
        self.assertNotIn("decision", output)
        self.assertIsNone(output["text"])
        self.assertEqual(output["attempts"][-1]["state"], "transport-error")

    def test_juri_member_and_duration_limits_are_not_successes(self):
        stock = self.legi_archive([("x/a.xml", b"<a/>"), (self.juri_path(self.DECISION), self.decision(self.DECISION))])
        with patch.dict(sources.STREAM_LIMITS, {"members": 1}):
            output = self.juri({self.CASS_STOCK: stock})
        self.assertEqual((output["state"], output["statut"]), ("unavailable", "lecture-incomplete"))
        clock = iter([0, 0, 120, 120, 120])
        with patch.object(sources.time, "monotonic", lambda: next(clock)):
            output = self.juri({self.CASS_STOCK: stock}, max_minutes=1)
        self.assertEqual((output["state"], output["statut"]), ("unavailable", "lecture-incomplete"))
        self.assertEqual(output["attempts"][0]["reason"], "TimeoutError")

    def test_juri_deletion_list_withdraws_decision(self):
        stock = self.legi_archive([(self.juri_path(self.DECISION), self.decision(self.DECISION))])
        delta = self.legi_archive([("x/liste_suppression_cass.dat",
                                    ("juri/cass/global/sociale/JURI/TEXT/00/00/07/04/63/" + self.DECISION + "\n").encode())])
        output = self.juri({self.CASS_STOCK: stock, self.CASS_DELTA: delta})
        self.assertEqual(output["statut"], "absent-des-archives-lues")
        self.assertTrue(output["attempts"][-1]["deleted"])

    def test_juri_divergent_copies_and_wrong_identity_are_refused(self):
        stock = self.legi_archive([(self.juri_path(self.DECISION), self.decision(self.DECISION)),
                                   (self.juri_path(self.DECISION, "x/juri/cass/global"), self.decision(self.DECISION, solution="Rejet"))])
        self.assertEqual(self.juri({self.CASS_STOCK: stock})["statut"], "copies-divergentes")
        stock = self.legi_archive([(self.juri_path(self.DECISION), self.decision("JURITEXT000000000001"))])
        output = self.juri({self.CASS_STOCK: stock})
        self.assertEqual((output["state"], output["statut"]), ("unavailable", "xml-invalide"))

    def test_juri_refuses_wrong_fund_identifier_and_archives(self):
        for fund, identifier, archives in (("LEGI", self.DECISION, [self.CASS_STOCK]),
                                           ("JADE", self.DECISION, None),
                                           ("CASS", "JURITEXT00000704636", [self.CASS_STOCK]),
                                           ("CASS", self.DECISION, [self.CASS_STOCK.replace("CASS/", "CAPP/")]),
                                           ("CASS", self.DECISION, ["https://example.com/CASS_20260930-215413.tar.gz"]),
                                           ("CASS", self.DECISION, [])):
            with self.subTest(fund=fund, identifier=identifier, archives=archives), self.assertRaises(ValueError):
                sources.juri_read(fund, identifier, archives=archives, transport=lambda *a, **k: self.fail("network call"),
                                  stream=lambda *a, **k: self.fail("network call"))

    def test_juri_selects_fund_stock_and_later_deltas(self):
        html = "".join(f'<a href="{n}">{n}</a>' for n in (
            "Freemium_capp_global_20250713-140000.tar.gz", "CAPP_20250707-210159.tar.gz",
            "CAPP_20261008-213853.tar.gz", "Freemium_cass_global_20250713-140000.tar.gz"))
        self.assertIn("CAPP", sources.FUNDS)
        _, archives = sources.fund_archives("CAPP", transport=lambda *a, **k: response(html))
        self.assertEqual([a.rsplit("/", 1)[-1] for a in archives],
                         ["Freemium_capp_global_20250713-140000.tar.gz", "CAPP_20261008-213853.tar.gz"])

    def test_hidden_scripts_do_not_supply_expected_passage(self):
        text, _ = sources.extract_text("<script>fake law</script><p>real content</p>")
        self.assertEqual(text, "real content")


if __name__ == "__main__":
    unittest.main()
