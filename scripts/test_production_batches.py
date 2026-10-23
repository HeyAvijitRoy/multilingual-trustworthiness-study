"""Production selection, prespecified review sampling and evidence protection tests."""
from copy import deepcopy
import json
from pathlib import Path
import random
import tempfile
import unittest
from unittest.mock import patch

import prepare_production_batches as production
from validate_pilot_annotations import read_jsonl
from validate_prompt_corpus import load_rows


class ProductionBatchTests(unittest.TestCase):
    def setUp(self):
        self.plan = production.build()

    def test_exact_disjoint_reserved_membership_and_size(self):
        queue = json.loads((production.ANN / 'SCALING_QUEUE.json').read_text())
        expansion = json.loads((production.ANN / 'EXPANSION_BATCHES.json').read_text())
        excluded = {r['task_id'] for r in queue['tasks'] if r['next_step'] == 'gold-frozen'}
        excluded |= {r['task_id'] for b in expansion['batches'] for r in b['tasks']}
        ids = [r['task_id'] for b in self.plan['batches'] for r in b['tasks']]
        self.assertEqual(len(ids), 343)
        self.assertEqual(len(set(ids)), 343)
        self.assertFalse(set(ids) & excluded)
        self.assertEqual(set(ids) | excluded, {r['task_id'] for r in queue['tasks']})
        self.assertEqual(sorted(b['task_count'] for b in self.plan['batches']), [24]*7 + [25]*7)
        for batch in self.plan['batches']:
            self.assertEqual(len(batch['domain_counts']), 5)
            self.assertEqual(set(batch['difficulty_counts']), {'easy', 'medium', 'hard'})

    def fixture(self, root):
        target = root / 'data/annotations'
        target.mkdir(parents=True)
        for name in ('SCALING_QUEUE.json', 'EXPANSION_BATCHES.json'):
            (target/name).write_bytes((production.ANN/name).read_bytes())
        return target

    def test_assignment_ignores_source_order(self):
        with tempfile.TemporaryDirectory() as dirname:
            root = Path(dirname)
            target = self.fixture(root)
            path = target/'SCALING_QUEUE.json'
            queue = json.loads(path.read_text())
            random.Random(240319).shuffle(queue['tasks'])
            path.write_text(json.dumps(queue))
            expansion_path = target/'EXPANSION_BATCHES.json'
            expansion = json.loads(expansion_path.read_text())
            expansion['batches'].reverse()
            for batch in expansion['batches']:
                batch['tasks'].reverse()
            expansion_path.write_text(json.dumps(expansion))
            self.assertEqual(production.build(root)['batches'], self.plan['batches'])

    def test_duplicate_or_missing_reserved_task_fails(self):
        for mode in ('duplicate', 'missing'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as dirname:
                root = Path(dirname)
                target = self.fixture(root)
                path = target/'SCALING_QUEUE.json'
                queue = json.loads(path.read_text())
                item = next(r for r in queue['tasks'] if r['task_id'] == 'CYBER002')
                if mode == 'duplicate':
                    queue['tasks'].append(item)
                else:
                    queue['tasks'].remove(item)
                path.write_text(json.dumps(queue))
                with self.assertRaisesRegex(ValueError, '343 unique'):
                    production.build(root)

    def draft_fixture(self):
        records = [r for p in sorted((production.ANN/'production/P01').glob('*.jsonl')) for r in read_jsonl(p)]
        prompts = {r['task_id']: r for r in load_rows()}
        ambiguity = json.loads((production.PACKETS/'P01_ambiguities.json').read_text())
        return records, prompts, ambiguity

    def test_sample_is_order_invariant_and_at_least_twenty_percent_per_stratum(self):
        records, _, _ = self.draft_fixture()
        sample, strata = production.ordinary_sample(records, 'P01')
        shuffled = deepcopy(records)
        random.Random(71).shuffle(shuffled)
        for row in shuffled:
            row['rius'].reverse()
        self.assertEqual(production.ordinary_sample(shuffled, 'P01'), (sample, strata))
        self.assertEqual(len(sample), sum(s['selected_units'] for s in strata))
        for stratum in strata:
            self.assertGreaterEqual(stratum['selected_units'] * 5, stratum['ordinary_units'])
            self.assertEqual(stratum['selected_units'], (stratum['ordinary_units'] + 4)//5)
        self.assertTrue(all(u['criticality'] == 'supporting' for r in records for u in r['rius'] if (r['task_id'],u['id']) in sample))

    def test_packet_covers_critical_ambiguity_and_sample_and_stays_pending(self):
        records, prompts, ambiguity = self.draft_fixture()
        manifest, text = production.packet(self.plan['batches'][0], records, prompts, ambiguity)
        rows = {(r['task_id'],r['riu_id']):r for r in manifest['unit_checklist']}
        for record in records:
            for unit in record['rius']:
                if unit['criticality'] == 'critical':
                    self.assertIn('all-critical', rows[(record['task_id'],unit['id'])]['review_reasons'])
            for issue in ambiguity[record['task_id']]:
                for unit_id in issue['riu_ids']:
                    self.assertIn('identified-ambiguity-or-boundary', rows[(record['task_id'],unit_id)]['review_reasons'])
            for language in ('en','bn','bn_cs'):
                self.assertIn(prompts[record['task_id']]['prompt_'+language], text)
        self.assertEqual(manifest['human_reviewed_count'], 0)
        self.assertEqual(manifest['approved_count'], 0)
        self.assertTrue(all(r['reviewer'] is None and r['decision'] is None and r['independent_review_status']=='pending' for r in rows.values()))

    def test_status_promotion_and_missing_boundary_inputs_rejected(self):
        records, prompts, ambiguity = self.draft_fixture()
        records[0]['status'] = 'method-audited'
        with self.assertRaisesRegex(ValueError, 'pending draft'):
            production.packet(self.plan['batches'][0], records, prompts, ambiguity)
        records[0]['status'] = 'draft'
        ambiguity.pop(records[0]['task_id'])
        with self.assertRaisesRegex(ValueError, 'explicit ambiguity'):
            production.packet(self.plan['batches'][0], records, prompts, ambiguity)

    def test_check_is_read_only_and_generated_packets_never_overwrite_review_edits(self):
        with tempfile.TemporaryDirectory() as dirname:
            root = Path(dirname)
            path = root/'packet.json'
            with patch.object(production, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'missing/stale'):
                    production.update(path, 'new', True)
                self.assertFalse(path.exists())
                production.update(path, 'new', False)
                production.update(path, 'new', True)
                path.write_text('reviewer: actual human decision')
                with self.assertRaisesRegex(ValueError, 'refusing to overwrite'):
                    production.update(path, 'new', False)
                with self.assertRaisesRegex(ValueError, 'missing/stale'):
                    production.update(path, 'new', True)
                self.assertEqual(path.read_text(), 'reviewer: actual human decision')


if __name__ == '__main__':
    unittest.main()
