# Added by Judge FR/UE for BASE-014, 2026-10-17.
"""Fixtures for the BASE-014 source review gate and the lot builder.

python scripts/test-source-reviews.py
"""

from datetime import date
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from source_reviews import check_plugin  # noqa: E402

TODAY = date(2026, 10, 17)
SINCE = date(2026, 10, 17)
URL_A = 'https://code.travail.gouv.fr/code-du-travail/l1221-19'
URL_B = 'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32008R0593'


def reference(review_a, review_b='2026-10-17 · inchangee · CELLAR', version='1.0.0', extra=''):
    return (f"# Repères\n\nVersion `{version}`, 15 octobre 2026.\n\n"
            "| Texte | Usage | Relecture |\n|---|---|---|\n"
            f"| [L1221-19]({URL_A}) | Essai CDI | {review_a} |\n"
            f"| [Rome I]({URL_B}) | Loi du contrat | {review_b} |\n{extra}").encode('utf-8')


def plugin(ref, notice=b'NOTICE\n'):
    return {'demo-legal/references/demo-fr.md': ref, 'demo-legal/NOTICE': notice,
            'demo-legal/references/shared/research-citation-method.md':
                f'[S1]({URL_B}) sans colonne de relecture'.encode('utf-8'),
            'demo-legal/references/isolation.md': b'Aucune source.\n'}


class SourceReviewTests(unittest.TestCase):
    def check(self, files):
        return check_plugin(files, 'demo-legal', SINCE, TODAY)

    def test_normal_all_unchanged(self):
        errors, reviews = self.check(plugin(reference('2026-10-17 · inchangee · CDTN')))
        self.assertEqual(errors, [])
        self.assertEqual([r['issue'] for r in reviews], ['inchangee', 'inchangee'])
        self.assertEqual(reviews[0]['date'], '2026-10-17')

    def test_review_before_lot_preparation_is_refused(self):
        errors, _ = self.check(plugin(reference('2026-10-15 · inchangee · CDTN')))
        self.assertTrue(any('non relue pour ce lot' in e for e in errors), errors)

    def test_future_or_invalid_review_is_refused(self):
        errors, _ = self.check(plugin(reference('2026-10-18 · inchangee · CDTN')))
        self.assertTrue(any('future' in e for e in errors), errors)
        errors, _ = self.check(plugin(reference('17/10/2026 · inchangee · CDTN')))
        self.assertTrue(any('date de relecture invalide' in e for e in errors), errors)

    def test_incomplete_or_unknown_issue_is_refused(self):
        errors, _ = self.check(plugin(reference('2026-10-17 · inchangee')))
        self.assertTrue(any('incomplète' in e for e in errors), errors)
        errors, _ = self.check(plugin(reference('2026-10-17 · ok · CDTN')))
        self.assertTrue(any('issue inconnue' in e for e in errors), errors)

    def test_source_outside_review_table_is_refused(self):
        extra = '\nPiste : [arrêt](https://www.legifrance.gouv.fr/juri/id/JURITEXT000007046365/).\n'
        errors, _ = self.check(plugin(reference('2026-10-17 · inchangee · CDTN', extra=extra)))
        self.assertEqual(len(errors), 1)
        self.assertIn('source sans relecture', errors[0])

    def test_modified_article_requires_reference_update_and_notice(self):
        not_integrated = reference('2026-10-17 · modifiee · CDTN · version du 01/01/2027')
        errors, _ = self.check(plugin(not_integrated))
        self.assertTrue(any('sans mise à jour de la référence' in e for e in errors), errors)
        stale_version = reference('2026-10-17 · modifiee · CDTN · intégrée 1.1.0')
        errors, _ = self.check(plugin(stale_version))
        self.assertTrue(any('sans mise à jour de la référence' in e for e in errors), errors)
        updated = reference('2026-10-17 · modifiee · CDTN · intégrée 1.1.0', version='1.1.0')
        errors, _ = self.check(plugin(updated))
        self.assertTrue(any('sans entrée NOTICE' in e for e in errors), errors)
        errors, reviews = self.check(plugin(updated, b'BASE-014: demo-fr.md 1.1.0 updated\n'))
        self.assertEqual(errors, [])
        self.assertEqual(reviews[0]['issue'], 'modifiee')

    def test_alternative_official_route_is_recorded(self):
        review = '2026-10-17 · inchangee · CDTN après Légifrance HTTP 403'
        errors, reviews = self.check(plugin(reference(review)))
        self.assertEqual(errors, [])
        self.assertEqual(reviews[0]['voie'], 'CDTN après Légifrance HTTP 403')

    def test_inaccessible_source_needs_recorded_reserve(self):
        errors, _ = self.check(plugin(reference('2026-10-17 · inaccessible · Légifrance')))
        self.assertTrue(any('sans réserve' in e for e in errors), errors)
        errors, _ = self.check(plugin(reference('2026-10-17 · inaccessible · Légifrance · réserve maintenue')))
        self.assertEqual(errors, [])


class BuildLotTests(unittest.TestCase):
    """Builds employment-legal from the working tree into a temporary directory."""

    def build(self, since, out):
        notes = SCRIPTS.parent / 'backlog/04-livraison/liv-001-annexes/liv-001-notes-version.md'
        return subprocess.run([sys.executable, str(SCRIPTS / 'build-lot.py'), '--lot', 'lot-test',
                               '--plugin', 'employment-legal', '--notes', str(notes),
                               '--relecture-depuis', since, '--out', out],
                              capture_output=True, text=True, encoding='utf-8')

    def test_lot_built_with_review_dates_in_inventory(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = self.build('2026-10-17', tmp)
            self.assertEqual(result.returncode, 0, result.stderr)
            inventory = json.loads((Path(tmp) / 'lot-test/lot-inventory.json').read_text(encoding='utf-8'))
            reviews = inventory['source_reviews']['reviews']
            self.assertEqual(inventory['source_reviews']['since'], '2026-10-17')
            self.assertTrue(reviews)
            self.assertTrue(all(r['date'] >= '2026-10-17' and r['issue'] for r in reviews))
            self.assertIn('employment-legal/references/hiring-review-fr.md', {r['reference'] for r in reviews})

    def test_lot_refused_when_sources_not_reread_for_this_lot(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = self.build('2999-01-01', tmp)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('not reviewed for this lot', result.stderr)
            self.assertFalse((Path(tmp) / 'lot-test').exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
